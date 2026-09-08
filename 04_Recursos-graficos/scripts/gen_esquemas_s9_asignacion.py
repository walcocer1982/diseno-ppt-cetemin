# -*- coding: utf-8 -*-
"""Esquemas de la sesión 9 · Asignación de equipos por labor en minería subterránea.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO. Las cuatro labores —frente, tajeo, rampa y chimenea—
    tienen forma real y están en planos: aquí solo aparecen como FILAS de una
    tabla, con lo que cada una pide. Ni una sección, ni un perfil, ni un
    esquema de labores. Los equipos tampoco se dibujan: la silueta del
    scooptram y la fotografía del jumbo perforando entran por imágenes de
    fuente ya aprobadas.

    Lo que se dibuja son RELACIONES: qué pide cada labor, qué equipo entra y
    en cuál no, cómo se prueba una observación, y el armazón de la sesión.

NO SE FILTRA LA RESPUESTA
    El encargo pide observar el programa firmado: decir qué asignaciones no
    proceden y por qué. Por eso ninguna lámina de Adquisición nombra las
    asignaciones del caso ni cuántas están mal. La matriz de equipo × labor
    enseña la REGLA en genérico —dónde entra cada tipo de equipo— y deja el
    cruce con las fichas al estudiante.

    El caso lo dice expreso: «el programa no dice cuáles asignaciones están
    mal, ni cuántas». Las láminas tampoco.

EL PROGRAMA VA EN LA CARPETA, NO EN LA LÁMINA
    `casos.csv · recursos` no fija qué equipo se asignó a cada labor, así que
    la lámina del programa muestra su ESTRUCTURA —las cuatro labores, la
    columna de equipo y la firma— y remite a la carpeta que recibe cada
    pareja. Inventar aquí las asignaciones sería escribir el caso, y el caso
    se escribe en la base.

Uso:  python gen_esquemas_s9_asignacion.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    VERDE, guardar, lienzo, nota,
)

S = chr(10)


def _caja(ax, x, y, w, h, color, r=1.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.2,rounding_size=%.1f" % r,
                                facecolor=color, edgecolor="none"))


def _txt(ax, x, y, t, size=None, color=MARINO, bold=False, ha="center"):
    ax.text(x, y, t, ha=ha, va="center", family=F, fontsize=size or CUERPO,
            color=color, linespacing=1.3, fontweight="bold" if bold else "normal")


def _tabla(ax, x0, y0, anchos, alto, cabecera, filas, destacar=None, tam=None):
    y, x = y0, x0
    for w, t in zip(anchos, cabecera):
        ax.add_patch(Rectangle((x, y), w, alto, facecolor=MARINO, edgecolor=BLANCO, lw=2))
        _txt(ax, x + w / 2, y + alto / 2, t, tam or CUERPO - 4, BLANCO, bold=True)
        x += w
    for i, fila in enumerate(filas):
        y -= alto
        x = x0
        base = CLARO if i % 2 == 0 else BLANCO
        for j, (w, t) in enumerate(zip(anchos, fila)):
            es = destacar and (i, j) in destacar
            ax.add_patch(Rectangle((x, y), w, alto, facecolor=AMBAR if es else base,
                                   edgecolor=BLANCO, lw=2))
            _txt(ax, x + w / 2, y + alto / 2, t, tam or CUERPO - 4, MARINO,
                 bold=(j == 0 or es))
            x += w
    return y


# ═══════════════════════════════ 10 · las cuatro labores (PC1 · 1-4)
def cuatro_labores():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 16, [22, 40, 29], 12,
           ["LA LABOR", "ES", "Y POR ESO"],
           [["FRENTE", "el fondo de una labor que avanza", "se perfora y se limpia"],
            ["TAJEO", "donde se saca el mineral", "no avanza: produce"],
            ["RAMPA", "comunica niveles", "circula todo el equipo"],
            ["CHIMENEA", "vertical o inclinada", "casi no admite equipo"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 12, 91, 13, AMBAR)
    _txt(ax, 50, 18.5, "Cada una tiene su sección y su gradiente propias",
         CUERPO, MARINO, bold=True)
    nota(ax, 6, "Antes de asignar un equipo se lee la ficha de la labor.")
    return guardar(fig, "s9_cuatro-labores.png")


# ═══════════════════════════════ 11 · la labor manda (PC1 · 5-8)
def labor_manda():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 12, H - 13, 76, 11, MARINO)
    _txt(ax, 50, H - 7.5, "LA LABOR NO SE ADAPTA AL EQUIPO", CUERPO, AMBAR, bold=True)
    y = H * 0.34
    for x, cab, txt, col, letra in (
            (5, "SE EXCAVA Y LUEGO SE VE", "la labor queda hecha" + S + "y el equipo no entra",
             GRIS, BLANCO),
            (53, "SE ELIGE POR LA LABOR", "se lee su ficha" + S + "y se asigna lo que cabe",
             VERDE, BLANCO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, letra, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, letra)
    _txt(ax, 50, y - 12, "Una labor angosta no admite" + S + "el mismo equipo que una rampa.",
         CUERPO - 2, MARINO)
    nota(ax, 5, "Ensanchar una labor hecha cuesta más que elegir bien el equipo.")
    return guardar(fig, "s9_labor-manda.png")


# ═══════════════════════════════ 12 · dónde entra cada equipo (PC2 · 1-4)
def donde_entra():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 16, [27, 16, 16, 16, 16], 12,
           ["EL EQUIPO", "FRENTE", "TAJEO", "RAMPA", "CHIMENEA"],
           [["Jumbo", "sí", "sí", "sí", "no"],
            ["Scooptram", "sí", "sí", "sí", "no"],
            ["Winche de arrastre", "no", "sí", "no", "no"],
            ["Camión de bajo perfil", "no", "no", "sí", "no"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 12, 91, 13, CLARO)
    _txt(ax, 50, 18.5, "La chimenea se trabaja con equipo propio", CUERPO - 1,
         MARINO, bold=True)
    nota(ax, 6, "Es la regla general. Cada máquina se confirma con su ficha.")
    return guardar(fig, "s9_donde-entra.png")


# ═══════════════════════════════ 14 · no es lento, es inservible (PC3 · 1-4)
def no_es_lento():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 16, H - 13, 68, 11, AMBAR)
    _txt(ax, 50, H - 7.5, "NO CABE NO ES «VA LENTO»", CUERPO, MARINO, bold=True)
    y = H * 0.34
    for x, cab, txt, col in (
            (5, "«ES QUE DEMORA MÁS»", "se asigna igual" + S + "y la labor se detiene", GRIS),
            (53, "«NO CUMPLE LA SECCIÓN»", "se observa," + S + "con el dato que lo prueba", MARINO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, AMBAR if col is MARINO else BLANCO, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, BLANCO)
    _txt(ax, 50, y - 12, "La exigencia que falla se NOMBRA:" + S + "no basta decir «no entra».",
         CUERPO - 2, MARINO)
    nota(ax, 5, "Asignar mal detiene la labor toda la guardia, no un rato.")
    return guardar(fig, "s9_no-es-lento.png")


# ═══════════════════════════════ 15 · cómo se prueba (PC3 · 5-8)
def como_se_prueba():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = [("1", "el dato de la ficha del EQUIPO"),
             ("2", "el dato de la ficha de la LABOR"),
             ("3", "los dos, uno al lado del otro"),
             ("4", "y ahí se ve si procede o no")]
    y = H - 14
    for i, (n, t) in enumerate(pasos):
        col = AMBAR if i == 3 else MARINO
        ax.add_patch(Circle((11, y), 4.4, facecolor=col))
        _txt(ax, 11, y + 0.3, n, CUERPO - 3, MARINO if i == 3 else BLANCO, bold=True)
        _txt(ax, 19, y + 0.3, t, CUERPO - 2, MARINO, ha="left")
        y -= 11
    _caja(ax, 5, y - 8, 90, 12, CLARO)
    _txt(ax, 50, y - 2, "Sin el dato, la observación no se sostiene", CUERPO - 1,
         MARINO, bold=True)
    nota(ax, 5, "Generalizar «este equipo no sirve» es respuesta equivocada.")
    return guardar(fig, "s9_como-se-prueba.png")


# ═══════════════════════════════ 16 · se devuelve observado (PC4 · 1-4)
def devolver():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 13, 80, 11, MARINO)
    _txt(ax, 50, H - 7.5, "UN PROGRAMA FIRMADO NO SE DESOBEDECE", CUERPO - 2,
         AMBAR, bold=True)
    y = H * 0.34
    for x, cab, txt, col, letra in (
            (5, "SE DEVUELVE OBSERVADO", "y a tiempo, antes de" + S + "que bajen los equipos",
             VERDE, BLANCO),
            (53, "SOLO LO QUE NO PROCEDE", "observar de más cuesta" + S +
             "lo mismo que no observar", AMBAR, MARINO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, letra, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, letra)
    _txt(ax, 50, y - 12, "Cada observación lleva la exigencia" + S + "y el dato que la prueba.",
         CUERPO - 2, MARINO)
    nota(ax, 5, "Observar es trabajo del técnico, no desconfianza del jefe.")
    return guardar(fig, "s9_devolver.png")


# ═══════════════════════════════ 17 · aprobar, declarar y firmar (PC4 · 5-8)
def aprobar_declarar():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 16, [30, 61], 12,
           ["TAMBIÉN SE ESCRIBE", "PORQUE"],
           [["el visto bueno", "lo que está bien también se aprueba"],
            ["la labor sin equipo", "se declara, no se disimula"],
            ["la firma y la fecha", "alguien responde por lo observado"],
            ["y se entrega a tiempo", "después de la hora ya no sirve"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 12, 91, 13, AMBAR)
    _txt(ax, 50, 18.5, "Devolver a tiempo es trabajo del técnico", CUERPO,
         MARINO, bold=True)
    nota(ax, 6, "Una hoja sin firma no es una observación: es un comentario.")
    return guardar(fig, "s9_aprobar-declarar.png")


# ═══════════════════════════════ 19 · el programa firmado
def el_programa():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "PROGRAMA SEMANAL · SALA DE REPARTO", CUERPO - 1,
         BLANCO, bold=True)
    _tabla(ax, 4.5, H - 25, [30, 35, 26], 12,
           ["LABOR", "EQUIPO ASIGNADO", "VISTO / OBSERVADO"],
           [["FRENTE 285", "", ""], ["TAJEO 12", "", ""],
            ["RAMPA 340", "", ""], ["CHIMENEA 07", "", ""]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 14, 91, 12, AMBAR)
    _txt(ax, 50, 20, "Firmado por el jefe de mina. Firmado no es revisado.",
         CUERPO - 1, MARINO, bold=True)
    nota(ax, 7, "La columna de equipo viene llena en la carpeta de cada pareja.")
    return guardar(fig, "s9_el-programa.png")


# ═══════════════════════════════ 20 · las seis máquinas de almacén
def seis_maquinas():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 13, [46, 45], 9,
           ["EN ALMACÉN ESTA SEMANA", "LO QUE HAY QUE MIRAR"],
           [["Jumbo de un brazo", "su ficha"],
            ["Jumbo de dos brazos", "su ficha"],
            ["Scooptram eléctrico de 6 yd³", "su ficha"],
            ["Scooptram diésel de 1,5 yd³", "su ficha"],
            ["Winche de arrastre", "su ficha"],
            ["Camión de bajo perfil", "su ficha"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 4, 91, 11, CLARO)
    _txt(ax, 50, 9.5, "Seis máquinas, cuatro labores. No todas proceden.",
         CUERPO - 1, MARINO, bold=True)
    return guardar(fig, "s9_seis-maquinas.png")


# ═══════════════════════════════ 21 · el encargo
def encargo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "EL PROGRAMA, DEVUELTO", CUERPO, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 25, [24, 22, 24, 21], 12,
           ["LABOR", "VISTO / OBS.", "LA EXIGENCIA QUE FALLA", "EL DATO"],
           [["FRENTE 285", "", "", ""], ["TAJEO 12", "", "", ""],
            ["RAMPA 340", "", "", ""], ["CHIMENEA 07", "", "", ""]],
           tam=CUERPO - 5)
    _caja(ax, 4.5, 14, 91, 12, AMBAR)
    _txt(ax, 50, 20, "Abajo: la labor que queda sin poder trabajar. Firma y fecha.",
         CUERPO - 2, MARINO, bold=True)
    nota(ax, 7, "En parejas · 20 minutos · se devuelve el propio programa marcado.")
    return guardar(fig, "s9_encargo.png")


# ═══════════════════════════════ 22 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "el programa" + S + "y las fichas", "4'"),
             ("2", "Crucen", "las cuatro asignaciones," + S + "una por una", "12'"),
             ("3", "Cierren", "la labor sin equipo," + S + "y firmen", "4'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 20 minutos · un programa devuelto y firmado")
    return guardar(fig, "s9_como-trabajamos.png")


# ═══════════════════════════════ 25 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Qué pusieron en el frente 285? ¿Con qué dato?",
             "¿Y en la chimenea 07?",
             "¿Alguna asignación llevó visto bueno?" + S + "¿Cuál, y por qué?",
             "¿Qué labor declararon sin equipo posible?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 5, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».", CUERPO - 5, MARINO)
    nota(ax, 5, "Cada respuesta con el dato de la ficha, no con la costumbre.")
    return guardar(fig, "s9_puesta-en-comun.png")


# ═══════════════════════════════ 26 · observar de más
def observar_de_mas():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 14, 80, 12, AMBAR)
    _txt(ax, 50, H - 8, "Cuatro observaciones que no eran, y media guardia parada",
         CUERPO - 3, MARINO, bold=True)
    y = H * 0.24
    for x, cab, txt in ((5, "NO OBSERVAR LO QUE FALLA", "la labor se detiene" + S + "toda la guardia"),
                        (53, "OBSERVAR LO QUE SÍ PROCEDE", "las máquinas esperan" + S +
                         "mientras se discute")):
        _caja(ax, x, y, 42, 26, MARINO)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 5, AMBAR, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, BLANCO)
    _txt(ax, 50, H - 27, "Las dos cuestan lo mismo," + S + "y las dos las paga la guardia.",
         CUERPO - 2, MARINO)
    nota(ax, 5, "Lo abre el instructor en plenario. No se entrega ni se califica.")
    return guardar(fig, "s9_observar-de-mas.png")


# ═══════════════════════════════ armazón de la sesión
def ruta():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    tramos = [("CONEXIÓN", 20, AZUL), ("ADQUISICIÓN", 45, VERDE),
              ("APLICACIÓN", 35, MORADO), ("DISCUSIÓN", 25, AMBAR),
              ("REFLEXIÓN", 10, GRIS)]
    x0, ancho, y, alto = 5, 90, H * 0.42, 13
    x = x0
    for nom, mins, col in tramos:
        w = ancho * mins / 135
        _caja(ax, x, y, w - 0.6, alto, col, r=0.6)
        _txt(ax, x + w / 2, y + alto / 2 + 0.5, "%d'" % mins, CUERPO - 4,
             MARINO if col is AMBAR else BLANCO, bold=True)
        _txt(ax, x + w / 2, y + alto + (6 if mins >= 20 else 13), nom,
             CUERPO - 6, MARINO, bold=True)
        x += w
    _txt(ax, 50, y - 12, "135 minutos. Hoy: qué equipo entra en cada labor," + S +
         "cuál no, y cómo se observa un programa firmado.")
    return guardar(fig, "s9_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 8", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "qué le exige una labor" + S + "al equipo que entra",
         CUERPO - 4, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 9", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "cuál de los equipos que hay" + S + "cumple, y cuál no",
         CUERPO - 4, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "Ayer se escribió la exigencia." + S +
         "Hoy se cruza contra las máquinas que hay en almacén.", CUERPO - 3)
    return guardar(fig, "s9_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, cuatro_labores, labor_manda, donde_entra,
              no_es_lento, como_se_prueba, devolver, aprobar_declarar, el_programa,
              seis_maquinas, encargo, como_trabajamos, puesta_en_comun,
              observar_de_mas):
        print(" ", f())
