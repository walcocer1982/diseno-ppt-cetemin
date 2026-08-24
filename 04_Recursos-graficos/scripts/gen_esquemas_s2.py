# -*- coding: utf-8 -*-
"""Esquemas de la sesion 2: sostenimiento y sus elementos.

Dibujados, no generados: son esquemas de proceso y de concepto, sin geometria
de catalogo que verificar. El §10 (nunca texto->imagen) aplica a EQUIPOS.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

AZUL, AMBAR, BLANCO, GRIS = "#0D2632", "#FFC505", "#FFFFFF", "#8A9AA3"
F = "Arial"
SALIDA = Path("../EOM/esquemas")


def elementos_de_sostenimiento() -> Path:
    """Que se instala segun la calidad de la roca. El RMR decide."""
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.2, 4.5); ax.axis("off")
    fig.patch.set_alpha(0)

    cols = [("PERNO", "RMR > 60\nroca buena",
             "cose la roca suelta\nal macizo firme detrás"),
            ("PERNO + MALLA", "RMR 40 – 60\nroca regular",
             "la malla retiene\nlo que el perno no alcanza"),
            ("SHOTCRETE", "RMR 30 – 40\nroca mala",
             "sella la superficie\ny evita que se descomprima"),
            ("CUADROS", "RMR < 30\nroca muy mala",
             "sostienen donde la roca\nno admite perno")]
    ancho = 2.30
    for i, (nombre, rmr, que) in enumerate(cols):
        x = i * 2.52
        ax.add_patch(FancyBboxPatch((x, 1.30), ancho, 2.55,
                     boxstyle="round,pad=0.03,rounding_size=0.09",
                     facecolor=AZUL, edgecolor=AMBAR, linewidth=1.6))
        ax.text(x + ancho / 2, 3.52, nombre, ha="center", va="center", family=F,
                fontsize=11.5, fontweight="bold", color=BLANCO)
        ax.text(x + ancho / 2, 2.92, rmr, ha="center", va="center", family=F,
                fontsize=9.5, fontweight="bold", color=AMBAR, linespacing=1.4)
        ax.text(x + ancho / 2, 1.95, que, ha="center", va="center", family=F,
                fontsize=8.4, color=BLANCO, alpha=0.9, linespacing=1.5)

    ax.add_patch(FancyArrowPatch((0.15, 0.85), (9.9, 0.85),
                 arrowstyle="-|>,head_width=4,head_length=8", color=GRIS, lw=1.6))
    ax.text(0.15, 0.45, "roca buena", family=F, fontsize=8.5, color=GRIS)
    ax.text(9.9, 0.45, "roca mala", family=F, fontsize=8.5, color=GRIS, ha="right")
    ax.text(5.05, 0.06, "Lo que se instala lo decide la calidad del macizo, no la costumbre.",
            ha="center", family=F, fontsize=9.5, color=AZUL)

    SALIDA.mkdir(parents=True, exist_ok=True)
    f = SALIDA / "elementos-sostenimiento.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


def orden_de_operaciones() -> Path:
    """El orden despues del disparo. Alterarlo es un accidente."""
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(0.0, 3.3); ax.axis("off")
    fig.patch.set_alpha(0)

    pasos = [("VENTILAR", "evacuar los gases\ndel disparo"),
             ("DESATAR", "hacer caer\nla roca suelta"),
             ("LIMPIAR", "sacar el material\nroto del frente"),
             ("SOSTENER", "asegurar la labor\nantes de seguir")]
    ancho = 2.20
    for i, (nombre, que) in enumerate(pasos):
        x = i * 2.55
        ax.add_patch(FancyBboxPatch((x, 1.15), ancho, 1.45,
                     boxstyle="round,pad=0.03,rounding_size=0.09",
                     facecolor=AZUL, edgecolor=AMBAR, linewidth=1.6))
        ax.text(x + ancho / 2, 2.20, f"{i + 1}", ha="center", va="center", family=F,
                fontsize=10, fontweight="bold", color=AMBAR)
        ax.text(x + ancho / 2, 1.85, nombre, ha="center", va="center", family=F,
                fontsize=12, fontweight="bold", color=BLANCO)
        ax.text(x + ancho / 2, 1.42, que, ha="center", va="center", family=F,
                fontsize=8.2, color=BLANCO, alpha=0.9, linespacing=1.4)
        if i < len(pasos) - 1:
            ax.add_patch(FancyArrowPatch((x + ancho + 0.05, 1.87), (x + 2.50, 1.87),
                         arrowstyle="-|>,head_width=4.5,head_length=8", color=AMBAR, lw=2.2))
    ax.text(4.95, 0.55, "Entrar a limpiar sin desatar es la primera causa de accidentes\n"
                        "por caída de rocas en mina subterránea.",
            ha="center", va="center", family=F, fontsize=10, color=AZUL, linespacing=1.5)

    f = SALIDA / "orden-despues-del-disparo.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


if __name__ == "__main__":
    for f in (elementos_de_sostenimiento(), orden_de_operaciones()):
        print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")


def carguio_segun_seccion() -> Path:
    """Con que se limpia segun el ancho de la labor.

    No hay imagen citable de winche de arrastre en las fuentes disponibles. En
    vez de poner «algo relacionado» —que fue lo que se hizo primero, una ficha
    de datos donde faltaba imagen— se dibuja el CRITERIO, que es lo que la
    lamina enseña: la seccion decide el equipo.
    """
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.1, 4.2); ax.axis("off")
    fig.patch.set_alpha(0)

    casos = [("SCOOPTRAM", "sección ≥ 3,00 m", "carga y transporta\nen la misma máquina",
              "hasta 200 m de acarreo"),
             ("WINCHE DE ARRASTRE", "sección 1,50 – 3,00 m", "arrastra el material\ncon una rastra",
              "hasta 60 m, por riel o piso"),
             ("CARRETILLA", "sección < 1,50 m", "carga manual\ncon lampa",
              "distancias cortas, al echadero")]
    ancho = 3.05
    for i, (nombre, cuando, que, alcance) in enumerate(casos):
        x = i * 3.45
        ax.add_patch(FancyBboxPatch((x, 1.05), ancho, 2.35,
                     boxstyle="round,pad=0.03,rounding_size=0.09",
                     facecolor=AZUL, edgecolor=AMBAR, linewidth=1.6))
        ax.text(x + ancho / 2, 3.08, nombre, ha="center", va="center", family=F,
                fontsize=11.5, fontweight="bold", color=BLANCO)
        ax.text(x + ancho / 2, 2.66, cuando, ha="center", va="center", family=F,
                fontsize=9.5, fontweight="bold", color=AMBAR)
        ax.text(x + ancho / 2, 2.05, que, ha="center", va="center", family=F,
                fontsize=8.6, color=BLANCO, alpha=0.92, linespacing=1.45)
        ax.text(x + ancho / 2, 1.38, alcance, ha="center", va="center", family=F,
                fontsize=8, color=AMBAR, alpha=0.9)
    ax.text(5.05, 0.42, "La sección de la labor decide con qué se limpia.",
            ha="center", va="center", family=F, fontsize=10.5, color=AZUL)
    f = SALIDA / "carguio-segun-seccion.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return f


if __name__ == "__main__":
    f = carguio_segun_seccion()
    print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")
