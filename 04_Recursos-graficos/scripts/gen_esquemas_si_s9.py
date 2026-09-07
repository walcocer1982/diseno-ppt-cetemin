# -*- coding: utf-8 -*-
"""Esquemas de la sesión 9 de SI-SGCSSMA · recursos, competencia y capacitación · 7.1–7.3

Lo legal sale del §15, verificado el 2026-09-03:
  Ley 29783 · 27 competencia del puesto · 35 b) cuatro al año · 35 d) licencias con goce
  de haber · 49 f) recursos al comité · 49 g) los tres momentos en que hay que capacitar
  DS 005-2012-TR · 27 en qué se centra la formación · 28 dentro de la jornada y el costo
  nunca lo paga el trabajador · 29 a) y b) por riesgo y por gente competente ·
  33 g) el registro · 98 fuera de jornada se remunera

Uso:  python gen_esquemas_si_s9.py
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
        ("20'", "CONEXIÓN", "Un registro de capacitación, tal como quedó llenado", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué es competencia y qué reglas pone la ley a capacitar", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas muestran cómo forman a su gente", MORADO),
        ("20'", "DISCUSIÓN", "Si el trabajador quedó competente, y con qué se prueba", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s9.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué se propone hacer la empresa", "Y cómo se comprueba que lo hizo"], AZUL2),
        ("HOY", ["Con qué gente y con qué recursos", "Se hace todo eso"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Un programa sin gente preparada es una lista de buenas intenciones",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_puente.png", DEST)


def estimulo():
    """Un registro de capacitacion tal como quedo llenado. Solo hechos."""
    im, d = lienzo(990)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "REGISTRO DE CAPACITACIÓN", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Sesión 3 de 4 del programa del año", 38, BLANCO, ancho=W - 200)
    campos = [("TEMA", "Uso correcto de EPP"),
              ("FECHA", "Sábado 14, 8:00 a. m."),
              ("DURACIÓN", "1 hora"),
              ("EXPOSITOR", "El jefe de producción"),
              ("COSTO", "120 soles por participante")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 92], 12, fill=GRISC)
        cen(d, 90, y + 24, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 22, val, CUE, AZUL, ancho=W - 560)
        y += 104
    banda(d, 840, 130, "Asistieron los 26 conductores y firmaron la lista", px=CUE)
    return guardar(im, "s9_estimulo.png", DEST)


def recursos_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("PERSONAS", ["Cuántas hacen falta, y con qué preparación"], AZUL2),
        ("TIEMPO", ["Horas de trabajo pagadas, no sábados regalados"], TEAL),
        ("DINERO", ["El presupuesto que el programa anual necesita"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "La cláusula 7.1 pide determinar y proporcionar los recursos", px=CUE)
    return guardar(im, "s9_recursos-1.png", DEST)


def recursos_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("EQUIPOS", ["Instalaciones, herramientas y protección"], AZUL2),
        ("ASESORÍA", ["Quien sepa del tema, dentro o fuera de la empresa"], TEAL),
        ("COMITÉ", ["Se le asignan los recursos para que funcione de verdad",
                    "Ley 29783, artículo 49 f)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Sin recursos, el comité existe en el papel y no en la planta",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_recursos-2.png", DEST)


def competencia():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("EDUCACIÓN", ["Lo que estudió"], AZUL2),
        ("FORMACIÓN", ["Los cursos que llevó y aprobó"], TEAL),
        ("EXPERIENCIA", ["El tiempo que lleva haciéndolo"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Competencia es poder hacer la tarea sin dañarse ni dañar a otro",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_competencia.png", DEST)


def brecha():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PUESTO", ["Qué competencia se le pide", "Ley 29783, artículo 27"], AZUL2),
        ("PERSONA", ["Qué trae quien lo ocupa"], TEAL),
        ("BRECHA", ["Se cierra capacitando, entrenando o reubicando"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Si nadie escribió qué se le pide al puesto, no hay con qué comparar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_brecha.png", DEST)


def tres_momentos():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("CONTRATAR", ["Al momento de contratarlo", "Sea cual sea su tipo de contrato"], AZUL2),
        ("TRABAJAR", ["Durante el desempeño de la labor"], TEAL),
        ("CAMBIAR", ["Cuando cambia el puesto, la función o la tecnología"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Los tres momentos del artículo 49 g) de la Ley 29783",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_tres-momentos.png", DEST)


def cuantas_y_cuando():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("CUATRO", ["No menos de cuatro al año", "Ley 29783, artículo 35 b)"], AZUL2),
        ("INDUCCIÓN", ["Va antes de pisar el frente de trabajo", "No el mes siguiente"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Cuatro es el mínimo, no la meta. Y llegar tarde es no haber llegado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_cuantas-y-cuando.png", DEST)


def reglas_1():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("JORNADA", ["Se dicta dentro de la jornada de trabajo", "DS 005, artículo 28"], AZUL2),
        ("PAGO", ["Si se dicta fuera, se remunera", "DS 005, artículo 98"], TEAL),
        ("COSTO", ["Lo asume íntegramente el empleador", "Nunca el trabajador"], ROJO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "No es criterio: el reglamento lo dice con esas palabras",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_reglas-1.png", DEST)


def reglas_2():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("RIESGOS", ["Se arma según los riesgos de cada puesto", "DS 005, artículo 29 a)"],
         AZUL2),
        ("EXPOSITOR", ["Lo dicta gente competente y con experiencia", "DS 005, artículo 29 b)"],
         TEAL),
        ("REGISTRO", ["Inducción, capacitación, entrenamiento y simulacros",
                      "DS 005, artículo 33 g)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Un curso igual para todos no atiende los riesgos de ninguno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_reglas-2.png", DEST)


def capacitar_o_conciencia():
    im, d = lienzo(1080)
    y = tabla(d, ["CAPACITAR  ·  7.2", "TOMAR CONCIENCIA  ·  7.3"], [
        ([["Enseñar a hacer la tarea"], ["Saber por qué importa y qué pasa si no"]],
         "", None, None),
        ([["Cómo se usa el equipo"], ["La política y los objetivos del sistema"]],
         "", None, None),
        ([["Qué pasos sigue el procedimiento"],
          ["Que puede alejarse de un peligro grave"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Se puede estar capacitado y no haber tomado conciencia de nada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_capacitar-o-conciencia.png", DEST)


def como_se_comprueba():
    im, d = lienzo(1010)
    y = comparativa(d, "NO LO PRUEBA", "SÍ LO PRUEBA", [
        (["La firma en la lista"], ["Que sepa qué hacer si la máquina se traba"]),
        (["La foto en el grupo"], ["Que sepa a quién avisar y en cuánto tiempo"]),
        (["El certificado enmarcado"], ["Que sepa que puede parar y alejarse"]),
    ], y=50)
    banda(d, y + 20, 150, "La toma de conciencia se comprueba preguntando en el puesto",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_como-se-comprueba.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué condiciones incumple", "Y qué artículo lo manda"], AZUL2),
        ("PASO 2", ["Si quedó competente y consciente", "Y con qué hecho se prueba"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas muestran al cliente cómo forman a su gente",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s9_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2010)
    y = caso(d, "CASO A", "Transportes y Logística Cordillera S.A.C.  ·  transporte de carga  ·  40 trabajadores",
        ["H1 · De los 40 trabajadores, 26 son conductores",
         "H2 · En el año se dictaron ocho capacitaciones, todas los sábados, fuera de la jornada",
         "H3 · A quien asistió el sábado no se le pagó ese tiempo ni se le compensó",
         "H4 · El curso de manejo defensivo lo pagó cada conductor de su bolsillo: 120 soles",
         "H5 · Los ocho temas fueron los mismos para conductores, oficina y estibadores",
         "H6 · Un conductor entró un lunes y salió a ruta ese mismo día",
         "H7 · Su inducción está programada para el mes siguiente",
         "H8 · No existe una descripción de qué competencia se le pide al puesto de conductor"],
        color=AZUL2, y=50, alto=200)
    banda(d, y + 24, 140, "El cliente audita su gestión de personal antes de renovar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Confecciones y Acabados Textiles S.A.C.  ·  52 trabajadores  ·  la auditoría llega en dos semanas",
        ["H1 · Hay comité de seguridad, elegido en febrero",
         "H2 · Hay matriz de competencias por puesto, con educación, formación y experiencia",
         "H3 · Cada ingreso recibe inducción el primer día, antes de entrar a planta, y firma",
         "H4 · El programa del año tiene cuatro capacitaciones: las cuatro son «uso correcto de EPP»",
         "H5 · El IPERC marca como riesgo alto el atrapamiento en la máquina de corte",
         "H6 · Ningún curso del año toca ese riesgo",
         "H7 · Las dicta el jefe de producción, que no acredita formación en seguridad",
         "H8 · No hay registro: la evidencia son fotos en el grupo de WhatsApp"],
        color=TEAL, y=50, alto=200)
    banda(d, y + 24, 150, "Cuatro operarios no saben qué hacer si la máquina de corte se traba",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Cada condición revisada", "Con el artículo que la manda"], AZUL2),
        ("Y ADEMÁS", ["Si quedó competente y consciente", "Y qué falta para cerrarlo"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Esta capacitación incumple, y decimos en qué"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo que lo manda"], TEAL),
        ("PREGUNTA", ["¿Con qué hecho probamos que sabe hacer el trabajo?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por el hecho que lo prueba",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s9_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que estar capacitado era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Alguna vez firmaste una lista de un curso que no entendiste?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s9_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 9")
    for fn in (ruta, puente, estimulo, recursos_1, recursos_2, competencia, brecha,
               tres_momentos, cuantas_y_cuando, reglas_1, reglas_2,
               capacitar_o_conciencia, como_se_comprueba, encargo, ficha_caso_a,
               ficha_caso_b, a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
