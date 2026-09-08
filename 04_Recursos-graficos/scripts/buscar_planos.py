# -*- coding: utf-8 -*-
"""Encuentra los PLANOS dentro de un PDF (tesis, informe, catalogo).

EL PROBLEMA
    Una tesis trae decenas de figuras: fotos de campo, organigramas, graficos
    estadisticos, tablas capturadas como imagen... y entre todas, uno o dos
    PLANOS. Revisarlas a ojo una por una no escala, y es donde se cuela una
    figura que no sirve.

COMO SE RECONOCE UN PLANO (medible, no opinable)
    Un dibujo tecnico tiene una firma distinta a la de una foto o un esquema:

    1. FONDO BLANCO dominante        - el plano se dibuja sobre papel
    2. TINTA ESCASA y FINA           - son lineas, no areas rellenas
    3. MUCHAS RECTAS LARGAS          - niveles, grillas, ejes, cotas
    4. POCOS COLORES PLANOS          - sin degradados
    5. GRADIENTES DUROS              - borde de linea, no transicion suave

    Una FOTO falla 1, 2, 4 y 5 (poco blanco, muchos colores, gradientes suaves).
    Un ORGANIGRAMA cumple 1 y 4 pero falla 3 (cajas, no rectas largas continuas).
    Una TABLA cumple 1 y 3 pero su tinta es casi toda texto: falla el balance.

Uso:  python buscar_planos.py <archivo.pdf> [carpeta_salida]
"""
from __future__ import annotations

import sys
from pathlib import Path

import fitz
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

MIN_PX = 300            # ignorar figuras diminutas
UMBRAL_BLANCO = 238     # por encima de esto se considera papel


