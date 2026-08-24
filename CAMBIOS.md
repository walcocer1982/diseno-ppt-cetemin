# Registro de cambios

Qué se movió, qué se decidió y **por qué**. Lo más reciente arriba.

> Se anota aquí lo que cambia la **estructura del proyecto o una regla de trabajo** — no cada edición de contenido. Si alguien vuelve dentro de tres meses y no entiende por qué algo está donde está, la respuesta debería estar en esta página.

---

## 2026-08-12 · La rúbrica es la nota, y limpieza de archivos

### `rubricas.csv` gana `indicador_id` y `puntos_max`

**La rúbrica no acompaña a la nota: la rúbrica ES la nota.** 5 criterios × 4 puntos = 20; el mínimo es 5 × 1 = 5. De ahí sale una regla que parecía estética y no lo es: **los criterios tienen que ser exactamente cinco**. Con cuatro la nota máxima sería 16 y con seis, 24.

**No se añadió columna `peso`** — no existe ponderación. Los cinco criterios valen lo mismo por diseño, y eso es precisamente lo que hace que la suma dé 20. `revisar_rubricas.py` ahora comprueba ese total y avisa de los criterios sin `indicador_id`.

> **Corrección al registro:** el `00_LEEME.md` de la base marcaba *"rúbrica del TC1 con pesos iguales"* como mejora pendiente. **No es un defecto.** Quedó anotado al revés, y quien lo hubiera "corregido" ponderando criterios habría roto la escala vigesimal.

### Los 5 criterios son los mismos en los 70 TC

Salió de mirar las **rúbricas oficiales de PM · Matemática aplicada**: sus criterios **4 y 5 son idénticos palabra por palabra entre el caso 1 y el caso 2**. Son los fijos. Los tres primeros cambian de nombre pero no de función — siguen el recorrido **entender → resolver → interpretar**.

| # | Posición | |
|---|---|---|
| 1 | Comprensión del problema | la nombra el caso |
| 2 | Desarrollo técnico | la nombra el caso |
| 3 | Conclusiones y análisis | la nombra el caso |
| 4 | `Presentación PPT: contenido y diseño` | 🔒 literal |
| 5 | `Presentación oral: dominio y claridad` | 🔒 literal |

**El instructor no elige los criterios: elige qué escribe en cada uno.** `revisar_rubricas.py` ya lo comprueba.

**Los criterios 4 y 5 miden contenido, no oratoria.** Son 8 de 20 puntos —el 40 % de la nota—: se conserva el título oficial, pero el PPT debe **mostrar el procedimiento** (no ser *"visualmente atractivo"*) y la oral debe **responder preguntas técnicas** (no ser *"fluida"*). Un curso técnico que gasta 8 puntos en presentación premia al equipo con buen PowerPoint por encima del que entendió el proceso.

**La nota es del equipo.** El descriptor menciona integrantes porque la conducta individual es la evidencia, pero de ahí sale una sola nota. El criterio 5 pregunta si *cualquier integrante puede explicar cualquier parte* — no si todos hablaron.

### La rúbrica no puede pedir más de lo que el egresado será

Formamos **técnico operativo NV2**, y la rúbrica del TC2 de EOM calificaba en NV3: pedía *"Recomendación sustentada"* y *"analiza los trade-offs"*. Los verbos del curso son **identificar, describir y explicar** — ninguno dice recomendar.

**No se corrige bajando el verbo, se corrige acotando el objeto.** El operador sí analiza: verifica si el método corresponde, identifica el control que le toca, detecta la desviación y la reporta. Lo que no hace es decidir el método.

> Es la segunda vez en el mismo curso (`OBS-6` y `OBS-9`), y la segunda pasó porque al reorientar el caso **la rúbrica se quedó arriba**. Si se toca un TC, su rúbrica se revisa en el mismo movimiento.

### Cargado PM y hallazgos

`PM/rubricas.csv` estaba vacío; ahora tiene los dos casos de Matemática con el texto oficial. Al enlazarlos aparecieron tres cosas (`OBS-PM-MAT-1/2/3`): los **tres indicadores están sin descripción**, **`IND-MAT-3` no se evalúa en ningún colaborativo** (0 de 40 puntos) y las **12 sesiones repiten el mismo aprendizaje esperado**.

### Ordenado lo que sobraba

