# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 de EOM · Fundamentos mecánicos de equipos mineros.

Son los DIECIOCHO que se dibujan. La S1 no pide ninguna imagen con cuerpo: no
hay corte de transmisión ni despiece de convertidor —eso sería inventar
geometría (regla 3)—. La cadena del tren de potencia va como SECUENCIA DE
BLOQUES NOMBRADOS, que es un flujo, y los flujos sí se dibujan.

Lo único físico de la sesión es el estímulo de Conexión, y ahí se reusa una
fotografía real que ya está aprobada: IMG-EOM-SCOOP-CARGANDO.

CARPETA. Los esquemas de EOM se ordenan por curso y luego por sesión. Este
curso es el tercero de la carrera, así que va a `fmeq/s1/`.

Métrica del §11: lienzo de 1500 px de ancho, cuerpo de 52 px, sin bbox_inches.
Van SIN título dentro: el título lo pone la lámina.

Uso:  python gen_esquemas_fmeq_s1.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, cuerpo, guardar, lienzo, nota, rotulo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402

CARPETA = "fmeq/s1/"


def _guardar(fig, nombre):
    guardar(fig, CARPETA + nombre)


def _cabecera(ax, x, y, w, h, txt, color, tam=None):
    _caja(ax, x, y, w, h, color)
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", family=F,
            fontsize=tam or NOTA * 0.92, fontweight="bold", color=BLANCO)


def _flecha_abajo(ax, x, y, alto=2.4, color=GRIS):
    ax.annotate("", xy=(x, y - alto), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=2.4))


def _flecha_der(ax, x, y, largo=4.0, color=GRIS):
    ax.annotate("", xy=(x + largo, y), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=2.4))


def _banda(ax, y, alto, texto, x0=3.0, ancho=94.0, color=AMBAR, tinta=MARINO):
    """La idea que hay que llevarse, al pie del esquema."""
    _redonda(ax, x0, y, ancho, alto, color)
    ax.text(x0 + ancho / 2, y + alto / 2, texto, ha="center", va="center",
            family=F, fontsize=NOTA, fontweight="bold", color=tinta)


# ═══════════════════════════════════════════ 1 · el curso en una lámina
def curso_bloques():
    """Los dos bloques con sus sesiones y el colaborativo que cierra cada uno."""
    ASP = 1.30
    fig, ax = lienzo(ASP)

    bloques = [
        (66, 50, AZUL, "BLOQUE 1", "Equipos de mina subterránea",
         ["S1", "S2", "S3", "S4", "S5"], "TC1"),
        (38, 22, MORADO, "BLOQUE 2", "Equipos de minería superficial",
         ["S7", "S8", "S9", "S10", "S11"], "TC2"),
    ]
    for y_tit, y, color, nombre, tema, sesiones, tc in bloques:
        ax.text(5, y_tit, nombre, ha="left", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=color)
        ax.text(26, y_tit, tema, ha="left", va="center", family=F,
                fontsize=NOTA, color=MARINO)
        x = 5
        for s in sesiones:
            _redonda(ax, x, y, 12.5, 12, color)
            ax.text(x + 6.25, y + 6, s, ha="center", va="center", family=F,
                    fontsize=CUERPO, fontweight="bold", color=BLANCO)
            x += 14.5
        _redonda(ax, x + 3, y, 15, 12, AMBAR)
        ax.text(x + 10.5, y + 6, tc, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=MARINO)

    ax.text(50, 10, "Cada bloque cierra con un trabajo colaborativo\n"
                    "que vale el 25 % de la nota.", ha="center", va="center",
            family=F, fontsize=CUERPO, color=MARINO, linespacing=1.35)
    nota(ax, 3, "Doce sesiones · 48 horas · 2 créditos.")
    _guardar(fig, "fmeq-s1_curso-bloques.png")


