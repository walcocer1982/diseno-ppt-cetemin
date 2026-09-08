# -*- coding: utf-8 -*-
"""Rotula en castellano la figura de instalación de cable bolting.

QUÉ HACE Y QUÉ NO HACE
    Maqueta y rotula. No redibuja el mecanismo: el dibujo de los tres pasos
    —el tubo de lechada llevado al fondo, el retorno por el barreno, la cuña
    de la boca— sale tal cual de la tesis y no se toca ni un trazo. Lo único
    que cambia es el idioma de los rótulos, que venían en inglés y son una
    barrera en un curso peruano.

    Es el mismo criterio de unir_formas_cuerpo.py: el script maqueta y rotula;
    no dibuja geología.

FUENTE
    Conde Castelo, Y. (2019). «Análisis del macizo rocoso y su aplicación de
    cables bolting en la ejecución de echaderos de relleno detrítico en la mina
    San Rafael, Melgar - Puno». UNSAAC, figura N° 9.

Uso:  python componer_cable_bolting.py <figura-original.png>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
import numpy as np
from PIL import Image, ImageDraw

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AZUL, BLANCO, F, GRIS, MARINO, NOTA, guardar, lienzo,
)

# recorte que deja los tres paneles y bota las columnas de rótulos en inglés
CAJA = (168, 0, 566, 748)
# rótulos ingleses que quedan dentro del dibujo, en coordenadas del recorte
TAPAR = [(158, 36, 238, 74), (80, 698, 178, 734)]    # TOE · COLLAR

PASOS = [
    ("1", "Entra el cable con su tubo hasta el fondo"),
    ("2", "Se inyecta la lechada, que retorna por el barreno"),
    ("3", "El taladro queda lleno y el cable anclado"),
]
LEYENDA = [
    ("Cabezal", 0.90),
    ("Cable de acero trenzado", 0.58),
    ("Tubo de lechada", 0.74),
    ("Cuña de la boca", 0.12),
]


def limpiar(origen):
    """Recorta las columnas de rótulos y tapa los dos que quedan dentro."""
    im = Image.open(origen).convert("RGB").crop(CAJA)
    d = ImageDraw.Draw(im)
    for caja in TAPAR:
        d.rectangle(caja, fill=(255, 255, 255))
    return im


def componer(origen):
    im = limpiar(origen)
    ancho_px, alto_px = im.size

    ASP = 1.12
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    # el dibujo, a la izquierda, con su proporción intacta
    alto = H * 0.68
    ancho = alto * ancho_px / alto_px
    x0, y0 = 6.0, H * 0.24
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    ax.text(x0 + ancho / 2, y0 + alto + H * 0.045, "FONDO DEL TALADRO",
            ha="center", va="center", family=F, fontsize=NOTA * 0.8, color=GRIS)
    ax.text(x0 + ancho / 2, y0 - H * 0.045, "BOCA DEL TALADRO",
            ha="center", va="center", family=F, fontsize=NOTA * 0.8, color=GRIS)

    # la leyenda, a la derecha, con su línea de guía hasta el dibujo
    xl = x0 + ancho + 4.0
    for texto, frac in LEYENDA:
        y = y0 + alto * frac
        ax.plot([x0 + ancho - 1.0, xl - 1.5], [y, y], color=AZUL,
                linewidth=1.2, zorder=3)
        ax.text(xl, y, texto, ha="left", va="center", family=F,
                fontsize=NOTA * 0.9, color=MARINO)

    # los tres pasos, abajo y a todo el ancho: en la columna de la leyenda
    # se salian del lienzo por la derecha
    y = H * 0.145
    for n, txt in PASOS:
        ax.text(x0, y, "%s   %s" % (n, txt), ha="left", va="center", family=F,
                fontsize=NOTA * 0.85, color=GRIS)
        y -= H * 0.052

    return guardar(fig, "sost/s1/sost-s1_cable-instalacion.png")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("USO · python componer_cable_bolting.py <figura-original.png>")
    componer(sys.argv[1])
    print("  ok  sost/s1/sost-s1_cable-instalacion.png")
