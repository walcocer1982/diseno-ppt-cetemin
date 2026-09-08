# -*- coding: utf-8 -*-
"""Genera los entregables de un trabajo colaborativo en el formato oficial de CETEMIN.

    python 05_Base-de-datos/generar_tc.py EOM-METEXP          los dos TC del curso
    python 05_Base-de-datos/generar_tc.py EOM-METEXP 1        solo el TC1

Sale de la base (casos.csv y rubricas.csv) y escribe en la carpeta del curso,
dentro de 03_Entregables-diseño:

    TC1 (indicaciones).docx     ficha del caso, plantilla 003C
    TC1 (rúbrica).xlsx          5 criterios x 4 niveles, cierra en 20

La estructura copia la de los recursos de evaluación oficiales del paquete:
el Word es una tabla de dos columnas; el Excel lleva la cabecera de tres filas
—CRITERIOS · Peso · NIVELES DE DESEMPEÑO · PUNTAJE ASIGNADO por grupo— y una
fila de PUNTAJE TOTAL con fórmula.

Si el curso no tiene carpeta en 03_Entregables-diseño, la crea.
Nunca toca la base: solo lee.
"""
from __future__ import print_function

import csv
import io
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, u'05_Base-de-datos')
SALIDA = os.path.join(RAIZ, u'03_Entregables-diseño')

TIEMPO_POR_DEFECTO = (u'2 horas de trabajo aut\u00f3nomo \u00b7 equipos de 4 \u00b7 '
                      u'sustentaci\u00f3n de 8 minutos')

NIVELES = [(u'Destacado', 4), (u'Logrado', 3), (u'En proceso', 2), (u'En inicio', 1)]

NOTAS = (u"Destacado (4): excede las expectativas en todos los aspectos del criterio.   "
         u"Logrado (3): cumple lo esperado.   "
         u"En proceso (2): cumple parcialmente; requiere apoyo.   "
         u"En inicio (1): no alcanza lo esperado.   "
         u"La nota es del equipo. Nota mínima aprobatoria: 13 (Reglamento Interno v03, Art. 52.8).")


# --------------------------------------------------------------------- lectura

def _tabla(nombre, carrera=None):
    ruta = os.path.join(BASE, carrera, nombre) if carrera else os.path.join(BASE, nombre)
    with io.open(ruta, encoding='utf-8-sig') as f:
        filas = list(csv.reader(f))
    cab = filas[0]
    return [dict(zip(cab, r)) for r in filas[1:]]


def _carrera_de(curso_id):
    return curso_id.split(u'-')[0]


def _sin_tildes(txt):
    nfkd = unicodedata.normalize('NFKD', txt)
    return u''.join(c for c in nfkd if not unicodedata.combining(c))


def _carpeta_curso(curso):
    """03_Entregables-diseño/Curso<n>_<Nombre-del-curso>, respetando la que ya exista."""
    nombre = curso[u'nombre_curso']
    slug = _sin_tildes(nombre).replace(u' ', u'-')
    slug = re.sub(u'[^A-Za-z0-9\\-]', u'', slug)

    # Un curso puede tener MAS de una carpeta que termine igual: por ejemplo
    # "Curso1_Metodos-de-explotacion" y "EOM-Metodos-de-explotacion". Conviven a
    # proposito y no se unifican, asi que aqui no vale quedarse con la primera
    # que coincida por sufijo: los TC van siempre a la carpeta "Curso<n>_".
    if os.path.isdir(SALIDA):
        candidatas = [h for h in sorted(os.listdir(SALIDA))
                      if os.path.isdir(os.path.join(SALIDA, h))
                      and _sin_tildes(h).lower().endswith(slug.lower())]
        conprefijo = [h for h in candidatas if re.match(r'^Curso\d+_', h)]
        if conprefijo:
            return os.path.join(SALIDA, conprefijo[0])
        if candidatas:
            return os.path.join(SALIDA, candidatas[0])

    cursos = _tabla(u'cursos.csv')
    delmismo = [c for c in cursos if c[u'carrera'] == curso[u'carrera']]
    try:
        n = delmismo.index(curso) + 1
    except ValueError:
        n = 1
    return os.path.join(SALIDA, u'Curso%d_%s' % (n, slug))


