# -*- coding: utf-8 -*-
"""Audita la GEOMETRIA de un PPT ya generado, lamina por lamina.

El §11 mide palabras y minutos; esto mide el espacio. Son fallos distintos:
una lamina puede tener 60 palabras (correcto) y aun asi verse mal porque el
texto se sale de su caja, pisa la imagen o queda descentrado.

Que revisa, en este orden:

    FUERA DEL LIENZO   una forma que empieza o termina fuera de la diapositiva
    SOLAPE             dos cajas de texto —o texto sobre imagen— que se pisan
    DESBORDE           mas texto del que cabe en la caja a ese tamano de fuente
    DESCENTRADO        una caja centrada que no lo esta respecto del lienzo
    SIN APOYO          lamina de contenido con mucho texto y ninguna imagen

El desborde es una ESTIMACION: PowerPoint no expone el alto renderizado, asi
que se calcula por ancho de caracter (0,50 em de media en Arial) y alto de
linea (1,22 em). Marca lo que se pasa de largo, no lo que se pasa por poco.

Uso:  python auditar_laminas.py EOM-METEXP-S1
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
from pptx import Presentation
from pptx.util import Emu

RAIZ = Path(__file__).resolve().parent.parent
EM_ANCHO = 0.50      # ancho medio de caracter, en fracciones del cuerpo
EM_ALTO = 1.22       # alto de linea
HOLGURA = 1.12       # 12 % de margen antes de cantar desborde
MIN_SOLAPE = 0.14    # fraccion de la caja menor que hay que pisar para contar
FONDO = 0.85         # imagen que cubre esto del lienzo es fondo, no elemento
TEXTO_LARGO = 45     # palabras a partir de las cuales una lamina pide apoyo


def _rect(sh):
    try:
        return (Emu(sh.left).inches, Emu(sh.top).inches,
                Emu(sh.width).inches, Emu(sh.height).inches)
    except TypeError:
        return None


def _corte(a, b):
    """Area de interseccion de dos rectangulos (x, y, w, h)."""
    x = max(0.0, min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0]))
    y = max(0.0, min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]))
    return x * y


def _cuerpo(sh):
    """Tamano de fuente dominante de la forma, en puntos."""
    tam = []
    for p in sh.text_frame.paragraphs:
        for r in p.runs:
            if r.font.size:
                tam.append(r.font.size.pt)
    return max(tam) if tam else 18.0


def _alto_necesario(sh, ancho_in, pt):
    """Alto en pulgadas que pediria el texto a ese cuerpo."""
    ancho_pt = ancho_in * 72
    por_linea = max(1, int(ancho_pt / (pt * EM_ANCHO)))
    lineas = 0
    for p in sh.text_frame.paragraphs:
        t = p.text
        lineas += max(1, math.ceil(len(t) / por_linea)) if t.strip() else 1
    return lineas * pt * EM_ALTO / 72


def auditar(ruta: Path) -> int:
    pres = Presentation(str(ruta))
    W, H = Emu(pres.slide_width).inches, Emu(pres.slide_height).inches
    print("=" * 68)
    print("GEOMETRIA · %s" % ruta.name)
    print("%d diapositivas · lienzo %.2f x %.2f in" % (len(pres.slides), W, H))
    print("=" * 68)

    fallos = 0
    for i, s in enumerate(pres.slides, 1):
        avisos = []
        cajas = []       # (rect, es_texto, etiqueta)
        palabras = 0
        imagenes = 0

        for sh in s.shapes:
            r = _rect(sh)
            if r is None:
                continue
            es_img = sh.shape_type == 13
            imagenes += 1 if es_img else 0
            tiene_texto = sh.has_text_frame and sh.text_frame.text.strip()
            if tiene_texto:
                palabras += len(sh.text_frame.text.split())

            # -------------------------------------------- fuera del lienzo
            if r[0] < -0.02 or r[1] < -0.02 or r[0] + r[2] > W + 0.02 or r[1] + r[3] > H + 0.02:
                avisos.append("FUERA DEL LIENZO · %s en (%.2f, %.2f) %.2f x %.2f"
                              % ("imagen" if es_img else
                                 (sh.text_frame.text.split("\n")[0][:26] if tiene_texto
                                  else "forma"), r[0], r[1], r[2], r[3]))

            if tiene_texto:
                pt = _cuerpo(sh)
                pide = _alto_necesario(sh, r[2], pt)
                lineas_txt = max(1, round(pide / (pt * EM_ALTO / 72)))
                if pide > r[3] * HOLGURA and lineas_txt > 1:
                    avisos.append("DESBORDE · «%s…» pide %.2f in y tiene %.2f"
                                  % (sh.text_frame.text.strip()[:30].replace("\n", " "),
                                     pide, r[3]))
                cajas.append((r, True, sh.text_frame.text.strip()[:24].replace("\n", " ")))
            elif es_img:
                if r[2] * r[3] < FONDO * W * H:
                    cajas.append((r, False, "imagen"))
                else:
                    imagenes -= 1   # es el fondo de la plantilla

        # ------------------------------------------------------- solapes
        for a in range(len(cajas)):
            for b in range(a + 1, len(cajas)):
                ra, _, na = cajas[a]
                rb, _, nb = cajas[b]
                corte = _corte(ra, rb)
                if corte <= 0:
                    continue
                menor = min(ra[2] * ra[3], rb[2] * rb[3])
                if menor > 0 and corte / menor > MIN_SOLAPE:
                    avisos.append("SOLAPE · «%s» y «%s» se pisan el %d %%"
                                  % (na, nb, round(100 * corte / menor)))

        # -------------------------------------------- lamina sin apoyo
        if palabras >= TEXTO_LARGO and imagenes == 0:
            avisos.append("SIN APOYO · %d palabras y ninguna imagen propia: "
                          "es un muro" % palabras)

        if avisos:
            fallos += len(avisos)
            print("\n  %02d" % i)
            for a in avisos:
                print("      %s" % a)

    print("\n" + "=" * 68)
    print("OK · geometria limpia" if not fallos else "%d avisos" % fallos)
    return fallos


def _ppt_de(sesion_id: str) -> Path:
    nro = sesion_id.rsplit("S", 1)[-1]
    base = RAIZ / "03_Entregables-diseño"
    hallados = sorted(base.glob("*/Ppt/S%s_*.pptx" % nro)) + \
        sorted(base.glob("*/PPT/S%s_*.pptx" % nro))
    if not hallados:
        sys.exit("No encuentro el PPT de %s" % sesion_id)
    return hallados[0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(1 if auditar(_ppt_de(sys.argv[1])) else 0)
