# 03 — Pipeline de plantillas CETEMIN (001 → 005)

**CETEMIN ya tiene un sistema oficial de plantillas de diseño instruccional.** No hay que inventar formatos: el trabajo de diseño consiste en **llenar bien estas plantillas** (evitando los 8 errores, §08). Están en el repositorio P16 (ver §09), en las carpetas de cada curso.

## Paso 1 · Triangulación y sílabo

**Antes de tocar nada de un curso se leen sus dos documentos de origen — y en este orden.** Están juntos en la misma carpeta del paquete: `1. Triangulación y sílabo/`.

| | Documento | Qué es |
|---|---|---|
| **1.º** | **Triangulación** (001A) | La **fuente**. Un solo cuadro con capacidad ↔ indicadores ↔ contenidos ↔ evaluación. De visualización solo para instructores |
| **2.º** | **Sílabo** (002A) | Lo que se **deriva** de ella para el estudiante |

**Por qué la triangulación va primero:** es el documento que muestra las cuatro columnas alineadas, que es justo lo que hay que auditar. El sílabo las presenta en prosa y por separado, así que un desajuste entre capacidad e indicadores se ve en la triangulación y se disimula en el sílabo.

**Y por qué el sílabo va después, no en lugar de:** es lo que recibe el estudiante. Si difiere de la triangulación, esa diferencia ya es un hallazgo.

> **Error cometido, para no repetirlo.** Se auditó la capacidad de EOM · Métodos de explotación leyendo solo el sílabo, y la conclusión —*"la capacidad parece ser de otro curso"*— quedó mal formulada. La triangulación traía la sumilla, que dice que el curso tributa a las **UC 02 y 03** (*"Controlar las condiciones de perforación y voladura"*): la capacidad **no es de otro curso, es la de la unidad de competencia del módulo**. El problema real es otro —capacidad e indicadores están a distinta altura—. Verificar contra el documento derivado da un diagnóstico plausible y equivocado.

Lo que se saca de este paso, antes de seguir:

1. **La capacidad y los indicadores, transcritos literalmente** — primero como están, antes de juzgarlos. Lo que se cambie después queda registrado (regla 2 del `CLAUDE.md`).
2. **Si capacidad, indicadores y contenidos hablan de lo mismo.** Aquí aparecen los desajustes de origen.
3. **Los contenidos oficiales**, que son la materia prima de los puntos clave.
4. **Toda diferencia entre triangulación y sílabo**, registrada en `observaciones.csv`.

### Cada paso cierra con feedback

Terminado el paso se emite un **juicio corto y por partes** —qué está bien, qué falla y con qué evidencia—, no un resumen de lo leído. Sirve para decidir si se sigue o se para.

### Cuando un indicador es impreciso, mira primero si basta la rúbrica

Un indicador vago —*"describe los **principales** métodos"*, sin decir cuántos— hace que dos evaluadores califiquen distinto el mismo trabajo. Se puede corregir el indicador; pero antes conviene ver si la rúbrica ya resuelve el problema.

```
indicador (7A)      →  "los principales métodos"
rúbrica  (nuestra)  →  "los seis métodos del curso"
```

**Se obtiene la misma consistencia de calificación sin abrir una diferencia con el sílabo.** No es una prohibición: es que la vía barata suele bastar, y conviene reservar el cambio del indicador para lo que de verdad no se puede resolver abajo.

*El indicador es el techo; la rúbrica es la que mide.*

### Pedir aprobación es dar la ubicación

Nunca *"¿apruebas los tres esquemas?"*. Siempre **qué es, dónde está y dónde quedó registrado**:

```
Ciclo de minado · sesión 1
   archivo   04_Recursos-graficos/EOM/esquemas/ciclo-de-minado_s1.png
   registro  05_Base-de-datos/imagenes.csv → IMG-CICLO-S1
   lámina    S1 · orden 7
```

