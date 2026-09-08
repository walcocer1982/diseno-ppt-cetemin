# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 · El dimensionamiento de la labor.

Complementan a `gen_esquemas_s1_yacimiento.py`: aquél explica el CUERPO
mineralizado (forma, potencia, buzamiento); éste explica qué decide el ANCHO
de la labor —el RMR, la tabla geomecánica y el sostenimiento.

Cada uno responde a la frase `que_muestra` de su lámina, escrita ANTES de
producir. Métrica y paleta se importan del módulo del yacimiento para que
todo el set de la S1 se vea igual: lienzo 1500 px, cuerpo 52 px, sin
bbox_inches, esquemas SIN título dentro (el título lo pone la lámina).
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, PROPORCION, VERDE, cuerpo, guardar, lienzo, nota, rotulo,
)

H = 100 / PROPORCION


def _caja(ax, x, y, w, h, color, borde="none", lw=0):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=borde, lw=lw))


def _cota(ax, x1, x2, y, texto, color=MARINO, arriba=True):
    """Línea de cota con topes y su medida."""
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=2.2,
                                mutation_scale=16))
    for x in (x1, x2):
        ax.plot([x, x], [y - 1.4, y + 1.4], color=color, lw=1.8)
    ax.text((x1 + x2) / 2, y + (2.9 if arriba else -3.0), texto, ha="center",
            va="center", family=F, fontsize=CUERPO, fontweight="bold", color=color)


def _arco(x, y, w, h, alto_arco):
    """Polígono de labor con bóveda en arco: hastiales rectos y techo curvo."""
    pts = [(x, y), (x, y + h)]
    for i in range(41):
        a = math.pi * i / 40
        pts.append((x + w / 2 - (w / 2) * math.cos(a),
                    y + h + alto_arco * math.sin(a)))
    pts += [(x + w, y + h), (x + w, y)]
    return pts


# ═══════════════════════════════════════════════════════ 1 · la escala del RMR
def rmr_escala():
    """La nota del macizo, de 0 a 100, con sus cinco tramos de calidad."""
    fig, ax = lienzo()

    tramos = [("Muy mala", 0, 20, MARINO, BLANCO),
              ("Mala", 20, 40, MORADO, BLANCO),
              ("Regular", 40, 60, AZUL, BLANCO),
              ("Buena", 60, 80, VERDE, BLANCO),
              ("Muy buena", 80, 100, AMBAR, MARINO)]

    x0, ancho, y, alto = 8, 84, 44, 15
    for nombre, a, b, color, tinta in tramos:
        xa, xb = x0 + ancho * a / 100, x0 + ancho * b / 100
        _caja(ax, xa, y, xb - xa, alto, color)
        ax.text((xa + xb) / 2, y + alto / 2, nombre, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=tinta)

    for v in (0, 20, 40, 60, 80, 100):
        x = x0 + ancho * v / 100
        ax.plot([x, x], [y - 2.2, y], color=MARINO, lw=1.6)
        ax.text(x, y - 5.2, str(v), ha="center", va="center", family=F,
                fontsize=NOTA, color=GRIS)

    # el dato del caso, señalado sin color: la flecha basta
    xm = x0 + ancho * 40 / 100
    ax.annotate("", xy=(xm, y + alto + 0.6), xytext=(xm, y + alto + 9),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.6,
                                mutation_scale=20))
    rotulo(ax, xm, y + alto + 12.5, "RMR 40", size=FUERTE)
    cuerpo(ax, xm, y + alto + 17.5, "las cajas de la veta Mary", GRIS)

    cuerpo(ax, 50, y - 14, "A menor RMR, peor calidad de roca\ny menos estabilidad.")
    nota(ax, 8, "El RMR sale del mapeo geomecánico, no del criterio del maestro.")
    return guardar(fig, "comun/rmr-escala.png")


