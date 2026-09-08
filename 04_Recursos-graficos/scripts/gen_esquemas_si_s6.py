# -*- coding: utf-8 -*-
"""Esquemas de la sesión 6 de SI-SGCSSMA · riesgos, peligros y aspectos ambientales · 6.1

Lo legal sale del §15, verificado el 2026-09-03 contra el articulado del DS 024-2016-EM:
artículo 97 (IPERC de línea base, Anexo 8) · artículo 95 (IPERC continuo, Anexo 7) ·
artículo 96 (los cinco niveles de la jerarquía, con la redacción de la norma).

Dónde va cada forma, que aquí importa:
  · `tabla`       cuando ninguna columna está mal — solo son cosas distintas
  · `comparativa` cuando un lado SÍ incumple: pinta la izquierda de rojo, y eso afirma algo
  · `franjas`     cuando hay orden o niveles apilados

Uso:  python gen_esquemas_si_s6.py
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
        ("20'", "CONEXIÓN", "Una fila de un IPERC, tal como la llenaron", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué identifica cada norma y en qué orden se controla", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos matrices entregadas al cliente", MORADO),
        ("20'", "DISCUSIÓN", "Qué control debió venir antes", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s6.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["A quién hay que preguntarle", "Antes de decidir por él"], AZUL2),
        ("HOY", ["Qué se identifica en la actividad", "Y qué se controla primero"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Ya sabemos con quién se decide. Falta saber sobre qué",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_puente.png", DEST)


def estimulo():
    """Una fila de IPERC tal como la llenaron. Solo hechos: el juicio lo pone el estudiante."""
    im, d = lienzo(940)
    d.rectangle([50, 50, W - 50, 740], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 190], fill=AZUL)
    izq(d, 90, 76, "MATRIZ IPERC — LÍNEA BASE", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 134, "Fila 1 de 14  ·  aprobada en marzo de 2023", 38, BLANCO, ancho=W - 200)
    campos = [("TAREA", "Perforación de taladros de producción"),
              ("PELIGRO", "Caída de persona a distinto nivel"),
              ("RIESGO", "Alto"),
              ("MEDIDA DE CONTROL", "Uso obligatorio de arnés de seguridad"),
              ("RESPONSABLE", "El trabajador")]
    y = 230
    for etq, val in campos:
        d.rounded_rectangle([90, y, 470, y + 86], 12, fill=GRISC)
        cen(d, 90, y + 22, 380, etq, 40, GRIS, True)
        izq(d, 500, y + 20, val, CUE, AZUL, ancho=W - 560)
        y += 98
    banda(d, 780, 130, "Así está escrita en la matriz que entregó la empresa", px=CUE)
    return guardar(im, "s6_estimulo.png", DEST)


def tres_normas():
    im, d = lienzo(1010)
    y = tabla(d, ["ISO 45001", "ISO 14001", "ISO 9001"], [
        ([["Al trabajador"], ["Al entorno"], ["Al propio sistema"]], "", None, None),
        ([["Peligros y riesgos"], ["Aspectos e impactos"], ["Riesgos y oportunidades"]],
         "", None, None),
    ], [50, 530, 1010, W - 50], y=50)
    banda(d, y + 30, 150, "La misma cláusula 6.1 en las tres, y cada una mira otra cosa",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_tres-normas.png", DEST)


def misma_actividad():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("SST", ["El operador puede caer de la plataforma"], AZUL2),
        ("AMBIENTE", ["La máquina descarga aceite usado al suelo"], TEAL),
        ("CALIDAD", ["El sondaje puede salir desviado y repetirse"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Una sola perforadora, un solo turno, y tres cosas distintas que identificar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_misma-actividad.png", DEST)


def peligro_y_riesgo():
    im, d = lienzo(1080)
    y = tabla(d, ["PELIGRO", "RIESGO"], [
        ([["La fuente que puede causar daño"],
          ["Qué tan probable es y qué tan grave sería"]], "", None, None),
        ([["Está ahí, se identifica"], ["No está ahí, se estima"]], "", None, None),
        ([["Se elimina"], ["Se reduce"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "La misma fuente da riesgos distintos según quién y cómo haga la tarea",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_peligro-y-riesgo.png", DEST)


def columna_peligro():
    """Aqui SI hay un lado equivocado, y por eso va en comparativa."""
    im, d = lienzo(1010)
    y = comparativa(d, "NO ES UN PELIGRO", "SÍ ES UN PELIGRO", [
        (["Caída a distinto nivel"], ["Plataforma sin baranda"]),
        (["Hipoacusia del operador"], ["Ruido de la perforadora"]),
        (["Quemadura en la mano"], ["Aceite hidráulico a presión"]),
    ], y=50)
    banda(d, y + 20, 150, "A la izquierda está el daño. El peligro es lo que puede causarlo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_columna-peligro.png", DEST)


def aspecto_e_impacto():
    im, d = lienzo(1080)
    y = tabla(d, ["ASPECTO  ·  es nuestro", "IMPACTO  ·  es del entorno"], [
        ([["Lo que nuestra actividad le hace al ambiente"],
          ["El cambio que ese aspecto produce"]], "", None, None),
        ([["Se derrama aceite"], ["El suelo queda contaminado"]], "", None, None),
        ([["Se levanta polvo en la vía"], ["Baja la calidad del aire del caserío"]],
         "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Primero el aspecto, que es nuestro. Después el impacto, que es del entorno",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_aspecto-e-impacto.png", DEST)


def significativos():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("CICLO", ["Se miran todas las etapas", "De la compra al residuo"], AZUL2),
        ("PRIMERO", ["Los aspectos significativos", "Que son los que más pesan"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Si el mantenimiento se hace en la cancha, la cancha entra en la matriz",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_significativos.png", DEST)


def iperc_linea_base():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("BASE", ["El IPERC de línea base", "Anexo 8 · artículo 97"], AZUL2),
        ("MAPA", ["De esa base sale el mapa de riesgos"], TEAL),
        ("PROGRAMA", ["Los dos entran al Programa Anual de SSO"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Y la línea base se actualiza cada año", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_iperc-linea-base.png", DEST)


def iperc_continuo():
    im, d = lienzo(1230)
    y = franjas(d, [
        ("CUÁNDO", ["Al inicio de toda tarea", "Anexo 7 · artículo 95"], AZUL2),
        ("QUIÉN", ["Lo hacen los trabajadores", "La supervisión ratifica o modifica"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "Si la tarea es de más de dos, se hace en equipo y firman todos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_iperc-continuo.png", DEST)


def jerarquia():
    im, d = lienzo(1690)
    y = franjas(d, [
        ("1", ["ELIMINAR", "Cambiar el proceso de trabajo"], AZUL),
        ("2", ["SUSTITUIR", "Poner otro peligro menos peligroso"], AZUL2),
        ("3", ["INGENIERÍA", "Diseño, aislamiento, selección de equipos"], TEAL),
        ("4", ["ADMINISTRATIVOS", "Señalización, procedimientos, capacitación"], AMBAR),
        ("5", ["EPP", "Adecuado a la actividad del área"], GRIS),
    ], im, y=50, alto=250)
    banda(d, y + 20, 150, "Artículo 96 del DS 024. Es un orden, no una lista para escoger",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_jerarquia.png", DEST)


def el_atajo():
    im, d = lienzo(1010)
    y = comparativa(d, "SE SALTA LA JERARQUÍA", "LA CUMPLE", [
        (["Escribir un PETS y seguir igual"], ["Eliminar el peligro si se puede"]),
        (["Empezar por el EPP"], ["Bajar nivel por nivel"]),
        (["Capacitar sobre la curva sin peralte"], ["Peraltar la curva"]),
    ], y=50)
    banda(d, y + 20, 150, "El PETS sí es control: es el nivel 4. Y el EPP es el 5, no el 1",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_el-atajo.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué identifica cada norma", "Y qué falta o está al revés"], AZUL2),
        ("PASO 2", ["En qué nivel cae cada control", "Y cuál debió venir antes"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas entregaron su matriz IPERC y su matriz ambiental",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s6_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2010)
    y = caso(d, "CASO A", "Perforación Diamantina Andina S.A.C.  ·  entrega su matriz IPERC y su matriz ambiental",
        ["H1 · El IPERC de línea base se aprobó hace tres años y no se ha vuelto a tocar",
         "H2 · En la columna «peligro» de la primera fila dice «caída de persona a distinto nivel»",
         "H3 · Para el ruido de la perforadora, el único control anotado es «uso de tapones auditivos»",
         "H4 · Para el aceite hidráulico a presión, el control anotado es «charla de cinco minutos»",
         "H5 · El IPERC continuo del turno lo llena el supervisor y lo firma solo él",
         "H6 · No existe mapa de riesgos",
         "H7 · La matriz ambiental está en blanco, y la máquina descarga aceite usado en la plataforma",
         "H8 · El Programa Anual de SSO no incluye la línea base ni el mapa"],
        color=AZUL2, y=50, alto=200)
    banda(d, y + 24, 140, "El cliente pide la matriz IPERC y la matriz de aspectos ambientales",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Movimiento de Tierras Alto Chicama S.A.C.  ·  entrega su matriz IPERC y su matriz ambiental",
        ["H1 · El IPERC de línea base se actualizó en enero y está dentro del Programa Anual",
         "H2 · Hay mapa de riesgos, colgado en el comedor",
         "H3 · El IPERC continuo se llena al inicio de la tarea y lo firman los cuatro trabajadores",
         "H4 · En la matriz ambiental, «aspecto» dice «suelo contaminado» e «impacto» dice «derrame de combustible»",
         "H5 · El único aspecto registrado es el del grifo; el mantenimiento en la cancha no figura",
         "H6 · Para la volcadura del volquete, los controles son señalización de vías y capacitación",
         "H7 · El estudio de vías dice que la curva de la rampa no tiene peralte. No se ha corregido",
         "H8 · La matriz de calidad tiene una sola fila: «riesgo: que el cliente reclame»"],
        color=TEAL, y=50, alto=200)
    banda(d, y + 24, 140, "El cliente pide la matriz IPERC y la matriz de aspectos ambientales",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Lo que ve cada norma ahí", "Y lo que no vieron"], AZUL2),
        ("Y ADEMÁS", ["Cada control en su nivel del 96", "Y cuál debió venir antes"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este control está en el nivel que decimos"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo 96"], TEAL),
        ("PREGUNTA", ["¿Qué se pudo eliminar y se decidió señalizar?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por lo que la empresa no identificó",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s6_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que controlar un riesgo era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Cuántas veces firmaste un papel en lugar de arreglar algo?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s6_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 6")
    for fn in (ruta, puente, estimulo, tres_normas, misma_actividad, peligro_y_riesgo,
               columna_peligro, aspecto_e_impacto, significativos, iperc_linea_base,
               iperc_continuo, jerarquia, el_atajo, encargo, ficha_caso_a, ficha_caso_b,
               a_trabajar, formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
