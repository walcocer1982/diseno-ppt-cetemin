# -*- coding: utf-8 -*-
"""Formas comunes a los esquemas de EOM · Fundamentos mecánicos de equipos mineros.

POR QUÉ EXISTE
    Las diez sesiones del curso tienen el mismo armazón —la ficha del caso, el
    encargo de cuatro filas, los pasos del trabajo en equipo, la puesta en
    común, el puente— y sus láminas de tema caen casi siempre en tres formas:
    una lista numerada, una comparativa de dos columnas o tres fichas. Escribir
    eso una vez por sesión son ochocientas líneas repetidas y ocho sitios donde
    equivocarse con el mismo solape.

    Aquí está cada forma UNA vez, con su reparto de alto ya resuelto. Lo que
    cambia por sesión son los textos, y eso vive en el script de la sesión.

LO QUE NO ESTÁ AQUÍ, Y NO VA A ESTAR
    Nada con cuerpo. Ni cortes, ni despieces, ni contornos de labor: eso sale
    del dibujo del fabricante (regla 3). Estas son cajas, flechas y tablas.

Métrica del §11: lienzo de 1500 px de ancho, cuerpo de 52 px, sin bbox_inches.
Van SIN título dentro: el título lo pone la lámina.
"""
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402,F401
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, cuerpo, guardar, lienzo, nota, rotulo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402,F401

ROJO = "#C0392B"          # solo lo que está mal, y con moderación (§11)
ROJO_CLARO = "#F7E4E1"    # su fondo, para que el rojo no grite


# ── piezas sueltas ────────────────────────────────────────────────────────
def _ancho(txt, tam):
    """Ancho aproximado del texto, en unidades del lienzo (100 = 1500 px).

    Arial en negrita mide ~0,55 em por carácter en minúsculas, pero las
    MAYÚSCULAS son bastante más anchas: ~0,68. Midiendo todo a 0,55 los rótulos
    en caja alta seguían saliéndose. A 200 dpi un punto son 2,78 px y una unidad
    son 15 px. No es exacto, y no hace falta: sirve para decidir si hay que bajar
    de punto antes de que el rótulo se salga de su caja.
    """
    em = 0.68 if txt == txt.upper() else 0.55
    return len(txt) * em * tam * (200 / 72) / 15


def partir(txt, ancho, tam, sangria=0.0):
    """Parte el texto en las líneas que caben en `ancho` unidades.

    Bajar de punto sirve para un rótulo de cabecera, que es corto. Para una
    frase larga NO sirve: una consigna de setenta caracteres tendría que bajar
    a ocho puntos proyectados, y a esa altura no se lee. Lo que corresponde es
    envolverla. Esto se descubrió con la lámina del encargo de la S3, donde
    cuatro consignas salían cortadas por la derecha sin que nada avisara.
    """
    em = 0.68 if txt == txt.upper() else 0.55
    por_caracter = em * tam * (200 / 72) / 15
    cabe = max(12, int((ancho - sangria) / por_caracter))
    if len(txt) <= cabe:
        return txt
    return chr(10).join(textwrap.wrap(txt, cabe))


def cabecera(ax, x, y, w, h, txt, color, tam=None):
    """Cabecera de columna. BAJA DE PUNTO sola si el rótulo no cabe.

    Con tamaño fijo, «LO QUE SOLO SE VE EN EL PRE-USO» se salía de su columna
    por los dos lados y nadie se enteraba: el verificador mide el cuerpo del
    esquema, no si un rótulo desborda su caja.
    """
    _caja(ax, x, y, w, h, color)
    tam = tam or NOTA * 0.92
    while tam > NOTA * 0.55 and _ancho(txt, tam) > w * 0.92:
        tam -= 0.4
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", family=F,
            fontsize=tam, fontweight="bold", color=BLANCO)


def flecha_abajo(ax, x, y, alto=2.4, color=GRIS):
    ax.annotate("", xy=(x, y - alto), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=2.4))


def flecha_der(ax, x, y, largo=4.0, color=GRIS):
    ax.annotate("", xy=(x + largo, y), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=2.4))


def banda(ax, y, alto, texto, x0=3.0, ancho=94.0, color=AMBAR, tinta=MARINO):
    """La idea que hay que llevarse, al pie del esquema."""
    _redonda(ax, x0, y, ancho, alto, color)
    ax.text(x0 + ancho / 2, y + alto / 2, partir(texto, ancho - 6, NOTA),
            ha="center", va="center", family=F, fontsize=NOTA,
            fontweight="bold", color=tinta, linespacing=1.3)


