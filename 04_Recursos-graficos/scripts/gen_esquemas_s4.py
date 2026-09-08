# -*- coding: utf-8 -*-
"""Esquemas de la sesion 4: sublevel stoping y block caving.

Se dibujan porque son GEOMETRIA DE METODO, no de equipo: la disposicion de
subniveles, taladros y puntos de extraccion es la que caracteriza al metodo, no
las cotas de una mina concreta. El §10 (nunca texto->imagen) aplica a EQUIPOS.

Los dos metodos son opuestos —uno deja el vacio abierto, el otro lo provoca— y
los dibujos lo muestran: el mismo lienzo, el mismo cuerpo, y lo que pasa con el
hueco.
"""
from __future__ import annotations

import random
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle

AZUL, AMBAR, BLANCO, GRIS = "#0D2632", "#FFC505", "#FFFFFF", "#8A9AA3"
ROCA, VACIO = "#D9DEE0", "#FFFFFF"
F = "Arial"
SALIDA = Path("../EOM/esquemas/comun")
# CARPETAS. Los esquemas de EOM se ordenan por CURSO y luego por sesion:
# metexp/s1..s11, sost/s1..., y comun/ para lo que sirve a mas de uno.
# Antes colgaban de la raiz por sesion, cuando EOM tenia un solo curso
# disenado; con el segundo, «s1» era ambiguo. Ver OBS-EOM-SOST-18.



def sublevel_stoping() -> Path:
    """El tajeo abierto entre subniveles, con los taladros largos."""
    fig, ax = plt.subplots(figsize=(9.5, 6.4), dpi=200)
    ax.set_xlim(-0.5, 9.5); ax.set_ylim(-1.1, 8.3); ax.axis("off")
    fig.patch.set_alpha(0)
    ax.add_patch(Rectangle((0, 0), 9, 7.4, facecolor=ROCA, edgecolor=AZUL, lw=1.4))
    ax.add_patch(Polygon([(3.2, 0.6), (5.8, 0.6), (6.1, 6.9), (3.5, 6.9)],
                 facecolor=AMBAR, alpha=0.30, edgecolor=AMBAR, lw=1.4))
    ax.add_patch(Polygon([(3.55, 1.7), (5.55, 1.7), (5.8, 6.4), (3.8, 6.4)],
                 facecolor=VACIO, edgecolor=AZUL, lw=1.2))
    ax.text(4.68, 4.3, "TAJEO\nVACÍO", ha="center", va="center", family=F,
            fontsize=10, fontweight="bold", color=AZUL, linespacing=1.3)

    for y, et in ((6.4, "subnivel superior"), (4.4, "subnivel"), (2.4, "subnivel")):
        ax.add_patch(Rectangle((0.55, y - 0.20), 2.9, 0.40, facecolor=VACIO, edgecolor=AZUL, lw=1.1))
        ax.text(0.65, y, et, va="center", family=F, fontsize=7.6, color=AZUL)
        for k in range(5):
            ax.plot([3.5, 3.78], [y - 0.16 + k * 0.08, y - 1.70 + k * 0.28],
                    color=AZUL, lw=0.8, alpha=0.75)
    ax.text(1.9, 7.80, "TALADROS LARGOS desde cada subnivel", family=F,
            fontsize=8.6, fontweight="bold", color=AZUL)

    ax.add_patch(Rectangle((0.55, 0.25), 7.9, 0.55, facecolor=VACIO, edgecolor=AZUL, lw=1.2))
    ax.text(6.95, 0.52, "nivel de extracción", va="center", family=F, fontsize=8, color=AZUL)
    for x in (4.0, 4.7, 5.4):
        ax.add_patch(FancyArrowPatch((x, 1.62), (x, 0.92),
                     arrowstyle="-|>,head_width=3.5,head_length=6", color=AMBAR, lw=1.8))
    ax.text(6.45, 1.35, "el mineral cae\npor gravedad", va="center", family=F,
            fontsize=8.2, color=AZUL, linespacing=1.4)
    ax.text(4.5, -0.78, "El vacío queda abierto: nada lo rellena ni lo apuntala.",
            ha="center", family=F, fontsize=10, color=AZUL)

    f = SALIDA / "sublevel-stoping.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


