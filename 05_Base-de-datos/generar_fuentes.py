# -*- coding: utf-8 -*-
"""De dónde salió cada sesión: el documento de trazabilidad de fuentes.

    python generar_fuentes.py EOM-METEXP        (desde 05_Base-de-datos/)

Escribe 03_Entregables-diseño/<carpeta del curso>/02_Fuentes-por-sesion.pdf, con
una sección por sesión de adquisición: su aprendizaje esperado, de dónde sale el
caso, de dónde bajan los puntos clave y de dónde sale cada imagen que se proyecta.

POR QUÉ EXISTE
    La regla 3 del CLAUDE.md dice que nada físico se inventa: la fuente es el
    dibujo del fabricante, el plano o la fotografía real. Eso está registrado
    imagen por imagen en imagenes.csv y caso por caso en casos.csv, pero
    disperso: nadie puede abrir un PPT y decir de dónde salió lo que ve. Este
    documento junta lo que ya está en la base y lo pone por sesión.

    NO INVENTA NADA NI INVESTIGA: lee la base. Si una imagen no tiene fuente
    citable, el documento lo dice en la última sección en vez de disimularlo.

    Se genera, no se escribe. Si una fuente cambia, se corrige en imagenes.csv
    o en casos.csv y se vuelve a generar.
"""
from __future__ import print_function

import csv
import os
import re
import sys
import unicodedata

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSO = sys.argv[1] if len(sys.argv) > 1 else u"EOM-METEXP"
CARRERA = CURSO.split(u"-")[0]

MARINO = colors.HexColor("#0D2632")
AZUL = colors.HexColor("#167FB9")
GRIS = colors.HexColor("#6C7A82")
CLARO = colors.HexColor("#EEF1F3")
AMBAR = colors.HexColor("#FFC505")
BLANCO = colors.white


# ────────────────────────────────────────────────────────────── la base
def leer(nombre, carpeta=None):
    ruta = os.path.join(RAIZ, u"05_Base-de-datos", carpeta or u"", nombre)
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


cursos = leer(u"cursos.csv")
imagenes = {r[u"imagen_id"]: r for r in leer(u"imagenes.csv")}
sesiones = [r for r in leer(u"sesiones.csv", CARRERA) if r[u"curso_id"] == CURSO]
casos = {r[u"sesion_id"]: r for r in leer(u"casos.csv", CARRERA)
         if r.get(u"alcance") == u"sesion" and r.get(u"sesion_id")}
contenidos = leer(u"contenidos.csv", CARRERA)
laminas = leer(u"laminas.csv", CARRERA)
indicadores = {r[u"indicador_id"]: r[u"descripcion"] for r in leer(u"indicadores.csv", CARRERA)}
rubricas = [r for r in leer(u"rubricas.csv", CARRERA) if r.get(u"curso_id") == CURSO]

nombre_curso = next((c[u"nombre_curso"] for c in cursos if c[u"curso_id"] == CURSO), CURSO)


