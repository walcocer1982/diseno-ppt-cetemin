# 14 — La lista de cotejo de sesión: **la lista de cotejo**

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

## Los cinco criterios

Son **los cinco de la rúbrica del colaborativo, un escalón más abajo**. La sesión es el ensayo y el TC es la función: cuando el estudiante llega al colaborativo lleva veinte sesiones practicando exactamente lo que se le va a calificar.

| | Criterio | **Logrado (3)** es… | **Destacado (4)** añade… |
|---|---|---|---|
| 1 | **DESARROLLO TÉCNICO** | Resuelve el problema en su totalidad, utilizando métodos o formas aprendidas en clase | el sustento es **verificable**: la norma con su artículo, el parámetro técnico o la consecuencia específica |
| 2 | **CONCLUSIONES** | La conclusión se desprende del desarrollo y responde a la(s) pregunta(s) del caso | identifica el hecho que, **presentándose como conforme, no lo es**, y describe la discrepancia |
| 3 | **ORGANIZACIÓN DEL PRODUCTO** | El producto está ordenado, tiene claridad y coherencia | expone el **recorrido completo** y puede seguirse sin la explicación oral |
| 4 | **SUSTENTACIÓN ORAL** | Los integrantes exponen la parte que les corresponde, con orden y claridad | **cualquier integrante responde consultas** sobre una parte que no expuso |
| 5 | **TIEMPO DE EXPOSICIÓN** | Se ajusta al tiempo asignado sin desviaciones | se ajusta dentro del 10 % del tiempo asignado |

> **Los enunciados de Logrado los redactó Jorge Canchiz el 2026-09-02** y son la versión que manda. Viven en `CRITERIOS`, dentro de `05_Base-de-datos/cotejo_excel.py`: **se cambian ahí y se regenera**. Editarlos en el `.xlsx` no sirve — se pierden en la siguiente generación.

**El criterio 1 es el que lleva la cobertura.** *«En su totalidad»* es lo que hace que un equipo que resuelve tres pasos de cuatro no pueda estar Logrado, por ordenado y coherente que sea su producto. Sin esa palabra, ningún criterio mediría si respondieron todo.

**Y siguen siendo de forma, no de contenido.** Por eso el mismo juego sirve en un caso de flotación de PM, uno de sostenimiento de EOM y uno de sistemas de gestión de SI. Esa es toda la razón por la que hay un solo instrumento y no setecientos.

> **El criterio 5 funciona con cualquier duración**, así que la misma vara sirve para los 2 minutos de la sustentación de sesión y para los 8 del colaborativo. Sobre 2 minutos: Destacado hasta ±12 s, Logrado hasta ±30 s, En proceso hasta ±60 s.

### La escala

| Valor | **0** | **1** | **2** | **3** | **4** |
|---|---|---|---|---|---|
| **Nivel** | No presenta | En inicio | En proceso | **Logrado** | **Destacado** |

**Cinco criterios × cuatro puntos = 20.**

| | |
|---|---|
| **20** | Destacado en los cinco |
| **15** | **Logrado en los cinco** — el trabajo bien hecho |
| **13** | La nota mínima del curso: tres logrados y dos en proceso |
| **10** | En proceso en todo |
| **0** | No presenta nada |

Es la misma aritmética de las rúbricas de los colaborativos ([§06](06_casos-rubricas-evaluacion.md)), **y es a propósito**.

> **Por qué dejó de ser binaria.** Con sí/no, un equipo que citaba dos hechos de tres y otro que no citaba ninguno recibían la misma marca. La escala de cuatro niveles distingue al que va a medio camino del que no arrancó — que es justamente la conversación que la lista quiere provocar.

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

1. **Se muestra ANTES de trabajar.** La lámina «Lista de cotejo» va en la Aplicación, después del encargo y los casos A y B. El estudiante sabe con qué se le va a mirar **antes** de empezar, no después.
2. **Marca el instructor**, y nadie más. Cinco criterios por equipo, de 0 a 4, mientras cada equipo sustenta.
3. La nota se suma sola. **No entra al promedio.**
4. Se le devuelve al equipo con **una frase**: en qué criterio cayó y qué le habría faltado para subir un nivel.

> **No hay autoevaluación.** Se consideró y se descartó (decisión de Jorge Canchiz, 2026-09-02). El argumento a favor era la brecha —lo que el equipo cree frente a lo que se observa—; el argumento en contra ganó por dos razones prácticas: **duplicaba el tecleo** de cada sesión, y la marca de un equipo novato se desvía hacia arriba de forma sistemática, así que el dato exigía una conversación que no siempre cabe en el cierre. **La lista mide desempeño observado, no percepción.**
>
> Lo que la autoevaluación aportaba —que el estudiante conozca el criterio antes de trabajar— lo sigue dando el **paso 1**: la lámina se muestra antes, siempre.