# ----------------------------------------------------------------------- Word

def escribir_indicaciones(ruta, curso, caso, capacidad, indicadores, criterios):
    import docx
    from docx.enum.section import WD_ORIENT, WD_SECTION
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Cm, Pt, RGBColor

    GRIS = RGBColor(0x55, 0x5F, 0x5C)
    doc = docx.Document()

    s0 = doc.sections[0]
    s0.left_margin = s0.right_margin = Cm(2.2)
    s0.top_margin = s0.bottom_margin = Cm(2.0)

    normal = doc.styles[u'Normal']
    normal.font.name = u'Arial'
    normal.font.size = Pt(10)
    normal.paragraph_format.space_after = Pt(6)

    def titulo(n, texto):
        par = doc.add_paragraph()
        par.paragraph_format.space_before = Pt(16)
        run = par.add_run(u'%d. %s' % (n, texto.upper()))
        run.bold = True
        run.font.size = Pt(11)

    def rotulo(texto):
        par = doc.add_paragraph()
        run = par.add_run(texto)
        run.bold = True
        run.font.size = Pt(9)

    def tabla_dos(filas):
        t = doc.add_table(rows=0, cols=2)
        t.style = u'Table Grid'
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for rot, valor in filas:
            celdas = t.add_row().cells
            celdas[0].width = Cm(4.6)
            celdas[1].width = Cm(12.2)
            run = celdas[0].paragraphs[0].add_run(rot)
            run.bold = True
            run.font.size = Pt(9)
            primero = True
            for linea in valor.split(u'\n'):
                par = celdas[1].paragraphs[0] if primero else celdas[1].add_paragraph()
                par.add_run(linea)
                primero = False
        return t

    # ---------------------------------------------------------------- portada
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = par.add_run(u'TRABAJO COLABORATIVO %s' % caso[u'nro'])
    run.bold = True
    run.font.size = Pt(16)

    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = par.add_run(u'%s \u00b7 %s' % (curso[u'nombre_curso'], curso[u'carrera']))
    run.font.size = Pt(11)
    run.font.color.rgb = GRIS

    # ------------------- la ficha de nueve filas (formato oficial del ejemplo)
    inds = u'\n'.join(texto for ind_id, texto in indicadores
                      if ind_id in caso[u'indicador_id'])

    producto = caso[u'producto']
    roles = (caso.get(u'roles') or u'').strip()
    if not roles:
        partes = re.split(u'Roles:', producto, 1)
        if len(partes) == 2:
            producto, roles = partes[0].strip(), partes[1].strip()
    tiempo = (caso.get(u'tiempo') or u'').strip() or TIEMPO_POR_DEFECTO

    tabla_dos([
        (u'PROGRAMA DE ESTUDIOS', curso[u'carrera']),
        (u'UNIDAD DID\u00c1CTICA', curso[u'nombre_curso']),
        (u'INDICADOR/ES DE LOGRO DE LA CAPACIDAD', inds),
        (u'DESCRIPCI\u00d3N DEL CASO %s' % caso[u'nro'], caso[u'descripcion']),
        (u'PREGUNTA GATILLADORA', caso[u'pregunta_gatilladora']),
        (u'PRODUCTO', producto),
        (u'ROLES', roles),
        (u'TIEMPO', tiempo),
        (u'RECURSOS', caso[u'recursos'].replace(u' \u00b7 ', u'\n')),
    ])

    # ------------------------------------------------------------------- pie
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(14)
    run = par.add_run(u'Generado desde la base de diseño (casos.csv y rubricas.csv). Si el caso o la rúbrica '
                      u'cambian, se corrigen allí y se vuelve a generar este documento; no se edita a mano.')
    run.italic = True
    run.font.size = Pt(8)
    run.font.color.rgb = GRIS

    doc.save(ruta)


