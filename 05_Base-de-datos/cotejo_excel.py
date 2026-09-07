# -*- coding: utf-8 -*-
"""La lista de cotejo del instructor. UNA SOLA HOJA, generica, que se usa y se descarta.

    python cotejo_excel.py SI-SGCSSMA        (desde 05_Base-de-datos/)

No hay una hoja por sesion ni hoja de resumen. DECISION de Jorge Canchiz, 2026-09-02: la
evaluacion es formativa, no se registra y no se guarda; lo de la sesion pasada no interesa
en la siguiente. Con veinticuatro hojas el instructor administraba un historial que nadie
iba a leer. Se imprime o se llena, se le devuelve al equipo y se descarta.

Por eso la hoja no lleva el tema ni el aprendizaje esperado prefijados: lleva casillas en
blanco para el numero de sesion, la fecha y la consigna del dia, que el instructor copia
del guion. Asi la MISMA hoja sirve para un curso de 96 horas y para uno de 48.

Los cinco criterios y la escala son doctrina (§14): no se editan aqui, ni por curso ni por
carrera. Son los mismos cinco de la rubrica del colaborativo, un escalon mas abajo.
"""
import csv, io, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSO = sys.argv[1] if len(sys.argv) > 1 else "SI-SGCSSMA"
CARRERA = CURSO.split("-")[0]

AZUL, AZUL2, GRIS, AMBAR, VERDE, ROJO = "1F3864", "2E5496", "F2F2F2", "FFF2CC", "E2EFDA", "FCE4D6"
BORDE = Border(*[Side(style="thin", color="BFBFBF")] * 4)
N_EQUIPOS = 8

# ── los cinco criterios (§14). Fijos en los 35 cursos ──────────────────────
# (nombre, que es estar LOGRADO —el 3—, que añade el DESTACADO —el 4—)
# Los enunciados de LOGRADO son los que Jorge Canchiz escribio a mano el 2026-09-02.
# Se cambian AQUI, no en el xlsx: editando el xlsx se pierden al regenerar.
CRITERIOS = [
 ("DESARROLLO TÉCNICO",
  "Resuelve el problema en su totalidad, utilizando métodos o formas aprendidas en clase",
  "el sustento es verificable: la norma con su artículo, el parámetro técnico o la "
  "consecuencia específica"),
 ("CONCLUSIONES",
  "La conclusión se desprende del desarrollo y responde a la(s) pregunta(s) del caso",
  "identifica el hecho que, presentándose como conforme, no lo es, y describe la discrepancia"),
 ("ORGANIZACIÓN DEL PRODUCTO",
  "El producto está ordenado, tiene claridad y coherencia",
  "expone el recorrido completo y puede seguirse sin la explicación oral"),
 ("SUSTENTACIÓN ORAL",
  "los integrantes exponen la parte que les corresponde, con orden y claridad",
  "cualquier integrante responde consultas sobre una parte que no expuso"),
 ("TIEMPO DE EXPOSICIÓN",
  "se ajusta al tiempo asignado sin desviaciones",
  "se ajusta dentro del 10 % del tiempo asignado"),
]
NIVELES = [("0", "No presenta"), ("1", "En inicio"), ("2", "En proceso"),
           ("3", "Logrado"), ("4", "Destacado")]

COL_1 = 3                                  # el equipo 1 arranca en la columna C
ULT = COL_1 + N_EQUIPOS - 1
ANCHO = ULT


def leer(n):
    p = os.path.join(BASE, "05_Base-de-datos", n)
    if not os.path.exists(p):
        return []
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


nombre = next((c.get("nombre_curso", CURSO) for c in leer("cursos.csv")
               if c.get("curso_id") == CURSO), CURSO)

wb = Workbook()
ws = wb.active
ws.title = "Lista de cotejo"
ws.sheet_view.showGridLines = False


def put(r, c, v, *, bold=False, size=10, color="000000", fill=None, h="left", wrap=True,
        borde=True):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = Font(name="Calibri", size=size, bold=bold, color=color)
    cell.alignment = Alignment(horizontal=h, vertical="center", wrap_text=wrap)
    if fill:
        cell.fill = PatternFill("solid", fgColor=fill)
    if borde:
        cell.border = BORDE
    return cell


def banda(r, texto, *, fill=AZUL2, size=11, color="FFFFFF", alto=None):
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ANCHO)
    put(r, 1, texto, bold=True, size=size, color=color, fill=fill)
    if alto:
        ws.row_dimensions[r].height = alto


# ── cabecera ───────────────────────────────────────────────────────────────
banda(1, "LISTA DE COTEJO — evaluación formativa de sesión", fill=AZUL, size=14, alto=28)
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ANCHO)
put(2, 1, "%s  ·  %s" % (CURSO, nombre), size=11, fill=GRIS, h="center")

# Casillas en blanco: la MISMA hoja sirve para cualquier sesion de cualquier curso.
put(3, 1, "SESIÓN N°", bold=True, size=10, fill=GRIS)
put(3, 2, None, fill=AMBAR)
put(3, 3, "FECHA", bold=True, size=10, fill=GRIS, h="center")
ws.merge_cells(start_row=3, start_column=4, end_row=3, end_column=5)
put(3, 4, None, fill=AMBAR)
put(3, 6, "INSTRUCTOR", bold=True, size=10, fill=GRIS, h="center")
ws.merge_cells(start_row=3, start_column=7, end_row=3, end_column=ANCHO)
put(3, 7, None, fill=AMBAR)

put(4, 1, "LA CONSIGNA\nDE HOY", bold=True, size=9, fill=GRIS)
ws.merge_cells(start_row=4, start_column=2, end_row=4, end_column=ANCHO)
put(4, 2, None, fill=AMBAR, size=10)
ws.row_dimensions[4].height = 38

