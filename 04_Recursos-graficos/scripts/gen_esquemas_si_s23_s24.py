# -*- coding: utf-8 -*-
"""Esquemas de las sesiones 23 y 24 de SI-SGCSSMA · sustentación del TC2

Cierran el curso. Misma forma que la S11 y la S12: plantilla 003B —tres fases— y
PPT 004B, de una docena de láminas. La plantilla oficial no está en el repo, así
que la estructura sale del §05 y el §07 y el lenguaje visual de las sesiones de
adquisición.

Los datos del TC2 —entregables, roles de auditor, tiempos y criterios de la
rúbrica— salen de 11_TC2_Indicaciones.docx y 13_TC2_Rubrica.xlsx.
El turno es el mismo que se fijó para el TC1: 12 minutos de sustentación y 8 de
preguntas, cinco equipos por sesión.

Uso:  python gen_esquemas_si_s23_s24.py
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


# ─────────────────────────────── sesión 23 ───────────────────────────────

def ruta_s23():
    im, d = lienzo(1180)
    filas_letra(d, [
        ("①", "PRESENTACIÓN", "Cada equipo sustenta su informe de auditoría interna", AZUL2),
        ("②", "RETROALIMENTACIÓN", "Preguntas del instructor y del resto de equipos", TEAL),
        ("③", "CIERRE", "Qué se llevan a corregir para la última sesión", MORADO),
    ], y=50, alto=340, sep=30)
    return guardar(im, "s23_ruta.png", DEST)


def objetivo_s23():
    im, d = lienzo(1000)
    y = franjas(d, [
        ("HOY", ["Sustentan el informe de auditoría interna",
                 "Sobre las cláusulas 8, 9 y 10"], AZUL2),
        ("SE MIDE", ["Con la rúbrica del trabajo colaborativo 2",
                     "Cinco criterios, de 1 a 4"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "Es la evaluación del segundo bloque: vale el 25 % del curso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s23_objetivo.png", DEST)


def rubrica_tc2():
    """Los cinco criterios y que gana el 4. La rubrica completa la tienen desde la S22."""
    im, d = lienzo(1840)
    y = filas_letra(d, [
        ("1", "COMPRENSIÓN", "Verifica los tres índices y señala qué excluyó el cálculo del tablero", AZUL2),
        ("2", "DESARROLLO", "Clasifica las evidencias con su cláusula y su categoría", TEAL),
        ("3", "CONCLUSIONES", "Describe el hallazgo ambiental y qué exige el sistema", MORADO),
        ("4", "EL PPT", "Recorre las siete láminas sin saltarse ninguna", AMBAR),
        ("5", "LA ORAL", "Los cuatro exponen su rol y responden la pregunta que les toca", GRIS),
    ], y=50, alto=290, sep=26)
    banda(d, y + 20, 150, "Así se gana el 4 en cada criterio. Los cinco suman 20",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s23_rubrica.png", DEST)


def orden_s23():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("ORDEN", ["El sorteo decide qué equipo abre", "El resto sigue en ese orden"], AZUL2),
        ("REGLAS", ["Exponen los cuatro auditores, cada uno su rol",
                    "El PPT se proyecta desde una sola máquina"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "Mientras un equipo expone, los demás anotan una pregunta técnica",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s23_orden.png", DEST)


def turno_s23():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("DOCE", ["Minutos de sustentación", "Portada y seis láminas de contenido"], AZUL2),
        ("OCHO", ["Minutos de preguntas", "Del instructor y de los otros equipos"], TEAL),
        ("CIERRA", ["El instructor devuelve lo observado, con la rúbrica delante"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "El mismo turno para todos. El tiempo de sustentación no se estira",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s23_turno.png", DEST)


def correccion_s23():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("UNA", ["Cada equipo se lleva UNA sección observada"], AZUL2),
        ("CORRIGE", ["La rehace con lo que se dijo hoy"], TEAL),
        ("VUELVE", ["Y la defiende la próxima sesión, en seis minutos"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "La observación no se archiva: se usa, y se vuelve a mirar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s23_encargo-correccion.png", DEST)


def reflexion_s23():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes de auditar pensaba que lo difícil sería…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué evidencia te costó más clasificar, y por qué?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s23_reflexion.png", DEST)


# ─────────────────────────────── sesión 24 ───────────────────────────────

def ruta_s24():
    im, d = lienzo(1180)
    filas_letra(d, [
        ("①", "PRESENTACIÓN", "Cada equipo defiende la sección que corrigió", AZUL2),
        ("②", "RETROALIMENTACIÓN", "Cada equipo revisa la corrección de otro", TEAL),
        ("③", "CIERRE", "Lo que queda del curso completo", MORADO),
    ], y=50, alto=340, sep=30)
    return guardar(im, "s24_ruta.png", DEST)


def objetivo_s24():
    im, d = lienzo(1000)
    y = franjas(d, [
        ("HOY", ["Se defiende la sección corregida", "Y se revisa la de otro equipo"], AZUL2),
        ("Y DESPUÉS", ["Se cierra el curso", "Las diez cláusulas, de principio a fin"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "Es la última sesión: la nota ya está puesta, y todavía queda algo por aprender",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s24_objetivo.png", DEST)


def panorama_s24():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("1", "CATEGORÍA", "Se clasificó la evidencia sin decir si era mayor o menor", AZUL2),
        ("2", "POBLACIÓN", "Se verificó el índice sin decir sobre qué población se calculó", TEAL),
        ("3", "JERARQUÍA", "La acción correctiva no se ubicó en su nivel", MORADO),
        ("4", "LA DIRECCIÓN", "No se dijo qué se eleva a la revisión por la dirección", AMBAR),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s24_panorama.png", DEST)


def defensa_s24():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("QUÉ", ["Qué decía la sección antes"], AZUL2),
        ("CAMBIÓ", ["Qué dice ahora, y por qué se cambió"], TEAL),
        ("PRUEBA", ["Con qué se sostiene: cláusula, artículo o evidencia del caso"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Seis minutos por equipo. No se vuelve a exponer todo el informe",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s24_defensa.png", DEST)


def cruzada_s24():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("MIRA", ["Cada equipo revisa la corrección de otro"], AZUL2),
        ("DEVUELVE", ["Una cosa que quedó bien y una que sigue floja"], TEAL),
        ("RESPONDE", ["El equipo revisado contesta, sin justificarse"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Se revisa el trabajo, no a las personas. Y se dice con qué se sostiene",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s24_cruzada.png", DEST)


def cierre_curso():
    im, d = lienzo(2130)
    y = filas_letra(d, [
        ("4", "CONTEXTO", "Quién le importa a la empresa y hasta dónde llega su sistema", AZUL2),
        ("5", "LIDERAZGO", "Quién responde, qué dice la política y a quién se consulta", TEAL),
        ("6", "PLANIFICAR", "Qué se identifica, qué obliga por ley y qué se propone el año", MORADO),
        ("7", "APOYO", "Con qué gente y recursos, qué se comunica y qué se documenta", AMBAR),
        ("8", "OPERAR", "Cómo se controla la tarea, se compra y se responde a una emergencia", GRIS),
        ("9 y 10", "VERIFICAR", "Cómo se mide, se audita, se revisa y se mejora", AZUL2),
    ], y=50, alto=290, sep=26)
    banda(d, y + 20, 160, "Las siete cláusulas auditables, en el orden en que las recorrimos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s24_cierre-curso.png", DEST)


def reflexion_s24():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("LA PRIMERA", ["En la sesión 1 escribiste qué creías que era un sistema"], GRIS),
        ("HOY", ["Después de veinticuatro sesiones, ¿qué escribirías?"], AZUL2),
        ("EL LUNES", ["¿Qué te llevas de este curso al trabajo?"], TEAL),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Es el cierre del curso. Se escribe, y el que quiera lo comparte",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s24_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesiones 23 y 24 (evaluación del TC2)")
    for fn in (ruta_s23, objetivo_s23, rubrica_tc2, orden_s23, turno_s23, correccion_s23,
               reflexion_s23,
               ruta_s24, objetivo_s24, panorama_s24, defensa_s24, cruzada_s24,
               cierre_curso, reflexion_s24):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