**Quien aprueba no tiene que buscar lo que aprueba.** Sin la ruta, la pregunta obliga al instructor a rastrear el archivo, y lo que ocurre en la práctica es que aprueba sin mirar — con lo cual la firma deja de valer.

Vale igual para textos: si se pide validar una rúbrica, se dice el archivo, la fila y el criterio.

### Toda decisión se firma

Una observación no se cierra sola. Por eso `observaciones.csv` lleva **`decision`** y **`aprobado_por`**: qué se resolvió, por qué y quién lo decidió, con fecha.

**Decide el instructor líder de la carrera**, también cuando toca capacidad o indicadores. No hace falta autorización previa de nadie: lo que hace falta es que quede escrito.

> **Por qué se registra igual.** Capacidad e indicadores figuran en el sílabo, así que cambiarlos abre una diferencia entre la base y el documento oficial. El registro no es un permiso — es lo que permite, meses después, **saber si esa diferencia fue una mejora o un descuido**, y tramitar la corrección del sílabo cuando toque.

> Ejemplo real: `OBS-EOM-METEXP-12` — *"Opción A · no se toca el indicador; la precisión va a la rúbrica y al aprendizaje esperado"*, firmado y fechado.

## Paso 2 · Sesiones, aprendizajes esperados y puntos clave

Con los indicadores ya auditados, se reparten las **12 sesiones** y se redacta qué logra cada una. **Se revisan todas, no solo las que se van a cambiar**: un curso donde la mitad de las sesiones se replanteó y la otra mitad no, queda peor que antes.

### El reparto

Cada bloque tributa a los indicadores de su colaborativo. En EOM · Métodos de explotación:

```
Bloque 1 · S1–S5 adquisición + S6 evaluación  →  IND 1 y 2  →  TC1
Bloque 2 · S7–S11 adquisición + S12 evaluación →  IND 3      →  TC2
```

**La última sesión de adquisición ensaya el colaborativo.** S11 hace exactamente la tarea que el TC2 evalúa, con otro yacimiento. El alumno llega a la evaluación habiendo hecho una vez lo que se le va a pedir.

### Las cinco comprobaciones

| | Qué se comprueba | El error que evita |
|---|---|---|
| 1 | **El verbo de la sesión no supera al del indicador** | El indicador dice *explica* y la sesión enseñaba a *seleccionar y combinar*: se enseña más de lo que se puede evaluar |
| 2 | **Una sesión promete una sola cosa** | *"Analizar la productividad, los costos, la dilución y la seguridad"* — cuatro promesas en 135 minutos no se cumplen |
| 3 | **Los puntos clave dicen lo mismo que el aprendizaje esperado** | El aprendizaje se corrigió y los puntos clave se quedaron con el enfoque viejo |
| 4 | **El tema respeta la distribución de los puntos clave** | Se propusieron temas nuevos sin mirar los puntos que ya existían y quedaron cruzados |
| 5 | **El contenido tiene prerrequisito en el itinerario** | Ver abajo |

### Comprobar el itinerario, no la dificultad

Antes de dar por bueno un contenido, mirar **qué cursos llevó el estudiante antes** (`cursos.csv`, columna `ciclo`).

> **Caso real.** Las sesiones 8, 9 y 10 pedían justificar con **criterios de costo y productividad** (TM/Hg, $/TM, dilución). Los cuatro cursos previos del ciclo I son de geología: **ninguno de matemática, costos ni economía**. No era contenido difícil — era contenido **sin prerrequisito**. Se retiró (`OBS-13`).
>
> El mismo itinerario dio la respuesta contraria en otro punto: *Cartografía geológica y geomecánica* está en ciclo I, así que **el RMR sí lo traen**, y las condiciones geomecánicas se pueden exigir sin problema.

**La pregunta no es «¿es muy difícil?» sino «¿dónde lo aprendió?».** Si no hay curso previo que lo dé, el contenido sobra por mucho que convenga al tema.

### Antes de proponer, abrir lo que ya existe

**El paquete del curso trae más de lo que parece.** Antes de redactar nada, listar qué documentos tocan el tema y abrirlos todos:

```
1. Triangulación y sílabo/        ← capacidad, indicadores, contenidos, evaluación
2. Recursos de evaluación/        ← casos, rúbricas, CV, exámenes (las INDICACIONES, no solo la rúbrica)
3. Sesiones y PPTS/               ← los planes de sesión 003A ya redactados, y los PPT
4. Recursos autónomos/            ← lo que el estudiante trabaja en el asincrónico
```

Y dentro de la base: los puntos clave y los enlaces que ya estén cargados.

> **Ocurrió cuatro veces en una sola sesión de trabajo:** se auditó la capacidad sin abrir la triangulación; se propusieron temas de sesión sin mirar los puntos clave existentes; se diseñó la ruta de la sesión 1 sin abrir los **doce planes oficiales**, que eran más detallados; y se diagnosticó una capacidad ajena sin comparar con los cursos hermanos del módulo. Las cuatro veces, el documento existía y traía la respuesta.

**Reescribir sin haber leído produce trabajo que hay que deshacer.** Y lo peor: hace perder lo bueno que el original ya tenía — el plan oficial de la sesión 1 traía las preguntas de apertura y el desarrollo minuto a minuto, que la propuesta nueva no tenía.

### Una duda técnica se resuelve en la fuente, no preguntando

Ante una duda de contenido —cuántas operaciones tiene el ciclo, cómo se llaman los tramos del disparo, qué RMR exige un método— **se busca en un libro o una tesis antes de escribir nada**. No se pregunta al instructor lo que está publicado, y mucho menos se rellena con lo que suena razonable.

> **Caso real.** El esquema del ciclo de minado se dibujó con *ventilación* como una de las cinco operaciones unitarias. La tesis de Ccaso Yucasi (UNAP, §2.6) enumera **perforación, voladura, desatado de rocas sueltas, limpieza y carguío, acarreo y sostenimiento** — la ventilación no está: es servicio auxiliar. Lo que faltaba era el **desatado**, que es precisamente la operación de seguridad del ciclo. Un esquema plausible habría enseñado mal a doce promociones.

**Dónde buscar, en orden:** la bibliografía del propio sílabo · tesis de repositorios peruanos (UNAP, UNSAAC, UNSCH, UNI, ALICIA-Concytec) · normativa vigente (DS 024-2016-EM) · catálogos de fabricante para lo que sea equipo.

**Y la fuente se cita** en `imagenes.csv` o en el `sustento` de la observación, con autor, obra, sección y URL. Un dato sin fuente es un dato que nadie podrá volver a comprobar.

#### Leer la definición, no la enumeración

Ir a la fuente no basta: **una fuente responde la pregunta que ella se hace, no la nuestra.**

> **Segunda parte del mismo caso.** Ya en la tesis, se tomó la lista del §2.6 porque el título decía «Operaciones unitarias del minado» — y se metió el **desatado** en el ciclo. Dos renglones más abajo, la propia tesis lo definía: *"es **la actividad** que consiste en hacer caer las rocas sueltas **antes, durante y después** de las labores"*. Lo que acompaña a todas las etapas no es una de ellas.
>
> Aplicando la **definición** de operación unitaria —etapa que transforma o desplaza el material, con equipo, insumo y producto propios, medible por sí sola— salen las cinco que la base ya tenía: **perforación · voladura · carguío · acarreo · sostenimiento**. Desatado, ventilación y drenaje son **condiciones permanentes de seguridad**, y así se dibujan: rodeando el ciclo, no dentro.

**La prueba:** preguntar *¿qué le hace esta etapa al material?* Si la respuesta es «nada, previene un riesgo», no es operación unitaria — lo cual no la hace menos importante, la pone en otro sitio.

> Y una consecuencia incómoda: **la base original estaba bien**. Dos correcciones seguidas la empeoraron. Cuando lo que hay contradice a la fuente, la primera hipótesis a descartar es que la fuente se esté leyendo mal.

### Lo que no se sabe, se marca