# ═══════════════════════════════════════════ 2 · ruta de la sesión
def ruta():
    """Los cinco momentos con sus minutos: 20 · 45 · 40 · 20 · 10."""
    ASP = 2.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    momentos = [("CONEXIÓN", 20, AZUL), ("ADQUISICIÓN", 45, MARINO),
                ("APLICACIÓN", 40, VERDE), ("DISCUSIÓN", 20, MORADO),
                ("REFLEXIÓN", 10, GRIS)]
    # Las cajas van IGUALES y la proporción del tiempo se cuenta en la barra de
    # abajo. Con cajas proporcionales, «REFLEXIÓN» —diez minutos— recibía una
    # caja de seis unidades y el rótulo se salía por los dos lados.
    total = sum(m[1] for m in momentos)
    margen, hueco = 3.0, 1.2
    w = (100 - 2 * margen - hueco * (len(momentos) - 1)) / len(momentos)
    x = margen
    for nombre, mins, color in momentos:
        _redonda(ax, x, H * 0.40, w, H * 0.30, color)
        ax.text(x + w / 2, H * 0.585, nombre, ha="center", va="center", family=F,
                fontsize=NOTA * 0.80, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, H * 0.470, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA * 0.80, color=BLANCO)
        x += w + hueco
    x = margen
    for nombre, mins, color in momentos:
        ancho = (100 - 2 * margen) * mins / total
        _caja(ax, x, H * 0.20, ancho, H * 0.10, color)
        x += ancho
    ax.text(50, H * 0.85, "135 minutos", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=MARINO)
    nota(ax, H * 0.09, "La barra muestra cuánto pesa cada momento.")
    # La ruta es la MISMA en las diez sesiones —20·45·40·20·10—, así que vive en
    # comun/ y no se redibuja por sesión. Ver la válvula del CLAUDE.md.
    guardar(fig, "fmeq/comun/fmeq_ruta.png")


# ═══════════════════════════════════════════ 3 · la cadena de la fuerza
def cadena():
    """Los eslabones en orden, del motor a la rueda. Es un flujo, no un corte."""
    ASP = 1.02
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    eslabones = [("MOTOR", AZUL), ("CONVERTIDOR DE PAR", AZUL),
                 ("TRANSMISIÓN", MARINO), ("ÁRBOL DE TRANSMISIÓN", MARINO),
                 ("DIFERENCIAL", VERDE), ("MANDOS FINALES", VERDE)]
    # Siete cajas y su nota al pie tienen que caber en el alto: se reparte el
    # espacio ANTES de trazar. La primera versión dejaba «LA RUEDA» fuera del
    # lienzo, encima de la nota y cortada por abajo.
    y_nota = H * 0.045
    disponible = H * 0.94 - y_nota
    alto = disponible / (len(eslabones) + 1) * 0.74
    hueco = disponible / (len(eslabones) + 1) * 0.26
    y = H * 0.94 - alto
    for i, (nombre, color) in enumerate(eslabones):
        _redonda(ax, 12, y, 76, alto, color)
        ax.text(50, y + alto / 2, nombre, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=BLANCO)
        ax.text(7, y + alto / 2, str(i + 1), ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=GRIS)
        _flecha_abajo(ax, 50, y - hueco * 0.2, hueco * 0.6)
        y -= alto + hueco
    _redonda(ax, 26, y, 48, alto, AMBAR)
    ax.text(50, y + alto / 2, "LA RUEDA", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=MARINO)
    nota(ax, y_nota * 0.55, "Cada eslabón recibe de uno y entrega al siguiente.")
    _guardar(fig, "fmeq-s1_cadena.png")


# ═══════════════════════════════════════════ 4 · del motor al convertidor
def motor_convertidor():
    """Qué entrega el motor y qué le hace el convertidor cuando arranca cargado."""
    ASP = 1.20
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 4, H * 0.60, 26, H * 0.22, AZUL)
    ax.text(17, H * 0.71, "MOTOR", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=BLANCO)
    _flecha_der(ax, 31, H * 0.71, 6.5)
    _redonda(ax, 39, H * 0.60, 34, H * 0.22, VERDE)
    ax.text(56, H * 0.74, "CONVERTIDOR", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=BLANCO)
    ax.text(56, H * 0.66, "DE PAR", ha="center", va="center", family=F,
            fontsize=CUERPO, fontweight="bold", color=BLANCO)
    _flecha_der(ax, 74, H * 0.71, 6.5)
    _redonda(ax, 82, H * 0.60, 14, H * 0.22, CLARO)
    ax.text(89, H * 0.71, "sigue", ha="center", va="center", family=F,
            fontsize=NOTA, color=GRIS)

    ax.text(17, H * 0.50, "entrega giro\ny par", ha="center", va="center",
            family=F, fontsize=NOTA, color=MARINO, linespacing=1.35)
    ax.text(56, H * 0.50, "acopla sin embrague mecánico\ny multiplica el par al arrancar",
            ha="center", va="center", family=F, fontsize=NOTA, color=MARINO,
            linespacing=1.35)

    filas = [("EL MOTOR", "gira siempre, aunque el equipo esté detenido"),
             ("EL ACEITE", "es lo que transmite el giro entre los dos"),
             ("AL ARRANCAR CARGADO", "el convertidor entrega más par que el que recibe")]
    y = H * 0.34
    for rot, det in filas:
        _celda(ax, 4, y, 30, H * 0.095, rot, CLARO, GRIS, negrita=True, tam=NOTA * 0.82)
        _celda(ax, 35, y, 61, H * 0.095, det, BLANCO, MARINO, tam=NOTA * 0.88)
        y -= H * 0.115
    _banda(ax, H * 0.035, H * 0.085, "Multiplicar par es dar más fuerza y menos vueltas")
    _guardar(fig, "fmeq-s1_motor-convertidor.png")


