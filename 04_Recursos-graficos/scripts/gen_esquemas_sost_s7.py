# -*- coding: utf-8 -*-
"""Esquemas de la sesión 7 de EOM · Del mapeo al sostenimiento estándar.

Abre el bloque 2, el del cálculo. Aquí no se calcula todavía: se deja la ficha
de la que después salen todas las cantidades, y se aprende de dónde sale cada
dato —y de dónde NO, que es lo que el caso pone a prueba—.

Uso:  python gen_esquemas_sost_s7.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, GRIS, MARINO, MORADO, NOTA, VERDE,
    guardar, lienzo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402
from gen_esquemas_sost_s1 import _cabecera  # noqa: E402
from gen_esquemas_sost_s2 import _cierre, _pasos, _tabla  # noqa: E402
from gen_esquemas_sost_s5 import _dos_columnas  # noqa: E402

CARPETA = "sost/s7/"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


def _bloque_datos(nombre, titulo, items, cierre, asp=1.45):
    """Una lista de datos con su origen, cada uno en su tarjeta."""
    fig, ax = lienzo(asp)
    H = 100 / asp
    _cabecera(ax, 3.0, H * 0.84, 94.0, H * 0.09, titulo, MARINO, NOTA * 0.8)
    y = H * 0.84
    for dato, origen, color in items:
        y -= H * 0.135
        _redonda(ax, 3.0, y, 94.0, H * 0.115, CLARO)
        _caja(ax, 3.0, y, 1.5, H * 0.115, color)
        ax.text(8.0, y + H * 0.0575, dato, ha="left", va="center", family=F,
                fontsize=NOTA * 0.9, fontweight="bold", color=MARINO)
        ax.text(52.0, y + H * 0.0575, origen, ha="left", va="center", family=F,
                fontsize=NOTA * 0.82, color=GRIS)
        y -= H * 0.005
    # la franja va pegada a la ultima fila, no al pie del lienzo: con tres o
    # cuatro items el hueco de abajo se notaba
    _cierre(ax, H, cierre, max(H * 0.04, y - H * 0.155))
    _g(fig, nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    _dos_columnas("sost-s7_de-donde-venimos.png",
                  ("EL BLOQUE 1", "qué elemento le toca\na cada labor", AZUL),
                  ("EL BLOQUE 2", "cuánto material\nhay que pedir", VERDE),
                  "Saber qué va no basta: alguien tiene que decir cuánto", asp=2.10,
                  guardar_en=_g)


# ═══════════════════════════════════════ 2 · lo que trae el parte
def el_parte_de_mapeo():
    _bloque_datos("sost-s7_el-parte-de-mapeo.png",
                  "LO QUE TRAE EL PARTE DE MAPEO",
                  [("Fracturas por metro cuadrado", "del conteo en la celda", AZUL),
                   ("Condición de picota", "de la prueba en la caja", AZUL),
                   ("Presencia de agua", "de lo que se ve en el frente", AZUL),
                   ("Casilla GSI y calidad", "del cruce en la cartilla", VERDE)],
                  "Con esos tres datos sale la calidad, y no antes")


# ═══════════════════════════════════ 3 · lo que no trae el parte
def lo_que_falta_del_plano():
    _bloque_datos("sost-s7_lo-que-falta-del-plano.png",
                  "LO QUE NO TRAE EL PARTE, Y HAY QUE BUSCAR",
                  [("Tipo y sección de labor", "del plano", MORADO),
                   ("Avance por disparo", "del plan de minado", MORADO),
                   ("Longitud pendiente", "de lo que falta hasta el nivel", MORADO)],
                  "Todo eso cabe en una hoja que se llena antes de pedir")


# ══════════════════════════════════════ 4 · qué es el estándar
def que_es_el_estandar():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Es el documento propio de cada mina", "no vale el de la mina de al lado"),
                   ("Fija el espaciamiento y la longitud de perno", "por tamaño de sección de labor"),
                   ("La cartilla remite a él", "cuando en la fila pone «según estándar»"),
                   ("Dos minas, dos estándares", "para la misma sección y la misma roca")],
           H * 0.72, H * 0.155)
    _cierre(ax, H, "La cartilla dice qué elemento; el estándar dice con qué medida", H * 0.055)
    _g(fig, "sost-s7_que-es-el-estandar.png")


# ══════════════════════════════════ 5 · quién lo escribe y quién lo lee
def quien_lo_aprueba():
    _dos_columnas("sost-s7_quien-lo-aprueba.png",
                  ("LO APRUEBA GEOMECÁNICA", "y lo actualiza cuando\ncambian las condiciones", MORADO),
                  ("LO LEE EL TÉCNICO", "está publicado:\nno se recuerda de memoria", AZUL),
                  "El técnico no escribe el estándar, lo aplica", asp=1.75,
                  guardar_en=_g)


# ═════════════════════════════════════════ 6 · la ficha de partida
def ficha_de_partida():
    ASP = 1.34
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.86, 94.0, H * 0.085,
              "LOS SEIS DATOS DE LOS QUE SALE TODO EL PEDIDO", MARINO, NOTA * 0.78)
    seis = [("1", "Casilla GSI"), ("2", "Calidad con su banda de RMR"),
            ("3", "Tipo y sección de labor"), ("4", "Sostenimiento que corresponde"),
            ("5", "Espaciamiento"), ("6", "Longitud de perno")]
    y = H * 0.86
    for n, txt in seis:
        y -= H * 0.115
        _redonda(ax, 3.0, y, 94.0, H * 0.095, CLARO)
        _redonda(ax, 4.5, y + H * 0.014, H * 0.067, H * 0.067, AZUL)
        ax.text(4.5 + H * 0.0335, y + H * 0.0475, n, ha="center", va="center",
                family=F, fontsize=NOTA * 0.85, fontweight="bold", color=BLANCO)
        ax.text(14.0, y + H * 0.0475, txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.9, color=MARINO)
    ax.text(50, H * 0.115, "Ninguno se deduce después: se registra ahora",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "La ficha se firma: alguien responde por lo que dice", H * 0.02)
    _g(fig, "sost-s7_ficha-de-partida.png")


# ══════════════════════════════════ 7 · un dato mal escrito se multiplica
def un_dato_mal_escrito():
    ASP = 1.85
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    pasos = [("EL ESPACIAMIENTO", "un número en la ficha", AZUL),
             ("LOS PERNOS DE UNA FILA", "salen de dividir por él", MORADO),
             ("EL TRAMO ENTERO", "multiplica esa fila", VERDE)]
    x = 4.0
    for titulo, txt, color in pasos:
        _redonda(ax, x, H * 0.36, 28.0, H * 0.34, CLARO)
        _caja(ax, x, H * 0.665, 28.0, 1.0, color)
        ax.text(x + 14.0, H * 0.60, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.78, fontweight="bold", color=color)
        ax.text(x + 14.0, H * 0.47, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.82, color=MARINO)
        if x < 60:
            ax.annotate("", xy=(x + 31.0, H * 0.53), xytext=(x + 28.5, H * 0.53),
                        arrowprops=dict(arrowstyle="->", color=MARINO, linewidth=1.8))
        x += 31.5
    _cierre(ax, H, "Un dato mal escrito acá se multiplica en todo el pedido", H * 0.10)
    _g(fig, "sost-s7_un-dato-mal-escrito.png")


# ═══════════════════════════════════ 8 · el espaciamiento no se estira
def no_se_estira():
    ASP = 1.48
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Sale del cálculo de geomecánica", "no del avance ni del material que hay"),
                   ("Ampliarlo deja bloques sin coser", "el perno que falta no está en ningún lado"),
                   ("El reglamento obliga a mantenerse dentro", "art. 214 g) del D.S. 024-2016-EM"),
                   ("Si el material no alcanza, se pide", "no se estira")],
           H * 0.74, H * 0.155)
    _cierre(ax, H, "Cambiar el estándar es decisión de geomecánica, no de la guardia", H * 0.05)
    _g(fig, "sost-s7_no-se-estira.png")


# ═════════════════════════════════ 9 · lo que hereda la guardia siguiente
def la_guardia_siguiente():
    ASP = 1.90
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.52, 90.0, H * 0.28, CLARO)
    ax.text(50, H * 0.66, "Un espaciamiento cambiado en la labor\nno queda registrado en ninguna parte",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.26, AMBAR)
    ax.text(50, H * 0.27, "La guardia siguiente hereda un tramo que cree sostenido",
            ha="center", va="center", family=F, fontsize=NOTA * 0.95,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s7_la-guardia-siguiente.png")


# ══════════════════════════════════════════ 10 · la galería 480
def la_galeria_480():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(46.0, "LO QUE SE SABE"), (48.0, "DE DÓNDE SALE")]
    filas = [["Cuatro por cuatro", "del plano"],
             ["Tres metros por disparo", "del plan de minado"],
             ["Ochenta metros hasta la chimenea", "de lo que falta por avanzar"],
             ["Catorce fracturas por metro cuadrado", "del mapeo del viernes"],
             ["Se rompe con uno o dos golpes", "del mapeo del viernes"],
             ["Goteo desde los sesenta metros", "del mapeo del viernes"]]
    _tabla(ax, H, 2.0, cols, filas, H * 0.82, H * 0.085, H * 0.105, tam=NOTA * 0.82)
    ax.text(50, H * 0.075, "Entra a sostenerse el lunes",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _g(fig, "sost-s7_la-galeria-480.png")


# ═════════════════════════════════════ 11 · el parte de la guardia anterior
def el_parte_anterior():
    ASP = 1.95
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.46, 90.0, H * 0.34, BLANCO)
    _caja(ax, 5.0, H * 0.79, 90.0, 1.0, MORADO)
    ax.text(50, H * 0.70, "PARTE DE LA GUARDIA ANTERIOR  ·  otro tramo de la misma galería",
            ha="center", va="center", family=F, fontsize=NOTA * 0.78,
            fontweight="bold", color=GRIS)
    ax.text(50, H * 0.58, "espaciamiento mayor al del estándar",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO)
    ax.text(50, H * 0.50, "«no alcanzó el material»", ha="center", va="center",
            family=F, fontsize=NOTA * 0.9, color=GRIS)
    _cierre(ax, H, "«Si sale mal acá, sale mal todo lo demás»", H * 0.12)
    _g(fig, "sost-s7_el-parte-anterior.png")


# ═════════════════════════════════════════ 12 · la ficha que se entrega
def ficha_encargo():
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    y = H * 0.88
    for rot in ("Casilla GSI:", "Calidad y banda de RMR:", "Tipo y sección de labor:",
                "Sostenimiento que corresponde:", "Espaciamiento:", "Longitud de perno:"):
        ax.text(3.0, y, rot, ha="left", va="center", family=F,
                fontsize=NOTA * 0.85, color=MARINO)
        _caja(ax, 3.0, y - H * 0.048, 94.0, 0.4, GRIS)
        y -= H * 0.125
    y -= H * 0.03
    ax.text(3.0, y, "Por qué no se usa el espaciamiento que anotó la guardia anterior:",
            ha="left", va="center", family=F, fontsize=NOTA * 0.85, color=MARINO)
    _caja(ax, 3.0, y - H * 0.048, 94.0, 0.4, GRIS)
    ax.text(50, H * 0.05, "Firma del equipo técnico: ____________", ha="center",
            va="center", family=F, fontsize=NOTA * 0.75, color=GRIS)
    _g(fig, "sost-s7_ficha-encargo.png")


# ═════════════════════════════════════════════ 13 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean el parte del viernes y el plano", 3, AZUL, H * 0.72),
                                ("Llenen las seis casillas de la ficha", 9, MARINO, H * 0.53),
                                ("Escriban la línea del espaciamiento", 3, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 15 minutos · se entrega la ficha de partida",
            ha="center", va="center", family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
    _g(fig, "sost-s7_como-trabajamos.png")


# ══════════════════════════════════════════════ 14 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por la casilla y la calidad", "cómo salieron del parte"),
                   ("Seguimos por el espaciamiento", "de dónde lo sacaron"),
                   ("Cerramos por la línea del final", "por qué no se usa el de la guardia anterior")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s7_puesta-comun.png")


# ═══════════════════════════════════════════════ 15 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "«Lo que ustedes escriban acá\nes de donde salen las cantidades»",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Qué se arrastra si el espaciamiento sale mal de esta ficha?",
            ha="center", va="center", family=F, fontsize=NOTA * 0.95,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s7_una-ultima.png")


# ═══════════════════════════════════════════════ 16 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "De los seis datos de la ficha,\n¿cuál no está en el parte de mapeo?",
                 "La próxima: de dónde salen la longitud\ny el espaciamiento del perno"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s7_reflexion.png")


TODOS = [de_donde_venimos, el_parte_de_mapeo, lo_que_falta_del_plano,
         que_es_el_estandar, quien_lo_aprueba, ficha_de_partida,
         un_dato_mal_escrito, no_se_estira, la_guardia_siguiente,
         la_galeria_480, el_parte_anterior, ficha_encargo, como_trabajamos,
         puesta_comun, una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
