# Base de datos — diseño instruccional

**La fuente de verdad del diseño.** La matriz de diseño instruccional de las tres carreras, en modelo **relacional**: una tabla por entidad, enlazadas por **ID**, en CSV.

De aquí se **genera** todo lo demás —planes de sesión, PPT, vistas para NotebookLM—; nada de eso se escribe a mano por separado. Si algo del diseño cambia, cambia aquí.

### Cómo está repartida

**Los datos de diseño van por carrera; lo común, en la raíz.** Así cada instructor líder trabaja su carpeta sin poder pisar a los otros, y la doctrina y los scripts siguen siendo únicos.

```
05_Base-de-datos/
├── cursos.csv        ← COMÚN · la ficha oficial de los 35 (anexo 9A)
├── imagenes.csv      ← COMÚN · el catálogo, para que una silueta se reuse
├── equipos.csv       ← COMÚN · qué equipo se dibuja y con qué control
├── EOM/   ← Erick Salazar
├── PM/    ← Harley Pereyra
└── SI/    ← Jorge Canchiz
        capacidades · indicadores · sesiones · contenidos · casos
        evaluaciones · bloques · rubricas · laminas · observaciones
        contenido_imagen · valoraciones · actividades · curso_detalle
```

**Por qué `imagenes.csv` es común:** si Erick produce el jumbo, Harley puede usarlo sin duplicar el archivo. La relación con el curso la lleva `contenido_imagen.csv`, que sí es de cada uno.

**Los IDs llevan prefijo de carrera** (`EOM-METEXP-S1`), así que nunca colisionan al juntarlas.

El visor lee las tres carpetas y da la vista de los 35 cursos; el filtro de carrera muestra solo la que interese.

## Las tablas y cómo se enlazan

```
cursos (curso_id)
  ├── capacidades (capacidad_id, curso_id)
  │      └── indicadores (indicador_id, capacidad_id)
  ├── sesiones (sesion_id, curso_id, bloque)
  │      └── contenidos (contenido_id, sesion_id, indicador_id)   ← enlaza contenido con el indicador que desarrolla
  │             └── contenido_imagen (contenido_id, imagen_id)    ← qué imagen ilustra ese punto clave
  ├── casos (caso_id, curso_id, bloque, indicador_id)
  └── evaluaciones (evaluacion_id, curso_id)

imagenes (imagen_id)        ← catálogo propio, independiente del curso
```

| Tabla | Una fila = | Clave propia | Enlaza con |
|---|---|---|---|
| `cursos.csv` | un curso | `curso_id` | — |
| `capacidades.csv` | una capacidad | `capacidad_id` | `curso_id` |
| `indicadores.csv` | un indicador de logro | `indicador_id` | `capacidad_id` |
| `sesiones.csv` | una sesión | `sesion_id` | `curso_id` |
| `contenidos.csv` | un contenido / punto clave | `contenido_id` | `sesion_id`, `indicador_id` |
| `casos.csv` | un caso | `caso_id` | `curso_id`, `indicador_id` |
| `evaluaciones.csv` | un evento calificado | `evaluacion_id` | `curso_id` |
| `imagenes.csv` | una imagen | `imagen_id` | — |
| `contenido_imagen.csv` | un uso de una imagen | `enlace_id` | `contenido_id`, `imagen_id` |

## Las imágenes: por qué cuelgan del contenido y no del curso

`contenido_imagen.csv` es una tabla de enlace **muchos a muchos**: un contenido puede necesitar varias imágenes, y una imagen puede usarse en muchos cursos. Eso responde en los dos sentidos:

- *¿Qué imágenes necesita este curso?* → por sus sesiones y contenidos.
- *¿Qué cursos usan el jumbo Boomer S1?* → todos de un vistazo; si se regenera, se sabe qué se ve afectado.

