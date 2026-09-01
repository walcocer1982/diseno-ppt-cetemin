# 14 — La lista de cotejo de sesión: **los cinco de siempre**

**Un solo instrumento para las 24 sesiones de los 35 cursos, en las tres carreras.**

Complementa al [§06](06_casos-rubricas-evaluacion.md) —que fija las rúbricas de los colaborativos— y es el paso ④ del [§13](13_ORDEN-DE-TRABAJO.md).

---

## Qué es, y qué no es

| | |
|---|---|
| **Qué es** | Cómo se le dice al estudiante, cada sesión, si su trabajo está bien hecho — y cuánto sacaría si se calificara |
| **Qué NO es** | Una rúbrica. Y **no da nota**: los seis eventos calificados están cerrados |
| **Cuánto cuesta** | Tres minutos al cierre de la sesión |

**Los seis eventos calificados** son CV1 (5 %), CV2 (5 %), EP (20 %), EF (20 %), TC1 (25 %) y TC2 (25 %). Suman 100 % y los fija el Reglamento Interno v03. **Un séptimo rompería el reparto**, así que la lista de cotejo no promedia.

**Entonces para qué sirve el trabajo de sesión.** Para las dos cosas que sí se califican: cada caso de sesión **tributa a un criterio** de TC1 o TC2 (§13 ②), y el contenido de la sesión es lo que preguntan CV, EP y EF.

---

## Los cinco ítems

| | Ítem | Se observa cuando… |
|---|---|---|
| 1 | **COMPLETO** | ningún paso del encargo, ninguna fila ni casilla sin resolver |
| 2 | **CON LOS DATOS DEL CASO** | cada afirmación se apoya en un dato; ninguna sale de suponer |
| 3 | **CON EL TÉRMINO CORRECTO** | los términos de la sesión aparecen, y bien usados |
| 4 | **CON EL PORQUÉ** | la norma, la causa o la consecuencia que lo sustenta |
| 5 | **SUSTENTADO POR TODOS** | cada integrante expone, y responde sobre lo que no expuso |

**Son binarios: se observa o no se observa.** Nada de «a medias».

**Y son de forma, no de contenido.** Por eso el mismo juego sirve en un caso de flotación de PM, uno de sostenimiento de EOM y uno de sistemas de gestión de SI. Esa es toda la razón por la que hay un solo instrumento y no setecientos.

### La escala

| Se observan | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|
| **Nota** | **20** | **16** | 12 | 8 | 4 | 0 |

> **Con cuatro de cinco, apruebas. Con tres, no.**

**Cuatro puntos por ítem, cinco ítems, 20.** Es la misma aritmética de las rúbricas de los colaborativos ([§06](06_casos-rubricas-evaluacion.md)), **y es a propósito**: el estudiante ensaya veinte veces las cinco conductas con las que se le va a calificar en la sustentación. Cuando llega el TC ya sabe qué se le mira.

---

## Lo único que se escribe por sesión

**Una línea: qué significa «completo» hoy.**

```
Hoy, «completo» es:  cada documento con su letra del SSOMAC · los que faltan y los
vencidos, señalados · cada hueco con a quién deja desprotegido
```

**Y no hay que inventarla: son los pasos del encargo**, que el caso de sesión ya trae del paso ③ del §13. Se copian, separados por `·`.

### Cómo se escribe bien

| | |
|---|---|
| **Sale del encargo** | Si no coincide con los pasos que la lámina pide, uno de los dos está mal |
| **Es observable** | Se mira el producto y se ve. Si hay que deducirlo, no sirve |
| **Cabe en dos renglones** | Va al pie de una lámina y de una hoja de cálculo |
| **No nombra la respuesta** | Dice *qué tiene que estar*, no *cuál es el resultado correcto* |

**Dónde vive:** `05_Base-de-datos/<CARRERA>/listas_cotejo.csv`, **una fila por sesión**, en la columna `observable`.

Los cinco ítems y la escala **no van a ninguna tabla**: viven aquí y dentro de `generar_ppt.py`. Si algún día cambian, cambian en un sitio.

---

## Cómo se usa en clase — tres minutos

