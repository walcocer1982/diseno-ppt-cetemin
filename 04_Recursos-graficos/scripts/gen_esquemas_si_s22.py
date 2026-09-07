# -*- coding: utf-8 -*-
"""Esquemas de la sesión 22 de SI-SGCSSMA · mejora continua e integración · 10.1 y 10.3

Cierra el curso, y trae la lámina de pautas del TC2. Sus datos —tres entregables,
cuatro roles de auditor, dos horas y doce minutos de sustentación— salen del propio
`11_TC2_Indicaciones.docx`. Si el TC2 cambia, esta figura se rehace.

Lo legal sale del §15, verificado el 2026-09-04:
  Ley 29783 art. 46 · las nueve entradas de la mejora continua, entre ellas f) las
  propuestas del comité y de cualquier miembro de la empresa
  art. 45 · las auditorías y exámenes identifican las causas de la disconformidad
  art. 47 · los procedimientos se revisan periódicamente

Uso:  python gen_esquemas_si_s22.py
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
        ("20'", "CONEXIÓN", "Dos formatos del mismo turno, uno al lado del otro", AZUL2),
        ("45'", "ADQUISICIÓN", "De dónde sale la mejora y cómo se integra el sistema", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: una certificada y una que no lo está", MORADO),
        ("20'", "DISCUSIÓN", "Qué se integra primero, y las pautas del TC2", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas del curso", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s22.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué se hace cuando algo falla", "Y cómo se busca la causa"], AZUL2),
        ("HOY", ["De dónde sale lo que se mejora", "Y cómo los tres sistemas se hacen uno"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Última sesión: se cierra el círculo que abrimos en la primera",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_puente.png", DEST)


def estimulo():
    """Dos formatos del mismo turno, uno al lado del otro. Solo hechos."""
    im, d = lienzo(910)
    cen(d, 50, 60, W - 100, "Dos de los tres formatos que llena el motorizado al empezar",
        48, AZUL, True)
    mid = W / 2
    for x0, x1, titulo, lineas, col in (
            (50, mid - 20, "FORMATO DE SEGURIDAD",
             ["Fecha y hora", "Nombre y placa", "Estado de la unidad",
              "Kilometraje de salida"], AZUL2),
            (mid + 20, W - 50, "FORMATO DE CALIDAD",
             ["Fecha y hora", "Nombre y placa", "Guías asignadas",
              "Kilometraje de salida"], TEAL)):
        d.rounded_rectangle([x0, 170, x1, 720], 18, fill=GRISC)
        d.rounded_rectangle([x0, 170, x1, 292], 18, fill=col)
        d.rectangle([x0, 252, x1, 292], fill=col)
        cen(d, x0, 200, x1 - x0, titulo, 46, BLANCO, True)
        y = 350
        for t in lineas:
            cen(d, x0 + 30, y, x1 - x0 - 60, t, CUE, AZUL, False)
            y += 88
    banda(d, 752, 130, "Hay un tercero, el ambiental. Los llena el mismo motorizado", px=CUE)
    return guardar(im, "s22_estimulo.png", DEST)


def que_es_mejora():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("QUÉ MEJORA", ["La conveniencia, la adecuación y la eficacia del sistema"], AZUL2),
        ("QUÉ NO ES", ["Hacer más cosas. Es que el sistema sirva mejor"], TEAL),
        ("DÓNDE SE VE", ["En el desempeño, no en el papel que lo describe"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Cláusula 10.3, y está igual en las tres normas", px=CUE)
    return guardar(im, "s22_que-es-mejora.png", DEST)


def con_la_gente():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("CULTURA", ["Promover una cultura que apoye al sistema"], AZUL2),
        ("PARTICIPAR", ["Promover la participación de los trabajadores en la mejora"], TEAL),
        ("CONTAR", ["Comunicarles los resultados de lo que se mejoró"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Mejorar sin que la gente se entere de qué cambió no cambia la cultura",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_con-la-gente.png", DEST)


def entradas_46_1():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("a", "OBJETIVOS", "Los objetivos de seguridad y salud de la empresa", AZUL2),
        ("b", "RIESGOS", "Los resultados del IPERC y de la matriz ambiental", TEAL),
        ("c", "MEDICIÓN", "Los resultados de la supervisión y la medición", MORADO),
    ], y=50, alto=290, sep=30)
    banda(d, 990, 150, "Tres de las nueve entradas del artículo 46 de la Ley 29783",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_entradas-46-1.png", DEST)


def entradas_46_2():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("d", "INVESTIGAR", "La investigación de accidentes, enfermedades e incidentes", AZUL2),
        ("e", "AUDITAR", "Los resultados de auditorías y de la revisión por la dirección", TEAL),
        ("f", "LA GENTE", "Lo que propone el comité, o cualquier miembro de la empresa", AMBAR),
    ], y=50, alto=290, sep=30)
    banda(d, 990, 160, "El inciso f) es el que casi nunca se cumple. Quedan tres más: g), h) e i)",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_entradas-46-2.png", DEST)


def un_solo_sistema():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("LO COMÚN", ["Un contexto, un alcance, unas partes interesadas"], AZUL2),
        ("LO PROPIO", ["Tres miradas sobre la misma actividad"], TEAL),
        ("LO ÚNICO", ["Un programa anual, una auditoría, una revisión"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Tres certificados si se quiere, pero un solo sistema",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_un-solo-sistema.png", DEST)


def lo_que_permite():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("POR QUÉ SE PUEDE", ["Porque las tres comparten la estructura de alto nivel",
                              "Es lo que vimos en la sesión 1"], AZUL2),
        ("UNA POLÍTICA", ["Que cubra calidad, ambiente y seguridad", "Firmada una sola vez"],
         TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "El curso empezó con esa estructura. Aquí se ve para qué servía",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_lo-que-permite.png", DEST)


def integrar_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SE PARTE", ["De lo que ya existe, no de una plantilla nueva"], AZUL2),
        ("SE UNE", ["Un procedimiento sirve a las tres si el requisito es común"], TEAL),
        ("SE AÑADE", ["Si una norma pide algo propio, se añade el apartado"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Se añade el apartado, no otro documento con otra numeración",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_integrar-1.png", DEST)


def integrar_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SE ELIMINA", ["Lo duplicado: dos matrices legales son una matriz mal hecha"], AZUL2),
        ("SE UNIFICA", ["La numeración y el control de versiones"], TEAL),
        ("SE DISEÑA", ["El registro una vez, con las columnas de las tres"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Un dato que se pide dos veces se contradice a sí mismo tarde o temprano",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_integrar-2.png", DEST)


def falla_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SOLO PAPEL", ["Se integran los documentos y no las decisiones"], ROJO),
        ("TRES ISLAS", ["Tres responsables que no se hablan entre ellos"], ROJO),
        ("SE CONTRADICE", ["Un manual integrado con anexos que dicen cosas distintas"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres formas de tener un sistema integrado solo en la portada", px=CUE)
    return guardar(im, "s22_falla-1.png", DEST)


def falla_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("PRESTADO", ["Copiar la documentación de otra empresa y cambiarle el logo"], ROJO),
        ("PARA LA FOTO", ["Integrar solo para la auditoría de certificación"], ROJO),
        ("SE NOTA", ["La integración se ve en la reunión, no en la carpeta"], AZUL2),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Si los tres siguen reuniéndose por separado, no hay integración",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_falla-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["De dónde salió lo que mejoraron", "Y qué entradas del 46 no usan"], AZUL2),
        ("PASO 2", ["Qué integrarían primero", "Y qué se elimina o se unifica"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Una empresa certificada y una que no lo está",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s22_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Muebles y Melamina del Sur S.A.C.  ·  75 trabajadores  ·  certificada en las tres normas",
        ["H1 · Está certificada en las tres normas desde hace dos años",
         "H2 · Tiene un manual integrado del sistema, de 180 páginas",
         "H3 · El manual remite a tres anexos: calidad, ambiente y seguridad",
         "H4 · El anexo de calidad cierra las no conformidades en 15 días; el de seguridad, en 30",
         "H5 · Hay tres matrices de requisitos legales, con filas repetidas entre ellas",
         "H6 · Cada sistema tiene su reunión mensual, con actas separadas",
         "H7 · La mejora del año son ocho acciones; siete salieron de la auditoría de certificación",
         "H8 · Ninguna acción del año salió de una propuesta de un trabajador"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "La auditoría de seguimiento llega el mes que viene",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Courier y Distribución Expreso Andino S.A.C.  ·  140 trabajadores, 60 motorizados  ·  sin certificar",
        ["H1 · Tiene los tres sistemas armados por separado, cada uno con su documentación",
         "H2 · El motorizado llena tres formatos distintos al inicio del turno, uno por sistema",
         "H3 · Dos de los tres formatos piden los mismos datos",
         "H4 · Este año se registraron 22 propuestas de mejora hechas por los trabajadores",
         "H5 · Catorce de esas 22 se implementaron",
         "H6 · Las catorce están registradas con su resultado",
         "H7 · Las propuestas salieron del buzón y de las reuniones de los motorizados",
         "H8 · Gerencia dice que integrar «es un tema de la certificación, y no estamos en eso»"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "No está certificada, y quiere ordenar su sistema",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["El origen de cada mejora del año", "Y las entradas que no usan"], AZUL2),
        ("Y ADEMÁS", ["Qué integrarían primero", "Y qué documento sobra"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Esta empresa mejora desde aquí, y no desde allá"], AZUL2),
        ("APOYO", ["Y lo sostenemos en las nueve entradas del artículo 46"], TEAL),
        ("PREGUNTA", ["¿Cuál de las dos tiene un sistema, y cuál tiene una carpeta?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por el origen de la mejora",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_discusion.png", DEST)


def pautas_tc2():
    """Los datos salen de 11_TC2_Indicaciones.docx. No se inventan aqui."""
    im, d = lienzo(1400)
    y = franjas(d, [
        ("ENTREGAN", ["El informe de auditoría interna, el anexo con la hoja de trabajo",
                      "Y el PPT de sustentación"], AZUL2),
        ("ROLES", ["Auditor de desempeño, de operación, de cumplimiento y líder",
                   "Uno por integrante"], TEAL),
        ("TIEMPO", ["2 horas de trabajo autónomo, en equipos de 4",
                    "Sustentación de 12 minutos y 8 de preguntas"], MORADO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Trabajo colaborativo 2 · sobre las cláusulas 8, 9 y 10",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_pautas-tc2.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["En la primera sesión pensaba que un sistema de gestión era…"], GRIS),
        ("AHORA", ["Después de veintidós sesiones, pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué te vas a llevar de este curso al trabajo del lunes?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Se escribe, no se dice. Es el cierre del curso", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s22_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 22")
    for fn in (ruta, puente, estimulo, que_es_mejora, con_la_gente, entradas_46_1,
               entradas_46_2, un_solo_sistema, lo_que_permite, integrar_1, integrar_2,
               falla_1, falla_2, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, pautas_tc2, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