**Se engancha al contenido, no al curso**, por la misma razón que `contenido → indicador`: obliga a que cada imagen sirva a un punto clave, y ese punto clave a un indicador. Una imagen que no cuelga de ningún contenido es una imagen que sobra — la regla número uno del proyecto, aplicada a lo gráfico.

Los **archivos** viven en `04_Recursos-graficos/`, en carpetas planas por tipo. La relación vive aquí. Nunca se organizan carpetas de imágenes por curso.

### Columnas de `imagenes.csv` que no son obvias

| Columna | Para qué |
|---|---|
| `aspecto_control` | El número que sale de las cotas oficiales (3,90 para el jumbo en perfil). Permite reverificar la imagen sin volver a buscar el catálogo |
| `origen_control` | De dónde salió ese número: cotas oficiales, o la silueta de perfil ya verificada (en planta no hay cotas útiles) |
| `vista` | perfil / planta / frontal. Son imágenes distintas, no variantes: la firma de una pieza cambia con la vista (§10) |
| `tipo` | `figura-fabricante` (con marca y cotas, citada) o `silueta` (elaboración propia). El §10 los trata como entregables distintos |
| `estado` | `pendiente` / `verificada`. **Ninguna imagen entra a un PPT sin estar verificada** |
| `fuente` | La cita obligatoria del fabricante. Con esto la lámina de fuentes del PPT se genera sola |

## Por qué esto sirve: valida la alineación (anti-8-errores)

Con los datos así, revisar la calidad deja de ser "a ojo" y pasa a ser una consulta. Validaciones ya corridas sobre Matemática (todas **OK**):