# ═══════════════════════════════════════════ 5 · del árbol a la rueda
def arbol_rueda():
    """Árbol, diferencial y mandos finales: qué reparte y qué reduce cada uno."""
    ASP = 1.12
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    piezas = [("ÁRBOL DE\nTRANSMISIÓN", MARINO, "traslada el giro\nhasta el eje"),
              ("DIFERENCIAL", VERDE, "reparte el giro entre\nlas dos ruedas"),
              ("MANDOS\nFINALES", MORADO, "última reducción,\njusto en la rueda")]
    x = 4
    for nombre, color, det in piezas:
        _redonda(ax, x, H * 0.56, 29, H * 0.26, color)
        ax.text(x + 14.5, H * 0.69, nombre, ha="center", va="center", family=F,
                fontsize=NOTA * 1.02, fontweight="bold", color=BLANCO,
                linespacing=1.3)
        ax.text(x + 14.5, H * 0.475, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.9, color=MARINO, linespacing=1.35)
        if x < 60:
            _flecha_der(ax, x + 30, H * 0.69, 2.4)
        x += 33.5

    ax.text(50, H * 0.35, "Por qué hace falta el diferencial", ha="center",
            va="center", family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    _celda(ax, 8, H * 0.20, 38, H * 0.11, "en curva, la rueda de afuera\nrecorre más camino",
           CLARO, MARINO, tam=NOTA * 0.88)
    _celda(ax, 54, H * 0.20, 38, H * 0.11, "el diferencial deja que una\ngire más que la otra",
           CLARO, MARINO, tam=NOTA * 0.88)
    _banda(ax, H * 0.045, H * 0.085, "La fuerza que llega al piso es la del último eslabón")
    _guardar(fig, "fmeq-s1_arbol-rueda.png")


# ═══════════════════════════════════════════ 6 · par y vueltas
def par_vueltas():
    """Lo que se gana de un lado se pierde del otro."""
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 5, H * 0.56, 41, H * 0.30, AZUL)
    ax.text(25.5, H * 0.775, "PAR", ha="center", va="center", family=F,
            fontsize=FUERTE * 1.15, fontweight="bold", color=BLANCO)
    ax.text(25.5, H * 0.655, "la fuerza con que gira", ha="center", va="center",
            family=F, fontsize=NOTA, color=BLANCO)
    _redonda(ax, 54, H * 0.56, 41, H * 0.30, VERDE)
    ax.text(74.5, H * 0.775, "VUELTAS", ha="center", va="center", family=F,
            fontsize=FUERTE * 1.15, fontweight="bold", color=BLANCO)
    ax.text(74.5, H * 0.655, "la velocidad con que gira", ha="center",
            va="center", family=F, fontsize=NOTA, color=BLANCO)

    ax.annotate("", xy=(53, H * 0.71), xytext=(47, H * 0.71),
                arrowprops=dict(arrowstyle="<|-|>", color=GRIS, linewidth=2.6))
    ax.text(50, H * 0.44, "Un eslabón que multiplica el par\nbaja las vueltas en la misma medida",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)
    _banda(ax, H * 0.10, H * 0.13, "Más fuerza y menos velocidad. No se gana de los dos lados")
    _guardar(fig, "fmeq-s1_par-vueltas.png")


