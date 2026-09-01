# 11 — Cómo se produce un PPT de sesión

Estándar de producción de los PPT de sesión (plantillas 004A/004B): **cómo se pide, qué lleva, y de qué tamaño va el texto y la imagen.** Aplica a las tres carreras.

Sale de rehacer la sesión 1 de SI · Sistema de gestión: el primer PPT era correcto en contenido y **ilegible al proyectar** —el texto de las imágenes salía a 5,6 pt—, y media lámina quedaba en blanco. Ninguno de los dos defectos era de contenido: nadie había fijado cuánto debe medir una letra ni qué lámina lleva imagen.

Complementa al [§07](07_ppt-004A-004B.md), que define la anatomía del PPT. **Está escrito para ser autosuficiente:** quien va a producir un PPT no debería tener que abrir tres documentos.

---

## 1 · Cómo se pide un PPT

**El PPT no se maqueta: se genera.** Sale de `laminas.csv` con `generar_ppt.py`, sobre la plantilla oficial que ya trae la marca montada.

```
laminas.csv  →  generar_ppt.py  →  revisar_ppt.py  →  mirar lo marcado  →  entregar
```

> **El archivo es el resultado, no el original.** Lo que hay que corregir se corrige en la base y se vuelve a generar. Retocar el .pptx a mano funciona hasta la siguiente corrida, en la que se pierde. Nos pasó con el título de una lámina.

### Lo que hay que tener listo antes de pedirlo

Sin esto, quien produzca el PPT tendrá que inventar — y lo inventado no traza al aprendizaje esperado.

| | Qué se entrega | Dónde vive |
|---|---|---|
| 1 | **Aprendizaje esperado** de la sesión, con el verbo dentro del techo del indicador | `sesiones.csv` |
| 2 | **3 a 5 puntos clave**, cada uno con `origen` = `oficial` (baja del temario) o con quién lo aprobó | `contenidos.csv` |
| 3 | **Desarrollo** de cada punto clave: 7 a 10 ideas de 8 a 11 palabras, separadas por ` \| ` | `contenidos.csv`, columna `desarrollo` |
| 4 | **Caso breve** de la sesión y a qué colaborativo tributa | `casos.csv` |
| 5 | **Ruta de los 5 momentos** con minutaje que sume 135, y en cada uno su **rutina** y su **técnica** | `actividades.csv` |
| 6 | **Qué debe mostrar** cada imagen, en una frase | `laminas.csv`, columna `que_muestra` |

**El punto 3 es el que más se olvida y el que más se nota.** Sin desarrollo, la lámina de tema queda con una línea y el instructor sin de qué hablar. Una lámina vacía es falta de contenido, no de diseño.

**El punto 6 es el encargo de las imágenes.** Escribir *«esquema de las piezas de un sistema de gestión: política, objetivos, procesos y registros»* permite dibujarlas sin adivinar y, después, contrastar que lo dibujado sea lo pedido.

---

## 2 · El presupuesto de la sesión

| | Valor |
|---|---|
| Diapositivas | **28 a 32** para 135 minutos |
| Minutaje | Conexión 20 · Adquisición 45 · Aplicación 40 · Discusión 20 · Reflexión 10 |
| Ideas por lámina de tema | **3 a 4** — menos es lámina flaca, más es muro |
| Palabras por lámina | máximo **90** (110 en la triangulación) |

> Un PPT oficial que revisamos traía **45 diapositivas** para los mismos 135 minutos. Es el error #4 del [§08](08_criterios-de-calidad.md): no se puede cerrar por tiempo, y lo que se bota es la reflexión.

### El esqueleto obligatorio

Estas láminas van siempre, en este orden. Lo demás cuelga de ellas.

| | Lámina | Minutos |
|---|---|---|
| 1 | Portada del programa | — |
| 2 | Subportada de sesión (unidad didáctica · N° · tema) | — |
| 3 | **CONEXIÓN** — una palabra, un ícono | — |
| 4 | Escala de ánimo *(ver abajo)* | 3 |
| 5 | **Ruta de aprendizaje** — los cinco momentos con sus minutos | 2 |
| 6 | **Triangulación** — aprendizaje previsto · puntos claves · evaluación | 3 |
| 7 | Estímulo de la rutina de Conexión | 6 – 8 |
| 8 | **ADQUISICIÓN** | — |
| … | Láminas de tema, una por tramo de puntos clave | 45 en total |
| … | **APLICACIÓN** → planteamiento del caso → trabajo en equipo | 40 |
| … | **DISCUSIÓN** → sustentación con formato | 20 |
| … | **REFLEXIÓN** → rutina de cierre → cierre y puente a la sesión siguiente | 10 |
| final | Tapa | — |

