# -*- coding: utf-8 -*-
"""Esquemas de la sesión 8 · Requerimientos operativos de los equipos mineros.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO. En esta sesión la tentación es dibujar la rampa —sube,
    baja, el agua corre—, y la rampa es una labor: tiene forma real y está en
    planos. Lo que se dibuja es la RELACIÓN: qué cambia y qué no cuando cambia
    el sentido, y hacia dónde se junta el agua. Ni una sección de rampa, ni una
    cuneta, ni un perfil de terreno.

    Lo físico entra por imágenes de fuente ya aprobadas: la silueta del
    scooptram sacada del dibujo del fabricante (IMG-EOM-SCOOP-PERFIL) para
    enseñar de dónde sale cada número, y la fotografía del carguío
    (IMG-EOM-SCOOP-CARGANDO) para el Veo–Pienso–Me pregunto.

NO SE FILTRA LA RESPUESTA
    El encargo pide decir QUÉ LÍNEAS hay que rehacer al cambiar el sentido de
    la rampa. Por eso ninguna lámina de Adquisición dice cuáles: enseñan la
    regla —quién impone cada valor, qué depende del sentido— con equipos y
    números que NO son los del caso. Los tres equipos del caso aparecen solo en
    Aplicación, y con sus datos de catálogo, sin la columna de la decisión.

    Y la ficha del scooptram del caso no trae gradiente máxima cargado a
    propósito: es el dato que hay que SOLICITAR. Ninguna lámina lo rellena.

Uso:  python gen_esquemas_s8_requerimientos.py
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


# ═══════════════════════════════ 10 · las cinco exigencias (PC1 · 1-4)
def cinco_exigencias():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 16, [24, 67], 12,
           ["LA LABOR EXIGE", "Y ES"],
           [["SECCIÓN", "el hueco por donde entra y maniobra"],
            ["GRADIENTE", "la pendiente que sube o baja cargado"],
            ["ENERGÍA", "la que necesita: diésel o red"],
            ["VÍA", "rieles donde los hay; calzada y radio de giro donde no"],
            ["PISO", "firmeza y drenaje para pararse y frenar"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 8, 91, 12, AMBAR)
    _txt(ax, 50, 14, "Las cinco se declaran ANTES de excavar, no después",
         CUERPO - 2, MARINO, bold=True)
    return guardar(fig, "s8_cinco-exigencias.png")


# ═══════════════════════════════ 11 · con cuatro no basta (PC1 · 5-8)
def una_no_basta():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 14, H - 13, 72, 11, MARINO)
    _txt(ax, 50, H - 7.5, "CINCO CUMPLIDAS, O NO TRABAJA", CUERPO - 1, AMBAR, bold=True)
    y = H * 0.34
    for x, cab, txt, col, letra in (
            (5, "CUATRO DE CINCO", "el equipo no entra," + S + "o entra y no puede operar",
             AMBAR, MARINO),
            (53, "LAS CINCO", "el equipo trabaja" + S + "toda la guardia", VERDE, BLANCO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, letra)
    _txt(ax, 50, y - 12, "No se promedian ni se compensan:" + S +
         "la que falta manda sobre las otras cuatro.", CUERPO - 3, MARINO)
    nota(ax, 5, "Y se sabe antes: la hoja se llena en gabinete, no en la labor.")
    return guardar(fig, "s8_una-no-basta.png")


# ═══════════════════════════════ 13 · quién impone cada valor (PC2 · 5-8)
def quien_manda():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 16, [24, 34, 33], 12,
           ["LA LÍNEA", "LA IMPONE", "EL DATO SALE DE"],
           [["ANCHO", "el equipo más ancho", "su ficha, con cuchara"],
            ["ALTO", "el más alto", "su ficha, con torreta"],
            ["GRADIENTE", "el que menos sube cargado", "su ficha, cargado"],
            ["ENERGÍA", "el único que pide red", "su ficha"],
            ["VÍA", "el que rueda, no el que va sobre rieles", "su radio de giro"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 8, 91, 12, AMBAR)
    _txt(ax, 50, 14, "Ningún equipo manda en las cinco a la vez",
         CUERPO - 2, MARINO, bold=True)
    return guardar(fig, "s8_quien-manda.png")


# ═══════════════════════════════ 14 · el sentido de la rampa (PC3 · 1-4)
def sentido_rampa():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 16, H - 12, 68, 10, MARINO)
    _txt(ax, 50, H - 7, "MISMO HUECO, MISMO NÚMERO", CUERPO - 2, AMBAR, bold=True)
    _tabla(ax, 4.5, H - 26, [22, 34, 35], 12,
           ["", "RAMPA POSITIVA", "RAMPA NEGATIVA"],
           [["hacia dónde va", "sube desde el nivel", "baja hasta el nivel"],
            ["la carga", "sale bajando", "sale subiendo"],
            ["la gradiente es", "freno", "tracción"],
            ["el agua", "sale sola por la boca", "se junta en el fondo"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 7, 91, 11, CLARO)
    _txt(ax, 50, 12.5, "La sección no cambia: el equipo mide lo mismo en los dos sentidos",
         CUERPO - 4, MARINO, bold=True)
    return guardar(fig, "s8_sentido-rampa.png")


# ═══════════════════════════════ 15 · a dónde va el agua (PC3 · 5-8)
def agua_al_fondo():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 12, H - 13, 76, 11, AMBAR)
    _txt(ax, 50, H - 7.5, "EL AGUA CORRE SIEMPRE HACIA ABAJO", CUERPO - 2, MARINO, bold=True)
    pasos = [("la gradiente", "12 % para que el agua fluya"),
             ("en la positiva", "el agua sale sola por la boca"),
             ("en la negativa", "el agua se junta en el fondo"),
             ("y entonces", "cuneta con salida, y bombeo")]
    y = H - 24
    for i, (a, b) in enumerate(pasos):
        col = AMBAR if i == 3 else MARINO
        ax.add_patch(Circle((10, y), 4.2, facecolor=col))
        _txt(ax, 10, y + 0.3, str(i + 1), CUERPO - 4, MARINO if i == 3 else BLANCO, bold=True)
        _txt(ax, 18, y + 0.3, a, CUERPO - 4, GRIS, bold=True, ha="left")
        _txt(ax, 42, y + 0.3, b, CUERPO - 4, MARINO, ha="left")
        y -= 10
    nota(ax, 6, "La gradiente no es solo para el equipo: también para el agua.")
    return guardar(fig, "s8_agua-al-fondo.png")


# ═══════════════════════════════ 16 · la hoja de condiciones (PC4 · 1-4)
def hoja():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "HOJA DE CONDICIONES DE LA LABOR", CUERPO, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 25, [22, 24, 24, 21], 12,
           ["LÍNEA", "VALOR EXIGIDO", "EQUIPO QUE LO IMPONE", "SU FICHA"],
           [["SECCIÓN", "", "", ""], ["GRADIENTE", "", "", ""],
            ["ENERGÍA", "", "", ""], ["VÍA", "", "", ""], ["PISO", "", "", ""]],
           tam=CUERPO - 5)
    _caja(ax, 4.5, 7, 91, 11, AMBAR)
    _txt(ax, 50, 12.5, "Se firma: el contratista construye con ella",
         CUERPO - 1, MARINO, bold=True)
    return guardar(fig, "s8_hoja.png")


# ═══════════════════════════════ 17 · el dato que no está (PC4 · 5-8)
def dato_solicitado():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 18, H - 13, 64, 11, MARINO)
    _txt(ax, 50, H - 7.5, "EL DATO NO ESTÁ EN LA FICHA", CUERPO - 2, AMBAR, bold=True)
    y = H * 0.36
    for x, cab, txt, col, letra in (
            (5, "SE SUPONE", "se firma un número" + S + "que nadie midió", GRIS, BLANCO),
            (53, "SE SOLICITA", "se marca la línea" + S + "y no se firma en blanco",
             VERDE, BLANCO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 2, letra, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, letra)
        ax.annotate("", xy=(x + 21, y + 27.5), xytext=(x + 21, y + 33),
                    arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=14))
    _txt(ax, 50, y - 12, "Lo que no se exige por escrito" + S + "no se reclama después.",
         CUERPO - 3, MARINO)
    nota(ax, 5, "Una línea sin cerrar se marca. Rehacer de más también para la obra.")
    return guardar(fig, "s8_dato-solicitado.png")


# ═══════════════════════════════ 19 · la hoja con el tachón
def el_tachon():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "RAMPA 340 · HOJA DE CONDICIONES, YA FIRMADA", CUERPO - 3,
         BLANCO, bold=True)
    lineas = [("SECCIÓN", "4,50 × 4,00 m"), ("GRADIENTE", "12 %"),
              ("ENERGÍA", "llena"), ("VÍA", "llena"), ("PISO", "llena")]
    y = H - 22
    for a, b in lineas:
        _txt(ax, 8, y, a, CUERPO - 3, MARINO, bold=True, ha="left")
        _txt(ax, 40, y, b, CUERPO - 3, GRIS, ha="left")
        y -= 9
    _caja(ax, 20, y - 12, 60, 13, AMBAR)
    _txt(ax, 50, y - 5.5, "positiva  →  NEGATIVA", CUERPO - 1, MARINO, bold=True)
    _txt(ax, 50, y - 19, "Tachado a mano en la reunión. Sin fecha y sin firma.",
         CUERPO - 4, MARINO)
    nota(ax, 5, "El contratista empieza el lunes con la hoja que se le mande.")
    return guardar(fig, "s8_el-tachon.png")


# ═══════════════════════════════ 20 · los tres equipos del caso
def tres_equipos():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 16, [30, 30, 31], 12,
           ["EQUIPO", "LO QUE TRAE SU FICHA", "LO QUE NO TRAE"],
           [["Jumbo Sandvik DD321", "dos brazos", "—"],
            ["Scooptram CAT R1600G", "6 yd³", "gradiente máxima cargado"],
            ["Camión de bajo perfil", "5,0 m³", "—"]],
           destacar=[(1, 2)], tam=CUERPO - 4)
    _caja(ax, 4.5, 20, 91, 12, CLARO)
    _txt(ax, 50, 26, "La galería tiene rieles de 60 lb y trocha de 30\"; la rampa, ninguno",
         CUERPO - 4, MARINO, bold=True)
    _txt(ax, 50, 12, "Estándar de la unidad: 3,50 × 3,50 · 4,00 × 4,00 · 4,50 × 4,00 m",
         CUERPO - 4, MARINO)
    nota(ax, 4, "El dato que falta no se supone: se solicita y se marca la línea.")
    return guardar(fig, "s8_tres-equipos.png")


# ═══════════════════════════════ 21 · el encargo
def encargo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "HOJA DE CONDICIONES CORREGIDA", CUERPO - 2, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 25, [20, 22, 27, 22], 12,
           ["LÍNEA", "VALOR", "EQUIPO QUE LO IMPONE", "¿SE REHACE?"],
           [["SECCIÓN", "", "", ""], ["GRADIENTE", "", "", ""],
            ["ENERGÍA", "", "", ""], ["VÍA", "", "", ""], ["PISO", "", "", ""]],
           tam=CUERPO - 5)
    _caja(ax, 4.5, 7, 91, 11, AMBAR)
    _txt(ax, 50, 12.5, "Al pie: el dato solicitado. Y la firma.", CUERPO - 2,
         MARINO, bold=True)
    return guardar(fig, "s8_encargo.png")


# ═══════════════════════════════ 22 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "las tres fichas" + S + "y el estándar", "3'"),
             ("2", "Llenen", "las cinco líneas," + S + "con su equipo", "10'"),
             ("3", "Marquen", "las que se rehacen," + S + "y firmen", "5'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 20 minutos · una hoja firmada")
    return guardar(fig, "s8_como-trabajamos.png")


# ═══════════════════════════════ 25 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Qué pusieron en la línea de sección, y quién la impone?",
             "¿La gradiente se rehace o se queda? ¿Por qué?",
             "¿Qué línea marcaron con dato solicitado?",
             "¿Alguna pareja rehizo las cinco?" + S + "¿Qué cuesta eso en obra?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 5, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».", CUERPO - 5, MARINO)
    nota(ax, 5, "La cuarta la cierra el instructor: rehacer de más también para.")
    return guardar(fig, "s8_puesta-en-comun.png")


# ═══════════════════════════════ 26 · hacia dónde corre el agua
def hacia_donde_corre():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 14, 80, 12, AMBAR)
    _txt(ax, 50, H - 8, "¿Hacia dónde corre el agua en cada sentido?",
         CUERPO - 2, MARINO, bold=True)
    y = H * 0.24
    for x, cab, txt in ((5, "SI LA RAMPA SUBE", "el agua sale sola" + S + "por la boca"),
                        (53, "SI LA RAMPA BAJA", "el agua se junta" + S + "en el fondo")):
        _caja(ax, x, y, 42, 26, MARINO)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, AMBAR, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, BLANCO)
    _txt(ax, 50, H - 27, "Y en el fondo, ¿qué hace falta" + S + "que la hoja no pedía?",
         CUERPO - 3, MARINO)
    nota(ax, 5, "Lo abre el instructor en plenario. No se entrega ni se califica.")
    return guardar(fig, "s8_hacia-donde-corre.png")


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
    _txt(ax, 50, y - 12, "135 minutos. Hoy: qué le exige la labor" + S +
         "al equipo que va a entrar en ella.")
    return guardar(fig, "s8_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 7", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "cuánto se puede abrir" + S + "según lo que admite la roca",
         CUERPO - 4, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 8", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "qué le exige esa labor" + S + "al equipo que entra en ella",
         CUERPO - 4, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "El terreno puso el límite de arriba." + S +
         "El equipo pone el de abajo.", CUERPO - 3)
    return guardar(fig, "s8_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, cinco_exigencias, una_no_basta, quien_manda,
              sentido_rampa, agua_al_fondo, hoja, dato_solicitado, el_tachon,
              tres_equipos, encargo, como_trabajamos, puesta_en_comun,
              hacia_donde_corre):
        print(" ", f())
