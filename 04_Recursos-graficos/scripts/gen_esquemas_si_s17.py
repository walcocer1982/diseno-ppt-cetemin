# -*- coding: utf-8 -*-
"""Esquemas de la sesión 17 de SI-SGCSSMA · emergencias · 8.2 (45001 · 14001)

Lo legal sale del §15, verificado el 2026-09-04:
  DS 005-2012-TR art. 83 a) información y coordinación a todas las personas ·
  b) informar a autoridades, VECINDAD y servicios de intervención · c) primeros
  auxilios, extinción y evacuación a TODAS LAS PERSONAS QUE SE ENCUENTREN EN EL
  LUGAR DE TRABAJO · d) formación en todos los niveles, con ejercicios periódicos
  DS 005 art. 33 g) · el registro de simulacros es obligatorio

Uso:  python gen_esquemas_si_s17.py
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
        ("20'", "CONEXIÓN", "La carátula de un plan de emergencias, tal como está", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué exige la 8.2, a quiénes alcanza y para qué el simulacro", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos planes y la gente que dejan fuera", MORADO),
        ("20'", "DISCUSIÓN", "Qué probaría el próximo simulacro", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s17.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué se le exige a quien entra a trabajar", "Y quién responde por él"], AZUL2),
        ("HOY", ["Qué pasa cuando algo se sale de control", "Y a quién hay que sacar de ahí"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Todo lo anterior es para que esto no pase. Esto es para cuando pasa",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_puente.png", DEST)


def estimulo():
    """La caratula del plan tal como esta. Solo hechos."""
    im, d = lienzo(1000)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "PLAN DE EMERGENCIAS", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Estación de servicios  ·  operación 24 horas", 38, BLANCO, ancho=W - 200)
    campos = [("APROBADO", "Marzo de 2022"),
              ("JEFE DE BRIGADA", "El que figura salió en 2023"),
              ("ÚLTIMO SIMULACRO", "Sismo, hace catorce meses"),
              ("SIMULACRO DE DERRAME", "—"),
              ("SIMULACRO DE INCENDIO", "—")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 590, y + 94], 12, fill=GRISC)
        cen(d, 90, y + 25, 500, etq, 40, GRIS, True)
        izq(d, 620, y + 23, val, CUE, AZUL, ancho=W - 680)
        y += 106
    banda(d, 850, 130, "A media cuadra hay un mercado y un colegio", px=CUE)
    return guardar(im, "s17_estimulo.png", DEST)


def que_pide_82():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("PREPARAR", ["Procesos para prepararse y responder, incluida la primera ayuda"], AZUL2),
        ("PROBAR", ["Ejercicios periódicos de la respuesta planificada"], TEAL),
        ("REVISAR", ["Evaluar después y ajustar el proceso"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "Y se revisa sobre todo cuando la emergencia ocurrió de verdad",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_que-pide-82.png", DEST)


def ocho_dos_en_9001():
    im, d = lienzo(1010)
    y = tabla(d, ["ISO 45001  ·  ISO 14001", "ISO 9001"], [
        ([["8.2 es preparación y respuesta ante emergencias"],
          ["8.2 son los requisitos para los productos y servicios"]], "", None, None),
        ([["La tienen las dos"], ["Aquí el mismo número dice otra cosa"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 160, "Es el caso donde citar «la 8.2» a secas confunde: hay que decir la norma",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_82-en-9001.png", DEST)


def que_es_emergencia():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SE SALE", ["Un evento que sale del control de la operación normal"], AZUL2),
        ("DAÑA", ["Puede dañar a personas, al ambiente o a las instalaciones"], TEAL),
        ("YA ESTABA", ["Sale de lo que identificaron el IPERC y la matriz ambiental"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "No toda emergencia es un accidente, ni todo accidente es una emergencia",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_que-es-emergencia.png", DEST)


def ejemplos():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("1", "INCENDIO", "Y el amago, que es el que más veces ocurre", AZUL2),
        ("2", "DERRAME", "De combustible, de químico, de aceite", TEAL),
        ("3", "SISMO", "Y lo que viene después: colapso, atrapamiento", MORADO),
        ("4", "DE AFUERA", "Lo que llega del vecino, del clima o de la vía", AMBAR),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s17_ejemplos.png", DEST)


def art_83_1():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("INFORMA", ["Información, comunicación interna y coordinación",
                     "DS 005, artículo 83 a)"], AZUL2),
        ("AFUERA", ["A las autoridades, a la vecindad y a los servicios de intervención",
                    "Artículo 83 b)"], TEAL),
        ("ATIENDE", ["Primeros auxilios, asistencia médica, extinción y evacuación",
                     "Artículo 83 c)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "El inciso b) mira hacia afuera, y casi ningún plan lo contempla",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_art-83-1.png", DEST)


def todas_las_personas():
    im, d = lienzo(1010)
    y = comparativa(d, "NO DICE ESO", "DICE ESTO", [
        (["«Todos los trabajadores»"], ["«Todas las personas que se encuentren»"]),
        (["Los de planilla"], ["El cliente, el huésped, el proveedor, la visita"]),
        (["Los que hicieron la inducción"], ["Los que estén ahí cuando suene la alarma"]),
    ], y=50)
    banda(d, y + 20, 160, "Artículo 83 c). La formación, además, en todos los niveles — 83 d)",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_todas-las-personas.png", DEST)


def simulacro():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PRUEBA", ["Lo que el plan dice, no lo que sabemos que sale bien"], AZUL2),
        ("MIDE", ["Se cronometra y se registra", "Es uno de los ocho registros obligatorios"],
         TEAL),
        ("CAMBIA", ["Lo que falló se corrige en el plan"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "Participan también los contratistas y quien esté de visita ese día",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_simulacro.png", DEST)


def simulacro_teatro():
    im, d = lienzo(1010)
    y = comparativa(d, "FUE TEATRO", "FUE EJERCICIO", [
        (["El acta dice «todo conforme»"], ["El acta lista lo que falló"]),
        (["Se avisó la hora exacta"], ["Se probó el turno de noche también"]),
        (["El plan quedó igual"], ["El plan cambió después"]),
    ], y=50)
    banda(d, y + 20, 160, "Un simulacro sin hallazgos casi siempre significa que no se buscó ninguno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_simulacro-teatro.png", DEST)


def errores_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("COPIADO", ["Nombra áreas o equipos que esta empresa no tiene"], ROJO),
        ("GENTE", ["Brigadistas que ya no trabajan aquí"], ROJO),
        ("EQUIPOS", ["Extintores bien señalizados y con la carga vencida"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres cosas que se ven abriendo el plan y mirando la pared", px=CUE)
    return guardar(im, "s17_errores-1.png", DEST)


def errores_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("LA RUTA", ["Termina en una puerta cerrada con llave"], ROJO),
        ("LA PERSONA", ["El único que sabe el procedimiento está de vacaciones"], ROJO),
        ("EL VECINO", ["Nadie le avisó de qué hay adentro"], ROJO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "Estos tres solo se ven caminando la ruta y preguntando afuera",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_errores-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué exige la ley que el plan no cubre", "Y a quién deja fuera"], AZUL2),
        ("PASO 2", ["Qué probaría el próximo simulacro", "Y qué cambiaría del plan"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Los dos tienen plan. Uno viejo y uno impecable",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s17_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Estación de Servicios San Cristóbal S.A.C.  ·  combustible 24 horas  ·  18 trabajadores",
        ["H1 · Los 18 trabajadores se reparten en tres turnos",
         "H2 · Hay plan de emergencias, aprobado hace cuatro años",
         "H3 · El plan nombra como jefe de brigada a una persona que dejó la empresa en 2023",
         "H4 · El último simulacro fue de sismo, hace catorce meses",
         "H5 · Nunca se ha simulado un derrame de combustible ni un amago de incendio",
         "H6 · Los extintores están señalizados; dos tienen la tarjeta de recarga vencida",
         "H7 · El plan no dice a quién se avisa fuera de la estación",
         "H8 · A media cuadra hay un mercado y un colegio"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "La municipalidad pidió revisar el plan",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Hotel Villa del Sol S.A.C.  ·  55 trabajadores  ·  capacidad para 120 huéspedes",
        ["H1 · Hay plan de evacuación, actualizado en enero, con planos por piso",
         "H2 · Se hacen dos simulacros al año, con cronómetro y con acta",
         "H3 · En los simulacros participa solo el personal. Nunca los huéspedes",
         "H4 · El acta del último dice «se cumplió el tiempo previsto»",
         "H5 · Esa acta no lista ningún hallazgo",
         "H6 · Las instrucciones de evacuación de las habitaciones están solo en español",
         "H7 · La salida de emergencia del segundo piso da a un pasillo con carros de limpieza",
         "H8 · El cuarenta por ciento de los huéspedes del último trimestre fueron extranjeros"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "La cadena va a auditar su preparación ante emergencias",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Lo que la ley exige y el plan no cubre", "Con su artículo"], AZUL2),
        ("Y ADEMÁS", ["A quién deja fuera", "Y qué probaría el próximo simulacro"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este plan deja fuera a estas personas"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo que las nombra"], TEAL),
        ("PREGUNTA", ["Si suena la alarma hoy, ¿quién no sabe qué hacer?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por quién queda fuera",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s17_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que un simulacro servía para…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Sabes por dónde saldrías del sitio donde trabajas?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s17_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 17")
    for fn in (ruta, puente, estimulo, que_pide_82, ocho_dos_en_9001, que_es_emergencia,
               ejemplos, art_83_1, todas_las_personas, simulacro, simulacro_teatro,
               errores_1, errores_2, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