# ═══════════════════════════════════════════ 7 · marcha corta y larga
def marchas():
    """Comparativa: qué da cada marcha y dónde se usa."""
    ASP = 1.22
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    x0, w_rot, w_col, sep = 2.0, 24.0, 35.0, 1.0
    y = H * 0.78
    _cabecera(ax, x0 + w_rot, y, w_col, H * 0.115, "MARCHA CORTA", AZUL)
    _cabecera(ax, x0 + w_rot + w_col + sep, y, w_col, H * 0.115, "MARCHA LARGA", VERDE)
    filas = [("FUERZA", "mucha", "poca"),
             ("VELOCIDAD", "poca", "mucha"),
             ("DÓNDE SE USA", "rampa arriba\ny cargado", "plano\ny vacío"),
             ("QUIÉN LA ELIGE", "la transmisión, según\nla marcha puesta",
              "la transmisión, según\nla marcha puesta")]
    alto = H * 0.145
    for rot, a, b in filas:
        y -= alto + 0.8
        _celda(ax, x0, y, w_rot, alto, rot, BLANCO, GRIS, negrita=True, tam=NOTA * 0.82)
        _celda(ax, x0 + w_rot, y, w_col, alto, a, CLARO, MARINO, tam=NOTA * 0.92)
        _celda(ax, x0 + w_rot + w_col + sep, y, w_col, alto, b, CLARO, MARINO,
               tam=NOTA * 0.92)
    _banda(ax, H * 0.04, H * 0.085,
           "La transmisión elige la relación entre giro y fuerza")
    _guardar(fig, "fmeq-s1_marchas.png")


