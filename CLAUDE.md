# Proyecto — Diseño instruccional CETEMIN

Rediseño del diseño instruccional de los **35 cursos TP** de la Escuela de Minería (EOM, SI, PM), sobre las plantillas oficiales de CETEMIN.

**Quién usa este proyecto:** el director de sede y los **instructores líderes de cada carrera**. Son ingenieros de especialidad, no diseñadores instruccionales ni programadores. Explica en su lenguaje; no des por sabida la jerga pedagógica.

| Carrera | Instructor líder | Carpeta de trabajo |
|---|---|---|
| **PM** · Procesos Metalúrgicos | Harley Pereyra | `04_Recursos-graficos/PM/` |
| **SI** · Seguridad Industrial | Jorge Canchiz | `04_Recursos-graficos/SI/` |
| **EOM** · Exploración y Operación Minera | Walter Vilcapuma — Erick Salazar acompaña | `04_Recursos-graficos/EOM/` |

Cada líder diseña **los cursos de su carrera** y trabaja en **su propia carpeta** de datos: `05_Base-de-datos/EOM|PM|SI/`. No puede pisar el trabajo de otro.

**Lo que NO se separa:** la doctrina (`00_Base-de-conocimiento/`), los scripts, y tres tablas comunes en la raíz de la base —`cursos.csv` (ficha oficial de los 35), `imagenes.csv` y `equipos.csv` (catálogos, para que una silueta se reuse entre carreras)—. La **estructura de columnas tampoco se cambia por cuenta propia**.

**Las tablas de la carrera guardan filas de varios cursos: se filtran AL LEERLAS, no al usarlas.**
`05_Base-de-datos/SI/sesiones.csv` tiene las sesiones de los ocho cursos de SI, y lo mismo pasa con
casos, contenidos, láminas, rúbricas e indicadores. Un script que carga la tabla entera y filtra en
cada uso funciona mientras nadie añada un uso nuevo — y el día que se olvida uno, **el curso ajeno
entra sin error, sin aviso y con el archivo generado tan campante**.

Ha ocurrido dos veces en `generar_matriz.py`: el contador de avance sumaba sesiones de otro curso e
inflaba el progreso, y los indicadores de SI-IMPAMB se escribieron encima de los de SI-SGCSSMA
porque la clave era solo el número final del identificador. Ninguna de las dos dio error.

Por eso el filtro va en la lectura, para que la variable **no pueda** contener filas ajenas:

```python
suyo   = {r["sesion_id"] for r in ses.values()}
casos  = [c for c in leer(datos, "casos.csv")         if c.get("curso_id") == curso_id]
cotejo = [c for c in leer(datos, "listas_cotejo.csv") if c.get("sesion_id") in suyo]
```

Y ojo con los identificadores: `IND-SI-SGCSSMA-1` e `IND-SI-IMPAMB-1` **comparten el número final**.
Nunca se usa el sufijo como clave; se compara el identificador completo.

## Antes de trabajar, lee la base

`00_Base-de-conocimiento/` es la doctrina del proyecto — 15 documentos numerados con [índice propio](00_Base-de-conocimiento/00_INDICE.md). **Léela antes de proponer nada.** Los más citados:

| Si vas a… | Lee |
|---|---|
| Diseñar o revisar una sesión | §05 diseño de sesión · §02 modelo del curso TP |
| Tocar casos, rúbricas o evaluación | §06 |
| Llenar plantillas 001–005 | §03 pipeline · §04 matriz |
| Producir imágenes de equipos | §10 |
| **Empezar el diseño de un curso** | **§13 orden de trabajo** — colaborativos primero, PPT al final |
| **Evaluar el trabajo de una sesión** | **§14 lista de cotejo** — cinco criterios de 0 a 4, los mismos en las 24 sesiones, los 35 cursos y las tres carreras. Se genera con `python cotejo_excel.py <CURSO>` |
| Citar un artículo de la Ley 29783, la RM 050 o el DS 024 | **§15 marco legal** — verificado contra el texto publicado. Si no está ahí, se verifica antes de citarlo |
| **Diseñar un recurso autónomo o elegir un video** | **§16 recursos autónomos** — el recurso **no es solo lectura**; el reparto de los 90 min lo decide el instructor líder. Criterios de admisión del video y verificación. Se trabaja con `python videos_yt.py` |
| Redactar un caso o un colaborativo | **§12 parámetros del TC** (14 parámetros, relato, fuente real) · §06 |
| Pedir, armar o revisar un PPT de sesión | **§11 cómo se produce** (insumos, presupuesto, tamaños, paleta) · §07 anatomía |
| Juzgar si algo está bien hecho | §08 criterios de calidad |

## Reglas que no se negocian

