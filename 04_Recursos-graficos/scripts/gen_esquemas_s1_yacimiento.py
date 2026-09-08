# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 · El yacimiento.

Cada uno responde a la frase `que_muestra` de su lámina, escrita ANTES de
producir. Son dibujo determinista: cajas, cortes y cotas trazadas por código.

MÉTRICA DEL §11 — es lo que separa un esquema legible de uno que no lo es:

    lienzo 1500 px  ·  cuerpo 52 px  ·  nota al pie 42 px
    pt_proyectado = 6 × px_fuente ÷ px_lienzo × 72   →   15 pt

    Con dpi=200: pt_matplotlib = px × 72 / 200. De ahí CUERPO y NOTA.
    NO se usa bbox_inches="tight": recorta el lienzo y rompe la razón
    fuente/ancho, que es lo que decide la legibilidad.

Proporción ~1,07 para entrar en el hueco de lámina de tema (6,15 × 5,85 in).
Los esquemas van SIN título dentro: el título lo pone la lámina.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle

# ---------------------------------------------------------------- la paleta §11
MARINO = "#0D2632"   # texto, cabeceras, bloques de énfasis
AZUL = "#167FB9"     # primera categoría
VERDE = "#00B29C"    # segunda
MORADO = "#5052A9"   # tercera
AMBAR = "#FFC505"    # lo que hay que destacar — texto marino encima, nunca blanco
GRIS = "#6C7A82"     # texto secundario
CLARO = "#EEF1F3"    # fondo de bloque
BLANCO = "#FFFFFF"

F = "Arial"
DPI = 200
ANCHO_PX = 1500
PROPORCION = 1.07

CUERPO = 52 * 72 / DPI      # 18.7 pt → 52 px → 15 pt proyectados
NOTA = 42 * 72 / DPI        # 15.1 pt → 42 px → 12 pt proyectados
FUERTE = 58 * 72 / DPI      # rótulo de bloque, un punto por encima del cuerpo

SALIDA = Path(__file__).resolve().parent.parent / "EOM" / "esquemas"


def lienzo(alto_rel=PROPORCION):
    """Figura de 1500 px de ancho. Coordenadas 0-100 en x para trazar cómodo."""
    ancho_in = ANCHO_PX / DPI
    fig, ax = plt.subplots(figsize=(ancho_in, ancho_in / alto_rel), dpi=DPI)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 / alto_rel)
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.patch.set_facecolor(BLANCO)
    return fig, ax


def guardar(fig, nombre):
    """Guarda en la carpeta de su sesión.

    Los esquemas se ordenan por sesión (Erick, 2026-09-02): s1/, s2/, ... y
    comun/ para lo que sirve a más de una. El nombre ya lleva el prefijo —
    `s1_ruta.png`—, así que la carpeta se deduce de él y ningún script tiene
    que acordarse. Sin esto, un esquema regenerado caía en la carpeta vieja y
    el PPT seguía usando la copia anterior sin avisar.
    """
    import re
    if "/" not in nombre:
        m = re.match(r"(s\d+)_", nombre)
        nombre = ("metexp/%s/%s" % (m.group(1), nombre)) if m else "comun/" + nombre
# CARPETAS. Los esquemas de EOM se ordenan por CURSO y luego por sesion:
# metexp/s1..s11, sost/s1..., y comun/ para lo que sirve a mas de uno.
# Antes colgaban de la raiz por sesion, cuando EOM tenia un solo curso
# disenado; con el segundo, «s1» era ambiguo. Ver OBS-EOM-SOST-18.

    f = SALIDA / nombre
    f.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(f, dpi=DPI, facecolor=BLANCO)   # sin bbox_inches: el ancho manda
    plt.close(fig)
    return f


def nota(ax, y, texto):
    ax.text(50, y, texto, ha="center", va="center", family=F, fontsize=NOTA, color=GRIS)


def rotulo(ax, x, y, texto, color=MARINO, size=None):
    ax.text(x, y, texto, ha="center", va="center", family=F,
            fontsize=size or FUERTE, fontweight="bold", color=color)


def cuerpo(ax, x, y, texto, color=MARINO, ha="center"):
    ax.text(x, y, texto, ha=ha, va="center", family=F, fontsize=CUERPO,
            color=color, linespacing=1.35)


