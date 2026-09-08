# -*- coding: utf-8 -*-
"""Esquemas de la sesión 2 de EOM · Sostenimiento pasivo.

Son los que se dibujan. Los siete elementos con cuerpo —malla, shotcrete,
cuadro y cimbra— salen de la tesis de La Libertad y viven en `planos/`.

La ruta de la sesión NO se rehace: la S1 y la S2 tienen el mismo reparto de
minutos, así que comparten `sost/comun/sost_ruta.png`.

Métrica del §11: lienzo de 1500 px de ancho, cuerpo de 52 px, sin bbox_inches.
Van SIN título dentro: el título lo pone la lámina.

Uso:  python gen_esquemas_sost_s2.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, guardar, lienzo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402
from gen_esquemas_sost_s1 import _cabecera  # noqa: E402

CARPETA = "sost/s2/"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


# ─────────────────────────────────────────── piezas que se repiten
def _tabla(ax, H, x0, cols, filas, y_cab, alto_cab, alto_fila, hueco=1.0,
           color_cab=MARINO, tam_cab=None, tam=None):
    """Cabeceras + filas. cols es [(ancho, titulo)] y filas es [[celda, ...]]."""
    x = x0
    for w, titulo in cols:
        if titulo:                      # la columna de rotulos no lleva cabecera:
            _cabecera(ax, x, y_cab, w, alto_cab, titulo, color_cab, tam_cab or NOTA * 0.78)
        x += w + hueco                  # una caja oscura vacia solo hace ruido
    y = y_cab
    for fila in filas:
        y -= alto_fila + hueco
        x = x0
        for (w, _), txt in zip(cols, fila):
            _celda(ax, x, y, w, alto_fila, txt, CLARO, MARINO, tam=tam or NOTA * 0.85)
            x += w + hueco
    return y


def _pasos(ax, H, pasos, y0, alto, color=AZUL, ancho=94.0, x0=3.0):
    """Lista numerada de pasos, cada uno con su circulo."""
    y = y0
    for n, (titulo, detalle) in enumerate(pasos, start=1):
        _redonda(ax, x0, y, ancho, alto, CLARO)
        _redonda(ax, x0 + 1.6, y + alto * 0.22, alto * 0.55, alto * 0.55, color)
        ax.text(x0 + 1.6 + alto * 0.275, y + alto * 0.495, str(n), ha="center",
                va="center", family=F, fontsize=NOTA * 0.95, fontweight="bold", color=BLANCO)
        ax.text(x0 + 13.0, y + alto * (0.66 if detalle else 0.5), titulo, ha="left",
                va="center", family=F, fontsize=NOTA * 0.92, fontweight="bold", color=MARINO)
        if detalle:
            ax.text(x0 + 13.0, y + alto * 0.28, detalle, ha="left", va="center",
                    family=F, fontsize=NOTA * 0.82, color=GRIS)
        y -= alto + H * 0.025
    return y


def _cierre(ax, H, texto, y=None):
    """La franja ámbar del final, con la idea que se lleva la lámina."""
    y = H * 0.05 if y is None else y
    _redonda(ax, 6.0, y, 88.0, H * 0.10, AMBAR)
    ax.text(50, y + H * 0.05, texto, ha="center", va="center", family=F,
            fontsize=NOTA * 0.9, fontweight="bold", color=MARINO)


# ══════════════════════════════════════════ 0 · ruta compartida S1 y S2
def ruta_comun():
    """Los cinco momentos con sus minutos. La misma en la S1 y en la S2."""
    ASP = 2.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    momentos = [("CONEXIÓN", 20, AZUL), ("ADQUISICIÓN", 45, MARINO),
                ("APLICACIÓN", 40, VERDE), ("DISCUSIÓN", 20, MORADO),
                ("REFLEXIÓN", 10, GRIS)]
    total = sum(m[1] for m in momentos)
    x, margen, hueco = 3.0, 3.0, 1.0
    util = 100 - 2 * margen - hueco * (len(momentos) - 1)
    for nombre, mins, color in momentos:
        w = util * mins / total
        _redonda(ax, x, H * 0.34, w, H * 0.34, color)
        ax.text(x + w / 2, H * 0.51, nombre, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, H * 0.22, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, color=GRIS)
        x += w + hueco
    ax.text(50, H * 0.86, "135 minutos", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=MARINO)
    guardar(fig, "sost/comun/sost_ruta.png")


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    ASP = 2.10
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for x0, titulo, txt, color in ((3.0, "LA SESIÓN PASADA",
                                    "El refuerzo: pernos y cable,\nlo que entra al taladro", AZUL),
                                   (52.0, "HOY",
                                    "El soporte: malla, shotcrete,\ncuadros y cimbras", VERDE)):
        _redonda(ax, x0, H * 0.26, 45.0, H * 0.50, CLARO)
        _caja(ax, x0, H * 0.70, 45.0, 1.0, color)
        ax.text(x0 + 22.5, H * 0.64, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, fontweight="bold", color=color)
        ax.text(x0 + 22.5, H * 0.44, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO, linespacing=1.4)
    ax.annotate("", xy=(51.0, H * 0.51), xytext=(48.5, H * 0.51),
                arrowprops=dict(arrowstyle="->", color=MARINO, linewidth=2.0))
    _cierre(ax, H, "Casi toda labor lleva los dos, y en ese orden", H * 0.06)
    _g(fig, "sost-s2_de-donde-venimos.png")


# ═════════════════════════════════════ 2 · qué prefiere la cartilla
def cartilla_prefiere():
    ASP = 1.34
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(30.0, "CONDICIÓN DE LA ROCA"), (32.0, "SOPORTE QUE APARECE"), (33.0, "POR QUÉ")]
    filas = [["Buena", "Poco o nada", "la roca se sostiene\ncasi sola"],
             ["Regular", "Malla sobre el perno", "retiene lo que se\nsuelta entre pernos"],
             ["Mala", "Shotcrete sumado\nal perno y la malla", "sella la superficie\nya fracturada"],
             ["Muy mala", "Cuadro de madera\no cimbra", "la roca ya no\nse sostiene sola"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.78, H * 0.09, H * 0.135, tam=NOTA * 0.8)
    _cierre(ax, H, "El shotcrete se suma al perno y la malla, no los reemplaza")
    _g(fig, "sost-s2_cartilla-prefiere.png")


# ══════════════════════════════ 3 · una fila trae elemento y espaciamiento
def fila_completa():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.66, 94.0, H * 0.11,
              "LO QUE DEVUELVE UNA FILA DE LA CARTILLA", MARINO, NOTA * 0.8)
    partes = [("ELEMENTO", "Cuadro de madera", AZUL),
              ("ESPACIAMIENTO", "cada 1,50 m", VERDE),
              ("REFUERZO", "con guardacabeza", MORADO)]
    x = 3.0
    for rot, val, color in partes:
        _redonda(ax, x, H * 0.40, 30.0, H * 0.22, CLARO)
        _caja(ax, x, H * 0.60, 30.0, 1.0, color)
        ax.text(x + 15.0, H * 0.545, rot, ha="center", va="center", family=F,
                fontsize=NOTA * 0.75, fontweight="bold", color=color)
        ax.text(x + 15.0, H * 0.475, val, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO)
        x += 32.0
    ax.text(50, H * 0.29, "Los tres se copian juntos, tal como están",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9, color=GRIS)
    _cierre(ax, H, "Un elemento sin su espaciamiento es media instrucción", H * 0.10)
    _g(fig, "sost-s2_fila-completa.png")


# ═══════════════════════════════════ 4 · firme no es lo mismo que conforme
def firme_vs_estandar():
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(24.0, ""), (35.0, "«QUEDÓ FIRME»"), (35.0, "CUMPLE EL ESTÁNDAR")]
    filas = [["QUIÉN LO DICE", "el que instaló", "el parte, contra la fila"],
             ["CON QUÉ", "la sensación de la mano", "espaciamiento y\nespecificación medidos"],
             ["CUÁNTO DURA", "lo que aguante hoy", "lo que la labor necesita"],
             ["SE PUEDE RECIBIR", "no", "sí, si está anotado"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.125, tam=NOTA * 0.82)
    _cierre(ax, H, "Firme hoy no dice nada de cómo estará dentro de un año")
    _g(fig, "sost-s2_firme-vs-estandar.png")


# ═════════════════════════════════════════════ 5 · cómo se recibe un tramo
def recepcion():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Se lee la fila que le toca a esa labor", "calidad, tipo y ancho de minado"),
                   ("Se compara con lo que dice el parte", "elemento, especificación y espaciamiento"),
                   ("Lo que no cumple se anota no conforme", "no se discute con quien instaló"),
                   ("Sin espaciamiento anotado, no se recibe", "el parte es la prueba de lo que se puso")],
           H * 0.70, H * 0.155)
    _cierre(ax, H, "Recibir mal un tramo lo deja fuera de control para siempre", H * 0.055)
    _g(fig, "sost-s2_recepcion.png")


# ══════════════════════════════════════════════ 6 · los cuatro tramos
def cuatro_tramos():
    ASP = 1.36
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(14.0, "TRAMO"), (40.0, "LO QUE SE INSTALÓ"), (41.0, "LO QUE ANOTÓ EL PARTE")]
    filas = [["1", "Malla sobre pernos ya puestos", "traslape de una cocada"],
             ["2", "Concreto proyectado", "espesor de 2 pulgadas, sin fibra"],
             ["3", "Cuadros de madera", "cada 1,50 m, con guardacabeza"],
             ["4", "Arcos de acero", "cada 1,50 m"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.76, H * 0.09, H * 0.125, tam=NOTA * 0.82)
    ax.text(50, H * 0.155, "«Ese último lo armó el turno de noche, y quedó igual de firme»",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    ax.text(50, H * 0.09, "La valorización del contratista entra el lunes",
            ha="center", va="center", family=F, fontsize=NOTA * 0.8, color=GRIS)
    _g(fig, "sost-s2_cuatro-tramos.png")


# ═══════════════════════════════════════ 7 · el cuaderno de instalación
def cuaderno():
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    # la ultima cabecera tocaba el borde del lienzo: se estrechan las columnas
    cols = [(10.0, "TRAMO"), (23.0, "ELEMENTO"), (22.0, "ESPECIFICACIÓN"),
            (17.0, "ESPACIAMIENTO"), (18.0, "¿CORRESPONDE?")]
    filas = [[t, "", "", "", ""] for t in ("1", "2", "3", "4")]
    y = _tabla(ax, H, 2.0, cols, filas, H * 0.78, H * 0.085, H * 0.11, tam_cab=NOTA * 0.62)
    y -= H * 0.08
    for txt in ("Qué falta en cada uno:",
                "Cuál no se recibe, y qué tiene que pasar para recibirlo:"):
        ax.text(2.5, y, txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.82, color=MARINO)
        _caja(ax, 2.5, y - H * 0.045, 94.0, 0.4, GRIS)
        y -= H * 0.115
    _g(fig, "sost-s2_cuaderno.png")


# ═════════════════════════════════════════════ 8 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    pasos = [("Lean el cuaderno de los cuatro tramos", 4, AZUL),
             ("Llenen la fila de cada tramo contra la cartilla", 10, MARINO),
             ("Escriban cuál no se recibe, y por qué", 4, VERDE)]
    y = H * 0.72
    for txt, mins, color in pasos:
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
        y -= H * 0.19
    ax.text(50, H * 0.10, "En parejas · 18 minutos · se entrega el cuaderno cerrado",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _g(fig, "sost-s2_como-trabajamos.png")


# ═══════════════════════════════════════════════ 9 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por el cuarto tramo", "qué anotaron y si lo reciben"),
                   ("Seguimos por el segundo", "el shotcrete sin fibra, ¿corresponde?"),
                   ("Cerramos con el primero y el tercero", "los que sí cumplen, y en qué se nota")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s2_puesta-comun.png")


# ══════════════════════════════════════════════ 10 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "«Quedó igual de firme que los cuadros,\nasí que no le den vueltas»",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Por qué eso no es un criterio de recepción?",
            ha="center", va="center", family=F, fontsize=CUERPO,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s2_una-ultima.png")


# ═══════════════════════════════════════════════ 11 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["De los cuatro elementos de hoy,\n¿cuál lleva espaciamiento y cuál no?",
                 "¿Qué tendrías que ver en un parte\npara recibir un tramo sin dudar?",
                 "La próxima: cómo se mide la roca\ny hasta dónde llega una zona"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.90, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s2_reflexion.png")


TODOS = [ruta_comun, de_donde_venimos, cartilla_prefiere, fila_completa,
         firme_vs_estandar, recepcion, cuatro_tramos, cuaderno, como_trabajamos,
         puesta_comun, una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas (uno de ellos en sost/comun/)" % len(TODOS))


if __name__ == "__main__":
    main()
