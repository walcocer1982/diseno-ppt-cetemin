# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 de EOM · Sostenimiento de labores mineras.

Son los TRECE que se dibujan. Las otras seis láminas de la sesión piden cosas
con cuerpo —split set, perno helicoidal, hydrabolt, cable, placa y cuña, y el
mostrador de almacén— y esas salen de fuente real, nunca de aquí (regla 3).

Lo que sí se dibuja: tablas comparativas, flujos, escalas numéricas y el
armazón de la sesión. Nada de secciones de labor ni de elementos en la roca:
un contorno de labor es geometría, y dibujarla es inventarla. Por eso «las
tres labores» y «la cuña» salen como escala numérica y no como corte.

CARPETA. Los esquemas de EOM se ordenan por sesión —s1/, s2/…— pero esas
carpetas ya son de Métodos de explotación. Con un segundo curso en la misma
carrera el nombre choca, así que este va a `sost/s1/`. Ver la observación
OBS-EOM-SOST-18.

Métrica del §11: lienzo de 1500 px de ancho, cuerpo de 52 px, sin bbox_inches.
Van SIN título dentro: el título lo pone la lámina.

Uso:  python gen_esquemas_sost_s1.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, cuerpo, guardar, lienzo, rotulo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402

CARPETA = "sost/s1/"


def _guardar(fig, nombre):
    guardar(fig, CARPETA + nombre)


def _cabecera(ax, x, y, w, h, txt, color, tam=None):
    """Cabecera de tabla.

    El tamaño por defecto es NOTA y no FUERTE: con FUERTE, «ELEMENTO Y
    ESPECIFICACIÓN» se salía de su columna y pisaba la vecina. Quien meta una
    cabecera larga en una columna estrecha tiene que bajarlo con `tam`.
    """
    _caja(ax, x, y, w, h, color)
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", family=F,
            fontsize=tam or NOTA * 0.92, fontweight="bold", color=BLANCO)


def _m(valor):
    """Metros con coma decimal, que es como se escriben en castellano."""
    return ("%.2f" % valor).replace(".", ",")


# ═════════════════════════════════════════════════ 1 · ruta de la sesión
def ruta():
    """Los cinco momentos con sus minutos: 20 · 45 · 40 · 20 · 10."""
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
    _guardar(fig, "sost-s1_ruta.png")


