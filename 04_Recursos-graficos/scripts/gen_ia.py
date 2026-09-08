# -*- coding: utf-8 -*-
"""Siluetas de equipos con IA (gpt-image-2) + VERIFICACION.  PERFIL y PLANTA.

Enfoque HIBRIDO:
  - IA para la FORMA -> imagen->imagen con el DIBUJO REAL del catalogo.
    Nunca texto->imagen (ahi inventa geometria).
  - Nuestro pipeline para la VERDAD:
      * PERFIL: aspecto contra las COTAS OFICIALES del catalogo.
      * PLANTA: no hay largo/alto oficial util (la maquina va articulada),
        asi que se contrasta contra NUESTRA silueta ya validada.
  - Si no pasa, REGENERA (hasta N intentos) y si ninguno pasa lo DECLARA.

Uso:   python gen_ia.py jumbo            (las dos vistas)
       python gen_ia.py jumbo perfil     (solo una)
"""
import csv, sys, base64, math
from pathlib import Path
import numpy as np
from scipy import ndimage as ndi
from PIL import Image
from config import cliente, MODELO_IMAGEN

# El taller de cada equipo (catalogo + referencias + crudos) vive en ../equipos/.
# La silueta APROBADA se promueve luego a ../siluetas/ con el nombre normalizado
# que registra 05_Base-de-datos/imagenes.csv.
RAIZ = Path(__file__).resolve().parent.parent

# El catalogo de equipos ya NO vive en el codigo: esta en
# 05_Base-de-datos/figuras.csv. Dar de alta un equipo o una figura es AGREGAR UNA FILA,
# no editar este script. Asi el script queda comun a las tres carreras y
# no se toca nunca.
CATALOGO = Path(__file__).resolve().parents[2] / "05_Base-de-datos" / "figuras.csv"