# ══════════════════════════════════════════════ 2 · el RMR es del terreno
def rmr_por_zona():
    """Un mismo frente con tres calidades: caja techo, mineral y caja piso."""
    fig, ax = lienzo()

    x0, w = 10, 50
    zonas = [("CAJA TECHO", "RMR 40", MORADO, H - 34, 17),
             ("MINERAL", "RMR 55", AZUL, H - 51, 17),
             ("CAJA PISO", "RMR 40", MORADO, H - 68, 17)]

    for nombre, valor, color, y, alto in zonas:
        _caja(ax, x0, y, w, alto, color)
        ax.text(x0 + w / 2, y + alto / 2 + 2.6, nombre, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
        ax.text(x0 + w / 2, y + alto / 2 - 3.2, valor, ha="center", va="center",
                family=F, fontsize=CUERPO, fontweight="bold", color=BLANCO)
        ax.annotate("", xy=(x0 + w + 8.5, y + alto / 2),
                    xytext=(x0 + w + 2.5, y + alto / 2),
                    arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.2,
                                    mutation_scale=16))

    ax.add_patch(FancyBboxPatch((x0 + w + 10, H - 68), 100 - x0 - w - 14, 51,
                                boxstyle="round,pad=0.3,rounding_size=1.2",
                                facecolor=CLARO, edgecolor="none"))
    ax.text(x0 + w + 10 + (100 - x0 - w - 14) / 2, H - 42.5,
            "Es el mismo\nfrente.\n\nTres calidades\ndistintas.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)

    cuerpo(ax, 50, 18, "El RMR no cambia con el ancho que se abra:\n"
                       "es una condición del terreno.")
    nota(ax, 7, "Por eso la ficha lo declara por zona, y no una sola vez por labor.")
    return guardar(fig, "s1_rmr-por-zona.png")


# ══════════════════════════════════════ 3 · potencia, ancho de minado, sección
def tres_medidas():
    """Las tres medidas acotadas sobre el mismo dibujo, para no confundirlas."""
    fig, ax = lienzo()

    # la excavación: 3,00 x 3,00 m
    xl, wl, yl, hl = 27, 46, H - 62, 34
    _caja(ax, xl - 13, yl - 4, wl + 26, hl + 8, CLARO)
    _caja(ax, xl, yl, wl, hl, BLANCO, MARINO, 2.6)

    # la veta dentro: 1,20 m de los 3,00
    wv = wl * 1.20 / 3.00
    _caja(ax, xl + (wl - wv) / 2, yl, wv, hl, VERDE)
    ax.text(xl + wl / 2, yl + hl / 2, "VETA", ha="center", va="center", family=F,
            fontsize=NOTA, fontweight="bold", color=BLANCO, rotation=90)

    _cota(ax, xl + (wl - wv) / 2, xl + (wl + wv) / 2, yl + hl + 6,
          "potencia  1,20 m", VERDE)
    _cota(ax, xl, xl + wl, yl - 7, "ancho de minado  3,00 m", AZUL, arriba=False)

    ax.annotate("", xy=(xl - 5.5, yl), xytext=(xl - 5.5, yl + hl),
                arrowprops=dict(arrowstyle="<|-|>", color=MORADO, lw=2.2,
                                mutation_scale=16))
    ax.text(xl - 8.5, yl + hl / 2, "3,00 m", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=MORADO, rotation=90)
    rotulo(ax, 85, yl + hl / 2, "sección\n3,00 × 3,00", MORADO, size=CUERPO)

    cuerpo(ax, 50, 12.5, "La potencia es un dato del yacimiento.\n"
                         "El ancho de minado es una decisión de la mina.")
    nota(ax, 4.5, "Una veta de 1,20 m no da una labor de 1,20 m.")
    return guardar(fig, "s1_tres-medidas.png")


# ═══════════════════════════════════════════ 4 · la tabla geomecánica
def tabla_geomecanica():
    """La tabla que por el Art. 33 se publica en cada labor."""
    fig, ax = lienzo()

    # Cuatro columnas es el maximo que admite el ancho a 52 px: la cabecera va
    # en dos lineas y un punto por debajo del cuerpo, o no entra.
    cols = [(5, 26), (31, 21), (52, 15), (67, 28)]
    cab = ["CALIDAD\nDE ROCA", "ABERTURA\nSIN SOSTENER", "AUTO-\nSOPORTE",
           "CON\nSOSTENIMIENTO"]
    filas = [("Regular A · 51-60", "5,0 m", "1 sem", "8,0 m", False),
             ("Regular B · 41-50", "3,5 m", "24 h", "10,0 m", False),
             ("Mala A · 31-40", "3,0 m", "10 h", "12,0 m", True),
             ("Mala B · 21-30", "2,0 m", "5 h", "6,0 m", False)]

    y = 74
    for (x, w), t in zip(cols, cab):
        _caja(ax, x, y, w - 1.2, 13, MARINO)
        ax.text(x + (w - 1.2) / 2, y + 6.5, t, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, fontweight="bold", color=BLANCO,
                linespacing=1.25)

    y -= 11.5
    for calidad, sin_s, auto, con_s, marcada in filas:
        fondo = AMBAR if marcada else CLARO
        for (x, w), v in zip(cols, (calidad, sin_s, auto, con_s)):
            _caja(ax, x, y, w - 1.2, 10, fondo)
            ax.text(x + (w - 1.2) / 2, y + 5, v, ha="center", va="center",
                    family=F, fontsize=NOTA * 0.9,
                    fontweight="bold" if marcada else "normal", color=MARINO)
        y -= 10.8

    ax.plot([5, 95], [27.5, 27.5], color=GRIS, lw=1.4)
    ax.text(5, 23.5, "Ing. geomecánico colegiado · vigencia: mes en curso",
            ha="left", va="center", family=F, fontsize=NOTA * 0.9, color=GRIS)

    cuerpo(ax, 50, 14, "Con el mismo macizo, el sostenimiento\ntriplica la abertura.")
    nota(ax, 4.5, "D.S. 024-2016-EM, Art. 33: se publica en cada labor.")
    return guardar(fig, "comun/tabla-geomecanica.png")


# ══════════════════════════════════════════ 5 · sostenimiento pasivo y activo
def pasivo_activo():
    """La madera recibe la carga después; el perno y el shotcrete, antes."""
    fig, ax = lienzo()

    for xo, titulo, color in ((5, "PASIVO", MORADO), (53, "ACTIVO", VERDE)):
        _caja(ax, xo, 80, 42, 9, color)
        ax.text(xo + 21, 84.5, titulo, ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)

    yl, hl, wl = 46, 22, 30

    # ---- pasivo: la roca ya se movió y la madera recibe
    xl = 11
    _caja(ax, xl - 6, 42, wl + 12, 36, CLARO)
    _caja(ax, xl, yl, wl, hl, BLANCO, MARINO, 2.4)
    for x in (xl + 2.5, xl + wl - 2.5):        # los dos postes del cuadro
        _caja(ax, x - 1.4, yl, 2.8, hl, MORADO)
    _caja(ax, xl + 2.5 - 1.4, yl + hl - 2.8, wl - 5 + 2.8, 2.8, MORADO)  # el sombrero
    for dx in (-8, 0, 8):                       # la carga, ya cayendo
        ax.annotate("", xy=(xl + wl / 2 + dx, yl + hl + 1.5),
                    xytext=(xl + wl / 2 + dx, yl + hl + 8),
                    arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4,
                                    mutation_scale=18))
    ax.text(xl + wl / 2, 36, "cuadros de madera\ncimbras", ha="center",
            va="center", family=F, fontsize=NOTA, color=MARINO, linespacing=1.3)

    # ---- activo: los pernos cosen la roca antes de que se mueva
    xl = 59
    _caja(ax, xl - 6, 42, wl + 12, 36, CLARO)
    _caja(ax, xl, yl, wl, hl, BLANCO, MARINO, 2.4)
    _caja(ax, xl, yl + hl - 1.6, wl, 1.6, VERDE)          # la capa de shotcrete
    for dx in (-9, -3, 3, 9):                              # los pernos, hacia adentro
        ax.annotate("", xy=(xl + wl / 2 + dx, yl + hl + 8),
                    xytext=(xl + wl / 2 + dx, yl + hl - 1.2),
                    arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2.6,
                                    mutation_scale=18))
    ax.text(xl + wl / 2, 36, "pernos Hydrabolt\nshotcrete SFR", ha="center",
            va="center", family=F, fontsize=NOTA, color=MARINO, linespacing=1.3)

    cuerpo(ax, 26, 21, "Recibe la carga\ncuando la roca se mueve.", MORADO)
    cuerpo(ax, 74, 21, "Trabaja con la roca\nantes de que se mueva.", VERDE)
    nota(ax, 6, "Por eso el mismo terreno admite más abertura con sostenimiento activo.")
    return guardar(fig, "s1_pasivo-activo.png")


