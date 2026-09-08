# -*- coding: utf-8 -*-
"""Sesión 1 · las láminas que pasan de DIBUJO A TABLA.

POR QUÉ EXISTE ESTE ARCHIVO
    Cuatro esquemas de la S1 dibujaban objetos FÍSICOS de cero: la labor
    partida en zonas de RMR, las tres medidas acotadas sobre un corte, dos
    labores sostenidas de distinta manera, y la misma labor abierta a tres
    anchos. La regla 3 del CLAUDE.md no lo permite: lo físico se extrae de
    fuente, y dibujarlo es inventarlo. La prueba de que no es un escrúpulo:
    uno de esos esquemas salió con las cajas de la veta invertidas y ningún
    verificador podía cazarlo (OBS-32).

    Pero al mirar QUÉ ENSEÑA cada una de esas cuatro láminas, ninguna enseña
    un objeto. Enseñan una RELACIÓN:

        · el RMR cambia según la zona de la labor, no según el ancho
        · potencia, ancho de minado y sección son tres cosas distintas
        · el sostenimiento pasivo espera la carga; el activo la anticipa
        · con el mismo RMR, el sostenimiento mueve la abertura admisible

    Una relación no se fotografía: se tabula. Y una tabla sí se dibuja —está
    en el repertorio del §11— porque no tiene geometría que falsear. Ese es el
    criterio: **si lo que enseña la lámina es una relación, va a tabla; si es
    un objeto, va a fuente.**

    Es la salida 1 de las cuatro que hay cuando no aparece el plano: cambiar la
    pregunta, no la fuente.

DE DÓNDE SALEN LOS DATOS
    De la tabla geomecánica del caso de la sesión, que a su vez sale de la
    U.M. Parcoy (Consorcio Minero Horizonte, tesis UNSAAC) y del Art. 33 del
    D.S. 024-2016-EM, que obliga a publicarla en cada labor. No hay ninguna
    cifra inventada aquí: las cuatro filas —Regular A, Regular B, Mala A,
    Mala B— son las del RECURSO 2 de `casos.csv`.

Métrica del §11: lienzo 1500 px, cuerpo 52 px, sin bbox_inches, sin título
dentro (el título lo pone la lámina).

Uso:  python gen_esquemas_s1_tablas.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import Rectangle

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, PROPORCION, VERDE, guardar, lienzo, nota,
)


def _celda(ax, x, y, w, h, txt, fondo, tinta=MARINO, negrita=False, tam=None):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fondo, edgecolor=BLANCO, lw=2.0))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", family=F,
            fontsize=tam or CUERPO, color=tinta, linespacing=1.30,
            fontweight="bold" if negrita else "normal")


def _tabla(ax, x0, y0, anchos, alto_fila, cabecera, filas, colores_fila=None,
           destacar=None, tam_cab=None, tam_cel=None):
    """Tabla de cabecera oscura y filas alternas. `destacar` pinta una celda en ámbar."""
    y = y0
    x = x0
    for w, txt in zip(anchos, cabecera):
        _celda(ax, x, y, w, alto_fila, txt, MARINO, BLANCO, True, tam_cab or CUERPO)
        x += w
    for i, fila in enumerate(filas):
        y -= alto_fila
        x = x0
        base = colores_fila[i] if colores_fila else (CLARO if i % 2 == 0 else BLANCO)
        for j, (w, txt) in enumerate(zip(anchos, fila)):
            es = destacar and (i, j) in destacar
            _celda(ax, x, y, w, alto_fila, txt,
                   AMBAR if es else base, MARINO, es or j == 0, tam_cel or CUERPO)
            x += w
    return y


# ═══════════════════════════════════ 15 · el RMR es del terreno, no de la labor
def rmr_tres_zonas():
    """Antes: la labor dibujada partida en tres bandas. Ahora: qué zona tiene
    qué RMR y qué se sigue de eso. La labor no hace falta para entenderlo."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 6, H - 18, [26, 18, 44], 13,
               ["ZONA", "RMR", "QUÉ SE SIGUE DE ESO"],
               [["Caja techo", "40", "es la que puede caer:\nmanda el sostenimiento"],
                ["Mineral", "55", "más competente,\nno decide la abertura"],
                ["Caja piso", "40", "sostiene el piso\ny los equipos"]],
               colores_fila=[CLARO, BLANCO, CLARO], destacar={(0, 1)},
               tam_cab=NOTA, tam_cel=NOTA)
    ax.text(50, y - 12, "El RMR lo trae el mapeo geomecánico.\n"
                        "No cambia porque se abra más o menos ancho.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)
    nota(ax, 6, "Datos de la ficha de labor del caso · RMR de cajas 40.")
    return guardar(fig, "s1_rmr-tres-zonas.png")


# ═══════════════════════════════════════ 16 · tres medidas que no son la misma
def tres_medidas_tabla():
    """Antes: las tres cotas dibujadas sobre un corte inventado. Ahora: qué es
    cada una y QUIÉN la decide, que es lo que el alumno confunde."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 5, H - 18, [24, 32, 32], 13,
               ["MEDIDA", "QUÉ ES", "QUIÉN LA DECIDE"],
               [["Potencia", "lo que mide la veta\nentre sus dos cajas", "la geología:\nes un dato"],
                ["Ancho de\nminado", "lo que se rompe\nen cada disparo", "la mina:\nes una decisión"],
                ["Sección", "el hueco por donde\ncircula el equipo", "el equipo\nque tiene que entrar"]],
               colores_fila=[CLARO, BLANCO, CLARO], tam_cab=NOTA, tam_cel=NOTA)
    ax.text(50, y - 12, "El ancho de minado nunca es menor que la potencia,\n"
                        "y casi siempre es mayor.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)
    nota(ax, 6, "Confundir potencia con ancho de minado es el error más común.")
    return guardar(fig, "comun/tres-medidas-tabla.png")


# ═══════════════════════════════════════════ 19 · sostenimiento pasivo y activo
def pasivo_activo_tabla():
    """Antes: dos labores dibujadas con la carga cayendo. Ahora: en qué se
    diferencian, que es lo único que la lámina pide distinguir."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 5, H - 18, [22, 33, 33], 13,
               ["", "PASIVO", "ACTIVO"],
               [["Cuándo\ntrabaja", "cuando la roca\nya se movió", "antes de que\nla roca se mueva"],
                ["Con qué", "cuadros de madera,\ncimbras", "pernos Hydrabolt,\nshotcrete"],
                ["Qué hace\ncon la carga", "la recibe", "la reparte dentro\ndel macizo"]],
               colores_fila=[CLARO, BLANCO, CLARO], tam_cab=NOTA, tam_cel=NOTA)
    ax.text(50, y - 12, "Con el mismo RMR, el activo permite abrir mucho más.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO)
    nota(ax, 6, "La tabla geomecánica de la labor dice cuál toca en cada caso.")
    return guardar(fig, "comun/pasivo-activo-tabla.png")


# ══════════════════════════════════════ 20 · el sostenimiento mueve el límite
def sostenimiento_abertura():
    """Antes: la misma labor dibujada tres veces con anchos distintos. Ahora:
    la fila de la tabla geomecánica que lo dice, con los números del caso."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 4, H - 18, [30, 30, 32], 13,
               ["SOSTENIMIENTO", "ABERTURA QUE\nHABILITA", "TIEMPO DE\nAUTOSOPORTE"],
               [["Sin sostener", "3,0 m", "10 horas"],
                ["Pernos\nsistemáticos", "8,0 m", "1 semana"],
                ["Shotcrete SFR\n+ Hydrabolt", "12,0 m", "—"]],
               colores_fila=[CLARO, BLANCO, CLARO], destacar={(2, 1)},
               tam_cab=NOTA, tam_cel=NOTA)
    ax.text(50, y - 12, "Es el mismo macizo en los tres casos: RMR 40.\n"
                        "Lo que cambia es lo que se le pone encima.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)
    nota(ax, 6, "Tabla geomecánica de la labor · D.S. 024-2016-EM, Art. 33.")
    return guardar(fig, "comun/sostenimiento-abertura.png")


# ══════════════════════════════════════ 12 · potencia y buzamiento: cómo se miden
def escala_buzamiento():
    """Antes: el cuerpo dibujado a 8, 45 y 70 grados, con un pie que afirmaba
    «sobre 50 grados el carguío lo hace la gravedad» SIN FUENTE. Se cayó la
    afirmación y se cayó el dibujo: queda la escala, que es lo que la lámina
    enseña, y un caso real que la ancla."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 6, H - 18, [22, 30, 36], 13,
               ["BUZAMIENTO", "CÓMO SE LE DICE", "CÓMO SE MIDE"],
               [["8° – 20°", "tendida,\ncasi echada", "el ángulo entre la veta\ny la horizontal"],
                ["45°", "intermedia", "nunca a lo largo\nde la veta"],
                ["70° – 79°", "parada,\ncasi vertical", "se lee en la ficha\nde la labor"]],
               colores_fila=[CLARO, BLANCO, CLARO], destacar={(2, 0)},
               tam_cab=NOTA, tam_cel=NOTA)
    ax.text(50, y - 12, "La potencia se mide perpendicular a las cajas.\n"
                        "El buzamiento, contra la horizontal.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)
    nota(ax, 6, "Caso real: tajeo 882, buzamiento 79° y RMR 57 · tesis UNDAC.")
    return guardar(fig, "s1_escala-buzamiento.png")


if __name__ == "__main__":
    for f in (escala_buzamiento, rmr_tres_zonas, tres_medidas_tabla,
              pasivo_activo_tabla, sostenimiento_abertura):
        print(" ", f())
