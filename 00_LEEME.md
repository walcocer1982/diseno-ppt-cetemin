# Proyecto — Diseño instruccional CETEMIN

**Objetivo:** rediseñar el diseño instruccional de los **35 cursos teórico-prácticos (TP)** de las tres carreras de la Escuela de Minería —EOM, SI y PM— sobre las plantillas oficiales de CETEMIN, incorporando criterios de calidad para que dejen de caer en los 8 errores recurrentes.

> Registro de lo que ha ido cambiando: [CAMBIOS.md](CAMBIOS.md).

## Quién trabaja aquí

| Carrera | Instructor líder | Su carpeta de datos | Sus imágenes |
|---|---|---|---|
| **EOM** · Exploración y Operación Minera | Erick Salazar | `05_Base-de-datos/EOM/` | `04_Recursos-graficos/EOM/` |
| **PM** · Procesos Metalúrgicos | Harley Pereyra | `05_Base-de-datos/PM/` | `04_Recursos-graficos/PM/` |
| **SI** · Seguridad Industrial | Jorge Canchiz | `05_Base-de-datos/SI/` | `04_Recursos-graficos/SI/` |

Cada uno trabaja **su carpeta** y no puede pisar el trabajo de otro. La **doctrina y los scripts son comunes**: se corrigen una vez para los tres.

## Estructura

