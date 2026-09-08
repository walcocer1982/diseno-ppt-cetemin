# -*- coding: utf-8 -*-
"""Esquemas de armazón de la sesión 1 de EOM · lo que no es contenido técnico.

Son los cuadros que sostienen los momentos de Conexión, Aplicación y cierre:
el curso en una lámina, cómo se califica, la ruta de la sesión, las tres fichas
del caso y el cuadro que la pareja llena. Siguen el molde de la S1 de SI
(`04_Recursos-graficos/SI/esquemas/`): misma paleta, misma métrica, y cada uno
con la proporción que le pide su lámina —no todas son cuadradas.

Métrica del §11: lienzo 1500 px de ancho, cuerpo 52 px, sin bbox_inches.
Van SIN título dentro: el título lo pone la lámina.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import FancyBboxPatch, Rectangle

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, cuerpo, guardar, lienzo, nota, rotulo,
)


def _redonda(ax, x, y, w, h, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.25,rounding_size=1.1",
                                facecolor=color, edgecolor="none"))


def _caja(ax, x, y, w, h, color):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor="none"))


def _celda(ax, x, y, w, h, txt, fondo, tinta=MARINO, negrita=False, tam=None):
    _caja(ax, x, y, w, h, fondo)
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", family=F,
            fontsize=tam or NOTA * 0.9, color=tinta, linespacing=1.3,
            fontweight="bold" if negrita else "normal")


# ═══════════════════════════════════════════════ 1 · el curso en una lámina
def curso_bloques():
    """Los dos bloques con sus sesiones, y el colaborativo que cierra cada uno."""
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    bloques = [
        (66, 50, AZUL, "BLOQUE 1",
         "El ciclo de minado y los métodos subterráneos",
         ["S1", "S2", "S3", "S4", "S5"], "TC1"),
        (38, 22, MORADO, "BLOQUE 2",
         "Geomecánica, equipos y explotación a tajo abierto",
         ["S7", "S8", "S9", "S10", "S11"], "TC2"),
    ]

    for y_tit, y, color, nombre, tema, sesiones, tc in bloques:
        ax.text(5, y_tit, nombre, ha="left", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=color)
        ax.text(24, y_tit, tema, ha="left", va="center", family=F,
                fontsize=NOTA, color=MARINO)
        x = 5
        for s in sesiones:
            _redonda(ax, x, y, 12.5, 12, color)
            ax.text(x + 6.25, y + 6, s, ha="center", va="center", family=F,
                    fontsize=CUERPO, fontweight="bold", color=BLANCO)
            x += 14.5
        _redonda(ax, x + 3, y, 15, 12, AMBAR)
        ax.text(x + 10.5, y + 6, tc, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=MARINO)

    ax.text(50, 10, "Cada bloque cierra con un trabajo colaborativo\n"
                    "que vale el 25 % de la nota.", ha="center", va="center",
            family=F, fontsize=CUERPO, color=MARINO, linespacing=1.35)
    nota(ax, 3, "Doce sesiones · 48 horas · 2 créditos.")
    return guardar(fig, "s1_curso-bloques.png")


# ═══════════════════════════════════════════════════ 2 · cómo se califica
def evaluacion():
    """El peso de cada evento, y la mitad que sale de los colaborativos."""
    ASP = 1.70
    fig, ax = lienzo(ASP)

    x0, ancho, y, alto = 6, 88, 24, 13
    tramos = [("TC1", 25, AMBAR, MARINO), ("TC2", 25, AMBAR, MARINO),
              ("EP", 20, AZUL, BLANCO), ("EF", 20, AZUL, BLANCO),
              ("CV", 10, GRIS, BLANCO)]

    x = x0
    for nombre, peso, color, tinta in tramos:
        w = ancho * peso / 100
        _caja(ax, x, y, w - 0.5, alto, color)
        ax.text(x + w / 2, y + alto / 2, nombre, ha="center", va="center",
                family=F, fontsize=CUERPO, fontweight="bold", color=tinta)
        ax.text(x + w / 2, y + alto + 4, "%d %%" % peso, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=MARINO)
        x += w

    # la llave sobre los dos colaborativos
    xf = x0 + ancho * 0.50
    ax.plot([x0, xf], [y + alto + 9.5, y + alto + 9.5], color=MARINO, lw=2.0)
    for xx in (x0, xf):
        ax.plot([xx, xx], [y + alto + 7.6, y + alto + 9.5], color=MARINO, lw=2.0)
    ax.text((x0 + xf) / 2, y + alto + 13, "la mitad de la nota", ha="center",
            va="center", family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)

    ax.text(50, 15, "TC · trabajo colaborativo    EP · examen parcial\n"
                    "EF · examen final    CV · cuestionarios de verificación",
            ha="center", va="center", family=F, fontsize=NOTA, color=GRIS,
            linespacing=1.4)
    ax.text(50, 6, "Nota mínima aprobatoria: 13", ha="center", va="center",
            family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    # va a comun/ y no a metexp/s1/: la barra de la nota es la misma en los
    # cinco cursos del módulo —25 · 25 · 20 · 20 · 5 · 5— y la usa también la
    # S1 de Sostenimiento. Si se regenerara dentro de la sesión, el catálogo
    # seguiría apuntando a la copia de comun/ y esta quedaría vieja sin avisar.
    return guardar(fig, "comun/evaluacion.png")


# ══════════════════════════════════════════════════ 3 · ruta de la sesión
def ruta_s1():
    """Los cinco momentos con sus minutos, de largo proporcional al tiempo."""
    ASP = 1.12
    fig, ax = lienzo(ASP)

    momentos = [("CONEXIÓN", 20, MORADO), ("ADQUISICIÓN", 45, AZUL),
                ("APLICACIÓN", 40, VERDE), ("DISCUSIÓN", 20, MORADO),
                ("REFLEXIÓN", 10, GRIS)]

    y, alto, hueco = 74, 11, 14
    for nombre, mins, color in momentos:
        _redonda(ax, 4, y, 30, alto, color)
        ax.text(19, y + alto / 2, nombre, ha="center", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=BLANCO)
        w = 44 * mins / 45.0
        _caja(ax, 37, y + 2.2, w, alto - 4.4, CLARO)
        ax.text(37 + w + 2.5, y + alto / 2, "%d min" % mins, ha="left",
                va="center", family=F, fontsize=CUERPO, fontweight="bold",
                color=MARINO)
        y -= hueco

    ax.text(50, 12, "Así vamos a trabajar hoy,\ny cuánto dura cada tramo.",
            ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
            linespacing=1.35)
    nota(ax, 4, "135 minutos en total.")
    return guardar(fig, "s1_ruta.png")


# ═══════════════════════════════════════════════ 4 · las tres fichas del caso
def tres_fichas():
    """Las tres labores comparadas: es la misma veta y el mismo macizo."""
    fig, ax = lienzo()

    _caja(ax, 3, 83, 94, 9, MARINO)
    ax.text(50, 87.5, "VETA MARY  ·  potencia 1,20 m  ·  buzamiento 70°  ·  "
                      "RMR de cajas 40 en las tres", ha="center", va="center",
            family=F, fontsize=NOTA * 0.85, fontweight="bold", color=BLANCO)

    cols = [(3, 21), (24, 18), (42, 32), (74, 23)]
    cab = ["LABOR", "ANCHO\nDE MINADO", "GEOMETRÍA Y\nSOSTENIMIENTO", "EQUIPO"]
    filas = [("Tajeo\nantiguo", "3,00 m", "recta\ncuadros de madera",
              "jackleg y\ncarretilla"),
             ("Tajeo\nnuevo A", "6,00 m", "bóveda en arco\nshotcrete SFR + Hydrabolt",
              "jumbo y\nscooptram"),
             ("Tajeo\nnuevo B", "12,00 m", "bóveda en arco\nshotcrete SFR + Hydrabolt",
              "jumbo y\nscooptram")]

    y = 70
    for (x, w), t in zip(cols, cab):
        _celda(ax, x, y, w - 1, 10, t, CLARO, MARINO, True, NOTA * 0.8)
    y -= 16.5
    for fila in filas:
        for (x, w), v in zip(cols, fila):
            _celda(ax, x, y, w - 1, 15, v, CLARO, MARINO, False, NOTA * 0.8)
        y -= 16.5

    ax.text(50, 12, "«En la labor de madera tuvimos dos desprendimientos\n"
                    "el año pasado. En las otras dos, ninguno.»",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.9,
            color=MARINO, linespacing=1.35)
    nota(ax, 5, "el capataz, al pasar")
    return guardar(fig, "s1_tres-fichas.png")


# ══════════════════════════════════════════ 5 · el cuadro que llena la pareja
def cuadro_encargo():
    """El impreso que se entrega: lo que hay que devolver lleno."""
    fig, ax = lienzo()

    ax.text(4, 88, "1 ·  Cuánto mide la veta y cuánto el ancho de minado",
            ha="left", va="center", family=F, fontsize=CUERPO * 0.9,
            fontweight="bold", color=MARINO)

    cols = [(4, 30), (34, 31), (65, 31)]
    cab = ["LABOR", "POTENCIA DE LA VETA", "ANCHO DE MINADO"]
    y = 72
    for (x, w), t in zip(cols, cab):
        _celda(ax, x, y, w - 1, 9, t, MARINO, BLANCO, True, NOTA * 0.8)
    y -= 11
    for labor in ("Tajeo antiguo", "Tajeo nuevo A", "Tajeo nuevo B"):
        _celda(ax, cols[0][0], y, cols[0][1] - 1, 9.5, labor, CLARO,
               MARINO, False, NOTA * 0.85)
        for x, w in cols[1:]:
            _caja(ax, x, y, w - 1, 9.5, BLANCO)
            ax.plot([x + 3, x + w - 4], [y + 2.6, y + 2.6], color=GRIS, lw=1.3)
        y -= 11

    ax.text(4, 27, "2 ·  ¿Cuánto admite ese terreno sin sostener?",
            ha="left", va="center", family=F, fontsize=CUERPO * 0.9,
            fontweight="bold", color=MARINO)
    ax.plot([4, 96], [21, 21], color=GRIS, lw=1.3)
    ax.text(4, 16, "     ¿Qué hace que dos de ellas puedan pasar de ahí?",
            ha="left", va="center", family=F, fontsize=CUERPO * 0.9,
            fontweight="bold", color=MARINO)
    for yy in (10.5, 5.5):
        ax.plot([4, 96], [yy, yy], color=GRIS, lw=1.3)
    return guardar(fig, "s1_cuadro-encargo.png")


# ══════════════════════════════════════════════ 6 · cómo trabaja la pareja
def como_trabajamos():
    """Los tres pasos del encargo, en el orden en que se hacen."""
    ASP = 1.70
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = [("1", "LEER", "las tres fichas", AZUL),
             ("2", "BUSCAR", "en la tabla\ngeomecánica", MORADO),
             ("3", "LLENAR", "el cuadro", VERDE)]

    x, w, y, alto = 4, 26, 18, 24
    for n, verbo, que, color in pasos:
        _redonda(ax, x, y, w, alto, color)
        ax.text(x + w / 2, y + alto - 5, n, ha="center", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, y + alto - 11.5, verbo, ha="center", va="center",
                family=F, fontsize=CUERPO, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, y + 5.5, que, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, color=BLANCO, linespacing=1.25)
        if n != "3":
            ax.annotate("", xy=(x + w + 5.5, y + alto / 2),
                        xytext=(x + w + 1.5, y + alto / 2),
                        arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.6,
                                        mutation_scale=20))
        x += w + 7

    _redonda(ax, 22, 46, 56, 10, AMBAR)
    ax.text(50, 51, "En parejas  ·  20 minutos", ha="center", va="center",
            family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    ax.text(50, 11, "Al terminar, entregan el cuadro.", ha="center", va="center",
            family=F, fontsize=CUERPO, color=MARINO)
    nota(ax, 4, "Tienen las tres fichas y la tabla geomecánica sobre la mesa.")
    return guardar(fig, "s1_como-trabajamos.png")


# ═══════════════════════════════════════════ 7 · el orden de la puesta en común
def puesta_en_comun():
    """Por dónde se abre la discusión, y con qué formato responde el equipo."""
    ASP = 1.12
    fig, ax = lienzo(ASP)

    pasos = [("¿Cuánto admite ese terreno\nsin sostener?",
              "que una pareja lo señale en la tabla", AZUL),
             ("¿Cuáles de las tres labores\npasan de ese número?",
              "las dos nuevas", MORADO),
             ("¿Qué se lo permite?", "la respuesta de hoy", VERDE)]

    y, alto = 68, 15
    for n, (preg, apunte, color) in enumerate(pasos, start=1):
        _redonda(ax, 4, y, 8, alto, color)
        ax.text(8, y + alto / 2, str(n), ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=BLANCO)
        _redonda(ax, 14, y, 82, alto, CLARO)
        ax.text(56, y + alto / 2 + 2.4, preg, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, fontweight="bold", color=MARINO,
                linespacing=1.25)
        ax.text(56, y + 3.2, apunte, ha="center", va="center", family=F,
                fontsize=NOTA * 0.8, color=GRIS)
        if n != 3:
            ax.annotate("", xy=(8, y - 4.5), xytext=(8, y - 0.5),
                        arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4,
                                        mutation_scale=18))
        y -= alto + 5

    _redonda(ax, 14, 12, 72, 11, MARINO)
    ax.text(50, 17.5, "AFIRMACIÓN  ·  APOYO  ·  PREGUNTA", ha="center",
            va="center", family=F, fontsize=CUERPO, fontweight="bold",
            color=BLANCO)
    nota(ax, 5, "Así responde cada pareja cuando le toca.")
    return guardar(fig, "s1_puesta-en-comun.png")


# ═══════════════════════════════════════════ 8 · la pregunta que abre el TC1
def puente_tc1():
    """Lo que cuesta y lo que rinde: la pregunta se sustenta en el colaborativo."""
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    ax.text(50, H - 10, "La labor de doce metros rompe mucho más\n"
                        "desmonte que veta. ¿Por qué la mina la prefiere igual?",
            ha="center", va="center", family=F, fontsize=CUERPO,
            fontweight="bold", color=MARINO, linespacing=1.35)

    for x, titulo, detalle, color in (
            (5, "LO QUE CUESTA", "más desmonte que\nromper y transportar", MORADO),
            (52, "LO QUE RINDE", "más tonelaje por tarea\ny ningún desprendimiento",
             VERDE)):
        _redonda(ax, x, 26, 43, 26, color)
        ax.text(x + 21.5, 45, titulo, ha="center", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=BLANCO)
        ax.text(x + 21.5, 34, detalle, ha="center", va="center", family=F,
                fontsize=NOTA * 0.9, color=BLANCO, linespacing=1.3)

    _redonda(ax, 5, 8, 90, 11, AMBAR)
    ax.text(50, 13.5, "Sustentarlo con datos  →  Trabajo Colaborativo 1",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.9,
            fontweight="bold", color=MARINO)
    return guardar(fig, "s1_puente-tc1.png")


if __name__ == "__main__":
    from PIL import Image
    for fn in (curso_bloques, evaluacion, ruta_s1, tres_fichas, cuadro_encargo,
               como_trabajamos, puesta_en_comun, puente_tc1):
        f = fn()
        w, h = Image.open(f).size
        pt = 6 * 52 / w * 72
        print("  %-28s %4d x %4d px  asp %.2f  cuerpo -> %.1f pt %s"
              % (f.name, w, h, w / h, pt, "OK" if pt >= 14.5 else "!! BAJO"))