ws.merge_cells(start_row=5, start_column=1, end_row=5, end_column=ANCHO)
put(5, 1, "ESTO NO SE REGISTRA. Es formativa: no entra al promedio ni sube al sistema. Se llena, "
          "se le devuelve al equipo y se descarta. Los únicos que dan nota son los cuestionarios "
          "de verificación, el parcial, el final y los dos colaborativos.", size=9, fill=AMBAR)
ws.row_dimensions[5].height = 30

ws.merge_cells(start_row=6, start_column=1, end_row=6, end_column=ANCHO)
put(6, 1, "ESCALA:   " + "   ·   ".join("%s %s" % (v, e) for v, e in NIVELES),
    bold=True, size=11, color=AZUL, fill=GRIS, h="center")
ws.row_dimensions[6].height = 22

# ── la rejilla: criterios en filas, equipos en columnas ────────────────────
F_CAB, F_INT, F_1 = 8, 9, 10
F_NOTA = F_1 + len(CRITERIOS)

put(F_CAB, 1, "N°", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
put(F_CAB, 2, "CRITERIO  ·  qué es estar LOGRADO", bold=True, size=10, color="FFFFFF", fill=AZUL2)
for k in range(N_EQUIPOS):
    put(F_CAB, COL_1 + k, "Equipo %d" % (k + 1), bold=True, size=10, color="FFFFFF", fill=AZUL2,
        h="center")
ws.row_dimensions[F_CAB].height = 24

put(F_INT, 1, "", fill=GRIS)
put(F_INT, 2, "INTEGRANTES", bold=True, size=9, fill=GRIS)
for k in range(N_EQUIPOS):
    put(F_INT, COL_1 + k, None, size=9, h="center", fill=AMBAR)
ws.row_dimensions[F_INT].height = 44

# showDropDown=False NO oculta la lista: el atributo significa «suprimir», asi que con
# False la flecha se ve. Y showErrorMessage tiene que ir en True o se puede teclear un 7.
dv = DataValidation(type="list", formula1='"0,1,2,3,4"', allow_blank=True,
                    showDropDown=False, showErrorMessage=True)
dv.error = "Solo 0, 1, 2, 3 o 4."
dv.errorTitle = "Valor fuera de la escala"
ws.add_data_validation(dv)

for i, (n, logrado, _) in enumerate(CRITERIOS):
    r = F_1 + i
    put(r, 1, i + 1, bold=True, h="center", size=12)
    c = ws.cell(row=r, column=2, value="%s\n%s" % (n, logrado))
    c.font = Font(name="Calibri", size=9)
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    c.border = BORDE
    ws.row_dimensions[r].height = 52
    for k in range(N_EQUIPOS):
        dv.add(put(r, COL_1 + k, None, h="center", size=14, fill=AMBAR))

put(F_NOTA, 1, "", fill=GRIS)
put(F_NOTA, 2, "NOTA   /20", bold=True, size=11, fill=GRIS)
for k in range(N_EQUIPOS):
    col = get_column_letter(COL_1 + k)
    put(F_NOTA, COL_1 + k, '=IF(COUNT(%s%d:%s%d)=0,"",SUM(%s%d:%s%d))'
        % (col, F_1, col, F_NOTA - 1, col, F_1, col, F_NOTA - 1),
        bold=True, size=14, h="center", fill=GRIS)
ws.row_dimensions[F_NOTA].height = 28

rango = "%s%d:%s%d" % (get_column_letter(COL_1), F_NOTA, get_column_letter(ULT), F_NOTA)
ws.conditional_formatting.add(rango, CellIsRule(
    operator="greaterThanOrEqual", formula=["13"], fill=PatternFill("solid", bgColor=VERDE)))
ws.conditional_formatting.add(rango, CellIsRule(
    operator="lessThan", formula=["13"], fill=PatternFill("solid", bgColor=ROJO)))

# La hoja TERMINA en la nota. Los bloques de «DESTACADO» y «CÓMO SE USA» que iban al pie
# los retiro Jorge Canchiz el 2026-09-02: la lista es la rejilla y nada mas. Lo que aquellos
# decian vive en el §14, y el tercer elemento de CRITERIOS lo conserva para la doctrina.
r = F_NOTA

ws.column_dimensions["A"].width = 5
ws.column_dimensions["B"].width = 62
for k in range(N_EQUIPOS):
    ws.column_dimensions[get_column_letter(COL_1 + k)].width = 11
ws.page_setup.orientation = "landscape"
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 1
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = "A1:%s%d" % (get_column_letter(ANCHO), r)

# ── dónde se guarda ────────────────────────────────────────────────────────
dest = None
base_ent = os.path.join(BASE, "03_Entregables-diseño")
for ciclo in sorted(os.listdir(base_ent)) if os.path.isdir(base_ent) else []:
    p = os.path.join(base_ent, ciclo)
    if not (os.path.isdir(p) and ciclo.startswith(CARRERA + " - Ciclo")):
        continue
    for cur in sorted(os.listdir(p)):
        if " - %s - " % CURSO in cur:
            q = os.path.join(p, cur, "Instrumentos de evaluación")
            if os.path.isdir(q):
                dest = q
if dest is None:
    raise SystemExit("no encuentro la carpeta de instrumentos de %s" % CURSO)

OUT = os.path.join(dest, "16_Lista-de-cotejo.xlsx")
wb.save(OUT)
print("generado: 16_Lista-de-cotejo.xlsx  ·  una sola hoja, %d equipos, 5 criterios × 0-4" % N_EQUIPOS)
print("  sirve para cualquier sesión: la sesión, la fecha y la consigna van en blanco")