# ---------------------------------------------------------------------- Excel

def escribir_rubrica(ruta, curso, caso, criterios, indicadores=None):
    """Formato oficial: una columna PUNTAJE, TOTAL con formula, y las tres
    secciones de abajo —notas, que mide cada criterio, techo de verbo—."""
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

    NEGRO = u'FF1A1918'
    GRIS = u'FF5E5D59'
    FONDO = u'FFF5F4EF'
    borde = Border(*[Side(style=u'thin', color=u'FFBFBDB6')] * 4)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = u'Caso %s' % caso[u'nro']

    for col, ancho in zip(u'ABCDEF', [34, 44, 38, 36, 30, 10]):
        ws.column_dimensions[col].width = ancho

    def celda(ref, valor, negrita=False, tam=10, color=NEGRO,
              wrap=True, arriba=True, centro=False, fondo=None):
        c = ws[ref]
        c.value = valor
        c.font = Font(name=u'Arial', size=tam, bold=negrita, color=color)
        c.alignment = Alignment(wrap_text=wrap,
                                vertical=u'top' if arriba else u'center',
                                horizontal=u'center' if centro else u'left')
        if fondo:
            c.fill = PatternFill(u'solid', fgColor=fondo)
        return c

    # ------------------------------------------------------------- cabecera
    ws.merge_cells(u'A1:F1')
    celda(u'A1', u'R\u00daBRICA DE EVALUACI\u00d3N DE LA PRESENTACI\u00d3N P\u00daBLICA DEL PRODUCTO',
          negrita=True, tam=12, arriba=False)
    ws.row_dimensions[1].height = 26

    celda(u'A2', u'Especialidad:', negrita=True, tam=9)
    ws.merge_cells(u'B2:C2'); celda(u'B2', curso[u'carrera'], tam=9)
    celda(u'D2', u'Curso:', negrita=True, tam=9)
    ws.merge_cells(u'E2:F2'); celda(u'E2', curso[u'nombre_curso'], tam=9)

    celda(u'A3', u'Caso:', negrita=True, tam=9)
    ws.merge_cells(u'B3:C3')
    celda(u'B3', u'%s  \u00b7  %s' % (caso[u'nro'], _titulo_caso(caso[u'descripcion'])), tam=9)
    celda(u'D3', u'Producto:', negrita=True, tam=9)
    ws.merge_cells(u'E3:F3'); celda(u'E3', _producto_corto(caso[u'producto']), tam=9)

    ws.merge_cells(u'A4:F4')
    celda(u'A4', u'La suma de los cinco criterios ES la nota vigesimal del equipo '
                 u'(m\u00ednimo 5, m\u00e1ximo 20). Todos los criterios pesan igual: '
                 u'4 puntos cada uno.', tam=9, color=GRIS)

    # ------------------------------------------------------- cabecera tabla
    for ref, txt in ((u'B6', u'Excelente'), (u'C6', u'Bueno'),
                     (u'D6', u'Regular'), (u'E6', u'En inicio')):
        celda(ref, txt, negrita=True, tam=10, arriba=False, centro=True, fondo=FONDO).border = borde
    ws[u'A6'].border = borde
    ws[u'F6'].border = borde
    ws.row_dimensions[6].height = 20

    celda(u'A7', u'CRITERIOS', negrita=True, arriba=False, fondo=FONDO).border = borde
    for ref, txt in ((u'B7', 4), (u'C7', 3), (u'D7', 2), (u'E7', 1)):
        celda(ref, txt, negrita=True, arriba=False, centro=True, fondo=FONDO).border = borde
    celda(u'F7', u'PUNTAJE', negrita=True, tam=9, arriba=False, centro=True, fondo=FONDO).border = borde
    ws.row_dimensions[7].height = 20

    # ----------------------------------------------------------- criterios
    fila = 8
    for cr in criterios:
        celda(u'A%d' % fila, cr[u'criterio'], negrita=True, tam=10).border = borde
        for col, clave in zip(u'BCDE', [u'nivel_4', u'nivel_3', u'nivel_2', u'nivel_1']):
            celda(u'%s%d' % (col, fila), cr[clave], tam=9).border = borde
        celda(u'F%d' % fila, None, arriba=False, centro=True).border = borde
        ws.row_dimensions[fila].height = 128
        fila += 1

    ws.merge_cells(u'A%d:E%d' % (fila, fila))
    celda(u'A%d' % fila, u'TOTAL', negrita=True, arriba=False).border = borde
    c = celda(u'F%d' % fila, u'=SUM(F8:F%d)' % (fila - 1), negrita=True, arriba=False, centro=True)
    c.border = borde
    ws.row_dimensions[fila].height = 24
    fin_tabla = fila

    # ------------------------------------------------------------- secciones
    fila = fin_tabla + 2
    celda(u'A%d' % fila, u'NOTAS ESPEC\u00cdFICAS', negrita=True, tam=9)
    ws.merge_cells(u'B%d:F%d' % (fila, fila))
    celda(u'B%d' % fila, u'Excelente (4): excede las expectativas en todos los criterios.   \u00b7   '
                         u'Bueno (3): cumple con las expectativas, con \u00e1reas menores de mejora.   \u00b7   '
                         u'Regular (2): cumple los requisitos m\u00ednimos, necesita mejorar.   \u00b7   '
                         u'En inicio (1): no alcanza los requisitos m\u00ednimos.', tam=9, color=GRIS)
    ws.row_dimensions[fila].height = 30

    fila += 2
    celda(u'A%d' % fila, u'QU\u00c9 MIDE CADA CRITERIO', negrita=True, tam=9)
    ws.merge_cells(u'B%d:F%d' % (fila, fila))
    contenido = sum(4 for cr in criterios if cr.get(u'indicador_id') != u'transversal')
    celda(u'B%d' % fila, u'Reparto de puntos: contenido %d (criterios 1 a 3) \u00b7 transversales %d '
                         u'(criterios 4 y 5). Los cinco nombres son los oficiales del \u00a706 y no se '
                         u'cambian: lo que cambia es qu\u00e9 se escribe en cada uno.'
                         % (contenido, 20 - contenido), tam=9, color=GRIS)

    for cr in criterios:
        fila += 1
        celda(u'A%d' % fila, u'%s \u00b7 %s' % (cr[u'n'], cr[u'criterio']), tam=9)
        ws.merge_cells(u'B%d:F%d' % (fila, fila))
        etq = (cr.get(u'indicador_id') or u'')
        for orden, (ind_id, _txt) in enumerate(indicadores or [], start=1):
            etq = etq.replace(ind_id, u'Indicador %d' % orden)
        celda(u'B%d' % fila, etq.replace(u';', u' \u00b7 '), tam=9, color=GRIS)

    # techo de verbo, derivado de los indicadores del curso
    verbos = []
    for _ind_id, texto in (indicadores or []):
        primera = texto.split(u' ')[0].upper()
        if primera and primera not in verbos:
            verbos.append(primera)
    fila += 2
    ws.merge_cells(u'A%d:F%d' % (fila, fila))
    celda(u'A%d' % fila, u'Techo de verbo: los indicadores dicen %s. Los verbos de los descriptores no '
                         u'lo superan; quedan fuera explicar, justificar y recomendar.'
                         % (u' / '.join(verbos) if verbos else u'\u2014'), tam=9, color=GRIS)
    ws.row_dimensions[fila].height = 30

    fila += 1
    ws.merge_cells(u'A%d:F%d' % (fila, fila))
    celda(u'A%d' % fila, u'PROTOCOLO DEL CRITERIO 5 \u2014 el instructor formula al menos una pregunta '
                         u't\u00e9cnica a CADA integrante, sobre una parte del trabajo que ese integrante '
                         u'no expuso. Sin ese protocolo el criterio no se puede marcar.', tam=9, color=GRIS)
    ws.row_dimensions[fila].height = 30

    ws.freeze_panes = u'A8'
    wb.save(ruta)


