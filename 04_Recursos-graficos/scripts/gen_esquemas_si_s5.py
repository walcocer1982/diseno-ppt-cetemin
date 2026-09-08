# -*- coding: utf-8 -*-
"""Esquemas de la sesión 5 de SI-SGCSSMA · consulta y participación · 5.4 (45001)

La sesión se escribió entera, así que casi todo es nuevo: solo se reciclan la
escala de ánimo y la ruta de aprendizaje.

El umbral del órgano está verificado contra el §15: Ley 29783 artículo 29
—veinte o más trabajadores, comité paritario— y artículo 30 —menos de veinte,
supervisor nombrado por los propios trabajadores.

Uso:  python gen_esquemas_si_s5.py
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
    """La ruta traia los subtitulos de la sesion vieja —los documentos de la ley—,
    asi que se rehace con lo que la sesion hace ahora."""
    im, d = lienzo(1620)
    filas_letra(d, [
        ("20'", "CONEXIÓN", "¿A alguien le preguntaron antes de decidir?", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué exige la 45001 y con qué órgano se cumple aquí", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas y la evidencia que entregaron", MORADO),
        ("20'", "DISCUSIÓN", "El órgano que corresponde, y quién se queda sin voz", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s5.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Qué debe decir la política", "Y quién tiene que firmarla"], AZUL2),
        ("HOY", ["A quién hay que preguntarle", "Antes de decidir por él"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "La política se firma arriba. La seguridad se decide con los de abajo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_puente.png", DEST)


def estimulo():
    """Un memorando de designacion. Solo hechos: el juicio lo pone el estudiante."""
    im, d = lienzo(960)
    d.rectangle([50, 50, W - 50, 760], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 200], fill=AZUL)
    izq(d, 90, 88, "MEMORANDO N.º 014-2026-GG", 52, BLANCO, True, ancho=W - 200)
    izq(d, 90, 148, "Servicios Eléctricos de Mina S.A.C.", 40, BLANCO, ancho=W - 200)
    y = 250
    for t in ["De: Gerencia General",
              "Para: todo el personal",
              "Asunto: designación del supervisor de seguridad y salud en el trabajo",
              "",
              "Se designa al Sr. Julio Antezana como supervisor de seguridad y salud en el "
              "trabajo, por su experiencia en la actividad."]:
        if t:
            y = izq(d, 90, y, t, CUE, AZUL, ancho=W - 180) + 14
        else:
            y += 30
    d.line([W / 2 - 220, 686, W / 2 + 220, 686], fill=GRIS, width=3)
    cen(d, W / 2 - 300, 700, 600, "Gerencia General", NOTA, GRIS, False)
    banda(d, 800, 130, "26 trabajadores en planilla · enero", px=CUE)
    return guardar(im, "s5_estimulo.png", DEST)


def solo_45001():
    """En tabla, no en comparativa: la comparativa pinta de rojo la columna izquierda, y
    aqui la 9001 y la 14001 no estan mal — sencillamente no traen esta clausula."""
    im, d = lienzo(1010)
    y = tabla(d, ["ISO 9001  ·  ISO 14001", "ISO 45001"], [
        ([["No traen esta cláusula"], ["5.4 Consulta y participación"]], "", None, None),
        ([["Hablan de comunicar"], ["Habla de decidir con la gente"]], "", None, None),
        ([["Miran al cliente y al entorno"], ["Mira a quien se juega la salud"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 140, "Es la única cláusula que exige una sola de las tres normas",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_solo-45001.png", DEST)


def por_que_existe():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("POR QUÉ", ["El trabajador conoce el peligro de su tarea", "Y es quien paga el error"], AZUL2),
        ("QUÉ ES", ["Un requisito auditable", "No una declaración de intenciones"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Aquí se ve si el sistema cuenta con la gente o solo con el papel",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_por-que-existe.png", DEST)


def tres_verbos():
    im, d = lienzo(1220)
    y = franjas(d, [
        ("INFORMAR", ["Avisar cuando ya está decidido"], GRIS),
        ("CONSULTAR", ["Pedir la opinión ANTES de decidir"], AZUL2),
        ("PARTICIPAR", ["Intervenir en la decisión y en lo que sigue"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "La norma pide las dos últimas, y no son intercambiables",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_tres-verbos.png", DEST)


def a_quien_le_toca():
    im, d = lienzo(1000)
    y = comparativa(d, "NO CUMPLE", "SÍ CUMPLE", [
        (["Avisar por correo"], ["Preguntar antes de comprar"]),
        (["Poner el aviso en la pared"], ["Que el trabajador esté en la decisión"]),
        (["Decidir y después contar"], ["Decidir con quien hace la tarea"]),
    ], y=50)
    banda(d, y + 20, 140, "A los trabajadores no directivos les toca consulta Y participación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_a-quien-le-toca.png", DEST)


def asuntos_1():
    im, d = lienzo(1250)
    y = franjas(d, [
        ("EMPEZAR", ["Qué esperan las partes interesadas"], AZUL2),
        ("DIRIGIR", ["La política", "Los roles y las responsabilidades"], TEAL),
        ("PLANIFICAR", ["Los peligros y los controles que se aplican"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Tres de los seis asuntos en que la norma obliga a consultar", px=CUE)
    return guardar(im, "s5_asuntos-1.png", DEST)


def asuntos_2():
    im, d = lienzo(1250)
    y = franjas(d, [
        ("FORMAR", ["Qué competencia y qué formación hacen falta"], AZUL2),
        ("INVESTIGAR", ["Qué pasó en el incidente y qué se hace"], TEAL),
        ("MEDIR", ["Cómo se hace el seguimiento del desempeño"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Si no queda constancia, para el sistema no se consultó",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_asuntos-2.png", DEST)


def comite_o_supervisor():
    """Tambien en tabla: ninguno de los dos lados esta mal. Cada uno es el organo que
    corresponde a su tamano, y pintar uno de rojo diria lo contrario."""
    im, d = lienzo(1060)
    y = tabla(d, ["MENOS DE VEINTE", "VEINTE O MÁS"], [
        ([["Supervisor de SST"], ["Comité de SST"]], "", None, None),
        ([["Ley 29783, artículo 30"], ["Ley 29783, artículo 29"]], "", None, None),
        ([["Lo nombran los propios trabajadores"],
          ["Paritario: mitad del empleador, mitad de los trabajadores"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "El número de trabajadores decide el órgano. No lo decide la empresa",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_comite-o-supervisor.png", DEST)


def quien_los_elige():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("ELIGEN", ["Los representantes de los trabajadores", "Con votación y con acta"], AZUL2),
        ("DESIGNAN", ["Los representantes del empleador", "Por la gerencia"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Designar a dedo al de los trabajadores no cumple ni la ley ni la 5.4",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_quien-los-elige.png", DEST)


def libro_de_actas():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("ACTA", ["Qué se trató", "Qué se acordó", "Quién estuvo"], AZUL2),
        ("PRUEBA", ["Es la prueba de la consulta", "Ante el cliente y ante el inspector"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Sin acta, la reunión no existe para el sistema", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_libro-de-actas.png", DEST)


def obstaculos():
    im, d = lienzo(1250)
    y = franjas(d, [
        ("ESTORBAN", ["El miedo a la represalia", "El horario en que se convoca"], ROJO),
        ("TAMBIÉN", ["El idioma en que se explica", "No saber cómo hacerlo"], GRIS),
    ], im, y=60, alto=330)
    banda(d, y + 20, 150, "La norma manda eliminarlos. Si reportar cuesta el puesto, no hay participación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_obstaculos.png", DEST)


def encargo():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("PASO 1", ["Qué órgano corresponde", "Y si el que hay cumple"], AZUL2),
        ("PASO 2", ["Qué asuntos se consultaron", "Y qué obstáculos aparecen"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas entregaron su evidencia de participación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s5_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(1900)
    y = caso(d, "CASO A", "Servicios Eléctricos de Mina S.A.C.  ·  adjunta el memorando de su supervisor",
        ["H1 · La empresa tiene 26 trabajadores en planilla",
         "H2 · Hay un supervisor de seguridad, designado por gerencia en enero",
         "H3 · No hubo elección: el memorando dice «se designa por su experiencia»",
         "H4 · El supervisor lleva un cuaderno con las charlas de cinco minutos",
         "H5 · Antes de comprar los arneses nuevos, nadie preguntó a los electricistas",
         "H6 · La política se difundió por correo; tres trabajadores no tienen correo",
         "H7 · Un técnico pidió cambiar la hora de la charla y le dijeron que no se podía",
         "H8 · No existe libro de actas"],
        color=AZUL2, y=50, alto=190)
    banda(d, y + 24, 140, "El cliente pide la evidencia de consulta y participación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(1900)
    y = caso(d, "CASO B", "Mantenimiento de Fajas y Chutes S.A.C.  ·  adjunta el acta de su comité",
        ["H1 · La empresa tiene 17 trabajadores en planilla",
         "H2 · Hay un comité de seguridad con cuatro miembros, los cuatro jefes de área",
         "H3 · A los cuatro los puso la gerencia: los trabajadores no eligieron a nadie",
         "H4 · El acta de la última reunión es de hace ocho meses",
         "H5 · En esa acta figura un solo punto: «se aprueba el programa anual»",
         "H6 · Al investigar el último incidente no participó ningún trabajador",
         "H7 · El buzón de sugerencias está dentro de la oficina del jefe de planta",
         "H8 · Dos operarios dicen que reportar una condición insegura «trae problemas»"],
        color=TEAL, y=50, alto=190)
    banda(d, y + 24, 140, "El cliente pide la evidencia de consulta y participación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("ENTREGAN", ["El órgano que corresponde", "Con el número que lo decide"], AZUL2),
        ("Y ADEMÁS", ["Los asuntos consultados y los que no", "Los obstáculos que aparecen"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["A esta empresa le toca este órgano"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el número y en la ley"], TEAL),
        ("PREGUNTA", ["¿Quién se queda sin voz mientras siga así?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 140, "Dos minutos por equipo. Empezamos por el órgano que corresponde",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s5_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que consultar a los trabajadores era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Cuándo fue la última vez que te preguntaron antes de decidir?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s5_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 5")
    for fn in (ruta, puente, estimulo, solo_45001, por_que_existe, tres_verbos, a_quien_le_toca,
               asuntos_1, asuntos_2, comite_o_supervisor, quien_los_elige, libro_de_actas,
               obstaculos, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
