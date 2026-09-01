# 13 — Orden de trabajo de una unidad didáctica

**Aplica a los 35 cursos, desde ahora.** Fija en qué orden se produce el diseño de un curso y qué se entrega en cada paso.

Sale de haber hecho la sesión 1 de SI al revés: primero los aprendizajes esperados sacados del temario, después los colaborativos. Funcionó, pero costó dos reestructuraciones — y en el camino apareció un punto clave que se enseñaba y no se aplicaba en ninguna parte. **El colaborativo define hacia dónde va todo; si se diseña al final, lo anterior no apunta a nada.**

Complementa al [§03](03_pipeline-de-plantillas.md) —que dice qué plantillas existen— y al [§04](04_matriz-y-distribucion.md) —que dice cómo se reparte por bloques—. Este dice **en qué orden se hace**.

---

## La secuencia

```
       triangulación (001A) — la capacidad y los indicadores, intocables
                    ↓
   ①  LOS DOS TRABAJOS COLABORATIVOS          TC1 y TC2, con sus rúbricas
                    ↓
   ②  LOS APRENDIZAJES ESPERADOS              10 o 20, uno por sesión
                    ↓
   ③  LOS DOS CASOS DE LA SESIÓN           caso A y caso B, otros datos
                    ↓
   ④  LA CONCRECIÓN DE LA LISTA               una línea: qué es «completo» hoy
                    ↓
   ⑤  LOS PUNTOS CLAVE                        3 a 5, del temario oficial
                    ↓
   ⑥  EL PPT DE LA SESIÓN                     la proyección
```

**Cada paso se hace para el anterior.** Si un paso no sirve al de arriba, sobra.

> **Por qué la lista de cotejo va antes que los puntos clave.** Parece invertido y no lo es: la lista dice **qué tiene que quedar observable**, y los puntos clave son **lo que hay que enseñar para que lo esté**. Al revés se enseña primero y luego se busca qué evaluar, que es como se acaba evaluando algo que la sesión no enseñó.

---

## Paso 0 · La triangulación manda

**No es un paso, es el suelo.** La capacidad y los indicadores bajan del formato oficial 7A y **no se reformulan** (regla 2 del `CLAUDE.md`). Todo lo que sigue tiene que caber debajo:

- el **verbo del indicador es el techo**: si dice *describe*, ninguna rúbrica puede pedir *recomienda*
- los **contenidos del temario** son el piso de cobertura: si un contenido oficial no llega a ningún aprendizaje esperado, es un hueco y **se reporta** en `observaciones.csv`

---

## ① Los dos trabajos colaborativos

Se diseñan **primero**, con el [§12](12_PARAMETROS-TC.md) en la mano: sus parámetros, el relato en párrafos y el riesgo sin rotular.

> **El colaborativo no lleva casos A y B: es un solo caso para toda la clase.** Es la evaluación del bloque y todos tienen que rendir sobre lo mismo — si cada mitad resuelve un caso distinto, las notas dejan de ser comparables. Los casos A y B son de los **casos de sesión**, donde sí sirven: ahí el trabajo es formativo y lo que se busca es que dos equipos no se copien.

Sale de aquí:

| | Dónde vive |
|---|---|
| El caso de TC1 y el de TC2, **uno cada uno, un solo caso** | `casos.csv` · `alcance = colaborativo` |
| Las dos rúbricas: 5 criterios × 4 puntos = 20 | `rubricas.csv` |
| Qué indicador evalúa cada criterio | `rubricas.csv · indicador_id` |

**Comprobación:** `python revisar_tc.py <CARRERA>`.

Los criterios 4 y 5 son literales en los 70 colaborativos —*Presentación PPT: contenido y diseño* y *Presentación oral: dominio y claridad*—; los tres primeros siguen el recorrido **entender → resolver → interpretar** ([§06](06_casos-rubricas-evaluacion.md)).

---

## ② Los aprendizajes esperados