**Solo en la sesión 1** se añaden el curso en una lámina y el sistema de evaluación, y la Conexión sube a 20 minutos repartidos.

**La lámina de Ruta de aprendizaje** dice qué se hace en cada momento y **cuántos minutos dura**. El estudiante sabe dónde está parado y cuánto falta. Se redibuja en cada sesión con su propio minutaje.

**La Aplicación va en dos láminas, no en una:** el planteamiento con las preguntas que conduce el instructor (fases 1 y 2 del trabajo con el caso) y luego la consigna del trabajo en equipo (fase 3). Saltar de la consigna al trabajo es el defecto que señala el [§06](06_casos-rubricas-evaluacion.md).

**Los tiempos y el tamaño de equipo van escritos en la lámina:** *«Equipos de 3 · 30 min de trabajo»*, *«2 min por equipo»*.

---

## 3 · Rutina y técnica en cada momento

Cada momento lleva **una rutina de pensamiento nombrada** y **una técnica de enseñanza declarada**. Las dos se registran en `actividades.csv`, columnas `rutina` y `tecnica`.

| Momento | Rutina que funciona | Costo | Técnica |
|---|---|---|---|
| Conexión | Veo–Pienso–Me pregunto | 6 – 8' | Estudio de casos · apertura |
| Adquisición | ¿Qué te hace decir eso? | **0'** — se intercala | Enseñanza por contraste |
| Aplicación | Semáforo · Tira y afloja | estructura el momento | Estudio de casos · fases 1 a 3 |
| Discusión | Afirmación–Apoyo–Pregunta | **0'** — es el formato de la exposición | Estudio de casos · fase 4 |
| Reflexión | Titular · Antes pensaba… ahora pienso… | 4 – 7' | Metacognición |

**La rutina no se suma al momento: lo estructura.** El repertorio completo y su costo en minutos están en el [§05](05_diseno-de-sesion.md).

**La columna `tecnica` es nueva.** Antes solo se registraba la rutina, así que la técnica se aplicaba sin quedar en ninguna parte y nadie podía verificar que se cumplió.

---

## 4 · Las dos bandas de tamaño

| | Banda | Dónde |
|---|---|---|
| **Título de lámina** | **36 – 40 pt** | Toda lámina de tema y de contenido |
| **Cuerpo** | **20 – 24 pt** | Viñetas, consignas, preguntas, triangulación |

**No son mínimos deseables: son mínimos de lectura.** Una sesión virtual se ve en pantallas de portátil y en teléfonos; por debajo de 20 pt el cuerpo deja de leerse y el estudiante desconecta de la lámina.

**No se fijan a pelo, se ajustan solos.** El generador arranca cada título en 40 y lo baja de punto en punto solo si no cabe, con suelo en 36; el cuerpo arranca en 24 y no baja de 20. Así la lámina con poco texto usa el tamaño mayor y ninguna se sale del rango.

```python
# 05_Base-de-datos/generar_ppt.py
TITULO_MAX, TITULO_MIN = 40, 36
CUERPO_MAX, CUERPO_MIN = 24, 20
texto(..., banda="titulo")   # o banda="cuerpo"
```

### Lo que esto obliga: menos texto por lámina

A 20 pt cabe **la mitad** que a 14. Los presupuestos reales, ya medidos sobre las cajas de la plantilla:

| Tipo de lámina | Caja de cuerpo | Cabe |
|---|---|---|
| Tema (texto izquierda / imagen derecha) | 5,35 × 3,30 in | **3 a 4 viñetas de 8 a 11 palabras** |
| Tema (imagen izquierda / texto derecha) | 5,85 × 3,55 in | 3 a 4 viñetas de 10 a 12 palabras |
| Contenido con imagen | 5,60 × 4,10 in | Una consigna de 6 a 8 líneas cortas |
| Contenido a ancho completo | 10,5 × 3,90 in | Una consigna de 8 a 10 líneas |
| Triangulación | tres zonas | 90 – 110 palabras en total (§07) |

**Acortar la viñeta no es recortar el curso.** Lo que se cuenta lo cuenta el instructor; la lámina es apoyo. Una viñeta de 20 palabras es un párrafo que nadie lee mientras alguien habla.

