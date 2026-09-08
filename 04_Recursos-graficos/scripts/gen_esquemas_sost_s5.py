# -*- coding: utf-8 -*-
"""Esquemas de la sesión 5 de EOM · Selección del sostenimiento.

Cierra el bloque 1 y es la que alimenta el TC1: aquí se junta todo —la calidad
que trae la roca, el tipo de labor, el ancho de minado y la temporalidad— y se
lee la fila. Y aquí se aprende también que la cartilla no cubre todo.

La matriz de la cartilla se reusa por id de la S3. Uso:  python gen_esquemas_sost_s5.py
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

CARPETA = "sost/s5/"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


def _dos_columnas(nombre, izq, der, cierre, asp=1.90, guardar_en=None):
    """Dos bloques enfrentados con su título y su texto.

    `guardar_en` existe porque otras sesiones importan este helper: sin él
    guardaba siempre en `sost/s5/`, y los esquemas de la S7 acabaron ahí con
    nombre de S7. Quien lo importe pasa su propio guardador.
    """
    fig, ax = lienzo(asp)
    H = 100 / asp
    for x0, (titulo, txt, color) in ((4.0, izq), (52.0, der)):
        _redonda(ax, x0, H * 0.34, 44.0, H * 0.40, CLARO)
        _caja(ax, x0, H * 0.685, 44.0, 1.0, color)
        ax.text(x0 + 22.0, H * 0.62, titulo, ha="center", va="center", family=F,
                fontsize=CUERPO * 0.92, fontweight="bold", color=color)
        ax.text(x0 + 22.0, H * 0.46, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.86, color=MARINO, linespacing=1.35)
    _cierre(ax, H, cierre, H * 0.10)
    (guardar_en or _g)(fig, nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    _dos_columnas("sost-s5_de-donde-venimos.png",
                  ("LO QUE YA TENEMOS", "los elementos, la casilla\ny la calidad del macizo", AZUL),
                  ("LO QUE FALTA", "que la labor también\nvota en la decisión", VERDE),
                  "La roca sola no decide: la labor vota con ella", asp=2.10)


# ══════════════════════════════════ 2 · avance frente a explotación
def avance_vs_explotacion():
    _dos_columnas("sost-s5_avance-vs-explotacion.png",
                  ("LABORES DE AVANCE", "abren camino\n\ncrucero · galería\nrampa · subnivel", AZUL),
                  ("LABORES DE EXPLOTACIÓN", "sacan mineral\n\nel tajeo", VERDE),
                  "Cada familia lee su propia tabla en la cartilla", asp=1.70)


# ═══════════════════════════════ 3 · temporal frente a permanente
def temporal_vs_permanente():
    _dos_columnas("sost-s5_temporal-vs-permanente.png",
                  ("TEMPORAL", "se cierra antes del año\n\nun crucero que muere\ncon su bloque", MORADO),
                  ("PERMANENTE", "se queda mientras\nla mina opere\n\nla galería principal,\nla cámara de bombeo", VERDE),
                  "La misma roca pide más sostenimiento si la labor se queda", asp=1.60)


# ══════════════════════════════════════════ 4 · las cuatro llaves
def cuatro_llaves():
    """Lo que hay que tener antes de buscar la fila."""
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    llaves = [("CALIDAD DEL MACIZO", "la letra que trae la casilla", AZUL),
              ("TIPO DE LABOR", "avance o explotación", VERDE),
              ("ANCHO DE MINADO", "por encima o por debajo de 2,40 m", MORADO),
              ("TEMPORALIDAD", "temporal o permanente", GRIS)]
    y = H * 0.82
    for n, (titulo, detalle, color) in enumerate(llaves, start=1):
        y -= H * 0.165
        _redonda(ax, 3.0, y, 94.0, H * 0.135, CLARO)
        _redonda(ax, 4.5, y + H * 0.018, H * 0.10, H * 0.10, color)
        ax.text(4.5 + H * 0.05, y + H * 0.068, str(n), ha="center", va="center",
                family=F, fontsize=NOTA * 0.95, fontweight="bold", color=BLANCO)
        ax.text(15.0, y + H * 0.090, titulo, ha="left", va="center", family=F,
                fontsize=NOTA * 0.88, fontweight="bold", color=MARINO)
        ax.text(15.0, y + H * 0.042, detalle, ha="left", va="center", family=F,
                fontsize=NOTA * 0.8, color=GRIS)
    _cierre(ax, H, "Las cuatro se anotan antes de buscar el sostenimiento", H * 0.05)
    _g(fig, "sost-s5_cuatro-llaves.png")


# ═════════════════════════════════════ 5 · dónde entra cada llave
def donde_entra_cada_llave():
    ASP = 1.36
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(30.0, "LA LLAVE"), (34.0, "QUÉ DECIDE EN LA CARTILLA"), (32.0, "SI FALTA")]
    filas = [["Tipo de labor", "cuál de las tablas se usa", "se lee la tabla\nde otra familia"],
             ["Ancho de minado", "qué columna dentro de\nesa tabla", "se lee la columna\nvecina"],
             ["Temporalidad", "separa las de avance\nen dos grupos", "se pide de menos\nen la permanente"],
             ["Buzamiento", "solo cuando la labor\nes un tajeo", "no aplica en avance"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.145, tam=NOTA * 0.78)
    _cierre(ax, H, "Faltando una llave, la fila que se lee es otra", H * 0.04)
    _g(fig, "sost-s5_donde-entra-cada-llave.png")


# ═════════════════════════════════ 6 · lo que devuelve la fila
def fila_devuelve():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.68, 94.0, H * 0.11, "LO QUE SE COPIA DE LA FILA", MARINO, NOTA * 0.8)
    partes = [("ELEMENTO", "cuadro de madera", AZUL),
              ("ESPACIAMIENTO", "cada 1,50 m", VERDE),
              ("REFUERZO", "con guardacabeza", MORADO)]
    x = 3.0
    for rot, val, color in partes:
        _redonda(ax, x, H * 0.42, 30.0, H * 0.22, CLARO)
        _caja(ax, x, H * 0.62, 30.0, 1.0, color)
        ax.text(x + 15.0, H * 0.565, rot, ha="center", va="center", family=F,
                fontsize=NOTA * 0.75, fontweight="bold", color=color)
        ax.text(x + 15.0, H * 0.495, val, ha="center", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO)
        x += 32.0
    ax.text(50, H * 0.31, "El espaciamiento de puntales y cuadros se mide a luz interna;\n"
                          "el del perno lo fija el estándar de la unidad",
            ha="center", va="center", family=F, fontsize=NOTA * 0.82,
            color=GRIS, linespacing=1.4)
    _cierre(ax, H, "Un sostenimiento sin espaciamiento no se pide ni se instala", H * 0.08)
    _g(fig, "sost-s5_fila-devuelve.png")


# ══════════════════════════════ 7 · el espaciamiento se copia, no se ajusta
def espaciamiento_se_copia():
    ASP = 1.70
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("La fila da el espaciamiento", "y ese número no es del que instala"),
                   ("Se copia tal como está", "sin redondear y sin ajustar en la labor"),
                   ("De ahí salen las cantidades", "es lo que convierte metros en pernos")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Ese número es el que después convierte metros en cantidades", H * 0.06)
    _g(fig, "sost-s5_espaciamiento-se-copia.png")


# ═════════════════════════════════════ 8 · lo que la tabla no cubre
def fuera_de_la_tabla():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("La cartilla no cubre todas las labores", "cubre avance y explotación"),
                   ("En una intersección remite a otro estándar", "ahí se cruzan dos secciones y la luz crece"),
                   ("Reconocerlo es parte del trabajo", "no es un fallo de la tabla"),
                   ("Lo que no resuelve se consulta", "no se inventa una fila parecida")],
           H * 0.74, H * 0.155)
    _cierre(ax, H, "La cartilla dice cuándo no alcanza: eso también es leerla", H * 0.05)
    _g(fig, "sost-s5_fuera-de-la-tabla.png")


# ════════════════════════════════════ 9 · las labores de infraestructura
def infraestructura():
    ASP = 1.42
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.82, 94.0, H * 0.09,
              "LLEVAN ESTÁNDAR PROPIO, NO FILA DE LA CARTILLA", MARINO, NOTA * 0.78)
    items = [("Polvorines", MORADO), ("Refugios mineros", MORADO), ("Comedores", MORADO),
             ("Cámara de bombeo", VERDE), ("Subestaciones", VERDE), ("Cámaras de izaje", VERDE)]
    y = H * 0.82
    for k in range(0, len(items), 2):
        y -= H * 0.135
        for j, (txt, color) in enumerate(items[k:k + 2]):
            x = 3.0 + j * 48.0
            _redonda(ax, x, y, 46.0, H * 0.115, CLARO)
            _caja(ax, x, y, 1.4, H * 0.115, color)
            ax.text(x + 6.0, y + H * 0.0575, txt, ha="left", va="center", family=F,
                    fontsize=NOTA * 0.9, color=MARINO)
    ax.text(50, H * 0.29, "No son de avance ni de explotación: son infraestructura",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "Notas 6 y 7 de la cartilla: se sostienen según estudio geomecánico", H * 0.07)
    _g(fig, "sost-s5_infraestructura.png")


# ══════════════════════════════════════ 10 · el mapeo, común a las cuatro
def mapeo_comun():
    ASP = 1.95
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    datos = [("12", "fracturas por m²", AZUL), ("2.º", "golpe de picota", MORADO),
             ("—", "sin agua", GRIS)]
    x = 5.0
    for valor, etq, color in datos:
        _redonda(ax, x, H * 0.38, 29.0, H * 0.34, CLARO)
        _caja(ax, x, H * 0.685, 29.0, 1.0, color)
        ax.text(x + 14.5, H * 0.585, valor, ha="center", va="center", family=F,
                fontsize=CUERPO * 1.25, fontweight="bold", color=MARINO)
        ax.text(x + 14.5, H * 0.455, etq, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, color=GRIS)
        x += 31.0
    ax.text(50, H * 0.26, "El mapeo de la semana dio lo mismo en las cuatro labores",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9, color=MARINO)
    _cierre(ax, H, "Misma roca. Y aun así, cuatro respuestas distintas", H * 0.06)
    _g(fig, "sost-s5_mapeo-comun.png")


# ═══════════════════════════════════════════ 11 · las cuatro labores
def cuatro_labores():
    ASP = 1.34
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(24.0, "LABOR"), (24.0, "SECCIÓN"), (24.0, "SE QUEDA"), (24.0, "QUIÉN ENTRA")]
    filas = [["Crucero", "3,50 × 3,50", "hasta que termine\nel bloque", "la cuadrilla"],
             ["Galería principal", "4,00 × 4,00", "mientras la\nmina opere", "todo el mineral\ndel nivel"],
             ["Tajeo", "2,00 de ancho,\nveta parada", "hasta agotar\nel corte", "la cuadrilla"],
             ["Cámara de bombeo", "con la bomba\nadentro", "mientras la\nmina opere", "mantenimiento,\ncada semana"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.80, H * 0.085, H * 0.145, tam=NOTA * 0.75)
    ax.text(50, H * 0.075, "«Es la misma roca en las cuatro, pongan lo mismo y terminamos»",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _g(fig, "sost-s5_cuatro-labores.png")


# ══════════════════════════════════════════════ 12 · el cuadro que se llena
def cuadro_encargo():
    ASP = 1.32
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    # la cabecera larga se salia del lienzo: se parte en dos lineas y se
    # estrechan las demas columnas para que las cinco quepan en el ancho
    cols = [(20.0, "LABOR"), (13.0, "TIPO"), (15.0, "ANCHO"),
            (18.0, "TEMPORALIDAD"), (28.0, "SOSTENIMIENTO\nY ESPACIAMIENTO")]
    filas = [[l, "", "", "", ""] for l in ("Crucero", "Galería principal", "Tajeo", "Cámara de bombeo")]
    y = _tabla(ax, H, 1.0, cols, filas, H * 0.78, H * 0.105, H * 0.115,
               tam_cab=NOTA * 0.62, tam=NOTA * 0.75)
    y -= H * 0.07
    ax.text(2.0, y, "Marca con asterisco la que no sale de la tabla, y escribe qué le falta:",
            ha="left", va="center", family=F, fontsize=NOTA * 0.82, color=MARINO)
    y -= H * 0.06
    _caja(ax, 2.0, y, 96.0, 0.4, GRIS)
    _g(fig, "sost-s5_cuadro-encargo.png")


# ═════════════════════════════════════════════ 13 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Anoten las cuatro llaves de cada labor", 5, AZUL, H * 0.72),
                                ("Busquen la fila y copien lo que devuelve", 11, MARINO, H * 0.53),
                                ("Marquen la que no sale de la tabla", 4, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 20 minutos · se entrega el cuadro de las cuatro labores",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _g(fig, "sost-s5_como-trabajamos.png")


# ══════════════════════════════════════════════ 14 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por el crucero y la galería", "misma roca, distinta temporalidad"),
                   ("Seguimos por el tajeo", "otra tabla, y entra el buzamiento"),
                   ("Cerramos por la cámara de bombeo", "la que no sale de la tabla")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s5_puesta-comun.png")


# ═══════════════════════════════════════════════ 15 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "La misma roca dio cuatro respuestas distintas",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95, color=MARINO)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Qué las separó?", ha="center", va="center", family=F,
            fontsize=CUERPO * 1.1, fontweight="bold", color=MARINO)
    _g(fig, "sost-s5_una-ultima.png")


# ═══════════════════════════════════════════════ 16 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "De las cuatro llaves, ¿cuál se te\nolvidaría con más facilidad?",
                 "La próxima sesión: el trabajo\ncolaborativo del bloque"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.90, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s5_reflexion.png")


TODOS = [de_donde_venimos, avance_vs_explotacion, temporal_vs_permanente,
         cuatro_llaves, donde_entra_cada_llave, fila_devuelve,
         espaciamiento_se_copia, fuera_de_la_tabla, infraestructura,
         mapeo_comun, cuatro_labores, cuadro_encargo, como_trabajamos,
         puesta_comun, una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