**Uno por sesión de adquisición.** Cuántos, según la carga:

| Horas | Sesiones | De adquisición | **Aprendizajes esperados** |
|---|---|---|---|
| 48 | 12 | 10 | **10** |
| 96 | 24 | 20 | **20** |

Las de evaluación —donde se sustentan los colaborativos— no llevan aprendizaje esperado propio: sustentan el del bloque.

### Cómo se derivan

Cada aprendizaje esperado tiene que **tributar a un criterio** de TC1 o de TC2. Se anota a cuál, en la columna *Tributa a* de la matriz.

**Pero no se derivan solo del colaborativo.** Tienen que respetar los **indicadores de logro involucrados**: el TC marca la dirección, el indicador marca el alcance. Un aprendizaje esperado que sirve al criterio pero se sale del indicador está mal, aunque el caso lo pida.

### Las cinco comprobaciones

| | Qué se comprueba |
|---|---|
| 1 | El verbo no supera al del indicador |
| 2 | La sesión promete **una sola cosa** |
| 3 | Traza a un criterio de TC1 o TC2 |
| 4 | Cabe dentro del indicador que ese criterio evalúa |
| 5 | El contenido tiene prerrequisito en el itinerario ([§03](03_pipeline-de-plantillas.md)) |

**Un criterio de rúbrica sin sesiones que lo alimenten es un hueco.** Se ve de un vistazo en la matriz.

---

## ③ Dos casos por sesión

**Son dos casos con el mismo procedimiento, no dos casos distintos.** Mismo procedimiento, mismos pasos, misma respuesta esperada — **cambian la empresa y los datos**. Existen para que dos equipos no se copien y para que la discusión pueda cruzarlas.

**Y son solo de la sesión.** El colaborativo va con un solo caso (paso ①): ahí se califica y todos deben rendir sobre el mismo caso.

> **El error que hay que evitar.** En la sesión 1 de SI se hicieron primero dos casos que se resolvían de forma distinta: uno pedía clasificar documentos y el otro razonar sobre la constancia del servicio. Eso no es caso A y caso B: son dos sesiones metidas en una. Hubo que rehacerlo.

Se redactan con las reglas del [§12](12_PARAMETROS-TC.md), en versión corta: **relato, datos dentro de la historia, riesgo sin rotular y sin nombrar la respuesta**.

| | Dónde vive |
|---|---|
| Descripción, pregunta gatilladora, producto | `casos.csv` · `alcance = sesion` |
| El texto de cada caso | `casos.csv · caso_a` y `caso_b` |

**Y el caso de sesión tributa al colaborativo:** la suma de los casos de un bloque construye el caso del TC que lo cierra ([§04](04_matriz-y-distribucion.md)).

---

## ④ La lista de cotejo — **los cinco de siempre**

**El instrumento completo está en el [§14](14_LISTA-DE-COTEJO.md).** Aquí solo lo que hace falta para no equivocar el paso.

Es **una sola lista**, la misma en las 24 sesiones de los 35 cursos y en las tres carreras: cinco ítems binarios de cuatro puntos —COMPLETO · CON LOS DATOS DEL CASO · CON EL TÉRMINO CORRECTO · CON EL PORQUÉ · SUSTENTADO POR TODOS—. **Con cuatro de cinco, apruebas.**

**Lo que este paso produce es una línea, no una lista:** qué significa «completo» en esta sesión. Y no se inventa — **son los pasos del encargo** que el caso ya trae del paso ③, separados por `·`.

| | Dónde vive |
|---|---|
| Los cinco ítems y la escala | §14 y `generar_ppt.py`. **No se copian a ninguna tabla** |
| La línea de concreción | `listas_cotejo.csv` · **una fila por sesión**, columna `observable` |
| La lámina | tipo **`cotejo`** en `laminas.csv`, con el texto **vacío**: la arma el generador |