| Qué | Por qué |
|---|---|
| **Dos carpetas del mismo curso** (`EOM-Métodos-de-explotación` y `EOM-Metodos-…`) | Windows y Git no codifican la tilde igual. `generar_ppt.py` ahora normaliza el nombre: una sola carpeta |
| **3 PPT de ejemplo** (12 MB) | Iteraciones superadas. Queda el que **sale de la base** |
| `02_Sesion-01_guion-de-diapositivas.md` | Decía 31 diapositivas cuando la base dice 20: un documento que miente estorba más que ayuda. Lo sustituye el visor |
| **5 generadores vectoriales** sueltos en `equipos/` | Método descartado (§10: el camino es el híbrido) |

Nada se borró: todo está en `04_Recursos-graficos/_descartado/`, para revisar antes de eliminar.

---

## 2026-08-12 · La plantilla del PPT

Ya existe el molde: **`04_Recursos-graficos/comun/plantilla/PLANTILLA-CETEMIN_sesion.pptx`**, vacío y con la marca montada. Se copia, no se edita.

**El color se unificó al `#0D2632`** de la tapa institucional —azul petróleo, más verdoso que el `#082848` de los PPT antiguos—. Se recolorearon las imágenes de fondo de los patrones **conservando la luminosidad de cada píxel**, para no aplanar sombras ni relieve del logo; solo se tocó el azul oscuro, y el amarillo y el blanco quedaron intactos. Como el cambio va en el patrón, afecta a todas las diapositivas de una vez.

**Se identificó un tipo que faltaba: el `tema`** (diseño «TITLE»), que abre cada punto clave con un panel oscuro y una imagen. Es la respuesta estructural a la fragmentación medida en EOM: en vez de repetir el mismo título en tres diapositivas, se abre el tema con una y se desarrolla.

**Marca extraída a `comun/`:** los íconos de las 5 subportadas, los fondos de portada, contenido y tapa, y el logo en versión azul y blanca.

**Ejemplo:** la sesión 1 en **16 diapositivas** contra las 40 del PPT actual.

Tres cosas aprendidas produciendo esto:
- Al vaciar un PPTX hay que **soltar la relación** de cada diapositiva, no solo quitarla de la lista: si no, las viejas se quedan dentro y el archivo pasa de 2 a 41 MB.
- Hay que **borrar los placeholders heredados** del diseño, o sale *"Haga clic para agregar título"* encima de la diapositiva.
- **El mapa de diseños cambia entre plantillas**: en una, `slideLayout8` son las subportadas; en otra, la tapa. No se puede dar por fijo.

---

## 2026-08-10 · Separación por carrera y limpieza para Git

### Cada líder trabaja su propia carpeta

Los datos de diseño se repartieron por carrera; **la doctrina y los scripts siguen siendo únicos**.

```
05_Base-de-datos/
├── cursos.csv · imagenes.csv · equipos.csv   ← COMUNES
├── EOM/  ← Erick Salazar        14 tablas
├── PM/   ← Harley Pereyra       14 tablas
└── SI/   ← Jorge Canchiz        14 tablas
```

**Por qué no se separó todo:** duplicar la doctrina significaría mantener 11 documentos y 5 scripts por triplicado. Solo en la sesión del 10 de agosto se hicieron **7 bloques de cambios** sobre esos archivos — habrían sido 21 ediciones, y a la tercera alguien se olvida y las tres versiones divergen.

**Por qué `imagenes.csv` y `equipos.csv` quedan comunes:** para que una silueta producida por una carrera la pueda usar otra sin duplicar el archivo.

### El catálogo de equipos salió del código

`gen_ia.py` tenía los equipos escritos dentro, así que había que editar el script cada vez que se daba de alta uno. Ahora viven en `05_Base-de-datos/equipos.csv`: **dar de alta un equipo es agregar una fila**, no tocar código.

### Qué dejó de estar versionado

| Ya no va a Git | Por qué |
|---|---|
| `02_Instructor-nuevo/` | Es del proceso de GTH (inducción al puesto), no del diseño instruccional |
| PDF de catálogos y tesis (~35 MB) | Material de terceros; están citados con su URL en `imagenes.csv` |
| `01_Insumos/` | 4,9 GB, con archivos de hasta 1,6 GB |

El repositorio quedó en **71 archivos, 12,5 MB**.

### Qué se eliminó

- **6 MB de duplicados**: al promover una imagen a la vitrina se copiaba en vez de moverse. Regla nueva: *el taller guarda el proceso, la vitrina el entregable — no ambos*.
- **El servicio de imágenes** (proxy + servidor MCP, 15 archivos): se descartó al optar por **una clave de API por instructor**. Se conservó solo el registro del porqué.
- **El logo y sus 11 scripts**: era una prueba, no parte del proyecto.
- **Horario 2025-III y perfiles de instructor**: contexto ya destilado en la base; anotado en el §09.
- **El proyecto `Imagenes-ppt`**: su contenido se incorporó al proyecto.

