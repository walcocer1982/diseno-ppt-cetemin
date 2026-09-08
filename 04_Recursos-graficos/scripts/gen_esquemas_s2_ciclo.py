# -*- coding: utf-8 -*-
"""Esquemas de la sesión 2 · El ciclo de minado.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    La regla 3 del CLAUDE.md: lo FÍSICO se extrae de fuente, se dibuja solo lo
    que no tiene cuerpo. Esta sesión enseña una SECUENCIA —cinco operaciones y
    el orden en que se ejecutan—, y una secuencia no se fotografía: se dibuja.
    Por eso todo lo de este archivo es legítimo dibujarlo.

    Lo físico de la sesión —el jumbo perforando, el scoop cargando, la labor
    sostenida— entra por fotografía citada de la tesis de Raura, no por aquí.

Métrica del §11: lienzo 1500 px, cuerpo 52 px, sin bbox_inches, sin título
dentro (el título lo pone la lámina).

Uso:  python gen_esquemas_s2_ciclo.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Wedge

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, PROPORCION, VERDE, cuerpo, guardar, lienzo, nota, rotulo,
)

SALIDA = "metexp/s2/"
# CARPETAS. Los esquemas de EOM se ordenan por CURSO y luego por sesion:
# metexp/s1..s11, sost/s1..., y comun/ para lo que sirve a mas de uno.
# Antes colgaban de la raiz por sesion, cuando EOM tenia un solo curso
# disenado; con el segundo, «s1» era ambiguo. Ver OBS-EOM-SOST-18.
          # las imágenes de la S2 viven en su carpeta (Erick)
ROJO = "#C0392B"

# Las cinco, con su color. El orden es el del ciclo.
CINCO = [("PERFORACIÓN", AZUL), ("VOLADURA", ROJO), ("CARGUÍO", VERDE),
         ("ACARREO", MORADO), ("SOSTENIMIENTO", GRIS)]


def _caja(ax, x, y, w, h, color, borde="none", lw=0, r=1.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.2,rounding_size=%.1f" % r,
                                facecolor=color, edgecolor=borde, linewidth=lw))


def _flecha(ax, x1, y1, x2, y2, color=MARINO, lw=2.4):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=20))


def _txt(ax, x, y, t, size=None, color=MARINO, bold=False, ha="center"):
    ax.text(x, y, t, ha=ha, va="center", family=F, fontsize=size or CUERPO,
            color=color, linespacing=1.3, fontweight="bold" if bold else "normal")


# ═══════════════════════════════ 10 · qué hace una operación unitaria
def que_es_operacion():
    """La definición, como flujo: entra material, sale material distinto o en
    otro sitio. Es el criterio que después separa lo que es del ciclo de lo que
    no (OBS-15), así que se dibuja como prueba, no como definición."""
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    y = H * 0.60
    _caja(ax, 4, y - 9, 24, 18, CLARO)
    _txt(ax, 16, y + 3, "MATERIAL", bold=True)
    _txt(ax, 16, y - 4, "como estaba", CUERPO - 3, GRIS)
    _caja(ax, 38, y - 11, 24, 22, AZUL)
    _txt(ax, 50, y + 4, "OPERACIÓN", NOTA, BLANCO, bold=True)
    _txt(ax, 50, y - 4, "equipo + insumo", CUERPO - 3, BLANCO)
    _caja(ax, 72, y - 9, 24, 18, AMBAR)
    _txt(ax, 84, y + 3, "MATERIAL", bold=True)
    _txt(ax, 84, y - 4, "transformado\no desplazado", NOTA, MARINO)
    _flecha(ax, 29, y, 37, y)
    _flecha(ax, 63, y, 71, y)
    _txt(ax, 50, y - 22, "Y se puede medir sola:\nmetros perforados, toneladas movidas.")
    nota(ax, 6, "Si al material no le pasa nada, no es una operación unitaria.")
    return guardar(fig, SALIDA + "s2_que-es-operacion.png")


# ═══════════════════════════════════════════ 11 · las cinco, en fila
def cinco_operaciones():
    """Las cinco con lo que le hacen al material. Una fila por operación: en
    columna caben las frases sin encogerlas."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    hace = ["abre los taladros",
            "rompe la roca",
            "levanta lo roto",
            "lo lleva al echadero",
            "sujeta el techo"]
    y, alto = H - 14, 13
    for (nom, col), h in zip(CINCO, hace):
        _caja(ax, 5, y, 33, alto - 2, col)
        _txt(ax, 21.5, y + (alto - 2) / 2, nom, CUERPO - 2, BLANCO, bold=True)
        _txt(ax, 41, y + (alto - 2) / 2, h, CUERPO - 2, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 7, "Cinco operaciones, cinco productos distintos.")
    nota(ax, 4, "Ninguna se puede saltar: el ciclo no cierra.")
    return guardar(fig, SALIDA + "s2_cinco-operaciones.png")