# ══════════════════════════════════════════════ 1 · los tres tipos de cuerpo
def tipos_de_cuerpo():
    """Veta, manto y cuerpo masivo en corte, uno al lado del otro."""
    fig, ax = plt.subplots(figsize=(ANCHO_PX / DPI, ANCHO_PX / DPI / PROPORCION), dpi=DPI)
    ax.set_xlim(0, 100); ax.set_ylim(0, 93.5); ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.patch.set_facecolor(BLANCO)

    paneles = [
        (2.5, "VETA", AZUL, "delgada y larga,\nentre dos cajas"),
        (35.0, "MANTO", VERDE, "una capa echada,\ncomo un piso"),
        (67.5, "CUERPO\nMASIVO", MORADO, "un volumen ancho\npor todos lados"),
    ]
    ancho, x0, y0, alto = 30.0, 0, 48, 38

    for x, nombre, color, pie in paneles:
        # la roca de alrededor
        ax.add_patch(Rectangle((x, y0), ancho, alto, facecolor=CLARO,
                               edgecolor=GRIS, linewidth=1.4))
        cx = x + ancho / 2

        if nombre == "VETA":
            ax.add_patch(Polygon([(x + 9, y0 + 1), (x + 13.5, y0 + 1),
                                  (x + 22, y0 + alto - 1), (x + 17.5, y0 + alto - 1)],
                                 facecolor=color, edgecolor=MARINO, linewidth=1.2))
            ax.text(x + 4.5, y0 + alto / 2, "caja", ha="center", va="center",
                    family=F, fontsize=NOTA, color=GRIS, rotation=90)
            ax.text(x + 26, y0 + alto / 2, "caja", ha="center", va="center",
                    family=F, fontsize=NOTA, color=GRIS, rotation=90)
        elif nombre == "MANTO":
            ax.add_patch(Polygon([(x + 1, y0 + 13), (x + ancho - 1, y0 + 17),
                                  (x + ancho - 1, y0 + 23), (x + 1, y0 + 19)],
                                 facecolor=color, edgecolor=MARINO, linewidth=1.2))
        else:
            ax.add_patch(Polygon([(x + 6, y0 + 5), (x + 24, y0 + 7),
                                  (x + 26, y0 + 26), (x + 8, y0 + 29)],
                                 facecolor=color, edgecolor=MARINO, linewidth=1.2))

        rotulo(ax, cx, y0 - 7.5, nombre, color=color)
        cuerpo(ax, cx, y0 - 22, pie)

    nota(ax, 9, "El mineral es lo pintado; lo gris, la roca que lo rodea.")
    return guardar(fig, "s1_tipos-de-cuerpo.png")


# ══════════════════════════════════════════════ 2 · la forma manda las labores
def forma_y_labores():
    """Los mismos tres cuerpos, con la labor dibujada encima."""
    fig, ax = plt.subplots(figsize=(ANCHO_PX / DPI, ANCHO_PX / DPI / PROPORCION), dpi=DPI)
    ax.set_xlim(0, 100); ax.set_ylim(0, 93.5); ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.patch.set_facecolor(BLANCO)

    ancho, y0, alto = 30.0, 48, 38
    for x, nombre, color, pie in [
        (2.5, "VETA", AZUL, "se sube por cortes,\nuno encima del otro"),
        (35.0, "MANTO", VERDE, "se avanza horizontal,\nabriendo cámaras"),
        (67.5, "CUERPO\nMASIVO", MORADO, "se prepara por subniveles\ny se saca al vacío"),
    ]:
        ax.add_patch(Rectangle((x, y0), ancho, alto, facecolor=CLARO,
                               edgecolor=GRIS, linewidth=1.4))
        cx = x + ancho / 2

        if nombre == "VETA":
            ax.add_patch(Polygon([(x + 9, y0 + 1), (x + 13.5, y0 + 1),
                                  (x + 22, y0 + alto - 1), (x + 17.5, y0 + alto - 1)],
                                 facecolor=color, alpha=0.35, edgecolor=MARINO, linewidth=1))
            for k in range(4):                       # los cortes, uno sobre otro
                yy = y0 + 4 + k * 7.2
                ax.add_patch(Rectangle((x + 10 + k * 2.1, yy), 4.6, 4.4,
                                       facecolor=AMBAR, edgecolor=MARINO, linewidth=1.1))
        elif nombre == "MANTO":
            ax.add_patch(Polygon([(x + 1, y0 + 13), (x + ancho - 1, y0 + 17),
                                  (x + ancho - 1, y0 + 23), (x + 1, y0 + 19)],
                                 facecolor=color, alpha=0.35, edgecolor=MARINO, linewidth=1))
            for k in range(4):                       # cámaras y pilares
                ax.add_patch(Rectangle((x + 3 + k * 6.4, y0 + 15.4 + k * 1.0), 4.3, 4.6,
                                       facecolor=AMBAR, edgecolor=MARINO, linewidth=1.1))
        else:
            ax.add_patch(Polygon([(x + 6, y0 + 5), (x + 24, y0 + 7),
                                  (x + 26, y0 + 26), (x + 8, y0 + 29)],
                                 facecolor=color, alpha=0.35, edgecolor=MARINO, linewidth=1))
            for yy in (y0 + 9, y0 + 18, y0 + 26):    # los subniveles
                ax.plot([x + 4, x + 27], [yy, yy], color=MARINO, lw=2.2)
                ax.add_patch(Rectangle((x + 12, yy - 1.4), 8, 2.8,
                                       facecolor=AMBAR, edgecolor=MARINO, linewidth=1))

        rotulo(ax, cx, y0 - 7.5, nombre, color=color)
        cuerpo(ax, cx, y0 - 22, pie)

    nota(ax, 9, "En ámbar, la labor que se abre para sacar el mineral.")
    return guardar(fig, "s1_forma-y-labores.png")