---

## 2026-08-10 · El diseño llega hasta la diapositiva

### Tablas nuevas

| Tabla | Qué registra |
|---|---|
| `laminas.csv` | El guion del PPT: momento, minutos, diapositivas e imagen de cada bloque |
| `imagenes.csv` | El catálogo de imágenes con su control de aspecto, su fuente y si está verificada |
| `contenido_imagen.csv` | Qué imagen ilustra qué punto clave (muchos a muchos) |
| `equipos.csv` | Qué equipo se dibuja, de qué vista y contra qué cota se verifica |

**Las imágenes cuelgan del contenido, no del curso.** Así una imagen que no sirve a ningún punto clave queda a la vista como imagen que sobra.

### El visor se regenera

`Visor.html` tenía los datos embebidos y se desactualizaba en silencio. Ahora se produce con `python generar_visor.py` y siempre refleja los CSV. Tres niveles: cursos → curso → sesión con su guion de diapositivas.

### Validaciones nuevas

A las seis que ya existían se sumaron: que cada sesión sume **135 minutos**, que ninguna pase de **34 diapositivas**, que la teoría no pase de **13**, y que ninguna lámina use una imagen sin verificar.

---

## 2026-08-10 · Doctrina

### §05 · Rutinas de pensamiento y su costo en minutos

La base exigía *"una rutina de pensamiento por momento"* pero no decía cuáles. Se añadió el repertorio de Project Zero (Harvard) mapeado a los 5 momentos, **con el tiempo que cuesta cada una**.

**La regla que faltaba:** la rutina **no se suma** al momento, **lo estructura**. Sumarla es lo que hace que la sesión no cierre en 135 minutos.

Y una consecuencia medida: **no cabe una rutina completa por momento** — serían 69 minutos. Lo que cabe es una rutina fuerte, una de cierre corta, y las de coste cero intercaladas.

### §07 · El formato del PPT, al detalle

Verificado abriendo los PPT oficiales de PM y EOM:

- **Las 5 subportadas de momento llevan UNA SOLA PALABRA** y su ícono. Nada más. No se redactan: se insertan.
- **La diapositiva de triangulación** tiene 3 zonas fijas (aprendizaje · puntos clave · evaluación). Es densa **por diseño** y no cuenta como muro de texto; lo que se revisa es el contenido de cada zona.
- Conviven **dos generaciones del formato**: PM no tiene "ruta de aprendizaje" y EOM sí. Decisión pendiente.

### §10 · De dónde sale el equipo

Se añadió el procedimiento de fuentes: **primero la tesis, después el catálogo**. Buscar en repositorios peruanos qué modelo se usa de verdad, y recién entonces ir al fabricante.

**La imagen es tan buena como la fuente:** con una hoja comercial sale un contorno plano; con un corte seccionado salen las partes internas. Si la lámina debe enseñar partes, hay que conseguir un corte.

---

## 2026-08-10 · Método de generación de imágenes

**El camino por defecto es el híbrido**, no la geometría: el modelo genera desde la referencia real del catálogo y el resultado **se verifica contra las cotas**. El vector dejó de ser requisito.

**Los aprendizajes del prompt están en [`04_Recursos-graficos/scripts/PROMPT.md`](04_Recursos-graficos/scripts/PROMPT.md)**, con lo que funcionó y lo que no. Antes de quitar una línea del prompt, buscarla ahí: casi todas están porque algo falló sin ellas.

**Herramienta nueva:** `buscar_planos.py` encuentra los planos dentro de una tesis descartando fotos, tablas y reportes. De 33 figuras deja 8 para revisar.

---

## Decisiones tomadas (y por qué)

| Decisión | Razón |
|---|---|
| **Una clave de API por instructor**, no un servicio central | Sin infraestructura que mantener; límite de gasto en el panel de OpenAI; y elimina el tope de 4,5 MB que estorbaba |
| **Doctrina y scripts comunes**, datos por carrera | Mantener 11 documentos por triplicado los hace divergir |
| **El prompt corto gana** | Medido tres veces: con menos instrucciones el modelo se ciñe más al dibujo |
| **Para planos con texto, la IA no cierra el trabajo** | Reescribe los glifos: cambió `NV-4675` por `NV-4670` pese a pedirle copia fiel |
| **Capacidad e indicadores no se reformulan** | Bajan del 7A. Excepción: error grave **con aprobación de Walther Alcocer** |