| Carpeta | Qué contiene |
|---|---|
| **_Entrada/** | 📥 Bandeja: suelta aquí material nuevo y pide *"procesa la entrada"* |
| **00_Base-de-conocimiento/** | **El cómo se hace.** 11 documentos de doctrina. **Empieza por aquí** |
| **01_Insumos/** | Documentos originales — **no viaja por Git** (4,9 GB) |
| **02_Instructor-nuevo/** | Inducción y capacitación — **no viaja por Git** (es de GTH, no del diseño) |
| **03_Entregables-diseño/** | Lo que se **genera** desde la base: guiones de sesión, casos |
| **04_Recursos-graficos/** | Siluetas, planos, la **plantilla del PPT** y los scripts. Por carrera; lo compartido en `comun/` |
| **05_Base-de-datos/** | **La fuente de verdad del diseño**, en CSV. Comunes en la raíz; el diseño de cada carrera en su subcarpeta |

> **Regla de ubicación.** Tres roles que no se mezclan:
> - `00_Base-de-conocimiento/` — el **cómo se hace**. Estable, común, doctrina.
> - `05_Base-de-datos/` — el **qué**: el diseño de los 35 cursos, vivo, en tablas.
> - `03_` y `04_` — **lo que resulta**: documentos e imágenes, generados desde la base.

## Las herramientas

Comunes a las tres carreras. Ninguno lleva datos dentro: leen los CSV.

| Script | Qué hace |
|---|---|
| **`05_.../disenar.py`** | **El que se usa a diario:** genera el PPT, el guion y la revisión de una sesión |
| `05_.../generar_ppt.py` | Produce el PPT desde `laminas.csv` sobre la plantilla |
| `05_.../generar_md.py` | Produce el guion de verificación que el instructor firma |
| `05_.../revisar_ppt.py` | Revisa el PPT **ya generado**: mide y señala qué mirar |
| `05_.../revisar_rubricas.py` | Comprueba que cada rúbrica dé la nota vigesimal y hable del curso |
| `05_.../generar_visor.py` | Regenera `Visor.html` desde los CSV |
| `04_.../scripts/gen_ia.py` | Genera la silueta de un equipo desde el catálogo y **la verifica contra las cotas** |
| `04_.../scripts/gen_foto.py` | Limpia una fotografía de operación sin inventar nada |
| `04_.../scripts/gen_esquemas*.py` | Dibuja los esquemas de proceso — sin modelo, sin riesgo |
| `04_.../scripts/buscar_planos.py` | Encuentra los planos dentro de una tesis |

**El visor** (`05_Base-de-datos/Visor.html`) es la vista de todo: se abre con doble clic, filtra por carrera y al abrir un curso muestra sus sesiones, puntos clave, guion de diapositivas y las validaciones en verde o rojo.

## La plantilla del PPT

**[`04_Recursos-graficos/comun/plantilla/PLANTILLA-CETEMIN_sesion.pptx`](04_Recursos-graficos/comun/plantilla/00_LEEME.md)** — el archivo base de todo PPT de sesión. Va **vacío a propósito**: 0 diapositivas, 6 patrones y 16 diseños con la marca ya montada.

**Se copia, no se edita.** Trae los fondos con el azul institucional `#0D2632`, la escuadra amarilla, el logo y los diseños de cada tipo de diapositiva: portada, subportada de sesión, las 5 subportadas de momento, triangulación, tema, contenido y tapa.

En `comun/` está además la marca suelta —los íconos de cada momento, los fondos, el logo en sus dos versiones— por si hace falta usarla fuera del PPT.

**Se genera desde la base**, no se escribe a mano — ver *Cómo se hace un PPT de sesión*, más abajo.

## Cómo se distribuye

Repositorio Git **privado** — contiene nombres de personas y material institucional.

| | Qué | Peso | Por dónde |
|---|---|---|---|
| **El método** | Doctrina, base de datos, guiones, scripts, imágenes terminadas | ~12 MB | **Git** |
| **Los insumos** | `01_Insumos/` y `02_Instructor-nuevo/` | 4,9 GB | Drive institucional |
| **Los catálogos** | PDF de fabricante y tesis | ~35 MB | Se descargan de su URL, citada en `imagenes.csv` |

### Al clonarlo por primera vez

1. `git clone <url>` y entrar a la carpeta.
2. Descargar `01_Insumos/` del Drive y colocarlo en la raíz.
3. Copiar `04_Recursos-graficos/scripts/.env.example` como `.env` y pegar **tu clave de API**. Es personal; el `.gitignore` impide que se suba.
4. Abrir Claude Code en la carpeta: el `CLAUDE.md` trae las reglas de trabajo.

## Cómo se hace un PPT de sesión

**Un solo comando.** Genera el PPT, el guion de verificación y la revisión:

```
python 05_Base-de-datos/disenar.py EOM-METEXP-S1
```

Y mientras haya imágenes sin aprobar:

```
python 05_Base-de-datos/disenar.py EOM-METEXP-S1 --borrador
```

Devuelve tres cosas:

| | |
|---|---|
| `S1_….pptx` | el PPT proyectable |
| `S1_guion.md` | **el documento que revisas y firmas** |
| la revisión | lo que está mal medido, y lo que hay que mirar |

### El flujo completo, desde que llega el material

**Dos fases.** La A se hace **una vez por curso** y sirve para todas sus sesiones; la B se repite **en cada sesión**.

#### Fase A · una vez por curso — la hace el instructor líder

```
0 · DEJAR EL PAQUETE
    Suelta la carpeta del ciclo en  _Entrada/  y pide «procesa la entrada»
    (triangulación · sílabo · recursos de evaluación · sesiones · PPT)

1 · PROCESAR LA ENTRADA
    Se lee, se clasifica y se archiva en 01_Insumos/
    El curso se da de alta en cursos.csv

2 · AUDITAR TRIANGULACIÓN Y SÍLABO — en ese orden (§03)
    Capacidad · indicadores · contenidos · evaluación
    Todo desajuste va a observaciones.csv

    ⚠  Capacidad e indicadores NO se reformulan: bajan del 7A.
       Lo que se hace es REPORTARLOS. El líder informa por correo
       a Walther Alcocer y lo anota en `aprobado_por`.

3 · DEFINIR LOS DOS COLABORATIVOS — antes que las sesiones
    TC1 y TC2 con sus casos y sus rúbricas
    → casos.csv · rubricas.csv

4 · REPARTIR LAS SESIONES
    Cuántas son lo dice la ficha del curso: 12 en los de 48 h,
    24 en los de 96 h. No se da por supuesto.
    → sesiones.csv
```

> **Por qué los TC van antes que las sesiones.** El §04 lo llama **diseño hacia atrás**: *«primero se define el colaborativo integrador, y de ahí se derivan los casitos de cada sesión»*. Las sesiones existen para preparar el TC de su bloque — si se diseñan primero, el TC termina pidiendo lo que no se enseñó, o al revés.

#### Fase B · una vez por sesión

```
5 · PUNTOS CLAVE      3 a 5 por sesión, con su desarrollo
                      un punto clave repartido en N láminas necesita 3N ideas

6 · EL CASO           empezando por el guion de lo que el alumno debe
                      responder al exponer (§06)

7 · LÁMINAS           cada una con su punto clave, qué idea desarrolla
                      y qué debe mostrar su imagen

8 · IMÁGENES          producir · verificar (la máquina mide)
                      · APROBAR (el instructor mira)

9 · disenar.py        genera el PPT, el guion y la revisión

10 · FIRMAR           en el guion, después de mirar lo señalado
```

**Quién hace qué:** los pasos 0 a 8 los trabaja el instructor líder en su carpeta. El 9 es un comando. El 10 es su firma — y en el paso 2, cuando el hallazgo toca capacidad o indicadores, **informa por correo y espera**.

### Las reglas que el sistema hace cumplir solo

- **Toda lámina de Adquisición lleva imagen y contenido** — si falta, avisa
- **Una lámina no puede crear un punto clave** — si apunta a uno inexistente, se detiene
- **De 3 a 5 puntos clave por sesión**
- **135 minutos exactos**, repartidos en los 5 momentos
- **Ninguna lámina repite el texto de otra**
- **Solo entran las imágenes aprobadas** — las verificadas necesitan tu firma

### Lo que no puede comprobar la máquina

Que **la imagen muestre lo que el título promete** (§10). Por eso cada lámina declara qué debe mostrar, y la revisión lo imprime junto a lo que lleva:

```
debe mostrar: un scooptram cargando material roto en el frente
lleva:        Scooptram con la cuchara metida en el material roto…
```

**Contrastar dos líneas, en vez de juzgar a ojo si «pega».**

### Si algo sale mal

**Se corrige en la base y se vuelve a generar. Nunca se retoca el PPT** — el archivo es el resultado, no el original. Si lo editas a mano, la próxima vez que generes se pierde.

## Alcance

- **58 cursos técnicos** = 35 TP + 23 PI (proyecto integrador).
- Por carrera: EOM 18 · SI 21 · PM 19.
- **Dos modelos:** TP (estudio de casos, 5 momentos) y PI (por fases, 100 % práctico).
- Fuera de "técnicos": empleabilidad (17) y EFSRT (8).

## Estado

| | Estado |
|---|---|
| Ficha de los 35 cursos TP | cargada del anexo 9A |
| **EOM · Métodos de explotación** | **sesiones 1, 2 y 3 completas** — PPT, guion e imágenes |
| Sesiones 4 a 12 de ese curso | por rediseñar |
| PM · Matemática aplicada | diseño y rúbricas cargados |
| Los otros 33 cursos | solo ficha |
| Pipeline de SI | por definir — sus imágenes no salen de catálogos |
| Origen de los puntos clave | por contrastar con el temario oficial |