### Excepciones declaradas

- **Portada y subportada de sesión** conservan sus tamaños (32 y 27 pt): son la maqueta institucional, con la escuadra y el logo montados en el patrón.
- **Subportadas de momento** van a 80 pt con una sola palabra, como manda el §07.

---

## 5 · El texto dentro de las imágenes

Es el error que más cuesta ver, porque en la pantalla del que diseña la imagen se ve perfecta: se abre a tamaño completo. **Dentro de la lámina se reduce, y el texto se reduce con ella.**

### La fórmula

```
pt_proyectado  =  6 × px_de_la_fuente ÷ px_de_ancho_del_lienzo × 72
```

El 6 son las pulgadas de ancho del hueco de imagen en la lámina.

> **El caso que lo enseñó.** El mural de la sesión 1 medía 1841 px de ancho con cuerpo de 24 px. Proyectado: **5,6 pt**. Ilegible. Los catorce esquemas de esa sesión estaban entre 9 y 10 pt por la misma razón.

### El estándar

| | Valor |
|---|---|
| Ancho del lienzo | **1500 px** |
| Cuerpo | **52 px** → 15 pt proyectados |
| Título dentro del esquema | **62 px** → 18 pt |
| Nota al pie del esquema | 42 px → 12 pt |

**Lo que decide la legibilidad no es el tamaño en píxeles: es la razón entre la fuente y el ancho del lienzo.** Ampliar el PNG no arregla nada — crecen los dos a la vez.

### La consecuencia: menos elementos, más grandes

Para que quepa a 52 px hay que quitar cosas. En la sesión 1: el mural bajó de seis documentos a cuatro, la tabla de normas de tres decretos a dos, el SSOMAC de frases a una línea por letra. **Ninguno perdió lo que enseñaba.**

Regla práctica: **un esquema, una idea**. Si necesita más de seis bloques o más de cuatro líneas por bloque, son dos esquemas.

### Huecos de imagen de la plantilla

| Tipo de lámina | Hueco | Proporción |
|---|---|---|
| Tema · texto izquierda | 6,15 × 5,85 in | 1,05 |
| Tema · texto derecha | 5,90 × 5,20 in | 1,13 |
| Contenido con imagen | 6,00 × 4,70 in | 1,28 |

Dibujar el lienzo con una proporción parecida evita que el esquema se encoja por el lado que le sobra.

---

## 6 · Qué imagen lleva cada lámina

**Toda lámina que se parta a la mitad necesita imagen.** Las de tema alternan texto a la izquierda y texto a la derecha: sin imagen, media lámina queda en blanco y el texto se apelmaza en una columna. Las de contenido a ancho completo no la necesitan.

### La imagen tiene que enseñar, no acompañar

| Sirve | No sirve |
|---|---|
| Una tabla que compara | Una foto de gente reunida |
| Un ciclo con sus etapas | Un dibujo de alguien pensando |
| Un mapa de procesos | Un icono decorativo |
| Un antes / después | Una imagen de banco de fotos |

Si la lámina se entiende igual tapando la imagen, la imagen sobra.

### La imagen no puede repetir el texto

Al ponerle esquema a todo aparece el defecto contrario: el dibujo lista las cuatro letras del SSOMAC y las viñetas también. **El esquema lleva el peso —es lo que se recuerda— y el texto aporta lo que el dibujo no puede decir**: el porqué, la consecuencia, el ejemplo.

### Un estímulo muestra hechos, no juicios

Vale para toda imagen que alimente una rutina de pensamiento. El mural de la sesión 1 llevaba primero sellos rojos —«SIN FIRMAR», «SIN SEGREGAR»— y eso **interpretaba por el estudiante**, que es exactamente lo que la rutina le pide hacer a él. Se quitaron: quedan la política con la línea de firma vacía, el mapa de riesgos en blanco, el extintor con su fecha. **El hecho lo pone la imagen; el juicio lo pone el alumno.**

### Los esquemas van sin título dentro del PPT

El título ya lo pone la lámina. Se generan con cabecera propia solo si van a verse sueltos (material autónomo, anexo).

---

## 7 · Cómo se dibujan los esquemas

**Dibujo determinista, no modelo generativo.** Son código que traza cajas, tablas y arcos: se reeditan, salen siempre iguales y no inventan nada. Para esquemas conceptuales **no aplica** el control de cotas del [§10](10_imagenes-y-siluetas-de-equipos.md), que es para equipos.

