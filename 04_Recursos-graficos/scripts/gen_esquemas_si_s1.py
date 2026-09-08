# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 de SI-SGCSSMA, sobre la estructura de alto nivel.

POR QUÉ NO PASA POR EL MODELO
    Son esquemas conceptuales —cajas y texto—, no equipos. La regla del §10
    (nunca texto→imagen) aplica a EQUIPOS: ahí el modelo inventaría geometría.
    Un esquema se dibuja, sale idéntico cada vez y se corrige en una línea.

QUÉ DIBUJA
    Las seis figuras de los puntos clave nuevos de la S1:
      anexo-sl_esqueleto-comun          punto clave 2
      clausulas_las-diez                punto clave 3
      clausulas_auditables              punto clave 3
      phva_sobre-las-clausulas          punto clave 4  (redibuja la anterior)
      citacion_numero-comun             punto clave 5
      citacion_donde-chocan             punto clave 5

Uso:  python gen_esquemas_si_s1.py
"""
from __future__ import annotations

import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      ciclo, cen, izq, caso, tabla)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def esqueleto_comun():
    """Lo que las tres normas comparten y lo que cada una pone aparte."""
    im, d = lienzo(1000)
    y = franjas(d, [
        ("LO MISMO", ["Un solo índice", "Los mismos títulos", "Los mismos términos"], AZUL2),
        ("LO PROPIO", ["Calidad: el cliente", "Ambiente: el entorno", "Seguridad: el trabajador"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Un mismo documento puede servir a más de un sistema", px=CUE)
    return guardar(im, "anexo-sl_esqueleto-comun.png", DEST)


def las_diez():
    """El mapa de las diez cláusulas, agrupadas por lo que hacen."""
    im, d = lienzo(1300)
    y = franjas(d, [
        ("1 A 3", ["Objeto y campo", "Referencias normativas", "Términos y definiciones"], GRIS),
        ("4 A 7", ["4 Contexto", "5 Liderazgo", "6 Planificación", "7 Apoyo"], AZUL2),
        ("8 A 10", ["8 Operación", "9 Evaluación del desempeño", "10 Mejora"], TEAL),
    ], im, y=60, alto=310)
    banda(d, y + 20, 130, "Las diez son iguales en la ISO 9001, la ISO 14001 y la ISO 45001", px=CUE)
    return guardar(im, "clausulas_las-diez.png", DEST)


def auditables():
    """Cuáles se auditan y cuáles no."""
    im, d = lienzo(1000)
    y = comparativa(d, "NO SE AUDITAN", "SE AUDITAN", [
        (["Cláusulas 1, 2 y 3"], ["Cláusulas 4 a 10"]),
        (["Dicen de qué trata la norma"], ["Dicen qué tiene que tener la empresa"]),
        (["No piden nada a la empresa"], ["Son los requisitos"]),
    ], y=50)
    banda(d, y + 20, 130, "El auditor pregunta por las siete, no por las tres primeras", px=CUE)
    return guardar(im, "clausulas_auditables.png", DEST)


def phva_sobre_clausulas():
    """El ciclo con las cláusulas repartidas en sus cuatro etapas."""
    im, d = lienzo(1420)
    ciclo(d, [("P", "PLANIFICAR", 180, 270, AZUL2),
              ("H", "HACER", 270, 360, TEAL),
              ("V", "VERIFICAR", 0, 90, MORADO),
              ("A", "ACTUAR", 90, 180, AMBAR)],
          cx=W / 2, cy=640, R=560, r=330,
          centro="Las diez cláusulas",
          lista=["P · 4, 5, 6 y 7", "H · 8", "V · 9", "A · 10"])
    banda(d, 1250, 130, "Si el ciclo no se cierra, el sistema no mejora", px=CUE)
    return guardar(im, "phva_sobre-las-clausulas.png", DEST)


def numero_comun():
    """Los niveles donde el número es el mismo en las tres normas."""
    im, d = lienzo(1080)
    d.rounded_rectangle([50, 60, W - 50, 300], 20, fill=GRISC)
    cen(d, 50, 110, W - 100, "PRIMER Y SEGUNDO NIVEL", TIT, AZUL)
    cen(d, 50, 200, W - 100, "el mismo número y el mismo asunto en las tres normas", CUE, GRIS, False)
    x, ancho = 60, (W - 120) / 5 - 20
    for etq, sub in [("4.1", "Contexto"), ("5.2", "Política"), ("7.5", "Documentada"),
                     ("9.2", "Auditoría"), ("10.2", "No conformidad")]:
        d.rounded_rectangle([x, 350, x + ancho, 610], 18, fill=AZUL2)
        cen(d, x, 400, ancho, etq, 88, BLANCO)
        cen(d, x, 520, ancho, sub, NOTA, BLANCO, False)
        x += ancho + 20
    banda(d, 670, 150, "Se citan sin paréntesis: van sin apellido de norma", px=CUE)
    d.rounded_rectangle([50, 860, W - 50, 1000], 18, fill=AMBAR)
    cen(d, 50, 900, W - 100, "Sin paréntesis = la cláusula es la misma en las tres", CUE, AZUL)
    return guardar(im, "citacion_numero-comun.png", DEST)


def donde_chocan():
    """Los dos números que significan cosas distintas según la norma."""
    im, d = lienzo(1180)
    y = 60
    for numero, izq_txt, der_txt in [
        ("8.2", ("ISO 45001 · ISO 14001", "Preparación y respuesta ante emergencias"),
                ("ISO 9001", "Requisitos para los productos y servicios")),
        ("9.1.2", ("ISO 45001 · ISO 14001", "Evaluación del cumplimiento legal"),
                  ("ISO 9001", "Satisfacción del cliente")),
    ]:
        d.rounded_rectangle([50, y, 300, y + 400], 20, fill=AZUL)
        cen(d, 50, y + 150, 250, numero, 104, AMBAR)
        for k, (norma, asunto) in enumerate([izq_txt, der_txt]):
            x0 = 340
            ancho = W - 50 - x0
            yy = y + k * 200
            d.rounded_rectangle([x0, yy + 10, x0 + ancho, yy + 180], 18,
                                fill=TEAL if k == 0 else GRISC)
            izq(d, x0 + 30, yy + 40, norma, NOTA, BLANCO if k == 0 else GRIS, True, ancho=ancho - 60)
            izq(d, x0 + 30, yy + 100, asunto, CUE, BLANCO if k == 0 else AZUL, ancho=ancho - 60)
        y += 440
    banda(d, y + 10, 150, "Del tercer nivel en adelante, el número va con la norma", px=CUE)
    return guardar(im, "citacion_donde-chocan.png", DEST)


def encargo():
    """Los dos pasos del encargo, cada uno en su cuadro."""
    im, d = lienzo(1150)
    y = franjas(d, [
        ("PASO 1", ["A qué sistema sirve cada documento",
                    "Marcar los que sirven a más de uno"], AZUL2),
        ("PASO 2", ["En qué cláusula lo exige la norma",
                    "Con el mapa de las diez a la vista"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Dos de los ocho no son documentos del sistema", px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  28 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s1_encargo.png", DEST)


def reflexion():
    """Las tres consignas del cierre, cada una en su cuadro."""
    im, d = lienzo(1200)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que un sistema de gestión era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué documento de tu trabajo sirve a más de un sistema?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s1_reflexion.png", DEST)


# ── las seis que se redibujan: estaban pegadas al diseno anterior del curso ──

def curso_en_una_lamina():
    """Los dos bloques del curso y sus dos colaborativos."""
    im, d = lienzo(1150)
    y = franjas(d, [
        ("BLOQUE 1", ["Cláusulas 4 a 7", "Montar el sistema", "Cierra con el TC1"], AZUL2),
        ("BLOQUE 2", ["Cláusulas 8 a 10", "Ponerlo en marcha", "Cierra con el TC2"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Doce sesiones cada bloque  ·  veinticuatro en total", px=CUE)
    banda(d, y + 175, 120, "Las tres normas van juntas de principio a fin", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_curso-en-una-lamina.png", DEST)


def evaluacion():
    """Que se califica y cuanto pesa."""
    im, d = lienzo(1150)
    y = franjas(d, [
        ("TC1", ["Informe de brechas", "Cinco criterios  ·  de 5 a 20"], AZUL2),
        ("TC2", ["Informe de auditoría interna", "Cinco criterios  ·  de 5 a 20"], TEAL),
        ("SESIÓN", ["Lista de cotejo  ·  cinco criterios de 0 a 4", "No lleva nota"], GRIS),
    ], im, y=60, alto=290)
    banda(d, y + 20, 140, "La suma de los cinco criterios ES la nota del equipo", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_evaluacion.png", DEST)


def ficha_caso_a():
    im, d = lienzo(1750)
    y = caso(d, "CASO A", "Perforaciones y Sondajes Mineros S.A.C.  ·  perforación diamantina  ·  78 trabajadores",
        ["Rosa Quispe tiene 48 horas. Si no entra el viernes, tres máquinas sin frente",
         "El cliente pide OCHO documentos. En el archivador hay SEIS",
         "Política firmada en marzo",
         "Matriz de residuos de enero",
         "Programa de mantenimiento con la fecha corregida a mano sobre la del año anterior",
         "Exámenes médicos vencidos el 12 de marzo del año pasado",
         "Hoja de datos del aceite, edición 2019",
         "Acta del comité de agosto"], color=AZUL2, y=50, alto=180)
    banda(d, y + 24, 140, "Todo guardado por área. La política, fotocopiada en las tres carpetas", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(1750)
    y = caso(d, "CASO B", "Obras Civiles y Movimiento de Tierras S.A.C.  ·  45 trabajadores",
        ["Julio Mamani tiene cinco días. Si no entra el lunes, cuatro excavadoras paradas",
         "El cliente pide OCHO documentos. En el archivador hay SEIS",
         "Política con la línea de firma en blanco",
         "Programa de residuos de febrero",
         "Cargos de EPP firmados uno por uno, todos con la misma letra",
         "Exámenes médicos vigentes hasta noviembre",
         "Hoja de datos del combustible, edición 2017",
         "Acta del comité de julio"], color=TEAL, y=50, alto=180)
    banda(d, y + 24, 140, "Cada área guarda lo suyo. El archivador de Calidad lo lleva la asistente, de vacaciones",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_caso-b.png", DEST)


def a_trabajar():
    """Que se entrega y como se reparte el tiempo."""
    im, d = lienzo(1150)
    y = franjas(d, [
        ("ENTREGAN", ["El cuadro de los ocho documentos", "Con su sistema y su cláusula"], AZUL2),
        ("MARCAN", ["Los que sirven a más de un sistema", "Los dos que no son del sistema"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "28 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_a-trabajar.png", DEST)


def formato_discusion():
    """El formato de la sustentacion: afirmacion, apoyo y pregunta."""
    im, d = lienzo(1180)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este documento sirve a estos sistemas"], AZUL2),
        ("APOYO", ["Y lo sostenemos en esta cláusula"], TEAL),
        ("PREGUNTA", ["¿En qué se diferencia del que marcó el otro equipo?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 140, "Dos minutos por equipo. Empezamos por los que sirven a más de un sistema",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_discusion.png", DEST)


def integrar():
    """Tres sistemas por separado frente a uno integrado. TRES, no cuatro:
    calidad, medio ambiente, y seguridad y salud en el trabajo."""
    im, d = lienzo(1320)
    SIST = [("SST", AZUL2), ("MA", TEAL), ("C", AMBAR)]
    cen(d, 0, 40, W, "POR SEPARADO", TIT, GRIS)
    ancho = (W - 100 - 2 * 40) / 3
    x = 50
    for etq, col in SIST:
        d.rounded_rectangle([x, 130, x + ancho, 500], 18, fill=BLANCO, outline=col, width=8)
        cen(d, x, 165, ancho, etq, 92, col)
        for k in range(3):
            d.rounded_rectangle([x + 40, 320 + k * 58, x + ancho - 40, 360 + k * 58], 10, fill=GRISC)
        x += ancho + 40
    cen(d, 0, 530, W, "3 políticas  ·  3 juegos de documentos", CUE, ROJO, False)
    d.polygon([(W / 2 - 46, 620), (W / 2 + 46, 620), (W / 2 + 46, 690),
               (W / 2 + 82, 690), (W / 2, 760), (W / 2 - 82, 690), (W / 2 - 46, 690)], fill=AMBAR)
    cen(d, 0, 790, W, "INTEGRADO", TIT, AZUL)
    d.rounded_rectangle([50, 880, W - 50, 1270], 22, fill=AZUL)
    ancho2 = (W - 200 - 2 * 40) / 3
    x = 100
    for etq, col in SIST:
        d.rounded_rectangle([x, 930, x + ancho2, 1050], 16, fill=col)
        cen(d, x, 950, ancho2, etq, 72, AZUL if col == AMBAR else BLANCO)
        x += ancho2 + 40
    d.line([160, 1090, W - 160, 1090], fill=AMBAR, width=8)
    cen(d, 50, 1120, W - 100, "1 política  ·  1 liderazgo", CUE, BLANCO)
    cen(d, 50, 1190, W - 100, "1 documentación  ·  1 ciclo", CUE, BLANCO)
    return guardar(im, "integrar_no-es-juntar-carpetas.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 1")
    for fn in (esqueleto_comun, las_diez, auditables, phva_sobre_clausulas,
               numero_comun, donde_chocan, encargo, reflexion,
               curso_en_una_lamina, evaluacion, ficha_caso_a, ficha_caso_b,
               a_trabajar, formato_discusion, integrar):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