# ═══════════════════════════════════ 12 · equipo, insumo y cómo se mide
def equipo_y_medida():
    fig, ax = lienzo()
    H = 100 / PROPORCION
    filas = [("Perforación", "jumbo o jackleg", "metros perforados"),
             ("Voladura", "emulsión y fanel", "toneladas rotas"),
             ("Carguío", "scooptram", "baldes o toneladas"),
             ("Acarreo", "camión de bajo perfil", "toneladas por viaje"),
             ("Sostenimiento", "pernos, malla, shotcrete", "metros sostenidos")]
    anchos = [28, 34, 32]
    y, alto = H - 10, 12
    x = 4
    for w, t in zip(anchos, ["OPERACIÓN", "CON QUÉ", "CÓMO SE MIDE"]):
        ax.add_patch(Rectangle((x, y), w, alto, facecolor=MARINO, edgecolor=BLANCO, lw=2))
        _txt(ax, x + w / 2, y + alto / 2, t, NOTA, BLANCO, bold=True)
        x += w
    for i, fila in enumerate(filas):
        y -= alto
        x = 4
        base = CLARO if i % 2 == 0 else BLANCO
        for j, (w, t) in enumerate(zip(anchos, fila)):
            ax.add_patch(Rectangle((x, y), w, alto, facecolor=base, edgecolor=BLANCO, lw=2))
            _txt(ax, x + w / 2, y + alto / 2, t, NOTA, MARINO, bold=(j == 0))
            x += w
    _txt(ax, 50, y - 10, "Cada operación tiene su equipo, su insumo\ny su forma de medirse.")
    nota(ax, 6, "El equipo cambia con el método; la operación, no.")
    return guardar(fig, SALIDA + "s2_equipo-y-medida.png")


# ══════════════════════════════════════════════ 13 · el ciclo, en orden
def ciclo_orden():
    """Las cinco en anillo. El círculo es el mensaje: la quinta devuelve a la
    primera, y por eso una guardia entra donde la anterior lo dejó."""
    fig, ax = lienzo(1.05)
    H = 100 / 1.05
    cx, cy, R = 50, H * 0.52, 24
    for i, (nom, col) in enumerate(CINCO):
        a = math.radians(90 - i * 72)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        ax.add_patch(Circle((x, y), 11.5, facecolor=col, edgecolor=BLANCO, lw=2.5))
        _txt(ax, x, y + 1.5, str(i + 1), FUERTE, BLANCO, bold=True)
        # El rotulo va CENTRADO SOBRE SU PROPIO CIRCULO, no empujado hacia
        # afuera: alejarlo radialmente sacaba «SOSTENIMIENTO» del lienzo por la
        # izquierda. Arriba o abajo segun donde caiga el circulo.
        dy = 17 if math.sin(a) >= 0 else -17
        _txt(ax, x, y + dy, nom, CUERPO - 4, col, bold=True)
    for i in range(5):
        a1 = math.radians(90 - i * 72 - 16)
        a2 = math.radians(90 - (i + 1) * 72 + 16)
        ax.add_patch(Wedge((cx, cy), R + 0.9, math.degrees(a2), math.degrees(a1),
                           width=1.8, facecolor=GRIS))
        _flecha(ax, cx + R * math.cos(a2 + 0.06), cy + R * math.sin(a2 + 0.06),
                cx + R * math.cos(a2), cy + R * math.sin(a2), GRIS, 2.0)
    _txt(ax, cx, cy + 3, "EL CICLO", CUERPO, MARINO, bold=True)
    _txt(ax, cx, cy - 4, "una vuelta =\nun avance", NOTA, GRIS)
    nota(ax, 5, "La quinta devuelve a la primera: por eso es un ciclo y no una lista.")
    return guardar(fig, SALIDA + "s2_ciclo-orden.png")