- Viven en `04_Recursos-graficos/<CARRERA>/esquemas/`.
- Los recursos comunes a las tres carreras —como la escala de ánimo— viven en `04_Recursos-graficos/comun/dinamicas/`.
- Se registran en `imagenes.csv` con `categoria=esquema`, `estado=verificada` y su descripción. **Verificada basta para que la figura entre a la lámina** — es la barra del `CLAUDE.md`. La firma del instructor líder se estampa de un golpe con `python aprobar_imagenes.py <CARRERA>`, y solo se exige cuando se genera con `--estricto`, para el entregable que va a revisión.
- La tipografía disponible en los equipos del proyecto es **Arial**. Las de marca (Barlow, Oswald) no están instaladas.

### La paleta

Los ocho colores del material. **Usar siempre estos**: si cada carrera elige los suyos, el material deja de parecer del mismo curso. Cierra la deuda que el §07 dejaba abierta —*«colores sin sistema, definir paleta»*—.

| | Hex | Para qué |
|---|---|---|
| Azul marino | `#0D2632` | Texto, cabeceras de tabla, bloques de énfasis |
| Azul | `#167FB9` | Primera categoría de una serie |
| Verde | `#00B29C` | Segunda categoría |
| Morado | `#5052A9` | Tercera categoría |
| Ámbar | `#FFC505` | Lo que hay que destacar. Con texto azul marino encima, nunca blanco |
| Gris | `#6C7A82` | Texto secundario |
| Gris claro | `#EEF1F3` | Fondo de bloque |
| Rojo | `#C0392B` | Solo para lo que está mal o vencido. Con moderación |

**Tipografía: Arial.** Las de marca (Barlow, Oswald) no están instaladas en los equipos del proyecto.

### Recursos comunes a las tres carreras

Viven en `04_Recursos-graficos/comun/dinamicas/` y se usan tal cual, sin rehacerlos.

| `imagen_id` | Qué es | Cuándo |
|---|---|---|
| `IMG-ESCALA-ANIMO` | Escala de ánimo de nueve pinturas célebres, numeradas. El estudiante responde **con los dedos de la mano** | Apertura de **cualquier** sesión, no solo la primera |

Es un recurso institucional ya en uso en los PPT oficiales de CETEMIN. Da lectura del grupo en 30 segundos y sin escribir nada.

### Repertorio de formas que ya funciona

**cadena** (pasos que se siguen) · **tabla** (comparar por columnas) · **ciclo** (PHVA y similares) · **franjas** (niveles: estratégico / operativo / apoyo) · **comparativa a dos columnas** (antes / después) · **fichas numeradas** (elementos a clasificar).

---

## 8 · Qué NO copiar de un PPT existente

Un PPT antiguo sirve de referencia de marca y de estructura, **no de molde**. Lo que hay que filtrar, medido sobre un PPT oficial real:

| Lo que se ve | Por qué no |
|---|---|
| **45 diapositivas** para 135 minutos | No cierra por tiempo · error #4 |
| Definiciones de norma copiadas enteras (111 y 142 palabras) | Muro de texto · error #5 |
| Ilustración decorativa de gente pensando junto a un interrogante | No enseña nada; ocupa el sitio de un esquema |
| Teoría incrustada como PNG a pantalla completa | No editable, no buscable, y se lleva el 96 % del peso |
| *«¿Qué observaron en el video?»* | Preguntar no es una rutina: no tiene estructura ni deja evidencia · error #1 |

**Lo que sí se toma:** la marca, el orden de los momentos, los tiempos escritos en la lámina y los recursos comunes.

---

## 9 · Lo que el revisor comprueba solo

`revisar_ppt.py` bloquea la entrega si encuentra:

- **muro de texto** — más de 90 palabras por lámina (110 en la triangulación)
- **lámina flaca** — una lámina de tema con menos de 3 ideas propias
- **lámina sin imagen** en Adquisición
- **lámina que anuncia una imagen** («mira la fotografía») y no la trae
- **texto repetido** entre láminas · **elementos fuera del lienzo** · **el minutaje no suma 135**

```
python revisar_ppt.py <sesion_id> [ruta.pptx]
```

**Lo medido no se opina y lo mirado no se mide.** El revisor también lista las láminas cuya imagen hay que **contrastar a ojo** contra lo que la lámina dice que debe mostrar. Esas se miran una por una antes de entregar.

