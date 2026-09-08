# -*- coding: utf-8 -*-
"""Esquemas de la sesión 9 de EOM · El requerimiento del tramo.

La S8 resolvió el perno: qué largo y a qué espaciamiento. Esta sesión lo
convierte en pedido —perímetro, pernos de una fila, filas del tramo, total,
metros de malla con su traslape y accesorios— y enseña por qué un pedido puede
cuadrar en el papel y faltar en la labor.

Las cifras del encargo cierran solas: galería de 4 × 4 con arco de radio 2,00,
perímetro sin piso de 10,28 m, perno de 7 pies a 1,20 m → 9 pernos por fila,
100 filas, 900 pernos y 1 234 m² de contorno.

QUÉ SE DIBUJA Y QUÉ NO
    Se dibujan las cuentas, las tablas y el armazón. Lo físico entra de fuente:
    dos composiciones sobre figura —la malla de instalación real y la sección
    con su contorno— y dos planos que ya estaban catalogados, el de la malla
    traslapada y el del perno helicoidal con su placa y su tuerca.

Uso:  python gen_esquemas_sost_s9.py
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

CARPETA = "sost/s9/"
PLANOS = Path(__file__).resolve().parents[1] / "EOM" / "planos"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    _dos_columnas("sost-s9_de-donde-venimos.png",
                  ("LA S8 RESOLVIÓ", "qué perno va\ny cada cuánto", AZUL),
                  ("HOY SE PIDE", "cuántos, cuánta malla\ny con qué accesorios", VERDE),
                  "Saber qué perno va no llena un vale: hay que contarlo", asp=2.10,
                  guardar_en=_g)


# ═══════════════════════════════════ 2 · la malla de una mina (fuente)
def componer_malla_real():
    """Maqueta y rotula la malla de instalación de pernos de una mina real.

    El dibujo —los pernos y sus cotas— sale tal cual de la tesis. Sus propias
    cotas dan 3 pt proyectados, muy por debajo del piso de 14 del §11, así que
    se rotulan aparte con la tipografía del kit.
    """
    im = Image.open(PLANOS / "gomez2021_ilus85_malla-tresbolillo_referencia.png").convert("RGB")
    ancho_px, alto_px = im.size

    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    # medido: con ancho 92 el dibujo pedia 38,2 unidades de alto y se salia 6 por
    # arriba, encima del titulo
    ancho = 76.0
    alto = ancho * alto_px / ancho_px
    x0, y0 = 12.0, H * 0.33
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    ax.text(50, H * 0.94, "LA MALLA DE PERNOS DE UNA RAMPA REAL", ha="center",
            va="center", family=F, fontsize=NOTA * 0.9, fontweight="bold", color=MARINO)
    ax.text(50, H * 0.88, "cada círculo es un perno · las cotas están en metros",
            ha="center", va="center", family=F, fontsize=NOTA * 0.78, color=GRIS)

    _redonda(ax, 7.0, H * 0.14, 86.0, H * 0.16, AMBAR)
    ax.text(50, H * 0.22, "¿Cuántos pernos hay en un metro de esta labor?",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            fontweight="bold", color=MARINO)
    ax.text(50, H * 0.055, "Gómez Mendoza (2021), UNSAAC · Ilustración 85", ha="center",
            va="center", family=F, fontsize=NOTA * 0.62, color=GRIS)
    _g(fig, "sost-s9_la-malla-real.png")


# ══════════════════════════════════ 3 · el contorno que se sostiene
def componer_el_contorno():
    """Maqueta la sección real y marca qué parte del contorno lleva perno.

    El dibujo sale tal cual de la tesis; lo que se añade son los tres rótulos.
    No lleva texto propio, así que no hay piso de legibilidad que forzar.
    """
    im = Image.open(PLANOS / "gomez2021_ilus83_seccion-filas_referencia.png").convert("RGB")
    ancho_px, alto_px = im.size

    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    alto = H * 0.60
    ancho = alto * ancho_px / alto_px
    x0, y0 = 4.0, H * 0.30
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    xl = x0 + ancho + 3.0
    for texto, frac, color in (("La corona lleva perno", 0.92, AZUL),
                               ("Las dos cajas también,\ndesarrolladas", 0.55, AZUL),
                               ("El piso no: por ahí\nse transita", 0.08, MORADO)):
        y = y0 + alto * frac
        ax.plot([x0 + ancho - 3.0, xl - 1.5], [y, y], color=color, linewidth=1.4, zorder=3)
        ax.text(xl, y, texto, ha="left", va="center", family=F,
                fontsize=NOTA * 0.84, color=MARINO, linespacing=1.35)

    _cierre(ax, H, "El perímetro sostenido es el contorno por donde puede caer roca", H * 0.10)
    ax.text(50, H * 0.035, "Gómez Mendoza (2021), UNSAAC · Ilustración 83", ha="center",
            va="center", family=F, fontsize=NOTA * 0.62, color=GRIS)
    _g(fig, "sost-s9_el-contorno.png")


# ═════════════════════════════════════════ 4 · los pernos de una fila
def los_pernos_de_una_fila():
    ASP = 1.58
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.70, 90.0, H * 0.17, CLARO)
    ax.text(50, H * 0.785, "pernos de una fila  =  perímetro  ÷  espaciamiento",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            fontweight="bold", color=MARINO)
    ax.text(50, H * 0.615, "una fila es el anillo de pernos de una misma posición",
            ha="center", va="center", family=F, fontsize=NOTA * 0.88, color=GRIS)

    _redonda(ax, 10.0, H * 0.32, 80.0, H * 0.23, BLANCO)
    _caja(ax, 10.0, H * 0.545, 80.0, 1.0, VERDE)
    ax.text(50, H * 0.475, "LA GALERÍA DE 4 × 4", ha="center", va="center", family=F,
            fontsize=NOTA * 0.8, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.395, "10,28 m  ÷  1,20 m  =  8,57", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.95, color=MARINO)
    ax.text(50, H * 0.345, "se redondea hacia arriba:  9 pernos", ha="center",
            va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "Hacia arriba siempre: no existe medio perno", H * 0.08)
    _g(fig, "sost-s9_los-pernos-de-una-fila.png")


# ═════════════════════════════════════════ 5 · las filas del tramo
def las_filas_del_tramo():
    ASP = 1.58
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.70, 90.0, H * 0.17, CLARO)
    ax.text(50, H * 0.785, "filas del tramo  =  longitud del tramo  ÷  espaciamiento",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.88,
            fontweight="bold", color=MARINO)
    ax.text(50, H * 0.615, "el tramo es lo que falta por sostener, no lo ya avanzado",
            ha="center", va="center", family=F, fontsize=NOTA * 0.88, color=GRIS)

    _redonda(ax, 10.0, H * 0.32, 80.0, H * 0.23, BLANCO)
    _caja(ax, 10.0, H * 0.545, 80.0, 1.0, VERDE)
    ax.text(50, H * 0.475, "EL TRAMO DE 120 METROS", ha="center", va="center", family=F,
            fontsize=NOTA * 0.8, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.395, "120 m  ÷  1,20 m  =  100 filas", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.95, color=MARINO)
    ax.text(50, H * 0.345, "la fila que ya está puesta no se vuelve a pedir", ha="center",
            va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "Con la fila resuelta, el tramo es multiplicar", H * 0.08)
    _g(fig, "sost-s9_las-filas-del-tramo.png")


# ══════════════════════════════════════════════ 6 · el total de pernos
def el_total_de_pernos():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(44.0, "LÍNEA DEL PEDIDO"), (46.0, "DE DÓNDE SALE")]
    filas = [["Perímetro sostenido · 10,28 m", "de la sección, sin el piso"],
             ["Pernos por fila · 9", "10,28 ÷ 1,20, hacia arriba"],
             ["Filas del tramo · 100", "120 ÷ 1,20"],
             ["Total de pernos · 900", "9 × 100"],
             ["Longitud · 7 pies", "del cálculo de la sesión pasada"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.83, H * 0.072, H * 0.098)
    ax.text(50, H * 0.175, "el total se anota siempre con su longitud al costado",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "Sin la longitud, almacén despacha lo que tiene a mano", H * 0.05)
    _g(fig, "sost-s9_el-total-de-pernos.png")


# ═══════════════════════════════════════════ 7 · los metros de malla
def los_metros_de_malla():
    ASP = 1.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.72, 90.0, H * 0.16, CLARO)
    ax.text(50, H * 0.80, "área del contorno  =  perímetro  ×  longitud del tramo",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.90,
            fontweight="bold", color=MARINO)

    _redonda(ax, 10.0, H * 0.44, 80.0, H * 0.22, BLANCO)
    _caja(ax, 10.0, H * 0.655, 80.0, 1.0, VERDE)
    ax.text(50, H * 0.585, "LA GALERÍA 615", ha="center", va="center", family=F,
            fontsize=NOTA * 0.8, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.500, "10,28 m  ×  120 m  =  1 234 m²", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.95, color=MARINO)

    ax.text(50, H * 0.345, "la malla cubre la misma superficie que llevan los pernos",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    ax.text(50, H * 0.275, "pero ese número todavía no es lo que se pide",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9,
            fontweight="bold", color=MORADO)
    _cierre(ax, H, "El área del contorno es el piso del pedido, no el pedido", H * 0.075)
    _g(fig, "sost-s9_los-metros-de-malla.png")


# ═══════════════════════════════════════════════ 8 · el traslape
def el_traslape():
    ASP = 1.48
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Las hojas no se ponen borde con borde", "cada una monta sobre la vecina"),
                   ("Esa franja de montaje es el traslape", "y se pierde en cobertura"),
                   ("Se suma aparte, en su propia línea", "no se estima dentro del área"),
                   ("Sin él, la malla cuadra y falta abajo", "a los sesenta metros se acabó")],
           H * 0.76, H * 0.155)
    _cierre(ax, H, "El área y el traslape van en líneas separadas", H * 0.055)
    _g(fig, "sost-s9_el-traslape.png")


# ═════════════════════════════════════════════ 9 · los accesorios
def los_accesorios():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(44.0, "POR CADA PERNO"), (46.0, "CUÁNTOS")]
    filas = [["Platina de 20 × 20 cm", "una, sin excepción"],
             ["Tuerca esférica", "una, sin excepción"],
             ["Cartucho de resina", "según el largo del perno"],
             ["Cartucho de cemento", "según el largo del perno"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.84, H * 0.072, H * 0.098)
    _redonda(ax, 3.0, H * 0.20, 94.0, H * 0.115, CLARO)
    ax.text(50, H * 0.2575, "el de siete pies lleva dos resinas y cuatro cementos;\n"
                            "uno más corto lleva menos, y la tabla no es la misma",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85,
            color=MARINO, linespacing=1.35)
    _cierre(ax, H, "Los accesorios se cuentan desde el total de pernos", H * 0.055)
    _g(fig, "sost-s9_los-accesorios.png")


# ═══════════════════════════════════════════════ 10 · la galería 615
def la_galeria_615():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.58, 90.0, H * 0.28, CLARO)
    _caja(ax, 5.0, H * 0.855, 90.0, 1.0, VERDE)
    ax.text(50, H * 0.775, "GALERÍA 615  ·  tramo por sostener", ha="center", va="center",
            family=F, fontsize=NOTA * 0.82, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.680, "4,00 × 4,00  ·  120 metros", ha="center", va="center",
            family=F, fontsize=CUERPO * 1.05, color=MARINO)
    ax.text(50, H * 0.610, "perno de 7 pies, espaciado a 1,20 m", ha="center",
            va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)

    _redonda(ax, 12.0, H * 0.26, 76.0, H * 0.22, BLANCO)
    _caja(ax, 12.0, H * 0.475, 76.0, 1.0, MORADO)
    ax.text(50, H * 0.405, "EL PEDIDO ANTERIOR", ha="center", va="center", family=F,
            fontsize=NOTA * 0.78, fontweight="bold", color=MORADO)
    ax.text(50, H * 0.315, "cuadraba, y a los 60 m se acabó la malla", ha="center",
            va="center", family=F, fontsize=CUERPO * 0.90, color=MARINO)
    _cierre(ax, H, "La labor paró tres guardias por una línea mal contada", H * 0.07)
    _g(fig, "sost-s9_la-galeria-615.png")


# ═════════════════════════════════════════ 11 · el pedido que falló
def el_pedido_viejo():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(46.0, "LO QUE DECÍA EL PEDIDO VIEJO"), (44.0, "LO QUE PASÓ")]
    filas = [["Pernos · exactos", "alcanzaron"],
             ["Malla · el área del contorno", "faltó a los sesenta metros"],
             ["Cartuchos · tres de cemento", "los llenó el practicante"],
             ["Firma · del que pidió", "nadie revisó las cuentas"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.82, H * 0.075, H * 0.098)
    _redonda(ax, 12.0, H * 0.17, 76.0, H * 0.115, CLARO)
    ax.text(50, H * 0.2275, "«la malla no se pone hoja pegada a hoja»", ha="center",
            va="center", family=F, fontsize=CUERPO * 0.90, color=MARINO)
    _cierre(ax, H, "Cada línea del pedido debe poder explicarse en voz alta", H * 0.05)
    _g(fig, "sost-s9_el-pedido-viejo.png")


# ══════════════════════════════════════ 12 · la ficha que se entrega
def ficha_encargo():
    ASP = 1.26
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    y = H * 0.90
    for rot in ("Perímetro que lleva sostenimiento  ·  ¿entra el piso?:",
                "Pernos de una fila:", "Número de filas del tramo:",
                "Total de pernos, con su longitud:",
                "Metros de malla · área del contorno:",
                "Metros de malla · traslape:", "Accesorios, con la cuenta por perno:"):
        ax.text(3.0, y, rot, ha="left", va="center", family=F,
                fontsize=NOTA * 0.82, color=MARINO)
        _caja(ax, 3.0, y - H * 0.042, 94.0, 0.4, GRIS)
        y -= H * 0.108
    y -= H * 0.02
    ax.text(3.0, y, "Dónde estaba el error del pedido viejo:", ha="left",
            va="center", family=F, fontsize=NOTA * 0.82, color=MARINO)
    _caja(ax, 3.0, y - H * 0.042, 94.0, 0.4, GRIS)
    ax.text(50, H * 0.045, "Firma del equipo técnico: ____________", ha="center",
            va="center", family=F, fontsize=NOTA * 0.75, color=GRIS)
    _g(fig, "sost-s9_ficha-encargo.png")


# ═════════════════════════════════════════════ 13 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean el encargo y saquen el perímetro", 3, AZUL, H * 0.72),
                                ("Armen el pedido, línea por línea", 14, MARINO, H * 0.53),
                                ("Escriban dónde falló el pedido viejo", 3, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 20 minutos · se entrega el pedido con sus cuentas",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s9_como-trabajamos.png")


# ══════════════════════════════════════════════ 14 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por el perímetro", "si el piso entró o no, y por qué"),
                   ("Seguimos por el total de pernos", "la fila, las filas y la multiplicación"),
                   ("Cerramos por la malla", "el área, el traslape y dónde falló el viejo")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s9_puesta-comun.png")


# ═══════════════════════════════════════════════ 15 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "«Pregúntenle al maestro cómo la amarra,\n"
                          "que él sí sabe por qué siempre le sobra un pedazo»",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.90,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 10.0, H * 0.14, 80.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Qué línea de tu pedido no sabrías explicar en voz alta?",
            ha="center", va="center", family=F, fontsize=NOTA * 0.95,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s9_una-ultima.png")


# ═══════════════════════════════════════════════ 16 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "¿Qué línea de un pedido es la que\nmás se olvida, y por qué?",
                 "La próxima: cómo se comprueba\nlo que ya quedó instalado"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s9_reflexion.png")


TODOS = [de_donde_venimos, componer_malla_real, componer_el_contorno,
         los_pernos_de_una_fila, las_filas_del_tramo, el_total_de_pernos,
         los_metros_de_malla, el_traslape, los_accesorios, la_galeria_615,
         el_pedido_viejo, ficha_encargo, como_trabajamos, puesta_comun,
         una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