# ─────────────────────────────────────── las fuentes recurrentes, con su código
# El orden es el de aparición en el curso. Cada patrón se busca dentro del campo
# `fuente` de imagenes.csv y del `recursos` de casos.csv: es texto que YA está en
# la base, no una lista escrita a mano aquí.
FUENTES = [
    (u"F1", [u"unap.edu.pe", u"Ccaso Yucasi"],
     u"Ccaso Yucasi, E. I. (2018). <i>Evaluación económica en el avance de frentes "
     u"horizontales del Nv 4100 con barras de 16 pies, Mina Minsur S.A., Unidad Minera "
     u"Raura</i>. Tesis, UNAP.",
     u"https://repositorio.unap.edu.pe/handle/20.500.14082/8268"),
    (u"F2", [u"20.500.12918/10444", u"253T20242039"],
     u"Tesis UNSAAC, Escuela Profesional de Ingeniería de Minas, 253T20242039 "
     u"(malla de perforación real; figura de Atlas Copco Rock Drills AB).",
     u"https://repositorio.unsaac.edu.pe/handle/20.500.12918/10444"),
    (u"F3", [u"ingemmet", u"Parcoy", u"TE0380"],
     u"U.M. Parcoy, Consorcio Minero Horizonte. Tesis UNSAAC consultada vía INGEMMET "
     u"(TE0380): tabla geomecánica de labor con sus dos aberturas.",
     u"https://app.ingemmet.gob.pe/biblioteca/pdf/TE0380.pdf"),
    (u"F4", [u"uap.edu.pe", u"Constancia", u"ControlSense"],
     u"Tesis UAP sobre carguío y acarreo con ControlSense — Mina Constancia (Hudbay), "
     u"Chumbivilcas, Cusco: flota, pases por camión y destinos del material.",
     u"https://repositorio.uap.edu.pe/handle/20.500.12990/4327"),
    (u"F5", [u"undac"],
     u"Tesis UNDAC — parámetros reales de Cerro Lindo (Nexa Resources) y del tajeo 882: "
     u"buzamiento, RMR de mineral y cajas, subniveles y dimensiones de tajeo.",
     u"http://repositorio.undac.edu.pe/bitstream/undac/1881/1/T026_73583383_T.pdf"),
    (u"F6", [u"D.S. 024", u"024-2016-EM"],
     u"D.S. 024-2016-EM, Reglamento de Seguridad y Salud Ocupacional en Minería. "
     u"Art. 33 (tabla geomecánica publicada en cada labor) y Art. 224 (desatado). "
     u"Verificado contra el texto publicado, §15 de la base de conocimiento.", u""),
    (u"F7", [u"Hartmann"],
     u"Hartmann, C. (1843). <i>Grundzüge der Geologie</i>, fig. 7, pág. 36. "
     u"J. J. Weber, Leipzig. Obra de DOMINIO PÚBLICO.", u""),
    (u"F8", [u"Naumann"],
     u"Naumann, C. F. (1850). <i>Lehrbuch der Geognosie</i>, vol. 1, pág. 915. "
     u"Wilhelm Engelmann, Leipzig. Obra de DOMINIO PÚBLICO.", u""),
    (u"F9", [u"Epiroc"],
     u"Epiroc. Catálogos del fabricante: <i>Boomer S1 — Technical specification</i> y "
     u"<i>Scooptram ST14 SG — Technical specification</i> (9869 0237 01b, 2025-04), "
     u"Örebro, Suecia, p. 4 de cada uno.", u""),
    (u"F10", [u"EXSA"],
     u"EXSA. <i>Manual práctico de voladura</i>: carga de fondo y de columna, taco, "
     u"y la secuencia de encendido en túneles (cap. 6).", u""),
    (u"F11", [u"NIOSH", u"CDC"],
     u"CDC / NIOSH. <i>Dust Control Handbook for Industrial Minerals Mining and "
     u"Processing</i> (2012), fig. 3.17. Dominio público, vía Wikimedia Commons.", u""),
    (u"F13", [u"Wikimedia Commons"],
     u"Wikimedia Commons — originales de dominio público (autores fallecidos hace más "
     u"de 70 años) usados en los recursos de dinámica comunes a las tres carreras.", u""),
    (u"F12", [u"material de clase de CETEMIN", u"PPT oficial CETEMIN", u"PPT oficiales de CETEMIN"],
     u"Material de clase de CETEMIN (informes de trabajo colaborativo y PPT oficiales). "
     u"<b>Sin procedencia externa verificable.</b>", u""),
]


def codigos_de(texto):
    """Qué fuentes reconoce el texto de un campo `fuente` o `recursos`."""
    t = (texto or u"")
    vistos = []
    for cod, patrones, _, _ in FUENTES:
        if any(p.lower() in t.lower() for p in patrones) and cod not in vistos:
            vistos.append(cod)
    return vistos


def es_propia(texto):
    t = (texto or u"").lower()
    return u"elaboraci" in t and u"propia" in t


# ────────────────────────────────────────────────────────────── el documento
estilos = getSampleStyleSheet()


