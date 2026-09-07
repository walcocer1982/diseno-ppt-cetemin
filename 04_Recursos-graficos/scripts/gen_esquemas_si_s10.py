# -*- coding: utf-8 -*-
"""Esquemas de la sesión 10 de SI-SGCSSMA · comunicación e información documentada · 7.4–7.5

Trae además la lámina de pautas del TC1. Sus datos —tres entregables, cuatro roles,
dos horas y doce minutos de sustentación— salen del propio `06_TC1_Indicaciones.docx`,
no se inventan aquí: si el TC1 cambia, esta figura se rehace.

Lo legal sale del §15, verificado el 2026-09-03:
  DS 005-2012-TR · 33 los ocho registros · 34 tercerización y formatos · 35 los tres
  plazos y el archivo activo de doce meses · 36 derecho a consultar los registros ·
  37 a) b) c) comunicación interna, externa y sugerencias atendidas

Uso:  python gen_esquemas_si_s10.py
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
        ("20'", "CONEXIÓN", "Dos versiones del mismo método, conviviendo", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué se comunica, qué se controla y qué se conserva", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas y un papel que no sirvió", MORADO),
        ("20'", "DISCUSIÓN", "Qué falló en cada uno, y las pautas del TC1", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s10.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Con qué gente y qué recursos", "Se ejecuta el programa"], AZUL2),
        ("HOY", ["Qué se comunica y a quién", "Y qué papel prueba lo que se hizo"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Se cierra la cláusula 7: lo que sostiene al sistema por dentro",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_puente.png", DEST)


def estimulo():
    """Las dos versiones del metodo, conviviendo. Solo hechos."""
    im, d = lienzo(880)
    cen(d, 50, 60, W - 100, "El mismo método de ensayo, en dos sitios de la empresa",
        50, AZUL, True)
    mid = W / 2
    for x0, x1, titulo, lineas, col in (
            (50, mid - 20, "REVISIÓN 2",
             ["Hoja plastificada", "Pegada al equipo", "Vigente desde 2023",
              "La usan los tres analistas"], AZUL2),
            (mid + 20, W - 50, "REVISIÓN 4",
             ["Archivo adjunto", "En el correo del jefe", "Llegó en abril, un jueves",
              "No la abrió nadie más"], TEAL)):
        d.rounded_rectangle([x0, 170, x1, 700], 18, fill=GRISC)
        d.rounded_rectangle([x0, 170, x1, 290], 18, fill=col)
        d.rectangle([x0, 250, x1, 290], fill=col)
        cen(d, x0, 196, x1 - x0, titulo, 54, BLANCO, True)
        y = 340
        for t in lineas:
            cen(d, x0 + 30, y, x1 - x0 - 60, t, CUE, AZUL, False)
            y += 88
    banda(d, 730, 130, "Las dos están escritas, firmadas y guardadas", px=CUE)
    return guardar(im, "s10_estimulo.png", DEST)


def comunicacion():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("INTERNA", ["Entre los distintos niveles y cargos", "DS 005, artículo 37 b)"], AZUL2),
        ("EXTERNA", ["Cliente, contratistas, autoridad y vecinos", "DS 005, artículo 37 a)"],
         TEAL),
        ("SUGERENCIAS", ["Las de los trabajadores se reciben y se atienden",
                         "DS 005, artículo 37 c)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "La cláusula 7.4 pide decidir qué se comunica, a quién, cuándo y cómo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_comunicacion.png", DEST)


def recibir_y_responder():
    im, d = lienzo(1010)
    y = comparativa(d, "NO ES COMUNICAR", "SÍ ES COMUNICAR", [
        (["Poner un buzón que nadie abre"], ["Recibir, documentar y responder"]),
        (["Mandar el correo y darlo por leído"], ["Confirmar que llegó a quien lo usa"]),
        (["Anotar la sugerencia"], ["Atenderla y decirle en qué quedó"]),
    ], y=50)
    banda(d, y + 20, 150, "La norma no pide un buzón: pide respuesta oportuna y adecuada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_recibir-y-responder.png", DEST)


def doc_y_registro():
    im, d = lienzo(1080)
    y = tabla(d, ["DOCUMENTO", "REGISTRO"], [
        ([["Dice cómo se hace algo"], ["Prueba que se hizo"]], "", None, None),
        ([["Procedimiento, plano, método"], ["Acta, cargo, planilla, informe"]],
         "", None, None),
        ([["Lleva versión, y se actualiza"], ["Lleva fecha, y se conserva"]], "", None, None),
    ], [50, W / 2, W - 50], y=50)
    banda(d, y + 30, 150, "Las tres normas los llaman igual: información documentada",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_doc-y-registro.png", DEST)


def no_se_corrige():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("CAMBIA", ["El documento sale en una versión nueva", "Y la vieja se retira"], AZUL2),
        ("NO CAMBIA", ["El registro no se corrige ni se rehace", "Se conserva como quedó"],
         TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "Corregir un registro para que cuadre no es controlarlo: es falsearlo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_no-se-corrige.png", DEST)


def control_1():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("APRUEBA", ["Alguien lo aprueba antes de que se use"], AZUL2),
        ("IDENTIFICA", ["Código, versión y fecha en el documento"], TEAL),
        ("DISTRIBUYE", ["Llega a quien lo usa, no al correo del jefe"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 140, "Tres pasos del control, y el tercero es el que más se salta", px=CUE)
    return guardar(im, "s10_control-1.png", DEST)


def control_2():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("VIGENTE", ["La versión nueva desplaza a la vieja", "En el puesto de trabajo"],
         AZUL2),
        ("OBSOLETA", ["Se retira, o se marca para que nadie la use"], TEAL),
        ("CONSULTA", ["El trabajador puede consultar los registros",
                      "DS 005, artículo 36"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Salvo los de su salud, que necesitan su autorización escrita",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_control-2.png", DEST)


def registros_1():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("a", "ACCIDENTES", "Y enfermedades e incidentes, con investigación y medidas", AZUL2),
        ("b", "SALUD", "Exámenes médicos ocupacionales", TEAL),
        ("c", "MONITOREO", "Agentes físicos, químicos, biológicos y ergonómicos", MORADO),
        ("d", "INSPECCIONES", "Inspecciones internas de seguridad y salud", AMBAR),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s10_registros-1.png", DEST)


def registros_2():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("e", "ESTADÍSTICAS", "Estadísticas de seguridad y salud", AZUL2),
        ("f", "EQUIPOS", "Equipos de seguridad o emergencia", TEAL),
        ("g", "FORMACIÓN", "Inducción, capacitación, entrenamiento y simulacros", MORADO),
        ("h", "AUDITORÍAS", "Los ocho salen del artículo 33 del DS 005", AMBAR),
    ], y=50, alto=280, sep=30)
    return guardar(im, "s10_registros-2.png", DEST)


def plazos():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("VEINTE", ["Años: enfermedades ocupacionales"], ROJO),
        ("DIEZ", ["Años: accidentes de trabajo e incidentes peligrosos"], AMBAR),
        ("CINCO", ["Años: todos los demás registros"], AZUL2),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Artículo 35 del DS 005. Decir «todo se guarda veinte años» es falso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_plazos.png", DEST)


def archivo():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("ACTIVO", ["Los últimos doce meses, a la mano"], AZUL2),
        ("PASIVO", ["Después, guardado por el plazo que le toque"], TEAL),
        ("TERCEROS", ["La empresa principal también los registra",
                      "DS 005, artículo 34"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Si trabajan en tus instalaciones, entran en tus registros",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_archivo.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué era documento y qué registro", "Y qué falló en cada uno"], AZUL2),
        ("PASO 2", ["Dónde falló la comunicación", "Y qué pasa el viernes"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas pierden dinero el viernes por un papel",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s10_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Servicios Analíticos Industriales S.A.C.  ·  laboratorio de ensayo químico  ·  22 trabajadores",
        ["H1 · El cliente reclama 240 000 soles por diferencia de ley en tres embarques",
         "H2 · El método de ensayo cambió en abril: la revisión 4 baja el límite de cuantificación",
         "H3 · La revisión 4 llegó al correo del jefe de laboratorio, un jueves. De ahí no salió",
         "H4 · Los tres analistas siguen con la hoja plastificada del equipo: revisión 2, de hace tres años",
         "H5 · La carpeta de calibraciones está impecable: doce hojas firmadas por el mismo jefe",
         "H6 · Un analista escribió dos veces avisando que los resultados no cuadraban. Nadie respondió",
         "H7 · Los registros de accidentes se depuran cada año; los del año pasado ya se eliminaron",
         "H8 · No hay lista de qué documentos están controlados ni quién los aprueba"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "El cliente pide el dossier del método el viernes",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Ingeniería y Montaje Electromecánico S.A.C.  ·  64 trabajadores  ·  ocho meses en obra",
        ["H1 · Cada día de atraso en el acta de entrega cuesta 8 000 soles",
         "H2 · Los soportes del tramo 3 se montaron con el plano revisión B; los del tramo 5, con la C",
         "H3 · La revisión C llegó por WhatsApp al capataz, un sábado",
         "H4 · En la caseta hay impresos de las dos revisiones, y ninguno tiene sello ni fecha",
         "H5 · El registro de torque está completo y dentro de tolerancia: la de la revisión B",
         "H6 · Nadie controla los planos: el residente lo hace «cuando puede»",
         "H7 · Un soldador preguntó cuál revisión mandaba; le dijeron que consultara al capataz",
         "H8 · Los registros de inducción están en el celular del prevencionista, que rotó a otra obra"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "La faja se entrega el viernes",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Documentos y registros separados", "Con lo que falló en cada uno"],
         AZUL2),
        ("Y ADEMÁS", ["Dónde falló la comunicación", "Con el artículo que lo manda"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este papel era documento, y este era registro"], AZUL2),
        ("APOYO", ["Y decimos qué falló en su control"], TEAL),
        ("PREGUNTA", ["¿En qué momento se pudo haber parado esto?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por el papel que sí estaba firmado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_discusion.png", DEST)


def pautas_tc1():
    """Los datos salen de 06_TC1_Indicaciones.docx. No se inventan aqui."""
    im, d = lienzo(1360)
    y = franjas(d, [
        ("ENTREGAN", ["El informe de brechas, el anexo con la hoja de trabajo",
                      "Y el PPT: portada y seis láminas"], AZUL2),
        ("ROLES", ["Analista, cumplimiento normativo, programa anual y jefatura",
                   "Uno por integrante"], TEAL),
        ("TIEMPO", ["2 horas de trabajo autónomo, en equipos de 4",
                    "Sustentación de 12 minutos"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 150, "Trabajo colaborativo 1 · sobre las cláusulas 4 a 7, las que ya vimos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s10_pautas-tc1.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que tener el papel firmado era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué versión están usando ahora mismo donde trabajas?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s10_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 10")
    for fn in (ruta, puente, estimulo, comunicacion, recibir_y_responder, doc_y_registro,
               no_se_corrige, control_1, control_2, registros_1, registros_2, plazos,
               archivo, encargo, ficha_caso_a, ficha_caso_b, a_trabajar, formato_discusion,
               pautas_tc1, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