def metricas(img: Image.Image) -> dict:
    a = np.array(img.convert("RGB")).astype(int)
    if min(a.shape[:2]) < 40:
        return {}
    lum = a.mean(2)
    sat = a.max(2) - a.min(2)
    papel = lum > UMBRAL_BLANCO
    tinta = ~papel

    # 1. cuanto papel hay
    blanco = float(papel.mean())

    # 2. cuanta tinta, y si es fina (lineas) o maciza (areas)
    densidad = float(tinta.mean())
    erosion = ndi.binary_erosion(tinta, np.ones((3, 3)))
    finura = 1.0 - (erosion.sum() / max(tinta.sum(), 1))   # 1 = todo son lineas finas

    # 3. rectas largas: filas/columnas donde la tinta se alinea de lado a lado
    h, w = tinta.shape
    filas = tinta.sum(1) / w
    cols = tinta.sum(0) / h
    rectas = float((filas > 0.55).sum() + (cols > 0.55).sum())

    # 4. variedad de color (cuantizada): una foto tiene muchisimos tonos
    q = (a // 32).astype(np.uint8)
    n_colores = len(np.unique(q.reshape(-1, 3), axis=0))
    sat_media = float(sat[tinta].mean()) if tinta.any() else 0.0

    # 5. gradientes: duros en un dibujo, suaves en una foto
    gx = ndi.sobel(lum, 0); gy = ndi.sobel(lum, 1)
    g = np.hypot(gx, gy)
    suaves = float(((g > 8) & (g < 60)).mean())          # transiciones intermedias
    duros = float((g >= 60).mean())

    # 6. DIAGONALES — la senal que separa un PLANO de una TABLA.
    #    Una tabla tambien tiene fondo blanco, trazo fino y muchas rectas
    #    largas: cumple toda la firma anterior (probado: 8 falsos positivos de
    #    15 en una tesis real). Lo que NO tiene son lineas en angulos
    #    arbitrarios. Un plano si: taludes, vetas, secciones, cotas inclinadas.
    borde = g > 40
    if borde.sum() > 50:
        ang = np.degrees(np.arctan2(gy[borde], gx[borde])) % 180
        cerca_hv = ((ang < 12) | (ang > 168) | ((ang > 78) & (ang < 102)))
        diagonales = float(1.0 - cerca_hv.mean())
    else:
        diagonales = 0.0

    # 7. CUANTA DE LA TINTA ES TEXTO — la senal decisiva.
    #    Las diagonales solas no bastan: las CURVAS DE LAS LETRAS tambien son
    #    diagonales, asi que una tabla con mucho texto pasaba igual el filtro.
    #    Un caracter es un componente conexo chico y de proporcion contenida;
    #    una linea de plano es un componente largo y delgado que cruza la figura.
    lb, n = ndi.label(tinta)
    texto_px = 0
    if 0 < n < 4000:
        objetos = ndi.find_objects(lb)
        for sl in objetos:
            alto = sl[0].stop - sl[0].start
            ancho = sl[1].stop - sl[1].start
            if 4 <= alto <= 40 and 3 <= ancho <= 40 and max(alto, ancho) / max(min(alto, ancho), 1) < 4:
                texto_px += alto * ancho
    texto = float(texto_px / max(tinta.sum(), 1))

    # 8. OSCILACION — caza los REPORTES DE INSTRUMENTACION (sismografo,
    #    vibracion). Una senal registrada cruza el papel decenas de veces por
    #    fila; una linea de plano, dos o tres. Se mide contando transiciones
    #    papel->tinta a lo largo de cada fila.
    cambios = np.diff(tinta.astype(np.int8), axis=1) != 0
    oscilacion = float(cambios.sum(1).mean())

    # 9. SUB-FOTOS — caza las laminas MIXTAS (foto + tabla + texto), que no son
    #    un plano aunque el conjunto tenga fondo blanco. Se busca en ventanas:
    #    si alguna zona es densa y de gradiente suave, ahi hay una fotografia.
    k = max(min(h, w) // 6, 16)
    dens_local = ndi.uniform_filter(tinta.astype(float), k)
    suave_local = ndi.uniform_filter(((g > 4) & (g < 45)).astype(float), k)
    subfoto = float(((dens_local > 0.80) & (suave_local > 0.30)).mean())

    # 10. FRANJAS VACIAS — caza los reportes partidos en PANELES apilados
    #     (Instantel y similares): entre panel y panel hay bandas de papel que
    #     cruzan la figura entera. Un plano es un dibujo continuo: su contenido
    #     no deja franjas limpias de lado a lado.
    ocupadas = np.where(filas > 0.005)[0]
    if len(ocupadas) > 10:
        interior = filas[ocupadas.min():ocupadas.max() + 1]
        franjas = float((interior < 0.004).mean())
    else:
        franjas = 0.0

    return dict(franjas=franjas,
                blanco=blanco, densidad=densidad, finura=finura, rectas=rectas,
                n_colores=n_colores, sat_media=sat_media, suaves=suaves,
                duros=duros, diagonales=diagonales, texto=texto,
                oscilacion=oscilacion, subfoto=subfoto)


def clasificar(m: dict) -> tuple[str, float, list[str]]:
    """Devuelve (tipo, confianza 0-1, razones)."""
    if not m:
        return "descartada", 0.0, ["demasiado pequena"]

    razones = []
    puntos = 0.0

    # --- descartes duros ---
    if m["blanco"] < 0.35:
        return "foto", 0.9, [f"solo {m['blanco']:.0%} de fondo claro"]
    if m["n_colores"] > 900 and m["suaves"] > 0.25:
        return "foto", 0.85, [f"{m['n_colores']} tonos y gradientes suaves"]

    # NOTA — hipotesis DESCARTADA: se probo detectar los reportes de
    # instrumentacion por "cruces de tinta por fila", suponiendo que una senal
    # registrada oscila mas que un dibujo. Medido, resulto al reves: el plano de
    # la Mina Chupa da 81 cruces/fila y los reportes de vibracion 16-38. La
    # metrica queda calculada por si sirve para otra cosa, pero NO se usa para
    # clasificar. (Se conserva escrito para no volver a intentarlo.)

    # --- documento en paneles: reporte de instrumentacion, no un plano ---
    if m["franjas"] > 0.16:
        return ("reporte en paneles", 0.85,
                [f"{m['franjas']:.0%} del alto son franjas vacias: esta partido en paneles"])

    # --- lamina mixta: lleva fotografias incrustadas ---
    if m["subfoto"] > 0.05:
        return ("lamina mixta", 0.8,
                [f"{m['subfoto']:.0%} del area son fotografias incrustadas"])

    # --- tabla o reporte: la mayor parte de la tinta son caracteres ---
    if m["texto"] > 0.55:
        return ("tabla/texto", 0.85,
                [f"{m['texto']:.0%} de la tinta son caracteres: es texto, no un dibujo"])

    # --- tabla o reporte: casi todo el trazo es horizontal/vertical ---
    if m["diagonales"] < 0.30:
        return ("tabla/grafico", 0.85,
                [f"solo {m['diagonales']:.0%} de trazo diagonal: es una grilla, no un dibujo"])

    # --- firma de plano ---
    if m["blanco"] > 0.55:
        puntos += 0.20; razones.append(f"fondo blanco {m['blanco']:.0%}")
    if m["densidad"] < 0.30:
        puntos += 0.15; razones.append(f"tinta escasa {m['densidad']:.0%}")
    if m["finura"] > 0.45:
        puntos += 0.15; razones.append(f"trazo fino {m['finura']:.0%}")
    if m["rectas"] >= 3:
        puntos += 0.15; razones.append(f"{int(m['rectas'])} rectas largas")
    if m["duros"] > m["suaves"]:
        puntos += 0.10; razones.append("bordes duros")
    if m["diagonales"] > 0.42:
        puntos += 0.25; razones.append(f"{m['diagonales']:.0%} de trazo diagonal")

    if puntos >= 0.70:
        return "plano", puntos, razones
    if m["rectas"] < 3 and m["blanco"] > 0.6 and m["densidad"] < 0.25:
        return "esquema/organigrama", puntos, razones + ["sin rectas largas"]
    return "otra figura", puntos, razones


def revisar(pdf: Path, salida: Path) -> list[dict]:
    doc = fitz.open(pdf)
    salida.mkdir(parents=True, exist_ok=True)
    hallazgos = []

    for i, pagina in enumerate(doc):
        for j, info in enumerate(pagina.get_images(full=True)):
            xref = info[0]
            try:
                pm = fitz.Pixmap(doc, xref)
                if pm.n > 4:
                    pm = fitz.Pixmap(fitz.csRGB, pm)
                if pm.width < MIN_PX or pm.height < MIN_PX:
                    continue
                img = Image.frombytes("RGB" if pm.n >= 3 else "L",
                                      (pm.width, pm.height), pm.samples).convert("RGB")
            except Exception:
                continue

            m = metricas(img)
            tipo, conf, razones = clasificar(m)
            reg = dict(pagina=i, tipo=tipo, confianza=round(conf, 2),
                       tam=f"{pm.width}x{pm.height}", razones=razones)
            if tipo == "plano":
                f = salida / f"p{i:03d}_plano.png"
                img.save(f)
                reg["archivo"] = str(f)
            hallazgos.append(reg)
    return hallazgos


if __name__ == "__main__":
    pdf = Path(sys.argv[1])
    salida = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf.parent / "_planos_detectados"
    res = revisar(pdf, salida)

    planos = [r for r in res if r["tipo"] == "plano"]
    print(f"\n{pdf.name}: {len(res)} figuras revisadas\n")
    for r in sorted(res, key=lambda x: -x["confianza"]):
        marca = ">>" if r["tipo"] == "plano" else "  "
        print(f"{marca} p{r['pagina']:<4} {r['tipo']:<20} {r['confianza']:.2f}  "
              f"{r['tam']:<12} {'; '.join(r['razones'])[:70]}")
    print(f"\nPLANOS DETECTADOS: {len(planos)}  -> {salida}")
    print("Revisa cada uno: el numero dice que TIENE FORMA de plano, no que sea el que buscas.")
