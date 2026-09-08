# -*- coding: utf-8 -*-
"""Figuras de lámina a partir de una figura REAL. Híbrido, verificación y montaje.

QUÉ RESUELVE
    Un plano de tesis o un grabado antiguo es la fuente correcta —trae cotas o
    geometría de algo que existe— y es **ilegible al proyectar**: sale a 300 px
    con rótulos de 8 px, o sea 2 pt en la lámina. Ampliarlo no arregla nada:
    crecen los dos a la vez (§11).

    Redibujarlo a mano tampoco: ahí se inventa la geometría, que es lo que el
    §10 prohíbe. El camino es el HÍBRIDO del CLAUDE.md, el del jumbo Boomer S1:

        fuente → referencia.png  →  gpt-image-2 images.edit  →  verificación

    Nunca texto→imagen. La geometría la pone la fuente; el modelo pone el color,
    el estilo y el tamaño de letra.

QUÉ CAMBIÓ, Y POR QUÉ (Erick, 2026-09-02)
    Erick hizo en ChatGPT con dos líneas lo que aquí costaba veintitantas
    llamadas, y le salió mejor. Tres lecciones, las tres metidas en este
    archivo:

    1 · EL PROMPT CORTO GANA. El largo peleaba contra la fuente —«conviértelo
        en vector plano, quita el achurado, rellena en colores planos»— y el
        resultado perdía los estratos del grabado. El corto se apoya en ella:
        «coloréala, es para material académico». La fidelidad la da tener la
        figura delante, no la longitud de la instrucción.

    2 · EL ENCARGO VIVE EN UNA TABLA, NO EN EL CÓDIGO. Antes era un diccionario
        aquí dentro, que es justo lo que la convención de `equipos.csv` prohíbe:
        «dar de alta un equipo es AGREGAR UNA FILA, no editar este script».
        Ahora sale de `05_Base-de-datos/figuras.csv`.

    3 · UN INTENTO POR DEFECTO. El bucle de tres existe para cazar deformación
        contra una cota oficial. Cuando lo único que se pide es colorear un
        grabado, no compra nada y triplica el gasto. La columna `intentos` lo
        decide por figura.

    Y el montaje de varios paneles dejó de ser un script suelto: es una fila
    más, de tipo `composicion`.

QUÉ SE MIDE, Y CONTRA QUÉ
    El control sale de la fuente, nunca a ojo, y se mide con la MISMA función
    que después juzga al entregable —esa lección costó tres repeticiones del
    error 19 del §10—.

        contorno · aspecto de la figura mayor que no es roja (las cotas son
                   rojas y caen fuera; moverlas cambiaría el número sin que la
                   figura esté mal)
        angulo   · inclinación dominante de la tinta, por PCA. Sirve cuando lo
                   que hay que conservar no es una proporción sino un ángulo

    Y para lo que se proyecta, un segundo check: la letra por encima de 14 pt
    (§11). Los paneles no lo pasan porque van SIN texto: el rótulo lo pone el
    montaje, fuera del dibujo, donde matplotlib lo escribe exacto.

Uso:  python gen_figura_fuente.py forma-veta
      python gen_figura_fuente.py formas-cuerpo          (monta la composición)
      python gen_figura_fuente.py --lista
"""
from __future__ import annotations

import argparse
import base64
import csv
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

from config import cliente, MODELO_IMAGEN

RAIZ = Path(__file__).resolve().parents[1]
TABLA = RAIZ.parent / "05_Base-de-datos" / "figuras.csv"

TOLERANCIA = 0.12     # §10: 12 % de desvío
PT_MINIMO = 14.0      # §11: por debajo, sobra contenido
W_LAMINA = 1500       # §11: de aquí salen los pt proyectados
CUERPO, NOTA = 52, 42
MARINO, GRIS, BLANCO = (13, 38, 50), (108, 122, 130), (255, 255, 255)
FUENTES = r"C:\Windows\Fonts"


# ── el encargo, que vive en la tabla ───────────────────────────────────────
def cargar() -> dict:
    with open(TABLA, encoding="utf-8-sig", newline="") as fh:
        return {r["figura_id"]: r for r in csv.DictReader(fh)}


FIGURAS = cargar()


# ── el prompt: corto, y apoyado en la fuente ───────────────────────────────
PROMPT = """Colorea esta figura como material académico.

Conserva el dibujo tal cual: no cambies ninguna línea, ninguna forma ni ninguna
inclinación, y no añadas ni quites nada. Si no llena el marco, deja blanco antes
que deformarlo.

{encargo}

Quita la marca de agua y las letras sueltas del autor. Fondo blanco.
"""


