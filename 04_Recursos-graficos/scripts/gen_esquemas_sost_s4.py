# -*- coding: utf-8 -*-
"""Esquemas de la sesión 4 de EOM · De la casilla GSI a la calidad y su RMR.

La matriz de la cartilla se reusa de la S3: es la misma herramienta y vive en
`planos/`. Aquí se dibuja lo que no tiene cuerpo: escalas, tablas y flujos.

Uso:  python gen_esquemas_sost_s4.py
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

CARPETA = "sost/s4/"

# las seis letras con su banda, tal como las trae la cartilla
LETRAS = [("A", "81 a 100", AZUL), ("B", "61 a 80", VERDE), ("C", "51 a 60", VERDE),
          ("D", "41 a 50", MORADO), ("E", "21 a 40", MORADO), ("F", "menos de 20", GRIS)]


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    ASP = 2.10
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for x0, titulo, txt, color in ((3.0, "LA SESIÓN PASADA",
                                    "Medir la roca y ubicar\nsu casilla en la cartilla", AZUL),
                                   (52.0, "HOY",
                                    "Qué sale de esa casilla,\ny con qué dato se pide", VERDE)):
        _redonda(ax, x0, H * 0.26, 45.0, H * 0.50, CLARO)
        _caja(ax, x0, H * 0.70, 45.0, 1.0, color)
        ax.text(x0 + 22.5, H * 0.64, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, fontweight="bold", color=color)
        ax.text(x0 + 22.5, H * 0.44, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO, linespacing=1.4)
    ax.annotate("", xy=(51.0, H * 0.51), xytext=(48.5, H * 0.51),
                arrowprops=dict(arrowstyle="->", color=MARINO, linewidth=2.0))
    _cierre(ax, H, "La casilla no es el final: es lo que devuelve la letra", H * 0.06)
    _g(fig, "sost-s4_de-donde-venimos.png")


# ══════════════════════════════════════ 2 · las letras y sus bandas
def letras_y_bandas():
    """Las seis calidades con su banda de RMR, de la mejor a la peor."""
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.85, 94.0, H * 0.085, "CALIDAD DEL MACIZO  ·  BANDA DE RMR",
              MARINO, NOTA * 0.8)
    y = H * 0.85
    for letra, banda, color in LETRAS:
        y -= H * 0.125
        _redonda(ax, 3.0, y, 94.0, H * 0.105, CLARO)
        _redonda(ax, 4.5, y + H * 0.013, 11.0, H * 0.079, color)
        ax.text(10.0, y + H * 0.0525, letra, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=BLANCO)
        ax.text(20.0, y + H * 0.0525, "RMR " + banda, ha="left", va="center", family=F,
                fontsize=NOTA * 0.9, fontweight="bold", color=MARINO)
    ax.text(50, H * 0.055, "A es la mejor roca y F la peor: la letra es lo que se lleva a la tabla",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _g(fig, "sost-s4_letras-y-bandas.png")


# ══════════════════════════════ 3 · las clases del RMR frente a las letras
def clases_vs_letras():
    """Las cinco clases romanas y las seis letras, sobre la misma escala."""
    ASP = 1.42
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    # una escala de RMR de 0 a 100 compartida por las dos filas
    x0, ancho = 6.0, 88.0

    def x_de(rmr):
        return x0 + ancho * rmr / 100.0

    clases = [("V", 0, 20, GRIS), ("IV", 21, 40, MORADO), ("III", 41, 60, AMBAR),
              ("II", 61, 80, VERDE), ("I", 81, 100, AZUL)]
    letras = [("F", 0, 20, GRIS), ("E", 21, 40, MORADO), ("D", 41, 50, AMBAR),
              ("C", 51, 60, AMBAR), ("B", 61, 80, VERDE), ("A", 81, 100, AZUL)]
    for etq, y, datos in (("CLASES DEL RMR", H * 0.60, clases),
                          ("LETRAS DE LA CARTILLA", H * 0.34, datos_letras := letras)):
        ax.text(x0, y + H * 0.155, etq, ha="left", va="center", family=F,
                fontsize=NOTA * 0.78, fontweight="bold", color=GRIS)
        for nombre, a, b, color in datos:
            _caja(ax, x_de(a), y, x_de(b) - x_de(a) - 0.4, H * 0.125, color)
            ax.text((x_de(a) + x_de(b)) / 2, y + H * 0.0625, nombre, ha="center",
                    va="center", family=F, fontsize=NOTA * 0.9,
                    fontweight="bold", color=BLANCO if color != AMBAR else MARINO)
    for rmr in (0, 20, 40, 60, 80, 100):
        ax.text(x_de(rmr), H * 0.24, str(rmr), ha="center", va="center", family=F,
                fontsize=NOTA * 0.7, color=GRIS)
    ax.plot([x_de(41), x_de(41)], [H * 0.30, H * 0.75], color=MARINO, linewidth=1.0, linestyle=":")
    ax.plot([x_de(60), x_de(60)], [H * 0.30, H * 0.75], color=MARINO, linewidth=1.0, linestyle=":")
    _cierre(ax, H, "La Clase III se parte en dos letras: C la mitad buena, D la mala", H * 0.06)
    _g(fig, "sost-s4_clases-vs-letras.png")


# ═════════════════════════════════════ 4 · dónde la cartilla afina
def cartilla_afina():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("El informe dice Clase III", "y con eso se ha pedido todo el año"),
                   ("Clase III cubre de 41 a 60 de RMR", "veinte puntos de diferencia dentro"),
                   ("La cartilla parte ese rango en C y D", "y cada letra da otra fila"),
                   ("Hay que saber en qué mitad cae", "un informe en clases no basta")],
           H * 0.72, H * 0.155)
    _cierre(ax, H, "Por eso la cartilla decide donde el informe agrupaba", H * 0.055)
    _g(fig, "sost-s4_cartilla-afina.png")


# ═════════════════════════════════════════ 5 · lo que envejece un mapeo
def vigencia():
    ASP = 1.34
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(32.0, "QUÉ PASA"), (32.0, "QUÉ LE HACE AL MAPEO"), (30.0, "¿SIGUE VALIENDO?")]
    filas = [["La labor avanza", "describe un tramo\nque quedó atrás", "no, para el frente nuevo"],
             ["Cruza una falla\no un contacto", "el macizo de hoy\nno es el de entonces", "no"],
             ["Entra agua", "cambia la condición\nsin cambiar la roca", "no del todo"],
             ["Pasan meses\nsin avanzar", "nada por sí solo", "sí, mientras nada cambie"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.145, tam=NOTA * 0.78)
    _cierre(ax, H, "Un mapeo describe la labor el día en que se hizo", H * 0.04)
    _g(fig, "sost-s4_vigencia.png")


# ═══════════════════════════════════ 6 · firmado no es lo mismo que vigente
def firmado_no_es_vigente():
    ASP = 1.90
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for x0, titulo, txt, color in ((4.0, "FIRMADO", "dice quién responde\npor lo que ahí pone", MORADO),
                                   (52.0, "VIGENTE", "dice que todavía\ndescribe la labor", VERDE)):
        _redonda(ax, x0, H * 0.34, 44.0, H * 0.40, CLARO)
        _caja(ax, x0, H * 0.685, 44.0, 1.0, color)
        ax.text(x0 + 22.0, H * 0.62, titulo, ha="center", va="center", family=F,
                fontsize=CUERPO * 0.95, fontweight="bold", color=color)
        ax.text(x0 + 22.0, H * 0.45, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO, linespacing=1.35)
    _cierre(ax, H, "La fecha del mapeo pesa tanto como la firma", H * 0.10)
    _g(fig, "sost-s4_firmado-no-es-vigente.png")


# ══════════════════════════════════════ 7 · dos fuentes que no coinciden
def dos_fuentes():
    ASP = 1.48
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Se elige, no se promedia", "el promedio de dos calidades no es una calidad"),
                   ("Gana la que describe la labor de hoy", "no la que tiene mejor firma"),
                   ("La elección se escribe y se sustenta", "con una línea, en el mismo papel"),
                   ("Lo descartado también se anota", "con su motivo, para que quede el rastro")],
           H * 0.74, H * 0.155)
    _cierre(ax, H, "Quien firma el pedido responde por el dato que usó", H * 0.05)
    _g(fig, "sost-s4_dos-fuentes.png")


# ═════════════════════════════════ 8 · mientras se regulariza la firma
def mientras_tanto():
    ASP = 1.75
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 4.0, H * 0.56, 92.0, H * 0.26, CLARO)
    ax.text(50, H * 0.69, "Se sostiene por lo más desfavorable de las dos",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            fontweight="bold", color=MARINO)
    _redonda(ax, 4.0, H * 0.26, 92.0, H * 0.24, CLARO)
    ax.text(50, H * 0.38, "El reglamento manda sostener de inmediato, no esperar el papel",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9, color=MARINO)
    ax.text(50, H * 0.16, "D.S. 024-2016-EM, art. 213", ha="center", va="center",
            family=F, fontsize=NOTA * 0.78, color=GRIS)
    _g(fig, "sost-s4_mientras-tanto.png")


# ══════════════════════════════════════════ 9 · el caso: las dos fuentes
def el_informe():
    ASP = 1.36
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(24.0, ""), (35.0, "EL INFORME DE ENERO"), (35.0, "EL MAPEO DEL MARTES")]
    filas = [["QUÉ DICE", "roca Clase III, regular", "dieciocho fracturas,\nuno o dos golpes"],
             ["QUIÉN LO FIRMA", "firmado y sellado", "nadie lo ha firmado"],
             ["DE CUÁNDO ES", "enero", "este martes"],
             ["QUÉ PASÓ EN MEDIO", "cuarenta metros de avance y el contacto con la caja piso", ""]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.13, tam=NOTA * 0.8)
    ax.text(50, H * 0.12, "El pedido de material sale mañana a primera hora",
            ha="center", va="center", family=F, fontsize=NOTA * 0.88, color=MARINO)
    _g(fig, "sost-s4_el-informe.png")


# ═══════════════════════════════════════════ 10 · el papel del pedido
def papel_del_pedido():
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    y = H * 0.86
    for rot in ("Casilla GSI del mapeo del martes:",
                "Calidad A-F y su banda de RMR:",
                "Calidad que se deduce del informe de enero:",
                "Con cuál se pide el material, y por qué:",
                "Qué se hace mientras se regulariza la firma:"):
        ax.text(3.0, y, rot, ha="left", va="center", family=F,
                fontsize=NOTA * 0.85, color=MARINO)
        _caja(ax, 3.0, y - H * 0.055, 94.0, 0.4, GRIS)
        y -= H * 0.155
    ax.text(50, H * 0.06, "Firma del equipo técnico: ____________", ha="center",
            va="center", family=F, fontsize=NOTA * 0.75, color=GRIS)
    _g(fig, "sost-s4_papel-del-pedido.png")


# ═════════════════════════════════════════════ 11 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean las dos fuentes que están sobre la mesa", 4, AZUL, H * 0.72),
                                ("Saquen la calidad de cada una, con su banda", 10, MARINO, H * 0.53),
                                ("Escriban con cuál se pide, y qué se hace mientras", 4, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.90, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 18 minutos · se entrega el papel del pedido",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _g(fig, "sost-s4_como-trabajamos.png")


# ══════════════════════════════════════════════ 12 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por la casilla del martes", "y la letra que sale de ella"),
                   ("Seguimos por la Clase III del informe", "en qué mitad de la clase cae"),
                   ("Cerramos con la decisión", "con cuál se pide, y qué se hace mientras")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s4_puesta-comun.png")


# ═══════════════════════════════════════════════ 13 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "El informe está firmado y sellado.\nEl cuaderno del martes no lo firma nadie.",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Qué hace que el cuaderno pese más?",
            ha="center", va="center", family=F, fontsize=CUERPO,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s4_una-ultima.png")


# ═══════════════════════════════════════════════ 14 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "Si mañana te dan un informe de hace\nun año, ¿qué le preguntas primero?",
                 "La próxima: la roca y la labor\ndeciden juntas el sostenimiento"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s4_reflexion.png")


# ══════════════════════════════════ 9b · lo que pasó entre enero y el martes
def lo_que_paso_en_medio():
    """Los datos del caso que explican por qué el informe pudo quedarse atrás."""
    ASP = 1.90
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    hitos = [("ENERO", "se firma el informe\ny se sella", MORADO),
             ("DESPUÉS", "cuarenta metros de avance\ny el contacto con la caja piso", GRIS),
             ("ESTE MARTES", "se mapea el mismo tramo\ny da otra cosa", VERDE)]
    x = 3.0
    for titulo, txt, color in hitos:
        _redonda(ax, x, H * 0.34, 30.0, H * 0.38, CLARO)
        _caja(ax, x, H * 0.685, 30.0, 1.0, color)
        ax.text(x + 15.0, H * 0.62, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, fontweight="bold", color=color)
        ax.text(x + 15.0, H * 0.45, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.8, color=MARINO, linespacing=1.35)
        if x < 60:
            ax.annotate("", xy=(x + 33.0, H * 0.53), xytext=(x + 30.5, H * 0.53),
                        arrowprops=dict(arrowstyle="->", color=MARINO, linewidth=1.8))
        x += 33.5
    _cierre(ax, H, "El pedido de material sale mañana a primera hora", H * 0.08)
    _g(fig, "sost-s4_lo-que-paso-en-medio.png")


TODOS = [de_donde_venimos, letras_y_bandas, clases_vs_letras, cartilla_afina,
         vigencia, firmado_no_es_vigente, dos_fuentes, mientras_tanto,
         el_informe, lo_que_paso_en_medio, papel_del_pedido, como_trabajamos, puesta_comun,
         una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