---

## 10 · El kit para dibujar los esquemas — código completo

**Este apartado existe porque un estándar sin herramienta no se reproduce.** El §11 se leyó en otra carrera y el resultado salió distinto: el documento describía tamaños que el generador de esa máquina no tenía programados, y no había con qué dibujar los esquemas.

El código de abajo **es el archivo** `04_Recursos-graficos/comun/esquemas.py`. Si tu clon está al día, ya lo tienes; si no, cópialo tal cual a esa ruta y funciona.

```
python -m pip install pillow
```

### Cómo se usa

```python
import sys, os
sys.path.insert(0, r"..._Recursos-graficos\comun")
from esquemas import *

DEST = r"..._Recursos-graficos\EOM\esquemas"

im, d = lienzo(1290)
filas_letra(d, [("P", "PLANIFICAR", "Definir qué se quiere y cómo", AZUL2),
                ("H", "HACER",      "Ejecutar lo planificado",      TEAL),
                ("V", "VERIFICAR",  "Medir si salió como se esperaba", MORADO),
                ("A", "ACTUAR",     "Corregir y volver a planificar",  AMBAR)])
guardar(im, "phva_etapas.png", DEST)
```

Al guardar imprime el tamaño proyectado. **Si el cuerpo baja de 14 pt, sobra contenido: quita elementos, no encojas la letra.**

### Las seis formas que trae

| Función | Para qué |
|---|---|
| `filas_letra` | Siglas: SSOMAC, PHVA — una fila por letra |
| `tabla` | Comparar por columnas, con una celda destacada |
| `ciclo` | Anillo de cuatro cuadrantes con núcleo |
| `franjas` | Niveles apilados: estratégicos / operativos / de apoyo |
| `comparativa` | Sin / con · antes / después, a dos columnas |
| `fichas` | Elementos numerados a clasificar |

Todas usan la paleta y los tamaños del estándar, y `guardar()` recorta el aire sobrante — sin ese recorte el esquema se dibuja más pequeño de lo que cabe, porque el hueco de la lámina se llena por proporción.

### El archivo