def _escribir(fn, ruta, *args):
    """Windows bloquea el archivo si esta abierto en Word o Excel. Avisar, no reventar."""
    try:
        fn(ruta, *args)
        return True
    except (IOError, OSError) as e:
        if getattr(e, 'errno', None) == 13:
            print(u'  ! %s esta abierto en Word o Excel: cierralo y vuelve a generar'
                  % os.path.basename(ruta))
            return False
        raise


def _titulo_caso(descripcion):
    m = re.search(u'[«"“]([^»"”]+)[»"”]', descripcion)
    return m.group(1) if m else descripcion[:60]


def _producto_corto(producto):
    return producto.split(u'.')[0][:90]


def generar(curso_id, cuales):
    carrera = _carrera_de(curso_id)
    cursos = [c for c in _tabla(u'cursos.csv') if c[u'curso_id'] == curso_id]
    if not cursos:
        sys.exit(u'No existe el curso %s en cursos.csv' % curso_id)
    curso = cursos[0]

    caps = [c for c in _tabla(u'capacidades.csv', carrera) if c[u'curso_id'] == curso_id]
    capacidad = caps[0][u'descripcion'] if caps else u'(sin capacidad cargada en la base)'
    indicadores = [(i[u'indicador_id'], i[u'descripcion'])
                   for i in _tabla(u'indicadores.csv', carrera)
                   if not caps or i[u'capacidad_id'] == caps[0][u'capacidad_id']]
    casos = [c for c in _tabla(u'casos.csv', carrera)
             if c[u'curso_id'] == curso_id and c[u'alcance'] == u'colaborativo']
    rubricas = _tabla(u'rubricas.csv', carrera)

    # Los TC y sus rubricas viven en la subcarpeta de evaluacion del curso,
    # junto al resto de recursos que el estudiante rinde.
    carpeta = os.path.join(_carpeta_curso(curso), u'Recursos de evaluacion')
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
        print(u'Carpeta creada: %s' % os.path.relpath(carpeta, RAIZ))

    for caso in sorted(casos, key=lambda c: c[u'caso_id']):
        nro = caso[u'caso_id'].rsplit(u'-', 1)[-1]
        if cuales and nro not in cuales:
            continue
        caso[u'nro'] = nro
        caso[u'titulo'] = _titulo_caso(caso[u'descripcion'])
        caso[u'producto_corto'] = _producto_corto(caso[u'producto'])

        criterios = sorted([r for r in rubricas if r[u'caso_id'] == caso[u'caso_id']],
                           key=lambda r: int(r[u'n']))
        if not criterios:
            print(u'  ! %s no tiene rúbrica; se omite el Excel' % caso[u'caso_id'])

        mios = indicadores
        if not any(i in caso[u'indicador_id'] for i, _ in indicadores):
            print(u'  ! %s no declara ningun indicador de la capacidad' % caso[u'caso_id'])

        doc = os.path.join(carpeta, u'TC%s (indicaciones).docx' % nro)
        if _escribir(escribir_indicaciones, doc, curso, caso, capacidad, mios, criterios):
            print(u'  ✔ %s' % os.path.relpath(doc, RAIZ))

        if criterios:
            xls = os.path.join(carpeta, u'TC%s (rúbrica).xlsx' % nro)
            if _escribir(escribir_rubrica, xls, curso, caso, criterios, indicadores):
                total = sum(int(c[u'puntos_max']) for c in criterios)
                print(u'  ✔ %s   %d criterios · %d pts' % (os.path.relpath(xls, RAIZ), len(criterios), total))
                if total != 20:
                    print(u'  ! la rúbrica no cierra en 20: revisa rubricas.csv')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    generar(sys.argv[1], set(sys.argv[2:]))
