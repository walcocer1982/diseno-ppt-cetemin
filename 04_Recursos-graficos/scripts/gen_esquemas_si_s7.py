# -*- coding: utf-8 -*-
"""Esquemas de la sesión 7 de SI-SGCSSMA · requisitos legales · 6.1.3 (45001 · 14001)

Lo legal sale del §15. Artículos usados aquí, todos verificados allí:
  Ley 29783 · 22 política · 29 y 30 comité y supervisor · 34 y 35 a) reglamento interno ·
  35 b) cuatro capacitaciones al año · 35 e) mapa exhibido · 37 línea base ·
  95 quién fiscaliza · 96 g) acta de infracción · 96 h) y 102 paralización

NO se reusaron `quien-fiscaliza.png` ni `escalera-de-consecuencias.png`, de la sesión
vieja: la primera cita el artículo 100, que no está verificado, y la segunda pone al
Ministerio Público como cuarto peldaño de una escalera. Ni la cita ni la escalera se
sostienen — la paralización no viene después de la multa, va cuando hay riesgo grave
e inminente. Aquí se rehacen con lo que el §15 sí respalda.

Uso:  python gen_esquemas_si_s7.py
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
        ("20'", "CONEXIÓN", "Dos filas de una matriz legal, tal como están", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué normas obligan, a quién, y qué pasa si faltan", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas que el cliente aprobó", MORADO),
        ("20'", "DISCUSIÓN", "Qué incumple cada una y quién se lo puede exigir", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s7.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué se identifica en la actividad", "Y en qué orden se controla"], AZUL2),
        ("HOY", ["Qué normas obligan a esta empresa", "Y qué pasa si no las cumple"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Los peligros los pone el trabajo. Las normas, alguien de afuera",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_puente.png", DEST)


def estimulo():
    """Dos filas de una matriz legal de una constructora. Solo hechos."""
    im, d = lienzo(950)
    d.rectangle([50, 50, W - 50, 760], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 200], fill=AZUL)
    izq(d, 90, 78, "MATRIZ DE REQUISITOS LEGALES", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 138, "Edificaciones y Acabados del Norte S.A.C.  ·  versión 1, año 2019",
        38, BLANCO, ancho=W - 200)
    y = 240
    for norma, exige in [("DS 024-2016-EM, art. 96",
                          "Seguir la jerarquía de controles en la actividad minera"),
                         ("DS 024-2016-EM, art. 26 b)",
                          "Formular el Programa Anual de Seguridad y Salud Ocupacional")]:
        d.rounded_rectangle([90, y, W - 90, y + 220], 14, fill=GRISC)
        izq(d, 130, y + 34, norma, 48, AZUL, True, ancho=W - 260)
        izq(d, 130, y + 108, exige, CUE, GRIS, ancho=W - 260)
        y += 250
    banda(d, 800, 130, "Las dos únicas filas de la matriz. La empresa levanta un edificio",
          px=CUE)
    return guardar(im, "s7_estimulo.png", DEST)


def quien_la_tiene():
    im, d = lienzo(1010)
    y = tabla(d, ["ISO 45001", "ISO 14001", "ISO 9001"], [
        ([["Requisitos legales y otros requisitos"],
          ["Obligaciones de cumplimiento"],
          ["No tiene esta cláusula"]], "", None, None),
        ([["Cláusula 6.1.3"], ["Cláusula 6.1.3"], ["Entran por la 8.2"]], "", None, None),
    ], [50, 530, 1010, W - 50], y=50)
    banda(d, y + 30, 150, "Dos de las tres la traen, y cada una la llama distinto",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_quien-la-tiene.png", DEST)


def ley_y_firmado():
    im, d = lienzo(1080)
    y = tabla(d, ["LA LEY", "LO QUE SE FIRMA"], [
        ([["Ley 29783 y sus reglamentos"],
          ["El contrato del cliente, el convenio"]], "", None, None),
        ([["Obliga aunque nadie la firme"], ["Obliga porque la empresa lo aceptó"]],
         "", None, None),
        ([["No se negocia"], ["Se negocia antes de firmar"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Los dos entran a la matriz. No entran al mismo nivel",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_ley-y-firmado.png", DEST)


def tres_verbos():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("IDENTIFICAR", ["Qué normas le aplican a esta empresa y a esta actividad"], AZUL2),
        ("ACCEDER", ["Tenerlas a la mano, no de oídas"], TEAL),
        ("ACTUALIZAR", ["Revisarlas cuando la norma cambia"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Y el resultado se guarda: la matriz es información documentada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_tres-verbos.png", DEST)


def cuando_se_usa():
    im, d = lienzo(1010)
    y = comparativa(d, "NO CUMPLE", "SÍ CUMPLE", [
        (["Sacarla cuando llega la auditoría"], ["Tenerla al planificar"]),
        (["Copiarla de otra empresa"], ["Armarla para lo que uno hace"]),
        (["Dejarla como quedó en 2019"], ["Revisarla cuando la norma cambia"]),
    ], y=50)
    banda(d, y + 20, 150, "Una matriz de hace seis años sin revisar no cumple la cláusula",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_cuando-se-usa.png", DEST)


def a_quien_obliga():
    im, d = lienzo(1080)
    y = tabla(d, ["A TODO EMPLEADOR", "SOLO A LA MINERÍA"], [
        ([["Ley 29783"], ["DS 024-2016-EM"]], "", None, None),
        ([["DS 005-2012-TR, su reglamento"],
          ["Alcanza al titular y a sus contratistas"]], "", None, None),
        ([["RM 050-2013-TR, los formatos"], ["No obliga a quien no es minero"]],
         "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Sea cual sea el rubro, la Ley 29783 obliga. El DS 024 no siempre",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_a-quien-obliga.png", DEST)


def se_suma():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("SUMA", ["El DS 024 se le suma a la ley", "No la reemplaza"], AZUL2),
        ("EXIGE", ["Ser contratista no rebaja nada", "Se cumple lo mismo, y más"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Citar una norma que no te obliga tampoco es cumplir: es no haber mirado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_se-suma.png", DEST)


def exige_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("POLÍTICA", ["Escrita, fechada y firmada", "Artículo 22"], AZUL2),
        ("BASE", ["Estudio de línea base", "Artículo 37"], TEAL),
        ("ÓRGANO", ["Comité con veinte o más; supervisor con menos",
                    "Artículos 29 y 30"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres de las seis exigencias que el inspector pide primero", px=CUE)
    return guardar(im, "s7_exige-1.png", DEST)


def exige_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("REGLAMENTO", ["Con veinte o más, y copia a cada trabajador",
                        "Artículos 34 y 35 a)"], AZUL2),
        ("CAPACITAR", ["No menos de cuatro al año", "Artículo 35 b)"], TEAL),
        ("MAPA", ["Exhibido en lugar visible", "Artículo 35 e)"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Tenerlo impreso no basta: la ley le pone una condición a cada uno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_exige-2.png", DEST)


def quien_fiscaliza():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("QUIÉN", ["La inspección del trabajo, hoy SUNAFIL", "Ley 29783, artículo 95"], AZUL2),
        ("QUÉ HACE", ["Entra sin aviso, toma fotos y planos",
                      "Y pide la información que requiera"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "La certificadora puede quitarte el certificado. Parar la obra, no",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_quien-fiscaliza.png", DEST)


def que_pasa():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("ACTA", ["Levanta acta de infracción", "Y con ella empieza la sanción · 96 g)"],
         AZUL2),
        ("MULTA", ["La sanción sale de la Ley 28806", "La de inspección del trabajo"], AMBAR),
        ("PARALIZA", ["Ante riesgo grave e inminente", "Artículos 96 h) y 102"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "La paralización no espera a la multa, es inmediata, y el jornal se paga igual",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_que-pasa.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué hechos incumplen", "Y qué artículo lo manda"], AZUL2),
        ("PASO 2", ["Qué le puede pasar por cada uno", "Y quién se lo puede exigir"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "A las dos empresas el cliente les aprobó la carpeta",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s7_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Edificaciones y Acabados del Norte S.A.C.  ·  edificio de seis pisos  ·  SUNAFIL dio tres días hábiles",
        ["H1 · La empresa tiene 34 trabajadores en planilla",
         "H2 · El inspector pidió línea base, política firmada, reglamento interno y capacitaciones",
         "H3 · Hay un supervisor designado por memorando de gerencia. No hay comité",
         "H4 · El reglamento interno está impreso en la oficina de obra; sin cargos de entrega firmados",
         "H5 · En el año se dictaron dos capacitaciones, las dos a pedido del cliente",
         "H6 · El mapa de riesgos está en la carpeta del cliente; en la obra no hay nada colgado",
         "H7 · El certificado ISO 45001 está enmarcado en la oficina, vigente hasta el año próximo",
         "H8 · La matriz legal la copiaron de otra empresa del grupo, que es minera: la mitad cita el DS 024"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El inspector llegó por una denuncia, sin aviso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Conservas y Congelados del Pacífico S.A.C.  ·  planta de congelado  ·  el informe, en 48 horas",
        ["H1 · La empresa tiene 26 trabajadores en planilla",
         "H2 · La auditoría del cliente dio 88 % y no dejó observaciones de fondo",
         "H3 · Hay comité de seguridad con cuatro miembros, designados por gerencia",
         "H4 · El 3 de septiembre un operario resbaló en la sala de fileteo; doce días de descanso médico",
         "H5 · El accidente no se investigó: no hay informe, ni medidas correctivas, ni registro",
         "H6 · El jefe de planta dice que no avisaron a nadie «porque no fue mortal»",
         "H7 · En el año se dictaron tres capacitaciones",
         "H8 · La matriz de requisitos legales se armó en 2019 y no se ha vuelto a revisar"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "El cliente pide el informe de investigación en 48 horas",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Los hechos que incumplen", "Cada uno con su artículo"], AZUL2),
        ("Y ADEMÁS", ["Qué acarrea y quién lo exige", "Y el hecho que engaña"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este hecho incumple, y este otro no"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo que lo manda"], TEAL),
        ("PREGUNTA", ["¿Cuál parecía estar bien y no lo estaba?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por el hecho que engaña",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s7_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que estar en regla era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Sabes qué normas le obligan a la empresa donde trabajas?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s7_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 7")
    for fn in (ruta, puente, estimulo, quien_la_tiene, ley_y_firmado, tres_verbos,
               cuando_se_usa, a_quien_obliga, se_suma, exige_1, exige_2, quien_fiscaliza,
               que_pasa, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
