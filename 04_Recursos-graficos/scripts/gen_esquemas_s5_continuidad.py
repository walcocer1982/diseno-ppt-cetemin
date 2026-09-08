# -*- coding: utf-8 -*-
"""Esquemas de la sesión 5 · Interdependencia de las operaciones y continuidad del ciclo.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO: ni un frente, ni una labor, ni el material roto. Eso
    entra al PPT por imágenes de fuente que ya están aprobadas —la ficha del
    frente tras el disparo, la labor sostenida, el ciclo completo y el orden
    del desatado—, y aquí no se repiten. Lo que se dibuja son RELACIONES y
    ARMAZÓN: la cadena de lo que cada operación entrega a la siguiente, la
    tabla de lo que se detiene, los formatos que el estudiante llena, y la
    ruta, la puesta en común y el puente.

NO SE FILTRA LA RESPUESTA
    Las láminas de Adquisición se proyectan ANTES de que las parejas llenen el
    reporte. Por eso ninguna nombra en qué operación continúa el frente 340, el
    tajeo 12 ni la rampa 02: enseñan la regla —qué entrega cada operación y qué
    se detiene si se altera el orden— y la atribución se la queda el estudiante.

LA NOTA AL PIE VA DENTRO DEL LIENZO
    En la S4 dos notas cayeron fuera y desaparecieron sin aviso: matplotlib
    recorta en silencio y revisar_esquemas.py solo caza la tinta pegada al
    borde, no la que quedó entera afuera. Aquí las notas van en coordenada
    fija, no calculada a partir del último bloque.

Uso:  python gen_esquemas_s5_continuidad.py
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


# ═══════════════════════════════ 14 · lo que cada operación entrega (PC3 · 1-4)
def cadena():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = [("PERFORACIÓN", "taladros abiertos"),
             ("VOLADURA", "material roto"),
             ("CARGUÍO", "el frente despejado"),
             ("ACARREO", "la labor libre"),
             ("SOSTENIMIENTO", "la labor asegurada")]
    y, alto = H - 13, 11
    for i, (op, entrega) in enumerate(pasos):
        _caja(ax, 5, y, 34, alto, MARINO)
        _txt(ax, 22, y + alto / 2, op, CUERPO - 5, BLANCO, bold=True)
        _txt(ax, 45, y + alto / 2, "entrega", CUERPO - 7, GRIS)
        _caja(ax, 55, y, 40, alto, CLARO)
        _txt(ax, 75, y + alto / 2, entrega, CUERPO - 5, MARINO)
        if i < 4:
            ax.annotate("", xy=(22, y - 2.4), xytext=(22, y - 0.4),
                        arrowprops=dict(arrowstyle="-|>", color=AMBAR, lw=2.2,
                                        mutation_scale=13))
        y -= alto + 2.6
    nota(ax, 4, "Y el sostenimiento devuelve el frente a la perforación: el ciclo cierra.")
    return guardar(fig, "s5_cadena.png")


# ═══════════════════════════════ 15 · lo que se detiene (PC3 · 5-8)
def que_se_detiene():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _tabla(ax, 5, H - 15, [38, 26, 26], 12,
           ["SI SE ADELANTA…", "SE DETIENE", "PORQUE"],
           [["perforar sin limpiar", "la perforación", "no hay cara libre"],
            ["cargar sin ventilar", "el ingreso", "los gases no bajaron"],
            ["sostener sobre desmonte", "el sostenimiento", "el perno no ancla"],
            ["perforar sin asegurar techo", "la labor entera", "sacan la cuadrilla"]],
           tam=CUERPO - 5)
    _caja(ax, 5, 4, 90, 12, AMBAR)
    _txt(ax, 50, 12.5, "Saltarse un paso no adelanta", CUERPO - 4, MARINO, bold=True)
    _txt(ax, 50, 6.8, "detiene el que viene después, y el costo lo paga la guardia siguiente",
         CUERPO - 6, MARINO)
    return guardar(fig, "s5_que-se-detiene.png")


# ═══════════════════════════════ 16 · las casillas del reporte (PC4 · 1-4)
def reporte():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _tabla(ax, 5, H - 14, [18, 24, 24, 24], 11,
           ["LABOR", "CÓMO LA RECIBO", "CON QUÉ SIGO", "QUÉ SE DETIENE"],
           [["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
           tam=CUERPO - 7)
    _txt(ax, 50, 22, "Una fila por labor recibida. Se llena con lo que se RECIBE," + S +
         "no con lo que se piensa hacer.", CUERPO - 5, MARINO)
    nota(ax, 6, "Al pie va la firma: sin firma, el reporte de guardia no vale.")
    return guardar(fig, "s5_reporte.png")


# ═══════════════════════════════ 17 · cuándo se anota «falta el dato» (PC4 · 5-8)
def falta_el_dato():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 26, H - 14, 48, 11, MARINO)
    _txt(ax, 50, H - 8.5, "¿EL PARTE ALCANZA PARA DECIDIR?", CUERPO - 4, AMBAR, bold=True)
    y = H * 0.30
    for x, cab, txt, col, letra in ((5, "SÍ", "se llena la fila" + S + "con la operación", VERDE, BLANCO),
                                    (53, "NO", "se marca «falta el dato»" + S + "y se nombra cuál",
                                     AMBAR, MARINO)):
        _caja(ax, x, y, 42, 24, col)
        _txt(ax, x + 21, y + 17, cab, CUERPO - 2, letra, bold=True)
        _txt(ax, x + 21, y + 7.5, txt, CUERPO - 5, letra)
        ax.annotate("", xy=(x + 21, y + 25.5), xytext=(x + 21, y + 31),
                    arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=14))
    _txt(ax, 50, 14, "Suponer lo que no dice el parte es firmar por la guardia anterior.",
         CUERPO - 5, MARINO)
    nota(ax, 5, "El que entra responde por lo que aceptó sin observar.")
    return guardar(fig, "s5_falta-el-dato.png")


# ═══════════════════════════════ 19 · el parte de la guardia saliente
def el_parte():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 5, H - 11, 90, 9, MARINO)
    _txt(ax, 50, H - 6.5, "PARTE DE LA GUARDIA SALIENTE", CUERPO - 4, BLANCO, bold=True)
    lineas = [("FRENTE 340", "disparado 05:00 · con humos · nadie entró"),
              ("TAJEO 12", "limpio al tope · techo sin asegurar"),
              ("RAMPA 02", "sostenida ayer · malla y pernos al tope")]
    y = H - 22
    for lab, est in lineas:
        _txt(ax, 7, y, lab, CUERPO - 5, MARINO, bold=True, ha="left")
        _txt(ax, 32, y, est, CUERPO - 5, GRIS, ha="left")
        y -= 9
    _caja(ax, 26, y - 9, 48, 11, AMBAR)
    _txt(ax, 50, y - 3.5, "«ver piso»", CUERPO - 3, MARINO, bold=True)
    _txt(ax, 50, y - 15, "al pie, con otra letra." + S +
         "No dice qué encontró ni quién lo escribió.", CUERPO - 5, GRIS)
    nota(ax, 4, "El programa del día dice avanzar en las tres.")
    return guardar(fig, "s5_el-parte.png")


# ═══════════════════════════════ 20 · las tres labores, ordenadas
def tres_labores():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _tabla(ax, 5, H - 15, [22, 46, 22], 13,
           ["LABOR", "CÓMO QUEDÓ", "LO ÚLTIMO QUE SE HIZO"],
           [["FRENTE 340", "con humos, sin entrar nadie", "se disparó"],
            ["TAJEO 12", "limpio, techo sin asegurar", "se limpió"],
            ["RAMPA 02", "malla y pernos hasta el tope", "se sostuvo"]],
           tam=CUERPO - 6)
    _txt(ax, 50, 26, "Las tres están a mitad del mismo ciclo," + S +
         "y ninguna se quedó en el mismo sitio.", CUERPO - 5, MARINO)
    nota(ax, 8, "El tajeo 12 lleva además la nota del capataz.")
    return guardar(fig, "s5_tres-labores.png")


# ═══════════════════════════════ 21 · el encargo
def encargo():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _tabla(ax, 5, H - 14, [18, 24, 24, 24], 11,
           ["LABOR", "CÓMO LA RECIBO", "CON QUÉ SIGO", "QUÉ SE DETIENE"],
           [["FRENTE 340", "", "", ""], ["TAJEO 12", "", "", ""], ["RAMPA 02", "", "", ""]],
           tam=CUERPO - 7)
    _caja(ax, 5, 20, 90, 11, CLARO)
    _txt(ax, 50, 25.5, "Donde el parte no alcance: «FALTA EL DATO» y cuál", CUERPO - 5,
         MARINO, bold=True)
    _txt(ax, 50, 12, "Se escribe poco: una operación por casilla." + S + "Y se firma.",
         CUERPO - 5, MARINO)
    nota(ax, 4, "En parejas · 15 minutos · un solo reporte por pareja.")
    return guardar(fig, "s5_encargo.png")


# ═══════════════════════════════ 22 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "el parte, línea" + S + "por línea", "3'"),
             ("2", "Decidan", "con qué operación" + S + "sigue cada labor", "8'"),
             ("3", "Firmen", "revisen las tres" + S + "filas y firmen", "4'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 15 minutos · un reporte firmado")
    return guardar(fig, "s5_como-trabajamos.png")


# ═══════════════════════════════ 25 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Con qué operación sigue el frente 340?",
             "¿Y por qué no con la que muchos pusieron?",
             "En el tajeo 12, ¿qué se detiene si perforan ya?",
             "¿Alguna pareja marcó «falta el dato»?" + S + "¿En cuál, y por qué?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 5, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».", CUERPO - 5, MARINO)
    nota(ax, 5, "La segunda la cierra el instructor: ventilar y desatar no son operación.")
    return guardar(fig, "s5_puesta-en-comun.png")


# ═══════════════════════════════ 26 · «ver piso»
def ver_piso():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 26, H - 14, 48, 12, AMBAR)
    _txt(ax, 50, H - 8, "«ver piso»", CUERPO - 1, MARINO, bold=True)
    _txt(ax, 50, H - 21, "Lo escribió el capataz, no el jefe de guardia." + S +
         "No dice qué encontró.", CUERPO - 5, MARINO)
    y = H * 0.20
    for x, cab, txt in ((5, "LO QUE NO SE PUEDE", "decidir la operación" + S + "del tajeo 12"),
                        (53, "LO QUE SÍ SE ANOTA", "«falta el dato»:" + S + "en qué estado quedó el piso")):
        _caja(ax, x, y, 42, 24, MARINO)
        _txt(ax, x + 21, y + 17, cab, CUERPO - 5, AMBAR, bold=True)
        _txt(ax, x + 21, y + 7.5, txt, CUERPO - 5, BLANCO)
    nota(ax, 6, "Una nota a mano sin autor no es un dato: es un aviso de que falta uno.")
    return guardar(fig, "s5_ver-piso.png")


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
    _txt(ax, 50, y - 12, "135 minutos. Cierra el bloque 1:" + S +
         "la próxima clase se sustenta el Trabajo Colaborativo 1.")
    return guardar(fig, "s5_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 4", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "qué método se aplica" + S + "y en qué se reconoce", CUERPO - 4, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 5", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "cómo se retoma un ciclo" + S + "que otro dejó a medias", CUERPO - 4, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "El método ordena las labores." + S +
         "Hoy, con qué operación se sigue y qué se detiene.", CUERPO - 3)
    return guardar(fig, "s5_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, cadena, que_se_detiene, reporte, falta_el_dato,
              el_parte, tres_labores, encargo, como_trabajamos, puesta_en_comun, ver_piso):
        print(" ", f())
