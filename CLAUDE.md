# Proyecto — Diseño instruccional CETEMIN

Rediseño del diseño instruccional de los **35 cursos TP** de la Escuela de Minería (EOM, SI, PM), sobre las plantillas oficiales de CETEMIN.

**Quién usa este proyecto:** el director de sede y los **instructores líderes de cada carrera**. Son ingenieros de especialidad, no diseñadores instruccionales ni programadores. Explica en su lenguaje; no des por sabida la jerga pedagógica.

| Carrera | Instructor líder | Carpeta de trabajo |
|---|---|---|
| **PM** · Procesos Metalúrgicos | Harley Pereyra | `04_Recursos-graficos/PM/` |
| **SI** · Seguridad Industrial | Jorge Canchiz | `04_Recursos-graficos/SI/` |
| **EOM** · Exploración y Operación Minera | Erick Salazar | `04_Recursos-graficos/EOM/` |

Cada líder diseña **los cursos de su carrera** y trabaja en **su propia carpeta** de datos: `05_Base-de-datos/EOM|PM|SI/`. No puede pisar el trabajo de otro.

**Lo que NO se separa:** la doctrina (`00_Base-de-conocimiento/`), los scripts, y tres tablas comunes en la raíz de la base —`cursos.csv` (ficha oficial de los 35), `imagenes.csv` y `equipos.csv` (catálogos, para que una silueta se reuse entre carreras)—. La **estructura de columnas tampoco se cambia por cuenta propia**.

## Antes de trabajar, lee la base

`00_Base-de-conocimiento/` es la doctrina del proyecto — 10 documentos numerados con [índice propio](00_Base-de-conocimiento/00_INDICE.md). **Léela antes de proponer nada.** Los más citados:

| Si vas a… | Lee |
|---|---|
| Diseñar o revisar una sesión | §05 diseño de sesión · §02 modelo del curso TP |
| Tocar casos, rúbricas o evaluación | §06 |
| Llenar plantillas 001–005 | §03 pipeline · §04 matriz |
| Producir imágenes de equipos | §10 |
| Pedir, armar o revisar un PPT de sesión | **§11 cómo se produce** (insumos, presupuesto, tamaños, paleta) · §07 anatomía |
| Juzgar si algo está bien hecho | §08 criterios de calidad |

## Reglas que no se negocian

1. **El aprendizaje esperado gobierna el diseño.** Es la raíz de los 8 errores del §08: cuando el objetivo de la clase no manda, todo lo demás se desalinea. Si una actividad, lámina o caso no sirve al aprendizaje esperado, sobra.
2. **Capacidad e indicadores de logro no se reformulan.** Bajan del formato oficial 7A del MINEDU y **deben figurar en el sílabo de cada curso**. Reformularlos es excepcional: solo ante un error grave y **con aprobación previa de Walther Alcocer**, director de la sede ABQ. Lo que sí se hace siempre es **reportar** el error detectado (ver `05_Base-de-datos/observaciones.csv`).
3. **Nada inventado por IA para equipos técnicos.** Nunca texto→imagen: ahí inventa geometrías falsas. La fuente es siempre el dibujo del fabricante (§10). El camino correcto es el **híbrido**: imagen→imagen partiendo del dibujo real, con **verificación contra las cotas oficiales** y regeneración si no pasa (así se resolvió el jumbo Boomer S1).
4. **La precisión no se confía, se mide.** Lo que hace legítimo usar el modelo no es que acierte, sino que el resultado **se comprueba contra las cotas del catálogo** y se corrige la proporción. Sin ese control, generar sería inventar. Con él, el modelo pone el estilo y nosotros ponemos la métrica.
5. **Al dibujar un equipo, paso 0 = revisar TODAS las vistas** del catálogo (perfil, frontal, planta) antes de trazar nada. La firma de una pieza cambia con la vista: una rueda es círculo en perfil y rectángulo en planta.
6. **Ante una contradicción entre documentos**, manda el Reglamento Interno v03 (§09).

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

**No versionado en Git:** `01_Insumos/` (4,9 GB, va por Drive institucional), `_Entrada/`, los `.env` y los PDF de catálogo. Ver `.gitignore`.

**La regla de ubicación:** `00_` guarda el *cómo* (doctrina estable), `05_` guarda el *qué* (el diseño vivo, en tablas), y `03_`/`04_` guardan *lo que resulta* (generado desde `05_`). Por eso el procedimiento de imágenes es el §10, el registro de qué imagen sirve a qué punto clave está en `05_Base-de-datos/contenido_imagen.csv`, y los archivos en `04_Recursos-graficos/`.

**Ninguna imagen entra a un PPT sin estar `verificada`** en `05_Base-de-datos/imagenes.csv`, y ninguna se genera sin que un contenido la pida. Los archivos van en carpetas planas por tipo — **nunca carpetas de imágenes por curso**: la relación curso↔imagen la lleva la tabla de enlace, que permite reusar una misma imagen en varios cursos.

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