# ═══════════════════════════════ 14 · cada paso deja listo al siguiente
def cadena_necesidad():
    fig, ax = lienzo(1.30)
    H = 100 / 1.30
    pares = [("Sin taladros", "no hay dónde poner el explosivo"),
             ("Sin disparo", "no hay material roto que cargar"),
             ("Sin carguío", "el frente queda tapado"),
             ("Sin acarreo", "la cámara se llena"),
             ("Sin desatar", "no se puede sostener")]
    y, alto = H - 15, 12.5
    for izq, der in pares:
        _caja(ax, 4, y, 32, alto - 2.5, MARINO)
        _txt(ax, 20, y + (alto - 2.5) / 2, izq, CUERPO - 3, BLANCO, bold=True)
        _flecha(ax, 37, y + (alto - 2.5) / 2, 42, y + (alto - 2.5) / 2)
        _txt(ax, 44, y + (alto - 2.5) / 2, der, CUERPO - 3, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 8, "El orden no es una costumbre:\ncada paso necesita al anterior.")
    nota(ax, 6, "Saltarse uno no adelanta el ciclo: lo detiene.")
    return guardar(fig, SALIDA + "s2_cadena-necesidad.png")


# ══════════════════════════ 16 · lo que acompaña al ciclo entero
def permanentes():
    """El anillo de fuera es lo que NO es operación unitaria. Es la corrección
    de OBS-15 dibujada: se ve que rodean al ciclo, no que estén dentro."""
    fig, ax = lienzo(1.05)
    H = 100 / 1.05
    cx, cy = 50, H * 0.48
    ax.add_patch(Circle((cx, cy), 35, facecolor=CLARO, edgecolor=GRIS,
                        lw=2.2, linestyle=(0, (6, 4))))
    ax.add_patch(Circle((cx, cy), 22, facecolor=AZUL, edgecolor=BLANCO, lw=3))
    _txt(ax, cx, cy + 5, "EL CICLO", CUERPO, BLANCO, bold=True)
    _txt(ax, cx, cy - 4, "las cinco\noperaciones", NOTA, BLANCO)
    for i, (t, sub) in enumerate([("VENTILAR", "saca los gases"),
                                  ("DESATAR", "baja lo suelto"),
                                  ("REGAR", "asienta el polvo")]):
        a = math.radians(90 + i * 120)
        x, y = cx + 35 * math.cos(a), cy + 35 * math.sin(a)
        ax.add_patch(Circle((x, y), 10.5, facecolor=AMBAR, edgecolor=BLANCO, lw=2.5))
        _txt(ax, x, y + 2, t, NOTA, MARINO, bold=True)
        _txt(ax, x, y - 4.5, sub, CUERPO - 5, MARINO)
    nota(ax, 5, "Ninguna transforma ni desplaza el material: previenen un daño.")
    return guardar(fig, SALIDA + "s2_permanentes.png")


