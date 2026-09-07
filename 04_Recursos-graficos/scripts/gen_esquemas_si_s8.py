# -*- coding: utf-8 -*-
"""Esquemas de la sesión 8 de SI-SGCSSMA · objetivos, plan y programa anual · 6.2

Lo legal sale del §15, verificado el 2026-09-03:
  Ley 29783 art. 38 planificación · art. 39 objetivos de la planificación
  DS 005-2012-TR art. 32 f) el Programa Anual entre los documentos que se exhiben ·
  art. 42 c) el comité lo APRUEBA · art. 81 las cinco condiciones del objetivo medible
  Ni «Plan Anual» ni «Programa Anual» aparecen en la Ley 29783: vienen del reglamento.

Uso:  python gen_esquemas_si_s8.py
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
        ("20'", "CONEXIÓN", "Los objetivos de una empresa, tal como los escribió", AZUL2),
        ("45'", "ADQUISICIÓN", "Cómo se formula un objetivo y cómo baja al programa", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas presentan su programa del año", MORADO),
        ("20'", "DISCUSIÓN", "Qué objetivo no se puede evaluar, y qué deja fuera el programa", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s8.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué normas obligan a la empresa", "Y qué pasa si no las cumple"], AZUL2),
        ("HOY", ["Qué se propone hacer este año", "Y cómo se comprueba que lo hizo"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Cumplir la ley es el piso. El objetivo dice a dónde quiere llegar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_puente.png", DEST)


def estimulo():
    """La hoja de objetivos de una empresa, tal como la escribio. Solo hechos."""
    im, d = lienzo(990)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "OBJETIVOS DEL SISTEMA DE GESTIÓN", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Objetivo 1 de 3  ·  hoja presentada al cliente", 38, BLANCO, ancho=W - 200)
    campos = [("OBJETIVO", "Mejorar la cultura de seguridad"),
              ("INDICADOR", "—"),
              ("META", "—"),
              ("PLAZO", "Durante el año"),
              ("RESPONSABLE", "Gerencia")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 92], 12, fill=GRISC)
        cen(d, 90, y + 24, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 22, val, CUE, AZUL, ancho=W - 560)
        y += 104
    banda(d, 840, 130, "Los otros dos objetivos están escritos igual", px=CUE)
    return guardar(im, "s8_estimulo.png", DEST)


def objetivo_que_es():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("COHERENTE", ["Sale de la política, no de una lluvia de ideas"], AZUL2),
        ("MEDIBLE", ["Se le puede poner un número y comprobarlo"], TEAL),
        ("CON DUEÑO", ["Un responsable con nombre y cargo"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres cosas sin las cuales no es un objetivo del sistema", px=CUE)
    return guardar(im, "s8_objetivo-que-es.png", DEST)


def art_81():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("ESCRITO", ["Documentado y comunicado a quien le toca"], AZUL2),
        ("REVISADO", ["Evaluado y actualizado, no dormido un año"], TEAL),
        ("EXIGIDO", ["El DS 005 pide objetivos medibles", "Artículo 81"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "La norma y la ley peruana piden lo mismo, con otras palabras",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_art-81.png", DEST)


def cuatro_partes():
    im, d = lienzo(1620)
    y = franjas(d, [
        ("INDICADOR", ["Qué se mide, y cómo se calcula"], AZUL2),
        ("META", ["El número al que se quiere llegar"], TEAL),
        ("PLAZO", ["Cuándo, con fecha"], MORADO),
        ("RESPONSABLE", ["Quién, con nombre y cargo"], AMBAR),
    ], im, y=50, alto=280)
    banda(d, y + 20, 150, "Si falta una de las cuatro, el objetivo no se puede evaluar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_cuatro-partes.png", DEST)


def deseo_u_objetivo():
    im, d = lienzo(1010)
    y = comparativa(d, "ES UN DESEO", "ES UN OBJETIVO", [
        (["Mejorar la seguridad"], ["Bajar el índice de 12 a 8 al 31 de diciembre"]),
        (["Cuidar el medio ambiente"], ["Bajar 15 % el agua por tonelada al 30 de junio"]),
        (["Responsable: gerencia"], ["Responsable: el jefe de planta"]),
    ], y=50)
    banda(d, y + 20, 150, "El deseo no se puede medir, así que tampoco se puede incumplir",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_deseo-u-objetivo.png", DEST)


def tres_sistemas():
    im, d = lienzo(1010)
    y = tabla(d, ["CALIDAD", "AMBIENTE", "SEGURIDAD"], [
        ([["Reclamos del cliente"], ["Agua por tonelada"], ["Condiciones corregidas"]],
         "", None, None),
        ([["De 8 a 3 al 31 de diciembre"], ["Bajar 15 % al 30 de junio"],
          ["90 % en 15 días"]], "", None, None),
    ], [50, 530, 1010, W - 50], y=50)
    banda(d, y + 30, 150, "Los tres van en un solo cuadro: el sistema es uno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_tres-sistemas.png", DEST)


def de_donde_sale():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("VIENE", ["De un riesgo o un aspecto ya identificado", "En la cláusula 6.1"], AZUL2),
        ("O NO", ["Si no viene de ahí, es un objetivo inventado"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 160, "Un programa se puede cumplir entero sin tocar lo que de verdad puede matar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_de-donde-sale.png", DEST)


def programa_anual():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("OBJETIVO", ["Dice a dónde se quiere llegar"], AZUL2),
        ("PROGRAMA", ["Dice cómo se llega: las actividades del año"], TEAL),
        ("CADA LÍNEA", ["Actividad, responsable, fecha y recursos"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Una actividad sin responsable y sin fecha no se puede seguir",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_programa-anual.png", DEST)


def quien_aprueba():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("EXHIBE", ["El programa anual está entre los seis documentos",
                    "DS 005, artículo 32 f)"], AZUL2),
        ("VISIBLE", ["La política y el IPERC, además, en lugar visible",
                     "DS 005, artículo 32"], TEAL),
        ("APRUEBA", ["El comité aprueba el programa anual",
                     "DS 005, artículo 42 c)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "No lo aprueba la gerencia sola. Y «se toma conocimiento» no es aprobar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_quien-aprueba.png", DEST)


def errores_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("COPIADO", ["El del año pasado con la fecha cambiada"], ROJO),
        ("INCOMPLETO", ["Actividades sin responsable, sin fecha o sin presupuesto"], ROJO),
        ("FANTASMA", ["Programado sobre equipos que ya se dieron de baja"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres formas de tener un programa que no se puede ejecutar", px=CUE)
    return guardar(im, "s8_errores-1.png", DEST)


def errores_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("INCOMPLETO", ["Deja fuera los riesgos altos que el IPERC identificó"], ROJO),
        ("TARDE", ["El indicador se mide en diciembre, cuando ya no se corrige"], ROJO),
        ("SIN VOTO", ["El acta dice «se toma conocimiento», no «se aprueba»"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Y estos tres no se ven al mirar el programa: hay que cruzarlo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_errores-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué objetivos se pueden evaluar", "Y a cuáles les falta algo"], AZUL2),
        ("PASO 2", ["Si el programa cubre lo identificado", "Y si lo aprobó quien debía"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas presentaron sus objetivos y su programa del año",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s8_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2010)
    y = caso(d, "CASO A", "Estructuras y Calderería Vulcano S.A.C.  ·  planta metalmecánica  ·  48 trabajadores",
        ["H1 · Hay comité de seguridad, elegido en marzo",
         "H2 · Los objetivos del año están escritos con indicador, meta, plazo y responsable",
         "H3 · Uno dice: bajar el índice de frecuencia de 12 a 8 al 31 de diciembre; responsable, el jefe de planta",
         "H4 · El programa anual es el del año pasado con la fecha cambiada: las mismas 14 actividades",
         "H5 · Tres actividades hablan del horno de tratamiento, que se dio de baja en enero",
         "H6 · Nadie midió el índice de frecuencia durante el año: el primer cálculo es de diciembre",
         "H7 · El acta del comité de enero dice «se toma conocimiento del programa anual»",
         "H8 · El programa no tiene columna de presupuesto"],
        color=AZUL2, y=50, alto=200)
    banda(d, y + 24, 140, "Presenta al cliente sus objetivos y su programa anual",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Packing y Frío Valle Norte S.A.C.  ·  empaque de arándanos  ·  60 trabajadores",
        ["H1 · Hay comité de seguridad, elegido en enero",
         "H2 · Los objetivos son tres: «mejorar la cultura de seguridad», «cuidar el medio ambiente» y «satisfacer al cliente»",
         "H3 · Ninguno tiene indicador ni meta. Los tres dicen «durante el año» y «responsable: gerencia»",
         "H4 · El programa anual tiene 22 actividades, cada una con responsable, semana y presupuesto",
         "H5 · El acta de febrero registra que el comité aprobó el programa anual, con los votos",
         "H6 · El IPERC puso como riesgo alto el trabajo en cámara de frío. Ninguna actividad lo toca",
         "H7 · La matriz ambiental puso como aspecto significativo el agua del lavado. Tampoco figura",
         "H8 · A fin de año se informó «cumplimiento del programa anual: 91 %»"],
        color=TEAL, y=50, alto=200)
    banda(d, y + 24, 140, "Presenta al cliente sus objetivos y su programa anual",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Cada objetivo con lo que le falta", "De las cuatro partes"], AZUL2),
        ("Y ADEMÁS", ["Qué deja fuera el programa", "Y quién lo aprobó"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este objetivo no se puede evaluar"], AZUL2),
        ("APOYO", ["Y decimos cuál de las cuatro partes le falta"], TEAL),
        ("PREGUNTA", ["¿Qué riesgo alto se quedó fuera del programa?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por lo que el programa dejó fuera",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s8_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que ponerse una meta era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Cómo sabrías en junio si vas bien o vas mal?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s8_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 8")
    for fn in (ruta, puente, estimulo, objetivo_que_es, art_81, cuatro_partes,
               deseo_u_objetivo, tres_sistemas, de_donde_sale, programa_anual,
               quien_aprueba, errores_1, errores_2, encargo, ficha_caso_a, ficha_caso_b,
               a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