def E(nombre, **kw):
    base = dict(fontName="Helvetica", fontSize=9, leading=12.5, textColor=MARINO,
                spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(nombre, **base)


TITULO = E("titulo", fontName="Helvetica-Bold", fontSize=19, leading=23,
           textColor=MARINO, spaceAfter=4)
SUB = E("sub", fontSize=10.5, leading=14, textColor=GRIS, spaceAfter=16)
H1 = E("h1", fontName="Helvetica-Bold", fontSize=13.5, leading=17, textColor=AZUL,
       spaceBefore=6, spaceAfter=8)
H2 = E("h2", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=MARINO,
       spaceBefore=9, spaceAfter=3)
CUERPO = E("cuerpo", alignment=TA_JUSTIFY)
PIE = E("pie", fontSize=8, leading=10.5, textColor=GRIS)
CELDA = E("celda", fontSize=8, leading=10.5)
CELDA_B = E("celda_b", fontSize=8, leading=10.5, fontName="Helvetica-Bold")


def tabla(filas, anchos, cabecera=True):
    t = Table(filas, colWidths=anchos, hAlign="LEFT")
    estilo = [("VALIGN", (0, 0), (-1, -1), "TOP"),
              ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFBDB6")),
              ("LEFTPADDING", (0, 0), (-1, -1), 5),
              ("RIGHTPADDING", (0, 0), (-1, -1), 5),
              ("TOPPADDING", (0, 0), (-1, -1), 4),
              ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
    if cabecera:
        estilo += [("BACKGROUND", (0, 0), (-1, 0), MARINO),
                   ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO)]
    t.setStyle(TableStyle(estilo))
    return t


def cinta(texto, fondo=CLARO):
    t = Table([[Paragraph(texto, CUERPO)]], colWidths=[17 * cm], hAlign="LEFT")
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), fondo),
                           ("LEFTPADDING", (0, 0), (-1, -1), 8),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t


def limpio(t, n=None):
    t = u" ".join((t or u"").split())
    return t if not n or len(t) <= n else t[:n - 1] + u"…"


def tributa(sesion):
    """A qué criterio de qué colaborativo alimenta esta sesión."""
    inds = [i.strip() for i in (sesion.get(u"indicador_id") or u"").split(u";") if i.strip()]
    salida = []
    for r in rubricas:
        if r.get(u"indicador_id") in inds and r.get(u"n") in (u"1", u"2", u"3"):
            tc = u"TC1" if r[u"caso_id"].endswith(u"-1") else u"TC2"
            salida.append(u"%s · c%s %s" % (tc, r[u"n"], r[u"criterio"]))
    return salida


def anclaje_del_caso(caso):
    """El tramo de `recursos` donde el caso declara su fuente real."""
    rec = caso.get(u"recursos") or u""
    m = re.search(r"(ANCLAJE|FUENTE de la tabla|FUENTE)\s*[:\-]?\s*(.+)$", rec,
                  re.S | re.IGNORECASE)
    return limpio(m.group(2)) if m else u""


historia = []
cuerpo = []

# ── portada ───────────────────────────────────────────────────────────────
cuerpo.append(Paragraph(u"De dónde salió cada sesión", TITULO))
cuerpo.append(Paragraph(
    u"%s · %s &nbsp;&nbsp;·&nbsp;&nbsp; trazabilidad de fuentes, sesión por sesión"
    % (CURSO, nombre_curso), SUB))
cuerpo.append(cinta(
    u"<b>Qué es este documento.</b> La regla 3 del proyecto dice que nada físico se "
    u"inventa: un equipo, una labor, una veta o un frente salen del dibujo del "
    u"fabricante, del plano o de la fotografía real, y solo se dibuja lo que no tiene "
    u"cuerpo —flujos, tablas y el armazón de la sesión—. Ese rastro está en la base, "
    u"imagen por imagen y caso por caso, pero disperso. Aquí está reunido y ordenado "
    u"por sesión, para que cualquiera pueda abrir una lámina y decir de dónde salió lo "
    u"que ve.<br/><br/>"
    u"<b>Se genera, no se escribe.</b> Sale de <font face='Courier'>imagenes.csv</font>, "
    u"<font face='Courier'>casos.csv</font> y <font face='Courier'>contenidos.csv</font> "
    u"con <font face='Courier'>generar_fuentes.py</font>. Si una fuente cambia, se "
    u"corrige en la base y se vuelve a generar."))
cuerpo.append(Spacer(1, 14))

cuerpo.append(Paragraph(u"Las fuentes del curso", H1))
cuerpo.append(Paragraph(
    u"Se citan por su código en cada sesión. Las que llevan enlace se pueden abrir y "
    u"comprobar.", PIE))