# ── medición ───────────────────────────────────────────────────────────────
def contorno(png: Path):
    """Aspecto de la figura mayor que no es roja. El rojo son las cotas, y las
    cotas caen fuera: moverlas cambiaría el número sin que la figura esté mal."""
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    m = (a.mean(2) < 170) & ~((R > 150) & (G < 110) & (B < 110))
    m = ndi.binary_fill_holes(ndi.binary_closing(m, np.ones((9, 9))))
    lb, n = ndi.label(m, np.ones((3, 3)))
    if not n:
        return None
    sz = ndi.sum(np.ones_like(lb), lb, index=range(1, n + 1))
    ys, xs = np.where(lb == int(np.argmax(sz)) + 1)
    w, h = int(xs.max() - xs.min()), int(ys.max() - ys.min())
    return dict(w=w, h=h, valor=w / max(h, 1))


def angulo(png: Path):
    """Inclinación dominante de la tinta, por PCA.

    EL MARGEN NO ES UN DETALLE. Con un recorte del 4 % entraba el MARCO de la
    figura —el del escaneo o el que el modelo dibuja alrededor del panel— y sus
    lados horizontales y verticales arrastraban el eje: la referencia daba 49°
    y el entregable 36°, dos números falsos que además no hablaban de lo mismo.
    Con el 10 %, referencia y entregable convergen: 57,19 y 57,77. Es la sexta
    vez que aparece el error 19 del §10, y siempre por lo mismo — medir tinta
    que no es la figura."""
    a = np.array(Image.open(png).convert("L")).astype(int)
    h, w = a.shape
    sub = a[int(h * 0.12):int(h * 0.88), int(w * 0.10):int(w * 0.90)]
    m = sub < 150
    if m.sum() < 200:
        return None
    ys, xs = np.where(m)
    x = xs - xs.mean()
    y = (sub.shape[0] - ys) - (sub.shape[0] - ys).mean()
    vals, vecs = np.linalg.eigh(np.cov(np.vstack([x, y])))
    d = vecs[:, int(np.argmax(vals))]
    return dict(valor=float(np.degrees(np.arctan2(d[1], d[0])) % 180))


MEDIDAS = {"contorno": contorno, "angulo": angulo}


def pt_proyectado(px: int, ancho: int) -> float:
    """§11: el hueco de imagen mide 6 pulgadas de ancho en la lámina."""
    return 6 * px / ancho * 72


def glifo(png: Path):
    """Altura de PALABRA, no de glifo suelto: el punto de «2.90» mide 8 px
    aunque los dígitos midan 35, y medirlo a él daba 5,6 pt en una imagen cuyo
    texto medía 9,8."""
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
    return dict(px=px, pt=pt_proyectado(px, W))


def revisar(d, g, control, sin_texto):
    """Las dos condiciones. El aspecto dice que la geometría es fiel; el pt dice
    que se lee. Fiel e ilegible no entra a la lámina, y legible deformada
    tampoco. Un panel no pasa la segunda: va SIN texto por diseño."""
    if d is None:
        return False, ["no se encontró qué medir"], 1.0
    err = abs(d["valor"] - control) / control if control else 0.0
    fallas = []
    if control and err > TOLERANCIA:
        fallas.append("medida %.3f vs control %.3f (desvío %.0f %%)"
                      % (d["valor"], control, err * 100))
    if not sin_texto:
        if g is None:
            fallas.append("no se encontró texto que medir")
        elif g["pt"] < PT_MINIMO:
            fallas.append("letra %d px = %.1f pt, bajo el piso de %.0f"
                          % (g["px"], g["pt"], PT_MINIMO))
    return (not fallas), fallas, err


# ── generación ─────────────────────────────────────────────────────────────
def generar_una(nombre: str, calidad="high") -> int:
    cfg = FIGURAS[nombre]
    ref, sal = RAIZ / cfg["referencia"], RAIZ / cfg["salida"]
    if not ref.exists():
        print("falta la referencia:", ref)
        return 1

    medir = MEDIDAS.get(cfg["medida"] or "contorno")
    control = float(cfg["control"]) if cfg["control"] else 0.0
    intentos = int(cfg["intentos"] or 1)
    sin_texto = cfg["tipo"] == "panel"

    base = medir(ref)
    print("REFERENCIA  %s" % ref.name)
    if base:
        print("  medida de la fuente %.3f  ·  control %.3f" % (base["valor"], control))
    print("  %s" % cfg["origen_control"][:78])
    print("  tolerancia %.0f %%  ·  %d intento(s)%s\n"
          % (TOLERANCIA * 100, intentos, "  ·  sin texto" if sin_texto else ""))

    prompt = PROMPT.format(encargo=cfg["encargo"])
    taller = ref.parent / "_crudos"
    taller.mkdir(parents=True, exist_ok=True)

    mejor = None
    for i in range(1, intentos + 1):
        with open(ref, "rb") as fh:
            r = cliente().images.edit(model=MODELO_IMAGEN, image=[fh], prompt=prompt,
                                      size=cfg["tam"], quality=calidad)
        crudo = taller / ("%s_%d.png" % (nombre, i))
        crudo.write_bytes(base64.b64decode(r.data[0].b64_json))
        d, g = medir(crudo), glifo(crudo)
        ok, fallas, err = revisar(d, g, control, sin_texto)
        print("  intento %d  %-8s medida %.3f  %s"
              % (i, "PASA" if ok else "no pasa", d["valor"] if d else 0, "; ".join(fallas)))
        if mejor is None or err < mejor[0] or ok:
            mejor = (err, crudo, d, g, ok)
        if ok:
            break

    err, crudo, d, g, ok = mejor
    sal.parent.mkdir(parents=True, exist_ok=True)
    Image.open(crudo).convert("RGB").save(sal)
    print("\nENTREGABLE  %s" % sal.relative_to(RAIZ.parent))
    if control:
        print("  medida %.3f contra control %.3f (desvío %.1f %%)"
              % (d["valor"], control, err * 100))
    if g and not sin_texto:
        print("  letra %d px  ->  %.1f pt proyectados" % (g["px"], g["pt"]))
    print("  VERIFICADA" if ok else
          "  NO PASÓ en %d intento(s). Se entrega el mejor y SE DECLARA." % intentos)
    return 0 if ok else 2