```python
# -*- coding: utf-8 -*-
"""Kit para dibujar los esquemas de las láminas. Común a las tres carreras.

POR QUÉ EXISTE
    El texto dentro de una imagen se reduce cuando la imagen entra en la lámina.
    Lo que decide si se lee no es el tamaño en píxeles sino la RAZÓN entre la
    fuente y el ancho del lienzo:

        pt_proyectado = 6 * px_fuente / px_ancho_lienzo * 72

    Con W = 1500 y cuerpo de 52 px salen 15 pt. Con 24 px sobre 1841 salían 5,6.

CÓMO SE USA
    from esquemas import *

    im, d = lienzo(1200)
    filas_letra(d, [("S", "SEGURIDAD", "Protege del accidente", AZUL2), ...])
    guardar(im, "ssomac_cuatro-letras.png", DEST)

REGLAS
    · un esquema, una idea. Más de 6 bloques o más de 4 líneas por bloque = dos esquemas
    · sin título: el título lo pone la lámina
    · si es estímulo de una rutina, muestra HECHOS y ningún juicio
    · los colores salen de la paleta de abajo, siempre

Requiere Pillow:  python -m pip install pillow
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageChops

# ── el lienzo y los tamaños ───────────────────────────────────────────────
W = 1500                     # ancho fijo: de aquí salen los pt proyectados
TIT, CUE, NOTA = 62, 52, 42  # 17,9 · 15,0 · 12,1 pt

# ── la paleta (§11). Usar siempre estos ───────────────────────────────────
AZUL   = (13, 38, 50)        # #0D2632  texto, cabeceras, bloques de énfasis
AZUL2  = (22, 127, 185)      # #167FB9  primera categoría
TEAL   = (0, 178, 156)       # #00B29C  segunda
MORADO = (80, 82, 169)       # #5052A9  tercera
AMBAR  = (255, 197, 5)       # #FFC505  lo que hay que destacar (texto AZUL encima)
GRIS   = (108, 122, 130)     # #6C7A82  texto secundario
GRISC  = (238, 241, 243)     # #EEF1F3  fondo de bloque
BLANCO = (255, 255, 255)
ROJO   = (192, 57, 43)       # #C0392B  solo lo que está mal. Con moderación

FUENTES = r"C:\Windows\Fonts"   # Arial: es la única instalada en los equipos


# ── utilidades ────────────────────────────────────────────────────────────
def fu(px, bold=False):
    return ImageFont.truetype(os.path.join(FUENTES, "arialbd.ttf" if bold else "arial.ttf"), px)


def an(d, t, f):
    a = d.textbbox((0, 0), t, font=f)
    return a[2] - a[0]


def cen(d, x, y, w, t, px, color, bold=True, margen=30):
    """Centra el texto y, si no cabe, baja de punto hasta que quepa."""
    f = fu(px, bold)
    while an(d, t, f) > w - margen and px > 26:
        px -= 2
        f = fu(px, bold)
    d.text((x + (w - an(d, t, f)) / 2, y), t, font=f, fill=color)


def izq(d, x, y, t, px, color, bold=False):
    d.text((x, y), t, font=fu(px, bold), fill=color)


def envolver(d, t, px, ancho):
    f, lineas, act = fu(px), [], ""
    for p in t.split():
        s = (act + " " + p).strip()
        if an(d, s, f) <= ancho:
            act = s
        else:
            lineas.append(act); act = p
    if act:
        lineas.append(act)
    return lineas


def lienzo(alto):
    im = Image.new("RGB", (W, alto), BLANCO)
    return im, ImageDraw.Draw(im)


def guardar(im, nombre, destino):
    """Recorta el aire sobrante y guarda. Sin recorte el esquema se dibuja
    más pequeño de lo que cabe, porque el hueco se llena por proporción."""
    caja = ImageChops.difference(im, Image.new("RGB", im.size, BLANCO)).getbbox()
    if caja:
        m = 24
        im = im.crop((max(0, caja[0] - m), max(0, caja[1] - m),
                      min(im.width, caja[2] + m), min(im.height, caja[3] + m)))
    os.makedirs(destino, exist_ok=True)
    im.save(os.path.join(destino, nombre), "PNG")
    print("   %-42s %sx%s · cuerpo %.1f pt" % (nombre, im.width, im.height,
                                               6.0 * CUE / im.width * 72))
    return im


def banda(d, y, alto, texto, px=NOTA, fondo=GRISC, tinta=AZUL):
    """Franja de cierre con la idea que hay que llevarse."""
    d.rounded_rectangle([50, y, W - 50, y + alto], 18, fill=fondo)
    cen(d, 50, y + (alto - px) / 2 - 6, W - 100, texto, px, tinta)


# ── las seis formas que ya funcionan ──────────────────────────────────────
def filas_letra(d, filas, y=60, alto=280, sep=30):
    """(letra, NOMBRE, detalle, color) — para siglas: SSOMAC, PHVA…"""
    for letra, nombre, det, col in filas:
        d.rounded_rectangle([50, y, W - 50, y + alto], 20, fill=GRISC)
        d.rounded_rectangle([50, y, 300, y + alto], 20, fill=col)
        d.rectangle([260, y, 300, y + alto], fill=col)
        cen(d, 50, y + alto / 2 - 58, 250, letra, 92, AZUL if col == AMBAR else BLANCO)
        izq(d, 350, y + 62, nombre, TIT, AZUL, True)
        izq(d, 350, y + 155, det, CUE, GRIS)
        y += alto + sep
    return y


def tabla(d, encabezados, filas, cortes, y=60):
    """Comparar por columnas. filas = [([col1...], [col2...], destacado, fondo, tinta)]"""
    x = cortes
    d.rectangle([x[0], y, x[-1], y + 100], fill=AZUL)
    for i, t in enumerate(encabezados):
        cen(d, x[i], y + 26, x[i + 1] - x[i], t, 48, BLANCO)
    y += 100
    for celdas, destacado, fondo, tinta in filas:
        alto = 60 + max(len(c) for c in celdas) * 66
        d.rectangle([x[0], y, x[-1], y + alto], fill=BLANCO, outline=(214, 220, 224), width=3)
        if destacado:
            d.rectangle([x[-2] + 14, y + 20, x[-1] - 14, y + alto - 20], fill=fondo)
        for j, col in enumerate(celdas):
            for i, t in enumerate(col):
                izq(d, x[j] + 32, y + (alto - len(col) * 64) / 2 + i * 64, t, CUE, AZUL)
        if destacado:
            cen(d, x[-2], y + alto / 2 - 26, x[-1] - x[-2], destacado, 46, tinta)
        y += alto
    return y


def ciclo(d, cuadrantes, cx, cy, R=560, r=310, centro=None, lista=()):
    """Anillo de cuatro cuadrantes. cuadrantes = [(letra, NOMBRE, ang0, ang1, color)]"""
    for _, _, a0, a1, col in cuadrantes:
        d.pieslice([cx - R, cy - R, cx + R, cy + R], a0 + 3, a1 - 3, fill=col)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANCO)
    for letra, nombre, a0, a1, col in cuadrantes:
        ang = math.radians((a0 + a1) / 2)
        px, py = cx + (R + r) / 2 * math.cos(ang), cy + (R + r) / 2 * math.sin(ang)
        tinta = AZUL if col == AMBAR else BLANCO
        f = fu(84, True); d.text((px - an(d, letra, f) / 2, py - 76), letra, font=f, fill=tinta)
        f = fu(40, True); d.text((px - an(d, nombre, f) / 2, py + 24), nombre, font=f, fill=tinta)
    if centro:
        cen(d, cx - r, cy - 96, 2 * r, centro, 52, AZUL)
        d.line([cx - 130, cy - 24, cx + 130, cy - 24], fill=AMBAR, width=8)
    for i, t in enumerate(lista):
        cen(d, cx - r, cy + 4 + i * 62, 2 * r, t, 46, GRIS, False)


def franjas(d, bloques, im, y=60, alto=330):
    """Niveles apilados. bloques = [(NOMBRE, [cajas], color)]"""
    for nombre, cajas, col in bloques:
        d.rounded_rectangle([50, y, W - 50, y + alto], 18, fill=GRISC)
        d.rounded_rectangle([50, y, 190, y + alto], 18, fill=col)
        d.rectangle([150, y, 190, y + alto], fill=col)
        tx = Image.new("RGB", (alto, 110), col)
        cen(ImageDraw.Draw(tx), 0, 30, alto, nombre, 46, BLANCO)
        im.paste(tx.rotate(90, expand=True), (52, y))
        x, ancho = 240, (W - 300) / len(cajas) - 26
        for c in cajas:
            d.rounded_rectangle([x, y + 55, x + ancho, y + alto - 55], 14, fill=BLANCO)
            cen(d, x, y + alto / 2 - 26, ancho, c, CUE, AZUL, False)
            x += ancho + 26
        y += alto + 30
    return y


def comparativa(d, izquierda, derecha, filas, y=50):
    """Antes / después, sin / con. filas = [([izq...], [der...])]"""
    mid = W / 2
    d.rounded_rectangle([50, y, mid - 20, y + 100], 14, fill=ROJO)
    d.rounded_rectangle([mid + 20, y, W - 50, y + 100], 14, fill=TEAL)
    cen(d, 50, y + 24, mid - 70, izquierda, 52, BLANCO)
    cen(d, mid + 20, y + 24, mid - 70, derecha, 52, BLANCO)
    y += 135
    for a, b in filas:
        alto = 40 + max(len(a), len(b)) * 62
        d.rounded_rectangle([50, y, mid - 20, y + alto], 14, fill=GRISC)
        d.rounded_rectangle([mid + 20, y, W - 50, y + alto], 14, fill=(226, 245, 241))
        for i, t in enumerate(a):
            cen(d, 50, y + 20 + i * 62, mid - 70, t, CUE, GRIS, False)
        for i, t in enumerate(b):
            cen(d, mid + 20, y + 20 + i * 62, mid - 70, t, CUE, AZUL, False)
        y += alto + 22
    return y


def fichas(d, items, y=50, alto=300, cols=2, pie=None):
    """Elementos numerados a clasificar. items = [texto, ...]"""
    ancho = (W - 100 - 40 * (cols - 1)) / cols
    for i, t in enumerate(items):
        x = 50 + (i % cols) * (ancho + 40)
        yy = y + (i // cols) * (alto + 34)
        d.rounded_rectangle([x, yy, x + ancho, yy + alto], 16, fill=GRISC)
        d.rounded_rectangle([x, yy, x + ancho, yy + 12], 16, fill=AZUL2)
        cen(d, x, yy + 40, ancho, str(i + 1), 54, AZUL2)
        cen(d, x, yy + 130, ancho, t, CUE, AZUL, False)
        if pie:
            d.rounded_rectangle([x + ancho / 2 - 110, yy + alto - 84,
                                 x + ancho / 2 + 110, yy + alto - 32], 10, outline=GRIS, width=3)
            cen(d, x, yy + alto - 72, ancho, pie, 40, GRIS, False)
    return y + ((len(items) + cols - 1) // cols) * (alto + 34)


# ── ejemplo mínimo ────────────────────────────────────────────────────────
if __name__ == "__main__":
    DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ejemplo")
    im, d = lienzo(1290)
    filas_letra(d, [("P", "PLANIFICAR", "Definir qué se quiere y cómo", AZUL2),
                    ("H", "HACER", "Ejecutar lo planificado", TEAL),
                    ("V", "VERIFICAR", "Medir si salió como se esperaba", MORADO),
                    ("A", "ACTUAR", "Corregir y volver a planificar", AMBAR)])
    guardar(im, "ejemplo_phva.png", DEST)
    print("\nSi el cuerpo sale por debajo de 14 pt, hay demasiado contenido: quita, no encojas.")

```

