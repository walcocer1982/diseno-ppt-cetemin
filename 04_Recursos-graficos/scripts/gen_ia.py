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
import csv, sys, base64
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
# 05_Base-de-datos/equipos.csv. Dar de alta un equipo es AGREGAR UNA FILA,
# no editar este script. Asi el script queda comun a las tres carreras y
# no se toca nunca.
CATALOGO = Path(__file__).resolve().parents[2] / "05_Base-de-datos" / "equipos.csv"


def cargar_equipos() -> dict:
    equipos: dict = {}
    with open(CATALOGO, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            eq = equipos.setdefault(r["equipo"], dict(carpeta=r["carpeta"],
                                                      carrera=r["carrera"], vistas={}))
            eq["vistas"][r["vista"]] = dict(
                referencia=r["referencia"], control=float(r["control"]),
                tam=r["tam"] or None, origen=r["origen"],
                vista=r["descripcion_vista"], partes=r["partes"],
                solo_calidad=bool(r["solo_calidad"]))
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


if __name__ == "__main__":
    eq = sys.argv[1] if len(sys.argv) > 1 else "jumbo"
    vistas = [sys.argv[2]] if len(sys.argv) > 2 else list(EQUIPOS[eq]["vistas"])
    estilo = "color"
    print(f"Modelo: {MODELO_IMAGEN}   estilo: {estilo}")
    for v in vistas:
        # la PLANTA es mas inestable (maquina articulada + geometria de la labor):
        # el descarte por seguridad rechaza varios intentos, asi que se dan mas.
        una_vista(eq, v, estilo=estilo, intentos=5 if v == "planta" else 3)
