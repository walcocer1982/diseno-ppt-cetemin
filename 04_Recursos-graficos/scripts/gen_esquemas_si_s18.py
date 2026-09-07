# -*- coding: utf-8 -*-
"""Esquemas de la sesión 18 de SI-SGCSSMA · seguimiento y medición · 9.1.1

Lo legal sale del §15, verificado el 2026-09-04:
  DS 005-2012-TR art. 85 · los indicadores se adecúan al tamaño, la actividad y
  los objetivos, y se define quién rinde cuentas · art. 86 a) las mediciones se
  basan en los peligros identificados · art. 87 b) la medición NO puede basarse
  exclusivamente en estadísticas de accidentes · 87 d) debe decir si las medidas
  se aplican y son eficaces
  DS 024-2016-EM art. 37 · las fórmulas de los tres índices y el factor 1 000 000

Uso:  python gen_esquemas_si_s18.py
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
        ("20'", "CONEXIÓN", "Un tablero de seguridad, tal como se presentó", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué se mide, con qué indicadores y por qué no basta uno", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas y sus números", MORADO),
        ("20'", "DISCUSIÓN", "Si los números sostienen lo que concluyen", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s18.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Cómo se controla la operación", "Y cómo se responde si algo pasa"], AZUL2),
        ("HOY", ["Cómo se sabe si todo eso funciona", "Y con qué números se demuestra"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Empieza la verificación: la cláusula 9 mira si lo hecho sirvió",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_puente.png", DEST)


def estimulo():
    """El tablero tal como se presento. Solo hechos."""
    im, d = lienzo(1010)
    d.rectangle([50, 50, W - 50, 810], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "TABLERO DE SEGURIDAD", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Acumulado del año  ·  presentado a gerencia", 38, BLANCO, ancho=W - 200)
    filas = [("ÍNDICE DE FRECUENCIA", "0,00"),
             ("ÍNDICE DE SEVERIDAD", "0,00"),
             ("ACCIDENTABILIDAD", "0,00")]
    y = 250
    for etq, val in filas:
        d.rounded_rectangle([90, y, W - 90, y + 130], 14, fill=GRISC)
        izq(d, 140, y + 40, etq, 48, AZUL, True, ancho=800)
        cen(d, W - 420, y + 30, 300, val, 66, AZUL, True)
        y += 150
    banda(d, 720, 130, "El tablero tiene tres filas. Es todo lo que se mide", px=CUE)
    banda(d, 862, 130, "En el mismo periodo el tópico atendió nueve cortes",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_estimulo.png", DEST)


def nueve_uno_uno():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("QUÉ", ["Qué necesita seguimiento y medición"], AZUL2),
        ("MÉTODO", ["Con qué método, para que el resultado sea válido"], TEAL),
        ("CRITERIO", ["Contra qué se compara el desempeño"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres decisiones que se toman antes de medir nada", px=CUE)
    return guardar(im, "s18_911.png", DEST)


def evidencia():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("CUÁNDO", ["Cuándo se mide, y cuándo se analiza y evalúa"], AZUL2),
        ("EVIDENCIA", ["Se conserva la información documentada"], TEAL),
        ("EQUIPOS", ["Los de medición se calibran o se verifican"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Medir con un equipo sin calibrar es opinar con decimales",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_evidencia.png", DEST)


def reactivo_proactivo():
    im, d = lienzo(1080)
    y = tabla(d, ["REACTIVO", "PROACTIVO"], [
        ([["Mide lo que ya pasó"], ["Mide lo que se hace para que no pase"]], "", None, None),
        ([["Accidentes, días perdidos"], ["Inspecciones hechas, hallazgos cerrados"]],
         "", None, None),
        ([["Llega tarde"], ["Permite corregir a tiempo"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Un tablero necesita los dos, y el que casi siempre falta es el segundo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_reactivo-proactivo.png", DEST)


def ejemplos_proactivos():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("HACER", ["Inspecciones hechas sobre las programadas"], AZUL2),
        ("CERRAR", ["Hallazgos cerrados dentro del plazo"], TEAL),
        ("MIRAR", ["Permisos verificados en campo, observaciones de conducta"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Todos se pueden medir este mes, y todos se pueden corregir este mes",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_ejemplos-proactivos.png", DEST)


def indices():
    im, d = lienzo(1400)
    y = filas_letra(d, [
        ("IF", "FRECUENCIA", "Accidentes × factor ÷ horas-hombre trabajadas", AZUL2),
        ("IS", "SEVERIDAD", "Días perdidos o cargados × factor ÷ horas-hombre", TEAL),
        ("IA", "ACCIDENTABILIDAD", "Frecuencia × severidad ÷ 1000", MORADO),
    ], y=50, alto=290, sep=30)
    banda(d, y + 20, 150, "En minería el factor es un millón — DS 024, artículo 37",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_indices.png", DEST)


def factores():
    im, d = lienzo(1010)
    y = comparativa(d, "NO SE PUEDE", "SÍ SE PUEDE", [
        (["Cambiar el factor a mitad de año"], ["Usar el mismo factor todo el periodo"]),
        (["Comparar dos series con factores distintos"], ["Recalcular la serie completa"]),
        (["Estimar las horas-hombre"], ["Tomarlas del registro real de horas"]),
    ], y=50)
    banda(d, y + 20, 160, "Pasar de 200 000 a un millón multiplica el índice por cinco, sin que pase nada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_factores.png", DEST)


def no_alcanza():
    im, d = lienzo(1400)
    y = franjas(d, [
        ("NO SOLO", ["La medición no puede basarse exclusivamente en estadísticas de accidentes",
                     "DS 005, artículo 87 b)"], ROJO),
        ("SÍ DEBE", ["Decir si las medidas de prevención se aplican y son eficaces",
                     "Artículo 87 d)"], AZUL2),
        ("Y SALE DE", ["Los peligros y riesgos que ya se identificaron",
                       "Artículo 86 a)"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "No es criterio del instructor: está escrito en el reglamento",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_no-alcanza.png", DEST)


def cero_accidentes():
    im, d = lienzo(1010)
    y = comparativa(d, "NO PRUEBA NADA", "SÍ DICE ALGO", [
        (["Cero accidentes con cero inspecciones"], ["Cero accidentes con el plan cumplido"]),
        (["El índice bajó y nadie sabe por qué"], ["El índice bajó y se sabe qué cambió"]),
        (["Un mes sin reportes"], ["Un mes con reportes y hallazgos cerrados"]),
    ], y=50)
    banda(d, y + 20, 160, "Cero accidentes con cero inspecciones no es un buen mes: es un mes sin mirar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_cero-accidentes.png", DEST)


def errores_1():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PRESTADO", ["Copiar el indicador de otra empresa",
                      "El artículo 85 pide adecuarlo a la propia"], ROJO),
        ("MOVIDO", ["Cambiar la fórmula a mitad de año y comparar igual"], ROJO),
        ("MAL CONTADO", ["Meter en el índice de frecuencia todo accidente registrado"], ROJO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 140, "Tres formas de que el número diga algo que no ocurrió", px=CUE)
    return guardar(im, "s18_errores-1.png", DEST)


def errores_2():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("TARDE", ["Medir recién al cierre, cuando ya no se corrige"], ROJO),
        ("MUDO", ["Un tablero que nadie mira ni discute en el comité"], ROJO),
        ("SIN DUEÑO", ["Nadie rinde cuentas de ese indicador",
                       "DS 005, artículo 85"], ROJO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "El artículo 85 pide definir la obligación de rendir cuentas, por nivel",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_errores-2.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué mide el tablero y qué no", "Y qué artículo obliga a medirlo"], AZUL2),
        ("PASO 2", ["Si los números sostienen la conclusión", "Y dos indicadores proactivos"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas presentaron sus números y sacaron una conclusión",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s18_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Avícola San Jacinto S.A.C.  ·  planta de beneficio y granjas  ·  210 trabajadores",
        ["H1 · El tablero mensual trae índice de frecuencia, índice de severidad y accidentabilidad",
         "H2 · En lo que va del año, el índice de frecuencia es cero",
         "H3 · Se hicieron 2 inspecciones internas de las 12 programadas",
         "H4 · Hay 14 hallazgos de inspección abiertos",
         "H5 · El más antiguo de esos hallazgos es de hace siete meses",
         "H6 · No se mide ninguna otra cosa: el tablero tiene tres filas",
         "H7 · La gerencia felicitó al área por «el mejor año en seguridad»",
         "H8 · En ese mismo periodo el tópico atendió 9 cortes en la sala de deshuese"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El tablero se presentó a la gerencia y al comité",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Vigilancia y Seguridad Patrimonial S.A.C.  ·  340 vigilantes en 46 puestos",
        ["H1 · Mide el índice de frecuencia y se lo reporta a cada cliente",
         "H2 · Hasta junio calculó el índice con factor 200 000",
         "H3 · Desde julio usa factor 1 000 000",
         "H4 · El informe anual presenta los doce meses en un solo gráfico de línea",
         "H5 · El gráfico muestra una subida fuerte a partir de julio",
         "H6 · El informe concluye que «la siniestralidad se disparó en el segundo semestre»",
         "H7 · Las horas-hombre de julio a diciembre las estimó administración",
         "H8 · No hay registro de horas por puesto, y no se mide ningún indicador proactivo"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "El informe ya se entregó a los 46 clientes",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Lo que el tablero mide y lo que no", "Con el artículo que lo obliga"], AZUL2),
        ("Y ADEMÁS", ["Si los números sostienen la conclusión", "Y dos indicadores proactivos"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este número no dice lo que la empresa cree"], AZUL2),
        ("APOYO", ["Y lo demostramos con la cuenta, o con el artículo"], TEAL),
        ("PREGUNTA", ["¿Qué medirían el mes que viene para poder corregir?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por la conclusión que no se sostiene",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s18_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que un índice en cero significaba…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué mide tu empresa que sí se puede corregir a tiempo?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s18_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 18")
    for fn in (ruta, puente, estimulo, nueve_uno_uno, evidencia, reactivo_proactivo,
               ejemplos_proactivos, indices, factores, no_alcanza, cero_accidentes,
               errores_1, errores_2, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
