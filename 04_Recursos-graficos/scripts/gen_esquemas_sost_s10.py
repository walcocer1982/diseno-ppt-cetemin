# -*- coding: utf-8 -*-
"""Esquemas de la sesión 10 de EOM · Control de calidad de la instalación.

La S9 dejó el pedido. Esta sesión recibe: qué se verifica en un perno puesto y
en un lanzado, con qué prueba o instrumento, quién responde de cada cosa, y qué
obliga a registrar el reglamento.

La bisagra de la sesión es que un certificado de proveedor puede ser cierto,
estar bien emitido y no alcanzar: habla del material que vendió, no de cómo
quedó instalado.

QUÉ SE DIBUJA Y QUÉ NO
    Se dibujan las tablas de verificación, la escala del reglamento, el acta y
    el armazón. Lo físico —la prueba de arranque, el espesor lanzado y la
    distancia de la boquilla— entra por fotografía y por plano de fuente, dos
    de ellos ya catalogados desde la S2.

Uso:  python gen_esquemas_sost_s10.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, GRIS, MARINO, MORADO, NOTA, VERDE,
    guardar, lienzo,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402
from gen_esquemas_sost_s1 import _cabecera  # noqa: E402
from gen_esquemas_sost_s2 import _cierre, _pasos, _tabla  # noqa: E402
from gen_esquemas_sost_s5 import _dos_columnas  # noqa: E402

CARPETA = "sost/s10/"


def _g(fig, nombre):
    return guardar(fig, CARPETA + nombre)


# ═══════════════════════════════════════════════ 1 · de dónde venimos
def de_donde_venimos():
    _dos_columnas("sost-s10_de-donde-venimos.png",
                  ("LA S9 PIDIÓ", "cuántos pernos, cuánta malla\ny con qué accesorios", AZUL),
                  ("HOY SE RECIBE", "si lo que se instaló\nquedó como se pidió", VERDE),
                  "Pedir bien no garantiza que quede bien puesto", asp=2.10,
                  guardar_en=_g)


# ═══════════════════════════════ 2 · lo que se mira en un perno puesto
def lo_que_se_mira_en_un_perno():
    ASP = 1.44
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(40.0, "LO QUE SE OBSERVA"), (50.0, "QUÉ SIGNIFICA")]
    filas = [["La platina no apoya contra la roca", "el perno no entró hasta el fondo"],
             ["El perno gira al ajustar la tuerca", "el anclaje no agarró"],
             ["Suena hueco al golpearlo", "está con baja tensión"],
             ["Sobresale más de lo roscado", "el taladro quedó corto"]]
    _tabla(ax, H, 3.0, cols, filas, H * 0.80, H * 0.075, H * 0.105)
    ax.text(50, H * 0.185, "el torque se comprueba con llave, sobre la tuerca",
            ha="center", va="center", family=F, fontsize=NOTA * 0.85, color=GRIS)
    _cierre(ax, H, "Todo esto se ve en la labor, y nada de esto está en un certificado",
            H * 0.055)
    _g(fig, "sost-s10_lo-que-se-mira-en-un-perno.png")


# ═════════════════════════════════════ 3 · las probetas y los 28 días
def las_probetas():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Se toman probetas cada cierto volumen lanzado", "no una por obra"),
                   ("Van a laboratorio, no se juzgan a la vista", "la resistencia no se estima"),
                   ("El resultado llega a los veintiocho días", "mucho después de firmar el acta"),
                   ("Por eso el espesor se mide el mismo día", "eso sí lo verifica quien recibe")],
           H * 0.76, H * 0.155)
    _cierre(ax, H, "El espesor lo verifica quien recibe; la resistencia la informa el ensayo",
            H * 0.055)
    _g(fig, "sost-s10_las-probetas.png")


# ══════════════════════════════════ 4 · lo que obliga el reglamento
def lo_que_obliga_el_reglamento():
    ASP = 1.70
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 5.0, H * 0.78, 90.0, H * 0.11, "DS 024-2016-EM  ·  ART. 214 b)", MARINO,
              NOTA * 0.85)
    ax.text(50, H * 0.685, "«Registrar mensualmente los ensayos y pruebas de control\n"
                           "de calidad, respecto de no menos del 1 % del sostenimiento\n"
                           "aplicado en dicho periodo»",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92,
            color=MARINO, linespacing=1.4)

    for x0, titulo, valor, color in ((8.0, "CADA CUÁNTO", "mensualmente", AZUL),
                                     (54.0, "SOBRE CUÁNTO", "no menos del 1 %", VERDE)):
        _redonda(ax, x0, H * 0.26, 38.0, H * 0.22, CLARO)
        _caja(ax, x0, H * 0.475, 38.0, 1.0, color)
        ax.text(x0 + 19.0, H * 0.415, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.78, fontweight="bold", color=color)
        ax.text(x0 + 19.0, H * 0.325, valor, ha="center", va="center", family=F,
                fontsize=CUERPO * 0.95, color=MARINO)
    _cierre(ax, H, "El 1 % se cuenta sobre lo sostenido en ese mismo periodo", H * 0.07)
    _g(fig, "sost-s10_lo-que-obliga-el-reglamento.png")


# ═══════════════════════════════════ 5 · registrar no es archivar
def registrar_no_es_archivar():
    _dos_columnas("sost-s10_registrar-no-es-archivar.png",
                  ("ARCHIVAR", "guardar el papel\nque trajo el contratista", MORADO),
                  ("REGISTRAR", "dejar escrito el resultado\nde cada verificación", VERDE),
                  "Sin registro, un tramo verificado equivale a uno sin verificar", asp=1.85,
                  guardar_en=_g)


# ══════════════════════════ 6 · el material y la instalación
def material_vs_instalacion():
    ASP = 1.42
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(2.0, "EL CERTIFICADO DEL PROVEEDOR", MORADO,
             ["Habla del material que vendió", "Dice que el cemento llega a 240",
              "Se ensaya en laboratorio", "Lo firma quien lo fabricó"]),
            (51.0, "EL ACTA DE RECEPCIÓN", VERDE,
             ["Habla de cómo quedó instalado", "Dice cuánto espesor se lanzó",
              "Se verifica en la labor", "La firma quien recibe"])]
    for x0, titulo, color, items in cols:
        w = 47.0
        _cabecera(ax, x0, H * 0.80, w, H * 0.11, titulo, color, NOTA * 0.72)
        y = H * 0.80
        for it in items:
            y -= H * 0.140
            _celda(ax, x0, y, w, H * 0.125, it, CLARO, MARINO, tam=NOTA * 0.80)
    _cierre(ax, H, "Un material conforme mal instalado no sostiene nada", H * 0.06)
    _g(fig, "sost-s10_material-vs-instalacion.png")


# ════════════════════════════════════════════ 7 · el certificado
def el_certificado():
    ASP = 1.55
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 5.0, H * 0.58, 90.0, H * 0.28, CLARO)
    _caja(ax, 5.0, H * 0.855, 90.0, 1.0, MORADO)
    ax.text(50, H * 0.775, "LO QUE TRAE EL CONTRATISTA", ha="center", va="center",
            family=F, fontsize=NOTA * 0.82, fontweight="bold", color=MORADO)
    ax.text(50, H * 0.685, "certificado del proveedor  ·  240 kg/cm² a los 28 días",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92, color=MARINO)
    ax.text(50, H * 0.615, "con sello y firma · más la guía de remisión de los pernos",
            ha="center", va="center", family=F, fontsize=NOTA * 0.82, color=GRIS)

    _redonda(ax, 12.0, H * 0.26, 76.0, H * 0.22, BLANCO)
    _caja(ax, 12.0, H * 0.475, 76.0, 1.0, VERDE)
    ax.text(50, H * 0.405, "EL TRAMO RECIBIDO", ha="center", va="center", family=F,
            fontsize=NOTA * 0.78, fontweight="bold", color=VERDE)
    ax.text(50, H * 0.315, "120 pernos instalados  ·  60 metros lanzados",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.92, color=MARINO)
    _cierre(ax, H, "«Con esto está conforme. El material es el que pidieron»", H * 0.07)
    _g(fig, "sost-s10_el-certificado.png")


# ═══════════════════════════════════ 8 · lo que se ve caminando
def caminando_el_tramo():
    ASP = 1.52
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _cabecera(ax, 3.0, H * 0.84, 94.0, H * 0.085, "LO QUE USTEDES VEN CAMINANDO EL TRAMO",
              MARINO, NOTA * 0.8)
    y = H * 0.84
    for txt, color in ((u"En dos pernos la platina no llega a apoyar, y baila con la mano", MORADO),
                       (u"En un tercio del avance el concreto se ve más delgado", MORADO),
                       (u"Hay bastante material caído al piso, todavía fresco", MORADO),
                       (u"Mañana entra la cuadrilla de perforación debajo de eso", AZUL)):
        y -= H * 0.155
        _redonda(ax, 3.0, y, 94.0, H * 0.13, CLARO)
        _caja(ax, 3.0, y, 1.5, H * 0.13, color)
        ax.text(8.0, y + H * 0.065, txt, ha="left", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO)
    _cierre(ax, H, "El acta se firma antes de las doce", H * 0.05)
    _g(fig, "sost-s10_caminando-el-tramo.png")


# ═════════════════════════════════════ 9 · el acta que se entrega
def acta_encargo():
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    cols = [(30.0, "QUÉ SE VERIFICA"), (26.0, "CON QUÉ"), (16.0, "QUIÉN"), (18.0, "RESULTADO")]
    filas = [["", "", "", ""] for _ in range(5)]
    y = _tabla(ax, H, 3.0, cols, filas, H * 0.84, H * 0.075, H * 0.095)
    ax.text(3.0, y - H * 0.09, "Se firma o no se firma el acta, y qué falta para firmarla:",
            ha="left", va="center", family=F, fontsize=NOTA * 0.85, color=MARINO)
    _caja(ax, 3.0, y - H * 0.135, 94.0, 0.4, GRIS)
    ax.text(50, H * 0.05, "Firma del equipo técnico: ____________", ha="center",
            va="center", family=F, fontsize=NOTA * 0.75, color=GRIS)
    _g(fig, "sost-s10_acta-encargo.png")


# ═════════════════════════════════════════════ 10 · cómo trabajamos
def como_trabajamos():
    ASP = 1.62
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    for txt, mins, color, y in (("Lean lo que trae y lo que vieron", 3, AZUL, H * 0.72),
                                ("Llenen el acta, una fila por verificación", 12, MARINO, H * 0.53),
                                ("Escriban si se firma, y qué falta", 3, VERDE, H * 0.34)):
        _redonda(ax, 3.0, y, 78.0, H * 0.16, CLARO)
        ax.text(6.0, y + H * 0.08, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.92, color=MARINO)
        _redonda(ax, 83.0, y, 14.0, H * 0.16, color)
        ax.text(90.0, y + H * 0.08, "%d min" % mins, ha="center", va="center",
                family=F, fontsize=NOTA, fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.10, "En parejas · 18 minutos · se entrega el acta de recepción",
            ha="center", va="center", family=F, fontsize=NOTA * 0.92,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s10_como-trabajamos.png")


# ══════════════════════════════════════════════ 11 · puesta en común
def puesta_comun():
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _pasos(ax, H, [("Empezamos por los dos pernos flojos", "qué prueba les toca y quién responde"),
                   ("Seguimos por el concreto delgado", "con qué se mide y quién lo mide"),
                   ("Cerramos por la firma", "se firma o no, y qué falta para firmar")],
           H * 0.72, H * 0.185)
    _cierre(ax, H, "Responde la pareja, no el que sabe", H * 0.07)
    _g(fig, "sost-s10_puesta-comun.png")


# ═══════════════════════════════════════════════ 12 · una última
def una_ultima():
    ASP = 2.00
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    _redonda(ax, 8.0, H * 0.52, 84.0, H * 0.30, CLARO)
    ax.text(50, H * 0.67, "El certificado del proveedor es cierto\ny está bien emitido",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            color=MARINO, linespacing=1.4)
    _redonda(ax, 12.0, H * 0.14, 76.0, H * 0.24, AMBAR)
    ax.text(50, H * 0.26, "¿Por qué entonces no alcanza para firmar el acta?",
            ha="center", va="center", family=F, fontsize=NOTA * 0.95,
            fontweight="bold", color=MARINO)
    _g(fig, "sost-s10_una-ultima.png")


# ═══════════════════════════════════════════════ 13 · antes de irnos
def reflexion():
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP
    preguntas = ["Vuelve a las tres líneas que\nescribiste al inicio",
                 "¿Qué verificación no puede\nesperar a los veintiocho días?",
                 "La próxima: qué se hace cuando\nel terreno cambia después"]
    y = H * 0.74
    for txt, color in zip(preguntas, (AZUL, MARINO, VERDE)):
        _redonda(ax, 3.0, y, 94.0, H * 0.19, CLARO)
        _caja(ax, 3.0, y, 1.6, H * 0.19, color)
        ax.text(9.0, y + H * 0.095, txt, ha="left", va="center", family=F,
                fontsize=CUERPO * 0.88, color=MARINO, linespacing=1.35)
        y -= H * 0.225
    _g(fig, "sost-s10_reflexion.png")


TODOS = [de_donde_venimos, lo_que_se_mira_en_un_perno, las_probetas,
         lo_que_obliga_el_reglamento, registrar_no_es_archivar,
         material_vs_instalacion, el_certificado, caminando_el_tramo,
         acta_encargo, como_trabajamos, puesta_comun, una_ultima, reflexion]


def main():
    for f in TODOS:
        f()
        print("  ok  %s" % f.__name__)
    print("\n  %d esquemas en EOM/esquemas/%s" % (len(TODOS), CARPETA))


if __name__ == "__main__":
    main()