cuerpo.append(Spacer(1, 6))
filas = [[Paragraph(u"CÓD.", CELDA_B), Paragraph(u"FUENTE", CELDA_B)]]
for cod, _, cita, url in FUENTES:
    txt = cita + (u"<br/><font color='#167FB9'>%s</font>" % url if url else u"")
    filas.append([Paragraph(u"<b>%s</b>" % cod, CELDA), Paragraph(txt, CELDA)])
cuerpo.append(tabla(filas, [1.6 * cm, 15.4 * cm]))
cuerpo.append(PageBreak())

# ── una sección por sesión ────────────────────────────────────────────────
adq = [s for s in sesiones if s.get(u"tipo_sesion") == u"adquisicion"]
adq.sort(key=lambda s: int(s[u"nro_sesion"]))
sin_fuente = []

for s in adq:
    sid = s[u"sesion_id"]
    bloque = []
    bloque.append(Paragraph(u"Sesión %s · %s" % (s[u"nro_sesion"], s[u"tema"]), H1))

    bloque.append(Paragraph(u"Aprendizaje esperado", H2))
    bloque.append(cinta(s.get(u"aprendizaje_esperado") or u"— pendiente —", CLARO))

    trib = tributa(s)
    inds = [i.strip() for i in (s.get(u"indicador_id") or u"").split(u";") if i.strip()]
    bloque.append(Paragraph(u"Tributa a", H2))
    bloque.append(Paragraph(
        u"%s<br/><font color='#6C7A82'>%s</font>"
        % (u" &nbsp;·&nbsp; ".join(trib) or u"—",
           u" &nbsp;/&nbsp; ".join(u"%s: %s" % (i, limpio(indicadores.get(i, u""), 110))
                                   for i in inds)), CUERPO))

    caso = casos.get(sid)
    if caso:
        bloque.append(Paragraph(u"El caso, y de dónde sale", H2))
        titulo_caso = limpio(caso[u"descripcion"], 90)
        anc = anclaje_del_caso(caso)
        cods = codigos_de(caso.get(u"recursos"))
        bloque.append(Paragraph(u"<b>%s</b>" % titulo_caso, CUERPO))
        if anc:
            bloque.append(Paragraph(limpio(anc, 900), CUERPO))
        bloque.append(Paragraph(
            u"<b>Fuentes:</b> %s" % (u" · ".join(cods) if cods
                                     else u"sin fuente externa declarada"), PIE))
        if not cods:
            sin_fuente.append((sid, u"el caso no declara fuente externa en «recursos»"))

    pcs = [c for c in contenidos if c.get(u"sesion_id") == sid]
    if pcs:
        bloque.append(Paragraph(u"Los puntos clave, y de dónde bajan", H2))
        filas = [[Paragraph(u"PUNTO CLAVE", CELDA_B), Paragraph(u"ORIGEN", CELDA_B),
                  Paragraph(u"RECURSO QUE LO APOYA", CELDA_B)]]
        for c in pcs:
            filas.append([Paragraph(limpio(c[u"contenido"], 90), CELDA),
                          Paragraph(limpio(c.get(u"origen"), 60), CELDA),
                          Paragraph(limpio(c.get(u"recursos"), 90), CELDA)])
        bloque.append(tabla(filas, [7.2 * cm, 4.4 * cm, 5.4 * cm]))

    usadas, orden = {}, []
    for l in laminas:
        if l.get(u"sesion_id") != sid:
            continue
        iid = (l.get(u"imagen_id") or u"").strip()
        if iid and iid not in usadas:
            usadas[iid] = l.get(u"que_muestra") or u""
            orden.append(iid)
    if orden:
        bloque.append(Paragraph(u"Las imágenes que se proyectan, y su procedencia", H2))
        filas = [[Paragraph(u"IMAGEN", CELDA_B), Paragraph(u"QUÉ MUESTRA", CELDA_B),
                  Paragraph(u"DE DÓNDE SALE", CELDA_B)]]
        for iid in orden:
            r = imagenes.get(iid, {})
            f = r.get(u"fuente") or u""
            # La procedencia puede estar repartida entre `fuente` y `observacion`:
            # el alias de la escala de animo cita el PPT institucional en la primera
            # y los originales de Wikimedia en la segunda. Se leen las dos.
            cods = codigos_de(f + u" " + (r.get(u"observacion") or u""))
            if cods:
                proc = u"<b>%s</b> — %s" % (u" · ".join(cods), limpio(f, 200))
            elif es_propia(f):
                proc = u"<b>Elaboración propia</b> — %s" % limpio(f, 200)
            else:
                proc = limpio(f, 200) or u"<b>sin fuente registrada</b>"
                sin_fuente.append((sid, u"%s no tiene fuente en imagenes.csv" % iid))
            if u"F12" in cods and [c for c in cods if c != u"F12"] == []:
                sin_fuente.append((sid, u"%s se apoya en material de clase de CETEMIN, "
                                        u"sin procedencia externa" % iid))
            if u"pendiente" in f.lower() or u"por confirmar" in f.lower():
                sin_fuente.append((sid, u"%s: la fuente queda declarada como pendiente "
                                        u"o por confirmar" % iid))
            filas.append([Paragraph(iid, CELDA), Paragraph(limpio(usadas[iid], 70), CELDA),
                          Paragraph(proc, CELDA)])
        bloque.append(tabla(filas, [4.6 * cm, 4.6 * cm, 7.8 * cm]))

    cuerpo.append(KeepTogether(bloque[:4]))
    cuerpo.extend(bloque[4:])
    cuerpo.append(PageBreak())

