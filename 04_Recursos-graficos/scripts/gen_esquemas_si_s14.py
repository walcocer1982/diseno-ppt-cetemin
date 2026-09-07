# -*- coding: utf-8 -*-
"""Esquemas de la sesión 14 de SI-SGCSSMA · jerarquía y gestión del cambio · 8.1.2–8.1.3

La S6 presentó los cinco niveles del artículo 96. Aquí NO se repiten: se aplican.
Lo nuevo es la diferencia de redacción entre la ISO y el DS 024, cómo se elige y
se combina, el riesgo residual, y la gestión del cambio.

Lo legal sale del §15:
  DS 024-2016-EM art. 96 · los cinco niveles, con la redacción de la norma
  Ley 29783 art. 49 c) · identificar las modificaciones en las condiciones de
  trabajo y disponer las medidas — el anclaje nacional de la cláusula 8.1.3

Uso:  python gen_esquemas_si_s14.py
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
        ("20'", "CONEXIÓN", "Un formato de gestión del cambio, tal como se llenó", AZUL2),
        ("45'", "ADQUISICIÓN", "Cómo se elige el control y qué cambios se evalúan antes", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas cambiaron algo y se les fue de las manos", MORADO),
        ("20'", "DISCUSIÓN", "Qué control correspondía y qué riesgo quedó", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s14.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué documento controla cada tarea", "Estándar, PETS, ATS o permiso"], AZUL2),
        ("HOY", ["Cómo se elige el control que va dentro", "Y qué pasa cuando algo cambia"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "El documento es el envase. El control es lo que va adentro",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_puente.png", DEST)


def estimulo():
    """El formato de gestion del cambio tal como se lleno. Solo hechos."""
    im, d = lienzo(1000)
    d.rectangle([50, 50, W - 50, 810], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "FORMATO DE GESTIÓN DEL CAMBIO", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Ampliación de racks: de dos a cuatro niveles", 38, BLANCO, ancho=W - 200)
    campos = [("QUÉ CAMBIA", "Altura de almacenaje"),
              ("MOTIVO", "Más capacidad en el mismo metraje"),
              ("TIEMPOS", "Sin variación"),
              ("COSTOS", "Se recupera en ocho meses"),
              ("APRUEBA", "El jefe de operaciones")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 94], 12, fill=GRISC)
        cen(d, 90, y + 25, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 23, val, CUE, AZUL, ancho=W - 560)
        y += 106
    banda(d, 850, 130, "El formato no tiene más casillas", px=CUE)
    return guardar(im, "s14_estimulo.png", DEST)


def niveles_3_y_4():
    im, d = lienzo(1080)
    y = tabla(d, ["ISO 45001  ·  8.1.2", "DS 024  ·  artículo 96"], [
        ([["3 · Ingeniería y reorganización del trabajo"],
          ["3 · Controles de ingeniería"]], "", None, None),
        ([["4 · Administrativos, incluida la formación"],
          ["4 · Señalización, alertas y controles administrativos"]], "", None, None),
        ([["5 · Equipos de protección personal"],
          ["5 · Equipos de protección personal"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Los cinco niveles y el orden son los mismos. Cambia qué entra en cada uno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_niveles-3-4.png", DEST)


def reorganizar():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("TURNOS", ["Cambiar el horario en que se hace la tarea"], AZUL2),
        ("SECUENCIA", ["Cambiar el orden de los pasos, o dónde se hace"], TEAL),
        ("QUIÉN", ["Cambiar quién la hace, o cuántos la hacen"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Reorganizar el trabajo es nivel 3, no nivel 4: pesa más que una charla",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_reorganizar.png", DEST)


def como_se_elige():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("ARRIBA", ["Se empieza por el nivel 1: eliminar"], AZUL2),
        ("BAJA", ["Solo se baja si el nivel de arriba no se puede"], TEAL),
        ("COMBINA", ["Un mismo riesgo puede llevar controles de varios niveles"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Bajar sin haber probado el de arriba es saltarse la jerarquía",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_como-se-elige.png", DEST)


def no_se_puede():
    im, d = lienzo(1010)
    y = comparativa(d, "NO ES «NO SE PUEDE»", "SÍ LO ES", [
        (["Cuesta caro"], ["No existe la tecnología que lo haga"]),
        (["Nos cambia la rutina"], ["El costo supera el valor de la obra, y se demuestra"]),
        (["Nadie lo ha hecho antes"], ["Introduce un peligro peor que el que quita"]),
    ], y=50)
    banda(d, y + 20, 150, "Descartar un nivel se sustenta y se escribe. No se supone",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_no-se-puede.png", DEST)


def residual():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("QUEDA", ["Es el riesgo que sobra después del control"], AZUL2),
        ("SE MIDE", ["Se vuelve a evaluar con el control puesto, no antes"], TEAL),
        ("SE DICE", ["Se declara y se comunica a quien hace la tarea"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Ningún control lo deja en cero, y no hace falta que lo deje",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_residual.png", DEST)


def residual_alto():
    im, d = lienzo(1010)
    y = comparativa(d, "MAL CERRADO", "BIEN CERRADO", [
        (["Se evaluó antes de poner el control"], ["Se evalúa con el control funcionando"]),
        (["Quedó alto y se dio por hecho"], ["Quedó alto, y se cambió el control"]),
        (["Solo lo sabe el que llenó la matriz"], ["Lo sabe el que hace la tarea"]),
    ], y=50)
    banda(d, y + 20, 150, "Lo que no se declara, el trabajador lo descubre solo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_residual-alto.png", DEST)


def gestion_del_cambio():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("ANTES", ["Se evalúa antes de implementarlo, no después"], AZUL2),
        ("TODOS", ["Los cambios permanentes y también los temporales"], TEAL),
        ("LA LEY", ["Identificar las modificaciones en las condiciones de trabajo",
                    "Ley 29783, artículo 49 c)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "En el Perú no es buena práctica importada: ya es obligación del empleador",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_gestion-del-cambio.png", DEST)


def despues_del_cambio():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("MÉTODO", ["La ISO 45001 le pone forma", "Cláusula 8.1.3"], AZUL2),
        ("DESPUÉS", ["Se revisan las consecuencias", "Las que no se previeron"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Un cambio bien evaluado también sorprende. Por eso se vuelve a mirar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_despues.png", DEST)


def que_cambios_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SUSTANCIA", ["Un insumo, un producto o un químico nuevo"], AZUL2),
        ("EQUIPO", ["Una máquina o una tecnología distinta"], TEAL),
        ("PROCESO", ["Cambia el método, la distribución o los turnos"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres de los seis cambios que se evalúan antes de hacerlos", px=CUE)
    return guardar(im, "s14_que-cambios-1.png", DEST)


def que_cambios_2():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("LA LEY", ["Un requisito legal nuevo o modificado"], AZUL2),
        ("LO APRENDIDO", ["Lo que dejó un incidente o su investigación"], TEAL),
        ("LA GENTE", ["Personal nuevo o reubicado: cambia quién hace la tarea"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "El último es el que más se olvida, y el que más rápido pasa",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_que-cambios-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué cambió y quién debió mirarlo", "Y qué peligro nuevo apareció"], AZUL2),
        ("PASO 2", ["En qué nivel cae el control puesto", "Y cuál correspondía"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas hicieron un cambio y algo se les fue de las manos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s14_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Artes Gráficas del Litoral S.A.C.  ·  imprenta de empaques  ·  55 trabajadores",
        ["H1 · En marzo se cambió el solvente de limpieza de rodillos, para bajar costos",
         "H2 · El cambio lo decidió compras; seguridad se enteró cuando llegó el primer lote",
         "H3 · No se hizo IPERC del solvente nuevo ni se pidió su hoja de datos de seguridad",
         "H4 · El solvente nuevo es más volátil: el olor llega hasta la zona de acabados",
         "H5 · La cabina de extracción localizada se diseñó para el solvente anterior y no se tocó",
         "H6 · A los operarios se les dio respirador nuevo y una charla de veinte minutos",
         "H7 · Dos operarios de acabados dicen que terminan el turno con dolor de cabeza. Sin registro",
         "H8 · El procedimiento de limpieza de rodillos sigue nombrando el solvente anterior"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El cambio ya está hecho y el solvente ya está en planta",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Centro de Distribución Andina S.A.C.  ·  almacén  ·  70 trabajadores",
        ["H1 · En enero los racks pasaron de dos a cuatro niveles, para almacenar más",
         "H2 · Hay un procedimiento de gestión del cambio, y el formato se llenó y se firmó",
         "H3 · El formato evalúa tiempos, costos y capacidad de almacenaje",
         "H4 · No tiene ninguna casilla sobre peligros nuevos ni sobre el IPERC",
         "H5 · Con el cuarto nivel, el montacargas trabaja al límite de su altura de elevación",
         "H6 · La medida que se tomó fue prohibir por escrito elevar con la carga inclinada",
         "H7 · El estudio del proveedor recomienda un montacargas de mayor alcance. No se compró",
         "H8 · En dos meses cayeron tres pallets desde el cuarto nivel. Ninguno alcanzó a nadie"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "El cambio se evaluó, y el formato está firmado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["El cambio y el peligro que trajo", "Con quién debió evaluarlo"], AZUL2),
        ("Y ADEMÁS", ["El control puesto y el que tocaba", "Y el riesgo que queda"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este control está en el nivel que decimos"], AZUL2),
        ("APOYO", ["Y decimos cuál correspondía, con lo ya identificado"], TEAL),
        ("PREGUNTA", ["¿Qué riesgo queda hoy, con el control que hay?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por quién debió mirar el cambio",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s14_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que un cambio pequeño era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué cambió este año donde trabajas, y quién lo evaluó?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s14_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 14")
    for fn in (ruta, puente, estimulo, niveles_3_y_4, reorganizar, como_se_elige,
               no_se_puede, residual, residual_alto, gestion_del_cambio,
               despues_del_cambio, que_cambios_1, que_cambios_2, encargo,
               ficha_caso_a, ficha_caso_b, a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
