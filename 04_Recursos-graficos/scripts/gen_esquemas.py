# -*- coding: utf-8 -*-
"""Genera los esquemas de proceso del curso: ciclos, secuencias, flujos.

POR QUE NO PASA POR EL MODELO
    Un esquema de proceso no es un equipo: no tiene geometria que verificar
    contra un catalogo. Es texto y flechas. Dibujarlo aqui es gratis, sale
    identico cada vez y se corrige cambiando una linea — mientras que pedirselo
    al modelo abriria la puerta a que invente pasos que no existen.

    La regla del §10 (nunca texto→imagen) aplica a EQUIPOS. Los esquemas se
    dibujan; las siluetas se generan y se miden.

Uso:  python gen_esquemas.py
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "04_Recursos-graficos/EOM/esquemas/comun"
# CARPETAS. Los esquemas de EOM se ordenan por CURSO y luego por sesion:
# metexp/s1..s11, sost/s1..., y comun/ para lo que sirve a mas de uno.
# Antes colgaban de la raiz por sesion, cuando EOM tenia un solo curso
# disenado; con el segundo, «s1» era ambiguo. Ver OBS-EOM-SOST-18.


AZUL, AMBAR, BLANCO, GRIS = "#0D2632", "#FFC505", "#FFFFFF", "#8A9AA3"
FUENTE = "Arial"        # Oswald es la de marca pero no está instalada como TTF del sistema

# LAS CINCO OPERACIONES UNITARIAS
#
# El criterio para entrar aqui no es "pasa en la labor", es la definicion de
# operacion unitaria: una etapa que TRANSFORMA O DESPLAZA EL MATERIAL, con
# equipo, insumo y producto propios, y medible por si sola (rendimiento, costo
# unitario, tiempo de ciclo).
#
#   perforacion   la horada        voladura   la fragmenta
#   carguio       la levanta       acarreo    la transporta
#   sostenimiento acondiciona la labor para seguir
#
# DESATADO y VENTILACION NO entran, aunque las tesis las enumeren junto a las
# demas: no le hacen nada al material, previenen un riesgo. La propia fuente
# (Ccaso Yucasi, UNAP, §2.6) delata el desatado al definirlo — "es LA ACTIVIDAD
# que consiste en hacer caer las rocas sueltas ANTES, DURANTE Y DESPUES de las
# labores" —: lo que acompana a todas las etapas no es una de ellas.
# Van como CONDICIONES PERMANENTES, rodeando el ciclo.
CICLO = [
    ("PERFORACIÓN",  "se abren los taladros\nen el frente"),
    ("VOLADURA",     "se carga y se dispara\nsegún la secuencia"),
    ("CARGUÍO",      "se levanta el material\nroto del frente"),
    ("ACARREO",      "se transporta\nfuera de la labor"),
    ("SOSTENIMIENTO","se asegura la labor\nantes de seguir"),
]
PERMANENTES = "DESATADO DE ROCAS  ·  VENTILACIÓN  ·  DRENAJE"

def ciclo_de_minado(destaca: tuple[str, ...] = (), nombre: str = "ciclo-de-minado") -> Path:
    """El ciclo en circulo. `destaca` resalta las operaciones de la sesion."""
    fig, ax = plt.subplots(figsize=(10, 7.2), dpi=200)
    ax.set_xlim(-1.40, 1.40); ax.set_ylim(-1.34, 1.22); ax.axis("off")
    fig.patch.set_alpha(0)

    n = len(CICLO)
    r = 0.82
    pos = []
    for i in range(n):
        a = math.pi / 2 - i * 2 * math.pi / n          # arranca arriba, gira horario
        pos.append((r * math.cos(a), r * math.sin(a)))

    # las flechas van primero: quedan por debajo de las cajas
    for i in range(n):
        (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % n]
        ax.add_patch(FancyArrowPatch(
            (x1 * 0.72, y1 * 0.72), (x2 * 0.72, y2 * 0.72),
            connectionstyle="arc3,rad=-0.32", arrowstyle="-|>,head_width=5,head_length=9",
            color=AMBAR, lw=2.4, shrinkA=14, shrinkB=14))

    for i, ((titulo, detalle), (x, y)) in enumerate(zip(CICLO, pos)):
        activa = titulo in destaca or not destaca
        fondo = AZUL if activa else BLANCO
        borde = AMBAR if titulo in destaca else (AZUL if activa else GRIS)
        letra = BLANCO if activa else GRIS
        ax.add_patch(FancyBboxPatch(
            (x - 0.40, y - 0.155), 0.80, 0.31, boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor=fondo, edgecolor=borde, linewidth=2.6 if titulo in destaca else 1.4))
        ax.text(x, y + 0.055, titulo, ha="center", va="center", family=FUENTE,
                fontsize=12.5, fontweight="bold", color=letra)
        ax.text(x, y - 0.072, detalle, ha="center", va="center", family=FUENTE,
                fontsize=8.2, color=letra, alpha=0.88, linespacing=1.35)

    ax.text(0, 0.05, "EL CICLO\nDE MINADO", ha="center", va="center", family=FUENTE,
            fontsize=14, fontweight="bold", color=AZUL, linespacing=1.3)

    # Lo que acompaña a TODAS las etapas no es una de ellas: va rodeando.
    ax.text(0, -1.10, PERMANENTES, ha="center", va="center", family=FUENTE,
            fontsize=9.5, fontweight="bold", color=AZUL)
    ax.text(0, -1.235, "condiciones permanentes de seguridad · antes, durante y después de cada operación",
            ha="center", va="center", family=FUENTE, fontsize=7.8, color=GRIS)

    SALIDA.mkdir(parents=True, exist_ok=True)
    f = SALIDA / f"{nombre}.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


def secuencia_de_encendido() -> Path:
    """Por que el disparo sale por fases y no todo a la vez.

    TRES FASES, no cinco tiempos. Los cinco nombres de taladro son correctos,
    pero cuadradores, alzas y arrastres salen JUNTOS: son el perimetro.
    FUENTE: Manual practico de voladura (EXSA), cap. 6 «En los tuneles» —
    «primero salen los taladros de arranque casi simultaneamente creando la
    cavidad cilindrica; en segunda fase los taladros de ayuda del nucleo rompen
    por colapso hacia el eje…; finalmente salen los taladros del perimetro
    (alzas, cuadradores y arrastres del piso), perfilando el tunel».
    """
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=200)
    ax.set_xlim(-0.30, 10.40); ax.set_ylim(0.10, 3.45); ax.axis("off")
    fig.patch.set_alpha(0)

    fases = [("ARRANQUE",  "abre la cavidad\nen el centro del frente",
              "sin cara libre\nnada más puede romper"),
             ("AYUDAS",    "rompen por colapso\nhacia el eje del arranque",
              "amplían el hueco\nhacia flancos y fondo"),
             ("PERIFERIA", "cuadradores · alzas · arrastres",
              "perfilan la labor:\nancho, techo y piso")]
    ancho = 3.05
    for i, (nombre, que, para) in enumerate(fases):
        x = i * 3.45
        ax.add_patch(FancyBboxPatch((x, 1.30), ancho, 1.85,
                     boxstyle="round,pad=0.03,rounding_size=0.1",
                     facecolor=AZUL, edgecolor=AMBAR, linewidth=1.8))
        ax.text(x + ancho / 2, 2.86, f"{i + 1}.ª FASE", ha="center", va="center",
                family=FUENTE, fontsize=9.5, fontweight="bold", color=AMBAR)
        ax.text(x + ancho / 2, 2.44, nombre, ha="center", va="center",
                family=FUENTE, fontsize=13, fontweight="bold", color=BLANCO)
        ax.text(x + ancho / 2, 2.00, que, ha="center", va="center",
                family=FUENTE, fontsize=8.4, color=BLANCO, alpha=0.9, linespacing=1.4)
        ax.text(x + ancho / 2, 1.56, para, ha="center", va="center",
                family=FUENTE, fontsize=8, color=AMBAR, alpha=0.9, linespacing=1.4)
        if i < len(fases) - 1:
            ax.add_patch(FancyArrowPatch((x + ancho + 0.06, 2.22), (x + 3.39, 2.22),
                         arrowstyle="-|>,head_width=5,head_length=9", color=AMBAR, lw=2.4))


    ax.text(5.05, 0.62, "Cada fase sale cuando la anterior ya le abrió cara libre.\n"
                        "Sin esa secuencia el disparo no rompe: comprime.",
            ha="center", va="center", family=FUENTE, fontsize=10, color=AZUL, linespacing=1.5)

    SALIDA.mkdir(parents=True, exist_ok=True)
    f = SALIDA / "secuencia-de-encendido.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


def malla_del_frente() -> Path:
    """Donde va cada taladro en el frente y por que.

    FUENTE: nucleo = arranque (cuele) y ayudas · perifericos = cuadradores
    (flancos), alzas (techo/corona) y arrastres (piso). Manual practico de
    voladura (EXSA) cap. 6 y revistaseguridadminera.com.
    """
    fig, ax = plt.subplots(figsize=(9, 7.4), dpi=200)
    ax.set_xlim(-0.6, 6.6); ax.set_ylim(-1.15, 5.35); ax.axis("off")
    ax.set_aspect("equal")          # si no, los taladros salen elipticos
    fig.patch.set_alpha(0)

    # seccion de la labor: paredes rectas y boveda
    import numpy as np
    xs = np.linspace(0, 6, 200)
    ax.plot([0, 0], [0, 3.2], color=AZUL, lw=2.2)
    ax.plot([6, 6], [0, 3.2], color=AZUL, lw=2.2)
    ax.plot([0, 6], [0, 0], color=AZUL, lw=2.2)
    ax.plot(xs, 3.2 + 1.5 * np.sqrt(np.clip(1 - ((xs - 3) / 3) ** 2, 0, 1)), color=AZUL, lw=2.2)

    def taladros(pts, color, r=0.115, relleno=True):
        for x, y in pts:
            ax.add_patch(plt.Circle((x, y), r, facecolor=color if relleno else "none",
                                    edgecolor=color, lw=1.8, zorder=3))

    arranque = [(2.72, 2.10), (3.28, 2.10), (2.72, 2.62), (3.28, 2.62)]
    ayudas   = [(2.05, 1.72), (3.95, 1.72), (2.05, 3.05), (3.95, 3.05),
                (3.00, 1.45), (3.00, 3.40)]
    cuadrad  = [(0.42, 0.75), (0.42, 1.75), (0.42, 2.75),
                (5.58, 0.75), (5.58, 1.75), (5.58, 2.75)]
    alzas    = [(1.15, 3.75), (2.10, 4.28), (3.00, 4.42), (3.90, 4.28), (4.85, 3.75)]
    arrastres= [(0.95, 0.35), (2.00, 0.35), (3.00, 0.35), (4.00, 0.35), (5.05, 0.35)]

    taladros(arranque, AMBAR)
    taladros(ayudas, AZUL)
    for g in (cuadrad, alzas, arrastres):
        taladros(g, GRIS, relleno=False)


    leyenda = [(AMBAR, True,  "ARRANQUE", "al centro · abre la cara libre"),
               (AZUL,  True,  "AYUDAS",   "alrededor · amplían el hueco"),
               (GRIS,  False, "CONTORNO", "cuadradores, alzas y arrastres · perfilan")]
    for i, (c, rel, t, d) in enumerate(leyenda):
        y = -0.32 - i * 0.30
        ax.add_patch(plt.Circle((0.35, y), 0.10, facecolor=c if rel else "none",
                                edgecolor=c, lw=1.8))
        ax.text(0.62, y, t, va="center", family=FUENTE, fontsize=9.5,
                fontweight="bold", color=AZUL)
        ax.text(1.85, y, d, va="center", family=FUENTE, fontsize=8.5, color=GRIS)

    SALIDA.mkdir(parents=True, exist_ok=True)
    f = SALIDA / "malla-del-frente.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


def carga_del_taladro() -> Path:
    """Que va dentro de un taladro y en que orden, desde el fondo.

    FUENTE: Manual practico de voladura (EXSA). La carga de fondo es la de
    mayor densidad y potencia «para romper la parte mas confinada»; encima va
    la carga de columna; y en la boca el taco, «un tapon de material inerte
    para sellar la carga explosiva» — se emplea arcilla porque los detritos se
    deslizarian sobre la carga. La columna ocupa de 1/2 a 2/3 del taladro.
    """
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=200)
    ax.set_xlim(-0.4, 11.0); ax.set_ylim(-1.35, 1.95); ax.axis("off")
    fig.patch.set_alpha(0)

    y0, alto = 0.0, 1.05
    S = chr(10)
    tramos = [(0.0, 1.9, AMBAR, "CARGA DE FONDO", "el cebo: inicia el disparo" + S + "y rompe lo más confinado"),
              (1.9, 5.6, AZUL,  "COLUMNA EXPLOSIVA", "de ½ a ⅔ del taladro" + S + "es la carga que rompe"),
              (7.5, 2.4, GRIS,  "TACO", "arcilla en la boca:" + S + "confina el disparo")]
    for x, w, c, t, d in tramos:
        ax.add_patch(FancyBboxPatch((x, y0), w, alto, boxstyle="square,pad=0",
                     facecolor=c, edgecolor="none"))
        ax.text(x + w / 2, y0 + alto / 2, t, ha="center", va="center", family=FUENTE,
                fontsize=9.5, fontweight="bold", color=BLANCO if c != GRIS else AZUL)
        ax.text(x + w / 2, y0 - 0.60, d, ha="center", va="center", family=FUENTE,
                fontsize=8.2, color=AZUL, linespacing=1.4)
    ax.plot([0, 9.9], [y0 + alto, y0 + alto], color=AZUL, lw=2.4)
    ax.plot([0, 9.9], [y0, y0], color=AZUL, lw=2.4)
    ax.plot([0, 0], [y0, y0 + alto], color=AZUL, lw=2.4)
    ax.text(-0.18, y0 + alto / 2, "fondo", ha="right", va="center", family=FUENTE,
            fontsize=8.5, color=GRIS)
    ax.text(10.10, y0 + alto / 2, "boca", ha="left", va="center", family=FUENTE,
            fontsize=8.5, color=GRIS)

    ax.text(4.95, 1.62, "Se carga desde el fondo hacia la boca.", ha="center", va="center",
            family=FUENTE, fontsize=9.5, color=AZUL)

    SALIDA.mkdir(parents=True, exist_ok=True)
    f = SALIDA / "carga-del-taladro.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


if __name__ == "__main__":
    for f in (ciclo_de_minado(("PERFORACIÓN", "VOLADURA"), "ciclo-de-minado_s1"),
              ciclo_de_minado((), "ciclo-de-minado_completo"),
              secuencia_de_encendido(), malla_del_frente(), carga_del_taladro()):
        print(f"  {f.relative_to(RAIZ)}  ({f.stat().st_size // 1024} KB)")