# ── lo que no cierra ──────────────────────────────────────────────────────
cuerpo.append(Paragraph(u"Lo que todavía no tiene fuente citable", H1))
cuerpo.append(Paragraph(
    u"Esta sección no es un anexo: es la razón por la que el documento se genera. "
    u"Una fuente no se descarta por su calidad, solo por no ser citable. Lo que sigue "
    u"sale de leer la base, no de una opinión.", CUERPO))
cuerpo.append(Spacer(1, 8))
if sin_fuente:
    filas = [[Paragraph(u"SESIÓN", CELDA_B), Paragraph(u"QUÉ FALTA", CELDA_B)]]
    vistos = set()
    for sid, aviso in sin_fuente:
        if (sid, aviso) in vistos:
            continue
        vistos.add((sid, aviso))
        filas.append([Paragraph(sid.split(u"-")[-1], CELDA), Paragraph(aviso, CELDA)])
    cuerpo.append(tabla(filas, [2.2 * cm, 14.8 * cm]))
else:
    cuerpo.append(Paragraph(u"Nada pendiente: todas las imágenes y todos los casos "
                            u"declaran una fuente citable.", CUERPO))


# ── pie de página ─────────────────────────────────────────────────────────
def pie_pagina(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GRIS)
    canvas.drawString(2 * cm, 1.3 * cm,
                      u"%s · %s — generado desde la base con generar_fuentes.py"
                      % (CURSO, nombre_curso))
    canvas.drawRightString(19 * cm, 1.3 * cm, u"%d" % doc.page)
    canvas.setStrokeColor(colors.HexColor("#BFBDB6"))
    canvas.line(2 * cm, 1.8 * cm, 19 * cm, 1.8 * cm)
    canvas.restoreState()


def _sin_tildes(txt):
    return u"".join(c for c in unicodedata.normalize("NFKD", txt)
                    if not unicodedata.combining(c))


SALIDA = os.path.join(RAIZ, u"03_Entregables-diseño")
slug = re.sub(u"[^A-Za-z0-9\\-]", u"", _sin_tildes(nombre_curso).replace(u" ", u"-"))
destino = None
if os.path.isdir(SALIDA):
    for h in sorted(os.listdir(SALIDA)):
        if os.path.isdir(os.path.join(SALIDA, h)) and \
                _sin_tildes(h).lower().endswith(slug.lower()):
            if re.match(r"^Curso\d+_", h) or destino is None:
                destino = os.path.join(SALIDA, h)
if destino is None:
    raise SystemExit(u"no encuentro la carpeta del curso %s" % CURSO)

OUT = os.path.join(destino, u"02_Fuentes-por-sesion.pdf")
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                        topMargin=1.8 * cm, bottomMargin=2.4 * cm,
                        title=u"De dónde salió cada sesión · %s" % nombre_curso,
                        author=u"CETEMIN · diseño instruccional")
doc.build(cuerpo, onFirstPage=pie_pagina, onLaterPages=pie_pagina)

print(u"  ✔ %s" % os.path.relpath(OUT, RAIZ))
print(u"    %d sesiones de adquisición · %d fuentes del curso · %d avisos"
      % (len(adq), len(FUENTES), len(set(sin_fuente))))
