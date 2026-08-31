# -*- coding: utf-8 -*-
"""Kit para dibujar los esquemas de las láminas. Común a las tres carreras.

POR QUÉ EXISTE
    El texto dentro de una imagen se reduce cuando la imagen entra en la lámina.
    Lo que decide si se lee no es el tamaño en píxeles sino la RAZÓN entre la
    fuente y el ancho del lienzo:

        pt_proyectado = 6 * px_fuente / px_ancho_lienzo * 72

    Con W = 1500 y cuerpo de 52 px salen 15 pt. Con 24 px sobre 1841 salían 5,6.

CÓMO SE USA
    from esquemas import *

    im, d = lienzo(1200)
    filas_letra(d, [("S", "SEGURIDAD", "Protege del accidente", AZUL2), ...])
    guardar(im, "ssomac_cuatro-letras.png", DEST)

REGLAS
    · un esquema, una idea. Más de 6 bloques o más de 4 líneas por bloque = dos esquemas
    · sin título: el título lo pone la lámina
    · si es estímulo de una rutina, muestra HECHOS y ningún juicio
    · los colores salen de la paleta de abajo, siempre

Requiere Pillow:  python -m pip install pillow
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageChops

# ── el lienzo y los tamaños ───────────────────────────────────────────────
W = 1500                     # ancho fijo: de aquí salen los pt proyectados
TIT, CUE, NOTA = 62, 52, 42  # 17,9 · 15,0 · 12,1 pt

# ── la paleta (§11). Usar siempre estos ───────────────────────────────────
AZUL   = (13, 38, 50)        # #0D2632  texto, cabeceras, bloques de énfasis
AZUL2  = (22, 127, 185)      # #167FB9  primera categoría
TEAL   = (0, 178, 156)       # #00B29C  segunda
MORADO = (80, 82, 169)       # #5052A9  tercera
AMBAR  = (255, 197, 5)       # #FFC505  lo que hay que destacar (texto AZUL encima)
GRIS   = (108, 122, 130)     # #6C7A82  texto secundario
GRISC  = (238, 241, 243)     # #EEF1F3  fondo de bloque
BLANCO = (255, 255, 255)
ROJO   = (192, 57, 43)       # #C0392B  solo lo que está mal. Con moderación

FUENTES = r"C:\Windows\Fonts"   # Arial: es la única instalada en los equipos


# ── utilidades ────────────────────────────────────────────────────────────
def fu(px, bold=False):
    return ImageFont.truetype(os.path.join(FUENTES, "arialbd.ttf" if bold else "arial.ttf"), px)


def an(d, t, f):
    a = d.textbbox((0, 0), t, font=f)
    return a[2] - a[0]


def cen(d, x, y, w, t, px, color, bold=True, margen=30):
    """Centra el texto y, si no cabe, baja de punto hasta que quepa."""
    f = fu(px, bold)
    while an(d, t, f) > w - margen and px > 26:
        px -= 2
        f = fu(px, bold)
    d.text((x + (w - an(d, t, f)) / 2, y), t, font=f, fill=color)


def izq(d, x, y, t, px, color, bold=False):
    d.text((x, y), t, font=fu(px, bold), fill=color)


def envolver(d, t, px, ancho):
    f, lineas, act = fu(px), [], ""
    for p in t.split():
        s = (act + " " + p).strip()
        if an(d, s, f) <= ancho:
            act = s
        else:
            lineas.append(act); act = p
    if act:
        lineas.append(act)
    return lineas


def lienzo(alto):
    im = Image.new("RGB", (W, alto), BLANCO)
    return im, ImageDraw.Draw(im)


def guardar(im, nombre, destino):
    """Recorta el aire sobrante y guarda. Sin recorte el esquema se dibuja
    más pequeño de lo que cabe, porque el hueco se llena por proporción."""
    caja = ImageChops.difference(im, Image.new("RGB", im.size, BLANCO)).getbbox()
    if caja:
        m = 24
        im = im.crop((max(0, caja[0] - m), max(0, caja[1] - m),
                      min(im.width, caja[2] + m), min(im.height, caja[3] + m)))
    os.makedirs(destino, exist_ok=True)
    im.save(os.path.join(destino, nombre), "PNG")
    print("   %-42s %sx%s · cuerpo %.1f pt" % (nombre, im.width, im.height,
                                               6.0 * CUE / im.width * 72))
    return im


def banda(d, y, alto, texto, px=NOTA, fondo=GRISC, tinta=AZUL):
    """Franja de cierre con la idea que hay que llevarse."""
    d.rounded_rectangle([50, y, W - 50, y + alto], 18, fill=fondo)
    cen(d, 50, y + (alto - px) / 2 - 6, W - 100, texto, px, tinta)


# ── las seis formas que ya funcionan ──────────────────────────────────────
def filas_letra(d, filas, y=60, alto=280, sep=30):
    """(letra, NOMBRE, detalle, color) — para siglas: SSOMAC, PHVA…"""
    for letra, nombre, det, col in filas:
        d.rounded_rectangle([50, y, W - 50, y + alto], 20, fill=GRISC)
        d.rounded_rectangle([50, y, 300, y + alto], 20, fill=col)
        d.rectangle([260, y, 300, y + alto], fill=col)
        cen(d, 50, y + alto / 2 - 58, 250, letra, 92, AZUL if col == AMBAR else BLANCO)
        izq(d, 350, y + 62, nombre, TIT, AZUL, True)
        izq(d, 350, y + 155, det, CUE, GRIS)
        y += alto + sep
    return y


def tabla(d, encabezados, filas, cortes, y=60):
    """Comparar por columnas. filas = [([col1...], [col2...], destacado, fondo, tinta)]"""
    x = cortes
    d.rectangle([x[0], y, x[-1], y + 100], fill=AZUL)
    for i, t in enumerate(encabezados):
        cen(d, x[i], y + 26, x[i + 1] - x[i], t, 48, BLANCO)
    y += 100
    for celdas, destacado, fondo, tinta in filas:
        alto = 60 + max(len(c) for c in celdas) * 66
        d.rectangle([x[0], y, x[-1], y + alto], fill=BLANCO, outline=(214, 220, 224), width=3)
        if destacado:
            d.rectangle([x[-2] + 14, y + 20, x[-1] - 14, y + alto - 20], fill=fondo)
        for j, col in enumerate(celdas):
            for i, t in enumerate(col):
                izq(d, x[j] + 32, y + (alto - len(col) * 64) / 2 + i * 64, t, CUE, AZUL)
        if destacado:
            cen(d, x[-2], y + alto / 2 - 26, x[-1] - x[-2], destacado, 46, tinta)
        y += alto
    return y


def ciclo(d, cuadrantes, cx, cy, R=560, r=310, centro=None, lista=()):
    """Anillo de cuatro cuadrantes. cuadrantes = [(letra, NOMBRE, ang0, ang1, color)]"""
    for _, _, a0, a1, col in cuadrantes:
        d.pieslice([cx - R, cy - R, cx + R, cy + R], a0 + 3, a1 - 3, fill=col)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANCO)
    for letra, nombre, a0, a1, col in cuadrantes:
        ang = math.radians((a0 + a1) / 2)
        px, py = cx + (R + r) / 2 * math.cos(ang), cy + (R + r) / 2 * math.sin(ang)
        tinta = AZUL if col == AMBAR else BLANCO
        f = fu(84, True); d.text((px - an(d, letra, f) / 2, py - 76), letra, font=f, fill=tinta)
        f = fu(40, True); d.text((px - an(d, nombre, f) / 2, py + 24), nombre, font=f, fill=tinta)
    if centro:
        cen(d, cx - r, cy - 96, 2 * r, centro, 52, AZUL)
        d.line([cx - 130, cy - 24, cx + 130, cy - 24], fill=AMBAR, width=8)
    for i, t in enumerate(lista):
        cen(d, cx - r, cy + 4 + i * 62, 2 * r, t, 46, GRIS, False)


def franjas(d, bloques, im, y=60, alto=330):
    """Niveles apilados. bloques = [(NOMBRE, [cajas], color)]"""
    for nombre, cajas, col in bloques:
        d.rounded_rectangle([50, y, W - 50, y + alto], 18, fill=GRISC)
        d.rounded_rectangle([50, y, 190, y + alto], 18, fill=col)
        d.rectangle([150, y, 190, y + alto], fill=col)
        tx = Image.new("RGB", (alto, 110), col)
        cen(ImageDraw.Draw(tx), 0, 30, alto, nombre, 46, BLANCO)
        im.paste(tx.rotate(90, expand=True), (52, y))
        x, ancho = 240, (W - 300) / len(cajas) - 26
        for c in cajas:
            d.rounded_rectangle([x, y + 55, x + ancho, y + alto - 55], 14, fill=BLANCO)
            cen(d, x, y + alto / 2 - 26, ancho, c, CUE, AZUL, False)
            x += ancho + 26
        y += alto + 30
    return y


def comparativa(d, izquierda, derecha, filas, y=50):
    """Antes / después, sin / con. filas = [([izq...], [der...])]"""
    mid = W / 2
    d.rounded_rectangle([50, y, mid - 20, y + 100], 14, fill=ROJO)
    d.rounded_rectangle([mid + 20, y, W - 50, y + 100], 14, fill=TEAL)
    cen(d, 50, y + 24, mid - 70, izquierda, 52, BLANCO)
    cen(d, mid + 20, y + 24, mid - 70, derecha, 52, BLANCO)
    y += 135
    for a, b in filas:
        alto = 40 + max(len(a), len(b)) * 62
        d.rounded_rectangle([50, y, mid - 20, y + alto], 14, fill=GRISC)
        d.rounded_rectangle([mid + 20, y, W - 50, y + alto], 14, fill=(226, 245, 241))
        for i, t in enumerate(a):
            cen(d, 50, y + 20 + i * 62, mid - 70, t, CUE, GRIS, False)
        for i, t in enumerate(b):
            cen(d, mid + 20, y + 20 + i * 62, mid - 70, t, CUE, AZUL, False)
        y += alto + 22
    return y


def fichas(d, items, y=50, alto=300, cols=2, pie=None):
    """Elementos numerados a clasificar. items = [texto, ...]"""
    ancho = (W - 100 - 40 * (cols - 1)) / cols
    for i, t in enumerate(items):
        x = 50 + (i % cols) * (ancho + 40)
        yy = y + (i // cols) * (alto + 34)
        d.rounded_rectangle([x, yy, x + ancho, yy + alto], 16, fill=GRISC)
        d.rounded_rectangle([x, yy, x + ancho, yy + 12], 16, fill=AZUL2)
        cen(d, x, yy + 40, ancho, str(i + 1), 54, AZUL2)
        cen(d, x, yy + 130, ancho, t, CUE, AZUL, False)
        if pie:
            d.rounded_rectangle([x + ancho / 2 - 110, yy + alto - 84,
                                 x + ancho / 2 + 110, yy + alto - 32], 10, outline=GRIS, width=3)
            cen(d, x, yy + alto - 72, ancho, pie, 40, GRIS, False)
    return y + ((len(items) + cols - 1) // cols) * (alto + 34)


# ── ejemplo mínimo ────────────────────────────────────────────────────────
if __name__ == "__main__":
    DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ejemplo")
    im, d = lienzo(1290)
    filas_letra(d, [("P", "PLANIFICAR", "Definir qué se quiere y cómo", AZUL2),
                    ("H", "HACER", "Ejecutar lo planificado", TEAL),
                    ("V", "VERIFICAR", "Medir si salió como se esperaba", MORADO),
                    ("A", "ACTUAR", "Corregir y volver a planificar", AMBAR)])
    guardar(im, "ejemplo_phva.png", DEST)
    print("\nSi el cuerpo sale por debajo de 14 pt, hay demasiado contenido: quita, no encojas.")