# ═══════════════════════════ 19 · cómo se ubica lo que uno ve
def del_bloc_al_reporte():
    """El criterio de OBS-15, convertido en una pregunta que el alumno puede
    aplicar solo. Es lo que el caso le va a pedir hacer nueve veces."""
    fig, ax = lienzo(1.20)
    H = 100 / 1.20
    _caja(ax, 28, H - 18, 44, 13, MARINO)
    _txt(ax, 50, H - 11.5, "¿QUÉ LE PASÓ AL MATERIAL?", NOTA, BLANCO, bold=True)
    _flecha(ax, 40, H - 19, 26, H - 30)
    _flecha(ax, 60, H - 19, 74, H - 30)
    _caja(ax, 5, H - 48, 40, 18, AZUL)
    _txt(ax, 25, H - 34, "SE TRANSFORMÓ", NOTA, BLANCO, bold=True)
    _txt(ax, 25, H - 41, "o se movió de sitio", CUERPO - 3, BLANCO)
    _caja(ax, 55, H - 48, 40, 18, AMBAR)
    _txt(ax, 75, H - 34, "NO LE PASÓ NADA", NOTA, MARINO, bold=True)
    _txt(ax, 75, H - 41, "se previno un daño", CUERPO - 3, MARINO)
    _txt(ax, 25, H - 56, "es OPERACIÓN:\nva al reporte del ciclo", NOTA, AZUL, bold=True)
    _txt(ax, 75, H - 56, "es CONTROL:\nva aparte", NOTA, MARINO, bold=True)
    nota(ax, 5, "La misma pregunta, una por una, para las nueve anotaciones.")
    return guardar(fig, SALIDA + "s2_del-bloc-al-reporte.png")


# ══════════════════════════════════════════ armazón de la sesión
def ruta():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    tramos = [("CONEXIÓN", 20, AZUL), ("ADQUISICIÓN", 45, VERDE),
              ("APLICACIÓN", 40, MORADO), ("DISCUSIÓN", 20, AMBAR),
              ("REFLEXIÓN", 10, GRIS)]
    x0, ancho, y, alto = 5, 90, H * 0.42, 13
    x = x0
    for nom, mins, col in tramos:
        w = ancho * mins / 135
        _caja(ax, x, y, w - 0.6, alto, col, r=0.6)
        _txt(ax, x + w / 2, y + alto / 2 + 0.5, "%d'" % mins, NOTA,
             MARINO if col is AMBAR else BLANCO, bold=True)
        # los tramos cortos llevan el rotulo mas arriba: si no, se pisan entre si
        dy = 6 if mins >= 20 else 13
        _txt(ax, x + w / 2, y + alto + dy, nom, NOTA - 2, MARINO, bold=True)
        x += w
    _txt(ax, 50, y - 12, "135 minutos. El caso se trabaja en la Aplicación.")
    return guardar(fig, SALIDA + "s2_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 1", NOTA, GRIS, bold=True)
    _txt(ax, 23, y - 4, "qué mide la veta\ny cuánto se abre", NOTA, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 2", NOTA, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "qué se hace dentro,\ny en qué orden", NOTA, BLANCO)
    _flecha(ax, 43, y, 57, y)
    _txt(ax, 50, y - 20, "La labor ya está abierta.\nHoy toca lo que pasa dentro de ella.")
    return guardar(fig, SALIDA + "s2_de-donde-venimos.png")


def bloc_ayudante():
    """Las nueve anotaciones del caso, tal como el ayudante las escribió."""
    fig, ax = lienzo(0.80)
    H = 100 / 0.80
    anot = ["Pusieron pernos y malla en el techo",
            "El jumbo hizo 38 taladros de 12 pies",
            "Bajaron rocas sueltas con barretilla",
            "El camión llevó el material al echadero",
            "Prendieron la manga; había humo",
            "El scoop sacó lo roto — nueve baldes",
            "Cargaron los taladros con emulsión y fanel",
            "Antes del jumbo, bajaron rocas otra vez",
            "Regaron el material roto antes de moverlo"]
    y, alto = H - 12, 10.5
    for i, t in enumerate(anot, 1):
        ax.add_patch(Rectangle((6, y - alto + 1.5), 88, alto - 2,
                               facecolor=CLARO if i % 2 else BLANCO,
                               edgecolor=GRIS, lw=1.0))
        ax.add_patch(Circle((12, y - alto / 2 + 1.5), 3.0, facecolor=MARINO))
        _txt(ax, 12, y - alto / 2 + 1.8, str(i), NOTA - 1, BLANCO, bold=True)
        _txt(ax, 18, y - alto / 2 + 1.5, t, CUERPO - 4, MARINO, ha="left")
        y -= alto
    nota(ax, 5, "En el orden en que las vio, que no es el orden en que se hacen.")
    return guardar(fig, SALIDA + "s2_bloc-ayudante.png")


def cuadro_encargo():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    anchos = [14, 40, 40]
    y, alto = H - 8, 11
    x = 4
    for w, t in zip(anchos, ["N°", "QUÉ LE PASA AL MATERIAL", "SI NADA: ¿CUÁNDO SE HACE?"]):
        ax.add_patch(Rectangle((x, y), w, alto, facecolor=MARINO, edgecolor=BLANCO, lw=2))
        _txt(ax, x + w / 2, y + alto / 2, t, NOTA - 1, BLANCO, bold=True)
        x += w
    for i in range(4):
        y -= alto
        x = 4
        for w in anchos:
            ax.add_patch(Rectangle((x, y), w, alto, facecolor=BLANCO, edgecolor=GRIS, lw=1.2))
            x += w
    _txt(ax, 50, y - 11, "Una fila por anotación.\nSi al material no le pasa nada, la casilla va en blanco.")
    nota(ax, 5, "En parejas · 20 minutos · se entrega solo este cuadro.")
    return guardar(fig, SALIDA + "s2_cuadro-encargo.png")


def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Ordenen", "numeren las nueve\nen el orden real"),
             ("2", "Pregunten", "¿qué le pasó\nal material?"),
             ("3", "Aparten", "lo que no le hace\nnada al material")]
    x0, w = 5, 30
    for i, (n, t, sub) in enumerate(pasos):
        x = x0 + i * 32
        _caja(ax, x, H * 0.34, w, 26, AZUL if i < 2 else AMBAR)
        _txt(ax, x + w / 2, H * 0.34 + 20, n, FUERTE, BLANCO if i < 2 else MARINO, bold=True)
        _txt(ax, x + w / 2, H * 0.34 + 13, t, NOTA, BLANCO if i < 2 else MARINO, bold=True)
        _txt(ax, x + w / 2, H * 0.34 + 5, sub, NOTA - 1, BLANCO if i < 2 else MARINO)
    _txt(ax, 50, H * 0.34 - 12, "Parejas · 20 minutos · un cuadro por pareja")
    return guardar(fig, SALIDA + "s2_como-trabajamos.png")


