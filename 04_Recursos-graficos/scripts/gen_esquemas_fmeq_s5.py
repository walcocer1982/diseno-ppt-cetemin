# -*- coding: utf-8 -*-
"""Esquemas de la sesión 5 de EOM · Fundamentos mecánicos de equipos mineros.

Diagnóstico de fallas. Es la sesión bisagra del curso: la única que enseña el
indicador 3 —reconocer las condiciones que impiden iniciar o continuar la
actividad— y la que alimenta los criterios 1 y 3 de la rúbrica del TC1.

Las quince láminas con imagen salen de las formas del módulo común. Lo único
propio de esta sesión es el cuadro de testigos del tablero, que se dibuja
porque un testigo es un rótulo de color, no una pieza con geometría.

Uso:  python gen_esquemas_fmeq_s5.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_esquemas_fmeq_comun import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, GRIS, MARINO, MORADO, NOTA, ROJO,
    VERDE,
    _celda, _redonda, _salida, antes_de_resolver, banda, cabecera,
    dos_columnas, ficha_caso, lienzo, lista_numerada, puente, puesta_comun,
    tres_fichas,
)

G = _salida("fmeq/s5/")


# ═══════════════════════════════════ 1 · de dónde venimos
def de_donde():
    dos_columnas(
        G, "fmeq-s5_de-donde.png",
        "LAS CUATRO SESIONES ANTERIORES", "ESTA SESIÓN",
        [("nombramos los componentes\nde cada equipo", "leemos lo que el equipo\navisa por su cuenta"),
         ("supimos qué hace cada uno", "sabemos cuál impide\nque la actividad empiece"),
         ("miramos la máquina", "miramos el tablero\ny el pre-uso, juntos")],
        pie="Hasta hoy describías el equipo. Hoy decides si entra o no",
        asp=1.40)


# ═══════════════════════════════════ 2 · los testigos del tablero
def tablero():
    """Qué avisa el tablero y con qué color. Un testigo es un rótulo, no una pieza."""
    fig, ax = lienzo(1.30)
    H = 100 / 1.30

    ax.text(50, H * 0.92, "El tablero avisa con testigos de color y con alarmas",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            fontweight="bold", color=MARINO)
    _redonda(ax, 3, H * 0.66, 45, H * 0.16, ROJO)
    ax.text(25.5, H * 0.74, "ROJO · DETENER", ha="center", va="center", family=F,
            fontsize=NOTA, fontweight="bold", color=BLANCO)
    _redonda(ax, 52, H * 0.66, 45, H * 0.16, AMBAR)
    ax.text(74.5, H * 0.74, "ÁMBAR · ATENCIÓN", ha="center", va="center", family=F,
            fontsize=NOTA, fontweight="bold", color=MARINO)

    filas = [("Presión de aceite de motor", "tiene su propio testigo"),
             ("Temperatura del aceite hidráulico", "se lee en el tablero"),
             ("Filtro de retorno", "avisa que está restringido")]
    y = H * 0.60
    alto = H * 0.13
    for a, b in filas:
        y -= alto + 1.2
        _celda(ax, 3, y, 45, alto, a, CLARO, MARINO, tam=NOTA * 0.88)
        _celda(ax, 52, y, 45, alto, b, BLANCO, GRIS, tam=NOTA * 0.88)
    banda(ax, H * 0.05, H * 0.11, "El color dice qué hacer, no qué está fallando")
    G(fig, "fmeq-s5_tablero.png")


# ═══════════════════════════════════ 3 · tablero y pre-uso
def tablero_preuso():
    dos_columnas(
        G, "fmeq-s5_tablero-preuso.png", "LO QUE MUESTRA EL TABLERO",
        "LO QUE SOLO SE VE EN EL PRE-USO",
        [("los testigos y las alarmas", "el nivel del tanque hidráulico"),
         ("lo que el equipo mide solo", "lo que alguien tiene que mirar"),
         ("aparece cuando ya pasó algo", "aparece antes de arrancar")],
        pie="Tablero y pre-uso se leen juntos, no por separado", asp=1.35)


# ═══════════════════════════════════ 4 · cada señal, su sistema
def senal_sistema():
    fig, ax = lienzo(1.15)
    H = 100 / 1.15

    x = [3.0, 52.0, 97.0]
    y = H * 0.82
    cabecera(ax, x[0], y, x[1] - x[0], H * 0.11, "LA SEÑAL", MARINO)
    cabecera(ax, x[1], y, x[2] - x[1], H * 0.11, "EL SISTEMA QUE LA ORIGINA", AZUL)
    filas = [("Presión de aceite de motor", "lubricación del motor"),
             ("Temperatura del aceite hidráulico", "hidráulico y su enfriador"),
             ("Filtro de retorno restringido", "hidráulico"),
             ("Nivel bajo del tanque", "hidráulico")]
    alto = H * 0.125
    for a, b in filas:
        y -= alto + 1.0
        _celda(ax, x[0], y, x[1] - x[0], alto, a, CLARO, MARINO, tam=NOTA * 0.88)
        _celda(ax, x[1], y, x[2] - x[1], alto, b, BLANCO, MARINO, tam=NOTA * 0.88)
    banda(ax, H * 0.05, H * 0.12, "Cada testigo pertenece a un sistema, no a la máquina")
    G(fig, "fmeq-s5_senal-sistema.png")


# ═══════════════════════════════════ 5 · dos señales, un sistema
def mismo_sistema():
    tres_fichas(
        G, "fmeq-s5_mismo-sistema.png", "Cuando salen varias a la vez",
        [("DEL MISMO\nSISTEMA", AZUL, "no son dos fallas:\nes una sola",
          "se reportan juntas"),
         ("DE SISTEMAS\nDISTINTOS", MORADO, "son hallazgos\nseparados",
          "se reportan por separado"),
         ("LA QUE OTRA\nFUENTE CONFIRMA", VERDE, "deja de ser dudosa",
          "el pre-uso confirma\nal tablero")],
        pie="Antes de contar señales, agrúpalas por sistema", asp=1.15)


# ═══════════════════════════════════ 6 · detiene o se reporta
def detiene_reporta():
    dos_columnas(
        G, "fmeq-s5_detiene-reporta.png", "DETIENE", "SE REPORTA Y SIGUE",
        [("compromete la seguridad", "degrada el rendimiento"),
         ("la presión de aceite baja,\nsiempre", "con la restricción\nque corresponda"),
         ("no se discute", "con plazo y responsable")],
        pie="La pregunta no es si molesta: es qué compromete", asp=1.35,
        color_izq=ROJO, color_der=VERDE)


# ═══════════════════════════════════ 7 · el cuadro de señales
def cuadro_senales():
    lista_numerada(
        G, "fmeq-s5_cuadro-senales.png",
        ["Un cuadro de varias señales pesa más que una sola",
         "Que un testigo salga siempre no lo vuelve falso",
         "Una señal que otra fuente confirma deja de ser dudosa"],
        cierre="La costumbre no es un diagnóstico",
        pie="Lo que sale siempre, se comprueba una vez y se cierra", asp=1.35)


# ═══════════════════════════════════ 8 · qué lleva el reporte
def que_lleva():
    lista_numerada(
        G, "fmeq-s5_que-lleva.png",
        ["Qué se observó, no qué se supone",
         "La señal, el sistema y dónde se leyó",
         "La medida tomada, escrita y no sobrentendida"],
        pie="Lo que se reporta sin medida queda sin dueño", asp=1.40)


# ═══════════════════════════════════ 9 · a quién va y qué lo prueba
def a_quien():
    lista_numerada(
        G, "fmeq-s5_a-quien.png",
        ["Va al turno entrante y al área de mantenimiento",
         "Sin fecha ni firma, el reporte no prueba nada",
         "Escribir la causa probable es trabajo del mecánico"],
        cierre="DS 024-2016-EM · artículo 39: entrega de guardia por escrito",
        pie="El técnico reporta lo que vio; el mecánico dice por qué pasó",
        asp=1.20)


# ═══════════════════════════════════ 10 a 15 · el armazón
def caso():
    ficha_caso(
        G, "fmeq-s5_caso-ficha.png",
        "Desarrollo y Preparación de Labores S.A.C.",
        "Empernador del nivel 3 · el único del nivel",
        [("AL ARRANCAR", "tres testigos encendidos: presión de aceite de motor,\n"
                         "temperatura del hidráulico y filtro restringido"),
         ("EL EQUIPO", "lleva diez minutos prendido y todavía está frío"),
         ("EL OPERADOR", "«dos de esos salen siempre desde que\nle cambiaron el sensor»"),
         ("EN EL PRE-USO", "el nivel del tanque hidráulico,\nmarcado en el mínimo")],
        pie_nota="Dos guardias sin sostener, y el disparo es a las siete.")


def antes():
    antes_de_resolver(
        G, "fmeq-s5_antes-de-resolver.png",
        "Si un testigo sale siempre, ¿deja de ser una señal?",
        [("TRES", "testigos encendidos\ncon el equipo frío"),
         ("MEDIA HORA", "es lo que el operador\npide para diez pernos"),
         ("EL ÚNICO", "empernador del nivel,\ny el frente espera")])


def encargo():
    lista_numerada(
        G, "fmeq-s5_encargo.png",
        ["Las señales que hay, y dónde se lee cada una: tablero o pre-uso",
         "A qué sistema pertenece cada una",
         "Cuáles impiden que el equipo entre y cuáles se reportan, con su razón",
         "El reporte a mantenimiento: lo observado, el sistema y la medida"],
        pie="Una hoja en blanco por equipo · 40 minutos", asp=1.10)


def como_trabajamos():
    lista_numerada(
        G, "fmeq-s5_como-trabajamos.png",
        ["Listen todas las señales antes de opinar sobre ninguna",
         "Pongan al costado de cada una el sistema del que viene",
         "Separen las que detienen de las que se reportan, y digan por qué",
         "Escriban el reporte como si lo fuera a leer el turno entrante"],
        pie="Equipos de 3 · 40 minutos · expone uno por equipo", asp=1.40)


def puesta():
    puesta_comun(
        G, "fmeq-s5_puesta-comun.png",
        [("AFIRMACIÓN", AZUL, "entra o no entra\nel empernador"),
         ("APOYO", VERDE, "qué señal lo decide\ny dónde se leyó"),
         ("PREGUNTA", MORADO, "lo que todavía\nfalta saber")],
        "Empezamos por los equipos que decidieron distinto")


def puente_tc1():
    puente(
        G, "fmeq-s5_puente-tc1.png",
        "LA PRÓXIMA SESIÓN", "El trabajo colaborativo:\nuna labor con cinco equipos\ny una decisión por cada uno",
        "CIERRA EL BLOQUE 1", "TC1: hay un operador\ndebajo de un equipo,\ny el reloj corre",
        "Hoy decidiste sobre un equipo con tres señales.\n"
        "En el TC1 vas a decidir sobre cinco, y solo dos traen hallazgo.",
        pie="Antes de la próxima clase: el recurso autónomo del EVA.")


if __name__ == "__main__":
    print("Esquemas de EOM-FMEQ-S5 · Diagnóstico de fallas\n")
    for f in (de_donde, tablero, tablero_preuso, senal_sistema, mismo_sistema,
              detiene_reporta, cuadro_senales, que_lleva, a_quien, caso, antes,
              encargo, como_trabajamos, puesta, puente_tc1):
        f()
    print("\n15 esquemas en 04_Recursos-graficos/EOM/esquemas/fmeq/s5/")