1. **El aprendizaje esperado gobierna el diseño.** Es la raíz de los 8 errores del §08: cuando el objetivo de la clase no manda, todo lo demás se desalinea. Si una actividad, lámina o caso no sirve al aprendizaje esperado, sobra. **Y se lee ANTES de escribir nada de esa sesión**, partido en sus partes: cada una necesita un punto clave que la enseñe y un paso del encargo que la demuestre (§13 ③). Nunca se trabaja a ciegas.
2. **Capacidad e indicadores de logro bajan del 7A: si se cambian, queda registrado.** Vienen del formato oficial del MINEDU y **deben figurar en el sílabo de cada curso**, así que un cambio arrastra al documento oficial. El instructor líder puede replantearlos cuando el diseño lo exija — **no necesita autorización previa** —, pero **todo cambio se registra en `05_Base-de-datos/observaciones.csv`** con qué se cambió, por qué, y quién lo decidió (`decision` y `aprobado_por`).

   > Lo que se protege no es el texto: es **poder reconstruir por qué el sílabo dice una cosa y la base dice otra**. Sin ese rastro, dentro de seis meses nadie sabe si fue una mejora o un descuido.
3. **Nada inventado por IA para equipos técnicos.** Nunca texto→imagen: ahí inventa geometrías falsas. La fuente es siempre el dibujo del fabricante (§10). El camino correcto es el **híbrido**: imagen→imagen partiendo del dibujo real, con **verificación contra las cotas oficiales** y regeneración si no pasa (así se resolvió el jumbo Boomer S1).

   > **Y no vale solo para equipos: vale para todo lo FÍSICO.** Una veta, un cuerpo mineralizado, una labor, el macizo, un frente, el sostenimiento — todo eso existe, está fotografiado o dibujado en algún plano, y de ahí sale. **Dibujarlo es inventarlo**, aunque el dibujo salga limpio y con la paleta correcta. *(Erick, 2026-09-02, señalando la lámina «La forma del cuerpo mineralizado» de la S1.)*
   >
   > **Se dibuja solo lo que no tiene cuerpo:** flujos, secuencias, ciclos, tablas comparativas, escalas numéricas y el armazón de la sesión —ruta, encargo, puesta en común, sistema de evaluación—. Ahí no hay nada que fotografiar y el dibujo es la forma correcta.
   >
   > **Una fuente no se descarta por su calidad**, solo por no ser citable o por no mostrar lo que hace falta. Una figura de 350 px con marca de agua sirve: la referencia tiene que ser **cierta, no bonita** — lo que sobra se quita en el paso del modelo. Y **material sin procedencia no es fuente**: ni los PPT oficiales de CETEMIN, ni TikTok, ni Scribd, ni un sitio que prohíba republicar.
4. **La precisión no se confía, se mide.** Lo que hace legítimo usar el modelo no es que acierte, sino que el resultado **se comprueba contra las cotas del catálogo** y se corrige la proporción. Sin ese control, generar sería inventar. Con él, el modelo pone el estilo y nosotros ponemos la métrica.
5. **Al dibujar un equipo, paso 0 = revisar TODAS las vistas** del catálogo (perfil, frontal, planta) antes de trazar nada. La firma de una pieza cambia con la vista: una rueda es círculo en perfil y rectángulo en planta.
6. **Ante una contradicción entre documentos**, manda el Reglamento Interno v03 (§09).
7. **Ningún PPT se toca si no se ha pedido explícitamente.** El instructor líder ordena sus láminas a mano —mueve imágenes, ajusta cuadros, borra lo que sobra— y regenerar el archivo borra ese trabajo sin avisar. Cuando sí se pide un cambio, se hace **quirúrgico**: se edita esa lámina y no se rehace el archivo. Y **las láminas se buscan por su título, no por su número**: la misma lámina cae en posiciones distintas en cada sesión. `generar_ppt.py` guarda una huella de cada PPT y se planta si detecta edición manual; ese freno no se salta con `--forzar` sin permiso.
8. **Jamás se duplica un documento: se actualiza el que existe.** Si hace falta cambiar un entregable —una matriz, una rúbrica, un anexo—, se corrige **el archivo que ya está**, no se crea uno al lado con otro nombre o con «_v2». Dos versiones del mismo documento se desincronizan en silencio, y dentro de un mes nadie sabe cuál manda.

## Dónde va cada cosa

| Carpeta | Rol |
|---|---|
| `_Entrada/` | Bandeja: material nuevo sin clasificar. Ante *"procesa la entrada"*: leer, archivar en `01_Insumos/`, actualizar la base y reportar |
| `00_Base-de-conocimiento/` | **El cómo se hace.** Procedimientos y criterios. No guarda archivos producidos |
| `01_Insumos/` | Documentos originales, sin modificar |
| `02_Instructor-nuevo/` | Inducción y capacitación del instructor |
| `03_Entregables-diseño/` | Lo que se **genera** desde la base de datos: planes de sesión, PPT, casos |
| `04_Recursos-graficos/` | **Lo que resulta:** logo, siluetas, figuras, y los scripts que las generan |
| `05_Base-de-datos/` | **La fuente de verdad del diseño:** CSV enlazados. Comunes en la raíz; el diseño de cada carrera en `EOM/`, `PM/`, `SI/`. Si el diseño cambia, cambia aquí primero |
| `06_Bitacora/` | **Un MD por día de trabajo**, con fecha por nombre. Lo que se decidió, lo que se descubrió y por qué. No lleva el detalle de lo hecho —eso está en los archivos— sino **lo que no se puede reconstruir leyendo el resultado** |