# ═════════════════════════════════════ 6 · el sostenimiento mueve el límite
def tres_anchos():
    """El mismo RMR 40 abierto a 3, 6 y 12 m según cómo se sostenga."""
    fig, ax = lienzo()

    # Escala unica para ancho Y alto: si el alto fuera fijo, la labor de 3 m
    # saldria como una torre y la de 12 m como un pasillo. Aqui son labores.
    esc = 3.15                                   # unidades de lienzo por metro
    labores = [(3.0, 3.0, "3,00 m", "cuadros\nde madera", MORADO, False),
               (6.0, 4.0, "6,00 m", "shotcrete SFR\ny Hydrabolt", VERDE, True),
               (12.0, 4.5, "12,00 m", "shotcrete SFR\ny Hydrabolt", VERDE, True)]

    # El RMR va una sola vez, arriba: es el mismo en las tres y dentro de la
    # labor de 3,00 m no cabe.
    ax.add_patch(FancyBboxPatch((32, 76), 36, 9,
                                boxstyle="round,pad=0.3,rounding_size=1.2",
                                facecolor=CLARO, edgecolor="none"))
    ax.text(50, 80.5, "el mismo macizo  ·  RMR 40", ha="center", va="center",
            family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)

    x, ybase = 9, 45
    for ancho_m, alto_m, cota, sost, color, arco in labores:
        w, h = ancho_m * esc, alto_m * esc
        if arco:
            ax.add_patch(Polygon(_arco(x, ybase, w, h, 0.18 * ancho_m * esc),
                                 closed=True, facecolor=BLANCO, edgecolor=color,
                                 lw=2.8))
        else:
            _caja(ax, x, ybase, w, h, BLANCO, color, 2.8)
        _cota(ax, x, x + w, ybase - 6, cota, color, arriba=False)
        ax.text(x + w / 2, ybase - 16, sost, ha="center", va="center", family=F,
                fontsize=NOTA, color=MARINO, linespacing=1.3)
        x += w + 7

    cuerpo(ax, 50, 15, "El mismo macizo, tres aberturas.\n"
                       "Lo único que cambia es cómo se sostiene.")
    nota(ax, 5, "U.M. Parcoy: de 3,00 m con madera a 12,00 m en bóveda.")
    return guardar(fig, "s1_tres-anchos.png")


if __name__ == "__main__":
    from PIL import Image
    for fn in (rmr_escala, rmr_por_zona, tres_medidas, tabla_geomecanica,
               pasivo_activo, tres_anchos):
        f = fn()
        w, h = Image.open(f).size
        pt = 6 * 52 / w * 72
        print("  %-30s %4d x %4d px   cuerpo -> %.1f pt proyectados %s"
              % (f.name, w, h, pt, "OK" if pt >= 14.5 else "!! BAJO"))
