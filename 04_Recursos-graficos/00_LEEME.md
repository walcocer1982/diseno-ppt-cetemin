# 04 — Recursos gráficos

**Qué es esta carpeta:** los **archivos gráficos producidos** del proyecto — logo, siluetas de equipos, figuras de fabricante — y los scripts que los generan.

**La regla que la separa de la base de conocimiento:**

| | Dónde |
|---|---|
| **Cómo se hace** (procedimiento, criterios, reglas de estilo) | [00_Base-de-conocimiento/10_imagenes-y-siluetas-de-equipos.md](../00_Base-de-conocimiento/10_imagenes-y-siluetas-de-equipos.md) |
| **Lo que resulta** (los archivos) | aquí |

Antes de producir cualquier imagen de equipo, se lee el §10. Recuerda su regla base: **nada inventado por IA para equipos técnicos**; la fuente es el dibujo del fabricante, y el paso 0 es revisar todas sus vistas (perfil, frontal, planta).

## Estructura

Hay dos zonas, y la diferencia importa: **el taller** (donde se trabaja, por equipo) y **la vitrina** (los entregables, en carpetas planas).

**Se organiza por carrera.** La carpeta dice **quién la produjo**, no quién puede usarla: si otra carrera necesita una imagen, la usa desde donde está — la relación curso↔imagen la lleva `contenido_imagen.csv`, sin duplicar archivos.

| Carpeta | Qué guarda |
|---|---|
| `EOM/` `PM/` `SI/` | Todo lo de cada carrera |
| `<carrera>/equipos/<fabricante-modelo>/` | El taller: catálogo PDF, scripts propios, referencias y crudos |
| `<carrera>/siluetas/` | Las imágenes terminadas (vitrina) |
| `<carrera>/planos/` | Planos de labor y sus fuentes |
| `comun/` | Lo que sirva a más de una carrera |
| `scripts/` | El motor común: `gen_ia.py` (generación + verificación), `config.py` (credenciales), `dibujar.py` (logo) | — |
| `scripts/_historial/` | Iteraciones abandonadas; se conservan como registro, **no se ejecutan** | — |
| `_descartado/` | Caminos evaluados y desechados, con el porqué ([ver](_descartado/00_LEEME.md)) | — |

**Cómo circula un archivo:** se trabaja en `equipos/`, y cuando la silueta pasa la verificación **se promueve** a `siluetas/` con el nombre normalizado `fabricante-modelo_vista.ext` (`epiroc-boomer-s1_perfil.png`). Ese nombre es el que registra [`05_Base-de-datos/imagenes.csv`](../05_Base-de-datos/imagenes.csv).

**Nunca se organizan las imágenes por curso.** La vitrina es plana; la relación curso↔imagen la lleva `contenido_imagen.csv` en la base de datos, que permite reusar una imagen en varios cursos.

## Credenciales

La generación de imágenes usa la API de OpenAI con **una clave por proyecto**: cada instructor tiene la suya, con su propio límite de gasto, revocable desde el panel de la organización.

Va en un `.env` local que el `.gitignore` excluye. **Nunca se escribe en el código ni se comparte** — si la necesitas, se pide, no se copia de otro.

## Los tres caminos, y en qué estado está cada equipo

El §10 admite tres formas de llegar a una imagen. La columna `metodo` de `imagenes.csv` registra cuál se usó:

| Método | Qué es | Usa la API |
|---|---|---|
| `extraccion` | La vista se saca del PDF con PyMuPDF: es la **referencia** que se le envía al modelo, y sirve además como figura del fabricante | no |
| `geometria` | Se segmenta y redibuja por código (densidad de tinta, clasificación de figuras, umbral de gris). Da vector, pero es frágil: cada catálogo dibuja distinto | no |
| **`hibrido`** | **El camino por defecto.** El modelo genera desde la referencia real y el resultado **se verifica contra las cotas**; si no pasa, se regenera | sí |

**El híbrido es el camino normal, no la excepción.** Da mejor calidad y un estilo uniforme para todo el set, que es lo que el §10 busca. La extracción se usa siempre —produce la referencia—; la geometría queda como recurso cuando conviene, no como meta.

**Se acepta el gasto que implica.** El bucle puede consumir varios intentos por vista; a cambio se obtiene una imagen legible y consistente, que es lo que llega a la clase.

**El vector no es un requisito.** La idea inicial era vectorizar todo, pero si el modelo entrega mejores siluetas en PNG, se trabaja en PNG. Lo que manda es la fidelidad al catálogo y la legibilidad de las piezas, no el formato.

| Equipo | Perfil | Planta | Estado |
|---|---|---|---|
| **Jumbo Boomer S1** | híbrido ✓ | híbrido ✓ | Pasaron el bucle automático; falta la **revisión visual** del instructor |
| **Scooptram ST14** | geometría | geometría | Lo que hay es la versión por código. **Por regenerar en híbrido** — ya está dado de alta en `gen_ia.py` con sus controles (4,18 y 1,57) |
| **Excavadora CAT 336** | geometría | — | **Por regenerar en híbrido.** Falta darla de alta en `gen_ia.py` y sacar su control de aspecto de las cotas |

## Pendiente

- **Regenerar el scooptram y la excavadora** por el camino híbrido. Lo que existe hoy es la versión geométrica, que queda como referencia.
- **Revisar visualmente el jumbo** y marcar `estado=verificada` en `imagenes.csv`. Ninguna imagen entra a un PPT sin eso.
- Dar de alta la **excavadora** en `gen_ia.py` con su control de aspecto.
- **Regenerar el visor** de la base de datos: aún no conoce las tablas `imagenes` ni `contenido_imagen`, ni las dos validaciones nuevas. *(En espera hasta que el resto esté claro.)*
- `figuras-fabricante/` sigue vacía: las figuras del scooptram están en su taller, por promover.
