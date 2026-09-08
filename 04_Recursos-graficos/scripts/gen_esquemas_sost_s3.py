# -*- coding: utf-8 -*-
"""Esquemas de la sesión 3 de EOM · Caracterización y zonificación.

La matriz de la cartilla NO se dibuja: se extrae del PDF del propio curso y
vive en `planos/sost_cartilla-gsi_matriz.png`. Es la herramienta de la sesión,
y redibujarla sería inventar una tabla que ya existe —y fue leer su
enumeración en vez de su matriz lo que costó el error del TC1 (OBS-19)—.

Aquí se dibuja lo que no tiene cuerpo: escalas, flujos y el armazón.

Uso:  python gen_esquemas_sost_s3.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, GRIS, MARINO, MORADO, NOTA, VERDE,
    guardar, lienzo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402
from gen_esquemas_sost_s1 import _cabecera  # noqa: E402
from gen_esquemas_sost_s2 import _cierre, _pasos, _tabla  # noqa: E402

CARPETA = "sost/s3/"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    ASP = 2.10
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for x0, titulo, txt, color in ((3.0, "LAS DOS PASADAS",
                                    "Los elementos: qué es cada uno\ny cómo se instala", AZUL),
                                   (52.0, "HOY",
                                    "La roca: cómo se mide\ny hasta dónde llega una zona", VERDE)):
        _redonda(ax, x0, H * 0.26, 45.0, H * 0.50, CLARO)
        _caja(ax, x0, H * 0.70, 45.0, 1.0, color)
        ax.text(x0 + 22.5, H * 0.64, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, fontweight="bold", color=color)
        ax.text(x0 + 22.5, H * 0.44, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO, linespacing=1.4)
    ax.annotate("", xy=(51.0, H * 0.51), xytext=(48.5, H * 0.51),
                arrowprops=dict(arrowstyle="->", color=MARINO, linewidth=2.0))
    _cierre(ax, H, "El elemento lo decide la roca, no al revés", H * 0.06)
    _g(fig, "sost-s3_de-donde-venimos.png")


# ══════════════════════════════════════ 2 · la celda y los rangos
def la_celda():
    """Un metro cuadrado marcado y los cuatro rangos de fracturamiento."""
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    # la primera version dejaba un cuarto del lienzo vacio entre los rangos y
    # la franja de cierre: se estira el bloque y se sube la franja
    _caja(ax, 6.0, H * 0.44, 26.0, H * 0.44, CLARO)
    for k in range(1, 4):
        ax.plot([6.0, 32.0], [H * 0.44 + H * 0.44 * k / 4] * 2, color=GRIS, linewidth=0.8)
        ax.plot([6.0 + 26.0 * k / 4] * 2, [H * 0.44, H * 0.88], color=GRIS, linewidth=0.8)
    ax.annotate("", xy=(32.0, H * 0.40), xytext=(6.0, H * 0.40),
                arrowprops=dict(arrowstyle="<->", color=AZUL, linewidth=1.6))
    ax.text(19.0, H * 0.33, "1,00 m", ha="center", va="center", family=F,
            fontsize=NOTA * 0.9, fontweight="bold", color=MARINO)
    ax.text(19.0, H * 0.94, "se marca con tiza sobre la caja", ha="center",
            va="center", family=F, fontsize=NOTA * 0.8, color=GRIS)
    rangos = [("LF", "2 a 5", "levemente fracturada", AZUL),
              ("F", "6 a 11", "moderadamente fracturada", VERDE),
              ("MF", "12 a 20", "muy fracturada", MORADO),
              ("IF", "más de 20", "intensamente fracturada", GRIS)]
    y = H * 0.88
    for sigla, rango, nombre, color in rangos:
        y -= H * 0.145
        _redonda(ax, 38.0, y, 59.0, H * 0.120, CLARO)
        _redonda(ax, 39.0, y + H * 0.016, 9.0, H * 0.088, color)
        ax.text(43.5, y + H * 0.060, sigla, ha="center", va="center", family=F,
                fontsize=NOTA * 0.9, fontweight="bold", color=BLANCO)
        ax.text(51.0, y + H * 0.060, rango, ha="left", va="center", family=F,
                fontsize=NOTA * 0.85, fontweight="bold", color=MARINO)
        ax.text(66.0, y + H * 0.060, nombre, ha="left", va="center", family=F,
                fontsize=NOTA * 0.82, color=GRIS)
    _cierre(ax, H, "Se cuentan las fracturas que cruzan ese metro cuadrado", H * 0.13)
    _g(fig, "sost-s3_la-celda.png")


# ══════════════════════════════════════════ 3 · las cuatro de la picota
def picota():
    """Las cuatro condiciones superficiales, en el orden de la cartilla.

    Esta es la lámina que evita el error de OBS-19: uno o dos golpes es
    REGULAR y no pobre, y eso hay que decirlo, no dejarlo implícito.
    """
    ASP = 1.32
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(26.0, "LO QUE HACE LA ROCA"), (34.0, "CON LA PICOTA"), (32.0, "CONDICIÓN")]
    filas = [["Se rompe", "con tres o más golpes", "BUENA"],
             ["Se rompe", "con uno o dos golpes", "REGULAR"],
             ["Se indenta", "menos de cinco milímetros", "POBRE"],
             ["Se indenta", "más de cinco milímetros", "MUY POBRE"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.78, H * 0.09, H * 0.135, tam=NOTA * 0.85)
    _cierre(ax, H, "Uno o dos golpes es REGULAR, no pobre: ahí se confunde")
    _g(fig, "sost-s3_picota.png")


# ══════════════════════════════════════════════ 4 · el agua y la fecha
def agua_y_fecha():
    ASP = 1.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.72, 94.0, H * 0.11, "EL TERCER DATO: EL AGUA", MARINO, NOTA * 0.82)
    x = 3.0
    for etq, color in (("SECO", AZUL), ("GOTEO", MORADO), ("FLUJO", VERDE)):
        _redonda(ax, x, H * 0.48, 30.0, H * 0.18, CLARO)
        _caja(ax, x, H * 0.645, 30.0, 1.0, color)
        ax.text(x + 15.0, H * 0.57, etq, ha="center", va="center", family=F,
                fontsize=CUERPO * 0.95, fontweight="bold", color=MARINO)
        x += 32.0
    ax.text(50, H * 0.38, "El agua no mueve la casilla: condiciona el elemento",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9, color=GRIS)
    _cierre(ax, H, "Los tres datos se levantan en el mismo punto y la misma fecha", H * 0.12)
    _g(fig, "sost-s3_agua-y-fecha.png")


# ═════════════════════════════════════ 5 · sin los dos datos no hay casilla
def sin_dos_datos():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    casos = [("Solo el conteo de fracturas", "MF / ?", "no hay casilla", GRIS),
             ("Solo la prueba de picota", "? / P", "no hay casilla", GRIS),
             ("Los dos, en el mismo punto", "MF / P", "casilla completa", VERDE)]
    y = H * 0.70
    for txt, casilla, veredicto, color in casos:
        _redonda(ax, 3.0, y, 94.0, H * 0.185, CLARO)
        ax.text(7.0, y + H * 0.093, txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO)
        _redonda(ax, 52.0, y + H * 0.032, 18.0, H * 0.12, BLANCO)
        ax.text(61.0, y + H * 0.093, casilla, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=color)
        ax.text(74.0, y + H * 0.093, veredicto, ha="left", va="center", family=F,
                fontsize=NOTA * 0.85, color=color)
        y -= H * 0.215
    _cierre(ax, H, "Sin los dos datos no hay casilla, y una casilla no se estima", H * 0.06)
    _g(fig, "sost-s3_sin-dos-datos.png")


# ═════════════════════════════════════════ 6 · el mapeo por celdas
def mapeo_por_celdas():
    """Una galería con sus celdas mapeadas y su metraje."""
    ASP = 2.05
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _caja(ax, 5.0, H * 0.42, 90.0, H * 0.20, CLARO)
    ax.text(50, H * 0.68, "120 metros de galería", ha="center", va="center",
            family=F, fontsize=NOTA * 0.85, color=GRIS)
    for frac, etq in ((0.02, "0 m"), (0.33, "40 m"), (0.66, "80 m"), (0.95, "110 m")):
        x = 5.0 + 90.0 * frac
        _caja(ax, x - 2.2, H * 0.44, 4.4, H * 0.16, BLANCO)
        _caja(ax, x - 2.2, H * 0.58, 4.4, 0.8, AZUL)
        ax.text(x, H * 0.36, etq, ha="center", va="center", family=F,
                fontsize=NOTA * 0.78, fontweight="bold", color=MARINO)
    ax.text(50, H * 0.24, "Cada celda queda con su casilla y con su metraje",
            ha="center", va="center", family=F, fontsize=NOTA * 0.88, color=MARINO)
    _cierre(ax, H, "Una sola celda no describe ciento veinte metros", H * 0.05)
    _g(fig, "sost-s3_mapeo-por-celdas.png")


# ══════════════════════════════════════════ 7 · el mapeo envejece
def mapeo_envejece():
    ASP = 1.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Se mapea la labor tal como está hoy", "la celda con su fecha"),
                   ("La labor avanza y cruza otra cosa", "una falla, un contacto, agua"),
                   ("El mapeo describe una labor que ya no existe", "y el pedido sale de él")],
           H * 0.70, H * 0.165)
    _cierre(ax, H, "El cuaderno de celdas es el registro que queda", H * 0.06)
    _g(fig, "sost-s3_mapeo-envejece.png")


# ══════════════════════════════════════════ 8 · qué es una zona
def que_es_una_zona():
    ASP = 2.05
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    tramos = [(5.0, 34.0, "ZONA 1", "se comporta igual\nen todo el tramo", AZUL),
              (41.0, 26.0, "ZONA 2", "otra casilla,\notro sostenimiento", MORADO),
              (69.0, 26.0, "ZONA 3", "y otra vez\ncambia", VERDE)]
    for x, w, etq, txt, color in tramos:
        _redonda(ax, x, H * 0.40, w, H * 0.30, CLARO)
        _caja(ax, x, H * 0.685, w, 1.0, color)
        ax.text(x + w / 2, H * 0.62, etq, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, fontweight="bold", color=color)
        ax.text(x + w / 2, H * 0.49, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.8, color=MARINO, linespacing=1.35)
    ax.text(50, H * 0.28, "El sostenimiento se pide por zona, no por galería entera",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9, color=MARINO)
    _cierre(ax, H, "Pedir para una galería entera deja tramos sin lo que piden", H * 0.05)
    _g(fig, "sost-s3_que-es-una-zona.png")


# ═══════════════════════════════════════ 9 · qué mueve el límite
def limites():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(30.0, "QUÉ APARECE"), (34.0, "QUÉ LE HACE AL MACIZO"), (30.0, "¿PARTE LA ZONA?")]
    filas = [["Una falla", "corta la roca de\ncaja a caja", "sí, aunque las celdas\nden lo mismo"],
             ["Un contacto\nlitológico", "cambia la roca sin\ncambiar el conteo", "sí"],
             ["Entrada de agua", "no mueve la casilla,\ncondiciona el elemento", "sí"],
             ["Más avance", "nada por sí solo", "no, hasta que\ncambie algo"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.145, tam=NOTA * 0.78)
    _cierre(ax, H, "El límite cae donde cambia algo que la roca acusa", H * 0.04)
    _g(fig, "sost-s3_limites.png")


# ═════════════════════════════════════════ 10 · las cuatro celdas del caso
def cuatro_celdas():
    ASP = 1.36
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(12.0, "CELDA"), (14.0, "METRAJE"), (20.0, "FRACTURAS"),
            (26.0, "PICOTA"), (22.0, "AGUA")]
    filas = [["1", "0 m", "nueve", "tercer golpe", "seca"],
             ["2", "40 m", "nueve", "tercer golpe", "seca"],
             ["3", "80 m", "dieciséis", "primer golpe", "seca"],
             ["4", "110 m", "dieciséis", "primer golpe", "goteo permanente"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.76, H * 0.085, H * 0.115, tam=NOTA * 0.78,
           tam_cab=NOTA * 0.68)
    ax.text(50, H * 0.16, "A los treinta metros, el plano marca una falla con relleno de arcilla",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=MARINO)
    ax.text(50, H * 0.09, "que cruza la galería de caja a caja",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=MARINO)
    _g(fig, "sost-s3_cuatro-celdas.png")


# ═══════════════════════════════════════════ 11 · el reparto que se entrega
def reparto():
    ASP = 1.34
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(16.0, "CELDA"), (28.0, "CASILLA GSI"), (50.0, "")]
    filas = [[c, "", ""] for c in ("1", "2", "3", "4")]
    y = _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.10)
    y -= H * 0.06
    ax.text(2.5, y, "Zonas en los 120 m, con su metraje:", ha="left", va="center",
            family=F, fontsize=NOTA * 0.85, color=MARINO)
    for _ in range(3):
        y -= H * 0.085
        _caja(ax, 2.5, y, 94.0, 0.4, GRIS)
    y -= H * 0.055
    ax.text(2.5, y, "Qué produce cada límite:", ha="left", va="center", family=F,
            fontsize=NOTA * 0.85, color=MARINO)
    y -= H * 0.075
    _caja(ax, 2.5, y, 94.0, 0.4, GRIS)
    _g(fig, "sost-s3_reparto.png")


# ═════════════════════════════════════════════ 12 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean el cuaderno de las cuatro celdas", 4, AZUL, H * 0.72),
                                ("Ubiquen la casilla GSI de cada una", 12, MARINO, H * 0.53),
                                ("Repartan las zonas y digan qué las separa", 4, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 20 minutos · se entrega el reparto de zonas",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _g(fig, "sost-s3_como-trabajamos.png")


# ══════════════════════════════════════════════ 13 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por las casillas", "las cuatro, una por una"),
                   ("Seguimos por el número de zonas", "cuántas salieron y por qué"),
                   ("Cerramos por los límites", "qué produce cada uno")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s3_puesta-comun.png")


# ═══════════════════════════════════════════════ 14 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "Las celdas 1 y 2 dieron exactamente lo mismo",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95, color=MARINO)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Por qué el límite va igual entre ellas?",
            ha="center", va="center", family=F, fontsize=CUERPO,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s3_una-ultima.png")


# ═══════════════════════════════════════════════ 15 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste frente a la fotografía",
                 "Si tuvieras que mapear ese frente,\n¿por dónde empezarías?",
                 "La próxima: de la casilla GSI\na la calidad y su banda de RMR"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.90, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s3_reflexion.png")


TODOS = [de_donde_venimos, la_celda, picota, agua_y_fecha, sin_dos_datos,
         mapeo_por_celdas, mapeo_envejece, que_es_una_zona, limites,
         cuatro_celdas, reparto, como_trabajamos, puesta_comun, una_ultima,
         reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