1. **Se muestra ANTES de trabajar.** La lámina «Los cinco de siempre» va en la Aplicación, después del encargo y los casos A y B. El estudiante sabe con qué se le va a mirar antes de empezar.
2. Al terminar, **el equipo se marca a sí mismo**.
3. **Después marca el instructor.**
4. **Donde no coinciden está la conversación.** Un equipo que se pone 20 y saca 12 tiene un problema distinto al que se pone 12 y saca 12: el primero no sabe mirarse, el segundo sí y necesita ayuda.
5. La hoja se le devuelve marcada. **No entra al promedio.**

> **El paso 2 no es relleno.** Que el equipo se marque primero es lo que convierte la lista en aprendizaje: obliga a mirar el propio trabajo con el criterio del que califica. Saltárselo la reduce a un checklist del instructor.

---

## La lámina

En `laminas.csv` va con **tipo `cotejo`** y el **texto vacío**. El generador la arma: los cinco ítems, la escala, la frase y la línea de concreción de esa sesión.

```
laminas.csv  →  tipo = cotejo, texto vacío  →  generar_ppt.py la compone
```

**No se escribe el contenido de esa lámina.** Si aparece escrito en `laminas.csv`, alguien lo copió y se va a desincronizar.

Va en el momento de **Aplicación**, después de «A trabajar».

---

## El cuaderno del instructor

Un solo Excel por curso. Se genera así:

```
cd 05_Base-de-datos
python cotejo_excel.py SI-SGCSSMA
```

Sale en `03_Entregables-diseño/<CARRERA> - Ciclo N/<n> - <CURSO> - .../Instrumentos de evaluación/16_Lista-de-cotejo_Los-cinco-de-siempre.xlsx`.

| Hoja | Qué trae |
|---|---|
| **Cómo se usa** | Los cinco ítems, la escala, la rutina de tres minutos. Y arriba, en ámbar: **esto no se registra** |
| **Resumen** | Se llena solo |
| **S1 … Sn** | Una por sesión de adquisición |

**Cada hoja de sesión** trae el tema, el aprendizaje esperado y la línea «Hoy, completo es…», y debajo la matriz: por equipo, cinco casillas que marca el equipo y cinco que marcas tú. La nota, la autoevaluación y la brecha salen solas.

Los **integrantes se escriben una sola vez**, en la hoja de la primera sesión; las demás los heredan.

Si una sesión todavía no tiene su línea, la hoja lo dice **en rojo**. Se corrige llenando `listas_cotejo.csv` y volviendo a generar.

### Cómo se lee el resumen

| | Qué dice |
|---|---|
| **Sesiones bajo 13**, por equipo | A quién acompañar |
| **En qué ítem falla la clase** | Qué hay que volver a enseñar |

> **El ítem con el total más alto es el que hay que volver a enseñar, no el que hay que castigar.** Y un equipo con dos o más sesiones bajo 13 necesita acompañamiento, no una nota.

**El número de equipos** está en `N_EQUIPOS`, dentro del script. Por defecto 8.

---

## Lo que esta lista NO hace

**No caza el error técnico fino.** Si un equipo escribe *supervisor* donde correspondía *comité*, el ítem 3 lo caza solo si el instructor lo nota.

Esta lista mide **si el trabajo está bien hecho**, no si la respuesta es correcta. Y está bien que así sea: la corrección técnica la juzga **la rúbrica del colaborativo**, con criterios propios de ese caso. La lista de sesión sirve para otra cosa — que el estudiante sepa cómo va, semana a semana, con el mismo espejo siempre.

**Si necesitas juzgar la corrección de una sesión concreta**, no toques los cinco ítems: aprieta la **línea de concreción**. Ahí es donde entra lo técnico de esa clase.

---

## El generador, completo

Está en `05_Base-de-datos/cotejo_excel.py`. Va aquí dentro para que **el documento y el código no puedan separarse**: si copias este MD, copias el generador.

