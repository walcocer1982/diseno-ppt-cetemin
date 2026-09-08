# -*- coding: utf-8 -*-
"""Une los TRES PANELES de la lámina 13 en una sola imagen de lámina.

EL REPARTO DE TRABAJO, Y POR QUÉ ES ASÍ
    La lámina 13 enseña algo FÍSICO —tres formas de cuerpo mineralizado— y eso
    no se dibuja de cero. Pero tampoco existe una figura única que las traiga a
    las tres. La salida, que propuso Erick: **tres imágenes, cada una de su
    fuente, y unificarlas**.

        veta    ←  Hartmann, C. (1843), Grundzüge der Geologie, Fig. 7, p. 36
        manto   ←  Naumann, C. F. (1850), Lehrbuch der Geognosie, p. 915
        lentes  ←  Naumann, C. F. (1850), la misma lámina, otro sector

    Cada panel lo produce `gen_figura_fuente.py` por el camino híbrido, con su
    control medido contra la fuente. Este script NO dibuja geología: recorta el
    aire sobrante, iguala los tres a la misma altura, los pone en fila y les
    escribe el rótulo debajo. Eso es maquetación.

    **La línea que no se cruza:** componer es legítimo, inventar no. Si un
    panel falta, este script se detiene y lo dice — no rellena el hueco.

POR QUÉ EL RÓTULO SE PONE AQUÍ Y NO EN EL PANEL
    Cuando se le pide al modelo dibujo Y letra grande a la vez, sacrifica una
    de las dos: en el intento anterior comprimió el dibujo un 33 % para meter
    los rótulos (OBS-39). Separando las tareas, el modelo solo dibuja y la
    letra la pone matplotlib, exacta, a 52 px sobre 1500 → 15 pt proyectados.

Uso:  python unir_formas_cuerpo.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parents[1]
PANELES = RAIZ / "EOM" / "esquemas" / "_paneles"
SALIDA = RAIZ / "EOM" / "esquemas" / "metexp" / "s1" / "s1_formas-del-cuerpo.png"
# CARPETAS. Los esquemas de EOM se ordenan por CURSO y luego por sesion:
# metexp/s1..s11, sost/s1..., y comun/ para lo que sirve a mas de uno.
# Antes colgaban de la raiz por sesion, cuando EOM tenia un solo curso
# disenado; con el segundo, «s1» era ambiguo. Ver OBS-EOM-SOST-18.


W = 1500                      # §11: de aquí salen los pt proyectados
CUERPO, NOTA = 52, 42         # 15,0 y 12,1 pt
MARINO, GRIS, BLANCO = (13, 38, 50), (108, 122, 130), (255, 255, 255)
FUENTES = r"C:\Windows\Fonts"

# El orden es el del desarrollo del punto clave: de lo más delgado a lo más ancho.
FORMAS = [
    ("forma_veta.png",   "VETA",   "delgada y larga,\nentre dos cajas"),
    ("forma_manto.png",  "MANTO",  "una capa echada,\nque sigue a los estratos"),
    ("forma_lentes.png", "CUERPO", "un volumen que corta\nlos estratos"),
]
PIE = ("Veta: Hartmann (1843), fig. 7, p. 36.   ·   "
       "Manto y cuerpo: Naumann (1850), p. 915.")


def _fuente(px, bold=False):
    return ImageFont.truetype(str(Path(FUENTES) / ("arialbd.ttf" if bold else "arial.ttf")), px)


def _recortar_aire(im: Image.Image, margen=12) -> Image.Image:
    """Quita el blanco sobrante. Sin esto, los paneles entran con aires
    distintos y la fila queda descuadrada aunque cada uno esté bien."""
    a = np.array(im.convert("L"))
    tinta = np.where(a < 235)
    if tinta[0].size == 0:
        return im
    y0, y1 = tinta[0].min(), tinta[0].max()
    x0, x1 = tinta[1].min(), tinta[1].max()
    return im.crop((max(x0 - margen, 0), max(y0 - margen, 0),
                    min(x1 + margen, im.width), min(y1 + margen, im.height)))


def unir() -> Path:
    faltan = [n for n, _, _ in FORMAS if not (PANELES / n).exists()]
    if faltan:
        raise SystemExit(
            "Faltan paneles: %s\n"
            "Genéralos primero, uno por uno, y solo entran los que PASEN:\n"
            "    python gen_figura_fuente.py forma-veta\n"
            "    python gen_figura_fuente.py forma-manto\n"
            "    python gen_figura_fuente.py forma-lentes"
            % ", ".join(faltan))

    ims = [_recortar_aire(Image.open(PANELES / n).convert("RGB")) for n, _, _ in FORMAS]

    # tres columnas iguales, y dentro de cada una el panel a la misma ALTURA:
    # igualar por ancho dejaría la veta enana al lado del manto apaisado.
    hueco = int(W / 3)
    alto_panel = int(hueco * 0.82)
    esc = [(int(im.width * alto_panel / im.height), alto_panel) for im in ims]
    esc = [(min(w, hueco - 30), h) for w, h in esc]
    ims = [im.resize(t, Image.LANCZOS) for im, t in zip(ims, esc)]

    y_panel, y_rotulo = 40, 40 + alto_panel + 40
    alto = y_rotulo + CUERPO + 18 + NOTA * 3 + 70
    lienzo = Image.new("RGB", (W, alto), BLANCO)
    d = ImageDraw.Draw(lienzo)

    for i, (im, (_, titulo, pie)) in enumerate(zip(ims, FORMAS)):
        cx = int(hueco * (i + 0.5))
        lienzo.paste(im, (cx - im.width // 2, y_panel + (alto_panel - im.height) // 2))
        f = _fuente(CUERPO, True)
        d.text((cx, y_rotulo), titulo, font=f, fill=MARINO, anchor="ma")
        f2 = _fuente(NOTA)
        d.multiline_text((cx, y_rotulo + CUERPO + 16), pie, font=f2, fill=MARINO,
                         anchor="ma", align="center", spacing=10)

    d.text((W // 2, alto - 52), PIE, font=_fuente(NOTA - 6), fill=GRIS, anchor="ma")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(SALIDA)
    print("ENTREGABLE  %s" % SALIDA.relative_to(RAIZ.parent))
    print("  lienzo %d x %d px" % (lienzo.width, lienzo.height))
    print("  rótulo %d px  ->  %.1f pt proyectados" % (CUERPO, 6 * CUERPO / W * 72))
    print("  pie    %d px  ->  %.1f pt proyectados" % (NOTA, 6 * NOTA / W * 72))
    return SALIDA


if __name__ == "__main__":
    sys.exit(0 if unir() else 1)