---

## 11 · Lo que tiene que estar en tu clon

El §11 **da por hecho** que estas cuatro cosas están en tu copia del repositorio. Si el resultado no se parece, comprueba esto antes que nada:

| | Qué | Cómo lo compruebas |
|---|---|---|
| 1 | `generar_ppt.py` con las bandas | `grep TITULO_MAX 05_Base-de-datos/generar_ppt.py` → debe decir `40, 36` |
| 2 | `revisar_ppt.py` con los avisos nuevos | `grep "ANUNCIA una imagen" 05_Base-de-datos/revisar_ppt.py` → debe encontrarlo |
| 3 | `04_Recursos-graficos/comun/esquemas.py` | que exista |
| 4 | Columna `tecnica` en tu `actividades.csv` | `head -1 05_Base-de-datos/<CARRERA>/actividades.csv` |

Si falta alguna: `git pull`. Y si sigue faltando, es que el cambio no se ha subido todavía — avisa antes de reescribirlo por tu cuenta.

**Un documento no cambia el resultado si la herramienta no cambia con él.** Los tamaños de texto de la lámina no los pone el diseñador: los pone `generar_ppt.py`. Leerlos aquí y no tenerlos allí produce exactamente lo que produjo: un PPT con el formato viejo.

---

## 12 · Lista de comprobación