def _salida(carpeta):
    """Devuelve la función de guardado de una sesión: `fmeq/s5/` y su prefijo."""
    def _g(fig, nombre):
        guardar(fig, carpeta + nombre)
    return _g


# ── las formas ────────────────────────────────────────────────────────────
def lista_numerada(guardar_en, archivo, items, pie=None, cierre=None,
                   colores=None, asp=1.25):
    """Pasos o filas numeradas. items = [texto, ...]

    El alto se reparte ANTES de trazar: las cajas, el cierre opcional y la
    banda tienen su tramo. Encadenando restas es como se monta una encima de
    otra, y eso ya pasó tres veces.
    """
    fig, ax = lienzo(asp)
    H = 100 / asp
    colores = colores or [AZUL, MARINO, VERDE, MORADO, AZUL, MARINO, VERDE]

    y_banda = H * 0.05 if pie else 0.0
    alto_banda = H * 0.11 if pie else 0.0
    alto_cierre = H * 0.14 if cierre else 0.0
    tope = H * 0.94
    piso = y_banda + alto_banda + (alto_cierre + H * 0.05 if cierre else H * 0.03)
    hueco = H * 0.018
    alto = (tope - piso - hueco * (len(items) - 1)) / len(items)

    y = tope - alto
    for i, t in enumerate(items):
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 12, alto, colores[i % len(colores)])
        ax.text(9, y + alto / 2, str(i + 1), ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(17, y + alto / 2, partir(t, 80, NOTA * 0.92), ha="left",
                va="center", family=F, fontsize=NOTA * 0.92, color=MARINO,
                linespacing=1.3)
        y -= alto + hueco
    if cierre:
        _redonda(ax, 3, y_banda + alto_banda + H * 0.04, 94, alto_cierre, MARINO)
        ax.text(50, y_banda + alto_banda + H * 0.04 + alto_cierre / 2,
                partir(cierre, 88, CUERPO * 0.92), ha="center", va="center",
                family=F, fontsize=CUERPO * 0.92, fontweight="bold",
                color=BLANCO, linespacing=1.3)
    if pie:
        banda(ax, y_banda, alto_banda, pie)
    guardar_en(fig, archivo)


def dos_columnas(guardar_en, archivo, izq, der, filas, pie=None, asp=1.25,
                 color_izq=AZUL, color_der=VERDE, fondo_der=CLARO, rotulos=None):
    """Comparativa de dos columnas. filas = [(izquierda, derecha), ...]

    Con `rotulos` se antepone una columna estrecha de etiquetas.
    """
    fig, ax = lienzo(asp)
    H = 100 / asp

    x0 = 3.0
    w_rot = 22.0 if rotulos else 0.0
    w = (94.0 - w_rot - 1.0) / 2
    y = H * 0.80
    cabecera(ax, x0 + w_rot, y, w, H * 0.12, izq, color_izq)
    cabecera(ax, x0 + w_rot + w + 1.0, y, w, H * 0.12, der, color_der)

    piso = (H * 0.05 + H * 0.11 + H * 0.04) if pie else H * 0.04
    hueco = 1.0
    alto = (y - piso - hueco * len(filas)) / len(filas)
    for i, (a, b) in enumerate(filas):
        y -= alto + hueco
        if rotulos:
            _celda(ax, x0, y, w_rot, alto, rotulos[i], BLANCO, GRIS, negrita=True,
                   tam=NOTA * 0.78)
        _celda(ax, x0 + w_rot, y, w, alto, a, CLARO, MARINO, tam=NOTA * 0.90)
        _celda(ax, x0 + w_rot + w + 1.0, y, w, alto, b, fondo_der, MARINO,
               tam=NOTA * 0.90)
    if pie:
        banda(ax, H * 0.05, H * 0.11, pie)
    guardar_en(fig, archivo)


def tres_fichas(guardar_en, archivo, titulo, fichas, pie=None, asp=1.10):
    """Tres tarjetas con cabecera de color. fichas = [(TÍTULO, color, texto, pie)]"""
    fig, ax = lienzo(asp)
    H = 100 / asp

    if titulo:
        ax.text(50, H * 0.93, titulo, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=MARINO)
    tope = H * (0.85 if titulo else 0.92)
    piso = (H * 0.10 + H * 0.13) if pie else H * 0.06
    alto = tope - piso
    x = 3
    for nombre, color, texto, detalle in fichas:
        _redonda(ax, x, piso, 30.5, alto, CLARO)
        _redonda(ax, x, tope - H * 0.13, 30.5, H * 0.13, color)
        ax.text(x + 15.25, tope - H * 0.065, nombre, ha="center", va="center",
                family=F, fontsize=NOTA * 0.90, fontweight="bold",
                color=MARINO if color == AMBAR else BLANCO, linespacing=1.3)
        ax.text(x + 15.25, piso + alto * 0.60, texto, ha="center", va="center",
                family=F, fontsize=NOTA * 0.90, color=MARINO, linespacing=1.35)
        if detalle:
            ax.text(x + 15.25, piso + alto * 0.28, detalle, ha="center",
                    va="center", family=F, fontsize=NOTA * 0.86, color=GRIS,
                    linespacing=1.35)
        x += 32.2
    if pie:
        banda(ax, H * 0.10, H * 0.13, pie)
    guardar_en(fig, archivo)


def ficha_caso(guardar_en, archivo, empresa, subtitulo, hechos, pie_nota=None,
               asp=1.16):
    """La ficha del caso: cabecera con la empresa y los hechos en dos columnas."""
    fig, ax = lienzo(asp)
    H = 100 / asp

    _redonda(ax, 3, H * 0.80, 94, H * 0.15, AZUL)
    ax.text(50, H * 0.895, empresa, ha="center", va="center", family=F,
            fontsize=CUERPO * 0.95, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.833, subtitulo, ha="center", va="center", family=F,
            fontsize=NOTA * 0.90, color=BLANCO)

    tope, piso = H * 0.76, H * (0.12 if pie_nota else 0.05)
    hueco = 1.0
    alto = (tope - piso - hueco * len(hechos)) / len(hechos)
    y = tope
    for rot, det in hechos:
        y -= alto + hueco
        _celda(ax, 3, y, 32, alto, rot, CLARO, GRIS, negrita=True, tam=NOTA * 0.80)
        _celda(ax, 36, y, 61, alto, det, BLANCO, MARINO, tam=NOTA * 0.88)
    if pie_nota:
        nota(ax, H * 0.055, pie_nota)
    guardar_en(fig, archivo)


def antes_de_resolver(guardar_en, archivo, pregunta, fichas, asp=1.60):
    """La pregunta gatilladora y los tres datos que aprietan."""
    fig, ax = lienzo(asp)
    H = 100 / asp

    _redonda(ax, 3, H * 0.58, 94, H * 0.30, MARINO)
    ax.text(50, H * 0.73, pregunta, ha="center", va="center", family=F,
            fontsize=CUERPO * 0.95, fontweight="bold", color=BLANCO,
            linespacing=1.4)
    x = 3
    for grande, det in fichas:
        _redonda(ax, x, H * 0.14, 30.5, H * 0.36, CLARO)
        ax.text(x + 15.25, H * 0.41, grande, ha="center", va="center", family=F,
                fontsize=CUERPO * 0.95, fontweight="bold", color=AZUL)
        ax.text(x + 15.25, H * 0.26, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.86, color=MARINO, linespacing=1.35)
        x += 32.2
    guardar_en(fig, archivo)


def puesta_comun(guardar_en, archivo, partes, pie, titulo="Dos minutos por equipo"):
    """Afirmación · apoyo · pregunta, con lo que toca a esta sesión."""
    tres_fichas(guardar_en, archivo, titulo,
                [(n, c, t, "") for n, c, t in partes], pie, asp=1.30)


def puente(guardar_en, archivo, prox_titulo, prox_texto, cierre_titulo,
           cierre_texto, remate, pie=None, asp=1.45):
    """Adónde va la sesión: la siguiente y el colaborativo del bloque."""
    fig, ax = lienzo(asp)
    H = 100 / asp

    _redonda(ax, 3, H * 0.56, 45, H * 0.32, AZUL)
    ax.text(25.5, H * 0.80, prox_titulo, ha="center", va="center", family=F,
            fontsize=NOTA * 0.90, fontweight="bold", color=BLANCO)
    ax.text(25.5, H * 0.66, prox_texto, ha="center", va="center", family=F,
            fontsize=NOTA * 0.88, color=BLANCO, linespacing=1.4)
    _redonda(ax, 52, H * 0.56, 45, H * 0.32, AMBAR)
    ax.text(74.5, H * 0.80, cierre_titulo, ha="center", va="center", family=F,
            fontsize=NOTA * 0.90, fontweight="bold", color=MARINO)
    ax.text(74.5, H * 0.66, cierre_texto, ha="center", va="center", family=F,
            fontsize=NOTA * 0.88, color=MARINO, linespacing=1.4)
    ax.text(50, H * 0.34, remate, ha="center", va="center", family=F,
            fontsize=NOTA, color=MARINO, linespacing=1.4)
    if pie:
        nota(ax, H * 0.12, pie)
    guardar_en(fig, archivo)