Un punto clave que depende de una fuente que aún no se tiene se escribe con el prefijo **`PENDIENTE (falta fuente X)`**. Redactarlo a ojo es inventar, y una tabla técnica inventada es peor que un hueco visible.

### Quién decide

**El diseñador sugiere; el instructor líder aprueba.** Toda decisión queda en `observaciones.csv` con `decision` y `aprobado_por`. Sin firma, la corrección se vuelve a discutir dentro de tres meses.

## El pipeline numerado

| Plantilla | Nombre | Qué produce |
|---|---|---|
| **001A / B / C** | Triangulación (TP / PI / EFSRT) | Alinea capacidad ↔ indicadores ↔ contenidos ↔ evaluación; sumilla, propósito, materiales, bibliografía |
| **002A / C / D / E** | Sílabo (TP 48h / PI 48h / PI 96h / EFSRT 128) | Documento del estudiante |
| **002G** | Plan de Proyecto Integrador | Solo PI |
| **003A** Distribución | Distribución de capacidades, indicadores y contenidos | Reparte capacidad/indicadores/contenidos **por bloque** |
| **003A** | Diseño instruccional — sesión **sincrónica** de adquisición | Plan de sesión: ruta de 5 momentos con **Actividades · Duración · Materiales** |
| **003B** | Diseño instruccional — sesión **sincrónica** de evaluación de colaborativos | Plan de la sesión de sustentación (3 fases) |
| **003B** lista | Lista de recursos de aprendizaje autónomo | Lo que el estudiante trabaja en el asincrónico |
| **003C** | Diseño instruccional — sesión **dirigida** de adquisición | Igual que 003A pero para modalidad presencial |
| **003C** | **Estructura de casos** | Ficha oficial del caso (ver §06) |
| **003D** | Diseño instruccional — sesión **dirigida** de evaluación | Versión presencial de 003B |
| **004A** | **PPT — Sesión sincrónica de adquisición** | El PPT proyectable (ver §07) |
| **004B** | **PPT — Sesión sincrónica de evaluación** | El PPT de sustentación |
| **005** | Interfaz del curso para el EVA | Cómo se arma el curso en Blackboard |

## Dos claves que esto aclara

1. **El guion con minutaje NO está en el PPT — está en la plantilla 003.** El PPT (004) es solo lo proyectable; el **plan de sesión con actividades, duración y materiales por momento** vive en el documento 003A/003B/003C/003D. Por eso los PPT no tienen notas del orador.

2. **Sincrónica (003A/B) = virtual · Dirigida (003C/D) = presencial.** El diseño de la sesión se hace en la caso que corresponda a la modalidad del ciclo (Ciclo I presencial → dirigida; Ciclo II virtual → sincrónica). El contenido pedagógico (ruta de 5 momentos) es el mismo; cambia el soporte.

## Flujo de trabajo del diseño (cómo encadenan)

```
7A/8A/9A
  → 001 Triangulación            (alinear el curso)
  → 002 Sílabo                   (documento del estudiante)
  → 003A Distribución            (repartir por bloques)
  → 003A/B/C/D Diseño de sesión  (plan de cada sesión: ruta + minutaje)   ← el "guion"
  → 003C Estructura de casos     (los casos del tramo) + rúbricas
  → 003B lista recursos autónomos (el asincrónico)
  → 004A/004B PPT                (la proyección)
  → 005 Interfaz EVA             (montaje en Blackboard)
```

## Implicación para el proyecto

- La **matriz de diseño instruccional** (§04) es el insumo que alimenta 001 y 003A-Distribución.
- La **matriz mejorada** debe garantizar que lo que baja a 003 (diseño de sesión) y 004 (PPT) ya venga alineado al objetivo y con presupuesto de tiempo y densidad — es decir, que las plantillas se puedan llenar bien.
- La capacitación del instructor (contexto de apoyo) se ancla a estas mismas plantillas: enseñar a llenar 001→005 sin caer en los 8 errores.