# ══════════════════════════════════════════════ 3 · la potencia es el ancho
def potencia_cota():
    """Corte de una veta con la potencia acotada de caja a caja."""
    fig, ax = lienzo()
    H = 100 / PROPORCION

    ax.add_patch(Rectangle((6, 16), 88, H - 32, facecolor=CLARO,
                           edgecolor=GRIS, linewidth=1.4))
    veta = Polygon([(30, 16), (43, 16), (66, H - 16), (53, H - 16)],
                   facecolor=AZUL, edgecolor=MARINO, linewidth=1.4)
    ax.add_patch(veta)

    ax.text(17, H / 2, "CAJA PISO", ha="center", va="center", family=F,
            fontsize=CUERPO, color=GRIS, rotation=90)
    ax.text(80, H / 2, "CAJA TECHO", ha="center", va="center", family=F,
            fontsize=CUERPO, color=GRIS, rotation=90)

    # la cota: perpendicular a la veta, no horizontal
    ax.annotate("", xy=(50.5, 52.8), xytext=(38.3, 59.4),
                arrowprops=dict(arrowstyle="<|-|>", color=MARINO, lw=2.6,
                                mutation_scale=22))
    ax.add_patch(FancyBboxPatch((30, 63), 40, 10,
                                boxstyle="round,pad=0.4,rounding_size=1.4",
                                facecolor=AMBAR, edgecolor=MARINO, linewidth=1.4))
    ax.text(50, 68, "POTENCIA", ha="center", va="center", family=F,
            fontsize=FUERTE, fontweight="bold", color=MARINO)

    cuerpo(ax, 50, 9, "Se mide de caja a caja, perpendicular a la veta.\n"
                      "Nunca a lo largo: eso daría un ancho falso.")
    return guardar(fig, "s1_potencia-cota.png")


# ══════════════════════════════════════════════ 4 · la potencia decide el equipo
def potencia_equipo():
    """Dos labores a la misma escala, con la persona como referencia."""
    fig, ax = lienzo()
    H = 100 / PROPORCION
    ESC = 9.0          # unidades de dibujo por metro — la MISMA en las dos
    base = 34

    def persona(cx, y):
        ax.add_patch(Circle((cx, y + 1.55 * ESC), 0.17 * ESC,
                            facecolor=MARINO, edgecolor="none"))
        ax.add_patch(Rectangle((cx - 0.19 * ESC, y + 0.62 * ESC),
                               0.38 * ESC, 0.78 * ESC,
                               facecolor=MARINO, edgecolor="none"))
        for dx in (-0.17, 0.05):
            ax.add_patch(Rectangle((cx + dx * ESC, y), 0.12 * ESC, 0.64 * ESC,
                                   facecolor=MARINO, edgecolor="none"))

    for x0, anchura, altura, nombre, equipo, color in [
        (11, 0.90, 2.00, "0,90 m", "jackleg", AZUL),
        (52, 4.00, 3.50, "4,00 m", "jumbo", VERDE),
    ]:
        w, h = anchura * ESC, altura * ESC
        ax.add_patch(Rectangle((x0, base), w, h, facecolor=CLARO,
                               edgecolor=MARINO, linewidth=2.0))
        persona(x0 + (w * 0.28 if anchura > 1 else w / 2), base)
        if anchura > 1:                              # el jumbo, esquemático
            ax.add_patch(Rectangle((x0 + w * 0.45, base + 0.15 * ESC),
                                   w * 0.42, 0.95 * ESC,
                                   facecolor=color, edgecolor=MARINO, linewidth=1.3))
            ax.plot([x0 + w * 0.87, x0 + w * 0.97], [base + 0.9 * ESC, base + 1.5 * ESC],
                    color=MARINO, lw=2.4)
        else:
            ax.plot([x0 + w / 2 + 1.4, x0 + w / 2 + 2.2],
                    [base + 0.5 * ESC, base + 1.9 * ESC], color=color, lw=3.4)

        ax.annotate("", xy=(x0, base - 3.2), xytext=(x0 + w, base - 3.2),
                    arrowprops=dict(arrowstyle="<|-|>", color=MARINO, lw=2.2,
                                    mutation_scale=18))
        rotulo(ax, x0 + w / 2, base - 8.5, nombre)
        ax.add_patch(FancyBboxPatch((x0 + w / 2 - 11, base + h + 3), 22, 9,
                                    boxstyle="round,pad=0.4,rounding_size=1.4",
                                    facecolor=color, edgecolor="none"))
        ax.text(x0 + w / 2, base + h + 7.5, equipo, ha="center", va="center",
                family=F, fontsize=FUERTE, fontweight="bold", color=BLANCO)

    cuerpo(ax, 50, 14, "Misma escala en las dos, y la persona mide 1,70 m.")
    nota(ax, 6, "Con menos de un metro no entra equipo mecanizado.")
    return guardar(fig, "s1_potencia-equipo.png")