# ── montaje ────────────────────────────────────────────────────────────────
def _fuente(px, bold=False):
    return ImageFont.truetype(str(Path(FUENTES) / ("arialbd.ttf" if bold else "arial.ttf")), px)


def _recortar(im: Image.Image, margen=12) -> Image.Image:
    """Sin esto los paneles entran con aires distintos y la fila queda
    descuadrada aunque cada uno esté bien."""
    a = np.array(im.convert("L"))
    t = np.where(a < 235)
    if t[0].size == 0:
        return im
    y0, y1, x0, x1 = t[0].min(), t[0].max(), t[1].min(), t[1].max()
    return im.crop((max(x0 - margen, 0), max(y0 - margen, 0),
                    min(x1 + margen, im.width), min(y1 + margen, im.height)))


def componer(nombre: str) -> int:
    """Monta varios paneles ya verificados en una imagen de lámina.

    Componer es maquetación; inventar la geometría de un panel sería lo
    prohibido. Si falta un panel, esto se detiene: no rellena el hueco."""
    cfg = FIGURAS[nombre]
    ids = [s.strip() for s in cfg["referencia"].split(";")]
    rot = [r.split("|") for r in cfg["rotulos"].split(";")]
    rutas = [RAIZ / FIGURAS[i]["salida"] for i in ids]
    faltan = [i for i, r in zip(ids, rutas) if not r.exists()]
    if faltan:
        print("Faltan paneles: %s\nGenéralos primero:" % ", ".join(faltan))
        for i in faltan:
            print("    python %s %s" % (Path(__file__).name, i))
        return 1

    ims = [_recortar(Image.open(r).convert("RGB")) for r in rutas]
    hueco = int(W_LAMINA / len(ims))
    alto_panel = int(hueco * 0.82)
    # se igualan por ALTURA: por ancho, la veta quedaría enana junto al manto
    ims = [im.resize((min(int(im.width * alto_panel / im.height), hueco - 30),
                      alto_panel), Image.LANCZOS) for im in ims]

    y_rot = 40 + alto_panel + 40
    alto = y_rot + CUERPO + 18 + NOTA * 3 + 70
    lienzo = Image.new("RGB", (W_LAMINA, alto), BLANCO)
    d = ImageDraw.Draw(lienzo)
    for i, (im, (titulo, pie)) in enumerate(zip(ims, rot)):
        cx = int(hueco * (i + 0.5))
        lienzo.paste(im, (cx - im.width // 2, 40 + (alto_panel - im.height) // 2))
        d.text((cx, y_rot), titulo, font=_fuente(CUERPO, True), fill=MARINO, anchor="ma")
        d.multiline_text((cx, y_rot + CUERPO + 16), pie.replace("\\n", "\n"),
                         font=_fuente(NOTA), fill=MARINO, anchor="ma",
                         align="center", spacing=10)
    d.text((W_LAMINA // 2, alto - 52), cfg["pie"], font=_fuente(NOTA - 6),
           fill=GRIS, anchor="ma")

    sal = RAIZ / cfg["salida"]
    sal.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(sal)
    print("ENTREGABLE  %s" % sal.relative_to(RAIZ.parent))
    print("  lienzo %d x %d px" % (lienzo.width, lienzo.height))
    print("  rótulo %d px -> %.1f pt  ·  pie %d px -> %.1f pt"
          % (CUERPO, pt_proyectado(CUERPO, W_LAMINA), NOTA, pt_proyectado(NOTA, W_LAMINA)))
    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("figura", nargs="?")
    p.add_argument("--lista", action="store_true")
    p.add_argument("--calidad", default="high", choices=["low", "medium", "high"])
    a = p.parse_args()
    if a.lista or not a.figura:
        for k, v in FIGURAS.items():
            print("  %-16s %-12s %s" % (k, v["tipo"], v["salida"]))
        sys.exit(0)
    if a.figura not in FIGURAS:
        sys.exit("no está en figuras.csv: " + a.figura)
    sys.exit(componer(a.figura) if FIGURAS[a.figura]["tipo"] == "composicion"
             else generar_una(a.figura, a.calidad))
