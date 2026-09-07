# -*- coding: utf-8 -*-
"""Esquemas de las sesiones 11 y 12 de SI-SGCSSMA · sustentación del TC1

Son las primeras sesiones de EVALUACIÓN del proyecto. Siguen la plantilla 003B
—tres fases, no cinco momentos— y el PPT 004B, de una docena de láminas. La
plantilla oficial no está en el repo: la estructura sale del §05 y el §07, y el
lenguaje visual se toma de las sesiones de adquisición ya hechas.

Las tres fases, textuales del §05:
  ① Presentación de trabajos en equipo
  ② Retroalimentación del instructor
  ③ Reflexión y cierre

Los datos del TC1 —entregables, roles, tiempos y criterios de la rúbrica— salen
de 06_TC1_Indicaciones.docx y 05_TC1_Rubrica.xlsx. No se inventan aquí.

Uso:  python gen_esquemas_si_s11_s12.py
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


# ─────────────────────────────── sesión 11 ───────────────────────────────

def ruta_s11():
    im, d = lienzo(1180)
    filas_letra(d, [
        ("①", "PRESENTACIÓN", "Cada equipo sustenta su informe de brechas", AZUL2),
        ("②", "RETROALIMENTACIÓN", "Preguntas del instructor y del resto de equipos", TEAL),
        ("③", "CIERRE", "Qué se llevan a corregir para la próxima sesión", MORADO),
    ], y=50, alto=340, sep=30)
    return guardar(im, "s11_ruta.png", DEST)


def objetivo_s11():
    im, d = lienzo(1000)
    y = franjas(d, [
        ("HOY", ["Sustentan el informe de brechas del sistema",
                 "Sobre las cláusulas 4 a 7"], AZUL2),
        ("SE MIDE", ["Con la rúbrica del trabajo colaborativo 1",
                     "Cinco criterios, de 1 a 4"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "Es la evaluación del primer bloque: vale el 25 % del curso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s11_objetivo.png", DEST)


def rubrica_tc1():
    """Los cinco criterios y que gana el 4. La rubrica completa ya la tienen
    desde la S10: proyectarla entera daria unos 5 pt."""
    im, d = lienzo(1840)
    y = filas_letra(d, [
        ("1", "COMPRENSIÓN", "Describe qué mide el informe del cliente y qué quedó fuera", AZUL2),
        ("2", "DESARROLLO", "El cuadro de correspondencia cubre las cuatro brechas, con su norma", TEAL),
        ("3", "CONCLUSIONES", "Señala a quién deja sin cubrir cada hueco, y por dónde empezar", MORADO),
        ("4", "EL PPT", "Recorre las siete láminas y muestra el procedimiento, no la norma copiada", AMBAR),
        ("5", "LA ORAL", "Los cuatro exponen su rol y el equipo responde preguntas técnicas", GRIS),
    ], y=50, alto=290, sep=26)
    banda(d, y + 20, 150, "Así se gana el 4 en cada criterio. Los cinco suman 20",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s11_rubrica.png", DEST)


def orden_de_exposicion():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("ORDEN", ["El sorteo decide qué equipo abre", "El resto sigue en ese orden"], AZUL2),
        ("REGLAS", ["Exponen los cuatro integrantes, cada uno su rol",
                    "El PPT se proyecta desde una sola máquina"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "Mientras un equipo expone, los demás anotan una pregunta técnica",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s11_orden.png", DEST)


def el_turno():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("DOCE", ["Minutos de sustentación", "Portada y seis láminas de contenido"], AZUL2),
        ("OCHO", ["Minutos de preguntas", "Del instructor y de los otros equipos"], TEAL),
        ("CIERRA", ["El instructor devuelve lo observado, con la rúbrica delante"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "El mismo turno para todos. El tiempo de sustentación no se estira",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s11_turno.png", DEST)


def encargo_correccion():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("UNA", ["Cada equipo se lleva UNA sección observada"], AZUL2),
        ("CORRIGE", ["La rehace con lo que se dijo hoy"], TEAL),
        ("VUELVE", ["Y la defiende la próxima sesión, en seis minutos"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "La observación no se archiva: se usa, y se vuelve a mirar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s11_encargo-correccion.png", DEST)


def reflexion_s11():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes de sustentar pensaba que lo difícil sería…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué pregunta del instructor no supiste responder?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s11_reflexion.png", DEST)


# ─────────────────────────────── sesión 12 ───────────────────────────────

def ruta_s12():
    im, d = lienzo(1180)
    filas_letra(d, [
        ("①", "PRESENTACIÓN", "Cada equipo defiende la sección que corrigió", AZUL2),
        ("②", "RETROALIMENTACIÓN", "Cada equipo revisa la corrección de otro", TEAL),
        ("③", "CIERRE", "Qué queda en claro de las cláusulas 4 a 7", MORADO),
    ], y=50, alto=340, sep=30)
    return guardar(im, "s12_ruta.png", DEST)


def objetivo_s12():
    im, d = lienzo(1000)
    y = franjas(d, [
        ("HOY", ["Se defiende la sección corregida", "Y se revisa la de otro equipo"], AZUL2),
        ("PARA", ["Cerrar las cláusulas 4 a 7", "Antes de entrar al bloque de operación"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "La nota del TC1 ya está puesta. Esto es lo que se aprende después",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s12_objetivo.png", DEST)


def panorama_errores():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("1", "CLÁUSULA", "Se nombró el documento sin decir qué cláusula incumple", AZUL2),
        ("2", "NORMA", "Se citó la norma de memoria, sin el artículo", TEAL),
        ("3", "OBJETIVO", "El programa de cierre trajo deseos, no objetivos medibles", MORADO),
        ("4", "SISTEMA", "Se olvidó el sistema de gestión que la evaluación no miró", AMBAR),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s12_panorama.png", DEST)


def defensa_correccion():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("QUÉ", ["Qué decía la sección antes"], AZUL2),
        ("CAMBIÓ", ["Qué dice ahora, y por qué se cambió"], TEAL),
        ("PRUEBA", ["Con qué se sostiene: cláusula, artículo o dato del caso"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Seis minutos por equipo. No se vuelve a exponer todo el informe",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s12_defensa.png", DEST)


def cruzada():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("MIRA", ["Cada equipo revisa la corrección de otro"], AZUL2),
        ("DEVUELVE", ["Una cosa que quedó bien y una que sigue floja"], TEAL),
        ("RESPONDE", ["El equipo revisado contesta, sin justificarse"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Se revisa el trabajo, no a las personas. Y se dice con qué se sostiene",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s12_cruzada.png", DEST)


def cierre_bloque():
    im, d = lienzo(1840)
    y = filas_letra(d, [
        ("4", "CONTEXTO", "Quién le importa a la empresa, y hasta dónde llega su sistema", AZUL2),
        ("5", "LIDERAZGO", "Quién responde, qué dice la política y a quién se consulta", TEAL),
        ("6", "PLANIFICAR", "Qué se identifica, qué obliga por ley y qué se propone el año", MORADO),
        ("7", "APOYO", "Con qué gente y qué recursos, qué se comunica y qué se documenta", AMBAR),
        ("8", "SIGUE", "Cómo se controla la tarea en el frente: el bloque que empieza", GRIS),
    ], y=50, alto=290, sep=26)
    banda(d, y + 20, 150, "Las cuatro cláusulas que evaluó el TC1, y la que viene",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s12_cierre-bloque.png", DEST)


def reflexion_s12():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes de corregir pensaba que la observación era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué te enseñó revisar el trabajo de otro equipo?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s12_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesiones 11 y 12 (evaluación del TC1)")
    for fn in (ruta_s11, objetivo_s11, rubrica_tc1, orden_de_exposicion, el_turno,
               encargo_correccion, reflexion_s11,
               ruta_s12, objetivo_s12, panorama_errores, defensa_correccion, cruzada,
               cierre_bloque, reflexion_s12):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