# ═══════════════════════════════════════════ 8 · el último eslabón
def ultimo_eslabon():
    """Lo que cada eslabón entrega al siguiente, y qué pasa si uno patina."""
    ASP = 1.35
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    ax.text(50, H * 0.90, "Lo que llega a la rueda", ha="center", va="center",
            family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    barras = [("MOTOR", 88, AZUL), ("CONVERTIDOR", 84, AZUL),
              ("TRANSMISIÓN", 80, MARINO), ("ÁRBOL", 78, MARINO),
              ("DIFERENCIAL", 75, VERDE), ("MANDOS FINALES", 72, VERDE)]
    # Las barras, el cuadro explicativo y la banda se reparten el alto por
    # tramos fijos. Encadenando restas, el cuadro caía encima de la banda.
    y = H * 0.80
    alto = H * 0.065
    for nombre, largo, color in barras:
        _celda(ax, 3, y, 27, alto, nombre, BLANCO, GRIS, negrita=True, tam=NOTA * 0.8)
        _redonda(ax, 31, y, largo * 0.66, alto, color)
        y -= alto + H * 0.018

    _redonda(ax, 3, H * 0.155, 94, H * 0.135, CLARO)
    ax.text(50, H * 0.2225, "Si un eslabón patina, entrega menos de lo que recibió\n"
                            "y todos los de abajo trabajan con menos",
            ha="center", va="center", family=F, fontsize=NOTA, color=MARINO,
            linespacing=1.35)
    _banda(ax, H * 0.03, H * 0.09, "El piso solo recibe lo que entrega el último")
    _guardar(fig, "fmeq-s1_ultimo-eslabon.png")


# ═══════════════════════════════════════════ 9 · qué hace el motor
def sintoma_motor():
    """Las tres descripciones posibles y qué dice cada una."""
    ASP = 1.06
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    ax.text(50, H * 0.93, "¿Qué hace el motor mientras el equipo no avanza?",
            ha="center", va="center", family=F, fontsize=CUERPO,
            fontweight="bold", color=MARINO)
    fichas = [("SE AHOGA\nO SE APAGA", MORADO, "el motor está\ncomprometido",
               "la revisión\nempieza en él"),
              ("MANTIENE\nLAS VUELTAS", AZUL, "el motor está\nentregando",
               "la pérdida está\nmás abajo"),
              ("SUBE\nLAS VUELTAS", VERDE, "el motor gira libre:\nno encuentra carga",
               "la pérdida está\nmás abajo")]
    x = 3
    for titulo, color, lectura, donde in fichas:
        _redonda(ax, x, H * 0.40, 30.5, H * 0.45, CLARO)
        _redonda(ax, x, H * 0.72, 30.5, H * 0.13, color)
        ax.text(x + 15.25, H * 0.785, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.92, fontweight="bold", color=BLANCO,
                linespacing=1.3)
        ax.text(x + 15.25, H * 0.635, lectura, ha="center", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO, linespacing=1.35)
        ax.text(x + 15.25, H * 0.485, donde, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, color=GRIS, linespacing=1.35)
        x += 32.2
    _banda(ax, H * 0.10, H * 0.115,
           "El síntoma se describe primero. Interpretarlo viene después")
    _guardar(fig, "fmeq-s1_sintoma-motor.png")


# ═══════════════════════════════════════════ 10 · vacío y cargado
def vacio_cargado():
    """La misma máquina en dos condiciones, y qué revela cada una."""
    ASP = 1.25
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    x0, w_rot, w_col, sep = 2.0, 22.0, 36.0, 1.0
    y = H * 0.78
    _cabecera(ax, x0 + w_rot, y, w_col, H * 0.115, "VACÍO Y EN PLANO", GRIS)
    _cabecera(ax, x0 + w_rot + w_col + sep, y, w_col, H * 0.115,
              "CARGADO Y EN RAMPA", AZUL)
    filas = [("QUÉ SE LE PIDE\nAL TREN", "poca fuerza", "toda la fuerza\nque puede dar"),
             ("QUÉ SE VE", "camina bien,\naunque algo falle", "aparece lo que\nen plano no salía"),
             ("QUÉ PRUEBA", "que el equipo\narranca y se mueve",
              "que la fuerza\nllega hasta la rueda")]
    alto = H * 0.165
    for rot, a, b in filas:
        y -= alto + 0.8
        _celda(ax, x0, y, w_rot, alto, rot, BLANCO, GRIS, negrita=True, tam=NOTA * 0.78)
        _celda(ax, x0 + w_rot, y, w_col, alto, a, CLARO, MARINO, tam=NOTA * 0.9)
        _celda(ax, x0 + w_rot + w_col + sep, y, w_col, alto, b, CLARO, MARINO,
               tam=NOTA * 0.9)
    _banda(ax, H * 0.04, H * 0.09,
           "La carga y la pendiente revelan lo que el plano oculta")
    _guardar(fig, "fmeq-s1_vacio-cargado.png")


# ═══════════════════════════════════════════ 11 · recibe y entrega
def recibe_entrega():
    """La pregunta que se le hace a cada eslabón, uno por uno."""
    ASP = 1.05
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    x = [2.0, 32.0, 65.0, 98.0]
    y = H * 0.83
    _cabecera(ax, x[0], y, x[1] - x[0], H * 0.10, "ESLABÓN", MARINO)
    _cabecera(ax, x[1], y, x[2] - x[1], H * 0.10, "QUÉ RECIBE", AZUL)
    _cabecera(ax, x[2], y, x[3] - x[2], H * 0.10, "QUÉ ENTREGA", VERDE)
    filas = [("Motor", "combustible y aire", "giro y par"),
             ("Convertidor", "el giro del motor", "más par, menos vueltas"),
             ("Transmisión", "el giro del convertidor", "la relación de la marcha"),
             ("Árbol", "el giro de la transmisión", "el mismo giro, en el eje"),
             ("Diferencial", "el giro del árbol", "giro repartido a dos ruedas"),
             ("Mandos finales", "el giro del diferencial", "la fuerza final a la rueda")]
    alto = H * 0.095
    for a, b, c in filas:
        y -= alto + 0.6
        _celda(ax, x[0], y, x[1] - x[0], alto, a, CLARO, MARINO, negrita=True,
               tam=NOTA * 0.88)
        _celda(ax, x[1], y, x[2] - x[1], alto, b, BLANCO, MARINO, tam=NOTA * 0.86)
        _celda(ax, x[2], y, x[3] - x[2], alto, c, BLANCO, MARINO, tam=NOTA * 0.86)
    _banda(ax, H * 0.045, H * 0.085,
           "Donde uno recibe y no entrega, ahí se corta la cadena")
    _guardar(fig, "fmeq-s1_recibe-entrega.png")


# ═══════════════════════════════════════════ 12 · hasta dónde llega el reporte
def reporte_limite():
    """Lo que nombra el técnico y lo que diagnostica el mecánico."""
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _cabecera(ax, 3, H * 0.76, 45, H * 0.12, "LO QUE REPORTA EL TÉCNICO", AZUL)
    # el rótulo largo baja de punto: a NOTA se salía de su columna por la derecha
    _cabecera(ax, 52, H * 0.76, 45, H * 0.12, "LO QUE DIAGNOSTICA EL MECÁNICO", GRIS,
              tam=NOTA * 0.74)
    izq = ["el eslabón donde se corta", "qué observó y en qué condición",
           "qué eslabón revisar primero"]
    der = ["qué pieza interna falló", "por qué falló", "qué repuesto se pide"]
    y = H * 0.74
    alto = H * 0.115
    for a, b in zip(izq, der):
        y -= alto + 0.8
        _celda(ax, 3, y, 45, alto, a, CLARO, MARINO, tam=NOTA * 0.92)
        _celda(ax, 52, y, 45, alto, b, BLANCO, GRIS, tam=NOTA * 0.92)
    _banda(ax, H * 0.05, H * 0.13,
           "Un parte que nombra el componente equivocado cuesta semanas")
    _guardar(fig, "fmeq-s1_reporte-limite.png")


# ═══════════════════════════════════════════ 13 · la ficha del caso
def caso_ficha():
    """Los hechos del caso, sin la respuesta."""
    ASP = 1.16
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.80, 94, H * 0.15, AZUL)
    ax.text(50, H * 0.895, "Transporte y Acarreo Subterráneo S.A.C.", ha="center",
            va="center", family=F, fontsize=CUERPO, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.833, "Minetruck del nivel 4 · único equipo de acarreo",
            ha="center", va="center", family=F, fontsize=NOTA, color=BLANCO)

    hechos = [("EN LA RAMPA,\nCARGADO", "el motor sube de vueltas\ny la máquina no avanza"),
              ("EN PLANO\nY VACÍO", "camina bien"),
              ("EN EL PARTE", "«falta de fuerza del motor»"),
              ("A LAS CUATRO", "se pide un solo repuesto\nal proveedor")]
    y = H * 0.63
    alto = H * 0.135
    for rot, det in hechos:
        _celda(ax, 3, y, 30, alto, rot, CLARO, GRIS, negrita=True, tam=NOTA * 0.85)
        _celda(ax, 34, y, 63, alto, det, BLANCO, MARINO, tam=NOTA * 0.92)
        y -= alto + 1.0
    nota(ax, H * 0.055, "Dos guardias parado. El material del disparo sigue en el frente.")
    _guardar(fig, "fmeq-s1_caso-ficha.png")


