# -*- coding: utf-8 -*-
"""Esquemas de la sesión 3 de SI-SGCSSMA · alcance del sistema y enfoque a procesos.

POR QUÉ NO PASA POR EL MODELO
    Son esquemas conceptuales —cajas y texto—, no equipos. La regla del §10
    (nunca texto→imagen) aplica a EQUIPOS.

QUÉ SE RECICLA SIN TOCAR
    proceso_entrada-salida  ·  mapa-de-procesos_contratista  ·  ruta-de-aprendizaje_s3

Uso:  python gen_esquemas_si_s3.py
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


def puente():
    """Lo que quedó de la sesión 2 y por qué lleva al alcance."""
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Quién es parte interesada", "Y qué espera de la empresa"], AZUL2),
        ("HOY", ["Hasta dónde llega el sistema", "Y qué actividades cubre"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Una parte interesada puede esperar algo de una actividad que el sistema no cubre",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_puente.png", DEST)


def estimulo():
    """Estimulo de Veo-Pienso-Me pregunto. Solo hechos, ningun juicio."""
    im, d = lienzo(1000)
    y = comparativa(d, "LO QUE DICE EL MANUAL", "LO QUE FACTURÓ EL AÑO", [
        (["Alcance del sistema:"], ["Perforación geotécnica    62 %"]),
        (["«perforación geotécnica"], ["Ensayos de laboratorio    24 %"]),
        (["en superficie»"], ["Alquiler de equipos       14 %"]),
    ], y=50)
    banda(d, y + 20, 130, "Una sola línea en el manual. Tres líneas en la facturación", px=CUE)
    return guardar(im, "s3_estimulo.png", DEST)


def alcance_que_es():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("QUÉ ES", ["Hasta dónde llega el sistema de gestión"], AZUL2),
        ("SE DEFINE POR", ["Procesos y actividades", "Productos y servicios", "Sedes"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "La cláusula 4.3 lo pide documentado y disponible", px=CUE)
    return guardar(im, "s3_alcance-que-es.png", DEST)


def alcance_como_se_define():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("SE PUEDE", ["Dejar fuera lo que no aplica", "Si se justifica por escrito"], AZUL2),
        ("NO SE PUEDE", ["Excluir un requisito que sí aplica", "Elegir por conveniencia"], ROJO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Un solo alcance puede servir a las tres normas", px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_alcance-como-se-define.png", DEST)


def fuera_del_alcance():
    im, d = lienzo(1250)
    y = franjas(d, [
        ("NO DESAPARECE", ["La actividad se sigue haciendo"], GRIS),
        ("PERO", ["No se audita", "Sus peligros no se gestionan", "Sus aspectos tampoco"], ROJO),
    ], im, y=60, alto=330)
    banda(d, y + 20, 140, "El cliente audita lo que está dentro. Lo de fuera no lo mira nadie",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_fuera-del-alcance.png", DEST)


def declarar_de_menos():
    im, d = lienzo(1000)
    y = comparativa(d, "DECLARAR DE MENOS", "DECLARAR COMPLETO", [
        (["Abarata la certificación"], ["Cuesta más auditar"]),
        (["Deja gente sin cubrir"], ["Cubre a todo el personal"]),
        (["El hueco aparece en el accidente"], ["El hueco aparece en la auditoría"]),
    ], y=50)
    banda(d, y + 20, 140, "Al revisar el alcance: ¿qué hacemos que no esté aquí?", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_declarar-de-menos.png", DEST)


def procesos_vs_areas():
    im, d = lienzo(1000)
    y = comparativa(d, "POR ÁREAS", "POR PROCESOS", [
        (["Quién manda a quién"], ["Qué transforma qué"]),
        (["Cada área guarda lo suyo"], ["La salida de uno entra al otro"]),
        (["El hueco cae entre dos áreas"], ["Cada proceso tiene responsable"]),
    ], y=50)
    banda(d, y + 20, 140, "Lo que no tiene responsable no es proceso: es una costumbre",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_procesos-vs-areas.png", DEST)


def mapa_y_alcance():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("EL MAPA", ["Muestra los procesos y cómo se enlazan"], AZUL2),
        ("Y ADEMÁS", ["Hace visible el alcance", "Lo que no está, no se gestiona"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Un mismo proceso puede servir a los tres sistemas", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_mapa-y-alcance.png", DEST)


def encargo():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("PASO 1", ["Cada hecho, dentro o fuera", "del alcance declarado"], AZUL2),
        ("PASO 2", ["Cada actividad en el mapa", "operativo, de apoyo o de dirección"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Y señalar los procesos que faltan y los que no tienen responsable",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s3_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(1780)
    y = caso(d, "CASO A", "Sondajes y Geotecnia del Sur S.A.C.  ·  perforación geotécnica",
        ["H1 · El alcance declarado dice: «perforación geotécnica en superficie»",
         "H2 · Opera además un laboratorio de suelos en la ciudad, con seis personas",
         "H3 · En el laboratorio se manejan reactivos y se generan residuos químicos",
         "H4 · Las máquinas se reparan en un taller propio, alquilado, a dos cuadras",
         "H5 · El transporte de las máquinas lo hace un tercero contratado",
         "H6 · El mapa de procesos tiene tres cajas: perforación, logística y administración",
         "H7 · Ni el laboratorio ni el taller aparecen en el mapa",
         "H8 · El cliente audita solo lo que está dentro del alcance declarado"],
        color=AZUL2, y=50, alto=190)
    banda(d, y + 24, 140, "Presenta su alcance al cliente antes de la auditoría de ingreso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(1780)
    y = caso(d, "CASO B", "Montaje de Estructuras Metálicas S.A.C.  ·  22 trabajadores en taller",
        ["H1 · El alcance declarado dice: «montaje de estructuras en unidades mineras»",
         "H2 · La empresa fabrica esas estructuras en su propio taller de la costa",
         "H3 · En ese taller hay soldadura, corte y pintura, con veintidós trabajadores",
         "H4 · El diseño de las estructuras lo hace un ingeniero externo por encargo",
         "H5 · El mapa tiene cuatro cajas: montaje, compras, calidad y recursos humanos",
         "H6 · La fabricación no aparece como proceso en el mapa",
         "H7 · Compras no tiene responsable asignado",
         "H8 · Dos no conformidades del año vinieron de piezas mal fabricadas"],
        color=TEAL, y=50, alto=190)
    banda(d, y + 24, 140, "Renueva su certificación. El auditor pide el alcance y el mapa",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("ENTREGAN", ["Los ocho hechos separados", "Dentro y fuera del alcance"], AZUL2),
        ("Y ADEMÁS", ["Cada actividad en su tipo de proceso", "Los que faltan y los que no tienen dueño"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Esta actividad quedó fuera del alcance"], AZUL2),
        ("APOYO", ["Y lo sostenemos en este hecho"], TEAL),
        ("PREGUNTA", ["¿Quién queda sin cubrir mientras siga fuera?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 140, "Dos minutos por equipo. Empezamos por lo que quedó fuera",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s3_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1200)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que el alcance de un sistema era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué hace tu empresa que no esté en su alcance?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s3_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 3")
    for fn in (puente, estimulo, alcance_que_es, alcance_como_se_define, fuera_del_alcance,
               declarar_de_menos, procesos_vs_areas, mapa_y_alcance, encargo,
               ficha_caso_a, ficha_caso_b, a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
