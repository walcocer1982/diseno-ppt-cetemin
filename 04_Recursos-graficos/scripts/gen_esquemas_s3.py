# -*- coding: utf-8 -*-
"""Esquemas de la sesion 3: clasificacion de metodos y sus condiciones.

Cada uno responde a la frase `que_muestra` de su lamina, escrita ANTES de
producir. Los cuatro son esquemas COMPARATIVOS porque las laminas ensenan
criterios —como se sostiene el vacio, cuando se usa cada metodo—, y un criterio
se muestra comparando, no con la foto de un tajeo.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

AZUL, AMBAR, BLANCO, GRIS = "#0D2632", "#FFC505", "#FFFFFF", "#8A9AA3"
F = "Arial"
SALIDA = Path("../EOM/esquemas/comun")
# CARPETAS. Los esquemas de EOM se ordenan por CURSO y luego por sesion:
# metexp/s1..s11, sost/s1..., y comun/ para lo que sirve a mas de uno.
# Antes colgaban de la raiz por sesion, cuando EOM tenia un solo curso
# disenado; con el segundo, «s1» era ambiguo. Ver OBS-EOM-SOST-18.



def tres_formas_de_sostener() -> Path:
    """Los tres grupos, por como sostienen el vacio que deja la extraccion."""
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.1, 4.6); ax.axis("off")
    fig.patch.set_alpha(0)
    grupos = [("SOPORTADOS", "el macizo se sostiene solo",
               "cámaras y pilares\nsublevel stoping", "pilares del propio mineral"),
              ("ARTIFICIALMENTE\nSOPORTADOS", "el vacío se rellena o apuntala",
               "corte y relleno\ncorte y almacenamiento", "relleno, madera o pilares artificiales"),
              ("POR HUNDIMIENTO", "el vacío se deja caer a propósito",
               "block caving\nsublevel caving", "no se sostiene: el techo hunde")]
    ancho = 3.05
    for i, (nombre, como, cuales, con_que) in enumerate(grupos):
        x = i * 3.45
        ax.add_patch(FancyBboxPatch((x, 0.95), ancho, 2.95,
                     boxstyle="round,pad=0.03,rounding_size=0.09",
                     facecolor=AZUL, edgecolor=AMBAR, linewidth=1.6))
        ax.text(x + ancho / 2, 3.52, nombre, ha="center", va="center", family=F,
                fontsize=11, fontweight="bold", color=BLANCO, linespacing=1.3)
        ax.text(x + ancho / 2, 2.92, como, ha="center", va="center", family=F,
                fontsize=9, fontweight="bold", color=AMBAR)
        ax.text(x + ancho / 2, 2.28, con_que, ha="center", va="center", family=F,
                fontsize=8.4, color=BLANCO, alpha=0.9, linespacing=1.4)
        ax.plot([x + 0.5, x + ancho - 0.5], [1.92, 1.92], color=GRIS, lw=0.8)
        ax.text(x + ancho / 2, 1.42, cuales, ha="center", va="center", family=F,
                fontsize=9, color=BLANCO, alpha=0.85, linespacing=1.5)
    ax.text(5.05, 0.35, "Lo que separa a los tres grupos es qué sostiene el hueco que deja el mineral extraído.",
            ha="center", va="center", family=F, fontsize=10, color=AZUL)
    f = SALIDA / "tres-formas-sostener-vacio.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06); plt.close(fig)
    return f


def tipos_de_relleno() -> Path:
    """Los cuatro rellenos: de que estan hechos y para que sirven."""
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.1, 3.9); ax.axis("off")
    fig.patch.set_alpha(0)
    tipos = [("DETRÍTICO", "roca estéril\nde la propia mina", "el más barato\nno se compacta bien"),
             ("HIDRÁULICO", "relave clasificado\nbombeado con agua", "llena bien\nnecesita drenaje"),
             ("CEMENTADO", "relave con cemento", "queda firme\ny permite trabajar encima"),
             ("EN PASTA", "relave espesado\ncon cemento", "no drena\nse bombea por tubería")]
    ancho = 2.30
    for i, (nombre, de_que, para) in enumerate(tipos):
        x = i * 2.52
        ax.add_patch(FancyBboxPatch((x, 0.85), ancho, 2.35,
                     boxstyle="round,pad=0.03,rounding_size=0.09",
                     facecolor=AZUL, edgecolor=AMBAR, linewidth=1.6))
        ax.text(x + ancho / 2, 2.88, nombre, ha="center", va="center", family=F,
                fontsize=11, fontweight="bold", color=BLANCO)
        ax.text(x + ancho / 2, 2.28, de_que, ha="center", va="center", family=F,
                fontsize=8.6, color=AMBAR, linespacing=1.45)
        ax.text(x + ancho / 2, 1.35, para, ha="center", va="center", family=F,
                fontsize=8.4, color=BLANCO, alpha=0.9, linespacing=1.5)
    ax.text(5.05, 0.30, "El relleno da piso para el corte de arriba y sostiene las cajas.",
            ha="center", va="center", family=F, fontsize=10, color=AZUL)
    f = SALIDA / "tipos-de-relleno.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06); plt.close(fig)
    return f


def condiciones(metodo: str) -> Path:
    """Que le pide el yacimiento a cada metodo. Mismo esquema, otro resaltado."""
    filas = [("POTENCIA",   "angosta · menos de 3 m",  "potente · manto de varios metros"),
             ("BUZAMIENTO", "alto · más de 60°",       "bajo · casi horizontal"),
             ("LA ROCA",    "admite cajas malas",      "necesita techo competente"),
             ("LA LEY",     "alta · no se puede perder mineral", "baja · el volumen compensa"),
             ("EL COSTO",   "caro y lento",            "barato y rápido"),
             ("RECUPERA",   "casi todo el mineral",    "deja mineral en los pilares")]
    cr = metodo == "corte-y-relleno"
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=200)
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.2, 4.9); ax.axis("off")
    fig.patch.set_alpha(0)
    ax.add_patch(Rectangle((3.55, 0.35), 3.05, 4.05,
                 facecolor=AZUL if cr else "none", edgecolor=AMBAR if cr else "none", lw=2))
    ax.add_patch(Rectangle((6.75, 0.35), 3.05, 4.05,
                 facecolor="none" if cr else AZUL, edgecolor="none" if cr else AMBAR, lw=2))
    ax.text(5.07, 4.60, "CORTE Y RELLENO", ha="center", family=F, fontsize=11.5,
            fontweight="bold", color=AZUL if not cr else AZUL)
    ax.text(8.27, 4.60, "CÁMARAS Y PILARES", ha="center", family=F, fontsize=11.5,
            fontweight="bold", color=AZUL)
    y = 3.95
    for k, a, b in filas:
        ax.text(0.15, y, k, family=F, fontsize=9.5, fontweight="bold", color=AZUL, va="center")
        ax.text(5.07, y, a, ha="center", va="center", family=F, fontsize=8.8,
                color=BLANCO if cr else GRIS)
        ax.text(8.27, y, b, ha="center", va="center", family=F, fontsize=8.8,
                color=GRIS if cr else BLANCO)
        y -= 0.62
    f = SALIDA / f"condiciones-{metodo}.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06); plt.close(fig)
    return f


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    for f in (tres_formas_de_sostener(), tipos_de_relleno(),
              condiciones("corte-y-relleno"), condiciones("camaras-y-pilares")):
        print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")


def camaras_y_pilares() -> Path:
    """El damero en planta y la seccion con los pilares dejados.

    Se dibuja porque no aparecio en las fuentes disponibles y porque es
    GEOMETRIA DE METODO, no de equipo: no hay cotas de catalogo que verificar.
    La disposicion es la caracteristica del metodo — pilares regulares y
    camaras entre ellos—, no una malla de diseno de una mina concreta.
    """
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 4.6), dpi=200,
                                 gridspec_kw={"width_ratios": [1.15, 1]})
    fig.patch.set_alpha(0)

    # --- planta: el damero
    a1.set_xlim(-0.4, 7.4); a1.set_ylim(-0.9, 6.2); a1.axis("off"); a1.set_aspect("equal")
    a1.add_patch(Rectangle((0, 0), 7, 5.4, facecolor="#EEF1F2", edgecolor=AZUL, lw=1.6))
    for fx in range(4):
        for fy in range(3):
            a1.add_patch(Rectangle((0.75 + fx * 1.65, 0.65 + fy * 1.65), 0.95, 0.95,
                         facecolor=AZUL, edgecolor=AMBAR, lw=1.4))
    a1.annotate("", xy=(2.20, 5.75), xytext=(0.75, 5.75),
                arrowprops=dict(arrowstyle="<->", color=GRIS, lw=1.2))
    a1.text(1.47, 5.95, "cámara", ha="center", family=F, fontsize=8.5, color=GRIS)
    a1.plot([1.22, 1.22], [1.75, 2.35], color=GRIS, lw=1)
    a1.text(1.22, 2.55, "pilar", ha="center", family=F, fontsize=8.5, color=GRIS)
    a1.text(3.5, -0.65, "EN PLANTA · el damero de pilares y cámaras",
            ha="center", family=F, fontsize=9.5, fontweight="bold", color=AZUL)

    # --- seccion: el manto y lo que queda dentro del pilar
    a2.set_xlim(-0.3, 7.3); a2.set_ylim(-0.9, 6.2); a2.axis("off")
    a2.add_patch(Rectangle((0, 3.4), 7, 1.15, facecolor="#D9DEE0", edgecolor=AZUL, lw=1.4))
    a2.text(3.5, 3.97, "techo", ha="center", va="center", family=F, fontsize=8.5, color=AZUL)
    for i in range(4):
        a2.add_patch(Rectangle((0.55 + i * 1.75, 2.05), 0.75, 1.35,
                     facecolor=AMBAR, edgecolor=AZUL, lw=1.2))
    a2.add_patch(Rectangle((0, 1.55), 7, 0.5, facecolor="#D9DEE0", edgecolor=AZUL, lw=1.4))
    a2.text(3.5, 1.80, "piso", ha="center", va="center", family=F, fontsize=8.5, color=AZUL)
    a2.plot([0.92, 0.92], [1.20, 1.95], color=GRIS, lw=1)
    a2.text(0.92, 0.95, "el pilar es mineral\nque no se extrae", ha="center", va="top",
            family=F, fontsize=8.2, color=AZUL, linespacing=1.4)
    a2.text(3.5, -0.65, "EN SECCIÓN · el pilar sostiene el techo",
            ha="center", family=F, fontsize=9.5, fontweight="bold", color=AZUL)

    f = SALIDA / "camaras-y-pilares.png"
    fig.savefig(f, transparent=True, bbox_inches="tight", pad_inches=0.06); plt.close(fig)
    return f


if __name__ == "__main__":
    f = camaras_y_pilares()
    print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")