# ═════════════════════════════════════════ 2 · refuerzo contra soporte
def refuerzo_soporte():
    """Tabla comparada: qué hace cada uno, dónde trabaja y cuándo actúa."""
    ASP = 1.28
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    filas = [("QUÉ HACE", "cose la roca\ndesde adentro", "recibe la carga\nque ya se soltó"),
             ("DÓNDE TRABAJA", "dentro del taladro", "sobre la superficie"),
             ("CUÁNDO ACTÚA", "antes de que\nel bloque se suelte", "después, cuando\nel bloque ya cedió")]
    x0, w_rot, w_col = 2.0, 26.0, 34.0
    y = H * 0.74
    _cabecera(ax, x0 + w_rot, y, w_col, H * 0.13, "REFUERZO", AZUL)
    _cabecera(ax, x0 + w_rot + w_col + 1.0, y, w_col, H * 0.13, "SOPORTE", VERDE)
    alto = H * 0.185
    for rot, a, b in filas:
        y -= alto + 1.0
        _celda(ax, x0, y, w_rot, alto, rot, BLANCO, GRIS, negrita=True, tam=NOTA * 0.85)
        _celda(ax, x0 + w_rot, y, w_col, alto, a, CLARO, MARINO, tam=NOTA * 0.95)
        _celda(ax, x0 + w_rot + w_col + 1.0, y, w_col, alto, b, CLARO, MARINO, tam=NOTA * 0.95)
    _redonda(ax, x0 + w_rot, y - alto * 0.85, w_col * 2 + 1.0, alto * 0.62, AMBAR)
    ax.text(50 + w_rot / 2 - 1, y - alto * 0.54, "Casi toda labor lleva los dos, y en ese orden",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_refuerzo-soporte.png")


# ═════════════════════════════════════════════ 3 · cuál es cuál
def dos_columnas():
    """Los elementos repartidos en las dos familias."""
    ASP = 1.28
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    grupos = [(2.0, "REFUERZO", AZUL, ["Perno split set", "Perno helicoidal",
                                       "Hydrabolt", "Cable bolting"]),
              (51.0, "SOPORTE", VERDE, ["Malla electrosoldada", "Shotcrete",
                                        "Cuadro de madera", "Cimbra metálica"])]
    for x0, titulo, color, items in grupos:
        w = 47.0
        _cabecera(ax, x0, H * 0.80, w, H * 0.13, titulo, color)
        y = H * 0.80
        for it in items:
            y -= H * 0.155
            _celda(ax, x0, y, w, H * 0.14, it, CLARO, MARINO, tam=NOTA * 0.95)
    ax.text(50, H * 0.09, "Entra al taladro → refuerzo.  Queda por fuera → soporte.",
            ha="center", va="center", family=F, fontsize=NOTA, color=GRIS)
    _guardar(fig, "sost-s1_dos-columnas.png")


# ═══════════════════════════════════ 4 · primero se refuerza, después se retiene
def secuencia():
    """El orden de instalación, en tres pasos."""
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    pasos = [("1", "SE PERFORA", "el taladro, diez centímetros\nmás corto que el perno", AZUL),
             ("2", "SE REFUERZA", "entra el perno y se cierra\ncon platina y tuerca", MARINO),
             ("3", "SE RETIENE", "va la malla encima,\nsujeta por esa misma platina", VERDE)]
    y = H * 0.80
    for n, titulo, txt, color in pasos:
        _redonda(ax, 3.0, y - H * 0.155, 94.0, H * 0.155, CLARO)
        _redonda(ax, 4.5, y - H * 0.135, H * 0.115, H * 0.115, color)
        ax.text(4.5 + H * 0.0575, y - H * 0.0775, n, ha="center", va="center",
                family=F, fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(16.0, y - H * 0.045, titulo, ha="left", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=color)
        ax.text(16.0, y - H * 0.108, txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO, linespacing=1.3)
        y -= H * 0.185
    ax.text(50, H * 0.085, "Pedir soporte sin refuerzo es tapar la roca sin sujetarla",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_secuencia.png")


# ═══════════════════════════════════════════════ 5 · la cuña que hay que pasar
def cuna():
    """Cuánto crece la cuña con el ancho, SIN cifras.

    La primera versión llevaba la profundidad de cuña en metros y las dos
    longitudes de perno como líneas horizontales. Se veía que en la labor
    ancha ninguno de los dos pasaba la cuña —que es cierto con el factor
    conservador— y eso contradice la respuesta del caso. Comprobar la cuña con
    números es trabajo de geomecánica, no del técnico: OBS-EOM-SOST-14 lo dejó
    como el porqué cualitativo. Así que aquí solo crece la banda.
    """
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    # el ancho de la columna es el ancho de la labor y el alto es la cuña: si
    # las tres salen igual de anchas, el esquema desmiente lo que dice el título
    labores = [("labor angosta", 0.36, AZUL), ("labor media", 0.60, MORADO),
               ("labor ancha", 0.90, VERDE)]
    base, tope, ancho_max = H * 0.26, H * 0.50, 26.0
    hueco = (100 - ancho_max * sum(f for _, f, _ in labores) - 12.0) / 2
    x = 6.0
    for etq, frac, color in labores:
        w = ancho_max * frac
        _caja(ax, x, base, w, tope * frac, CLARO)
        _caja(ax, x, base + tope * frac - 0.9, w, 0.9, color)
        ax.text(x + w / 2, base + tope * frac / 2, "cuña\nsuelta",
                ha="center", va="center", family=F, fontsize=NOTA * 0.82,
                color=GRIS, linespacing=1.3)
        ax.annotate("", xy=(x + w, base - H * 0.035), xytext=(x, base - H * 0.035),
                    arrowprops=dict(arrowstyle="<->", color=color, linewidth=1.6))
        ax.text(x + w / 2, base - H * 0.095, etq, ha="center", va="center",
                family=F, fontsize=NOTA * 0.85, fontweight="bold", color=MARINO)
        x += w + hueco
    ax.text(50, H * 0.93, "A más ancho de labor, más profunda la roca que se suelta",
            ha="center", va="center", family=F, fontsize=NOTA, color=GRIS)
    _redonda(ax, 8.0, H * 0.04, 84.0, H * 0.10, AMBAR)
    ax.text(50, H * 0.09, "Por eso el estándar da más largo de perno a más sección",
            ha="center", va="center", family=F, fontsize=NOTA,
            fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_cuna.png")


# ═════════════════════════════════════════ 6 · el largo que manda el estándar
def largo_por_seccion():
    """Tabla del estándar: sección de labor → longitud de perno."""
    ASP = 1.35
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    filas = [("2,50 × 2,50  a  2,70 × 2,70", "6 pies", "1,83 m"),
             ("3,00 × 3,00  hasta  4,50", "7 pies", "2,13 m"),
             ("mayores de 5,00 × 5,00", "8 pies", "2,44 m")]
    x0, w1, w2, w3 = 2.0, 52.0, 22.0, 22.0
    y = H * 0.72
    _cabecera(ax, x0, y, w1, H * 0.13, "SECCIÓN DE LA LABOR", MARINO, NOTA * 0.85)
    _cabecera(ax, x0 + w1 + 1, y, w2, H * 0.13, "PERNO", AZUL)
    _cabecera(ax, x0 + w1 + w2 + 2, y, w3, H * 0.13, "LARGO", AZUL)
    for sec, pies, metros in filas:
        y -= H * 0.155
        _celda(ax, x0, y, w1, H * 0.14, sec, CLARO, MARINO, tam=NOTA * 0.95)
        _celda(ax, x0 + w1 + 1, y, w2, H * 0.14, pies, CLARO, MARINO, negrita=True)
        _celda(ax, x0 + w1 + w2 + 2, y, w3, H * 0.14, metros, CLARO, GRIS, tam=NOTA * 0.9)
    ax.text(50, H * 0.13, "Lo fija el estándar de la unidad, no la labor",
            ha="center", va="center", family=F, fontsize=NOTA, color=GRIS)
    _guardar(fig, "sost-s1_largo-por-seccion.png")


# ═══════════════════════════════════════════ 7 · quién calcula y quién lee
def quien_decide():
    """Dónde termina el técnico: geomecánica es dueña del estándar, él lo ejecuta.

    Decía «Calcula la cuña» contra «Lee el estándar», que cerraba la puerta a la
    S8: ahí el técnico sí calcula, cuando la sección de la labor no figura en la
    tabla. Lo que se protege no es que no calcule, sino que no cambie por su
    cuenta un estándar firmado (OBS-EOM-SOST-26).
    """
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(2.0, "ÁREA DE GEOMECÁNICA", MORADO,
             ["Escribe y firma el estándar", "Fija espaciamiento y largo",
              "Aprueba lo que se sale de él", "Revisa si el terreno cambia"]),
            (51.0, "TÉCNICO EN LA LABOR", AZUL,
             ["Ejecuta el estándar", "Calcula si la sección no figura",
              "Reporta lo que no cuadra", "Nunca lo cambia solo"])]
    for x0, titulo, color, items in cols:
        w = 47.0
        _cabecera(ax, x0, H * 0.78, w, H * 0.12, titulo, color, NOTA * 0.82)
        y = H * 0.78
        for it in items:
            y -= H * 0.145
            _celda(ax, x0, y, w, H * 0.13, it, CLARO, MARINO, tam=NOTA * 0.95)
    _redonda(ax, 12.0, H * 0.05, 76.0, H * 0.10, AMBAR)
    ax.text(50, H * 0.10, "Art. 214 g) · el ancho y la altura se mantienen\ndentro de los parámetros calculados",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9,
            fontweight="bold", color=MARINO, linespacing=1.3)
    _guardar(fig, "sost-s1_quien-decide.png")


# ═════════════════════════════════════════════════ 8 · las tres labores
def tres_labores():
    """Escala comparada de las tres labores del vale, por su ancho."""
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    labores = [("TAJEO veta Rosario", 6.0, "se abre 6,00 m entre caja y caja", AMBAR, MARINO),
               ("RAMPA de acceso", 4.0, "4,00 × 4,00 m", AZUL, BLANCO),
               ("CRUCERO", 3.0, "3,00 × 3,00 m", VERDE, BLANCO)]
    x0, maxw = 30.0, 66.0
    y = H * 0.74
    for nombre, ancho, detalle, color, tinta in labores:
        w = maxw * ancho / 6.0
        _redonda(ax, x0, y, w, H * 0.15, color)
        ax.text(x0 + w / 2, y + H * 0.075, _m(ancho) + " m", ha="center", va="center",
                family=F, fontsize=CUERPO, fontweight="bold", color=tinta)
        ax.text(x0 - 2.0, y + H * 0.098, nombre, ha="right", va="center", family=F,
                fontsize=NOTA * 0.95, fontweight="bold", color=MARINO)
        ax.text(x0 - 2.0, y + H * 0.048, detalle, ha="right", va="center", family=F,
                fontsize=NOTA * 0.82, color=GRIS)
        y -= H * 0.215
    ax.text(50, H * 0.10, "El vale pide lo mismo para las tres",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_tres-labores.png")


# ═══════════════════════════════════════════════════ 9 · el vale a corregir
def encargo():
    """El formato que la pareja llena: tres filas y dos líneas de cierre."""
    ASP = 1.32
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    x0, w1, w2, w3 = 2.0, 30.0, 44.0, 20.0
    y = H * 0.80
    _cabecera(ax, x0, y, w1, H * 0.11, "LABOR", MARINO, NOTA * 0.85)
    _cabecera(ax, x0 + w1 + 1, y, w2, H * 0.11, "ELEMENTO Y ESPECIFICACIÓN", MARINO, NOTA * 0.72)
    _cabecera(ax, x0 + w1 + w2 + 2, y, w3, H * 0.11, "R / S", AZUL)
    for lab in ("Tajeo Rosario", "Rampa de acceso", "Crucero"):
        y -= H * 0.13
        _celda(ax, x0, y, w1, H * 0.12, lab, CLARO, MARINO, tam=NOTA * 0.9)
        _celda(ax, x0 + w1 + 1, y, w2, H * 0.12, "", BLANCO)
        _caja(ax, x0 + w1 + 1, y, w2, 0.4, GRIS)
        _celda(ax, x0 + w1 + w2 + 2, y, w3, H * 0.12, "", BLANCO)
        _caja(ax, x0 + w1 + w2 + 2, y, w3, 0.4, GRIS)
    y -= H * 0.10
    for txt in ("Por qué el tajeo lleva otro largo de perno:",
                "Por qué el cable del vale anterior no hace falta acá:"):
        y -= H * 0.115
        ax.text(x0, y + H * 0.055, txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO)
        _caja(ax, x0, y, 96.0, 0.4, GRIS)
    _guardar(fig, "sost-s1_encargo.png")


# ═════════════════════════════════════════════════ 10 · cómo trabajamos
def como_trabajamos():
    """Los tres pasos del encargo con sus minutos."""
    ASP = 1.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    pasos = [("Lean el vale y las tres labores", 4, AZUL),
             ("Llenen la fila de cada labor, con su letra", 9, MARINO),
             ("Escriban las dos líneas del final", 5, VERDE)]
    y = H * 0.72
    for txt, mins, color in pasos:
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.95, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
        y -= H * 0.19
    ax.text(50, H * 0.10, "En parejas · 18 minutos · se entrega el vale corregido",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_como-trabajamos.png")


# ═══════════════════════════════════════════════ 11 · la puesta en común
def puesta_comun():
    """El orden de la discusión y el formato de respuesta."""
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    pasos = [("Empezamos por el tajeo", "qué largo pusieron, y con qué lo sustentan"),
             ("Seguimos por la rampa y el crucero", "si las tres llevan el mismo elemento"),
             ("Cerramos con el cable", "por qué el vale anterior lo traía y este no")]
    y = H * 0.76
    for n, (titulo, detalle) in enumerate(pasos, start=1):
        _redonda(ax, 3.0, y, 94.0, H * 0.185, CLARO)
        _redonda(ax, 5.0, y + H * 0.035, H * 0.115, H * 0.115, AZUL)
        ax.text(5.0 + H * 0.0575, y + H * 0.0925, str(n), ha="center", va="center",
                family=F, fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(17.0, y + H * 0.125, titulo, ha="left", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=MARINO)
        ax.text(17.0, y + H * 0.062, detalle, ha="left", va="center", family=F,
                fontsize=NOTA * 0.9, color=GRIS)
        y -= H * 0.215
    ax.text(50, H * 0.08, "Responde la pareja, no el que sabe",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_puesta-comun.png")


# ═══════════════════════════════════════ 12 · quién responde por el despacho
def quien_responde():
    """El cierre dirigido: la cadena de firmas del vale."""
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cadena = [("GEOMECÁNICA", "fija el estándar", MORADO),
              ("QUIEN PIDE", "llena el vale", AZUL),
              ("ALMACÉN", "despacha lo que dice", GRIS),
              ("LA LABOR", "recibe lo que llegó", VERDE)]
    x, w, hueco = 2.0, 22.5, 2.0
    for titulo, detalle, color in cadena:
        _redonda(ax, x, H * 0.42, w, H * 0.26, color)
        ax.text(x + w / 2, H * 0.60, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.9, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, H * 0.49, detalle, ha="center", va="center", family=F,
                fontsize=NOTA * 0.82, color=BLANCO)
        x += w + hueco
    _redonda(ax, 12.0, H * 0.10, 76.0, H * 0.20, AMBAR)
    ax.text(50, H * 0.20, "¿Quién debía darse cuenta antes que el almacenero?",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            fontweight="bold", color=MARINO)
    _guardar(fig, "sost-s1_quien-responde.png")


# ═════════════════════════════════════════════════ 13 · antes de irnos
def reflexion():
    """Las tres preguntas del cierre."""
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste frente a la fotografía",
                 "De lo que ves ahí, ¿qué es\nrefuerzo y qué es soporte?",
                 "La próxima: la malla, el shotcrete,\nel cuadro y la cimbra"]
    colores = (AZUL, MARINO, VERDE)
    y = H * 0.74
    for txt, color in zip(preguntas, colores):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _guardar(fig, "sost-s1_reflexion.png")


# ═══════════════════════════════════════════ 14 · el vale tal como llega
def vale():
    """El vale de despacho que la pareja va a corregir.

    Sustituye a la fotografía de almacén, que no apareció con procedencia
    limpia. Un vale es un FORMATO y los formatos se dibujan: el relato ya
    cuenta la escena, y lo que el alumno necesita ver es el papel.
    """
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    # el vale ocupa casi todo el alto: en la primera versión se quedaba en los
    # dos tercios de arriba y el lienzo bajaba vacío
    x0, w = 3.0, 63.0
    y_alto, y_bajo = H * 0.94, H * 0.06
    _caja(ax, x0, y_bajo, w, y_alto - y_bajo, CLARO)

    cab = H * 0.11
    _cabecera(ax, x0, y_alto - cab, w, cab, "VALE DE DESPACHO  ·  ALMACÉN MINA",
              MARINO, NOTA * 0.82)
    y = y_alto - cab - H * 0.075
    ax.text(x0 + 2.5, y, "N° 0417", ha="left", va="center", family=F,
            fontsize=NOTA * 0.78, color=GRIS)
    ax.text(x0 + w - 2.5, y, "Sale hoy, 4:00 p.m.", ha="right", va="center",
            family=F, fontsize=NOTA * 0.78, color=GRIS)

    y -= H * 0.075
    ax.text(x0 + 4.5, y, "LABOR", ha="left", va="center", family=F,
            fontsize=NOTA * 0.72, fontweight="bold", color=GRIS)
    ax.text(x0 + 31.0, y, "MATERIAL SOLICITADO", ha="left", va="center", family=F,
            fontsize=NOTA * 0.72, fontweight="bold", color=GRIS)

    alto_fila = H * 0.155
    for labor in ("Tajeo veta Rosario", "Rampa de acceso", "Crucero"):
        y -= alto_fila + H * 0.02
        _caja(ax, x0 + 2.5, y, w - 5.0, alto_fila, BLANCO)
        ax.text(x0 + 4.5, y + alto_fila / 2, labor, ha="left", va="center",
                family=F, fontsize=NOTA * 0.85, color=MARINO)
        ax.text(x0 + 31.0, y + alto_fila * 0.68, "Perno helicoidal de 7 pies",
                ha="left", va="center", family=F, fontsize=NOTA * 0.8, color=MARINO)
        ax.text(x0 + 31.0, y + alto_fila * 0.28, "Malla electrosoldada",
                ha="left", va="center", family=F, fontsize=NOTA * 0.8, color=MARINO)

    ax.text(x0 + 4.5, y_bajo + H * 0.045,
            "Firma del solicitante ________     Firma de almacén ________",
            ha="left", va="center", family=F, fontsize=NOTA * 0.7, color=GRIS)

    # el vale del mes pasado, al margen: el dato que contradice
    xn, wn = 69.5, 27.5
    _redonda(ax, xn, y_bajo + H * 0.22, wn, H * 0.50, BLANCO)
    _caja(ax, xn, y_bajo + H * 0.68, wn, 0.9, AMBAR)
    yn = y_bajo + H * 0.64
    ax.text(xn + wn / 2, yn, "Vale del mes pasado", ha="center", va="center",
            family=F, fontsize=NOTA * 0.74, fontweight="bold", color=MARINO)
    ax.text(xn + wn / 2, yn - H * 0.055, "mismo tajeo", ha="center", va="center",
            family=F, fontsize=NOTA * 0.68, color=GRIS)
    ax.text(xn + wn / 2, yn - H * 0.165, "Carretes de acero de 7 mm\n\nLechada de cemento",
            ha="center", va="center", family=F, fontsize=NOTA * 0.76,
            color=MARINO, linespacing=1.5)
    ax.text(xn + wn / 2, yn - H * 0.35, "En almacén siguen\ndos carretes sin abrir",
            ha="center", va="center", family=F, fontsize=NOTA * 0.68,
            color=GRIS, linespacing=1.35)

    _guardar(fig, "sost-s1_vale.png")


# la ruta ya no se genera aqui: la S1 y la S2 reparten los mismos minutos y
# comparten sost/comun/sost_ruta.png, que hace gen_esquemas_sost_s2.ruta_comun
TODOS = [refuerzo_soporte, dos_columnas, secuencia, cuna, largo_por_seccion,
         quien_decide, tres_labores, encargo, como_trabajamos, puesta_comun,
         quien_responde, reflexion, vale]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