```python
# -*- coding: utf-8 -*-
"""El cuaderno de cotejo del instructor. Formativo: no se registra en el sistema.

Una hoja por sesion de adquisicion — se abre la del dia, se marcan cinco casillas por equipo
y se cierra. Mas una hoja de resumen que se llena sola y dice a quien acompanar y en que.

    python cotejo_excel.py SI-SGCSSMA        (desde 05_Base-de-datos/)

Los cinco items son doctrina (§14): no se editan aqui, ni por curso ni por carrera.
"""
import csv, io, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# La raiz sale de donde vive este archivo: 05_Base-de-datos/ esta colgado de ella.
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSO = sys.argv[1] if len(sys.argv) > 1 else "SI-SGCSSMA"
CARRERA = CURSO.split("-")[0]
DB = os.path.join(BASE, "05_Base-de-datos", CARRERA)

AZUL, AZUL2, GRIS, AMBAR, VERDE, ROJO = "1F3864", "2E5496", "F2F2F2", "FFF2CC", "E2EFDA", "FCE4D6"
BORDE = Border(*[Side(style="thin", color="BFBFBF")] * 4)
N_EQUIPOS = 8

# Los cinco de siempre (§13 ④). Fijos en los 35 cursos: aqui no se editan.
ITEMS = [("COMPLETO", "ningún paso del encargo, ninguna fila ni casilla sin resolver"),
         ("CON LOS DATOS DEL CASO", "cada afirmación se apoya en un dato; ninguna sale de suponer"),
         ("CON EL TÉRMINO CORRECTO", "los términos de la sesión aparecen, y bien usados"),
         ("CON EL PORQUÉ", "la norma, la causa o la consecuencia que lo sustenta"),
         ("SUSTENTADO POR TODOS", "cada integrante expone, y responde sobre lo que no expuso")]


def leer(n):
    p = os.path.join(DB, n)
    if not os.path.exists(p):
        return []
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


ses = sorted([s for s in leer("sesiones.csv")
              if s["curso_id"] == CURSO and s["tipo_sesion"] == "adquisicion"],
             key=lambda x: int(x["nro_sesion"]))
if not ses:
    raise SystemExit("no hay sesiones de adquisición de %s en %s/sesiones.csv" % (CURSO, CARRERA))
CONC = {c["sesion_id"]: c.get("observable", "") for c in leer("listas_cotejo.csv")}
nombre = next((c.get("nombre_curso", CURSO) for c in
               (leer("../cursos.csv") or []) if c.get("curso_id") == CURSO), CURSO)

wb = Workbook()


def put(ws, r, c, v, *, bold=False, size=10, color="000000", fill=None, h="left", wrap=True,
        borde=True):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = Font(name="Calibri", size=size, bold=bold, color=color)
    cell.alignment = Alignment(horizontal=h, vertical="center", wrap_text=wrap)
    if fill:
        cell.fill = PatternFill("solid", fgColor=fill)
    if borde:
        cell.border = BORDE
    return cell


# ══ Hoja 1 · cómo se usa ══════════════════════════════════════════════════
ws = wb.active
ws.title = "Cómo se usa"
ws.sheet_view.showGridLines = False
ws.merge_cells("A1:F1")
put(ws, 1, 1, "LOS CINCO DE SIEMPRE — cuaderno de cotejo del instructor", bold=True, size=14,
    color="FFFFFF", fill=AZUL, h="center")
ws.row_dimensions[1].height = 28
ws.merge_cells("A2:F2")
put(ws, 2, 1, "%s  ·  %s" % (CURSO, nombre), size=11, fill=GRIS, h="center")

ws.merge_cells("A4:F4")
put(ws, 4, 1, "ESTO NO SE REGISTRA. Es evaluación formativa: no entra al promedio ni sube al "
              "sistema. Sirve para que el estudiante sepa cómo va, y para que tú sepas a quién "
              "acompañar. Los seis eventos calificados —CV1, CV2, EP, EF, TC1 y TC2— siguen "
              "siendo los únicos que dan nota.", size=10, fill=AMBAR)
ws.row_dimensions[4].height = 42

r = 6
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
put(ws, r, 1, "LOS CINCO ÍTEMS — los mismos en las 24 sesiones, en los 35 cursos y en las tres carreras",
    bold=True, size=11, color="FFFFFF", fill=AZUL2)
r += 1
put(ws, r, 1, "N°", bold=True, size=10, fill=GRIS, h="center")
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
put(ws, r, 2, "ÍTEM", bold=True, size=10, fill=GRIS)
ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=6)
put(ws, r, 4, "SE OBSERVA CUANDO…", bold=True, size=10, fill=GRIS)
r += 1
for i, (n, regla) in enumerate(ITEMS, 1):
    put(ws, r, 1, i, bold=True, h="center")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    put(ws, r, 2, n, bold=True)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=6)
    put(ws, r, 4, regla)
    ws.row_dimensions[r].height = 30
    r += 1

r += 1
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
put(ws, r, 1, "LA ESCALA — cada ítem vale 4 puntos", bold=True, size=11, color="FFFFFF", fill=AZUL2)
r += 1
put(ws, r, 1, "Se observan", bold=True, size=10, fill=GRIS, h="center")
for k, v in enumerate(["5", "4", "3", "2", "1", "0"]):
    put(ws, r, 2 + k, v, bold=True, h="center", fill=GRIS)
r += 1
put(ws, r, 1, "Nota", bold=True, size=10, fill=GRIS, h="center")
for k, (v, f) in enumerate([("20", VERDE), ("16", VERDE), ("12", ROJO), ("8", ROJO), ("4", ROJO),
                            ("0", ROJO)]):
    put(ws, r, 2 + k, v, bold=True, size=12, h="center", fill=f)
r += 2
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
put(ws, r, 1, "Con cuatro de cinco, apruebas. Con tres, no.  ·  Es la misma aritmética que la "
              "rúbrica del colaborativo (5 × 4 = 20), a propósito: el estudiante ensaya veinte "
              "veces las cinco conductas con las que se le calificará en la sustentación.",
    bold=True, size=10, color=AZUL, fill=GRIS)
ws.row_dimensions[r].height = 32

r += 2
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
put(ws, r, 1, "CÓMO SE MARCA — tres minutos al cierre", bold=True, size=11, color="FFFFFF", fill=AZUL2)
for paso in ["1 · Se muestra la lámina «Los cinco de siempre» ANTES de trabajar. El estudiante "
             "sabe con qué se le va a mirar.",
             "2 · Al terminar, el EQUIPO se marca a sí mismo. Escribe una x en las casillas que "
             "considera que cumplió.",
             "3 · Después marcas TÚ. La nota y la brecha se calculan solas.",
             "4 · Donde no coinciden está la conversación. Un equipo que se pone 20 y saca 12 "
             "tiene un problema distinto al que se pone 12 y saca 12.",
             "5 · La hoja «Resumen» se llena sola: dice qué equipo cae y en cuál de los cinco "
             "ítems falla la clase entera."]:
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
    put(ws, r, 1, paso, size=10)
    ws.row_dimensions[r].height = 26

for col, anc in zip("ABCDEF", [12, 22, 22, 22, 22, 22]):
    ws.column_dimensions[col].width = anc

# ══ Una hoja por sesión ═══════════════════════════════════════════════════
COL_EQ, COL_INS = 3, 9        # C..G marca del equipo · I..M marca del instructor
FILA_1 = 9


def hoja_sesion(s, primera):
    h = wb.create_sheet("S%s" % s["nro_sesion"])
    h.sheet_view.showGridLines = False
    h.merge_cells(start_row=1, start_column=1, end_row=1, end_column=15)
    put(h, 1, 1, "SESIÓN %s  ·  %s" % (s["nro_sesion"], s["tema"]), bold=True, size=13,
        color="FFFFFF", fill=AZUL, h="center")
    h.row_dimensions[1].height = 26
    h.merge_cells(start_row=2, start_column=1, end_row=2, end_column=15)
    put(h, 2, 1, "Aprendizaje esperado:  " + s["aprendizaje_esperado"], size=10, fill=GRIS)
    h.row_dimensions[2].height = 26
    h.merge_cells(start_row=3, start_column=1, end_row=3, end_column=15)
    conc = CONC.get(s["sesion_id"], "")
    put(h, 3, 1, ("Hoy, «completo» es:  " + conc) if conc
        else "Hoy, «completo» es:  — pendiente: son los pasos del encargo de esta sesión —",
        size=10, bold=bool(conc), fill=AMBAR if conc else ROJO)
    h.row_dimensions[3].height = 28
    h.merge_cells(start_row=4, start_column=1, end_row=4, end_column=15)
    put(h, 4, 1, "Marca con una x. Primero el equipo, después tú. La nota y la brecha se "
                 "calculan solas. NO SE REGISTRA.", size=9, fill=GRIS)

    h.merge_cells(start_row=6, start_column=1, end_row=7, end_column=1)
    put(h, 6, 1, "EQUIPO", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
    h.merge_cells(start_row=6, start_column=2, end_row=7, end_column=2)
    put(h, 6, 2, "INTEGRANTES", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
    h.merge_cells(start_row=6, start_column=COL_EQ, end_row=6, end_column=COL_EQ + 4)
    put(h, 6, COL_EQ, "SE MARCA EL EQUIPO", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
    put(h, 6, COL_EQ + 5, "AUTO", bold=True, size=9, color="FFFFFF", fill=AZUL2, h="center")
    h.merge_cells(start_row=6, start_column=COL_INS, end_row=6, end_column=COL_INS + 4)
    put(h, 6, COL_INS, "MARCAS TÚ", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
    put(h, 6, COL_INS + 5, "NOTA", bold=True, size=9, color="FFFFFF", fill=AZUL2, h="center")
    put(h, 6, COL_INS + 6, "BRECHA", bold=True, size=9, color="FFFFFF", fill=AZUL2, h="center")
    for k in range(5):
        for c in (COL_EQ + k, COL_INS + k):
            put(h, 7, c, str(k + 1), bold=True, size=10, fill=GRIS, h="center")
    put(h, 7, COL_EQ + 5, "/20", size=9, fill=GRIS, h="center")
    put(h, 7, COL_INS + 5, "/20", size=9, fill=GRIS, h="center")
    put(h, 7, COL_INS + 6, "auto − tú", size=9, fill=GRIS, h="center")
    h.row_dimensions[7].height = 18

    for e in range(N_EQUIPOS):
        r = FILA_1 + e
        put(h, r, 1, "Equipo %d" % (e + 1), bold=True, h="center", size=10)
        # los integrantes se escriben UNA vez, en la hoja de la primera sesion;
        # las demas los heredan. Si no, cada hoja pediria volver a escribirlos.
        put(h, r, 2, "" if primera else "='S%s'!B%d" % (ses[0]["nro_sesion"], r),
            fill=AMBAR if primera else GRIS, size=9)
        for k in range(5):
            put(h, r, COL_EQ + k, "", h="center", fill=AMBAR)
            put(h, r, COL_INS + k, "", h="center", fill=AMBAR)
        a, b = get_column_letter(COL_EQ), get_column_letter(COL_EQ + 4)
        c, d = get_column_letter(COL_INS), get_column_letter(COL_INS + 4)
        put(h, r, COL_EQ + 5, '=COUNTA(%s%d:%s%d)*4' % (a, r, b, r), bold=True, h="center")
        put(h, r, COL_INS + 5, '=COUNTA(%s%d:%s%d)*4' % (c, r, d, r), bold=True, size=12,
            h="center", fill=VERDE)
        put(h, r, COL_INS + 6, '=%s%d-%s%d' % (get_column_letter(COL_EQ + 5), r,
                                               get_column_letter(COL_INS + 5), r), h="center")
        h.row_dimensions[r].height = 22

    r = FILA_1 + N_EQUIPOS + 1
    put(h, r, 2, "No lo cumplieron", bold=True, size=9, fill=GRIS, h="right")
    for k in range(5):
        col = get_column_letter(COL_INS + k)
        # equipos que existen (tienen integrantes escritos) menos los que llevan x
        put(h, r, COL_INS + k,
            '=COUNTA(B{f1}:B{f2})-COUNTA({c}{f1}:{c}{f2})'.format(
                c=col, f1=FILA_1, f2=FILA_1 + N_EQUIPOS - 1),
            h="center", size=10, bold=True, fill=ROJO)
    put(h, r, COL_INS + 5, "equipos", size=8, fill=GRIS, h="center")

    for col, anc in zip("AB", [11, 34]):
        h.column_dimensions[col].width = anc
    for k in range(5):
        h.column_dimensions[get_column_letter(COL_EQ + k)].width = 4.5
        h.column_dimensions[get_column_letter(COL_INS + k)].width = 4.5
    h.column_dimensions[get_column_letter(COL_EQ + 5)].width = 7
    h.column_dimensions[get_column_letter(COL_INS + 5)].width = 8
    h.column_dimensions[get_column_letter(COL_INS + 6)].width = 9
    h.freeze_panes = h.cell(row=FILA_1, column=3)
    return h


for k, s in enumerate(ses):
    hoja_sesion(s, k == 0)

# ══ Resumen ═══════════════════════════════════════════════════════════════
rs = wb.create_sheet("Resumen")
rs.sheet_view.showGridLines = False
ncol = 2 + len(ses) + 2
rs.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncol)
put(rs, 1, 1, "RESUMEN — se llena solo. Dice a quién acompañar, y en qué.", bold=True, size=13,
    color="FFFFFF", fill=AZUL, h="center")
rs.row_dimensions[1].height = 26
rs.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncol)
put(rs, 2, 1, "Nota simulada de cada equipo por sesión (la tuya, sobre 20). No se registra.",
    size=10, fill=GRIS)

put(rs, 4, 1, "EQUIPO", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
put(rs, 4, 2, "INTEGRANTES", bold=True, size=10, color="FFFFFF", fill=AZUL2, h="center")
for k, s in enumerate(ses):
    put(rs, 4, 3 + k, "S%s" % s["nro_sesion"], bold=True, size=9, color="FFFFFF", fill=AZUL2,
        h="center")
put(rs, 4, 3 + len(ses), "PROMEDIO", bold=True, size=9, color="FFFFFF", fill=AZUL2, h="center")
put(rs, 4, 4 + len(ses), "SESIONES BAJO 13", bold=True, size=9, color="FFFFFF", fill=AZUL2, h="center")

NOTA = get_column_letter(COL_INS + 5)
for e in range(N_EQUIPOS):
    r, fs = 5 + e, FILA_1 + e
    put(rs, r, 1, "Equipo %d" % (e + 1), bold=True, h="center", size=10)
    put(rs, r, 2, "='S%s'!B%d" % (ses[0]["nro_sesion"], fs), size=9)
    for k, s in enumerate(ses):
        put(rs, r, 3 + k, "='S%s'!%s%d" % (s["nro_sesion"], NOTA, fs), h="center", size=9)
    a, b = get_column_letter(3), get_column_letter(2 + len(ses))
    put(rs, r, 3 + len(ses), '=IFERROR(AVERAGEIF(%s%d:%s%d,">0"),"")' % (a, r, b, r), bold=True,
        h="center", fill=VERDE)
    put(rs, r, 4 + len(ses), '=COUNTIFS(%s%d:%s%d,">0",%s%d:%s%d,"<13")' % (a, r, b, r, a, r, b, r),
        bold=True, h="center", fill=ROJO)
    rs.row_dimensions[r].height = 20

r = 5 + N_EQUIPOS + 1
put(rs, r, 2, "Promedio de la clase", bold=True, size=9, fill=GRIS, h="right")
for k, s in enumerate(ses):
    col = get_column_letter(3 + k)
    put(rs, r, 3 + k, '=IFERROR(AVERAGEIF(%s5:%s%d,">0"),"")' % (col, col, 4 + N_EQUIPOS),
        h="center", size=9, fill=GRIS)

r += 2
rs.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncol)
put(rs, r, 1, "EN QUÉ ÍTEM FALLA LA CLASE — cuántos equipos NO lo cumplieron, sesión por sesión",
    bold=True, size=11, color="FFFFFF", fill=AZUL2)
r += 1
put(rs, r, 1, "ÍTEM", bold=True, size=9, fill=GRIS, h="center")
put(rs, r, 2, "", fill=GRIS)
for k, s in enumerate(ses):
    put(rs, r, 3 + k, "S%s" % s["nro_sesion"], bold=True, size=9, fill=GRIS, h="center")
put(rs, r, 3 + len(ses), "TOTAL", bold=True, size=9, fill=GRIS, h="center")
for i, (n, _) in enumerate(ITEMS):
    r += 1
    put(rs, r, 1, str(i + 1), bold=True, h="center", size=10)
    put(rs, r, 2, n, size=9, bold=True)
    col_item = get_column_letter(COL_INS + i)
    for k, s in enumerate(ses):
        put(rs, r, 3 + k,
            "=COUNTA('S{n}'!B{f1}:B{f2})-COUNTA('S{n}'!{c}{f1}:{c}{f2})".format(
                n=s["nro_sesion"], c=col_item, f1=FILA_1, f2=FILA_1 + N_EQUIPOS - 1),
            h="center", size=9)
    a, b = get_column_letter(3), get_column_letter(2 + len(ses))
    put(rs, r, 3 + len(ses), "=SUM(%s%d:%s%d)" % (a, r, b, r), bold=True, h="center", fill=ROJO)
    rs.row_dimensions[r].height = 20

r += 2
rs.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncol)
put(rs, r, 1, "El ítem con el TOTAL más alto es el que hay que volver a enseñar, no el que hay "
              "que castigar. Un equipo con dos o más sesiones bajo 13 necesita acompañamiento, "
              "no una nota.", size=10, bold=True, color=AZUL, fill=AMBAR)
rs.row_dimensions[r].height = 30

rs.column_dimensions["A"].width = 11
rs.column_dimensions["B"].width = 30
for k in range(len(ses)):
    rs.column_dimensions[get_column_letter(3 + k)].width = 5.5
rs.column_dimensions[get_column_letter(3 + len(ses))].width = 11
rs.column_dimensions[get_column_letter(4 + len(ses))].width = 11
rs.freeze_panes = rs.cell(row=5, column=3)

wb.move_sheet("Resumen", offset=-len(ses))

# ══ Guardar ═══════════════════════════════════════════════════════════════
dest = None
for ciclo in sorted(os.listdir(os.path.join(BASE, "03_Entregables-diseño"))):
    if ciclo.startswith(CARRERA + " - Ciclo"):
        raiz = os.path.join(BASE, "03_Entregables-diseño", ciclo)
        for cur in sorted(os.listdir(raiz)):
            if " - %s - " % CURSO in cur:
                dest = os.path.join(raiz, cur, "Instrumentos de evaluación")
if dest is None:
    raise SystemExit("no encontré la carpeta del curso %s" % CURSO)
OUT = os.path.join(dest, "16_Lista-de-cotejo_Los-cinco-de-siempre.xlsx")
wb.save(OUT)
print("generado:", os.path.basename(OUT))
print("  %d hojas de sesión (S%s a S%s) + Resumen + Cómo se usa · %d equipos"
      % (len(ses), ses[0]["nro_sesion"], ses[-1]["nro_sesion"], N_EQUIPOS))
sin = [s["nro_sesion"] for s in ses if not CONC.get(s["sesion_id"])]
print("  sesiones sin línea de concreción todavía:", ", ".join("S" + x for x in sin) or "ninguna")
```

---

## Lo que tiene que estar en tu clon

- [ ] `05_Base-de-datos/cotejo_excel.py`
- [ ] `05_Base-de-datos/<CARRERA>/listas_cotejo.csv` — con la columna `observable`
- [ ] `05_Base-de-datos/<CARRERA>/sesiones.csv` — con `tema`, `tipo_sesion` y `aprendizaje_esperado`
- [ ] `generar_ppt.py` con el tipo de lámina `cotejo`
- [ ] `openpyxl` instalado

---

## Lista de comprobación

- [ ] ¿Cada sesión de adquisición tiene su fila en `listas_cotejo.csv`?
- [ ] ¿La concreción son los pasos del encargo de esa sesión, y no otra cosa?
- [ ] ¿Cabe en dos renglones y se puede observar en el producto?
- [ ] ¿La lámina va con tipo `cotejo` y el texto vacío?
- [ ] ¿El cuaderno está regenerado, y ninguna hoja marca su línea en rojo?
- [ ] ¿El instructor sabe que **el equipo se marca primero**?
