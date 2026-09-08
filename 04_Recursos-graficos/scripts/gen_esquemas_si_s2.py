# -*- coding: utf-8 -*-
"""Esquemas de la sesión 2 de SI-SGCSSMA · contexto de la organización y partes interesadas.

POR QUÉ NO PASA POR EL MODELO
    Son esquemas conceptuales —cajas y texto—, no equipos. La regla del §10
    (nunca texto→imagen) aplica a EQUIPOS.

QUÉ DIBUJA
    Se reciclan de la versión anterior, sin tocar: contexto_que-es, contexto_externo,
    contexto_interno, partes-interesadas_quienes y partes-interesadas_que-espera.
    Aquí van las nueve que faltaban.

Uso:  python gen_esquemas_si_s2.py
"""
from __future__ import annotations

import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      caso, cen, izq)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def contexto_revision():
    """Cada cuánto se revisa el contexto y qué constancia queda."""
    im, d = lienzo(1150)
    y = franjas(d, [
        ("CUÁNDO", ["Antes de planificar nada", "Y otra vez cuando algo cambia"], AZUL2),
        ("CONSTANCIA", ["No hay formato obligatorio", "Pero tiene que quedar escrito"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Es la misma exigencia en la ISO 9001, la ISO 14001 y la ISO 45001", px=CUE)
    return guardar(im, "s2_contexto-revision.png", DEST)


def partes_olvidadas():
    """Las partes interesadas que se suelen dejar fuera."""
    im, d = lienzo(1180)
    y = franjas(d, [
        ("SE ANOTAN", ["El cliente", "La autoridad"], AZUL2),
        ("SE OLVIDAN", ["Los trabajadores", "Los contratistas", "Los vecinos"], ROJO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "La ISO 45001 nombra a los trabajadores expresamente", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    banda(d, y + 180, 120, "Se identifican por su relación con la empresa, no por su tamaño", px=NOTA)
    return guardar(im, "s2_partes-olvidadas.png", DEST)


def expectativa_requisito():
    """Cuando una expectativa se vuelve requisito del sistema."""
    im, d = lienzo(1000)
    y = comparativa(d, "EXPECTATIVA", "REQUISITO", [
        (["Lo que la parte espera"], ["Lo que la empresa adopta"]),
        (["No obliga por sí sola"], ["Hay que cumplirlo y demostrarlo"]),
        (["La empresa decide cuáles toma"], ["Entra al sistema de gestión"]),
    ], y=50)
    banda(d, y + 20, 140, "No toda expectativa es un requisito", px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s2_expectativa-requisito.png", DEST)


def encargo():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("PASO 1", ["Clasificar cada hecho", "Externa, interna o ninguna"], AZUL2),
        ("PASO 2", ["Qué espera cada parte interesada", "Y si eso es requisito del sistema"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Y a quién dejó fuera la hoja de gerencia", px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s2_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(1780)
    y = caso(d, "CASO A", "Mantenimiento de Equipos Mineros S.A.C.  ·  54 trabajadores  ·  entra a una unidad nueva",
        ["H1 · La unidad está a 4 100 m s. n. m. Ningún mecánico ha trabajado antes en altura",
         "H2 · El cliente exige avanzar hacia la certificación de calidad el año que viene",
         "H3 · De los 54 trabajadores, 31 entraron en los últimos seis meses",
         "H4 · El taller propio está a 300 metros de una zona de viviendas",
         "H5 · Dos de los cinco tornos tienen más de veinte años y paran una vez por semana",
         "H6 · La comunidad campesina tiene un convenio firmado con la unidad minera",
         "H7 · Gerencia escribió: «nuestro contexto es el cliente y la autoridad»",
         "H8 · En la relación de partes interesadas no aparecen los trabajadores"],
        color=AZUL2, y=50, alto=190)
    banda(d, y + 24, 140, "El cliente pide el contexto y las partes interesadas antes del ingreso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s2_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(1780)
    y = caso(d, "CASO B", "Transporte de Concentrado del Centro S.A.C.  ·  22 conductores  ·  renueva contrato",
        ["H1 · La ruta cruza dos centros poblados y un puente con límite de 30 toneladas",
         "H2 · La temporada de lluvias corta el acceso entre enero y marzo",
         "H3 · De los 22 conductores, 14 son de la zona y ocho vienen de la costa",
         "H4 · La aseguradora exige el registro de horas de conducción de cada chofer",
         "H5 · El cliente pide reporte diario de toneladas movidas y de incidentes",
         "H6 · Tres volquetes son alquilados a un tercero, que hace su propio mantenimiento",
         "H7 · Gerencia escribió: «nuestro contexto es la ruta y el clima»",
         "H8 · En la relación de partes interesadas no aparecen los centros poblados"],
        color=TEAL, y=50, alto=190)
    banda(d, y + 24, 140, "El cliente pide el contexto y las partes interesadas antes de firmar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s2_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("ENTREGAN", ["El cuadro de los ocho hechos", "Externa, interna o ninguna"], AZUL2),
        ("Y ADEMÁS", ["Cada parte interesada y qué espera", "Las que la hoja dejó fuera"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s2_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Esta parte interesada quedó fuera"], AZUL2),
        ("APOYO", ["Y lo sostenemos en este hecho"], TEAL),
        ("PREGUNTA", ["¿Qué se le escapa a la empresa por no tenerla?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 140, "Dos minutos por equipo. Empezamos por las partes olvidadas",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s2_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1200)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que el contexto de una empresa era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué parte interesada de tu trabajo nadie tiene anotada?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s2_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 2")
    for fn in (contexto_revision, partes_olvidadas, expectativa_requisito, encargo,
               ficha_caso_a, ficha_caso_b, a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
