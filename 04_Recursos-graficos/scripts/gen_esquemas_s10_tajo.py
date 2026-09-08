# -*- coding: utf-8 -*-
"""Esquemas de la sesión 10 · Explotación superficial: labores y ciclo a tajo abierto.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO, y en esta sesión eso pesa más que en ninguna. El banco,
    la rampa, el botadero, el pad y el talud son labores reales, fotografiadas
    y dibujadas en planos; la perforadora, la pala, el camión de 240 t, el
    tractor y la cisterna son máquinas de catálogo. NADA de eso se dibuja aquí:
    aparecen como filas de tabla, con lo que hacen y dónde.

    EL CURSO NO TIENE TODAVÍA NI UNA IMAGEN DE SUPERFICIE APROBADA. Las once
    fotos, planos y siluetas del catálogo son subterráneas. Por eso esta sesión
    va sin fotografía: hasta que entren imágenes de fuente real —del plano de
    la unidad y de los catálogos de los equipos, por el camino del §10—, el
    tajo abierto se enseña con tablas. Dibujarlo sería inventarlo.

EL ESTÍMULO DE LA CONEXIÓN
    Sin fotografía, el Veo–Pienso–Me pregunto se hace sobre la SECUENCIA de lo
    que la guardia vio durante el día, contada como la cuenta el caso: máquinas
    por lo que hacen, sin ponerles nombre de operación. Es lo que el estudiante
    tiene que mirar. Cuando haya foto de un banco en operación, esta lámina se
    sustituye y el resto de la sesión no se toca.

Uso:  python gen_esquemas_s10_tajo.py
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


# ═══════════════════════════════ 8 · lo que la guardia vio (estímulo)
def lo_que_se_vio():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "UN DÍA EN LA UNIDAD DE COBRE", CUERPO, BLANCO, bold=True)
    visto = ["una máquina sobre orugas abriendo huecos en el escalón",
             "un camión que llegó, llenó esos huecos, y sonó una sirena",
             "una máquina de brazo llenando camiones muy grandes",
             "los camiones bajando: unos a un lado, otros a otro",
             "una cisterna regando el camino porque no se veía",
             "un tractor emparejando el piso donde se para la máquina",
             "un cargador moviendo material en una ruma"]
    y = H - 20
    for t in visto:
        ax.add_patch(Circle((9, y), 1.5, facecolor=AMBAR))
        _txt(ax, 15, y, t, CUERPO - 3, MARINO, ha="left")
        y -= 8
    _caja(ax, 4.5, 4, 91, 11, CLARO)
    _txt(ax, 50, 9.5, "Nadie puso ni un perno en todo el día", CUERPO - 1,
         MARINO, bold=True)
    return guardar(fig, "s10_lo-que-se-vio.png")


# ═══════════════════════════════ 10 · las labores del tajo (PC1 · 1-4)
def labores_tajo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 14, [24, 38, 29], 11,
           ["LA LABOR", "ES", "RECIBE O SACA"],
           [["BANCO", "el escalón desde donde se extrae", "el material del tajo"],
            ["RAMPA", "comunica los bancos", "por ella sale todo"],
            ["BOTADERO", "depósito de lo que no tiene ley", "el desmonte"],
            ["PAD Y STOCK", "depósitos de mineral", "cada uno a su destino"],
            ["CHANCADORA", "la entrada de planta", "el mineral que se procesa"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 8, 91, 13, AMBAR)
    _txt(ax, 50, 14.5, "A cielo abierto no hay frente ni tajeo: hay banco",
         CUERPO, MARINO, bold=True)
    return guardar(fig, "s10_labores-tajo.png")


# ═══════════════════════════════ 11 · arriba y abajo (PC1 · 5-8)
def arriba_abajo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 15, [30, 30, 31], 12,
           ["LO MISMO SE LLAMA", "ABAJO", "ARRIBA"],
           [["donde se extrae", "frente y tajeo", "banco"],
            ["por donde se sale", "rampa y pique", "rampa"],
            ["dónde va el desmonte", "relleno o cancha", "botadero"],
            ["dónde va el mineral", "echadero y tolva", "pad, stock, chancadora"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 10, 91, 13, CLARO)
    _txt(ax, 50, 16.5, "La altura del banco la fija el diseño del talud, no la guardia",
         CUERPO - 2, MARINO, bold=True)
    nota(ax, 5, "Las labores del tajo se reconocen en el plano por su forma.")
    return guardar(fig, "s10_arriba-abajo.png")


# ═══════════════════════════════ 12 · el ciclo en superficie (PC2 · 1-4)
def ciclo_superficie():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 14, [26, 36, 29], 12,
           ["LA OPERACIÓN", "LA HACE", "EN LA LABOR"],
           [["PERFORACIÓN", "perforadora sobre orugas", "el banco"],
            ["VOLADURA", "camión fábrica, con ANFO", "el banco"],
            ["CARGUÍO", "pala hidráulica", "el banco"],
            ["ACARREO", "camión minero", "la rampa, hasta su destino"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 10, 91, 13, AMBAR)
    _txt(ax, 50, 16.5, "Cada operación ocurre en una labor, y se anota con ella",
         CUERPO - 1, MARINO, bold=True)
    nota(ax, 5, "El cargador frontal trabaja en los stocks, no en el banco.")
    return guardar(fig, "s10_ciclo-superficie.png")


# ═══════════════════════════════ 13 · misma función, otro tamaño (PC2 · 5-8)
def mismo_distinto():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 14, [26, 33, 32], 12,
           ["LA MISMA FUNCIÓN", "ABAJO", "ARRIBA"],
           [["perforar", "jumbo, taladros cortos", "orugas, taladros de 11\""],
            ["volar", "dinamita y emulsión", "ANFO desde camión fábrica"],
            ["cargar", "scooptram", "pala hidráulica"],
            ["acarrear", "camión de bajo perfil", "camión de 240 toneladas"]],
           tam=CUERPO - 4)
    _caja(ax, 4.5, 10, 91, 13, CLARO)
    _txt(ax, 50, 16.5, "Los equipos son los mismos en función y distintos en tamaño",
         CUERPO - 2, MARINO, bold=True)
    nota(ax, 5, "Suponer que a cielo abierto no se vuela es el error más común.")
    return guardar(fig, "s10_mismo-distinto.png")


# ═══════════════════════════════ 14 · cuatro de cinco (PC3 · 1-4)
def cuatro_de_cinco():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 14, H - 13, 72, 11, MARINO)
    _txt(ax, 50, H - 7.5, "DE LAS CINCO DE ABAJO, ARRIBA HAY CUATRO", CUERPO - 2,
         AMBAR, bold=True)
    ops = ["PERFORACIÓN", "VOLADURA", "CARGUÍO", "ACARREO", "SOSTENIMIENTO"]
    y = H * 0.44
    for i, op in enumerate(ops):
        x = 3 + i * 19
        col = AMBAR if i == 4 else VERDE
        _caja(ax, x, y, 17, 16, col)
        _txt(ax, x + 8.5, y + 8, op, CUERPO - 7, MARINO if i == 4 else BLANCO, bold=True)
    _txt(ax, 50, y - 10, "No hay techo que sostener.", CUERPO, MARINO, bold=True)
    _txt(ax, 50, y - 20, "El ciclo se acorta, pero no cambia de naturaleza.",
         CUERPO - 3, MARINO)
    nota(ax, 5, "Perforación y voladura sí existen, y con más explosivo.")
    return guardar(fig, "s10_cuatro-de-cinco.png")


# ═══════════════════════════════ 15 · qué da la estabilidad (PC3 · 5-8)
def talud():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 12, H - 13, 76, 11, AMBAR)
    _txt(ax, 50, H - 7.5, "LA ESTABILIDAD LA DA EL DISEÑO", CUERPO, MARINO, bold=True)
    y = H * 0.32
    for x, cab, txt in ((5, "NO ES UNA OPERACIÓN", "nadie la ejecuta" + S + "durante la guardia"),
                        (53, "ES UN DISEÑO", "ángulo, altura de banco" + S + "y berma, ya definidos")):
        _caja(ax, x, y, 42, 26, MARINO)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, AMBAR, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 5, BLANCO)
    _txt(ax, 50, y - 12, "Se decide ANTES de la guardia," + S + "no durante.",
         CUERPO - 1, MARINO)
    nota(ax, 5, "Lo que la guardia hace es respetar el diseño, no sostener.")
    return guardar(fig, "s10_talud.png")


# ═══════════════════════════════ 16 · el parte, fila por fila (PC4 · 1-4)
def parte_filas():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "EL PARTE TRAE LAS MISMAS CINCO FILAS", CUERPO - 1,
         BLANCO, bold=True)
    _tabla(ax, 4.5, H - 24, [31, 30, 30], 11,
           ["LA FILA", "SE LLENA CON", "Y CON"],
           [["cada operación", "el equipo que la hizo", "la labor donde ocurrió"],
            ["la que no ocurrió", "nada", "el porqué, al margen"],
            ["el acarreo", "el camión", "más de un destino"]],
           tam=CUERPO - 5)
    _caja(ax, 4.5, 10, 91, 13, AMBAR)
    _txt(ax, 50, 16.5, "Una fila vacía sin explicación es un parte incompleto",
         CUERPO - 1, MARINO, bold=True)
    return guardar(fig, "s10_parte-filas.png")


# ═══════════════════════════════ 17 · lo que va abajo (PC4 · 5-8)
def servicios():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 13, 80, 11, MARINO)
    _txt(ax, 50, H - 7.5, "¿CAMBIÓ EL ESTADO DEL MATERIAL?", CUERPO - 1, AMBAR, bold=True)
    y = H * 0.34
    for x, cab, txt, col, letra in (
            (5, "SÍ", "es operación unitaria:" + S + "va en una fila del ciclo",
             VERDE, BLANCO),
            (53, "NO", "es servicio de mina:" + S + "va en el bloque de abajo",
             AMBAR, MARINO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, FUERTE, letra, bold=True)
        _txt(ax, x + 21, y + 7, txt, CUERPO - 5, letra)
    _txt(ax, 50, y - 12, "Meterlas en el ciclo reporta la guardia" + S +
         "por debajo de lo que fue.", CUERPO - 2, MARINO)
    nota(ax, 5, "Al practicante le devolvieron el parte por una fila de más.")
    return guardar(fig, "s10_servicios.png")


# ═══════════════════════════════ 19 · el formato de arriba
def el_formato():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "PARTE DE GUARDIA · SUPERFICIE", CUERPO, BLANCO, bold=True)
    y = _tabla(ax, 4.5, H - 23, [31, 30, 30], 9,
               ["OPERACIÓN UNITARIA", "EQUIPO", "LABOR"],
               [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]],
               tam=CUERPO - 5)
    _caja(ax, 4.5, y - 14, 91, 12, CLARO)
    _txt(ax, 50, y - 8, "SERVICIOS DE MINA", CUERPO - 2, MARINO, bold=True)
    nota(ax, 5, "«Es igual, solo que aquí no hay techo», dijo el jefe de guardia.")
    return guardar(fig, "s10_el-formato.png")


# ═══════════════════════════════ 20 · los equipos de la unidad
def los_equipos():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _tabla(ax, 4.5, H - 13, [46, 45], 9,
           ["EN LA UNIDAD HAY", "Y ESO ES"],
           [["perforadora sobre orugas", "taladros de 11\", banco de 15 m"],
            ["camión fábrica", "carga ANFO en el taladro"],
            ["pala hidráulica", "cuchara de 27 m³"],
            ["camión minero", "240 toneladas por viaje"],
            ["cargador frontal", "trabaja en los stocks"],
            ["tractor y cisterna", "piso y polvo"]],
           tam=CUERPO - 3)
    _caja(ax, 4.5, 4, 91, 11, AMBAR)
    _txt(ax, 50, 9.5, "Seis máquinas, y solo cuatro filas de ciclo", CUERPO - 1,
         MARINO, bold=True)
    return guardar(fig, "s10_los-equipos.png")


# ═══════════════════════════════ 21 · el encargo
def encargo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 4.5, H - 11, 91, 9, MARINO)
    _txt(ax, 50, H - 6.5, "EL PARTE, LLENO", CUERPO, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 21, [31, 30, 30], 9,
           ["OPERACIÓN UNITARIA", "EQUIPO", "LABOR"],
           [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]],
           tam=CUERPO - 5)
    _caja(ax, 4.5, 4, 91, 16, AMBAR)
    _txt(ax, 50, 14, "La fila que quede vacía, con su porqué al margen",
         CUERPO - 1, MARINO, bold=True)
    _txt(ax, 50, 7.5, "Lo que no es operación unitaria va abajo, en servicios de mina",
         CUERPO - 4, MARINO)
    return guardar(fig, "s10_encargo.png")


# ═══════════════════════════════ 22 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "lo que pasó" + S + "en la guardia", "4'"),
             ("2", "Llenen", "cada fila con su" + S + "equipo y su labor", "12'"),
             ("3", "Cierren", "el margen, los servicios" + S + "y la firma", "4'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 20 minutos · un parte firmado")
    return guardar(fig, "s10_como-trabajamos.png")


# ═══════════════════════════════ 25 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Qué equipo pusieron en la fila de carguío?",
             "¿En qué labor ocurrió el acarreo, y hacia dónde?",
             "¿Qué fila quedó vacía, y qué escribieron al margen?",
             "¿Qué mandaron a servicios de mina, y por qué?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 5, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».", CUERPO - 5, MARINO)
    nota(ax, 5, "El acarreo es la única fila con más de un destino.")
    return guardar(fig, "s10_puesta-en-comun.png")


# ═══════════════════════════════ 26 · qué sostiene el talud
def que_sostiene():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 10, H - 14, 80, 12, AMBAR)
    _txt(ax, 50, H - 8, "Si no lo sostiene una operación del ciclo…",
         CUERPO - 1, MARINO, bold=True)
    _txt(ax, 50, H - 24, "¿qué sostiene el talud?", FUERTE, MARINO, bold=True)
    y = H * 0.16
    _caja(ax, 5, y, 90, 20, MARINO)
    _txt(ax, 50, y + 13, "Y si nadie lo ejecuta durante la guardia,",
         CUERPO - 3, BLANCO)
    _txt(ax, 50, y + 6, "¿quién responde de que se cumpla?", CUERPO - 3, AMBAR, bold=True)
    nota(ax, 5, "Lo abre el instructor en plenario. No se entrega ni se califica.")
    return guardar(fig, "s10_que-sostiene.png")


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
    _txt(ax, 50, y - 12, "135 minutos. Hoy salimos a la superficie:" + S +
         "las labores del tajo y su ciclo de minado.")
    return guardar(fig, "s10_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIONES 1 A 9", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "todo bajo tierra:" + S + "frente, tajeo, rampa y chimenea",
         CUERPO - 4, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 10", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "a cielo abierto:" + S + "el banco y su ciclo",
         CUERPO - 4, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "El ciclo es el mismo, y una de sus cinco" + S +
         "operaciones se queda abajo.", CUERPO - 3)
    return guardar(fig, "s10_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, lo_que_se_vio, labores_tajo, arriba_abajo,
              ciclo_superficie, mismo_distinto, cuatro_de_cinco, talud, parte_filas,
              servicios, el_formato, los_equipos, encargo, como_trabajamos,
              puesta_en_comun, que_sostiene):
        print(" ", f())
