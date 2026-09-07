# -*- coding: utf-8 -*-
"""Esquemas de la sesión 20 de SI-SGCSSMA · revisión por la dirección · 9.3

Lo legal sale del §15, verificado el 2026-09-04:
  DS 005-2012-TR art. 89 · las siete cosas que la revisión debe evaluar
  art. 90 · POR LO MENOS UNA VEZ AL AÑO, con el alcance definido según las
  necesidades y riesgos presentes
  art. 91 · las conclusiones se registran y se comunican al comité, a los
  trabajadores y a la organización sindical

Uso:  python gen_esquemas_si_s20.py
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
        ("20'", "CONEXIÓN", "Un acta de revisión por la dirección, tal como quedó", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué entra, qué sale y cada cuánto se hace", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: una revisión que no sirvió y una que no se hizo", MORADO),
        ("20'", "DISCUSIÓN", "Qué faltó, y qué debería traer la próxima", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s20.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Cómo se comprueba el cumplimiento", "Y quién audita el sistema"], AZUL2),
        ("HOY", ["Qué hace la dirección con todo eso", "Y cada cuánto tiene que hacerlo"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 160, "La sesión pasada terminó con unos hallazgos que nadie quiso llevar arriba",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_puente.png", DEST)


def estimulo():
    """El acta tal como quedo. Solo hechos."""
    im, d = lienzo(1000)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "ACTA DE REVISIÓN POR LA DIRECCIÓN", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Planta de alimentos balanceados  ·  cierre del año", 38, BLANCO,
        ancho=W - 200)
    campos = [("FECHA", "18 de diciembre"),
              ("DURACIÓN", "40 minutos"),
              ("PRESIDE", "El jefe de seguridad"),
              ("FIRMA", "El jefe de seguridad"),
              ("ACUERDOS", "Tres, sin responsable ni fecha")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 94], 12, fill=GRISC)
        cen(d, 90, y + 25, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 23, val, CUE, AZUL, ancho=W - 560)
        y += 106
    banda(d, 850, 130, "El gerente general no asistió", px=CUE)
    return guardar(im, "s20_estimulo.png", DEST)


def que_es():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("QUIÉN", ["La alta dirección, no el área de seguridad"], AZUL2),
        ("QUÉ MIRA", ["Si el sistema sigue siendo conveniente, adecuado y eficaz"], TEAL),
        ("CADA CUÁNTO", ["Por lo menos una vez al año", "DS 005, artículo 90"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "La norma dice «a intervalos planificados». La ley pone el número",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_que-es.png", DEST)


def no_es():
    im, d = lienzo(1010)
    y = comparativa(d, "NO ES", "SÍ ES", [
        (["Una reunión de avance del área"], ["La dirección mirando su propio sistema"]),
        (["Un informe de lo que salió bien"], ["Una comparación con lo que hoy se necesita"]),
        (["Un trámite de cierre de año"], ["La decisión de qué cambia el año que viene"]),
    ], y=50)
    banda(d, y + 20, 160, "El alcance se define según las necesidades y los riesgos presentes",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_no-es.png", DEST)


def entradas_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("LO ANTERIOR", ["En qué quedaron las acciones de la revisión pasada"], AZUL2),
        ("LOS CAMBIOS", ["En el contexto, en las partes interesadas y en los riesgos"], TEAL),
        ("LO PROPUESTO", ["Cuánto se cumplió de la política y de los objetivos"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres de las entradas. La primera es la que más se olvida", px=CUE)
    return guardar(im, "s20_entradas-1.png", DEST)


def entradas_2():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("LO QUE PASÓ", ["Incidentes, no conformidades y acciones correctivas"], AZUL2),
        ("LO MEDIDO", ["Seguimiento, evaluación del cumplimiento legal y auditoría"], TEAL),
        ("LA GENTE", ["La consulta y participación, y si los recursos alcanzan"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "Sin los resultados de la auditoría, la revisión mira solo lo cómodo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_entradas-2.png", DEST)


def salidas_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("CONCLUSIÓN", ["Si el sistema sigue sirviendo, y en qué no"], AZUL2),
        ("MEJORAS", ["Las oportunidades que se van a tomar"], TEAL),
        ("CAMBIOS", ["Lo que hay que cambiarle al sistema"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres de las salidas que la cláusula 9.3 pide por escrito", px=CUE)
    return guardar(im, "s20_salidas-1.png", DEST)


def salidas_2():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("RECURSOS", ["Los que hacen falta para lo que se decidió"], AZUL2),
        ("ESTRATEGIA", ["Lo que esto implica para la dirección de la empresa"], TEAL),
        ("CON DUEÑO", ["Cada salida con responsable y plazo"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Un acuerdo sin responsable ni fecha no es una salida: es una frase",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_salidas-2.png", DEST)


def art_89():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("OBJETIVOS", ["Si se alcanzaron los objetivos previstos",
                       "DS 005, artículo 89 a)"], AZUL2),
        ("A QUIÉN SIRVE", ["A la organización, a los trabajadores y a la autoridad",
                           "Artículo 89 b)"], TEAL),
        ("QUÉ CAMBIA", ["Si hay que cambiar el sistema, la política o los objetivos",
                        "Artículo 89 c)"], MORADO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "El 89 f) añade una más: los progresos en las medidas correctivas",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_art-89.png", DEST)


def art_90_91():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("AL AÑO", ["Por lo menos una vez", "DS 005, artículo 90"], AZUL2),
        ("SE REGISTRA", ["Las conclusiones se registran", "Artículo 91"], TEAL),
        ("SE COMUNICA", ["Al comité, a los trabajadores y al sindicato",
                         "Artículo 91 b)"], MORADO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 160, "Y a los responsables de los aspectos críticos, para que actúen — 91 a)",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_art-90-91.png", DEST)


def errores_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SIN AUDITORÍA", ["Se hace sin los hallazgos, para no incomodar"], ROJO),
        ("SOLO LO BUENO", ["Se presenta únicamente lo que salió bien"], ROJO),
        ("SIN MEMORIA", ["Se repiten las acciones del año pasado sin decir en qué quedaron"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres formas de que la reunión ocurra y no revise nada", px=CUE)
    return guardar(im, "s20_errores-1.png", DEST)


def errores_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SIN DUEÑO", ["Se sale sin responsable ni plazo para nada"], ROJO),
        ("SIN FIRMA", ["La firma el jefe de seguridad, y no la alta dirección"], ROJO),
        ("SIN SALIR", ["El acta no sale de la oficina de gerencia"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "El último incumple el artículo 91 b), que dice a quién se comunica",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_errores-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué entradas faltaron", "Y qué salidas no sirven"], AZUL2),
        ("PASO 2", ["Qué exige la ley y no se cumplió", "Y qué traería la próxima"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Una revisión que no sirvió, y una que dejó de hacerse",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s20_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Alimentos Balanceados del Norte S.A.C.  ·  molienda, peletizado y despacho  ·  120 trabajadores",
        ["H1 · La revisión duró 40 minutos y la presidió el jefe de seguridad",
         "H2 · El gerente general no asistió; el acta la firmó el jefe de seguridad",
         "H3 · La presentación trae los tres índices del año",
         "H4 · Y el cumplimiento del programa anual: 88 %",
         "H5 · No se presentaron los resultados de la auditoría interna de octubre",
         "H6 · No se revisó en qué quedaron las cinco acciones de la revisión del año pasado",
         "H7 · El acta lista tres acuerdos, ninguno con responsable ni con fecha",
         "H8 · El acta se archivó en la carpeta del sistema. El comité no la ha visto"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "La revisión se hizo y el acta está firmada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Servicios de Saneamiento del Valle S.A.C.  ·  cuatro plantas de tratamiento  ·  95 trabajadores",
        ["H1 · La última revisión por la dirección se hizo en noviembre de hace dos años",
         "H2 · Ese año la empresa operaba dos plantas. Hoy opera cuatro",
         "H3 · Dos de las plantas nuevas tienen procesos con cloro gas",
         "H4 · Antes la empresa no manejaba cloro gas",
         "H5 · La política y los objetivos son los mismos de aquella revisión",
         "H6 · El acta de entonces sí tiene acuerdos con responsable y fecha",
         "H7 · Cuatro de los seis acuerdos siguen abiertos, y nadie los ha vuelto a mirar",
         "H8 · Gerencia dice que la revisión se hará «cuando se estabilice la operación»"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 150, "El sistema sigue revisando una empresa que ya no existe",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Las entradas que faltaron", "Y las salidas que no sirven"], AZUL2),
        ("Y ADEMÁS", ["Lo que la ley exige y no se cumplió", "Y qué traería la próxima"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["A esta revisión le faltó esta entrada"], AZUL2),
        ("APOYO", ["Y lo sostenemos en la cláusula o en el artículo"], TEAL),
        ("PREGUNTA", ["¿Qué decisión no se pudo tomar por eso?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por la entrada que faltó",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s20_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que la revisión por la dirección era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Quién decide en tu empresa lo que cambia el año que viene?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s20_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 20")
    for fn in (ruta, puente, estimulo, que_es, no_es, entradas_1, entradas_2, salidas_1,
               salidas_2, art_89, art_90_91, errores_1, errores_2, encargo, ficha_caso_a,
               ficha_caso_b, a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
