# -*- coding: utf-8 -*-
"""Esquemas de la sesión 8 de EOM · Cálculo del perno.

Aquí se calcula por primera vez. La S7 dejó la ficha de partida; esta sesión
resuelve el dato que la cartilla no da y que el estándar delega —«longitud del
perno a usar: de acuerdo a estándar por tamaño de sección»— cuando la sección
de la labor no figura en la tabla.

El método es el del «peso muerto» de la Guía de criterios geomecánicos de
Osinergmin (2017), §9.1.1.3 y su Figura 9-4: altura de cuña = 0,5 × abertura,
peso del triángulo, y capacidad como suma de lo que cada perno ancla PASADA la
cuña. De ahí sale lo que más enseña la sesión: el perno del centro puede
aportar cero.

QUÉ SE DIBUJA Y QUÉ NO
    Se dibuja lo que no tiene cuerpo: cuentas, tablas, escalas y el armazón de
    la sesión. La cuña sobre la corona y el reparto del anclaje SON físicos y
    salen de figura de fuente: las dos funciones `componer_*` maquetan y
    rotulan esas figuras, no redibujan ni un trazo. Es el criterio de
    componer_cable_bolting.py y unir_formas_cuerpo.py.

Uso:  python gen_esquemas_sost_s8.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
import numpy as np
from PIL import Image

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, GRIS, MARINO, MORADO, NOTA, VERDE,
    guardar, lienzo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402
from gen_esquemas_sost_s1 import _cabecera  # noqa: E402
from gen_esquemas_sost_s2 import _cierre, _pasos, _tabla  # noqa: E402
from gen_esquemas_sost_s5 import _dos_columnas  # noqa: E402

CARPETA = "sost/s8/"
PLANOS = Path(__file__).resolve().parents[1] / "EOM" / "planos"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


def _bloque_datos(nombre, titulo, items, cierre, asp=1.45):
    """Una lista de datos con su origen. Copia local del helper de la S7: el
    de allá guarda siempre en `sost/s7/` y traía los esquemas de vuelta."""
    fig, ax = lienzo(asp)
    H = 100 / asp
    _cabecera(ax, 3.0, H * 0.86, 94.0, H * 0.085, titulo, MARINO, NOTA * 0.8)
    y = H * 0.86
    for dato, origen, color in items:
        y -= H * 0.125
        _redonda(ax, 3.0, y, 94.0, H * 0.105, CLARO)
        _caja(ax, 3.0, y, 1.5, H * 0.105, color)
        ax.text(8.0, y + H * 0.0525, dato, ha="left", va="center", family=F,
                fontsize=NOTA * 0.88, fontweight="bold", color=MARINO)
        ax.text(53.0, y + H * 0.0525, origen, ha="left", va="center", family=F,
                fontsize=NOTA * 0.80, color=GRIS)
    _cierre(ax, H, cierre, max(H * 0.04, y - H * 0.145))
    _g(fig, nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    _dos_columnas("sost-s8_de-donde-venimos.png",
                  ("LA S7 DEJÓ", "la ficha de partida\ncon sus seis datos", AZUL),
                  ("PERO UNO NO SALE", "de dónde vienen la longitud\ny el espaciamiento del perno", VERDE),
                  "Cuando la sección no está en el estándar, hay que sacarlo", asp=2.10,
                  guardar_en=_g)


# ════════════════════════════════════ 2 · la cuña con pernos (fuente)
def componer_cuna_con_pernos():
    """Maqueta y rotula la figura de la cuña sostenida con pernos.

    No redibuja nada: el dibujo sale tal cual de la fuente. Lo único que se
    añade son tres rótulos con la tipografía del kit, porque los de la figura
    original dan 9 pt proyectados y el piso del §11 es 14.
    """
    im = Image.open(PLANOS / "cubillas2017_cuna-con-pernos_referencia.png").convert("RGB")
    ancho_px, alto_px = im.size

    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    alto = H * 0.78
    ancho = alto * ancho_px / alto_px
    x0, y0 = 4.0, H * 0.14
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    # los rótulos, a la derecha, con su línea de guía hasta el dibujo
    xl = x0 + ancho + 3.0
    for texto, frac, color in (("La cuña que se puede\ndesprender", 0.74, MORADO),
                               ("El perno la pasa y ancla\nen roca sana", 0.90, AZUL),
                               ("Su peso baja sobre\nla corona", 0.50, GRIS)):
        y = y0 + alto * frac
        ax.plot([x0 + ancho - 2.0, xl - 1.5], [y, y], color=color, linewidth=1.4, zorder=3)
        ax.text(xl, y, texto, ha="left", va="center", family=F,
                fontsize=NOTA * 0.86, color=MARINO, linespacing=1.35)

    ax.text(50, H * 0.055, "Cubillas (2017), en Gómez Mendoza (2021), UNSAAC · Ilustración 10",
            ha="center", va="center", family=F, fontsize=NOTA * 0.62, color=GRIS)
    _g(fig, "sost-s8_la-cuna-con-pernos.png")


# ══════════════════════════════════════════ 3 · la mitad del ancho
def la_mitad_del_ancho():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(40.0, "LABOR"), (26.0, "ANCHO"), (26.0, "ALTURA DE LA CUÑA")]
    filas = [["Subnivel", "2,40 m", "1,20 m"],
             ["Galería", "3,00 m", "1,50 m"],
             ["Galería", "4,00 m", "2,00 m"],
             ["Rampa", "4,50 m", "2,25 m"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.80, H * 0.075, H * 0.095)
    ax.text(50, H * 0.235, "altura de la cuña  =  0,5  ×  ancho de la labor",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            fontweight="bold", color=MARINO)
    _cierre(ax, H, "Osinergmin la sitúa entre 0,3 y 0,5; se toma 0,5, que es el conservador",
            H * 0.06)
    _g(fig, "sost-s8_la-mitad-del-ancho.png")


# ═══════════════════════════════════════════ 4 · el peso de la cuña
def el_peso_de_la_cuna():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.70, 90.0, H * 0.17, CLARO)
    ax.text(50, H * 0.785, "peso muerto  =  ½  ×  ancho  ×  altura  ×  1 m  ×  densidad",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            fontweight="bold", color=MARINO)
    ax.text(50, H * 0.615, "la cuña es un triángulo: alta en el centro, nula en las cajas",
            ha="center", va="center", family=F, fontsize=NOTA * 0.88, color=GRIS)

    _redonda(ax, 10.0, H * 0.34, 80.0, H * 0.21, BLANCO)
    _caja(ax, 10.0, H * 0.545, 80.0, 1.0, VERDE)
    ax.text(50, H * 0.475, "LA RAMPA DE 4,50", ha="center", va="center", family=F,
            fontsize=NOTA * 0.8, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.385, "½ × 4,50 × 2,25 × 1 × 2,6  =  13,2 toneladas",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95, color=MARINO)
    _cierre(ax, H, "Se cuenta por cada metro de labor, no por toda la labor", H * 0.09)
    _g(fig, "sost-s8_el-peso-de-la-cuna.png")


# ═════════════════════════════ 5 · lo que queda fuera de la cuña (fuente)
def componer_fuera_de_la_cuna():
    """Maqueta y rotula el reparto del anclaje de la Figura 9-4.

    El dibujo —la cuña triangular, los pernos y sus arrastres a, b y c— sale
    tal cual de la guía. Se añaden los tres rótulos grandes porque los de la
    figura dan 11 pt proyectados, bajo el piso de 14 del §11.
    """
    im = Image.open(PLANOS / "osinergmin2017_fig9-4_anclaje-abc_referencia.png").convert("RGB")
    ancho_px, alto_px = im.size

    ASP = 1.15
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    # el ancho manda: con `alto` mandando, el dibujo se salia por arriba y se
    # comia su propia cabecera —«ADHERENCIA PASADA LA CUÑA»—, que es el rotulo
    # que explica la lamina
    ancho = 80.0
    alto = ancho * alto_px / ancho_px
    x0, y0 = 10.0, H * 0.40
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    # tres fichas, no cinco rotulos en linea: en linea se pisaban unos a otros
    for i, (rot, detalle, color) in enumerate(
            (("a", "junto a la caja\nancla 1,9 m → 18,5 t", VERDE),
             ("b", "intermedio\nancla 0,9 m → 11,7 t", AZUL),
             ("c", "el del centro\nancla 0,0 m → nada", MORADO))):
        x = 3.0 + i * 32.0
        _redonda(ax, x, H * 0.20, 30.0, H * 0.150, CLARO)
        _caja(ax, x, H * 0.20, 1.4, H * 0.150, color)
        ax.text(x + 5.0, H * 0.275, rot, ha="center", va="center", family=F,
                fontsize=CUERPO * 1.05, fontweight="bold", color=color)
        ax.text(x + 8.5, H * 0.275, detalle, ha="left", va="center", family=F,
                fontsize=NOTA * 0.64, color=MARINO, linespacing=1.3)

    _cierre(ax, H, "Un perno solo trabaja con lo que ancla fuera de la cuña", H * 0.055)
    ax.text(50, H * 0.022, "Osinergmin (2017), Guía de criterios geomecánicos · Figura 9-4",
            ha="center", va="center", family=F, fontsize=NOTA * 0.62, color=GRIS)
    _g(fig, "sost-s8_fuera-de-la-cuna.png")


# ══════════════════════════════════════ 6 · lo que aporta cada uno
def lo_que_aporta_cada_uno():
    ASP = 1.52
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(34.0, "PERNO"), (24.0, "ANCLA"), (34.0, "APORTA")]
    filas = [["a · junto a la caja", "1,9 m", "18,5 t · tope del acero"],
             ["b", "0,9 m", "11,7 t · 0,9 × 13"],
             ["c · el del centro", "0,0 m", "0 t"],
             ["b", "0,9 m", "11,7 t"],
             ["a · junto a la caja", "1,9 m", "18,5 t"]]
    y = _tabla(ax, H, 3.0, cols, filas, H * 0.83, H * 0.068, H * 0.082)
    _redonda(ax, 3.0, y - H * 0.10, 94.0, H * 0.085, AMBAR)
    ax.text(50, y - H * 0.0575, "CAPACIDAD DE LA FILA   ·   60 toneladas",
            ha="center", va="center", family=F, fontsize=NOTA * 0.95,
            fontweight="bold", color=MARINO)
    ax.text(50, H * 0.055, "cada metro anclado da 13 t · ninguno pasa de lo que resiste su acero",
            ha="center", va="center", family=F, fontsize=NOTA * 0.8, color=GRIS)
    _g(fig, "sost-s8_lo-que-aporta-cada-uno.png")


# ═════════════════════════════════════════ 7 · el factor de seguridad
def el_factor_de_seguridad():
    ASP = 1.70
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 6.0, H * 0.68, 88.0, H * 0.20, CLARO)
    ax.text(50, H * 0.805, "FACTOR DE SEGURIDAD  =  capacidad  ÷  peso muerto",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            fontweight="bold", color=MARINO)
    ax.text(50, H * 0.725, "60 t  ÷  19 t  =  3,2", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.95, color=GRIS)

    for x0, titulo, valor, color in ((8.0, "LABOR PERMANENTE", "tiene que pasar de 1,5", MARINO),
                                     (54.0, "LABOR TEMPORAL", "basta con 1,2", MORADO)):
        _redonda(ax, x0, H * 0.30, 38.0, H * 0.26, BLANCO)
        _caja(ax, x0, H * 0.555, 38.0, 1.0, color)
        ax.text(x0 + 19.0, H * 0.475, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.8, fontweight="bold", color=color)
        ax.text(x0 + 19.0, H * 0.375, valor, ha="center", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO)
    _cierre(ax, H, "Si el factor no llega, el sostenimiento propuesto no va", H * 0.08)
    _g(fig, "sost-s8_el-factor-de-seguridad.png")


# ═══════════════════════════════════════════════ 8 · si no pasa
def si_no_pasa():
    _dos_columnas("sost-s8_si-no-pasa.png",
                  ("ALARGAR EL PERNO", "suma anclaje en todos,\nsobre todo en el del centro", VERDE),
                  ("JUNTAR MÁS PERNOS", "agrega justo los que\nmenos aportan", MORADO),
                  "Primero se alarga; juntar es la segunda opción", asp=1.85,
                  guardar_en=_g)


# ═════════════════════════════════ 9 · de dónde sale el estándar
def de_donde_sale_el_estandar():
    ASP = 1.42
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("La cartilla dice el elemento", "«según estándar por sección de labor»"),
                   ("El estándar de la unidad da la medida", "este cálculo ya resuelto y redondeado"),
                   ("Si la sección figura, se ejecuta", "no se vuelve a comprobar nada"),
                   ("Si no figura, se propone y se comprueba", "y el cálculo queda escrito")],
           H * 0.76, H * 0.155)
    _cierre(ax, H, "Dos minas pueden pasar el factor con largos distintos", H * 0.055)
    _g(fig, "sost-s8_de-donde-sale-el-estandar.png")


# ═══════════════════════════════════════════════ 10 · la rampa 210
def la_rampa_210():
    ASP = 1.58
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.58, 90.0, H * 0.28, CLARO)
    _caja(ax, 5.0, H * 0.855, 90.0, 1.0, VERDE)
    ax.text(50, H * 0.775, "RAMPA 210  ·  labor permanente", ha="center", va="center",
            family=F, fontsize=NOTA * 0.82, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.675, "de 3,00 × 3,00  →  4,50 × 4,50", ha="center", va="center",
            family=F, fontsize=CUERPO * 1.05, color=MARINO)
    ax.text(50, H * 0.605, "entra scoop de 6 yd³ y volquetes de 30 t", ha="center",
            va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)

    _redonda(ax, 12.0, H * 0.26, 76.0, H * 0.22, BLANCO)
    _caja(ax, 12.0, H * 0.475, 76.0, 1.0, MORADO)
    ax.text(50, H * 0.405, "EL ESTÁNDAR DE LA UNIDAD", ha="center", va="center",
            family=F, fontsize=NOTA * 0.78, fontweight="bold", color=MORADO)
    ax.text(50, H * 0.315, "su tabla llega hasta 4,00 × 4,00", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.92, color=MARINO)
    _cierre(ax, H, "El geomecánico vuelve el jueves. El perno se pide hoy", H * 0.07)
    _g(fig, "sost-s8_la-rampa-210.png")


# ══════════════════════════════════════════ 11 · los datos que hay
def los_datos():
    _bloque_datos("sost-s8_los-datos.png",
                  "LO QUE HAY PARA DECIDIR",
                  [("Densidad de la roca · 2,6 t/m³", "del parte de mapeo", AZUL),
                   ("Adherencia · 13 t por metro", "del proveedor · macizo bajo 45 RMR", AZUL),
                   ("Ruptura de la barra · 18,5 t", "de la ficha del fabricante", MORADO),
                   ("Malla de perforación · 1,5 m", "la que maneja la empresa", MORADO),
                   ("Se venden 5, 6, 7 y 8 pies", "nada intermedio", VERDE)],
                  "Todo lo que hace falta está en el relato", asp=1.40)


# ══════════════════════════════════════ 12 · la ficha que se entrega
def ficha_encargo():
    ASP = 1.24
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    y = H * 0.90
    for rot in ("Altura de la cuña:", "Peso muerto por metro de labor:",
                "Perno que proponen:", "Lo que ancla cada perno de la fila:",
                "Lo que aporta cada uno:", "Capacidad de la fila:",
                "Factor de seguridad  ·  ¿pasa?:"):
        ax.text(3.0, y, rot, ha="left", va="center", family=F,
                fontsize=NOTA * 0.85, color=MARINO)
        _caja(ax, 3.0, y - H * 0.042, 94.0, 0.4, GRIS)
        y -= H * 0.108
    y -= H * 0.02
    ax.text(3.0, y, "Si no pasara, qué cambiarían primero y por qué:", ha="left",
            va="center", family=F, fontsize=NOTA * 0.85, color=MARINO)
    _caja(ax, 3.0, y - H * 0.042, 94.0, 0.4, GRIS)
    ax.text(50, H * 0.045, "Firma del equipo técnico: ____________", ha="center",
            va="center", family=F, fontsize=NOTA * 0.75, color=GRIS)
    _g(fig, "sost-s8_ficha-encargo.png")


# ═════════════════════════════════════════════ 13 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean el encargo y ubiquen los datos", 3, AZUL, H * 0.72),
                                ("Hagan la cuenta paso por paso", 14, MARINO, H * 0.53),
                                ("Escriban qué cambiarían si no pasa", 3, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 20 minutos · se entrega la ficha con la cuenta a la vista",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s8_como-trabajamos.png")


# ══════════════════════════════════════════════ 14 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por la cuña", "cuánto pesa y de dónde salió ese peso"),
                   ("Seguimos por el perno del centro", "cuánto ancló y cuánto aportó"),
                   ("Cerramos por el factor", "si pasa, y qué harían si no pasara")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s8_puesta-comun.png")


# ══════════════════════════════ 15 · lo que instaló una rampa de verdad
def lo_que_se_instalo():
    """La sección de la rampa Yumpag, con el resultado de comprobarla.

    El dibujo entra tal cual: no lleva texto propio, así que no hay piso de
    legibilidad que forzar. Lo que se añade son las dos cifras de la izquierda.
    """
    im = Image.open(PLANOS / "gomez2021_ilus83_seccion-filas_referencia.png").convert("RGB")
    ancho_px, alto_px = im.size

    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    # medido: con alto = 0,62 H el dibujo se salia 4,7 unidades por la derecha
    alto = H * 0.56
    ancho = alto * ancho_px / alto_px
    x0, y0 = 49.0, H * 0.27
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    _cabecera(ax, 4.0, H * 0.82, 44.0, H * 0.075, "RAMPA YUMPAG · 4,50 × 4,50", MARINO,
              NOTA * 0.72)
    y = H * 0.82
    for rot, val, color in (("Perno instalado", "helicoidal de 8 pies", AZUL),
                            ("Espaciamiento", "1,50 m", AZUL),
                            ("Peso muerto", "13,2 t por metro", MORADO),
                            ("Capacidad de la fila", "39,4 t", MORADO),
                            ("Factor de seguridad", "3,00", VERDE)):
        y -= H * 0.122
        _redonda(ax, 4.0, y, 44.0, H * 0.102, CLARO)
        _caja(ax, 4.0, y, 1.4, H * 0.102, color)
        ax.text(7.5, y + H * 0.068, rot, ha="left", va="center", family=F,
                fontsize=NOTA * 0.70, color=GRIS)
        ax.text(7.5, y + H * 0.032, val, ha="left", va="center", family=F,
                fontsize=NOTA * 0.88, fontweight="bold", color=MARINO)

    # esta linea pisaba la franja ambar: la franja ocupa de 0,03 a 0,13 de H
    ax.text(74.0, H * 0.215, "dos filas alternadas · ninguna en el piso",
            ha="center", va="center", family=F, fontsize=NOTA * 0.72, color=GRIS)
    _cierre(ax, H, "Una mina real lo instaló así, y el factor lo confirma", H * 0.03)
    _g(fig, "sost-s8_lo-que-se-instalo.png")


# ═══════════════════════════════════════════════ 16 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "¿Por qué el perno del centro\nes el que menos aporta?",
                 "La próxima: el perímetro, las filas\ny todo el pedido del tramo"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s8_reflexion.png")


TODOS = [de_donde_venimos, componer_cuna_con_pernos, la_mitad_del_ancho,
         el_peso_de_la_cuna, componer_fuera_de_la_cuna, lo_que_aporta_cada_uno,
         el_factor_de_seguridad, si_no_pasa, de_donde_sale_el_estandar,
         la_rampa_210, los_datos, ficha_encargo, como_trabajamos,
         puesta_comun, lo_que_se_instalo, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
