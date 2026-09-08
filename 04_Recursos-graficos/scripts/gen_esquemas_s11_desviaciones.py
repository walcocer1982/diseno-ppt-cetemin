# -*- coding: utf-8 -*-
"""Esquemas de la sesión 11 · Asignación, destino del material y reporte de desviaciones.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO. La pala, el camión de 240 t, el banco, la pista y el
    botadero son cosas reales, de catálogo y de plano: aquí aparecen como
    filas de tabla y como cifras. Se dibujan RELACIONES —de qué dependen los
    pases, qué separa la ley de corte, qué prueba una desviación— y el armazón
    de la sesión.

    Como en la S10, el curso sigue sin ninguna imagen de superficie aprobada.
    Cuando entren, la lámina del estímulo y las de flota se sustituyen sin
    tocar el resto.

NO SE FILTRA LA RESPUESTA
    El caso siembra un dato: la ficha del camión grande dice cinco pases y el
    reporte de movimiento anota cuatro toda la guardia. Ese cruce es el trabajo
    del estudiante, y la respuesta vive solo en la nota al instructor.

    Por eso NINGUNA lámina hace la cuenta del faltante, y los ejemplos de la
    regla usan otros números —pala de 20 m³, camión de 150 t, seis pases—, que
    no son los del caso. Las cifras del caso aparecen en Aplicación, en los
    papeles que la pareja recibe, sin conclusión al lado.

Uso:  python gen_esquemas_s11_desviaciones.py
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


# ═══════════════════════════════ 8 · las dos cifras del cierre (estímulo)
def dos_cifras():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 16, H - 12, 68, 10, MARINO)
    _txt(ax, 50, H - 7, "AL CIERRE DE LA GUARDIA", CUERPO - 1, AMBAR, bold=True)
    y = H * 0.36
    for x, cab, cifra, col, letra in ((5, "EL PROGRAMA DECÍA", "12 000 t", AZUL, BLANCO),
                                      (53, "EL SISTEMA MARCÓ", "7 280 t", AMBAR, MARINO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, letra, bold=True)
        _txt(ax, x + 21, y + 7, cifra, FUERTE + 6, letra, bold=True)
    _txt(ax, 50, y - 12, "Llovió desde el cambio de guardia" + S + "y no paró en toda la tarde.",
         CUERPO - 2, MARINO)
    nota(ax, 5, "Vinieron todos, y no se malogró ningún equipo.")
    return guardar(fig, "s11_dos-cifras.png")


# ═══════════════════════════════ 10 · de qué dependen los pases (PC1 · 1-4)
def pases():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "UN PASE ES UNA CUCHARADA DENTRO DE LA TOLVA",
         CUERPO - 2, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 24, [30, 30, 31], 11,
           ["LA CUCHARA", "LA TOLVA", "Y ENTRE LAS DOS"],
           [["se mide en m³", "se mide en toneladas", "la densidad convierte"],
            ["20 m³, por ejemplo", "150 t, por ejemplo", "6 pases"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 12, 91, 13, AMBAR)
    _txt(ax, 50, 18.5, "La ficha del camión declara con cuántos pases se llena",
         CUERPO - 1, MARINO, bold=True)
    nota(ax, 6, "Los números del ejemplo no son los de ninguna unidad concreta.")
    return guardar(fig, "s11_pases.png")


# ═══════════════════════════════ 11 · un pase de menos (PC1 · 5-8)
def pase_de_menos():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 12, H - 12, 76, 10, MARINO)
    _txt(ax, 50, H - 7, "UN PASE DE MENOS, TODA LA GUARDIA", CUERPO - 1, AMBAR, bold=True)
    _tabla(ax, 4.5, H - 25, [40, 25, 26], 11,
           ["EN EL EJEMPLO", "CON 6 PASES", "CON 5"],
           [["lo que lleva el camión", "150 t", "125 t"],
            ["por viaje se pierden", "—", "25 t"],
            ["en 40 viajes de guardia", "—", "1 000 t"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 10, 91, 13, CLARO)
    _txt(ax, 50, 16.5, "Lo que se pierde por viaje se multiplica por todos los viajes",
         CUERPO - 2, MARINO, bold=True)
    nota(ax, 5, "El camión sale igual de lleno a la vista, y va a media carga.")
    return guardar(fig, "s11_pase-de-menos.png")


# ═══════════════════════════════ 12 · la ley de corte (PC2 · 1-4)
def ley_de_corte():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 14, H - 13, 72, 11, MARINO)
    _txt(ax, 50, H - 7.5, "DEL BANCO NO SALE UN SOLO MATERIAL", CUERPO - 1,
         AMBAR, bold=True)
    y = H * 0.34
    for x, cab, txt, col, letra in (
            (5, "SOBRE LA LEY DE CORTE", "es mineral:" + S + "chancadora o stock",
             VERDE, BLANCO),
            (53, "BAJO LA LEY DE CORTE", "es desmonte:" + S + "botadero", GRIS, BLANCO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, letra, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, letra)
    _txt(ax, 50, y - 12, "El destino lo marca geología" + S + "ANTES de que la pala cargue.",
         CUERPO - 1, MARINO)
    nota(ax, 5, "Cada polígono del banco sale marcado con su ley.")
    return guardar(fig, "s11_ley-de-corte.png")


# ═══════════════════════════════ 13 · el destino equivocado (PC2 · 5-8)
def destino_equivocado():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 15, [30, 32, 29], 12,
           ["SI SE EQUIVOCA", "LO QUE PASA", "EN EL TONELAJE"],
           [["mineral al botadero", "se pierde la ley", "no se nota"],
            ["desmonte a chancadora", "ensucia la alimentación", "no se nota"],
            ["mineral a stock", "espera su turno", "no se nota"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 10, 91, 13, AMBAR)
    _txt(ax, 50, 16.5, "El destino equivocado no se ve en el tonelaje del día",
         CUERPO - 1, MARINO, bold=True)
    nota(ax, 5, "Un mineral al botadero no resta tonelaje: resta ley.")
    return guardar(fig, "s11_destino-equivocado.png")


# ═══════════════════════════════ 14 · ruta y condición de piso (PC3 · 1-4)
def ruta_y_piso():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = [("1", "la ficha declara la limitación del equipo"),
             ("2", "el clima decide si esa limitación aplica hoy"),
             ("3", "la ruta y la condición del piso hacen el resto"),
             ("4", "y ahí se ve si la asignación procede")]
    y = H - 14
    for i, (n, t) in enumerate(pasos):
        col = AMBAR if i == 3 else MARINO
        ax.add_patch(Circle((11, y), 4.4, facecolor=col))
        _txt(ax, 11, y + 0.3, n, CUERPO - 3, MARINO if i == 3 else BLANCO, bold=True)
        _txt(ax, 19, y + 0.3, t, CUERPO - 3, MARINO, ha="left")
        y -= 11
    _caja(ax, 5, y - 8, 90, 12, CLARO)
    _txt(ax, 50, y - 2, "Cada camión tiene su ruta y su condición de piso",
         CUERPO - 1, MARINO, bold=True)
    nota(ax, 5, "La desviación se prueba con la ficha, no con la impresión.")
    return guardar(fig, "s11_ruta-y-piso.png")


# ═══════════════════════════════ 15 · asignar mal rompe el programa (PC3 · 5-8)
def rompe_el_programa():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 12, H - 13, 76, 11, AMBAR)
    _txt(ax, 50, H - 7.5, "ASIGNAR MAL NO ROMPE EL EQUIPO", CUERPO - 1, MARINO, bold=True)
    y = H * 0.34
    for x, cab, txt in ((5, "EL EQUIPO", "sale de su ruta" + S + "y deja de hacer viajes"),
                        (53, "EL PROGRAMA", "los viajes que faltan" + S +
                         "son toneladas que no salieron")):
        _caja(ax, x, y, 42, 26, MARINO)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 3, AMBAR, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, BLANCO)
    _txt(ax, 50, y - 12, "Quien asigna responde." + S + "Quien lo ve, reporta.",
         CUERPO, MARINO, bold=True)
    return guardar(fig, "s11_rompe-el-programa.png")


# ═══════════════════════════════ 16 · los tres bloques (PC4 · 1-4)
def tres_bloques():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 12, 80, 10, MARINO)
    _txt(ax, 50, H - 7, "CADA DESVIACIÓN LLEVA TRES COSAS", CUERPO - 1, AMBAR, bold=True)
    y = H * 0.40
    for i, (cab, sub) in enumerate((("QUÉ PASÓ", "el hecho, en" + S + "una línea"),
                                    ("CON QUÉ SE PRUEBA", "el dato de la" + S + "ficha o del reporte"),
                                    ("QUÉ SE PIDE", "la corrección," + S + "concreta"))):
        x = 4 + i * 31
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, y, 29, 26, col)
        _txt(ax, x + 14.5, y + 18, cab, CUERPO - 5, letra, bold=True)
        _txt(ax, x + 14.5, y + 7, sub, CUERPO - 6, letra)
    _txt(ax, 50, y - 12, "Sin el dato que la prueba," + S + "la desviación no se sostiene.",
         CUERPO - 1, MARINO)
    nota(ax, 5, "Y la cuenta que la sostiene se escribe al pie.")
    return guardar(fig, "s11_tres-bloques.png")


# ═══════════════════════════════ 17 · se reporta igual (PC4 · 5-8)
def reportar_igual():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 15, [46, 45], 12,
           ["LO QUE SE PIENSA", "LO QUE ES"],
           [["«si no resta toneladas, no va»", "va igual: se reporta"],
            ["«el reporte es un descargo»", "no lo es: es una corrección"],
            ["«ya lo saben todos»", "lo que no se escribe se repite"],
            ["«lo firmo mañana»", "sin firma no lo responde nadie"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 10, 91, 13, AMBAR)
    _txt(ax, 50, 16.5, "Reportar es la última operación del técnico, no la opcional",
         CUERPO - 2, MARINO, bold=True)
    nota(ax, 5, "Lo que no se reporta se repite la guardia siguiente.")
    return guardar(fig, "s11_reportar-igual.png")


# ═══════════════════════════════ 19 · los tres papeles
def tres_papeles():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 12, 80, 10, MARINO)
    _txt(ax, 50, H - 7, "LO QUE HAY SOBRE LA MESA", CUERPO, AMBAR, bold=True)
    y = H * 0.40
    for i, (cab, sub) in enumerate((("LA ASIGNACIÓN", "qué equipo fue" + S + "a qué ruta"),
                                    ("LAS FICHAS", "lo que declara" + S + "cada máquina"),
                                    ("EL MOVIMIENTO", "viajes, pases" + S + "y destinos"))):
        x = 4 + i * 31
        _caja(ax, x, y, 29, 26, AZUL)
        _txt(ax, x + 14.5, y + 18, cab, CUERPO - 4, BLANCO, bold=True)
        _txt(ax, x + 14.5, y + 7, sub, CUERPO - 6, BLANCO)
    _txt(ax, 50, y - 12, "«Explíquenmelas con lo que está ahí," + S +
         "y déjenme algo escrito que yo pueda mandar.»", CUERPO - 2, MARINO)
    nota(ax, 5, "Quince minutos para la reunión del jefe de mina.")
    return guardar(fig, "s11_tres-papeles.png")


# ═══════════════════════════════ 20 · la flota y lo que declara
def flota():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    # Los dos papeles van SEPARADOS a proposito. El dato sembrado del caso es el
    # cruce entre lo que declara la ficha y lo que anoto el reporte: ponerlos en
    # la misma fila lo resolveria por el estudiante.
    _tabla(ax, 4.5, H - 14, [43, 48], 11,
           ["LAS FICHAS DECLARAN", ""],
           [["pala hidráulica", "cuchara de 27 m³"],
            ["camión de 240 t", "se llena con 5 pases"],
            ["camión de 230 t", "derrapa con pista mojada"]],
           tam=CUERPO - 4)
    _tabla(ax, 4.5, H - 53, [43, 48], 11,
           ["EL REPORTE ANOTA", ""],
           [["pases por camión", "4, la misma cifra toda la guardia"],
            ["un polígono sobre la ley", "descargado en botadero"],
            ["la asignación", "el camión de 230 t, a la ruta del botadero"]],
           tam=CUERPO - 4)
    nota(ax, 5, "Llovió desde el cambio de guardia y no paró en toda la tarde.")
    return guardar(fig, "s11_flota.png")


# ═══════════════════════════════ 21 · el encargo
def encargo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "REPORTE DE DESVIACIÓN DE LA GUARDIA", CUERPO, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 23, [22, 24, 24, 21], 10,
           ["DESVIACIÓN", "QUÉ PASÓ", "CON QUÉ SE PRUEBA", "QUÉ SE PIDE"],
           [["1", "", "", ""], ["2", "", "", ""], ["3", "", "", ""]],
           tam=CUERPO - 6)
    _caja(ax, 4.5, 4, 91, 16, AMBAR)
    _txt(ax, 50, 14, "Al pie: la cuenta de los pases, escrita a mano",
         CUERPO - 1, MARINO, bold=True)
    _txt(ax, 50, 7.5, "Firma, fecha y guardia. En parejas · 20 minutos.",
         CUERPO - 4, MARINO)
    return guardar(fig, "s11_encargo.png")


# ═══════════════════════════════ 22 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "los tres papeles," + S + "uno al lado del otro", "4'"),
             ("2", "Escriban", "las tres desviaciones" + S + "y la cuenta", "12'"),
             ("3", "Cierren", "firma, fecha" + S + "y guardia", "4'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 20 minutos · un reporte firmado")
    return guardar(fig, "s11_como-trabajamos.png")


# ═══════════════════════════════ 25 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Cuál fue su primera desviación, y con qué dato?",
             "¿Qué cuenta escribieron al pie?",
             "¿Qué pidieron corregir en cada una?",
             "¿Alguna de las tres no resta toneladas?" + S + "¿La reportaron igual?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 5, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».", CUERPO - 5, MARINO)
    nota(ax, 5, "Cada desviación con su dato: sin él no se sostiene.")
    return guardar(fig, "s11_puesta-en-comun.png")


# ═══════════════════════════════ 26 · la que no resta toneladas
def no_resta():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 8, H - 14, 84, 12, AMBAR)
    _txt(ax, 50, H - 8, "Una de las tres no resta ni una tonelada",
         CUERPO, MARINO, bold=True)
    _txt(ax, 50, H - 25, "¿Cuál es, y por qué se reporta igual?", FUERTE, MARINO, bold=True)
    y = H * 0.14
    _caja(ax, 5, y, 90, 20, MARINO)
    _txt(ax, 50, y + 13, "El tonelaje del día no la ve.", CUERPO - 2, BLANCO)
    _txt(ax, 50, y + 6, "¿Qué se pierde entonces, y quién lo paga?",
         CUERPO - 2, AMBAR, bold=True)
    nota(ax, 5, "Lo abre el instructor en plenario. No se entrega ni se califica.")
    return guardar(fig, "s11_no-resta.png")


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
    _txt(ax, 50, y - 12, "135 minutos. Cierra el bloque 2:" + S +
         "la próxima clase se sustenta el Trabajo Colaborativo 2.")
    return guardar(fig, "s11_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 10", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "las labores del tajo" + S + "y su ciclo de minado",
         CUERPO - 4, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 11", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "qué equipo, a dónde va" + S + "el material, y qué se reporta",
         CUERPO - 4, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "Ayer se llenó el parte de lo que pasó." + S +
         "Hoy se explica por qué no salió lo que debía.", CUERPO - 3)
    return guardar(fig, "s11_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, dos_cifras, pases, pase_de_menos, ley_de_corte,
              destino_equivocado, ruta_y_piso, rompe_el_programa, tres_bloques,
              reportar_igual, tres_papeles, flota, encargo, como_trabajamos,
              puesta_en_comun, no_resta):
        print(" ", f())
