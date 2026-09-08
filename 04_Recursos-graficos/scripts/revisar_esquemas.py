# -*- coding: utf-8 -*-
"""Comprueba que ningún esquema se salga de su lienzo, y que se lea al proyectar.

POR QUÉ EXISTE
    Erick vio esquemas «entrecortados»: rótulos partidos por el borde. El
    generador no avisa —matplotlib recorta en silencio lo que cae fuera de los
    límites— y a tamaño completo no se nota. Es el mismo patrón del §11: lo que
    no se mide, no se ve.

QUÉ MIDE, Y NO OPINA
    1 · DESBORDE — tinta pegada a cualquiera de los cuatro bordes. Si la hay,
        algo quedó cortado. Se ignoran los esquemas que llevan un marco a
        propósito: se detecta que el borde está lleno de lado a lado.
    2 · LEGIBILIDAD — altura de palabra pasada a pt proyectados (§11):
            pt = 6 × px_alto ÷ px_ancho × 72
        Se miden DOS cosas, porque el estándar tiene dos tamaños: el CUERPO
        (52 px → 15 pt, piso 14) y la NOTA al pie (42 px → 12,1 pt, piso 11).
        La primera versión de este revisor tomaba la MEDIANA de todas las
        palabras y daba por malos los 64 esquemas: la mediana caía entre el
        cuerpo y la nota. Medir dos poblaciones distintas con un solo número es
        el error 19 del §10, otra vez.

        Y una segunda vez en el mismo apartado: la fórmula del §11 usa el
        TAMAÑO DE FUENTE, y lo que se puede medir en un PNG es la ALTURA DE
        TINTA. No son lo mismo: una mayúscula ocupa ~0,72 del cuerpo, así que
        un texto de 52 px deja 38 px de tinta. Comparar los 38 contra el piso
        de 14 pt daba por ilegibles los 60 esquemas que están bien. Se divide
        por CAJA_ALTA antes de comparar.
    3 · ANCHO — el §11 fija 1500 px. Otro ancho cambia la razón fuente/lienzo,
        que es lo que decide si se lee.

Uso:  python revisar_esquemas.py                 (todos los de EOM)
      python revisar_esquemas.py EOM/esquemas/s2 (una carpeta)
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

RAIZ = Path(__file__).resolve().parents[1]
MARGEN = 4          # px desde el borde que se consideran "pegados"
PT_CUERPO = 14.0    # §11: por debajo, sobra contenido
PT_NOTA = 11.0      # la nota al pie va a 42 px = 12,1 pt; 11 es el suelo
CAJA_ALTA = 0.72   # altura de mayúscula sobre el cuerpo de la fuente
ANCHO = 1500
TOLERA_ANCHO = 60   # 1536 del modelo entra: 6*52/1536*72 = 14,6 pt


def _tinta(a):
    return a.mean(2) < 235 if a.ndim == 3 else a < 235


def desborde(png: Path):
    """Tinta pegada a un borde. Un marco intencionado llena el borde de lado a
    lado; un rótulo cortado solo toca un tramo. Esa es la diferencia que se usa
    para no dar por malo lo que está bien."""
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    t = _tinta(a)
    h, w = t.shape
    bordes = {"arriba": t[:MARGEN, :].any(0), "abajo": t[-MARGEN:, :].any(0),
              "izquierda": t[:, :MARGEN].any(1), "derecha": t[:, -MARGEN:].any(1)}
    fallas = []
    for nombre, linea in bordes.items():
        cubre = linea.mean()
        if 0 < cubre < 0.90:          # toca, pero no es un marco completo
            fallas.append("%s (%.0f %% del borde)" % (nombre, cubre * 100))
    return fallas


def legible(png: Path):
    """Altura de PALABRA en pt proyectados. Se miden palabras y no glifos
    sueltos: el punto de «2.90» mide 8 px aunque los dígitos midan 35."""
    a = np.array(Image.open(png).convert("RGB")).astype(int)
    W = a.shape[1]
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    tinta = ((R > 130) & (G < 120) & (B < 120)) | (a.mean(2) < 130)
    lb, _ = ndi.label(ndi.binary_dilation(tinta, np.ones((3, 15))), np.ones((3, 3)))
    altos = sorted(h for sl in ndi.find_objects(lb)
                   for h, w in [(sl[0].stop - sl[0].start, sl[1].stop - sl[1].start)]
                   if 12 <= h <= 130 and 0.4 <= w / h <= 14)
    if not altos:
        return None
    def a_pt(tinta_px):
        return 6 * (tinta_px / CAJA_ALTA) / W * 72
    # Se toma el PERCENTIL 90, no la mediana ni el minimo. Razon: la altura de
    # tinta de una palabra depende de si lleva mayusculas y de si tiene
    # ascendentes o descendentes —«nueve» ocupa la mitad que «BUZAMIENTO» con el
    # mismo cuerpo—. Solo las palabras altas informan del tamano real de la
    # fuente; las bajas no dicen nada. Medir la poblacion equivocada es el error
    # 19 del §10, y en este archivo ya cayo dos veces.
    cuerpo = altos[min(int(len(altos) * 0.90), len(altos) - 1)]
    minimo = altos[max(int(len(altos) * 0.25), 0)]
    return dict(cuerpo=cuerpo, pt_cuerpo=a_pt(cuerpo),
                minimo=minimo, pt_min=a_pt(minimo))


def revisar(carpeta: Path):
    # los paneles son piezas intermedias: no se proyectan, se montan
    pngs = sorted(p for p in carpeta.rglob("*.png")
                  if not p.name.startswith("_") and "_paneles" not in p.parts)
    malos = 0
    for p in pngs:
        im = Image.open(p)
        avisos = []
        d = desborde(p)
        if d:
            avisos.append("SE SALE: " + ", ".join(d))
        if abs(im.width - ANCHO) > TOLERA_ANCHO:
            avisos.append("ancho %d px (el §11 fija %d)" % (im.width, ANCHO))
        g = legible(p)
        if g is None:
            avisos.append("sin texto que medir")
        else:
            if g["pt_cuerpo"] < PT_CUERPO:
                avisos.append("cuerpo %d px = %.1f pt (piso %.0f)"
                              % (g["cuerpo"], g["pt_cuerpo"], PT_CUERPO))
            # informativo: la letra menuda de un esquema puede ser una nota al
            # pie legitima. Solo se avisa si baja de forma llamativa.
            if g["pt_min"] < PT_NOTA * 0.72:
                avisos.append("hay letra de %d px = %.1f pt" % (g["minimo"], g["pt_min"]))
        if avisos:
            malos += 1
            print("  %-46s %s" % (p.relative_to(RAIZ), " | ".join(avisos)))
    print("\n%d esquemas revisados · %d con avisos" % (len(pngs), malos))
    return malos


if __name__ == "__main__":
    sub = sys.argv[1] if len(sys.argv) > 1 else "EOM/esquemas"
    print("REVISIÓN DE ESQUEMAS · %s\n" % sub)
    sys.exit(1 if revisar(RAIZ / sub) else 0)
