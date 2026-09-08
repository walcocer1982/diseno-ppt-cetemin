# -*- coding: utf-8 -*-
"""Esquemas de la sesión 7 · Clasificación geomecánica, sostenimiento y abertura máxima.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO. Ni la veta entre sus cajas, ni un frente sostenido, ni
    un realce: todo eso existe, está fotografiado, y entra al PPT por imágenes
    de fuente ya aprobadas —la foto del frente con la malla, la veta y sus
    cajas, los elementos de sostenimiento—. Aquí se dibujan RELACIONES,
    TABLAS y ARMAZÓN: qué declara la tabla de la labor, cómo se compara un
    número con otro, qué formato llena el estudiante, la ruta y la puesta en
    común.

    En particular, el REALCE no se dibuja. Es una labor y tiene forma real; lo
    que se dibuja es la DECISIÓN —si el ancho supera lo habilitado, no se abre
    de una vez—, que es lo que la sesión enseña.

NO SE FILTRA LA RESPUESTA
    Las láminas de Adquisición se proyectan ANTES de que las parejas escriban
    la instrucción de minado. Por eso ninguna resuelve los tres tramos del
    caso: los ejemplos de la regla usan OTROS números (RMR 45, potencia 2,00 m)
    y los del caso solo aparecen en Aplicación, sin la columna del ancho.

LAS DOS ABERTURAS SON EL CORAZÓN DE LA SESIÓN
    La tabla del Art. 33 trae dos, y confundirlas es el error que la sesión
    persigue: lo que el terreno aguanta SOLO, y lo que HABILITA el
    sostenimiento aplicado. Cada esquema que las nombra las separa por color.

Uso:  python gen_esquemas_s7_geomecanica.py
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


# ═══════════════════════════════ 11 · cajas y mineral (PC1 · 5-8)
def cajas_y_mineral():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 20, H - 13, 60, 10, MARINO)
    _txt(ax, 50, H - 8, "LA TABLA DECLARA DOS NOTAS, NO UNA", CUERPO - 3, AMBAR, bold=True)
    y = H * 0.36
    for x, cab, sub, col, letra in (
            (5, "RMR DE LAS CAJAS", "la roca que sostiene" + S + "el hueco", AZUL, BLANCO),
            (53, "RMR DEL MINERAL", "la roca que se" + S + "va a romper", MORADO, BLANCO)):
        _caja(ax, x, y, 42, 26, col)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 4, letra, bold=True)
        _txt(ax, x + 21, y + 8, sub, CUERPO - 5, letra)
    _caja(ax, 5, y - 19, 90, 16, AMBAR)
    _txt(ax, 50, y - 7, "Pueden estar en calidades distintas, y casi siempre lo están",
         CUERPO - 4, MARINO, bold=True)
    _txt(ax, 50, y - 14.5, "La abertura se decide con la de las CAJAS: es la que aguanta el hueco",
         CUERPO - 6, MARINO)
    nota(ax, 5, "Se publica en cada labor, firmada y vigente · D.S. 024-2016-EM, Art. 33.")
    return guardar(fig, "s7_cajas-y-mineral.png")


# ═══════════════════════════════ 12 · potencia contra abertura (PC2 · 1-4)
def potencia_vs_abertura():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _txt(ax, 50, H - 7, "Ejemplo: cajas de RMR 45 · la tabla admite 3,50 m sin sostener",
         CUERPO - 4, GRIS)
    y = H * 0.40
    for x, cab, pot, veredicto, col, letra in (
            (5, "SI LA POTENCIA CABE", "potencia 2,00 m", "se rompe y ya", VERDE, BLANCO),
            (53, "SI LA SUPERA", "potencia 4,80 m", "no se abre hasta sostener", AMBAR, MARINO)):
        _caja(ax, x, y, 42, 28, col)
        _txt(ax, x + 21, y + 21, cab, CUERPO - 4, letra, bold=True)
        _txt(ax, x + 21, y + 13, pot, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 21, y + 5, veredicto, CUERPO - 5, letra)
        ax.annotate("", xy=(x + 21, y + 29.5), xytext=(x + 21, y + 35),
                    arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=14))
    _caja(ax, 5, y - 15, 90, 11, CLARO)
    _txt(ax, 50, y - 9.5, "La comparación se hace con números, no a ojo", CUERPO - 4,
         MARINO, bold=True)
    nota(ax, 6, "Y contra la columna que toca: el terreno solo, o con su sostenimiento.")
    return guardar(fig, "s7_potencia-vs-abertura.png")


# ═══════════════════════════════ 15 · la dilución que no es error (PC3 · 5-8)
def dilucion_forzada():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _tabla(ax, 5, H - 14, [30, 30, 30], 12,
           ["LO QUE MIDE LA VETA", "LO QUE SE ROMPE", "LO QUE ENTRA DE MÁS"],
           [["0,60 m", "2,40 m", "1,80 m de caja"],
            ["1,80 m", "2,40 m", "0,60 m de caja"],
            ["3,20 m", "3,20 m", "nada"]],
           tam=CUERPO - 5)
    _caja(ax, 5, 21, 90, 12, AMBAR)
    _txt(ax, 50, 27, "El desmonte que entra con el mineral es DILUCIÓN", CUERPO - 4,
         MARINO, bold=True)
    _txt(ax, 50, 13, "Aquí no es un error del maestro: la impone el equipo." + S +
         "Romper solo la potencia deja la labor sin sección para operar.", CUERPO - 5, MARINO)
    nota(ax, 4, "Ancho mínimo 2,40 m: por debajo no entran el jumbo ni el scooptram.")
    return guardar(fig, "s7_dilucion-forzada.png")


# ═══════════════════════════════ 16 · el orden de la instrucción (PC4 · 1-4)
def instruccion():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = [("1", "RMR", "de las cajas" + S + "del tramo"),
             ("2", "ABERTURA", "la que ese terreno" + S + "admite"),
             ("3", "POTENCIA", "lo que mide" + S + "la veta ahí"),
             ("4", "SOSTENIMIENTO", "el que va" + S + "antes de romper")]
    y = H * 0.40
    for i, (n, t, sub) in enumerate(pasos):
        x = 4 + i * 24
        _caja(ax, x, y, 22, 26, AZUL if i < 3 else AMBAR)
        letra = BLANCO if i < 3 else MARINO
        _txt(ax, x + 11, y + 20, n, FUERTE, letra, bold=True)
        _txt(ax, x + 11, y + 13, t, CUERPO - 5, letra, bold=True)
        _txt(ax, x + 11, y + 5.5, sub, CUERPO - 7, letra)
        if i < 3:
            ax.annotate("", xy=(x + 23.5, y + 13), xytext=(x + 22.3, y + 13),
                        arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=13))
    _caja(ax, 5, y - 16, 90, 12, CLARO)
    _txt(ax, 50, y - 10, "Un tramo, un renglón. No hay una instrucción para toda la veta.",
         CUERPO - 4, MARINO, bold=True)
    nota(ax, 6, "Va a la pizarra de la labor y lleva firma: alguien la ejecuta.")
    return guardar(fig, "s7_instruccion.png")


# ═══════════════════════════════ 17 · cuando el ancho no cabe (PC4 · 5-8)
def no_cabe():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 14, H - 13, 72, 11, MARINO)
    _txt(ax, 50, H - 7.5, "EL ANCHO QUE SE VA A ROMPER, ¿CABE?", CUERPO - 3, AMBAR, bold=True)
    y = H * 0.38
    ramas = ((4, "CABE SIN SOSTENER", "se rompe", VERDE, BLANCO),
             (35, "CABE CON SOSTENIMIENTO", "primero se sostiene," + S + "después se rompe", AZUL, BLANCO),
             (66, "NO CABE NI ASÍ", "no se abre de una vez:" + S + "se saca por realces", AMBAR, MARINO))
    for x, cab, txt, col, letra in ramas:
        _caja(ax, x, y, 30, 27, col)
        _txt(ax, x + 15, y + 19, cab, CUERPO - 6, letra, bold=True)
        _txt(ax, x + 15, y + 8, txt, CUERPO - 6, letra)
        ax.annotate("", xy=(x + 15, y + 28.5), xytext=(x + 15, y + 34),
                    arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=13))
    _txt(ax, 50, y - 11, "Se compara contra la abertura HABILITADA," + S +
         "no contra la que el terreno aguanta solo.", CUERPO - 4, MARINO)
    nota(ax, 5, "Abrir más de lo que la tabla admite es lo que precede a una caída de caja.")
    return guardar(fig, "s7_no-cabe.png")


# ═══════════════════════════════ 19 · el levantamiento por tramos
def levantamiento():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 5, H - 11, 90, 9, MARINO)
    _txt(ax, 50, H - 6.5, "TAJEO VETA MARY · LEVANTAMIENTO DE LA SEMANA", CUERPO - 4,
         BLANCO, bold=True)
    _tabla(ax, 5, H - 25, [24, 33, 33], 13,
           ["TRAMO", "POTENCIA", "RMR DE CAJAS"],
           [["PRIMERO", "1,10 m", "55"],
            ["SEGUNDO", "3,20 m", "26"],
            ["TERCERO", "0,60 m", "45"]],
           tam=CUERPO - 1)
    _txt(ax, 50, 21, "La potencia la midió geología; el RMR, geomecánica." + S +
         "La unidad es mecanizada: ancho mínimo de minado 2,40 m.", CUERPO - 4, MARINO)
    nota(ax, 6, "El maestro espera un ancho al pie de la chimenea.")
    return guardar(fig, "s7_levantamiento.png")


# ═══════════════════════════════ 20 · la tabla clavada en la entrada
def tabla_labor():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 5, H - 11, 90, 9, MARINO)
    _txt(ax, 50, H - 6.5, "TABLA GEOMECÁNICA DE LA LABOR · D.S. 024-2016-EM, Art. 33",
         CUERPO - 5, BLANCO, bold=True)
    _tabla(ax, 4.5, H - 25, [25, 19, 28, 19], 12,
           ["CALIDAD · RMR", "SIN SOSTENER", "SOSTENIMIENTO", "HABILITA"],
           [["Regular A · 51-60", "5,00 m", "pernos sistemáticos", "8,00 m"],
            ["Regular B · 41-50", "3,50 m", "pernos + malla", "10,00 m"],
            ["Mala A · 31-40", "3,00 m", "shotcrete + Hydrabolt", "12,00 m"],
            ["Mala B · 21-30", "2,00 m", "shotcrete + cimbras", "6,00 m"]],
           tam=CUERPO - 5)
    _caja(ax, 5, 17, 90, 11, AMBAR)
    _txt(ax, 50, 22.5, "Dos aberturas por fila, y no son la misma", CUERPO - 4, MARINO, bold=True)
    nota(ax, 9, "Clavada en la entrada del tajeo, firmada y con la vigencia del mes.")
    nota(ax, 4, "Fuente: U.M. Parcoy · tesis UNSAAC vía INGEMMET (TE0380).")
    return guardar(fig, "s7_tabla-labor.png")


# ═══════════════════════════════ 21 · el encargo
def encargo():
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 5, H - 11, 90, 9, MARINO)
    _txt(ax, 50, H - 6.5, "INSTRUCCIÓN DE MINADO · PIZARRA DE LABOR", CUERPO - 4,
         BLANCO, bold=True)
    _tabla(ax, 4.5, H - 25, [16, 21, 17, 20, 17], 12,
           ["TRAMO", "ABERTURA ADMITIDA", "POTENCIA", "ANCHO A ROMPER",
            "SOSTENIMIENTO"],
           [["PRIMERO", "", "", "", ""], ["SEGUNDO", "", "", "", ""],
            ["TERCERO", "", "", "", ""]],
           tam=CUERPO - 6)
    _caja(ax, 5, 19, 90, 11, AMBAR)
    _txt(ax, 50, 24.5, "Firma y fecha: el maestro la va a ejecutar", CUERPO - 4,
         MARINO, bold=True)
    nota(ax, 10, "En parejas · 20 minutos · una sola instrucción por pareja.")
    nota(ax, 5, "Un renglón por tramo, y se escribe poco: el maestro la lee de pie.")
    return guardar(fig, "s7_encargo.png")


# ═══════════════════════════════ 22 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "la tabla de la labor:" + S + "las dos aberturas", "4'"),
             ("2", "Escriban", "los tres renglones," + S + "uno por tramo", "12'"),
             ("3", "Firmen", "revisen y firmen" + S + "la instrucción", "4'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 20 minutos · una instrucción firmada")
    return guardar(fig, "s7_como-trabajamos.png")


# ═══════════════════════════════ 25 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Qué ancho pusieron en el tramo primero?",
             "En el segundo, ¿qué va antes de romper?",
             "En el tercero, ¿por qué el ancho no es la potencia?",
             "¿Alguna pareja escribió un solo ancho" + S + "para los tres tramos?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 5, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».", CUERPO - 5, MARINO)
    nota(ax, 5, "La segunda la cierra el instructor: sostener no asegura, habilita.")
    return guardar(fig, "s7_puesta-en-comun.png")


# ═══════════════════════════════ 26 · el tramo más angosto
def tramo_angosto():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 12, H - 14, 76, 12, AMBAR)
    _txt(ax, 50, H - 8, "El tramo más angosto es el que más desmonte produce",
         CUERPO - 3, MARINO, bold=True)
    y = H * 0.24
    for x, cab, txt in ((5, "LO QUE PARECE", "menos veta," + S + "menos trabajo"),
                        (53, "LO QUE PASA", "el ancho no baja del mínimo:" + S +
                         "todo lo que falta es caja")):
        _caja(ax, x, y, 42, 26, MARINO)
        _txt(ax, x + 21, y + 18, cab, CUERPO - 5, AMBAR, bold=True)
        _txt(ax, x + 21, y + 8, txt, CUERPO - 6, BLANCO)
    _txt(ax, 50, H - 26, "La misma veta, el mismo equipo, y tres tramos" + S +
         "que no se minan igual.", CUERPO - 4, MARINO)
    nota(ax, 5, "Lo abre el instructor en plenario. No se entrega ni se califica.")
    return guardar(fig, "s7_tramo-angosto.png")


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
    _txt(ax, 50, y - 12, "135 minutos. Abre el bloque 2:" + S +
         "cuánto se puede abrir un terreno, y con qué antes.")
    return guardar(fig, "s7_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "BLOQUE 1", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "el ciclo, los métodos" + S + "y las labores de cada uno",
         CUERPO - 4, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 7", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "cuánto se puede abrir" + S + "ese terreno, y con qué antes",
         CUERPO - 4, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "El método dice qué labores se abren." + S +
         "Hoy, hasta dónde las admite la roca.", CUERPO - 3)
    return guardar(fig, "s7_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, cajas_y_mineral, potencia_vs_abertura,
              dilucion_forzada, instruccion, no_cabe, levantamiento, tabla_labor,
              encargo, como_trabajamos, puesta_en_comun, tramo_angosto):
        print(" ", f())