# ══════════════════════════════════════════════ 5 · el buzamiento
def buzamiento():
    """El mismo cuerpo a 8°, 45° y 70°, con el mineral cayendo o quedándose."""
    import math
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y0, alto, ancho = 45, 32, 28

    for i, (grados, cae, color) in enumerate([(8, False, MORADO), (45, False, AZUL),
                                              (70, True, VERDE)]):
        x = 3 + i * 32.5
        ax.add_patch(Rectangle((x, y0), ancho, alto, facecolor=CLARO,
                               edgecolor=GRIS, linewidth=1.4))
        cx, cy = x + ancho / 2, y0 + alto / 2
        rad = math.radians(grados)
        largo, grosor = 11.4, 3.0
        dx, dy = largo * math.cos(rad), largo * math.sin(rad)
        nx, ny = -grosor * math.sin(rad), grosor * math.cos(rad)
        ax.add_patch(Polygon([(cx - dx + nx, cy - dy + ny), (cx + dx + nx, cy + dy + ny),
                              (cx + dx - nx, cy + dy - ny), (cx - dx - nx, cy - dy - ny)],
                             facecolor=color, edgecolor=MARINO, linewidth=1.3))
        ax.plot([x + 2, x + ancho - 2], [cy - dy, cy - dy], color=GRIS,
                lw=1.2, linestyle=(0, (4, 3)))
        rotulo(ax, cx, y0 - 7.5, "%d°" % grados, color=color)

        if cae:
            ax.annotate("", xy=(cx - dx + 2.5, cy - dy + 1.5), xytext=(cx + 2, cy + 5),
                        arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.6,
                                        mutation_scale=22))
            cuerpo(ax, cx, y0 - 20, "el mineral\nbaja solo")
        else:
            ax.add_patch(Rectangle((cx - 3.4, cy - 1.6), 6.8, 3.2,
                                   facecolor=AMBAR, edgecolor=MARINO, linewidth=1.2))
            cuerpo(ax, cx, y0 - 20, "hay que\nempujarlo")

    cuerpo(ax, 50, 15, "La inclinación del cuerpo respecto de la horizontal.")
    nota(ax, 7, "Sobre 50° el carguío lo hace la gravedad. Bajo 30°, el equipo.")
    return guardar(fig, "s1_buzamiento.png")