def block_caving() -> Path:
    """Socavar la base, el bloque se hunde solo, el mineral fluye."""
    fig, ax = plt.subplots(figsize=(9.5, 6.4), dpi=200)
    ax.set_xlim(-0.5, 9.5); ax.set_ylim(-1.1, 8.3); ax.axis("off")
    fig.patch.set_alpha(0)
    ax.add_patch(Rectangle((0, 0), 9, 7.4, facecolor=ROCA, edgecolor=AZUL, lw=1.4))
    ax.add_patch(Polygon([(2.6, 7.4), (3.4, 6.5), (5.6, 6.5), (6.4, 7.4)],
                 facecolor=VACIO, edgecolor=AZUL, lw=1.3))
    ax.text(4.5, 7.80, "SUBSIDENCIA · el hundimiento llega a superficie",
            ha="center", family=F, fontsize=8.6, fontweight="bold", color=AZUL)

    ax.add_patch(Rectangle((3.0, 1.55), 3.0, 4.95, facecolor=AMBAR, alpha=0.28,
                 edgecolor=AMBAR, lw=1.4))
    random.seed(4)                       # el mismo dibujo en cada corrida
    for _ in range(95):
        x = 3.05 + random.random() * 2.9
        y = 1.60 + random.random() * 4.8
        r = 0.045 + random.random() * 0.085 * (1.7 - y / 6.0)
        ax.add_patch(plt.Circle((x, y), max(r, 0.03), facecolor=AZUL, alpha=0.28, edgecolor="none"))
    ax.text(4.5, 5.70, "el bloque se fractura\npor su propio peso", ha="center", va="center",
            family=F, fontsize=8.6, color=AZUL, linespacing=1.4)
    for x in (3.6, 4.5, 5.4):
        ax.add_patch(FancyArrowPatch((x, 3.6), (x, 2.05),
                     arrowstyle="-|>,head_width=3.5,head_length=6", color=AMBAR, lw=1.8))

    ax.add_patch(Rectangle((2.8, 1.18), 3.4, 0.35, facecolor=VACIO, edgecolor=AZUL, lw=1.2))
    ax.text(6.35, 1.36, "nivel de socavación", va="center", family=F, fontsize=8, color=AZUL)
    ax.add_patch(Rectangle((0.55, 0.28), 7.9, 0.50, facecolor=VACIO, edgecolor=AZUL, lw=1.2))
    ax.text(6.65, 0.53, "nivel de extracción", va="center", family=F, fontsize=8, color=AZUL)
    for x in (3.4, 4.2, 5.0, 5.8):
        ax.add_patch(Polygon([(x - 0.22, 1.16), (x + 0.22, 1.16), (x, 0.80)],
                     facecolor=AMBAR, edgecolor=AZUL, lw=0.9))
    ax.text(1.5, 0.98, "puntos de\nextracción", ha="center", va="center", family=F,
            fontsize=7.8, color=AZUL, linespacing=1.35)
    ax.text(4.5, -0.78, "Se extrae de forma continua: no se vuelve a perforar ni a disparar.",
            ha="center", family=F, fontsize=10, color=AZUL)

    f = SALIDA / "block-caving.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


def condiciones_s4(cual: str) -> Path:
    """Que le pide el yacimiento a cada uno. Mismo cuadro, otro resaltado."""
    filas = [("EL CUERPO",   "regular, de contornos definidos", "masa grande, 200 m o más"),
             ("LA ROCA",     "competente: aguanta el vacío",    "se fractura sola al perder apoyo"),
             ("LA LEY",      "media a alta",                    "baja: el volumen compensa"),
             ("LA SUPERFICIE", "no se altera",                  "se hunde: hay subsidencia"),
             ("PREPARACIÓN", "moderada",                        "larga y cara"),
             ("¿SE DETIENE?", "sí, tajeo por tajeo",            "no: una vez iniciado, sigue")]
    sls = cual == "sublevel-stoping"
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.2, 5.1); ax.axis("off")
    fig.patch.set_alpha(0)
    ax.add_patch(Rectangle((3.35, 0.30), 3.20, 4.25, facecolor=AZUL if sls else "none",
                 edgecolor=AMBAR if sls else "none", lw=2))
    ax.add_patch(Rectangle((6.70, 0.30), 3.20, 4.25, facecolor="none" if sls else AZUL,
                 edgecolor="none" if sls else AMBAR, lw=2))
    ax.text(4.95, 4.80, "SUBLEVEL STOPING", ha="center", family=F, fontsize=11.5,
            fontweight="bold", color=AZUL)
    ax.text(8.30, 4.80, "BLOCK CAVING", ha="center", family=F, fontsize=11.5,
            fontweight="bold", color=AZUL)
    y = 4.10
    for k, a, b in filas:
        ax.text(0.15, y, k, family=F, fontsize=9.2, fontweight="bold", color=AZUL, va="center")
        ax.text(4.95, y, a, ha="center", va="center", family=F, fontsize=8.6,
                color=BLANCO if sls else GRIS)
        ax.text(8.30, y, b, ha="center", va="center", family=F, fontsize=8.6,
                color=GRIS if sls else BLANCO)
        y -= 0.66
    f = SALIDA / f"condiciones-{cual}.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    for f in (sublevel_stoping(), block_caving(),
              condiciones_s4("sublevel-stoping"), condiciones_s4("block-caving")):
        print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")
