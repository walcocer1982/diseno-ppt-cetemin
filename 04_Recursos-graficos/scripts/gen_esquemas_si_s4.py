# -*- coding: utf-8 -*-
"""Esquemas de la sesión 4 de SI-SGCSSMA · liderazgo, política y roles · 5.1-5.3

QUÉ SE RECICLA SIN TOCAR
    politica-pared_estimulo · liderazgo_no-es-firmar · delegar_no-libera
    politica_que-es · politica_que-dice · politica_como-se-difunde
    roles_quien-responde · roles_asignar-con-nombre · ruta-de-aprendizaje_s4

Uso:  python gen_esquemas_si_s4.py
"""
from __future__ import annotations

import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      caso, cen, izq)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Hasta dónde llega el sistema", "Y cómo se ordena por procesos"], AZUL2),
        ("HOY", ["Quién responde por él", "Y qué declara la empresa por escrito"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Un proceso sin responsable y una política sin firma se parecen mucho",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_puente.png", DEST)


def difusion_se_comprueba():
    im, d = lienzo(1000)
    y = comparativa(d, "NO ES DIFUNDIR", "SÍ ES DIFUNDIR", [
        (["Enmarcarla en la pared"], ["Que cada uno sepa qué le toca"]),
        (["Mandarla por correo una vez"], ["Explicarla donde se trabaja"]),
        (["Mirar el marco"], ["Preguntar y que respondan"]),
    ], y=50)
    banda(d, y + 20, 140, "Se revisa cuando cambia el contexto o el alcance", px=CUE)
    return guardar(im, "s4_difusion-se-comprueba.png", DEST)


def politica_integrada():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("TRES POLÍTICAS", ["Una de calidad", "Una de ambiente", "Una de seguridad y salud"], GRIS),
        ("O UNA SOLA", ["Que cubra los compromisos de las tres", "Firmada una vez, revisada una vez"], AZUL2),
    ], im, y=60, alto=320)
    banda(d, y + 20, 140, "Las tres normas piden política, y con la misma estructura", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_politica-integrada.png", DEST)


def politica_integrada_riesgo():
    im, d = lienzo(1000)
    y = comparativa(d, "MAL INTEGRADA", "BIEN INTEGRADA", [
        (["Se mezclan y se pierde alguno"], ["Están los compromisos de las tres"]),
        (["Habla solo de calidad"], ["Nombra requisitos legales y mejora"]),
        (["Nadie sabe qué norma cubre"], ["Se ve que el sistema es uno"]),
    ], y=50)
    banda(d, y + 20, 140, "Es el primer documento donde se ve si el sistema está integrado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_politica-integrada-riesgo.png", DEST)


def encargo():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("PASO 1", ["La política contra lo que exige la norma", "Y si cubre los tres sistemas"], AZUL2),
        ("PASO 2", ["Cada hecho con el rol que responde", "Y si ese rol está asignado"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Señalen lo que le falta a la política y lo que se quedó sin dueño",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s4_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(1780)
    y = caso(d, "CASO A", "Planta de Tratamiento de Aguas Industriales S.A.C.  ·  auditoría del cliente el jueves",
        ["H1 · La política cabe en cuatro líneas y lleva dos años en la pared de la sala de control",
         "H2 · Al pie está la firma del gerente general",
         "H3 · De los tres operadores presentes en la auditoría anterior, ninguno supo decir qué dice",
         "H4 · El mes pasado el cliente rechazó dos lotes de agua tratada: sólidos fuera de límite",
         "H5 · Cada lote rechazado cuesta S/ 12 000 en retratamiento",
         "H6 · El acta de septiembre está firmada por los seis jefes, con «calidad» en la agenda",
         "H7 · El gerente pidió «bajar los rechazos»: sin plazo y sin decir cómo se mide",
         "H8 · Si vuelve a haber rechazos, el contrato no se renueva en enero"],
        color=AZUL2, y=50, alto=190)
    banda(d, y + 24, 140, "Un operador contó que en su planta anterior un lote fuera de límite llegó a la red",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(1780)
    y = caso(d, "CASO B", "Servicios de Alimentación para Campamento S.A.C.  ·  auditoría de inocuidad el lunes",
        ["H1 · La política ocupa media página: inocuidad, seguridad, ambiente y comunidad",
         "H2 · La firmó el jefe de operaciones en enero, porque el gerente estaba de viaje",
         "H3 · Está enmarcada, con el sello de la certificadora y la fecha de renovación al pie",
         "H4 · Está en el mural del comedor, impresa en letra pequeña",
         "H5 · El cliente reclamó tres veces: raciones servidas sin registro de temperatura",
         "H6 · Las tres veces el cocinero dijo que nadie le explicó quién revisa el registro",
         "H7 · El gerente pidió «mejorar el servicio» al área de operaciones",
         "H8 · El contrato se renueva en noviembre"],
        color=TEAL, y=50, alto=190)
    banda(d, y + 24, 140, "El cocinero contó que en otro campamento una tanda mal conservada mandó a doce a tópico",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("ENTREGAN", ["La política revisada", "Con lo que le falta señalado"], AZUL2),
        ("Y ADEMÁS", ["Cada hecho con su rol responsable", "Marcando los que no tienen dueño"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1180)
    y = franjas(d, [
        ("AFIRMACIÓN", ["A esta política le falta este requisito"], AZUL2),
        ("APOYO", ["Y lo vemos en lo que dice, o en lo que no dice"], TEAL),
        ("PREGUNTA", ["¿Qué le falta para estar integrada?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 140, "Dos minutos por equipo. Empezamos por los requisitos que faltan",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s4_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1200)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que una política de gestión era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿De qué responde tu jefe que nadie ha puesto por escrito?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s4_reflexion.png", DEST)


# ── la politica real ────────────────────────────────────────────────────────
# NO es un esquema dibujado: es el recorte de un documento publico de un tercero.
# Se muestra como ejemplo de clase, con su atribucion en la propia lamina.
# Fuente: STRACON Group, «Politica del Sistema Integrado de Gestion», documento
# de gobierno corporativo publicado por la empresa. Sin restriccion de uso.
PDF_POLITICA = os.path.join(
    os.path.expanduser("~"), ".claude", "projects",
    "c--Users-jorge-Claude-diseno-ppt-cetemin",
    "4fd4dd2c-c9ec-4379-ba8d-c63df18ae0de", "tool-results",
    "webfetch-1788455900580-wtfis1.pdf")


def politica_real():
    """Recorte legible de una politica integrada publicada, con sus etiquetas.

    POR QUE UN RECORTE Y NO LA PAGINA ENTERA
        Una A4 completa metida en una lamina apaisada se escala por el alto y su
        cuerpo se proyecta a 5 pt: ilegible. El recorte de los tres primeros
        compromisos es apaisado, entra por el ancho, y se proyecta a 16 pt.
    """
    import pymupdf
    from PIL import Image as _Im
    pag = pymupdf.open(PDF_POLITICA)[1]
    pix = pag.get_pixmap(dpi=200)
    doc = _Im.frombytes("RGB", (pix.width, pix.height), pix.samples)
    recorte = doc.crop((0, 641, doc.width, 1123))          # compromisos 1 a 3

    # El alto de la banda se mide para que el conjunto quede APAISADO por encima
    # de 2,10: asi la lamina lo encaja por el ANCHO y el cuerpo se proyecta a 16 pt.
    # Con una banda mas alta entraria por el alto y bajaria a 12.
    ALTO_BANDA = 280
    im = _Im.new("RGB", (recorte.width, recorte.height + ALTO_BANDA), BLANCO)
    im.paste(recorte, (0, 0))
    from PIL import ImageDraw
    d = ImageDraw.Draw(im)
    y0 = recorte.height + 16
    ancho = (recorte.width - 100 - 2 * 24) / 3
    x = 50
    for etq, cual, col in [("1", "Ambiente de trabajo seguro", AZUL2),
                           ("2", "Requisitos legales", TEAL),
                           ("3", "Eliminar peligros", MORADO)]:
        d.rounded_rectangle([x, y0, x + ancho, y0 + 168], 18, fill=col)
        cen(d, x, y0 + 22, ancho, etq, 62, BLANCO)
        cen(d, x, y0 + 104, ancho, cual, 42, BLANCO, False)
        x += ancho + 24
    d.rounded_rectangle([50, y0 + 190, recorte.width - 50, y0 + 258], 14, fill=GRISC)
    cen(d, 50, y0 + 208, recorte.width - 100,
        "STRACON Group · Política del Sistema Integrado de Gestión · documento público",
        38, GRIS, False)
    return guardar(im, "s4_politica-real.png", DEST)


def politica_real_2():
    """Los compromisos 4 a 6 de la misma politica, y como cierra.

    Van en una segunda lamina porque los seis juntos ocupan una A4 en vertical:
    encajada en la lamina apaisada bajaria a 5 pt. Partida en dos, cada mitad
    entra por el ancho y se lee a 16 pt.
    """
    import pymupdf
    from PIL import Image as _Im, ImageDraw
    pag = pymupdf.open(PDF_POLITICA)[1]
    pix = pag.get_pixmap(dpi=200)
    doc = _Im.frombytes("RGB", (pix.width, pix.height), pix.samples)
    recorte = doc.crop((0, 1123, doc.width, 1650))         # compromisos 4 a 6

    ALTO_BANDA = 300
    im = _Im.new("RGB", (recorte.width, recorte.height + ALTO_BANDA), BLANCO)
    im.paste(recorte, (0, 0))
    d = ImageDraw.Draw(im)
    y0 = recorte.height + 16
    ancho = (recorte.width - 100 - 2 * 24) / 3
    x = 50
    for etq, cual, col in [("4", "Medio ambiente", TEAL),
                           ("5", "Calidad y mejora", AZUL2),
                           ("6", "Participación", MORADO)]:
        d.rounded_rectangle([x, y0, x + ancho, y0 + 168], 18, fill=col)
        cen(d, x, y0 + 22, ancho, etq, 62, BLANCO)
        cen(d, x, y0 + 104, ancho, cual, 42, BLANCO, False)
        x += ancho + 24
    d.rounded_rectangle([50, y0 + 190, recorte.width - 50, y0 + 278], 14, fill=AMBAR)
    cen(d, 50, y0 + 210, recorte.width - 100,
        "Cierra diciendo que está difundida a todos los niveles, y la firma el CEO",
        42, AZUL)
    return guardar(im, "s4_politica-real-2.png", DEST)


def politica_real_pagina():
    """La pagina entera del documento: logo, cabecera, los seis compromisos y la firma.

    ESTA LAMINA NO ES PARA LEER, ES PARA VER. El cuerpo de la pagina queda a 5 pt
    proyectados y da igual: los compromisos ya se leyeron en las dos laminas
    anteriores. Aqui el estudiante ve la FORMA del documento —de donde sale el
    logo, donde va la firma— y la columna de la derecha, esa si legible, le dice
    en que fijarse.
    """
    import pymupdf
    from PIL import Image as _Im, ImageDraw
    pag = pymupdf.open(PDF_POLITICA)[1]
    pix = pag.get_pixmap(dpi=200)
    doc = _Im.frombytes("RGB", (pix.width, pix.height), pix.samples)

    ALTO = 1020
    pagina = doc.resize((int(doc.width * ALTO / doc.height), ALTO))
    ANCHO = 2140
    im = _Im.new("RGB", (ANCHO, ALTO + 40), BLANCO)
    im.paste(pagina, (30, 20))
    d = ImageDraw.Draw(im)
    d.rectangle([30, 20, 30 + pagina.width, 20 + ALTO], outline=(200, 206, 210), width=3)

    x0 = 30 + pagina.width + 50
    ancho = ANCHO - x0 - 40
    y = 30
    for etq, txt, col in [
        ("ARRIBA", "El logo de la empresa: la política es suya, no de la certificadora", AZUL2),
        ("EN MEDIO", "Los seis compromisos, numerados y en un solo bloque", TEAL),
        ("ABAJO", "«Difundida a todos los niveles y disponible para los stakeholders»", MORADO),
        ("AL PIE", "La firma de la máxima autoridad: el CEO del grupo", AMBAR),
    ]:
        tinta = AZUL if col == AMBAR else BLANCO
        d.rounded_rectangle([x0, y, x0 + ancho, y + 200], 18, fill=col)
        izq(d, x0 + 34, y + 26, etq, 46, tinta, True, ancho=ancho - 68)
        izq(d, x0 + 34, y + 90, txt, CUE, tinta, ancho=ancho - 68)
        y += 228
    d.rounded_rectangle([x0, y, x0 + ancho, y + 84], 14, fill=GRISC)
    izq(d, x0 + 30, y + 22, "STRACON Group · documento público", NOTA, GRIS, ancho=ancho - 60)
    return guardar(im, "s4_politica-real-pagina.png", DEST)


# ── las dos politicas del caso ──────────────────────────────────────────────
# No son hechos sueltos: son DOS DOCUMENTOS para comparar contra lo aprendido.
# Cada uno entra en UNA lamina, apaisado y legible: 2100x1000 da 21 pt proyectados.

def _documento(nombre, titulo, datos, compromisos, firma, cargo, color, arch, firmado=False):
    from PIL import Image as _Im, ImageDraw
    # Con seis compromisos el cuerpo necesita mas alto. A 2100x1240 el conjunto
    # sigue apaisado y el cuerpo se proyecta a 17 pt: por encima del minimo.
    ANCHO, ALTO = 2100, 1240
    im = _Im.new("RGB", (ANCHO, ALTO), BLANCO)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, ANCHO, ALTO], outline=(200, 206, 210), width=4)

    d.rectangle([4, 4, ANCHO - 4, 180], fill=color)
    izq(d, 44, 44, nombre, 58, BLANCO, True, ancho=1250)
    izq(d, 44, 112, "SISTEMA DE GESTIÓN", 40, BLANCO, ancho=1250)
    x = 1400
    d.rounded_rectangle([x, 26, ANCHO - 40, 158], 12, fill=BLANCO)
    for i, t in enumerate(datos):
        izq(d, x + 24, 40 + i * 40, t, 34, GRIS, ancho=ANCHO - 40 - x - 48)

    d.rectangle([4, 180, ANCHO - 4, 286], fill=AMBAR)
    cen(d, 40, 210, ANCHO - 80, titulo, 52, AZUL)

    y = 330
    for i, c in enumerate(compromisos, 1):
        d.ellipse([54, y - 4, 54 + 46, y + 42], fill=color)
        cen(d, 54, y + 1, 46, str(i), 36, BLANCO, margen=0)
        y = izq(d, 128, y, c, CUE, AZUL, ancho=ANCHO - 220) + 26

    if firmado:
        # rubrica a mano alzada: dos trazos sueltos sobre la linea de firma
        import math as _m
        cx, cy = ANCHO / 2, ALTO - 176
        pts = []
        for k in range(0, 121):
            t = k / 120.0
            pts.append((cx - 210 + 420 * t,
                        cy + 34 * _m.sin(t * 9.4) * (1 - t * 0.45) - 26 * t))
        d.line(pts, fill=AZUL, width=5, joint="curve")
        d.line([(cx - 170, cy + 40), (cx + 120, cy + 30), (cx + 190, cy + 44)],
               fill=AZUL, width=4, joint="curve")
    d.line([ANCHO / 2 - 320, ALTO - 150, ANCHO / 2 + 320, ALTO - 150], fill=GRIS, width=3)
    cen(d, ANCHO / 2 - 400, ALTO - 132, 800, firma, CUE, AZUL)
    cen(d, ANCHO / 2 - 400, ALTO - 76, 800, cargo, NOTA, GRIS, False)
    return guardar(im, arch, DEST)


def politica_a():
    """CLAVE: bien controlada y FIRMADA por la maxima autoridad, pero NO integrada."""
    return _documento(
        "SONDAJES Y GEOTECNIA DEL SUR S.A.C.", "POLÍTICA DE CALIDAD",
        ["Código: SGS.SGC.POL.01", "Versión: 01", "Aprobación: 12/03/2021"],
        ["Satisfacer los requisitos de nuestros clientes, entregando el servicio "
         "en el plazo y las condiciones pactadas.",
         "Cumplir los requisitos legales y otros requisitos que la organización suscriba.",
         "Mejorar continuamente la eficacia del sistema de gestión de la calidad.",
         "Establecer y revisar objetivos de calidad medibles en cada proceso.",
         "Asegurar la disponibilidad de los recursos necesarios para mantener el sistema.",
         "Capacitar al personal en los procedimientos que le corresponden."],
        "Ing. Ana Beltrán", "Gerente General", AZUL2, "s4_politica-a.png", firmado=True)


def politica_b():
    """CLAVE: cubre los tres sistemas, pero sin control documental, SIN FIRMA,
    y le faltan dos compromisos obligatorios: requisitos legales y participacion."""
    return _documento(
        "MONTAJE DE ESTRUCTURAS METÁLICAS S.A.C.",
        "POLÍTICA INTEGRADA DE GESTIÓN",
        ["Código:  —", "Versión:  —", "Aprobación:  —"],
        ["Prevenir lesiones y deterioro de la salud de nuestros trabajadores mediante "
         "la identificación de peligros y el control de los riesgos.",
         "Proteger el medio ambiente previniendo la contaminación y gestionando "
         "los residuos de nuestras operaciones.",
         "Entregar estructuras que cumplan las especificaciones acordadas con el cliente.",
         "Establecer objetivos anuales para cada uno de los tres sistemas.",
         "Promover un clima laboral de respeto y colaboración entre todo el personal.",
         "Mejorar continuamente el desempeño del sistema integrado de gestión."],
        "Ing. Luis Ramírez", "Jefe de SSOMA", TEAL, "s4_politica-b.png", firmado=False)


def encargo_politicas():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("PASO 1", ["Marcar los seis requisitos", "que la norma pide a una política"], AZUL2),
        ("PASO 2", ["¿Está integrada?", "¿Y quién tendría que firmarla?"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Una empresa titular va a revisarlas antes de autorizar el ingreso",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s4_encargo.png", DEST)


def a_trabajar_politicas():
    im, d = lienzo(1250)
    y = franjas(d, [
        ("MARCAN", ["Propósito y tamaño", "Requisitos legales", "Mejora continua"], AZUL2),
        ("Y TAMBIÉN", ["Marco para los objetivos", "Consulta y participación", "Firma de la máxima autoridad"], TEAL),
    ], im, y=60, alto=330)
    banda(d, y + 20, 130, "Después: ¿cubre los tres sistemas? ¿Qué le falta para estar integrada?",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "30 min de trabajo  ·  equipos de 4  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s4_a-trabajar.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 4")
    for fn in (puente, difusion_se_comprueba, politica_integrada, politica_integrada_riesgo,
               formato_discusion, reflexion,
               politica_real, politica_real_2, politica_real_pagina,
               politica_a, politica_b, encargo_politicas, a_trabajar_politicas):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