**Antes de pedir el PPT**

- [ ] ¿El aprendizaje esperado está escrito y su verbo cabe bajo el del indicador?
- [ ] ¿Hay 3 a 5 puntos clave, todos con `origen` declarado?
- [ ] ¿Cada punto clave trae 7 a 10 ideas de desarrollo?
- [ ] ¿Está el caso de la sesión y a qué colaborativo tributa?
- [ ] ¿Cada momento tiene rutina y técnica, y el minutaje suma 135?
- [ ] ¿Cada imagen tiene escrito en una frase qué debe mostrar?

**Antes de entregarlo**

- [ ] ¿Entre 28 y 32 diapositivas?
- [ ] ¿Los títulos entre 36 y 40, y el cuerpo entre 20 y 24?
- [ ] ¿Cada viñeta baja de 12 palabras?
- [ ] ¿Toda lámina partida a la mitad tiene imagen?
- [ ] ¿El texto de la imagen llega a 15 pt proyectados? *(6 × px ÷ ancho × 72)*
- [ ] ¿La imagen enseña algo, o solo acompaña?
- [ ] ¿El texto de la lámina dice algo distinto de lo que dice la imagen?
- [ ] ¿Si es estímulo de una rutina, muestra hechos y no juicios?
- [ ] ¿Los colores salen de la paleta del §7?
- [ ] ¿`revisar_ppt.py` está en verde **y** se miraron las láminas que marcó?

---

## Referencia rápida

```
BANDAS DE TEXTO EN LA LÁMINA        títulos 36–40 pt   ·   cuerpo 20–24 pt
TEXTO DENTRO DE LA IMAGEN           lienzo 1500 px  ·  cuerpo 52 px  ·  título 62 px
                                    pt = 6 × px_fuente ÷ px_lienzo × 72   → 15 pt
SESIÓN                              28–32 láminas  ·  135 min  ·  3–5 puntos clave
                                    20+45+40+20+10  ·  3–4 ideas por lámina de tema
GENERAR                             python generar_ppt.py <sesion_id>
REVISAR                             python revisar_ppt.py <sesion_id> [ruta.pptx]
```
