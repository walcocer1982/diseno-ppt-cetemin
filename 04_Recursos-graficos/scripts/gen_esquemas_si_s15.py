# -*- coding: utf-8 -*-
"""Esquemas de la sesión 15 de SI-SGCSSMA · control operacional en ambiente y calidad · 8.1

NO toca residuos sólidos: eso es el bloque 2 de SI-IMPAMB, que tiene su propio
marco legal verificado. Aquí se trabaja el criterio de operación y el control de
la producción.

Lo legal citado sale del marco ambiental verificado de IMPAMB:
  Ley 28611 art. 32 · el LMP caracteriza un efluente o una emisión y es exigible
  Ley 28611 art. 31 · el ECA mide el cuerpo receptor

Uso:  python gen_esquemas_si_s15.py
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
        ("20'", "CONEXIÓN", "Dos procesos de la misma planta, uno con criterio y otro sin", AZUL2),
        ("45'", "ADQUISICIÓN", "De dónde sale el criterio y qué se controla en la producción", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas con un sistema ciego", MORADO),
        ("20'", "DISCUSIÓN", "Qué criterio falta y qué se pierde sin rastro", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s15.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Cómo se elige el control de un riesgo", "Y qué pasa cuando algo cambia"], AZUL2),
        ("HOY", ["Lo mismo, en ambiente y en calidad", "Con qué número se controla cada proceso"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "La cláusula 8.1 está en las tres normas. Hasta ahora la vimos en una",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_puente.png", DEST)


def estimulo():
    """Dos procesos de la misma planta, como estan en su informe. Solo hechos."""
    im, d = lienzo(1000)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 190], fill=AZUL)
    izq(d, 90, 74, "CONTROL DE PROCESOS", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 132, "Dos de los procesos de la planta", 38, BLANCO, ancho=W - 200)
    bloques = [("ELABORACIÓN DE YOGUR",
                ["Criterio: acidez de 0,70 a 0,90 %",
                 "Punto de medición: tanque de fermentación",
                 "Frecuencia: tres veces por turno"], AZUL2),
               ("DESCARGA DE SUERO",
                ["Criterio: —", "Punto de medición: —", "Frecuencia: —"], GRIS)]
    y = 230
    for titulo, lineas, col in bloques:
        d.rounded_rectangle([90, y, W - 90, y + 270], 14, fill=GRISC)
        d.rounded_rectangle([90, y, 130, y + 270], 14, fill=col)
        d.rectangle([110, y, 130, y + 270], fill=col)
        izq(d, 170, y + 24, titulo, 46, AZUL, True, ancho=W - 300)
        yy = y + 96
        for t in lineas:
            izq(d, 170, yy, t, CUE, GRIS, ancho=W - 300)
            yy += 58
        y += 300
    banda(d, 840, 130, "En su informe anual la empresa dice que cumple el ECA del río", px=CUE)
    return guardar(im, "s15_estimulo.png", DEST)


def ocho_uno_tres_normas():
    im, d = lienzo(1010)
    y = tabla(d, ["ISO 45001", "ISO 14001", "ISO 9001"], [
        ([["Lo que puede dañar al trabajador"], ["Lo que puede dañar al ambiente"],
          ["Lo que hace que el producto no cumpla"]], "", None, None),
        ([["El control de la jerarquía"], ["El límite de la descarga"],
          ["La especificación del cliente"]], "", None, None),
    ], [50, 530, 1010, W - 50], y=50)
    banda(d, y + 30, 150, "La misma cláusula 8.1 en las tres, y cada una controla otra cosa",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_81-tres-normas.png", DEST)


def lo_mismo():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("CRITERIOS", ["Se establece con qué condiciones debe salir el proceso"], AZUL2),
        ("CONTROL", ["Se ejecuta y se vigila según esos criterios"], TEAL),
        ("EVIDENCIA", ["Se guarda lo que da confianza de que se hizo así"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Las tres piden esto, y las tres piden controlar los cambios planificados",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_lo-mismo.png", DEST)


def de_donde_sale():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("AMBIENTE", ["Del límite que aplica a esa descarga o emisión"], AZUL2),
        ("CALIDAD", ["De la especificación acordada con el cliente"], TEAL),
        ("SEGURIDAD", ["Del control que fijó la jerarquía"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "Sin número y sin punto de medición no es criterio: es una intención",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_de-donde-sale.png", DEST)


def eca_y_lmp():
    im, d = lienzo(1080)
    y = tabla(d, ["ECA  ·  artículo 31", "LMP  ·  artículo 32"], [
        ([["Mide el cuerpo receptor"], ["Mide lo que sale del efluente o la emisión"]],
         "", None, None),
        ([["El aire, el agua o el suelo"], ["La chimenea o el punto de descarga"]],
         "", None, None),
        ([["Referente del diseño de instrumentos"],
          ["Obligación directa del titular de la fuente"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 160, "Los dos son legales. El criterio de tu descarga es el de la derecha",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_eca-y-lmp.png", DEST)


def ciclo_de_vida():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("1", "DISEÑO", "El producto o el servicio, cuando todavía se puede cambiar", AZUL2),
        ("2", "COMPRA", "La adquisición de insumos, el transporte y la entrega", TEAL),
        ("3", "USO", "Lo que pasa cuando el cliente lo usa", MORADO),
        ("4", "FINAL", "El tratamiento cuando termina su vida útil", AMBAR),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s15_ciclo-de-vida.png", DEST)


def hasta_donde():
    im, d = lienzo(1010)
    y = comparativa(d, "NO LO PIDE", "SÍ LO PIDE", [
        (["Un análisis de ciclo de vida completo"], ["Mirar todas las etapas"]),
        (["Controlar lo que no está en tu mano"], ["Decidir dónde sí puedes controlar"]),
        (["Un estudio para cada producto"], ["Que el control llegue antes de la operación"]),
    ], y=50)
    banda(d, y + 20, 150, "La perspectiva de ciclo de vida es una manera de mirar, no un estudio",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_hasta-donde.png", DEST)


def produccion_1():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("DÓNDE", ["La ISO 9001 lo detalla en la cláusula 8.5"], AZUL2),
        ("QUÉ HACER", ["Disponible qué se hace y qué resultado se espera"], TEAL),
        ("MEDIR", ["Con recursos adecuados, y en la etapa correcta"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Medir al final lo que se pudo medir en el proceso llega tarde",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_produccion-1.png", DEST)


def produccion_2():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PERSONAS", ["Competentes, y calificadas donde la tarea lo exija"], AZUL2),
        ("VALIDAR", ["Los procesos cuyo resultado no se puede verificar después"], TEAL),
        ("EL ERROR", ["Acciones para prevenir el error humano"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "Una pieza soldada y una desinfectada se ven igual por fuera: por eso se validan",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_produccion-2.png", DEST)


def identificacion():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("IDENTIFICAR", ["Qué es la salida y en qué estado está"], AZUL2),
        ("RASTREAR", ["De dónde vino y a dónde fue"], TEAL),
        ("GUARDAR", ["La información documentada que lo permite"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Sin identificación, un lote conforme y uno rechazado se mezclan",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_identificacion.png", DEST)


def preservar():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PRESERVAR", ["Que no se dañe entre que se hace y se entrega"], AZUL2),
        ("INCLUYE", ["Embalaje, almacenamiento, transporte y protección"], TEAL),
        ("SI NO", ["Se hizo bien, y llega mal. Y el cliente ve lo segundo"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "El producto no termina cuando sale de la máquina", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_preservar.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué criterio tiene cada proceso", "De dónde sale y cuál falta"], AZUL2),
        ("PASO 2", ["Qué falla en el control", "Y qué se pierde con eso"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas controlan bien un sistema y tienen ciego el otro",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s15_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Lácteos del Valle S.A.C.  ·  queso fresco y yogur  ·  80 trabajadores",
        ["H1 · Cada lote lleva código, y se puede rastrear desde el producto hasta el tanque de leche cruda",
         "H2 · La especificación de acidez del yogur está en el procedimiento, con rango y punto de medición",
         "H3 · El laboratorio mide la acidez tres veces por turno y deja registro",
         "H4 · El suero que queda del queso se descarga por el desagüe de la planta",
         "H5 · No hay criterio escrito para esa descarga: nadie sabe qué límite le aplica",
         "H6 · En su informe anual la empresa reporta que «cumple el ECA de agua del río»",
         "H7 · El río está a dos kilómetros de la planta",
         "H8 · En junio producción subió la temperatura de pasteurización. No se avisó a nadie más"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El cliente va a auditar su control de procesos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Lavandería Industrial Santa Rosa S.A.C.  ·  ropa de hospitales y hoteles  ·  45 trabajadores",
        ["H1 · Tiene autorización de vertimiento y mide su descarga cada mes, con laboratorio acreditado",
         "H2 · El criterio de operación está escrito: rango de cada parámetro y punto de muestreo",
         "H3 · La ropa hospitalaria y la hotelera se lavan en las mismas máquinas, en turnos distintos",
         "H4 · Una vez lavada, los coches de ropa no llevan identificación",
         "H5 · Se distinguen «por la vista»",
         "H6 · En agosto se entregaron a un hotel doce sábanas con marca de hospital",
         "H7 · El procedimiento exige validar el ciclo de desinfección. No se valida desde hace un año",
         "H8 · No hay registro de en qué máquina y en qué ciclo se lavó un lote"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "Un hotel devolvió un pedido y pide explicaciones",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["El criterio de cada proceso y su origen", "Y el que falta"], AZUL2),
        ("Y ADEMÁS", ["Qué falla en el control de la producción", "Y qué se pierde"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["A este proceso le falta su criterio"], AZUL2),
        ("APOYO", ["Y decimos de dónde tendría que salir"], TEAL),
        ("PREGUNTA", ["¿Qué no podrían demostrar si se lo piden mañana?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por el proceso sin criterio",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s15_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que controlar un proceso era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué proceso de tu trabajo no tiene un número que lo controle?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s15_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 15")
    for fn in (ruta, puente, estimulo, ocho_uno_tres_normas, lo_mismo, de_donde_sale,
               eca_y_lmp, ciclo_de_vida, hasta_donde, produccion_1, produccion_2,
               identificacion, preservar, encargo, ficha_caso_a, ficha_caso_b,
               a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