def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["Las que SÍ tocan el material",
             "¿Cuántas quedaron? ¿Coinciden?",
             "Las apartadas: ¿por qué no entran?",
             "Anotó dos veces la barretilla:\n¿cuál borramos?"]
    y, alto = H - 16, 14
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.2, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), NOTA, BLANCO if i < 4 else MARINO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 4, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 6, "Al responder: «yo digo… porque…».")
    nota(ax, 5, "La cuarta la cierra el instructor con el Art. 224 b) en pantalla.")
    return guardar(fig, SALIDA + "s2_puesta-en-comun.png")


def puente():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, AZUL)
    _txt(ax, 23, y + 4, "HOY", NOTA, BLANCO, bold=True)
    _txt(ax, 23, y - 4, "qué se hace\ny en qué orden", NOTA, BLANCO)
    _caja(ax, 59, y - 11, 36, 22, AMBAR)
    _txt(ax, 77, y + 4, "SESIÓN 3", NOTA, MARINO, bold=True)
    _txt(ax, 77, y - 4, "con qué equipo\ny qué controla el técnico", NOTA, MARINO)
    _flecha(ax, 43, y, 57, y)
    _txt(ax, 50, y - 20, "El TC1 pedirá las dos cosas juntas:\nla operación y el equipo que le toca.")
    return guardar(fig, SALIDA + "s2_puente.png")


if __name__ == "__main__":
    for f in (que_es_operacion, cinco_operaciones, equipo_y_medida, ciclo_orden,
              cadena_necesidad, permanentes, del_bloc_al_reporte, ruta,
              de_donde_venimos, bloc_ayudante, cuadro_encargo, como_trabajamos,
              puesta_en_comun, puente):
        print(" ", f())