def cargar_equipos() -> dict:
    equipos: dict = {}
    with open(CATALOGO, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            eq = equipos.setdefault(r["equipo"], dict(carpeta=r["carpeta"],
                                                      carrera=r["carrera"], vistas={}))
            eq["vistas"][r["vista"]] = dict(
                referencia=r["referencia"], control=float(r["control"] or 0),
                tam=r["tam"] or None, origen=r["origen"],
                vista=r["descripcion_vista"], partes=r["partes"],
                solo_calidad=bool(r["solo_calidad"]),
                # columnas nuevas: una FIGURA de fuente no es un equipo, pero pasa
                # por el mismo bucle. Lo unico que cambia es COMO se aisla lo que
                # se mide y donde se guarda.
                tipo=r.get("tipo") or "equipo",
                salida=r.get("salida", ""), medida=r.get("medida") or "saturacion",
                pt_minimo=float(r["pt_minimo"]) if r.get("pt_minimo") else 0.0,
                rotulos=r.get("rotulos", ""), pie=r.get("pie", ""))
    return equipos


EQUIPOS = cargar_equipos()

PROMPT_CALIDAD = """Mejora la calidad de esta imagen.

Que sea una copia fiel: no cambies nada del dibujo.
"""

PROMPT = """Redibuja esta imagen fiel al original.
{vista}
El dibujo mide {ratio} veces mas de ancho que de alto: respeta esa proporcion.

Hazla achurada y a color: cada tipo de componente con su propio color y su
propio achurado.

Elimina las lineas de medida, las lineas que forman los angulos, los valores
de los angulos y las medidas horizontales y verticales. Elimina tambien los
logotipos y el texto que no se haya pedido conservar.

Dibuja sobre fondo blanco.
"""


# Lienzo estandar de salida: 16:9, la proporcion de la diapositiva
LIENZO = (1920, 1080)
MARGEN = 0.06


def a_lienzo(img: Image.Image) -> Image.Image:
    """Centra el equipo en un lienzo 16:9 transparente, con margen uniforme."""
    LW, LH = LIENZO
    disp_w, disp_h = LW * (1 - 2 * MARGEN), LH * (1 - 2 * MARGEN)
    k = min(disp_w / img.width, disp_h / img.height)
    nw, nh = max(int(img.width * k), 1), max(int(img.height * k), 1)
    escalada = img.resize((nw, nh), Image.LANCZOS)
    lienzo = Image.new("RGBA", (LW, LH), (0, 0, 0, 0))
    lienzo.paste(escalada, ((LW - nw) // 2, (LH - nh) // 2), escalada)
    return lienzo


def solo_equipo(png: Path):
    """Separa el EQUIPO (colores pastel, saturados) de la ROCA (gris/pardo desaturado).
    Permite medir la proporcion del equipo aunque la imagen tenga piso y paredes."""
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    sat = a.max(2) - a.min(2)
    m = sat > 28                      # solo lo con color -> el equipo
    m = ndi.binary_closing(m, np.ones((7, 7)))
    m = ndi.binary_opening(m, np.ones((5, 5)))
    lb, nn = ndi.label(m, structure=np.ones((3, 3)))
    if nn:
        sz = ndi.sum(np.ones_like(lb), lb, index=range(1, nn + 1))
        mayor = sz.max()
        # OJO: no basta el componente mayor. Partes largas y delgadas del equipo
        # (el boom o la viga de avance extendidos) quedan como componentes SUELTOS
        # y al ignorarlos se mide solo el cuerpo -> proporcion equivocada.
        keep = [i + 1 for i in range(nn) if sz[i] >= mayor * 0.02]
        m = ndi.binary_fill_holes(np.isin(lb, keep))
    return m


def solo_cuerpo(png: Path):
    """Lo mismo que solo_equipo() pero para una FIGURA de fuente.

    Misma idea y misma razon: se mide el OBJETO, no la escena. En un equipo el
    objeto va en pastel y la roca en gris; en estas figuras el cuerpo mineralizado
    va coloreado y la roca en gris arena. La firma es identica, asi que el criterio
    tambien: lo que tiene saturacion es el cuerpo.

    Esto es lo que evita las seis veces que hoy medi tinta que no era la figura
    —el marco del escaneo, el marco del panel, el achurado del grabado, los
    rotulos, las flechas de cota y hasta el punto decimal de un numero—.
    """
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    sat = a.max(2) - a.min(2)
    m = sat > 40
    m = ndi.binary_closing(m, np.ones((9, 9)))
    m = ndi.binary_opening(m, np.ones((5, 5)))
    lb, nn = ndi.label(m, structure=np.ones((3, 3)))
    if nn:
        sz = ndi.sum(np.ones_like(lb), lb, index=range(1, nn + 1))
        keep = [i + 1 for i in range(nn) if sz[i] >= sz.max() * 0.02]
        m = ndi.binary_fill_holes(np.isin(lb, keep))
    return m


def angulo_de(m):
    """Inclinacion dominante del cuerpo, por PCA. Sirve cuando lo que hay que
    conservar no es una proporcion sino un angulo — la veta, por ejemplo."""
    ys, xs = np.where(m)
    if ys.size < 200:
        return None
    x = xs - xs.mean(); y = (-ys) - (-ys).mean()
    vals, vecs = np.linalg.eigh(np.cov(np.vstack([x, y])))
    d = vecs[:, int(np.argmax(vals))]
    return float(np.degrees(np.arctan2(d[1], d[0])) % 180)


def glifo_pt(png: Path, ancho_hueco_in=6):
    """Altura de PALABRA en pt proyectados (§11). Solo aplica a lo que lleva
    texto: los paneles van sin rotulos y se saltan este control."""
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    W = a.shape[1]
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    tinta = ((R > 130) & (G < 120) & (B < 120)) | (a.mean(2) < 130)
    lb, n = ndi.label(ndi.binary_dilation(tinta, np.ones((3, 15))), np.ones((3, 3)))
    altos = sorted(h for sl in ndi.find_objects(lb)
                   for h, w in [(sl[0].stop - sl[0].start, sl[1].stop - sl[1].start)]
                   if 16 <= h <= 130 and 0.4 <= w / h <= 12)
    if not altos:
        return None
    px = altos[len(altos) // 2]
    return dict(px=px, pt=ancho_hueco_in * px / W * 72)


def a_mascara(png: Path, estilo="silueta"):
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    if estilo in ("pastel", "color"):
        # los pasteles son claros: sirve "todo lo que no es blanco puro",
        # sea por oscuridad o por tener color (saturacion).
        sat = a.max(2) - a.min(2)
        m = (a.mean(2) < 246) | (sat > 12)
        k = 5
    else:
        m = a.mean(2) < 210
        # en achurado el interior queda blanco entre lineas: cerrar mas.
        k = 15 if estilo == "achurado" else 3
    return ndi.binary_fill_holes(ndi.binary_closing(m, np.ones((k, k))))


def medir(m):
    if m.sum() == 0:
        return None
    ys, xs = np.where(m)
    _, n = ndi.label(m, structure=np.ones((3, 3)))
    w, h = int(xs.max() - xs.min()), int(ys.max() - ys.min())
    return dict(asp=w / max(h, 1), piezas=n, w=w, h=h, area=int(m.sum()))


def revisar(d, control, tol=0.12):
    f = []
    if d is None:
        return False, ["imagen vacia"]
    err = abs(d["asp"] - control) / control
    if err > tol:
        f.append(f"aspecto {d['asp']:.2f} vs {control:.2f} (desvio {err:.0%})")
    if d["piezas"] > 3:
        f.append(f"{d['piezas']} piezas sueltas")
    return (not f), f


def una_vista(eq, vista, intentos=3, calidad="medium", estilo="color"):
    cfg = EQUIPOS[eq]; v = cfg["vistas"][vista]
    carp = RAIZ / cfg["carpeta"]; ref = carp / v["referencia"]
    if not ref.exists():
        print(f"  [{vista}] falta la referencia {ref.name}"); return None
    tam = v.get("tam") or ("1536x1024" if vista == "perfil" else "1024x1024")
    print(f"\n=== {eq} / {vista} ===")
    print(f"  referencia: {ref.name}   control aspecto={v['control']:.2f} ({v['origen']})")
    prompt = (PROMPT_CALIDAD if v.get("solo_calidad")
              else PROMPT.format(vista=v["vista"], ratio=f"{v['control']:.2f}"))
    suf = ""
    cli = cliente(); mejor = None
    for i in range(1, intentos + 1):
        try:
            with open(ref, "rb") as fh:
                r = cli.images.edit(model=MODELO_IMAGEN, image=[fh], prompt=prompt,
                                    size=tam, quality=calidad)
        except Exception as e:
            print("  ERROR API:", type(e).__name__, str(e)[:300]); return None
        crudo = carp / f"_{eq}_ia_{vista}{suf}_crudo.png"
        crudo.write_bytes(base64.b64decode(r.data[0].b64_json))
        m = solo_equipo(crudo)
        d = medir(m); ok, fallas = revisar(d, v["control"])
        print(f"  intento {i}: aspecto={d['asp']:.2f} piezas={d['piezas']} {d['w']}x{d['h']}  "
              + ("OK" if ok else "FALLA -> " + "; ".join(fallas)))
        salida = carp / f"{eq}_ia_{vista}{suf}.png"
        ys, xs = np.where(np.ones_like(m))   # la escena completa: roca + equipo
        if False:
            pass
        else:
            # ACHURADO / PASTEL: se conserva el dibujo tal cual (lineas o colores);
            # solo se vuelve transparente el fondo blanco.  La mascara 'm' se usa
            # unicamente para medir la proporcion.
            rgb = np.array(Image.open(crudo).convert("RGB"))
            tinta = np.ones(rgb.shape[:2], bool)   # escena completa (roca + equipo)
            out = np.zeros((*tinta.shape, 4), np.uint8)
            out[..., :3] = rgb
            out[..., 3] = np.where(tinta, 255, 0)
        rec = Image.fromarray(out[ys.min():ys.max()+1, xs.min():xs.max()+1], "RGBA")
        # CORRECCION DE PROPORCION: la IA deriva mas cuanto mas transforma el estilo.
        # Como el aspecto correcto lo sabemos (cotas oficiales / nuestra silueta),
        # se reescala para que quede dimensionalmente fiel.  La IA pone el estilo,
        # nosotros ponemos la proporcion.
        # El aspecto objetivo es el del EQUIPO, no el de la escena: se estira toda
        # la imagen por el factor que corrige al equipo (la galeria acompana).
        aw, ah = rec.size
        factor = v["control"] / d["asp"]
        # LIMITE DE SEGURIDAD: estirar mas de un 30% deforma visiblemente el dibujo.
        # Si el modelo se fue tan lejos, ese intento se descarta en vez de "arreglarlo".
        if not (0.77 <= factor <= 1.30):
            print(f"     descartado: requeriria estirar x{factor:.2f} (deformaria el dibujo)")
            continue
        if abs(factor - 1) > 0.03:
            rec = rec.resize((max(int(round(aw*factor)), 1), ah), Image.LANCZOS)
            print(f"     equipo {d['asp']:.2f} -> {v['control']:.2f}  (escena {aw}x{ah} -> "
                  f"{rec.size[0]}x{rec.size[1]}, factor {factor:.3f})")
        a_lienzo(rec).save(salida)          # lienzo 16:9 uniforme para todo el set
        if mejor is None or abs(d["asp"] - v["control"]) < mejor[1]:
            mejor = (salida, abs(d["asp"] - v["control"]), i, d["asp"])
        if ok:
            print(f"  -> APROBADO ({salida.name})"); return salida
    if mejor is None:
        print("  -> NINGUN intento fue utilizable: todos exigian una deformacion mayor al 30%.")
        print("     No se entrega imagen. Revisar la referencia o el prompt.")
        return None
    print(f"  -> ningun intento salio proporcionado del modelo "
          f"(mejor: intento {mejor[2]}, aspecto crudo {mejor[3]:.2f}).")
    print(f"     Se entrega el mejor CON LA PROPORCION CORREGIDA a {v['control']:.2f}.")
    return mejor[0]



# ══════════════════════════════════════════════════════════════════════════
#  FIGURAS DE FUENTE
#
#  Una figura de tesis o un grabado antiguo no es un equipo, pero el problema
#  es el mismo y por eso pasa por el mismo bucle: la fuente es correcta y es
#  ilegible al proyectar, el modelo la mejora, y hay que comprobar que no la
#  deformo. Cambian tres cosas, y solo tres:
#
#    · como se AISLA lo que se mide  -> solo_cuerpo() en vez de solo_equipo()
#    · que se COMPARA                -> aspecto o angulo, segun la columna
#    · donde se GUARDA               -> tal cual, sin lienzo 16:9 ni transparencia
#
#  Lo demas —el control que sale de la fuente, la tolerancia del 12 %, la
#  correccion de proporcion, el limite de estirado del 30 % y declarar cuando
#  ninguno pasa— es exactamente el metodo de los equipos, que ya estaba
#  resuelto. (Erick, 2026-09-02: «revisa como se hacen las imagenes de los
#  equipos». Tenia razon: yo estaba reescribiendo lo que ya existia.)
# ══════════════════════════════════════════════════════════════════════════

PROMPT_FIGURA = """Colorea esta figura como material academico.

{vista}

Conserva el dibujo tal cual: no cambies ninguna linea, ninguna forma ni ninguna
inclinacion, y no anadas ni quites nada. Si no llena el marco, deja blanco antes
que deformarlo.

Para colorearla: {partes}.

Quita la marca de agua y las letras sueltas del autor. Fondo blanco, sin marco.
"""


def una_figura(nombre, vista, intentos=3, calidad="high"):
    cfg = EQUIPOS[nombre]; v = cfg["vistas"][vista]
    ref = RAIZ / cfg["carpeta"] / v["referencia"]
    sal = RAIZ / v["salida"]
    if not ref.exists():
        print("  falta la referencia:", ref); return None

    por_angulo = v["medida"] == "angulo"
    print("\n=== %s ===" % nombre)
    print("  referencia: %s   control=%.2f (%s)" % (ref.name, v["control"], v["origen"]))
    print("  se mide el CUERPO por saturacion, no la escena")

    prompt = PROMPT_FIGURA.format(vista=v["vista"], partes=v["partes"])
    cli = cliente(); mejor = None

    for i in range(1, intentos + 1):
        with open(ref, "rb") as fh:
            r = cli.images.edit(model=MODELO_IMAGEN, image=[fh], prompt=prompt,
                                size=v["tam"] or "1536x1024", quality=calidad)
        crudo = sal.parent / ("_%s_crudo.png" % nombre)
        crudo.parent.mkdir(parents=True, exist_ok=True)
        crudo.write_bytes(base64.b64decode(r.data[0].b64_json))

        m = solo_cuerpo(crudo)
        d = medir(m)
        if d is None:
            print("  intento %d: no se encontro cuerpo con color" % i); continue
        val = angulo_de(m) if por_angulo else d["asp"]
        err = abs(val - v["control"]) / v["control"]
        print("  intento %d: %s=%.2f  (control %.2f, desvio %.0f%%)"
              % (i, "angulo" if por_angulo else "aspecto", val, v["control"], err * 100))

        im = Image.open(crudo).convert("RGB")
        # CORRECCION DE PROPORCION, igual que en los equipos: el aspecto correcto
        # lo sabemos, asi que se reescala en vez de tirar el intento. Para un
        # angulo el factor sale de la tangente: estirar en x lo tumba.
        factor = (math.tan(math.radians(v["control"])) / math.tan(math.radians(val))
                  if por_angulo else v["control"] / val)
        if not (0.77 <= factor <= 1.30):
            print("     descartado: exigiria estirar x%.2f" % factor); continue
        if abs(factor - 1) > 0.03:
            im = im.resize((max(int(round(im.width * factor)), 1), im.height), Image.LANCZOS)
            print("     corregido x%.3f -> %dx%d" % (factor, im.width, im.height))

        if mejor is None or err < mejor[1]:
            mejor = (im.copy(), err, i, val)
        if err <= 0.12:
            break

    if mejor is None:
        print("  -> NINGUN intento fue utilizable. No se entrega imagen."); return None
    im, err, i, val = mejor
    im.save(sal)
    print("  -> %s  (intento %d, desvio %.1f%%)"
          % (sal.relative_to(RAIZ.parent), i, err * 100))
    if v["pt_minimo"]:
        g = glifo_pt(sal)
        print("     letra %s" % ("%d px = %.1f pt" % (g["px"], g["pt"]) if g else "no medible"))
        if g and g["pt"] < v["pt_minimo"]:
            print("     NO LLEGA al piso de %.0f pt (§11): sobra contenido" % v["pt_minimo"])
    return sal


# ── montaje de varios paneles en una imagen de lamina ─────────────────────
W_LAMINA, CUERPO_PX, NOTA_PX = 1500, 52, 42
MARINO, GRIS = (13, 38, 50), (108, 122, 130)


def _tipo(px, bold=False):
    from PIL import ImageFont
    return ImageFont.truetype(r"C:\Windows\Fonts\%s" % ("arialbd.ttf" if bold else "arial.ttf"), px)


def _sin_aire(im, margen=12):
    a = np.array(im.convert("L")); t = np.where(a < 235)
    if t[0].size == 0:
        return im
    return im.crop((max(t[1].min() - margen, 0), max(t[0].min() - margen, 0),
                    min(t[1].max() + margen, im.width), min(t[0].max() + margen, im.height)))


def componer(nombre):
    """Monta paneles ya verificados en una imagen de lamina.

    Componer es maquetacion; inventar la geometria de un panel seria lo
    prohibido. Si falta un panel esto se detiene: no rellena el hueco."""
    from PIL import ImageDraw
    v = next(iter(EQUIPOS[nombre]["vistas"].values()))
    ids = [x.strip() for x in v["referencia"].split(";")]
    rot = [x.split("|") for x in v["rotulos"].split(";")]
    rutas = [RAIZ / next(iter(EQUIPOS[i]["vistas"].values()))["salida"] for i in ids]
    faltan = [i for i, r in zip(ids, rutas) if not r.exists()]
    if faltan:
        print("Faltan paneles: %s" % ", ".join(faltan))
        for i in faltan:
            print("    python gen_ia.py %s" % i)
        return 1

    ims = [_sin_aire(Image.open(r).convert("RGB")) for r in rutas]
    hueco = int(W_LAMINA / len(ims)); alto = int(hueco * 0.82)
    # se igualan por ALTURA: por ancho, la veta quedaria enana junto al manto
    ims = [im.resize((min(int(im.width * alto / im.height), hueco - 30), alto), Image.LANCZOS)
           for im in ims]
    y_rot = 40 + alto + 40
    H = y_rot + CUERPO_PX + 18 + NOTA_PX * 3 + 70
    lienzo = Image.new("RGB", (W_LAMINA, H), (255, 255, 255))
    d = ImageDraw.Draw(lienzo)
    for i, (im, (titulo, pie)) in enumerate(zip(ims, rot)):
        cx = int(hueco * (i + 0.5))
        lienzo.paste(im, (cx - im.width // 2, 40 + (alto - im.height) // 2))
        d.text((cx, y_rot), titulo, font=_tipo(CUERPO_PX, True), fill=MARINO, anchor="ma")
        d.multiline_text((cx, y_rot + CUERPO_PX + 16), pie.replace("\\n", "\n"),
                         font=_tipo(NOTA_PX), fill=MARINO, anchor="ma", align="center", spacing=10)
    d.text((W_LAMINA // 2, H - 52), v["pie"], font=_tipo(NOTA_PX - 6), fill=GRIS, anchor="ma")
    sal = RAIZ / v["salida"]
    sal.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(sal)
    print("ENTREGABLE  %s   %dx%d" % (sal.relative_to(RAIZ.parent), lienzo.width, lienzo.height))
    print("  rotulo %d px -> %.1f pt proyectados" % (CUERPO_PX, 6 * CUERPO_PX / W_LAMINA * 72))
    return 0


if __name__ == "__main__":
    eq = sys.argv[1] if len(sys.argv) > 1 else "jumbo"
    if eq not in EQUIPOS:
        sys.exit("no esta en figuras.csv: " + eq)
    primera = next(iter(EQUIPOS[eq]["vistas"].values()))
    if primera["tipo"] in ("panel", "figura", "composicion"):
        v0 = next(iter(EQUIPOS[eq]["vistas"]))
        sys.exit(componer(eq) if primera["tipo"] == "composicion"
                 else (0 if una_figura(eq, v0) else 1))
    vistas = [sys.argv[2]] if len(sys.argv) > 2 else list(EQUIPOS[eq]["vistas"])
    estilo = "color"
    print(f"Modelo: {MODELO_IMAGEN}   estilo: {estilo}")
    for v in vistas:
        # la PLANTA es mas inestable (maquina articulada + geometria de la labor):
        # el descarte por seguridad rechaza varios intentos, asi que se dan mas.
        una_vista(eq, v, estilo=estilo, intentos=5 if v == "planta" else 3)
