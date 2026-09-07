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
   ⑥  EL RECURSO AUTÓNOMO DEL BLOQUE       lectura + video + autoevaluación
                    ↓
   ⑦  EL PPT DE LA SESIÓN                     la proyección
```

**Cada paso se hace para el anterior.** Si un paso no sirve al de arriba, sobra.

### El orden no se salta, y menos por el final

**Regla de Jorge Canchiz, repetida el 2026-09-02:**

> **No se habla de armar el PPT sin tener antes los dos casos, y sin haber comprobado que de verdad demuestran el aprendizaje esperado.**
> **Recién con los casos delante se eligen los puntos clave.**
> **Y el PPT se arma AL FINAL, pensando en cumplir los puntos clave y en lo que los casos A y B piden.**

| | Se hace | Mirando a |
|---|---|---|
| ② | El aprendizaje esperado, partido en sus partes | El indicador y el criterio al que tributa |
| ③ | **Los dos casos** | Que cada parte del AE tenga un paso del encargo que la demuestre |
| ④ | La concreción de la lista | Los pasos del encargo |
| ⑤ | **Los puntos clave** | **Que el caso se pueda resolver.** Salen del temario oficial, pero *cuáles* y *con qué desarrollo* lo decide el caso |
| ⑥ | **El recurso autónomo** del bloque | Que el estudiante llegue a esas sesiones sabiendo lo que hace falta ([§16](16_RECURSOS-AUTONOMOS-Y-VIDEO.md)) |
| ⑦ | El PPT | Los puntos clave y lo que los casos piden |

**El recurso autónomo va después de los puntos clave y no antes.** Un cuadernillo escrito a ciegas enseña lo que a uno le parece; escrito con los puntos clave delante, **prepara exactamente lo que las sesiones van a construir encima**. Y es urgente sin parecerlo: el CV1 se responde **antes de la sesión 1**, así que su recurso tiene que estar listo antes de que el curso empiece.

**No es solo lectura.** Lectura, video y autoevaluación, en la proporción que el tema pida — la decide el instructor líder, y lo único obligatorio es que los minutos sumen 90 ([§16](16_RECURSOS-AUTONOMOS-Y-VIDEO.md)).

**Por qué el PPT va último, y no es una manía de orden.** Cuando se empieza por las láminas, las láminas deciden el contenido: aparecen puntos clave inventados para llenar diapositivas, y casos escritos para encajar en lo que ya se dibujó. Pasó en la S1 y en la S2, y costó rehacerlas.

**Y el paso ⑤ tiene dos amos, no uno.** Los puntos clave bajan del temario oficial —eso no se negocia— pero **el caso decide cuáles de ellos entran y qué ideas se desarrollan**. Un punto clave que el caso no necesita se enseña y no se aplica: es el error que dejó huérfano *«por qué la empresa se ordena por procesos»* en la S1.

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

### Antes de escribir una sola línea: leer el aprendizaje esperado

**Regla de Jorge Canchiz, 2026-09-01. No se negocia.**

**Nunca se trabaja a ciegas.** Antes de crear el caso A, el caso B o cualquier pieza de una sesión, se abre el aprendizaje esperado de esa sesión y **se lee entero, palabra por palabra**.

Y no basta leerlo: hay que **partirlo y comprobar que cada mitad tiene quién la demuestre**.

| Paso | Cómo se comprueba |
|---|---|
| 1 | Partir el aprendizaje esperado en sus partes. *«Describe qué información documentada exige la ISO 9001 **y por qué su cumplimiento es voluntario, a diferencia del sistema que manda la ley**»* son **dos** |
| 2 | Para cada parte, señalar **qué punto clave la enseña** |
| 3 | Para cada parte, señalar **qué paso del encargo la hace demostrar** |
| 4 | Si una parte no tiene punto clave o no tiene paso, **el caso está incompleto** — se corrige antes de seguir |
| 5 | Y el conjunto tiene que caber en el indicador y servir al criterio al que la sesión tributa |

> **De dónde sale esta regla.** La S4 se escribió sin hacerlo. Sus dos casos quedaban impecables y **la segunda mitad del aprendizaje esperado no se demostraba en ninguna parte**: un equipo podía resolver el caso perfecto sin tocar nunca la diferencia entre lo voluntario y lo obligatorio. Y esa mitad estaba ahí porque la S4 tributa al criterio 1 del TC1, que la pide.
>
> **Un caso bonito que no demuestra el aprendizaje esperado es trabajo perdido.**

### Y la matriz se actualiza siempre

Cada vez que una sesión avanza —caso, concreción, puntos clave, PPT— **se regenera la matriz de distribución**:

```
python matriz.py
```

**Un solo archivo por curso, y se genera; no se escribe a mano ni se duplica.** Nada de `_v2` ni `_final`. Si hay dos matrices, alguien va a leer la equivocada.

---



**Son dos casos con el mismo procedimiento, no dos casos distintos.** Mismo procedimiento, mismos pasos, misma respuesta esperada — **cambian la empresa y los datos**. Existen para que dos equipos no se copien y para que la discusión pueda cruzarlas.

**Y son solo de la sesión.** El colaborativo va con un solo caso (paso ①): ahí se califica y todos deben rendir sobre el mismo caso.

> **El error que hay que evitar.** En la sesión 1 de SI se hicieron primero dos casos que se resolvían de forma distinta: uno pedía clasificar documentos y el otro razonar sobre la constancia del servicio. Eso no es caso A y caso B: son dos sesiones metidas en una. Hubo que rehacerlo.

Se redactan con las reglas del [§12](12_PARAMETROS-TC.md), en versión corta: **relato, datos dentro de la historia, riesgo sin rotular y sin nombrar la respuesta**.

### Que sea retador, no descriptivo

**Un caso que solo describe un desorden no da nada que pensar.** «Hay tres archivos con el mismo nombre, descríbelo» se resuelve leyendo. Estos cinco ingredientes lo cambian, y caben en 170 palabras:

| | Qué es | Ejemplo (S4) |
|---|---|---|
| **Un reloj** | Algo se decide en una fecha | *El acta se firma el viernes* |
| **Un número que duele** | La consecuencia tiene precio | *S/ 8 000 por día de atraso* |
| **Alguien que se juega algo** | Una persona con nombre y cargo | *El jefe de laboratorio que recibió la revisión 4* |
| **Un riesgo contado de pasada** | Nunca rotulado como riesgo | *«En otra obra un soporte cedió con la faja cargada; no hubo heridos porque era domingo»* |
| **Un dato que contradice** | Lo que parece bien hecho y no lo está | *El registro de torque está completo y dentro de tolerancia — la de la revisión vieja* |

**El quinto es el que separa las notas.** Sin él, todos los equipos llegan a lo mismo leyendo. Con él, el equipo que solo lee llega a la conclusión contraria.

### La empresa cambia en cada sesión

**El colaborativo tiene su propia empresa, y no aparece en ninguna sesión.**

> **Regla de Jorge Canchiz, 2026-09-01: los trabajos colaborativos son independientes de los casos de sesión.** No comparten empresa. Si la misma contratista sale en la clase y en el trabajo calificado, el estudiante reconoce el patrón antes de pensar — y el TC deja de medir lo que cree medir.

En SI-SGCSSMA, **Servicios Mineros Huanza S.A.C. es exclusiva de los dos colaborativos**. Ninguna sesión la menciona.

**Los casos de sesión, no.** Cada sesión estrena empresa y **rubro distinto**: laboratorio de ensayo, montaje electromecánico, voladura, sostenimiento, perforación diamantina, manejo de residuos, catering, transporte de concentrado, planta de tratamiento de agua…

### El caso se basta a sí mismo

**Regla de Jorge Canchiz, 2026-09-01.** Un caso de sesión **no depende de recursos externos**: ni plantillas, ni anexos, ni extractos de norma. Lo único que el equipo recibe es **el relato**.

| De dónde sale cada cosa | |
|---|---|
| Los datos | **Del relato.** Si hace falta un número, va dentro de la historia |
| El criterio para juzgarlos | **De la sesión.** Es lo que se acaba de enseñar en la Adquisición |
| La estructura del producto | **Del encargo.** Cuatro pasos, cuatro filas en una hoja en blanco |

**Por qué, y no es solo por ahorrar trabajo:** si el criterio viene en una hoja, el alumno **copia**. Si tiene que salir de la sesión, tuvo que haberla escuchado. La hoja convierte una tarea de aplicación en una de transcripción.

> **Esto es de los casos de SESIÓN.** Los **colaborativos sí llevan recursos** —el anexo de datos, la relación para marcar—: ahí son dos horas de trabajo autónomo, se califica, y el instrumento es lo que hace que quepa en el tiempo (§12).

### Y el nombre de la empresa, sobrio

**Nombre técnico, descriptivo del rubro, con su forma societaria.** Como se llaman de verdad las contratistas.

| Así sí | Así no |
|---|---|
| Servicios Analíticos Industriales S.A.C. | Andes Analítica |
| Ingeniería y Montaje Electromecánico S.A.C. | Montajes Chalhuane |
| Servicios Mineros Huanza S.A.C. | MineraPro · GeoAndes · SafeMining |

**Nada de nombres de marca ni de fantasía.** El caso tiene que leerse como un expediente, no como un anuncio: el alumno va a trabajar con empresas que se llaman así, y el nombre no debe distraer de los datos.

> **Y el texto del caso es dato, no markdown.** Nada de `**negritas**` ni de viñetas dentro del CSV: ese texto se dibuja en la ficha del caso tal cual, y los asteriscos salen impresos. Si algo tiene que destacar, lo destaca la frase, no el formato.

Tres razones, y ninguna es estética:

1. **El alumno deja de reconocer el patrón.** Con la misma empresa veinte veces, a la quinta ya sabe qué le van a preguntar.
2. **El contenido se ve en contextos distintos**, que es lo que permite transferirlo. Un control de documentos en un laboratorio y en una obra de montaje no se parecen, y el criterio es el mismo.
3. **El egresado va a trabajar en cualquiera de esos rubros**, no en la contratista de mantenimiento del ejemplo.

> **Lo que sí se mantiene:** el caso A y el caso B de una misma sesión son **dos empresas distintas resolviendo lo mismo**. Eso no cambia — es lo que hace que se puedan cruzar en la Discusión.

| | Dónde vive |
|---|---|
| Descripción, pregunta gatilladora, producto | `casos.csv` · `alcance = sesion` |
| El texto de cada caso | `casos.csv · caso_a` y `caso_b` |

**Y el caso de sesión tributa al colaborativo:** la suma de los casos de un bloque construye el caso del TC que lo cierra ([§04](04_matriz-y-distribucion.md)).

---

## ④ La lista de cotejo — **la lista de cotejo**

**El instrumento completo está en el [§14](14_LISTA-DE-COTEJO.md).** Aquí solo lo que hace falta para no equivocar el paso.

Es **una sola lista**, la misma en las 24 sesiones de los 35 cursos y en las tres carreras: cinco ítems binarios de cuatro puntos —COMPLETO · CON LOS DATOS DEL CASO · CON EL TÉRMINO CORRECTO · CON EL PORQUÉ · SUSTENTADO POR TODOS—. **Con cuatro de cinco, apruebas.**

**Lo que este paso produce es una línea, no una lista:** qué significa «completo» en esta sesión. Y no se inventa — **son los pasos del encargo** que el caso ya trae del paso ③, separados por `·`.

| | Dónde vive |
|---|---|
| Los cinco ítems y la escala | §14 y `generar_ppt.py`. **No se copian a ninguna tabla** |
| La línea de concreción | `listas_cotejo.csv` · **una fila por sesión**, columna `observable` |
| La lámina | tipo **`cotejo`** en `laminas.csv`, con el texto **vacío**: la arma el generador |

**No promedia.** Los eventos calificados están cerrados y suman 100 %: los **cuestionarios de verificación** —cuatro en un curso de 96 h, dos en uno de 48 h—, el **examen parcial**, el **examen final** y los **dos trabajos colaborativos** (§06). La nota de la lista es una **simulación**: le dice al estudiante cuánto sacaría si esa sesión se calificara.

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

## ⑦ El PPT de la sesión

Se produce con el [§11](11_legibilidad-de-laminas-y-esquemas.md): insumos mínimos, presupuesto de 28 a 32 láminas, esqueleto, rutina y técnica por momento, bandas de texto, tamaños de imagen y paleta.

```
laminas.csv  →  generar_ppt.py  →  revisar_ppt.py  →  mirar lo marcado  →  entregar
```

**El PPT es el último paso, no el primero.** Cuando se empieza por él, las láminas deciden el contenido — y aparecen puntos clave inventados para llenar diapositivas.

---

## El seguimiento

**La matriz de distribución es el tablero.** Tiene una fila por sesión y una columna por paso: aprendizaje esperado · a qué criterio tributa · caso A · caso B · lista de cotejo · puntos clave · PPT. Verde lo hecho, rojo lo que falta, y un bloque de avance con el porcentaje de cada paso.

**Dos reglas sobre la matriz:**

1. **Los bloques van en el orden de la secuencia:** primero los colaborativos, después las sesiones. Y las columnas de la tabla de sesiones son los pasos ② a ⑦, de izquierda a derecha. Se lee como se trabaja.
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
