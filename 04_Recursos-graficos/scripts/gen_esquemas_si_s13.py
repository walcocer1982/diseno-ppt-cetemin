# -*- coding: utf-8 -*-
"""Esquemas de la sesión 13 de SI-SGCSSMA · control operacional · 8.1

Abre el bloque de operación. Lo legal sale del §15:
  DS 024-2016-EM · art. 7 definiciones de trabajo de alto riesgo y de PETAR ·
  art. 36 cuándo el PETAR es obligatorio · art. 98 estándares y PETS con
  participación de los trabajadores · art. 99 explicar la orden y el ATS

OJO: el número de anexo del formato PETAR NO está verificado en el §15, así que
no aparece en ninguna figura. Si se confirma, se añade aquí.

Uso:  python gen_esquemas_si_s13.py
"""
from __future__ import annotations

import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      caso, filas_letra, tabla, cen, izq)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def ruta():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("20'", "CONEXIÓN", "Un permiso de trabajo, tal como lo firmaron", AZUL2),
        ("45'", "ADQUISICIÓN", "Estándar, PETS, ATS y permiso: cuál toca en cada caso", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas y sus trabajos de alto riesgo", MORADO),
        ("20'", "DISCUSIÓN", "Qué documento faltaba y si el control alcanzaba", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s13.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Cómo se planifica el sistema", "Y con qué se documenta"], AZUL2),
        ("HOY", ["Cómo se controla la tarea", "En el frente, no en la oficina"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Empieza el bloque de operación: aquí el sistema se encuentra con el trabajo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_puente.png", DEST)


def estimulo():
    """El permiso tal como lo firmaron. Solo hechos."""
    im, d = lienzo(990)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "PERMISO DE TRABAJO", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Espacio confinado  ·  limpieza interior de tanques", 38, BLANCO,
        ancho=W - 200)
    campos = [("TAREA", "Limpieza interior del tanque 3"),
              ("FECHA", "Día 1 del mes"),
              ("VALIDEZ", "Todo el mes"),
              ("CONTROLES", "Uso de respirador y arnés"),
              ("FIRMA", "El prevencionista")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 92], 12, fill=GRISC)
        cen(d, 90, y + 24, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 22, val, CUE, AZUL, ancho=W - 560)
        y += 104
    banda(d, 840, 130, "Dos operarios entran al tanque cada semana", px=CUE)
    return guardar(im, "s13_estimulo.png", DEST)


def control_operacional():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("PLANIFICAR", ["Qué procesos hay que controlar"], AZUL2),
        ("CRITERIOS", ["Con qué condiciones debe salir el proceso"], TEAL),
        ("CONTROLAR", ["Que se ejecute según esos criterios"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Los tres pasos que pide la cláusula 8.1, en ese orden", px=CUE)
    return guardar(im, "s13_control-operacional.png", DEST)


def y_ademas():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("DOCUMENTAR", ["Guardar lo que dé confianza de que se hizo así"], AZUL2),
        ("CAMBIOS", ["Controlar también los cambios que se planifican"], TEAL),
        ("FRENTE", ["Aquí el sistema deja el papel y toca la tarea"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Todo lo anterior se decidió en oficina. Esto se comprueba en la labor",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_y-ademas.png", DEST)


def estandar_y_pets():
    im, d = lienzo(1080)
    y = tabla(d, ["ESTÁNDAR", "PETS"], [
        ([["Dice cómo debe quedar"], ["Dice cómo se hace"]], "", None, None),
        ([["El resultado que se espera"], ["La tarea, paso a paso"]], "", None, None),
        ([["La baranda va a 90 cm"], ["Cómo se arma y se revisa la baranda"]],
         "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "El DS 024 pide los dos, y con participación de los trabajadores",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_estandar-y-pets.png", DEST)


def pets_obligaciones():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PARTICIPAN", ["Los elabora el titular con los trabajadores",
                        "DS 024, artículo 98"], AZUL2),
        ("COLOCAN", ["Van en los manuales y en la labor y el área de trabajo"], TEAL),
        ("EXPLICAN", ["Antes de la orden, y se verifica en la labor",
                      "DS 024, artículo 99"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Distribuirlos e instruirlos es parte de la norma, no un extra",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_pets-obligaciones.png", DEST)


def ats_cuando():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("RUTINA", ["La actividad no es rutinaria"], AZUL2),
        ("BASE", ["No está identificada en el IPERC de línea base"], TEAL),
        ("PETS", ["Y no cuenta con un PETS", "DS 024, artículo 99"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Las tres a la vez. El ATS se hace en el sitio, con los que van a trabajar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_ats-cuando.png", DEST)


def ats_limite():
    im, d = lienzo(1010)
    y = comparativa(d, "YA NO ES ATS", "SÍ ES ATS", [
        (["Lo que se hace tres veces por semana"], ["Lo que se hace por primera vez"]),
        (["El formato fotocopiado"], ["Llenado en el sitio, ese día"]),
        (["Con la fecha cambiada"], ["Con los que van a ejecutar la tarea"]),
    ], y=50)
    banda(d, y + 20, 150, "Si la tarea se repite, deja de ser no rutinaria: toca escribir el PETS",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_ats-limite.png", DEST)


def petar_que_es():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("RIESGO", ["Tarea con alto potencial de daño grave o muerte",
                    "DS 024, artículo 7"], AZUL2),
        ("AUTORIZA", ["El permiso autoriza el trabajo en esa zona"], TEAL),
        ("DECIDE", ["Qué tareas son de alto riesgo lo fija el titular y la autoridad"],
         MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "No lo decide el criterio de cada quien: está establecido",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_petar-que-es.png", DEST)


def petar_firma():
    im, d = lienzo(1010)
    y = comparativa(d, "NO ES UN PETAR", "SÍ LO ES", [
        (["Firmado el día 1 para todo el mes"], ["Firmado para cada turno"]),
        (["Con una sola firma"], ["Ingeniero supervisor y jefe de área"]),
        (["Guardado en la oficina"], ["En el sitio donde se ejecuta"]),
    ], y=50)
    banda(d, y + 20, 160, "Obligatorio en minería, artículo 36. Fuera, es el permiso que exige el cliente",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_petar-firma.png", DEST)


def sirve_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("ESCRIBE", ["Lo redacta también quien hace la tarea"], AZUL2),
        ("VIVE", ["Está en la labor, no en la carpeta de la oficina"], TEAL),
        ("VERSIÓN", ["La copia que se usa es la vigente"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres condiciones para que el papel llegue al frente", px=CUE)
    return guardar(im, "s13_sirve-1.png", DEST)


def sirve_2():
    im, d = lienzo(1010)
    y = comparativa(d, "NO CONTROLA", "CONTROLA", [
        (["Solo lista el EPP"], ["Elimina, aísla o ventila primero"]),
        (["Nadie sabe qué dice"], ["El que ejecuta lo explica con sus palabras"]),
        (["Se archiva firmado"], ["Se verifica en la labor"]),
    ], y=50)
    banda(d, y + 20, 150, "Un PETS que nadie leyó es un papel, no un control",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_sirve-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué documento correspondía", "Y cuál falta o se usa mal"], AZUL2),
        ("PASO 2", ["Si los controles alcanzan", "Y qué habría que corregir"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas muestran cómo controlan sus trabajos de alto riesgo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s13_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Bebidas y Maltas del Centro S.A.C.  ·  90 trabajadores  ·  limpieza interior de tanques",
        ["H1 · La limpieza interior de los tanques de fermentación la hacen dos operarios",
         "H2 · El cliente exige permiso de trabajo para espacio confinado, y el formato existe",
         "H3 · El permiso del mes está firmado una sola vez, el día 1: «válido para todo el mes»",
         "H4 · Lo firmó solo el prevencionista. No hay firma del jefe de área",
         "H5 · Hay un PETS de limpieza de tanques, redactado por la consultora que implementó el sistema",
         "H6 · El PETS está en la carpeta de la oficina; en la sala de tanques no hay nada colgado",
         "H7 · Los únicos controles que lista el PETS son «uso de respirador» y «uso de arnés»",
         "H8 · No se mide el oxígeno antes de entrar al tanque: el PETS no lo menciona"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El corporativo del cliente audita los trabajos de alto riesgo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Mantenimiento Eléctrico Industrial S.A.C.  ·  45 trabajadores, 30 técnicos electricistas",
        ["H1 · Cada tarea nueva se hace con un ATS llenado en el sitio por los propios técnicos",
         "H2 · El cambio de luminarias en altura se hace tres veces por semana desde hace dos años",
         "H3 · Esa tarea se sigue haciendo siempre con ATS",
         "H4 · No existe PETS de trabajo en altura",
         "H5 · El ATS de esa tarea es el mismo formato fotocopiado, con la fecha cambiada",
         "H6 · Hay un estándar de trabajos en altura, de 2021, que exige línea de vida horizontal",
         "H7 · En el almacén del cliente no hay línea de vida: el arnés se ancla a la estructura",
         "H8 · Al preguntarles, dos técnicos dicen que el estándar «lo vieron en la inducción»"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "El cliente pide revisar cómo controla sus trabajos en altura",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Cada tarea con el documento que le tocaba", "Y el que falta"], AZUL2),
        ("Y ADEMÁS", ["Si el control alcanza para el peligro", "Y qué corregirían"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["A esta tarea le tocaba este documento"], AZUL2),
        ("APOYO", ["Y lo sostenemos en lo que la norma pide de él"], TEAL),
        ("PREGUNTA", ["¿Qué control faltaba antes de llegar al EPP?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por el documento que faltaba",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s13_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que tener el procedimiento era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Podrías explicar con tus palabras el PETS de tu tarea?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s13_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 13")
    for fn in (ruta, puente, estimulo, control_operacional, y_ademas, estandar_y_pets,
               pets_obligaciones, ats_cuando, ats_limite, petar_que_es, petar_firma,
               sirve_1, sirve_2, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