# ═══════════════════════════════════════════ 14 · antes de resolver
def antes_de_resolver():
    """La pregunta que abre, y lo que está en juego."""
    ASP = 1.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.58, 94, H * 0.30, MARINO)
    ax.text(50, H * 0.73, "Si el motor sube de vueltas y la máquina\n"
                          "no avanza, ¿el motor está fallando?",
            ha="center", va="center", family=F, fontsize=CUERPO,
            fontweight="bold", color=BLANCO, linespacing=1.4)
    fichas = [("UN SOLO", "repuesto se puede pedir"),
              ("TRES SEMANAS", "trabajó el nivel con winche\nla vez que se pidió mal"),
              ("LAS CUATRO", "hora del proveedor en línea")]
    x = 3
    for grande, det in fichas:
        _redonda(ax, x, H * 0.14, 30.5, H * 0.36, CLARO)
        ax.text(x + 15.25, H * 0.41, grande, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=AZUL)
        ax.text(x + 15.25, H * 0.26, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO, linespacing=1.35)
        x += 32.2
    _guardar(fig, "fmeq-s1_antes-de-resolver.png")


# ═══════════════════════════════════════════ 15 · el encargo
def encargo():
    """Las cuatro filas de la hoja en blanco."""
    ASP = 1.14
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    filas = ["La cadena, en orden, desde el motor hasta la rueda",
             "Al costado de cada eslabón, qué le hace a la fuerza",
             "En qué eslabón la fuerza deja de llegar, y por qué el motor no es",
             "Qué eslabón se revisa primero, y en una línea por qué ese"]
    y = H * 0.76
    alto = H * 0.145
    for i, t in enumerate(filas):
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 12, alto, AZUL)
        ax.text(9, y + alto / 2, str(i + 1), ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(17, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO)
        y -= alto + 1.2
    _banda(ax, H * 0.05, H * 0.11,
           "Una hoja en blanco por equipo · 40 minutos")
    _guardar(fig, "fmeq-s1_encargo.png")


# ═══════════════════════════════════════════ 16 · cómo trabajamos
def como_trabajamos():
    """Los pasos del trabajo en equipo, en orden."""
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = [("1", "Lean el parte y la nota del operador. Subrayen los hechos", AZUL),
             ("2", "Armen la cadena antes de opinar dónde se corta", MARINO),
             ("3", "Descarten eslabones con lo que el operador describe", VERDE),
             ("4", "Escriban el que se revisa primero, con su razón", MORADO)]
    y = H * 0.78
    alto = H * 0.145
    for n, t, color in pasos:
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 11, alto, color)
        ax.text(8.5, y + alto / 2, n, ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(16, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO)
        y -= alto + 1.2
    _banda(ax, H * 0.06, H * 0.13, "Equipos de 3 · 40 minutos · expone uno por equipo")
    _guardar(fig, "fmeq-s1_como-trabajamos.png")


# ═══════════════════════════════════════════ 17 · la puesta en común
def puesta_comun():
    """El orden de la sustentación y el formato de la respuesta."""
    ASP = 1.20
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    ax.text(50, H * 0.90, "Dos minutos por equipo", ha="center", va="center",
            family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    partes = [("AFIRMACIÓN", AZUL, "el eslabón donde\nse corta la fuerza"),
              ("APOYO", VERDE, "el dato del caso\nque lo sostiene"),
              ("PREGUNTA", MORADO, "lo que todavía\nfalta saber")]
    x = 3
    for nombre, color, det in partes:
        _redonda(ax, x, H * 0.32, 30.5, H * 0.48, CLARO)
        _redonda(ax, x, H * 0.68, 30.5, H * 0.12, color)
        ax.text(x + 15.25, H * 0.74, nombre, ha="center", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=BLANCO)
        ax.text(x + 15.25, H * 0.50, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO, linespacing=1.35)
        x += 32.2
    _banda(ax, H * 0.10, H * 0.13,
           "Empezamos por los equipos que no eligieron el mismo eslabón")
    _guardar(fig, "fmeq-s1_puesta-comun.png")


# ═══════════════════════════════════════════ 18 · el puente
def puente_s2():
    """Adónde va esto: la sesión siguiente y el colaborativo del bloque."""
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.56, 45, H * 0.32, AZUL)
    ax.text(25.5, H * 0.80, "LA PRÓXIMA SESIÓN", ha="center", va="center",
            family=F, fontsize=NOTA * 0.92, fontweight="bold", color=BLANCO)
    ax.text(25.5, H * 0.66, "El sistema hidráulico:\nqué sostiene una carga\ncon el motor apagado",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92, color=BLANCO,
            linespacing=1.4)
    _redonda(ax, 52, H * 0.56, 45, H * 0.32, AMBAR)
    ax.text(74.5, H * 0.80, "AL CIERRE DEL BLOQUE", ha="center", va="center",
            family=F, fontsize=NOTA * 0.92, fontweight="bold", color=MARINO)
    ax.text(74.5, H * 0.66, "TC1: la flota de una labor\nsubterránea, y si la\nactividad puede ejecutarse",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92, color=MARINO,
            linespacing=1.4)
    ax.text(50, H * 0.34, "Hoy nombraste los eslabones de un equipo.\n"
                          "En el TC1 vas a decidir si cinco equipos entran o no a la labor.",
            ha="center", va="center", family=F, fontsize=NOTA, color=MARINO,
            linespacing=1.4)
    nota(ax, H * 0.12, "Antes de la próxima clase: el recurso autónomo del EVA.")
    _guardar(fig, "fmeq-s1_puente-s2.png")


if __name__ == "__main__":
    print("Esquemas de EOM-FMEQ-S1 · Sistema de potencia\n")
    for f in (curso_bloques, ruta, cadena, motor_convertidor, arbol_rueda,
              par_vueltas, marchas, ultimo_eslabon, sintoma_motor, vacio_cargado,
              recibe_entrega, reporte_limite, caso_ficha, antes_de_resolver,
              encargo, como_trabajamos, puesta_comun, puente_s2):
        f()
    print("\n18 esquemas en 04_Recursos-graficos/EOM/esquemas/fmeq/s1/")