---

## La lámina

En `laminas.csv` va con **tipo `cotejo`** y el **texto vacío**. El generador la arma: a la izquierda los cinco criterios y la escala de 0 a 4; a la derecha, **con qué se te va a mirar**.

> **PENDIENTE:** el texto de la derecha todavía dice *«Márcate tú primero. Después marco yo»*, que era de la versión con autoevaluación. Hay que reemplazarlo cuando se rehaga la lámina.

**La lámina NO lleva la concreción de la sesión.** Se probó y se quitó: repetía el encargo, que el estudiante acaba de ver dos láminas antes, y leída suelta —*«Hoy, "completo" es…»*— parecía la definición de una palabra sin dueño. La concreción sigue viviendo en `listas_cotejo.csv` y en el guion, que es donde el instructor la necesita para marcar.

```
laminas.csv  →  tipo = cotejo, texto vacío  →  generar_ppt.py la compone
```

**No se escribe el contenido de esa lámina.** Si aparece escrito en `laminas.csv`, alguien lo copió y se va a desincronizar.

Va en el momento de **Aplicación**, después de «A trabajar».

---

## La hoja del instructor

**Una sola hoja, genérica, que se usa y se descarta.** Se genera así:

```
cd 05_Base-de-datos
python cotejo_excel.py SI-SGCSSMA
```

Sale en `03_Entregables-diseño/<CARRERA> - Ciclo N/<n> - <CURSO> - .../Instrumentos de evaluación/16_Lista-de-cotejo.xlsx`.

| | |
|---|---|
| **Arriba** | Casillas en blanco: **sesión, fecha, instructor** y **la consigna de hoy**, que el instructor copia del guion |
| **La rejilla** | Los cinco criterios en filas —cada uno con **qué es estar Logrado**— y ocho equipos en columnas. Cada celda es un desplegable de 0 a 4 y no acepta otra cosa |
| **La nota** | Se suma sola al pie de cada columna. **Verde si llega a 13, roja si no.** Una columna sin marcar queda en blanco: no muestra un cero falso |

**La hoja termina en la nota.** No lleva pie: ni los enunciados del nivel Destacado ni la rutina de tres minutos, que se retiraron el 2026-09-02. La lista es la rejilla y nada más — cabe holgada en **una hoja apaisada**, se imprime o se llena en pantalla, se le devuelve al equipo y se descarta. Lo que decía el pie vive aquí, en el §14, que es donde el instructor lo consulta una vez y no cada sesión.

> **No hay una hoja por sesión, ni hoja de resumen, ni historial.** Se hizo así y se deshizo (decisión de Jorge Canchiz, 2026-09-02). **La evaluación es formativa: no se registra y no se guarda.** Lo de la sesión pasada no interesa en la siguiente, y con veinticuatro hojas el instructor terminaba administrando un archivo que nadie iba a leer.
>
> Por eso la hoja es **genérica**: la misma sirve para un curso de 96 horas con 24 sesiones y para uno de 48 con 12. Lo que cambia cada día —la sesión y la consigna— va en blanco.

**El número de equipos** está en `N_EQUIPOS`, dentro del script. Por defecto 8.

---

## Lo que esta lista NO hace

**No caza el error técnico fino.** Si un equipo escribe *supervisor* donde correspondía *comité*, el criterio 1 lo caza solo si el instructor lo nota.

Esta lista mide **si el trabajo está bien hecho**, no si la respuesta es correcta. Y está bien que así sea: la corrección técnica la juzga **la rúbrica del colaborativo**, con criterios propios de ese caso. La lista de sesión sirve para otra cosa — que el estudiante sepa cómo va, semana a semana, con el mismo espejo siempre.

**Si necesitas juzgar la corrección de una sesión concreta**, no toques los cinco criterios: aprieta la **línea de concreción**. Ahí es donde entra lo técnico de esa clase.

---

## El generador, completo

Está en `05_Base-de-datos/cotejo_excel.py`. Va aquí dentro para que **el documento y el código no puedan separarse**: si copias este MD, copias el generador.

```python
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
          "se le devuelve al equipo y se descarta. Los seis eventos calificados —CV1, CV2, EP, EF, "
          "TC1 y TC2— siguen siendo los únicos que dan nota.", size=9, fill=AMBAR)
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
