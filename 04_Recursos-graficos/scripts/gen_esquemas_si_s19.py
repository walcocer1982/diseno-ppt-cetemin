# -*- coding: utf-8 -*-
"""Esquemas de la sesión 19 de SI-SGCSSMA · cumplimiento legal y auditoría · 9.1.2 · 9.2

Lo legal sale del §15, verificado el 2026-09-04:
  Ley 29783 art. 43 · auditorías periódicas por AUDITORES INDEPENDIENTES, con
  participación de los trabajadores en la selección del auditor y en todas las
  fases, incluido el análisis de los resultados
  art. 44 · los resultados se comunican al comité, a los trabajadores y a sus
  organizaciones sindicales, y deben poder cambiar la política y los objetivos
  DS 005 art. 33 h) · el registro de auditorías es uno de los ocho obligatorios

Uso:  python gen_esquemas_si_s19.py
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
        ("20'", "CONEXIÓN", "Tres filas de una matriz legal, tal como están llenadas", AZUL2),
        ("45'", "ADQUISICIÓN", "Cómo se evalúa el cumplimiento y quién puede auditar", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos auditorías, una que no vio nada", MORADO),
        ("20'", "DISCUSIÓN", "Qué debería pasar con los hallazgos", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s19.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Con qué números se mide el sistema", "Y por qué uno solo no alcanza"], AZUL2),
        ("HOY", ["Cómo se comprueba lo que la ley exige", "Y quién puede venir a revisarlo"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Medir dice cómo va. Auditar dice si el sistema entero se sostiene",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_puente.png", DEST)


def estimulo():
    """Tres filas de la matriz legal, tal como estan llenadas. Solo hechos."""
    im, d = lienzo(950)
    d.rectangle([50, 50, W - 50, 760], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 190], fill=AZUL)
    izq(d, 90, 74, "MATRIZ DE REQUISITOS LEGALES", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 132, "Filas 12 a 14 de 46  ·  revisada en marzo", 38, BLANCO, ancho=W - 200)
    y = 230
    for req in ["Examen médico al término de la relación laboral",
                "Entrega del reglamento interno a cada trabajador",
                "Cuatro capacitaciones al año como mínimo"]:
        d.rounded_rectangle([90, y, W - 90, y + 150], 14, fill=GRISC)
        izq(d, 140, y + 26, req, CUE, AZUL, ancho=940)
        d.rounded_rectangle([W - 300, y + 34, W - 140, y + 116], 12, fill=TEAL)
        cen(d, W - 300, y + 52, 160, "SÍ", 54, BLANCO, True)
        y += 168
    banda(d, 790, 130, "Las 46 filas dicen «sí». No hay columna de cómo se comprobó", px=CUE)
    return guardar(im, "s19_estimulo.png", DEST)


def evaluar_cumplimiento():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("DE DÓNDE", ["De la matriz legal que se armó en la cláusula 6.1.3"], AZUL2),
        ("CADA CUÁNTO", ["Con una frecuencia que se define, no cuando toca"], TEAL),
        ("CÓMO", ["Con un método: quién comprueba, con qué evidencia"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Una columna que dice «sí» sin decir cómo no es una evaluación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_evaluar-cumplimiento.png", DEST)


def si_no_cumple():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("ACCIÓN", ["Si algo no se cumple, se toman acciones"], AZUL2),
        ("SABER", ["Se mantiene el conocimiento del estado de cumplimiento"], TEAL),
        ("EVIDENCIA", ["Y se conserva lo que prueba que se evaluó"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Saber en qué se está incumpliendo ya es parte del cumplimiento",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_si-no-cumple.png", DEST)


def nueve_uno_dos():
    im, d = lienzo(1080)
    y = tabla(d, ["ISO 45001  ·  ISO 14001", "ISO 9001"], [
        ([["9.1.2 es evaluación del cumplimiento"],
          ["9.1.2 es la satisfacción del cliente"]], "", None, None),
        ([["De los requisitos legales y otros"], ["De quien recibe el producto o servicio"]],
         "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 160, "Segundo caso del curso donde el número coincide y el asunto no. El primero fue la 8.2",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_912-dos-cosas.png", DEST)


def como_se_cita():
    im, d = lienzo(1010)
    y = comparativa(d, "NO DICE NADA", "SÍ DICE", [
        (["«Incumple la 9.1.2»"], ["«Evaluación del cumplimiento · 9.1.2 (45001)»"]),
        (["«Falla en la 8.2»"], ["«Respuesta ante emergencias · 8.2 (45001 · 14001)»"]),
        (["El número solo"], ["El asunto, la cláusula, y la norma si hace falta"]),
    ], y=50)
    banda(d, y + 20, 150, "En trinorma, el número sin el asunto puede señalar dos cosas distintas",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_como-se-cita.png", DEST)


def auditoria():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("QUÉ MIRA", ["Si el sistema se aplica y si es eficaz"], AZUL2),
        ("PROGRAMA", ["Frecuencia, métodos, responsabilidades y forma de informar"], TEAL),
        ("ALCANCE", ["Cada auditoría define qué cubre y contra qué criterios"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Sin criterios definidos, la auditoría es una visita", px=CUE)
    return guardar(im, "s19_auditoria.png", DEST)


def el_auditor():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("IMPARCIAL", ["El auditor no audita su propio trabajo"], AZUL2),
        ("INFORMA", ["Los resultados van a la dirección que corresponde"], TEAL),
        ("REGISTRO", ["El de auditorías es uno de los ocho obligatorios"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Quien administra el sistema no puede ser quien lo audita",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_el-auditor.png", DEST)


def art_43():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("INDEPENDIENTE", ["Las auditorías las hacen auditores independientes",
                           "Ley 29783, artículo 43"], AZUL2),
        ("ELIGEN", ["Los trabajadores participan en la selección del auditor"], TEAL),
        ("TODAS", ["Y en todas las fases, incluido el análisis de los resultados"], MORADO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "La ISO pide imparcialidad. La ley peruana pide independencia y participación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_art-43.png", DEST)


def art_44():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("COMUNICA", ["Los resultados van al comité y a los trabajadores",
                      "Ley 29783, artículo 44"], AZUL2),
        ("CAMBIA", ["Deben permitir cambiar la política y los objetivos"], TEAL),
        ("Y SI NO", ["Un informe que solo ve la gerencia incumple el artículo 44"], ROJO),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "La auditoría no termina en el informe: termina en lo que cambia",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_art-44.png", DEST)


def cuatro_miradas():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("1", "INSPECCIÓN", "Mira una condición o un frente. Es frecuente y es interna", AZUL2),
        ("2", "AUDITORÍA", "Mira el sistema completo contra criterios. Es periódica", TEAL),
        ("3", "FISCALIZACIÓN", "La hace la autoridad, y puede sancionar", ROJO),
        ("4", "CERTIFICACIÓN", "La hace un tercero, y solo puede retirar el certificado", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s19_cuatro-miradas.png", DEST)


def no_se_reemplazan():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("ANTICIPA", ["Un hallazgo de auditoría no es una multa", "Pero suele anticipar una"],
         AZUL2),
        ("NI UNA NI OTRA", ["Ninguna de las cuatro reemplaza a las demás"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 160, "«Ya nos auditó el cliente» no responde por lo que mira el inspector",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_no-se-reemplazan.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué falla en la evaluación y en la auditoría", "Y qué lo manda"], AZUL2),
        ("PASO 2", ["Qué pasa con los hallazgos", "Y con la matriz legal"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas pasaron por su auditoría interna",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s19_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Clínica San Rafael S.A.C.  ·  130 trabajadores  ·  prepara la renovación de su certificación",
        ["H1 · Hay matriz de requisitos legales, revisada en marzo de este año",
         "H2 · La matriz tiene una columna «cumple: sí / no». Las 46 filas dicen «sí»",
         "H3 · No hay ninguna columna que diga cómo se comprobó cada cumplimiento",
         "H4 · La auditoría interna la hizo el jefe de calidad",
         "H5 · Ese jefe de calidad es además quien administra el sistema",
         "H6 · El informe de auditoría no registró ninguna no conformidad",
         "H7 · El informe se entregó a la gerencia. El comité no lo ha visto",
         "H8 · En la última capacitación, dos enfermeras preguntaron si tenían derecho a examen médico de salida"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El examen médico de salida es una de las 46 filas que dicen «sí»",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Concretos y Agregados del Sur S.A.C.  ·  planta y despacho  ·  85 trabajadores",
        ["H1 · La auditoría la hizo una empresa externa contratada por gerencia",
         "H2 · El comité de seguridad se enteró el día que llegaron los auditores",
         "H3 · El informe trae 11 no conformidades, cada una con su evidencia y su cláusula",
         "H4 · Siete de las once son sobre requisitos legales que la matriz daba por cumplidos",
         "H5 · La matriz legal no se ha vuelto a tocar desde que llegó el informe",
         "H6 · El informe llegó hace dos meses",
         "H7 · El informe se publicó en el mural del comedor, completo",
         "H8 · Gerencia decidió no incluir los hallazgos en la revisión por la dirección «para no alarmar»"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "La auditoría sí encontró. Lo que falta es lo que viene después",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Lo que falla, con su artículo", "Y el hecho que lo prueba"], AZUL2),
        ("Y ADEMÁS", ["Qué hacer con los hallazgos", "Y qué corregir en la matriz"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Esta auditoría incumple, y decimos en qué"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo 43 o el 44"], TEAL),
        ("PREGUNTA", ["¿Quién debería estar leyendo este informe y no lo está?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por quién no vio el informe",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s19_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que una auditoría sin hallazgos era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Has visto alguna vez el informe de una auditoría de tu empresa?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s19_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 19")
    for fn in (ruta, puente, estimulo, evaluar_cumplimiento, si_no_cumple, nueve_uno_dos,
               como_se_cita, auditoria, el_auditor, art_43, art_44, cuatro_miradas,
               no_se_reemplazan, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
