# -*- coding: utf-8 -*-
"""Esquemas de la sesión 11 de EOM · Recaracterización y corrección.

La última de adquisición. Cierra el ciclo: la S3 y la S4 caracterizaron, la S7
a la S9 pidieron, la S10 recibió, y aquí el terreno se movió DESPUÉS y hay que
volver a empezar sin empezar de cero.

La bisagra es que la malla puede estar entera y bien tensada y no decir nada:
lo que avisa son el perno que gira, el techo que se realzó contra la línea de
topografía, el agua que pasó de mancha a flujo y la roca que chispea.

QUÉ SE DIBUJA Y QUÉ NO
    Se dibujan las tablas de señales, la comparación de casillas, el pedido
    corregido y el armazón. Lo físico entra por figura de fuente: la cinta de
    convergencia entre cabezas de perno, que es el instrumento con el que se
    comprueba que el terreno se movió después de sostenido.

Uso:  python gen_esquemas_sost_s11.py
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

CARPETA = "sost/s11/"
PLANOS = Path(__file__).resolve().parents[1] / "EOM" / "planos"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    _dos_columnas("sost-s11_de-donde-venimos.png",
                  ("LA S10 RECIBIÓ", "y dijo si lo instalado\nquedó como se pidió", AZUL),
                  ("HOY EL TERRENO SE MOVIÓ", "meses después, con el\nsostenimiento ya puesto", VERDE),
                  "La roca no firma actas: sigue trabajando", asp=2.10, guardar_en=_g)


# ══════════════════════════ 2 · la cinta de convergencia (fuente)
def componer_cinta_convergencia():
    """Maqueta y rotula la cinta de convergencia entre cabezas de perno.

    El dibujo sale tal cual de la guía. Sus rótulos dan de 9 a 12 pt
    proyectados, bajo el piso de 14 del §11, así que se rotula con el kit.
    """
    im = Image.open(PLANOS / "osinergmin2017_fig12-2_cinta-convergencia_referencia.png").convert("RGB")
    ancho_px, alto_px = im.size

    ASP = 1.42
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    alto = H * 0.58
    ancho = alto * ancho_px / alto_px
    x0, y0 = 6.0, H * 0.32
    ax.imshow(np.asarray(im), extent=(x0, x0 + ancho, y0, y0 + alto),
              aspect="auto", zorder=1)

    xl = x0 + ancho + 3.0
    for texto, frac, color in (("Las cabezas de los pernos\nson los puntos fijos", 0.82, AZUL),
                               ("La cinta mide la distancia\nentre ellos", 0.52, VERDE),
                               ("Si esa distancia cambia,\nel terreno se movió", 0.20, MORADO)):
        y = y0 + alto * frac
        ax.plot([x0 + ancho - 3.0, xl - 1.5], [y, y], color=color, linewidth=1.4, zorder=3)
        ax.text(xl, y, texto, ha="left", va="center", family=F,
                fontsize=NOTA * 0.80, color=MARINO, linespacing=1.35)

    _cierre(ax, H, "Se mide en una labor que YA está sostenida", H * 0.10)
    ax.text(50, H * 0.035, "Osinergmin (2017), Guía de criterios geomecánicos · Figura 12-2",
            ha="center", va="center", family=F, fontsize=NOTA * 0.62, color=GRIS)
    _g(fig, "sost-s11_la-cinta-de-convergencia.png")


# ═════════════════════════════════════════ 3 · las señales del terreno
def las_senales():
    ASP = 1.44
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(42.0, "LO QUE SE OBSERVA"), (48.0, "QUÉ AVISA")]
    filas = [["Un perno gira con la mano", "perdió su anclaje"],
             ["Pernos partidos cerca de la cabeza", "están tomando carga"],
             ["El techo se realzó", "se mide contra la línea de topografía"],
             ["La roca chispea con la picota", "el macizo se está relajando"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.80, H * 0.075, H * 0.105)
    ax.text(50, H * 0.185, "el terreno sigue trabajando después de instalado el sostenimiento",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "Las señales se leen juntas, no de una en una", H * 0.055)
    _g(fig, "sost-s11_las-senales.png")


# ═══════════════════════════════ 4 · lo que la malla no prueba
def lo_que_no_prueba_la_malla():
    ASP = 1.72
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 6.0, H * 0.64, 88.0, H * 0.24, CLARO)
    ax.text(50, H * 0.795, "La malla está entera y bien tensada", ha="center", va="center",
            family=F, fontsize=CUERPO * 1.05, fontweight="bold", color=MARINO)
    ax.text(50, H * 0.705, "sin un solo paño roto", ha="center", va="center",
            family=F, fontsize=NOTA * 0.9, color=GRIS)

    _redonda(ax, 12.0, H * 0.30, 76.0, H * 0.26, BLANCO)
    _caja(ax, 12.0, H * 0.555, 76.0, 1.0, MORADO)
    ax.text(50, H * 0.475, "Y AUN ASÍ", ha="center", va="center", family=F,
            fontsize=NOTA * 0.8, fontweight="bold", color=MORADO)
    ax.text(50, H * 0.375, "la malla retiene lo que se suelta;\nno sujeta el macizo",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92,
            color=MARINO, linespacing=1.4)
    _cierre(ax, H, "El agua que antes era mancha y ahora corre también es señal", H * 0.075)
    _g(fig, "sost-s11_lo-que-no-prueba-la-malla.png")


# ══════════════════════════════════════════ 5 · recaracterizar
def recaracterizar():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Se vuelven a levantar los tres datos", "fracturas, picota y agua, otra vez"),
                   ("La casilla nueva se escribe al costado", "no encima de la vieja"),
                   ("Comparar las dos dice cuánto se movió", "esa diferencia es el hallazgo"),
                   ("Sin recaracterizar, el pedido repite el error", "y vuelve a fallar igual")],
           H * 0.76, H * 0.155)
    _cierre(ax, H, "Recaracterizar es volver a mapear la misma celda, hoy", H * 0.055)
    _g(fig, "sost-s11_recaracterizar.png")


# ═════════════════════════════════════ 6 · la casilla nueva y su fila
def la_fila_nueva():
    ASP = 1.50
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(30.0, "EL DATO"), (30.0, "EN EL MAPEO"), (30.0, "HOY")]
    filas = [["Fracturas por m²", "nueve", "hay que contarlas"],
             ["Golpes de picota", "cedía al tercero", "chispea"],
             ["Agua", "seca", "corre sobre la caja"],
             ["Casilla y calidad", "la del mapeo", "la que salga hoy"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.82, H * 0.072, H * 0.098)
    ax.text(50, H * 0.175, "bajar de calidad casi siempre suma un elemento",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "El agua en flujo cambia el elemento aunque la roca aguante", H * 0.05)
    _g(fig, "sost-s11_la-fila-nueva.png")


# ═══════════════════════════════════ 7 · corregir no es pedir de cero
def corregir_no_es_pedir():
    _dos_columnas("sost-s11_corregir-no-es-pedir.png",
                  ("PEDIR DE CERO", "vuelve a comprar lo que\nya está en la labor", MORADO),
                  ("CORREGIR", "mantiene lo que sirve\ny anula lo que no", VERDE),
                  "Almacén necesita saber qué anular, no solo qué mandar", asp=1.85,
                  guardar_en=_g)


# ══════════════════════════════════ 8 · las tres columnas del pedido
def tres_columnas():
    ASP = 1.48
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for i, (titulo, txt, color) in enumerate(
            (("SE MANTIENE", "del pedido inicial,\nlo que sigue sirviendo", AZUL),
             ("SE ANULA", "lo que ya no corresponde,\ncon su motivo escrito", MORADO),
             ("SE PIDE DE MÁS", "lo que falta, contra\nla fila nueva", VERDE))):
        x = 3.0 + i * 32.0
        _redonda(ax, x, H * 0.42, 30.0, H * 0.34, CLARO)
        _caja(ax, x, H * 0.745, 30.0, 1.0, color)
        ax.text(x + 15.0, H * 0.665, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.82, fontweight="bold", color=color)
        ax.text(x + 15.0, H * 0.535, txt, ha="center", va="center", family=F,
                fontsize=NOTA * 0.76, color=MARINO, linespacing=1.4)
    ax.text(50, H * 0.30, "las tres se escriben separadas, no en un solo total",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.88, color=MARINO)
    ax.text(50, H * 0.225, "y el pedido corregido lleva fecha y firma de quien lo hizo",
            ha="center", va="center", family=F, fontsize=NOTA * 0.82, color=GRIS)
    _cierre(ax, H, "Corregir no es pedir otra vez desde cero", H * 0.06)
    _g(fig, "sost-s11_tres-columnas.png")


# ═══════════════════════════════════════ 9 · reforzar o retirar
def reforzar_o_retirar():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(2.0, "REFORZAR ENCIMA", AZUL,
             ["No para el tránsito", "La cartilla lo admite en relajamiento",
              "Manda perno más malla al tope", "Suma sobre un anclaje que ya cedió"]),
            (51.0, "RETIRAR Y CAMBIAR", MORADO,
             ["Quita lo que ya no trabaja", "Permite otro sistema desde cero",
              "Expone gente bajo roca suelta", "Para la labor mientras se hace"])]
    for x0, titulo, color, items in cols:
        w = 47.0
        _cabecera(ax, x0, H * 0.80, w, H * 0.11, titulo, color, NOTA * 0.78)
        y = H * 0.80
        for it in items:
            y -= H * 0.140
            _celda(ax, x0, y, w, H * 0.125, it, CLARO, MARINO, tam=NOTA * 0.76)
    _cierre(ax, H, "Las dos se defienden; hay que decir con cuál fila de la cartilla", H * 0.06)
    _g(fig, "sost-s11_reforzar-o-retirar.png")


# ══════════════════════════════════════ 10 · cómo entra la gente
def como_entra_la_gente():
    ASP = 1.90
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "Antes de entrar se decide cómo se protege\na quien entra",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "Lo que no se decide en oficina se improvisa en el frente",
            ha="center", va="center", family=F, fontsize=NOTA * 0.95,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s11_como-entra-la-gente.png")


# ═════════════════════════════════════ 11 · la galería del nivel 9
def la_galeria_nivel_9():
    # medido: con ASP 1,52 la cuarta viñeta caia dentro de la franja ambar
    ASP = 1.34
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.64, 90.0, H * 0.24, CLARO)
    _caja(ax, 5.0, H * 0.875, 90.0, 1.0, VERDE)
    ax.text(50, H * 0.805, "GALERÍA DE TRANSPORTE  ·  NIVEL 9", ha="center", va="center",
            family=F, fontsize=NOTA * 0.82, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.735, "sostenida hace cinco meses", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.98, color=MARINO)
    ax.text(50, H * 0.680, "pasa la locomotora cuatro veces por guardia",
            ha="center", va="center", family=F, fontsize=NOTA * 0.82, color=GRIS)

    _cabecera(ax, 5.0, H * 0.52, 90.0, H * 0.075, "LO QUE ENCUENTRAN AL ENTRAR", MARINO,
              NOTA * 0.75)
    y = H * 0.52
    for txt in (u"La malla entera y bien tensada, sin un paño roto",
                u"Dos pernos que giran al empujarlos con la mano",
                u"Diez metros de techo realzado casi un metro",
                u"Agua corriendo donde antes había una mancha"):
        y -= H * 0.085
        ax.text(6.0, y + H * 0.0425, u"·  " + txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.82, color=MARINO)
    _cierre(ax, H, "«El motorista reportó que le caían piedras sobre la vía»", H * 0.04)
    _g(fig, "sost-s11_la-galeria-nivel-9.png")


# ══════════════════════════════════════════ 12 · la ficha vieja
def la_ficha_vieja():
    ASP = 1.90
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 8.0, H * 0.68, 84.0, H * 0.13, "DEL MAPEO DE HACE CINCO MESES", MARINO,
              NOTA * 0.8)
    for i, (rot, val) in enumerate((("Fracturas por m²", "nueve"),
                                    ("Picota", "cedía al tercer golpe"),
                                    ("Agua", "seca"))):
        x = 8.0 + i * 28.0
        _redonda(ax, x, H * 0.30, 26.0, H * 0.28, CLARO)
        ax.text(x + 13.0, H * 0.495, rot, ha="center", va="center", family=F,
                fontsize=NOTA * 0.72, color=GRIS)
        ax.text(x + 13.0, H * 0.395, val, ha="center", va="center", family=F,
                fontsize=NOTA * 0.86, fontweight="bold", color=MARINO, linespacing=1.3)
    _cierre(ax, H, "Esa ficha es contra la que se compara la de hoy", H * 0.09)
    _g(fig, "sost-s11_la-ficha-vieja.png")


# ═════════════════════════════════════ 13 · la ficha que se entrega
def ficha_encargo():
    ASP = 1.26
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    y = H * 0.90
    for rot in ("Casilla GSI y calidad de HOY  ·  al costado de las del mapeo:",
                "Sostenimiento que ahora manda:",
                "Qué se pide de más:",
                "Qué del pedido inicial ya no sirve:",
                "Qué se hace con los pernos y la malla que están puestos:",
                "Cómo entra la gente a hacerlo:"):
        ax.text(3.0, y, rot, ha="left", va="center", family=F,
                fontsize=NOTA * 0.82, color=MARINO)
        _caja(ax, 3.0, y - H * 0.042, 94.0, 0.4, GRIS)
        y -= H * 0.125
    ax.text(50, H * 0.06, "Firma del equipo técnico: ____________", ha="center",
            va="center", family=F, fontsize=NOTA * 0.75, color=GRIS)
    _g(fig, "sost-s11_ficha-encargo.png")


# ═════════════════════════════════════════════ 14 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean lo que vieron y la ficha vieja", 2, AZUL, H * 0.72),
                                ("Saquen la casilla de hoy y su fila", 10, MARINO, H * 0.53),
                                ("Escriban las tres líneas y cómo se entra", 8, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.90, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 20 minutos · se entrega el requerimiento corregido",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s11_como-trabajamos.png")


# ══════════════════════════════════════════════ 15 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por la casilla de hoy", "qué cambió respecto de la del mapeo"),
                   ("Seguimos por las tres líneas", "qué se mantiene, qué se anula, qué se pide"),
                   ("Cerramos por cómo entra la gente", "reforzar o retirar, y con qué protección")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s11_puesta-comun.png")


# ═══════════════════════════════════════════════ 16 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "La malla está entera y bien tensada,\nsin un solo paño roto",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Por qué eso no dice nada?", ha="center", va="center",
            family=F, fontsize=CUERPO * 0.95, fontweight="bold", color=MARINO)
    _g(fig, "sost-s11_una-ultima.png")


# ═══════════════════════════════════════════════ 17 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "¿Qué señal habrías pasado por alto\nsi solo miras la malla?",
                 "La próxima: sustentación del\nTrabajo Colaborativo 2"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s11_reflexion.png")


TODOS = [de_donde_venimos, componer_cinta_convergencia, las_senales,
         lo_que_no_prueba_la_malla, recaracterizar, la_fila_nueva,
         corregir_no_es_pedir, tres_columnas, reforzar_o_retirar,
         como_entra_la_gente, la_galeria_nivel_9, la_ficha_vieja,
         ficha_encargo, como_trabajamos, puesta_comun, una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
