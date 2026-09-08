# -*- coding: utf-8 -*-
"""Esquemas de la sesión 21 de SI-SGCSSMA · incidentes y acción correctiva · 10.2

Lo legal sale del §15:
  Ley 29783 art. 42 · la investigación identifica factores de riesgo, causas
  INMEDIATAS (actos y condiciones subestándares), causas BÁSICAS (factores
  personales y del trabajo) y las deficiencias del sistema — verificado 2026-09-04
  art. 92 · investigar con los representantes y comunicar las medidas a la autoridad
  DS 005 art. 88 · quién investiga y con quién · art. 33 a) el registro incluye la
  investigación y las medidas correctivas

Uso:  python gen_esquemas_si_s21.py
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
        ("20'", "CONEXIÓN", "Un informe de investigación, tal como se cerró", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué se hace, cómo se busca la causa y quién investiga", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos cierres que no cerraron nada", MORADO),
        ("20'", "DISCUSIÓN", "Hasta qué nivel de causa llegaron", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s21.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué revisa la dirección", "Y qué sale de esa revisión"], AZUL2),
        ("HOY", ["Qué se hace cuando algo falla", "Y cómo se busca por qué falló"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Empieza la cláusula 10: lo que el sistema hace con sus propios errores",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_puente.png", DEST)


def estimulo():
    """El informe tal como se cerro. Solo hechos."""
    im, d = lienzo(1000)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "INFORME DE INVESTIGACIÓN", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Patio de contenedores  ·  una página", 38, BLANCO, ancho=W - 200)
    campos = [("EVENTO", "Desestiba de contenedor"),
              ("FECHA", "12 de agosto"),
              ("CAUSA", "Error del operador"),
              ("ACCIÓN", "Charla de reforzamiento"),
              ("FIRMA", "El supervisor de patio")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 94], 12, fill=GRISC)
        cen(d, 90, y + 25, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 23, val, CUE, AZUL, ancho=W - 560)
        y += 106
    banda(d, 850, 130, "Es la tercera desestiba en el mismo patio en catorce meses", px=CUE)
    return guardar(im, "s21_estimulo.png", DEST)


def tres_cosas():
    im, d = lienzo(1010)
    y = tabla(d, ["INCIDENTE", "ACCIDENTE", "NO CONFORMIDAD"], [
        ([["El suceso que pudo causar daño"],
          ["El incidente que sí causó lesión"],
          ["El incumplimiento de un requisito"]], "", None, None),
    ], [50, 500, 950, W - 50], y=50)
    banda(d, y + 30, 160, "Los tres disparan lo mismo, y el requisito puede ser de la norma, de la ley o propio",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_tres-cosas.png", DEST)


def disparan():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("REACCIONAR", ["Controlar, corregir y atender la consecuencia"], AZUL2),
        ("BUSCAR", ["Evaluar si hace falta eliminar la causa"], TEAL),
        ("REGISTRAR", ["Qué pasó y qué se hizo después"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "El mismo camino para los tres, sin importar si hubo lesión o no",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_disparan.png", DEST)


def corregir():
    im, d = lienzo(1080)
    y = tabla(d, ["CORREGIR", "ACCIÓN CORRECTIVA"], [
        ([["Arregla lo que está mal ahora"], ["Elimina la causa"]], "", None, None),
        ([["Limpiar el derrame"], ["Cambiar la válvula que gotea"]], "", None, None),
        ([["El problema puede volver"], ["Se ataca para que no vuelva"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Las dos hacen falta. Solo la primera deja el problema esperando su turno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_corregir.png", DEST)


def el_orden():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("PRIMERO", ["Se reacciona: se controla y se atiende"], AZUL2),
        ("DESPUÉS", ["Se evalúa si hace falta acción correctiva"], TEAL),
        ("Y SE ELIGE", ["Con la jerarquía de controles, no con lo que sea más rápido"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "La acción correctiva también se elige por niveles: eliminar antes que capacitar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_el-orden.png", DEST)


def tres_niveles():
    im, d = lienzo(1440)
    y = filas_letra(d, [
        ("1", "INMEDIATAS", "Actos y condiciones subestándares", AZUL2),
        ("2", "BÁSICAS", "Factores personales y factores del trabajo", TEAL),
        ("3", "EL SISTEMA", "Cualquier deficiencia del sistema de gestión", MORADO),
    ], y=50, alto=290, sep=30)
    banda(d, y + 20, 160, "Los tres niveles los nombra la Ley 29783, artículo 42, con estas palabras",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_tres-niveles.png", DEST)


def por_que():
    im, d = lienzo(1010)
    y = comparativa(d, "SE QUEDA AHÍ", "SIGUE PREGUNTANDO", [
        (["No usó su EPP"], ["Por qué pudo trabajar sin él"]),
        (["Error del operador"], ["Qué del puesto hizo probable ese error"]),
        (["Falta de atención"], ["Qué falló en el sistema para que dependiera de eso"]),
    ], y=50)
    banda(d, y + 20, 160, "Si la causa es siempre la persona, la investigación se detuvo en el nivel 1",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_por-que.png", DEST)


def quien_investiga():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("QUIÉNES", ["El empleador y el comité o supervisor", "DS 005, artículo 88"], AZUL2),
        ("CON QUIÉN", ["Con apoyo de personas competentes",
                       "Y participación de los trabajadores"], TEAL),
        ("CÓMO QUEDA", ["Documentada, y dejando ver las deficiencias del sistema"], MORADO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Un informe de una página firmado por una sola persona no cumple el 88",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_quien-investiga.png", DEST)


def que_queda():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("REGISTRO", ["Incluye la investigación y las medidas correctivas",
                      "DS 005, artículo 33 a)"], AZUL2),
        ("AUTORIDAD", ["Se le comunican las medidas de prevención adoptadas",
                       "Ley 29783, artículo 92"], TEAL),
        ("COMITÉ", ["Y participa en la investigación, no solo se entera"], MORADO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "El registro sin las medidas es medio registro: el artículo pide las dos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_que-queda.png", DEST)


def despues_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("RIESGOS", ["Se revisa si los evaluados siguen siendo los mismos"], AZUL2),
        ("PELIGRO NUEVO", ["Si el control trae uno, se evalúa antes de aplicarlo"], TEAL),
        ("EFICACIA", ["Se revisa si la acción de verdad evitó la repetición"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Que la acción se hizo no prueba que sirvió. Eso se comprueba después",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_despues-1.png", DEST)


def despues_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("EL SISTEMA", ["Si hace falta, se cambia el sistema y no solo el procedimiento"], AZUL2),
        ("SE COMUNICA", ["Los resultados van a los trabajadores y sus representantes"], TEAL),
        ("Y SUBE", ["Entran a la revisión por la dirección del año"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Aquí se cierra el círculo con la sesión pasada", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_despues-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Hasta qué nivel de causa llegaron", "Y cuál quedó fuera"], AZUL2),
        ("PASO 2", ["Si fue corrección o acción correctiva", "Y qué correspondía"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas dieron por cerrado lo que les pasó",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s21_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Terminal Portuario Bahía Norte S.A.C.  ·  patio, muelle y almacén  ·  180 trabajadores",
        ["H1 · El 12 de agosto un contenedor se desestibó y cayó desde el segundo nivel",
         "H2 · No hubo lesionados",
         "H3 · El informe de investigación tiene una página y lo firmó solo el supervisor de patio",
         "H4 · La causa registrada es «error del operador del reach stacker»",
         "H5 · La acción tomada fue charla de reforzamiento al operador y llamada de atención",
         "H6 · En los últimos catorce meses hubo tres desestibas parecidas en el mismo patio",
         "H7 · Las tres se cerraron con charla de reforzamiento",
         "H8 · El piso del patio tiene un desnivel que mantenimiento reportó hace un año"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El informe está firmado y el caso está cerrado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Panificadora Santa Elena S.A.C.  ·  dos turnos  ·  60 trabajadores",
        ["H1 · La auditoría levantó una no conformidad: los registros de temperatura de horno de julio no existen",
         "H2 · La empresa imprimió los registros faltantes con los datos del sistema",
         "H3 · Los archivó en la carpeta del mes",
         "H4 · El informe de cierre dice «no conformidad subsanada» y lo firmó el jefe de producción",
         "H5 · No se preguntó por qué durante julio nadie llenó esos registros",
         "H6 · En julio el turno noche trabajó sin supervisor",
         "H7 · El supervisor de turno noche renunció el 30 de junio, y la vacante sigue abierta",
         "H8 · El comité no participó en el cierre de la no conformidad"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "La no conformidad figura como cerrada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["El nivel de causa al que llegaron", "Y la causa que quedó fuera"], AZUL2),
        ("Y ADEMÁS", ["Si fue corrección o acción correctiva", "Y qué exige la ley"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Esta investigación se detuvo en este nivel"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo 42 y en los hechos"], TEAL),
        ("PREGUNTA", ["¿Qué va a pasar la próxima vez, con lo que se hizo?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por la causa que nadie escribió",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s21_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que investigar un accidente era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Cuántas veces oíste «fue error del trabajador» como causa final?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s21_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 21")
    for fn in (ruta, puente, estimulo, tres_cosas, disparan, corregir, el_orden,
               tres_niveles, por_que, quien_investiga, que_queda, despues_1, despues_2,
               encargo, ficha_caso_a, ficha_caso_b, a_trabajar, formato_discusion,
               reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