**No promedia.** Los seis eventos calificados están cerrados y suman 100 %: CV1 y CV2 (5 % cada uno), EP (20 %), EF (20 %), TC1 (25 %) y TC2 (25 %). La nota de la lista es una **simulación**: le dice al estudiante cuánto sacaría si esa sesión se calificara.

---

## ⑤ Los puntos clave

**De 3 a 5 por sesión**, y cada uno con su `origen`:

- **`oficial`** — baja del temario de la triangulación
- **`propuesto`** — con quién lo aprobó y cuándo

**Un punto clave sin origen es uno que alguien inventó.**

Se eligen **para que la lista de cotejo se pueda marcar**. Si un ítem de la lista no tiene un punto clave que lo enseñe, o sobra el ítem o falta el contenido — y si falta contenido, se pide y **lo aprueba el instructor líder**; no se añade por cuenta propia ([§05](05_diseno-de-sesion.md)).

Cada punto clave lleva su **desarrollo**: de 7 a 10 ideas de 8 a 11 palabras. Es lo que llena las láminas de tema, y es lo que más se olvida.

| | Dónde vive |
|---|---|
| Enunciado, indicador y origen | `contenidos.csv` |
| Las ideas de desarrollo | `contenidos.csv · desarrollo` |

---

## ⑥ El PPT de la sesión

Se produce con el [§11](11_legibilidad-de-laminas-y-esquemas.md): insumos mínimos, presupuesto de 28 a 32 láminas, esqueleto, rutina y técnica por momento, bandas de texto, tamaños de imagen y paleta.

```
laminas.csv  →  generar_ppt.py  →  revisar_ppt.py  →  mirar lo marcado  →  entregar
```

**El PPT es el último paso, no el primero.** Cuando se empieza por él, las láminas deciden el contenido — y aparecen puntos clave inventados para llenar diapositivas.

---

## El seguimiento

**La matriz de distribución es el tablero.** Tiene una fila por sesión y una columna por paso: aprendizaje esperado · a qué criterio tributa · caso A · caso B · lista de cotejo · puntos clave · PPT. Verde lo hecho, rojo lo que falta, y un bloque de avance con el porcentaje de cada paso.

**Dos reglas sobre la matriz:**

1. **Los bloques van en el orden de la secuencia:** primero los colaborativos, después las sesiones. Y las columnas de la tabla de sesiones son los pasos ② a ⑥, de izquierda a derecha. Se lee como se trabaja.
2. **Se genera desde la base de datos**, no se escribe a mano. Se carga la información en los CSV y se vuelve a generar: así refleja el estado real y no una intención.
3. **Nunca se duplica.** Un solo archivo por curso. Nada de `01_`, `03_`, `_v2`, `_final`. Si hay dos matrices, alguien va a leer la equivocada.

```
python matriz.py
```

---

## Lista de comprobación del curso

- [ ] ¿Los dos colaborativos están en `casos.csv` —**uno cada uno, un solo caso**— con sus rúbricas de 5 criterios?
- [ ] ¿`revisar_tc.py` pasa?
- [ ] ¿Hay 10 o 20 aprendizajes esperados, según la carga?
- [ ] ¿Cada uno tributa a un criterio, y cabe dentro de su indicador?
- [ ] ¿Cada criterio de rúbrica tiene al menos una sesión que lo alimenta?
- [ ] ¿Cada contenido oficial del temario llega a algún aprendizaje esperado?
- [ ] ¿Cada sesión tiene sus **dos casos A y B**, con el mismo procedimiento?
- [ ] ¿Cada sesión tiene su línea de concreción en `listas_cotejo.csv`?
- [ ] ¿La concreción de «completo» son los pasos del encargo de esa sesión?
- [ ] ¿De 3 a 5 puntos clave por sesión, todos con `origen`?
- [ ] ¿El PPT pasa `revisar_ppt.py` y se miraron las láminas marcadas?
- [ ] ¿La matriz está regenerada y es la única?