# ══════════════════════════════════════════════ 6 · los tres datos juntos
def tres_datos():
    """Qué decide cada dato. Tres bandas, una por dato: la matriz de 3x3 era
    mayormente guiones —celdas vacías— y a 52 px no cabía a lo ancho."""
    fig, ax = lienzo()
    H = 100 / PROPORCION

    bandas = [("FORMA", AZUL, "qué labores\nvoy a ver allá abajo"),
              ("POTENCIA", VERDE, "si entra equipo\no trabajo a mano"),
              ("BUZAMIENTO", MORADO, "hacia dónde avanzo\ny si el mineral cae solo")]

    x0, w_rot, alto, hueco = 4, 34, 18, 4.5
    y = H - 24

    for nombre, color, decide in bandas:
        ax.add_patch(FancyBboxPatch((x0, y), w_rot, alto,
                                    boxstyle="round,pad=0.3,rounding_size=1.2",
                                    facecolor=color, edgecolor="none"))
        ax.text(x0 + w_rot / 2, y + alto / 2, nombre, ha="center", va="center",
                family=F, fontsize=CUERPO, fontweight="bold", color=BLANCO)
        ax.annotate("", xy=(x0 + w_rot + 8.5, y + alto / 2),
                    xytext=(x0 + w_rot + 2.5, y + alto / 2),
                    arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4,
                                    mutation_scale=20))
        ax.add_patch(FancyBboxPatch((x0 + w_rot + 10, y), 100 - x0 * 2 - w_rot - 10, alto,
                                    boxstyle="round,pad=0.3,rounding_size=1.2",
                                    facecolor=CLARO, edgecolor="none"))
        ax.text(x0 + w_rot + 10 + (100 - x0 * 2 - w_rot - 10) / 2, y + alto / 2, decide,
                ha="center", va="center", family=F, fontsize=CUERPO, color=MARINO,
                linespacing=1.3)
        y -= alto + hueco

    cuerpo(ax, 50, 15, "Un método se aplica donde los tres datos lo permiten.")
    nota(ax, 7, "Ningún dato manda solo: los tres se leen a la vez.")
    return guardar(fig, "s1_tres-datos.png")


# ══════════════════════════════ 7 · el estimulo de la Conexion (Veo-Pienso)
def frente_veta():
    """Un frente donde se distingue la franja de mineral entre las dos cajas.

    SIN rotulos, SIN flechas y SIN medidas: es el estimulo de una rutina de
    pensamiento, y el §11 pide que muestre HECHOS. Si le pongo la potencia
    acotada o la palabra "veta", interpreto yo lo que el alumno tiene que ver.
    """
    import math
    fig, ax = lienzo()
    H = 100 / PROPORCION

    ax.add_patch(Rectangle((0, 0), 100, H, facecolor="#DDE3E6", edgecolor="none"))

    # la franja de mineral, inclinada
    veta = Polygon([(28, -2), (41, -2), (72, H + 2), (59, H + 2)],
                   facecolor="#8C7A55", edgecolor="#4A4130", linewidth=2.2)
    ax.add_patch(veta)

    # achurado a plumilla en la roca de caja, a 45°, junto al limite (§10)
    for lado, signo in ((0, -1), (1, 1)):
        for k in range(46):
            t = k / 45.0
            xb = (28 if lado == 0 else 41) + t * 31
            yb = -2 + t * (H + 4)
            for d in (1.6, 3.4, 5.2, 7.0):
                x1 = xb + signo * d
                ax.plot([x1, x1 + signo * 2.0], [yb, yb - 2.0],
                        color="#7C8A92", lw=0.7, alpha=0.55)

    # la labor: un vacio ya excavado sobre la franja
    ax.add_patch(Polygon([(38.5, 18), (52.5, 18), (59.5, 52), (45.5, 52)],
                         facecolor=BLANCO, edgecolor=MARINO, linewidth=2.8))
    # roca suelta en el piso de la labor
    for cx, cy, r in ((43.5, 21.5, 2.3), (48.6, 20.6, 3.0), (53.4, 22.6, 1.9),
                      (46.2, 25.6, 1.7), (51.5, 25.0, 1.4)):
        ax.add_patch(Circle((cx, cy), r, facecolor="#9AA6AC", edgecolor="#5F6C73",
                            linewidth=0.9))
    # un perno instalado en la caja de la labor
    for yy in (34, 41, 48):
        x1 = 40.7 + (yy - 18) * 0.41
        ax.plot([x1, x1 - 4.2], [yy, yy - 1.2], color=MARINO, lw=2.6)
        ax.plot([x1 - 4.2], [yy - 1.2], marker="s", markersize=6, color=MARINO)

    return guardar(fig, "s1_frente-veta.png")


if __name__ == "__main__":
    from PIL import Image
    for fn in (tipos_de_cuerpo, forma_y_labores, potencia_cota,
               potencia_equipo, buzamiento, tres_datos, frente_veta):
        f = fn()
        w, h = Image.open(f).size
        pt = 6 * 52 / w * 72
        print("  %-30s %4d x %4d px   cuerpo -> %.1f pt proyectados %s"
              % (f.name, w, h, pt, "OK" if pt >= 14.5 else "!! BAJO"))