**No versionado en Git:** `01_Insumos/` (4,9 GB, va por Drive institucional), `_Entrada/`, los `.env` y los PDF de catálogo. Ver `.gitignore`.

**La regla de ubicación:** `00_` guarda el *cómo* (doctrina estable), `05_` guarda el *qué* (el diseño vivo, en tablas), y `03_`/`04_` guardan *lo que resulta* (generado desde `05_`). Por eso el procedimiento de imágenes es el §10, el registro de qué imagen sirve a qué punto clave está en `05_Base-de-datos/contenido_imagen.csv`, y los archivos en `04_Recursos-graficos/`.

**Ninguna imagen entra a un PPT sin estar `verificada`** en `05_Base-de-datos/imagenes.csv`, y ninguna se genera sin que un contenido la pida. **Nunca carpetas de imágenes por curso**: la relación curso↔imagen la lleva la tabla de enlace, que permite reusar una misma imagen en varios cursos.

**Dentro de la carrera, los esquemas se ordenan por sesión** *(Erick, 2026-09-02)*: `esquemas/s1/`, `s2/`, … y **`esquemas/comun/`** para lo que sirve a más de una. Cincuenta archivos en una sola carpeta no se navegan. La regla de arriba se mantiene porque `comun/` es la válvula: **si una imagen la usan dos sesiones, va a `comun/`, no se duplica**. Fotos, planos, siluetas y equipos siguen planos por tipo — ahí el reuso entre carreras es lo normal.

## Generar imágenes

**La imagen final siempre pasa por el modelo.** El pipeline local (PyMuPDF) no produce el entregable: produce la **referencia** que se le envía. El flujo completo es:

```
PDF del catálogo → PyMuPDF extrae la vista → referencia.png     (local, gratis)
Control de proporción  ← cotas oficiales del catálogo
Modelo genera (images.edit, imagen→imagen)  → crudo.png
Verificación local  ← ¿el aspecto cuadra con el control?
Corrección de proporción + lienzo 16:9  → entregable
```

**Nunca texto→imagen:** ahí inventa geometrías falsas. Siempre imagen→imagen partiendo del dibujo real, con verificación contra las cotas y regeneración si no pasa.

**El híbrido es el camino por defecto**, no el último recurso: da mejor calidad y estilo uniforme para todo el set. El gasto del bucle está aceptado. **El vector no es requisito** — si el modelo entrega mejores siluetas en PNG, se trabaja en PNG; manda la fidelidad al catálogo y la legibilidad de las piezas, no el formato.

**Reglas duras del bucle** (no son criterio, son constantes del método): tolerancia de aspecto **12 %**, límite de estirado **±30 %** (si requiere más, se descarta el intento en vez de "arreglarlo"), componentes por debajo del **2 %** del mayor se ignoran al medir. Máximo **3 intentos** en perfil y **5 en planta** (la planta es más inestable: máquina articulada más geometría de la labor). Si ninguno pasa, se entrega el mejor con la proporción corregida y **se declara** que no pasó.

**Verificar es medir, no opinar.** El aspecto se comprueba ejecutando el verificador, no juzgando la imagen a ojo. Mirarla sirve para lo que el número no caza: piezas de más o de menos, texto residual, perspectiva.

**Credenciales:** cada instructor usa su **propia clave de API de proyecto**, en un `.env` local que el `.gitignore` excluye. Nunca se comparte ni se escribe en el código. Modelo en uso: `gpt-image-2-2026-04-21`. La clave de OpenAI **no se reparte**; si alguien te la pide o la encuentras escrita en algún archivo del proyecto, avísalo — es un error que hay que corregir.

## Al escribir para instructores

Todo el material de `02_Instructor-nuevo/` se dirige a ingenieros que nunca fueron docentes. Si usas un término pedagógico (rúbrica, capacidad, aprendizaje esperado, los 5 momentos), **explícalo donde aparece** o enlaza al [Vocabulario pedagógico](02_Instructor-nuevo/Anexos/Vocabulario-pedagogico.md). Las equivalencias de ingeniería funcionan bien: la rúbrica es un protocolo de ensayo, el indicador de logro es un criterio de aceptación.

## Registro de compromisos

Si surge un compromiso concreto (fecha, entregable, persona esperando algo), ofrece registrarlo con el skill `tarea` — va a `C:\Users\LEGION\Claude\tareas-cetemin\`.