1. La suma de pesos de evaluación del curso da **100 %**.
2. Toda sesión de adquisición tiene **aprendizaje_esperado** (evita error #2).
3. Todo **contenido apunta a un indicador** válido (evita error #3: puntos clave desalineados).
4. Cada indicador cuelga de una capacidad válida (trazabilidad al 7A).
5. Cada **bloque tiene su caso** (evita error #6).
6. Cada indicador se trabaja en algún contenido (cobertura completa).

Con las imágenes en el modelo se suman dos que antes no se podían comprobar:

7. **Ninguna imagen sin verificar está enlazada a un contenido** — el error caro, porque llega a clase.
8. **Ninguna imagen huérfana**: si no cuelga de ningún contenido, se generó sin que un punto clave la pidiera.

El vínculo clave es `contenido → indicador`: es lo que **obliga** a que cada tema de clase sirva a un indicador, y cada indicador a la capacidad. Esa es la raíz de los 8 errores atacada por diseño.

## Cómo usarlo

- **Fuente de verdad:** estas tablas. Los documentos en prosa, PPT o vistas para **NotebookLM** se **generan** a partir de aquí (NotebookLM no une tablas: se le entrega una vista redactada por curso).
- **Trabajo en equipo:** cada instructor líder edita **las filas de su carrera**. Como los CSV se versionan en Git y las filas son disjuntas, no hay conflictos. La estructura de columnas, en cambio, no se cambia por cuenta propia: es común a los tres.
- **Escalar:** mismo patrón para las tres carreras, con el prefijo de carrera en los IDs.

### Cuidado al editar en Excel

Los CSV llevan acentos en casi todas las filas ("Diseño", "Metalúrgicos", "Perforación") y campos largos con comas. Excel los maltrata de tres formas:

1. **Cambia la codificación** al guardar y las tildes se corrompen. Hay que guardar como *CSV UTF-8*.
2. **Reescribe el archivo entero**, así que el `git diff` deja de mostrar "cambió la sesión 7" y muestra "cambió todo".
3. Convierte a fecha cualquier cosa que se le parezca.

Por eso lo recomendable es **pedirle a Claude que escriba los CSV y revisar el resultado**, en vez de editarlos a mano en Excel. Si igual los abres en Excel, verifica las tildes antes de guardar.

## Visor HTML

`Visor.html` — doble clic para abrirlo en el navegador (sin instalar nada). Se genera desde los CSV.
- **Filtro por carrera** (Todas / EOM / SI / PM) en la barra lateral; los cursos se agrupan por módulo.
- Al elegir un curso arma su vista (capacidad → indicadores → contenidos, sesiones, casos, evaluación) y corre las validaciones en vivo.

## Regla de fuente de verdad

La **estructura** (cursos, horas, tipo, nombres) viene de los **anexos oficiales 9A** — son la fuente correcta, siempre. Las matrices de diseño pueden tener errores y NO priman: solo aportan el **contenido de diseño** (capacidad, indicadores, contenidos, tareas). Ej.: la matriz EOM 2024 pone "Métodos de explotación" en 32 h, pero el anexo dice 48 h → se usa 48 h.

## Bloques (definición clave)

Un **bloque = el tramo de sesiones que culmina en un trabajo colaborativo**. Siempre hay **2 bloques** por curso TP (uno por colaborativo), sin importar las horas:
- **Bloque 1** → sesiones antes del **TC1** → cierra con TC1.
- **Bloque 2** → sesiones antes del **TC2** → cierra con TC2.
Lo que cambia con las horas es cuántas sesiones tiene cada bloque (48 h → ~6; 96 h → ~12), NO el número de bloques. Por eso `nro_bloques = 2` para todos. (Las divisiones temáticas de la matriz —2 o 4— NO son estos bloques; se ignoran.)

## Tablas nuevas (esquema extendido)

- `bloques.csv` — **2 por curso**: `bloque_id, curso_id, numero, colaborativo (TC1/TC2)`. Es la pieza central: sesiones, casos y colaborativos se enganchan aquí.
- `actividades.csv` — tareas del curso: `actividad_id, curso_id, tipo (individual/grupal), titulo, objetivo, descripcion`.
- `contenidos.csv` — se agregó columna `recursos`.
- `cursos.csv` — se agregaron `prerequisito` y `perfil_docente`; `nro_bloques` = 2 para todos.
- `sesiones.csv` y `casos.csv` — ahora enlazan por `bloque_id` (antes número suelto).
- `evaluaciones.csv` — se agregó `bloque_id` (CV1/EP/TC1 → Bloque 1; CV2/EF/TC2 → Bloque 2).
- `observaciones.csv` — **la evidencia**: `observacion_id, curso_id, entidad, ref_id, tipo (error/mejora/observacion), estado (detectado/corregido), descripcion, sustento`. Aquí se registran los errores/observaciones detectados al revisar cada curso, y su corrección (con sustento).

## Estado de EOM · Métodos de explotación

Cargado con el **diseño OFICIAL** del paquete del curso (triangulación + colaborativos), no la matriz: capacidad + 3 indicadores + 2 casos (TC1/TC2) + 6 evaluaciones. **8 observaciones registradas y corregidas** en `EOM/observaciones.csv` — las tres de mayor peso:

- ✅ error: la rúbrica del TC2 era de otro curso (decía *Mineralogía y Petrología* y evaluaba inglés) → rehecha.
- ✅ error: el TC2 citaba un indicador inexistente → reasignado a IND-1, con sustento.
- ✅ error: el Bloque 2 completo enseñaba perforación cuando el indicador pedía otra cosa.

> **Los pesos iguales NO son un defecto.** Los cinco criterios valen lo mismo por diseño: es lo que hace que la rúbrica dé la nota vigesimal (5 × 4 = 20). Si alguien "corrige" eso ponderando criterios, rompe la escala.

## Estado

- ✅ **35 cursos TP** con ficha (estructura del anexo 9A): EOM 11 · SI 12 · PM 12.
- ✅ **Detallados** (marcados con ✓ verde en el visor): **PM · Matemática aplicada** y **EOM · Métodos de explotación**.
- ⏳ Los otros 33 cursos — solo ficha; falta detallar desde su matriz (verificando contra el anexo).
- ⏳ Falta (si se decide): tablas `bloques`, `rubricas`, `momentos_sesion`.
