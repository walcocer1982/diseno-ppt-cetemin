# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 de SI-IMPAMB: aspecto, impacto y control.

POR QUÉ NO PASA POR EL MODELO
    Son esquemas conceptuales —cajas y texto—, no equipos. La regla del §10
    (nunca texto→imagen) aplica a EQUIPOS: ahí el modelo inventaría geometría.
    Un esquema se dibuja, sale idéntico cada vez y se corrige en una línea.

QUÉ DIBUJA
    Las nueve figuras de las láminas de tema de la S1:
      s1_entra-sale                 PK1 · láminas 11
      s1_como-se-nombra             PK1 · lámina 12
      s1_hay-aspecto                PK1 · lámina 13
      s1_actividad-aspecto-impacto  PK2 · lámina 14
      s1_dentro-fuera               PK2 · lámina 15
      s1_confundirlos               PK2 · lámina 16
      s1_sobre-que-actua            PK3 · lámina 17
      s1_faja-o-via                 PK3 · lámina 18
      s1_parece-control             PK3 · lámina 19

    El ejemplo de las tres primeras es neutro —el lavado de un equipo— a
    propósito: si el esquema usara la planta de concreto o el taller de
    estructuras, estaría resolviendo el caso antes de que el equipo lo lea.

Uso:  python gen_esquemas_impamb_s1.py
"""
from __future__ import annotations

import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      fichas, cen, izq, AVISOS)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ── PK1 · el aspecto es lo que sale de la actividad ────────────────────────
def entra_sale():
    """Las dos caras de una misma actividad. Ejemplo neutro: lavar un equipo."""
    im, d = lienzo(1080)
    y = comparativa(d, "LO QUE ENTRA", "LO QUE SALE", [
        (["Agua"], ["Equipo limpio"]),
        (["Detergente"], ["Agua con grasa y sólidos"]),
        (["Energía eléctrica"], ["Envase vacío del detergente"]),
    ], y=50)
    banda(d, y + 20, 140, "El aspecto está en las dos columnas: lo que se consume y lo que se genera",
          px=CUE)
    return guardar(im, "s1_entra-sale.png", DEST)


def como_se_nombra():
    """El aspecto se nombra con un sustantivo de acción, no con la cosa."""
    im, d = lienzo(1180)
    y = franjas(d, [
        ("ASÍ SE NOMBRA", ["Generación de residuo peligroso",
                           "Consumo de agua",
                           "Emisión de material particulado"], TEAL),
        ("ASÍ NO", ["Aceite usado", "El caño abierto", "Polvo"], ROJO),
    ], im, y=60, alto=330)
    banda(d, y + 20, 140, "Un sustantivo de acción, no la cosa ni la escena", px=CUE)
    return guardar(im, "s1_como-se-nombra.png", DEST)


def hay_aspecto():
    """Cuatro actividades para decidir si generan aspecto o no."""
    im, d = lienzo(1080)
    y = fichas(d, [
        "Cambiar el aceite de un motor",
        "Revisar un tablero eléctrico sin desmontarlo",
        "Lavar una tolva con agua a presión",
        "Firmar el parte de la guardia",
    ], y=50, alto=300, cols=2, pie="¿hay aspecto?")
    banda(d, y + 20, 140, "Si no entra ni sale nada, no hay aspecto que registrar", px=CUE)
    return guardar(im, "s1_hay-aspecto.png", DEST)


# ── PK2 · el impacto es el cambio que el aspecto produce ───────────────────
def actividad_aspecto_impacto():
    """La cadena de causa y efecto, en tres niveles."""
    im, d = lienzo(1280)
    y = franjas(d, [
        ("LA ACTIVIDAD", ["Lavar el equipo", "Es lo que se hace"], GRIS),
        ("EL ASPECTO", ["Generación de efluente", "Es lo que sale"], AZUL2),
        ("EL IMPACTO", ["Alteración de la calidad del agua", "Es el cambio que produce"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 140, "Uno causa al otro: sin aspecto no hay impacto", px=CUE)
    return guardar(im, "s1_actividad-aspecto-impacto.png", DEST)


def dentro_fuera():
    """Dónde ocurre cada uno, y por qué eso decide sobre cuál se puede actuar."""
    im, d = lienzo(1080)
    y = comparativa(d, "DENTRO DE LA OPERACIÓN", "FUERA DE ELLA", [
        (["Ocurre el aspecto"], ["Ocurre el impacto"]),
        (["La empresa manda aquí"], ["La empresa ya no manda"]),
        (["Se puede intervenir"], ["Solo queda reparar"]),
    ], y=50)
    banda(d, y + 20, 140, "Por eso el control se pone dentro, no fuera", px=CUE)
    return guardar(im, "s1_dentro-fuera.png", DEST)


def confundirlos():
    """Qué cambia en la matriz según se distingan o no."""
    im, d = lienzo(1080)
    y = comparativa(d, "SI SE CONFUNDEN", "SI SE DISTINGUEN", [
        (["Se registra el daño como si fuera la causa"], ["Se registra la causa y su efecto"]),
        (["El control se pone donde ya pasó"], ["El control se pone donde se origina"]),
        (["El aspecto sigue generando"], ["El aspecto se reduce"]),
    ], y=50)
    banda(d, y + 20, 140, "Confundirlos pone el control en el lugar equivocado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_confundirlos.png", DEST)


# ── PK3 · el control actúa sobre el aspecto ────────────────────────────────
def sobre_que_actua():
    """Las dos cosas que se llaman control y no son lo mismo."""
    im, d = lienzo(1180)
    y = franjas(d, [
        ("CONTROL DE ORIGEN", ["Actúa sobre el aspecto",
                               "Antes de que el cambio ocurra",
                               "Reduce lo que sale"], AZUL2),
        ("MITIGACIÓN", ["Actúa sobre el impacto",
                        "Después de que el cambio ocurrió",
                        "No reduce lo que sale"], GRIS),
    ], im, y=60, alto=340)
    banda(d, y + 20, 140, "Las dos hacen falta; solo una es control del aspecto", px=CUE)
    return guardar(im, "s1_sobre-que-actua.png", DEST)


def faja_o_via():
    """El mismo polvo, dos intervenciones distintas."""
    im, d = lienzo(1080)
    y = comparativa(d, "CUBRIR LA FAJA", "REGAR LA VÍA", [
        (["Sobre el aspecto"], ["Sobre el impacto"]),
        (["Ya no se levanta polvo"], ["El polvo se levanta igual"]),
        (["Deja de generarse"], ["Se asienta lo que ya salió"]),
    ], y=50)
    banda(d, y + 20, 140, "Regar es necesario y no sustituye a cubrir", px=CUE)
    return guardar(im, "s1_faja-o-via.png", DEST)


def parece_control():
    """Cuatro medidas para decidir sobre cuál de los dos actúa cada una."""
    im, d = lienzo(1080)
    y = fichas(d, [
        "Poner una malla contra el viento en el cerco",
        "Cambiar el detergente por uno biodegradable",
        "Sembrar árboles en el límite del terreno",
        "Cerrar la tolva de carga",
    ], y=50, alto=300, cols=2, pie="¿sobre cuál actúa?")
    banda(d, y + 20, 140, "Un control vistoso puede dar un aspecto por resuelto sin tocarlo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_parece-control.png", DEST)


FIGURAS = [entra_sale, como_se_nombra, hay_aspecto,
           actividad_aspecto_impacto, dentro_fuera, confundirlos,
           sobre_que_actua, faja_o_via, parece_control]

if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    print("Esquemas de SI-IMPAMB · S1")
    print("   destino: %s" % DEST)
    for fn in FIGURAS:
        print("   %s" % os.path.basename(str(fn())))
    if AVISOS:
        print("\nAVISOS — texto que no cupo en su caja:")
        for a in AVISOS:
            print("   !! %s" % a)
    else:
        print("\nSin avisos: todo el texto cupo en su caja.")
