# 10 — Imágenes y siluetas de equipos (procedimiento replicable)

Cómo generar las imágenes de equipos mineros (jumbo, scooptram, dumper, celdas, molinos…) para el **sílabo** y los **PPT**, a partir del **catálogo técnico del fabricante**. Es un procedimiento **repetible**: mismo método para cualquier equipo, mismo estilo para todo el material → el PPT se ve como un sistema.

> Regla base: **nada inventado por IA para equipos técnicos** (la IA inventa geometrías falsas). La fuente es el **dibujo técnico del fabricante**. La IA solo para lo decorativo/ambiental. Ver §08.

> **Dónde van los archivos:** este documento es el *cómo*. Las imágenes producidas, sus fuentes y los scripts viven en [04_Recursos-graficos/](../04_Recursos-graficos/00_LEEME.md).

---

## 0. De dónde sale el equipo: primero la tesis, después el catálogo

**No se elige el equipo "de memoria" ni por lo que salga primero en el buscador.** El equipo que se dibuja tiene que ser uno que **realmente se use en una operación peruana**, y eso se averigua antes de tocar ningún dibujo.

### PROCEDIMIENTO: identificar el equipo

**Paso 1 — Buscar en tesis y repositorios académicos peruanos.** ALICIA (CONCYTEC), y los repositorios de UNI, UNMSM, UNCP, UNSA, UCSM, UPC, UNDAC. Son ingenieros describiendo la operación real, con el **modelo exacto** del equipo instalado.

*Ejemplo real:* buscando plantas concentradoras aparecieron la **Metso MP1250** de Cerro Verde (las mayores del país), la **Nordberg C100** de la concentradora Iscaycruz, y una tesis de la UPC que propone una **Nordberg HP200** para una mina del norte.

**Paso 2 — Anotar el modelo exacto**, con fabricante y serie. Sin modelo no hay catálogo, y sin catálogo no hay dibujo.

**Paso 3 — Buscar el catálogo de ese modelo** en el sitio del fabricante (Epiroc, Sandvik, Metso, Caterpillar, Komatsu). Preferir siempre el **PDF oficial** antes que reproducciones de terceros.

**Paso 4 — Elegir el documento correcto.** No todo documento del fabricante sirve, y esto decide la calidad del resultado:

| Documento | Qué trae | Sirve para |
|---|---|---|
| **Folleto comercial** | Fotos, tablas de capacidad, argumentos de venta | **No sirve**: no tiene dibujo dimensional |
| **Hoja de especificación técnica** | Vistas ortogonales con cotas (L, H, W…) | Silueta y proporción verificable |
| **Corte seccionado / despiece** | El equipo por dentro, con las piezas rotuladas | **Enseñar cómo funciona** y nombrar partes |
| **Manual de partes** | Despieces detallados por conjunto | Detalle fino de un componente |

> **La imagen es tan buena como la fuente.** Con la hoja de la Sandvik CJ411 —que solo da el contorno exterior— la silueta salió correcta pero plana: un bloque, sin mandíbula fija ni móvil. Con el corte del cono Metso HP salieron la taza, el manto, la cóncava, la excéntrica, el eje principal y el contraeje. **Si la lámina tiene que enseñar partes, hay que conseguir un corte; ninguna instrucción al modelo suple una fuente pobre** (y pedírselas sería inventar).

**Paso 5 — Registrar la cita** en `05_Base-de-datos/imagenes.csv`, con fabricante, modelo, documento y página.

### Planos de labores y de planta

Para lo que **no es un equipo** —una galería, una chimenea, la sección de una labor, la disposición de una planta— la fuente equivalente es el **plano**, y se busca igual: en las tesis (suelen incluir secciones y planos de la operación que estudian), en manuales de diseño de minas, o en las normas del sector.

Se tratan con el mismo criterio que un catálogo: **se citan**, se extrae la vista con PyMuPDF y se limpia de cotas por la regla maestra. Un plano de sección de galería es la fuente correcta para dibujar la labor; **inventar sus medidas no es aceptable**, porque el ancho y el alto de la sección son justamente lo que decide si un equipo cabe.

---

## 1. Dos entregables por equipo (usos distintos)

> **Un tercer tipo: el CORTE.** Cuando la lámina tiene que explicar *cómo funciona* el equipo por dentro (cámara de trituración, transmisión, sistema hidráulico), el entregable es un **corte seccionado** con las piezas distinguidas por color y achurado. Suele venir del catálogo como **render en perspectiva**, no como vista ortogonal: es la única excepción admitida a la regla de vista plana, porque para enseñar partes internas la perspectiva muestra lo que una sección plana esconde. Se cita igual que la figura del fabricante.

| | **A. Figura del fabricante** | **B. Silueta** |
|---|---|---|
| **Qué es** | El dibujo técnico tal cual, **con el logo/marca del fabricante** y sus cotas | Contorno del equipo, **relleno macizo**, sin marca ni cotas |
| **Para qué** | **Explicar el equipo**: partes, dimensiones, capacidades | **Procesos y esquemas**: ubicar el equipo en un flujo o labor |
| **Dónde** | Sílabo · PPT de adquisición cuando toca describir el equipo | PPT: diagramas de proceso, ciclo de minado, secuencias |
| **Créditos** | **Obligatorio citar la fuente** (fabricante, modelo, catálogo, año) | Se cita el catálogo de origen en la lámina de fuentes |

**Por qué se conserva el logo en A:** usar la figura **con su marca y citada** es una **cita con atribución** en material educativo — es lo correcto. Borrar la marca y redistribuir el dibujo del fabricante como propio **no** lo es. La silueta (B) sí es una elaboración propia derivada, y también se acredita la fuente.

**Formato de referencia sugerido:**
`Fuente: Epiroc. Boomer S1 — Technical specification. [Catálogo del fabricante], p. 4.`

---

## 2. Procedimiento (replicable, 6 pasos)

## 1 bis. Que las PIEZAS se distingan (no una sola mancha)

**El problema (Walther):** al rellenar todo en un solo tono, **la cuchara y la cabina se leen como un solo cuerpo**. Una silueta plana pierde la lectura de las partes — y **hay piezas importantes cuya separación sí debe percibirse**.

**La solución, en 3 niveles (replicable para cualquier equipo):**

**Nivel 1 — La pieza es una FIGURA, no un trazo.**
Cada componente importante está dibujado como una **figura cerrada** del plano. Firma: **área de su bbox > ~2.5 % del área de la vista**. Filtrar por trazos sueltos trocea todo (probado: con umbral de 6 pt salieron 599 líneas y la silueta quedó picada); filtrar por **figura** deja solo las piezas (212 trazos, ruedas legibles).

**Nivel 2 — Firmas de forma para piezas típicas.**
- **Contorno exterior** → la figura mayor (>85 % del área de la máquina).
- **Ruedas / rodillos / poleas** → **en PERFIL**: bbox casi **cuadrado + 4 curvas** (así se dibuja un círculo). **En PLANTA**: **rectángulo** (la rueda vista desde arriba no es un círculo).
- **Vigas / brazos** → bbox muy alargado (relación > 5:1).

> ⚠️ **La firma de una pieza depende de la VISTA.** La misma rueda es círculo en perfil y rectángulo en planta; el techo/canopy es una línea fina en perfil y una figura grande en planta. Las firmas se declaran **por vista**, no por equipo.

**El umbral se mide contra la MÁQUINA, no contra la vista.** En planta el equipo ocupa una fracción chica del recorte (el resto son arcos de giro); si el umbral se calcula sobre la vista completa, ninguna pieza lo alcanza. *(Planta ST14: caja de la máquina = 67 068 pt²; con umbral 2 % salieron 14 piezas — incluidas las **4 ruedas**, que en planta miden ~60×60 pt.)*

**Nivel 0 (el más simple y el que mejor funciona) — ACHURADO POR PIEZAS (Walther).**
En vez de separar las piezas con líneas o huecos, **darle a cada pieza su propio achurado**: distinta **dirección** y **densidad** que sus vecinas (45° en una, verticales en la contigua, cruzadas en otra, juntas o separadas). Así **cada componente se identifica a simple vista** y no se funden en una masa — sin necesidad de clasificar figuras ni declarar listas.

> Ojo con el matiz: el achurado **no es sombreado de volumen**, es el **recurso para distinguir piezas**. Pedirlo como "sombra" da una ilustración bonita pero las piezas siguen sin leerse; pedirlo como "una trama por pieza" resuelve el problema.

**Nivel 3 — Lista declarada de piezas (del checklist del equipo).**
Las piezas que el catálogo dibuja **dentro** del contorno general (cuchara vs. cabina, cabina vs. motor) no se separan solas: se **declaran** desde la lista de componentes del equipo (§4) y se separan por su zona. Ahí es donde el checklist deja de ser solo verificación y pasa a **gobernar el dibujo**.

**Tres formas de presentar el equipo:**
| Variante | Cómo | Cuándo |
|---|---|---|
| **Sólida** | Silueta rellena en un tono | Diagramas de proceso, ubicar el equipo |
| **Lineada** | Silueta + límites en tono más claro | Cuando hay que rotular partes |
| **LINE ART** (solo líneas) | **Sin relleno**: únicamente contornos y límites de piezas | Preferida por Walther: se leen todas las partes, no pesa visualmente, y combina con cualquier fondo |

**Line art — cómo sale limpio:** dibujar solo los contornos, quitando (1) **cotas** por la regla maestra, (2) **rayado/hatching** y (3) el detalle irrelevante. Regla nueva para el rayado:

> **Rayado = grupos de rectas PARALELAS de IGUAL LONGITUD repetidas** (≥4 con el mismo ángulo y largo). No llevan número, así que la regla maestra no las caza, pero tampoco son la máquina.

**Ojo — la máquina no se dibuja igual en cada vista:** en **perfil** son pocas figuras grandes cerradas (contorno + ruedas ⇒ conviene el umbral por área); en **planta** son **miles de figuras pequeñas** (⇒ el umbral por área la borra: hay que tomar **todo lo que esté dentro de la caja de la máquina**). Se ajusta por vista.

> Regla corta: **silueta = una pieza por figura; separación = el límite entre figuras mayores.** El detalle fino (remaches, texturas) se descarta solo por área.

## 2 bis. La PLANTA de un LHD (scooptram): segmentar por DENSIDAD DE TINTA

**El scooptram siempre se dibuja girando** (Walther): la vista en planta de cualquier catálogo de LHD *es* el diagrama de radio de giro, con la máquina **articulada**. No existe una vista en planta con el equipo recto — no vale la pena buscar otro catálogo por eso. Hay que extraer la máquina **doblada**, que además es más útil: muestra cómo maniobra en la labor.

**El problema universal:** en ese diagrama los **arcos encierran el área barrida**, así que rellenar el contorno produce la mancha equivocada (un triángulo macizo), y las reglas por forma/posición fallan una tras otra.

**La solución que sí funciona — densidad de tinta:**

> **La máquina está llena de detalle; el área barrida está VACÍA.**
> Se segmenta por **densidad local de tinta**, no por relleno de contorno.

```
densidad = filtro_uniforme(tinta, ventana≈45 px)
semilla  = densidad > umbral        (≈0.055–0.085)
máquina  = rellenar_huecos( mayor_componente( cierre(semilla) ) )
```

Ventajas: funciona con dibujos **vectoriales y raster**, no necesita clasificar figuras una por una, y es inmune a arcos, cuñas y cotas (todos de baja densidad). Revisión: la cobertura de tinta debe caer en **55–85 %**, **1 sola pieza**, y no tocar el borde.

**Cómo ubicar las líneas que estorban** (si igual hace falta filtrarlas): tienen firmas reconocibles —
**(a) convergen en un mismo vértice** (bordes de una cuña o cono de barrido); **(b) son paralelas equiespaciadas de igual longitud** (rayado/hatching); **(c) horizontales o verticales largas** (marco y cotas).

> **Elegir bien la vista de origen.** Un diagrama de **radio de giro** dibuja el equipo **articulado (doblado)** y entrelazado con la cuña de barrido y los arcos: sirve como **figura de referencia**, pero es una **mala fuente para una silueta** (no hay límite nítido entre máquina y geometría de construcción). Para siluetas, buscar un dibujo donde el equipo esté **recto y solo**. Si no existe, entregar la referencia y decirlo.

### El entregable es SIEMPRE una vista plana (regla de Walther)

Aunque se genere con IA, la imagen **no deja de ser un dibujo técnico ortogonal**. Error cometido: al pedir "que se vean el piso y las paredes", pedí una **escena realista** (textura de roca, túnel abovedado, profundidad) y el modelo entregó una ilustración pictórica — **inservible**, porque deforma la vista y el equipo deja de leerse como plano.

**Lo correcto:** el piso y las paredes son **las líneas que ya trae el PDF**, no una cueva dibujada.

| Vista | Piso y paredes |
|---|---|
| **Perfil** | La **línea horizontal** bajo las llantas (piso) y otra por encima (techo de la labor) |
| **Planta** | Dos **rectas paralelas** a los lados = los **hastiales** de la galería |

**Cómo representar la roca sin salirse del plano (Walther):** cada línea de límite lleva, **del lado de la roca**, un **achurado a plumilla** — trazos finos y paralelos a ~45°, el convenio estándar de los planos de minería y geotecnia. En **gris neutro**, en una **franja junto a la línea** (nunca rellenando toda la zona), para que no compita con los colores del equipo.

> Regla corta: **piso y paredes = líneas del plano + achurado a plumilla del lado de la roca. Nunca una escena en perspectiva.**

### Antes de nada: identificar el TIPO de dibujo fuente

No todos los catálogos dibujan igual, y **el tipo manda el método**. Comprobar el histograma de grises del recorte antes de elegir técnica:

| Tipo | Cómo se reconoce | Método |
|---|---|---|
| **Vectorial de líneas** (Epiroc) | Miles de `get_drawings`, tinta < 10 % del área | Clasificar **figuras** (cotas por la regla maestra) + unión de figuras rellenas |
| **Raster de líneas** (Sandvik) | Imagen incrustada, sin vectores | **Densidad de tinta** |
| **Ilustración SOMBREADA** (CAT) | **Pico de gris medio** en el histograma (p. ej. 300 000 px en el tono 160) y tinta ~45 % del área | La **silueta ES el área sombreada**: umbralizar el gris. No usar relleno de contorno ni densidad — dan una mancha |

*Caso real:* con el CAT 336 apliqué relleno y densidad y siempre salía un bloque macizo; el histograma reveló que **la máquina está dibujada con rellenos grises**, no con líneas. Diagnosticar el tipo **antes** habría ahorrado varias iteraciones.

**Paso 0 — Conseguir el catálogo y revisar TODAS las vistas.**
Descargar el PDF de especificaciones del fabricante. **Antes de dibujar nada**, revisar las tres vistas: **perfil (lateral)**, **frontal** y **planta**. Perfil = forma general; planta = articulación y cobertura; frontal = ancho/gálibo. Decidir qué se quiere mostrar → elegir la(s) vista(s).

**Paso 1 — Listar los componentes del equipo (y sus subpartes).**
Sin esta lista no se puede verificar nada. *(Ejemplo jumbo, §4.)*

**Paso 2 — Extraer la vista como vector.**
Con PyMuPDF/`fitz`: `page.get_drawings()` da cada trazo con su bbox; se recorta la vista al área deseada. Es vector: escalable y sin pixelado.

### Regla maestra para eliminar cotas (Walther)

> **Toda cota lleva un NÚMERO al costado.** Si es una **longitud**, tiene **una recta**; si es un **ángulo**, tiene **dos rectas**.
> ⇒ **Se parte del número y se borran SUS rectas.**

Es una regla **semántica**, no geométrica: no adivina por forma, longitud ni posición — que es donde fallaron todos los intentos anteriores (borraba la viga, el techo, el chasis). Algoritmo:

1. **Detectar los números** del dibujo (`get_text`, filtrando lo que parece medida: `1 234`, `R 6644`, `Ø 1 788`, `44°`, `2 000 x 45°`).
   *Variante frecuente (CAT y otros):* el dibujo no lleva la medida sino un **índice de referencia (1…9)** y el valor va en la **tabla**. **La regla funciona igual**, porque el índice también se coloca junto a su línea de cota — solo cambia qué es el "número".
2. **Marcar como cota** toda recta larga (≥ ~14 pt) que pase **cerca** de un número (radio ≈ 2.6 × el tamaño del texto, mínimo ~34 pt).
3. **Propagar** a sus **extensiones colineales en contacto** (las líneas auxiliares que van del número a la pieza).
4. Todo lo demás **es la máquina**.

*Resultado medido (planta del ST14):* 9 números, 255 rectas largas → **69 marcadas como cota**, y entre ellas **los 3 bordes de la "cuña" de barrido** que habían resistido todas las reglas anteriores — porque en realidad eran las rectas de las cotas de radio **R 6644 / R 3402 / R 7255**. La cuña no era una figura aparte: **era una cota**.

**Paso 3 — Clasificar las FIGURAS (no los píxeles).**
Cada trazo del vector se clasifica en:

| Capa | Qué es | Qué se hace |
|---|---|---|
| **Equipo** | El cuerpo y sus partes | Se rellena macizo |
| **Terreno / piso** | Recta horizontal baja, tangente a las ruedas | Capa aparte (puede servir como piso de galería) |
| **Trayectoria de giro** | Arcos de gran radio que **envuelven** al equipo (turning radius) | Capa aparte, curva fina discontinua. **OJO: no son las paredes** — son el **camino barrido** al girar. Las **paredes son RECTAS** (esquina entre dos galerías); las cotas 3 000/2 250 son los **anchos** de cada labor |
| **Cota** | Rectas cortas pegadas a un número/flecha, o que van al margen | Se borra |
| **Texto** | Números y rótulos de cota | Se borra |

**Paso 3 bis — CALIBRAR la caja del equipo con las cotas oficiales (evita recortar "a ojo").**
El catálogo trae el **largo** y el **alto** reales. Con la línea de cota del largo se obtiene la **escala**, y de ahí la caja exacta:

```
escala (mm/pt) = largo_real_mm / largo_de_la_cota_en_pt
alto_pt        = alto_real_mm / escala
techo_y        = piso_y − alto_pt        →  caja = [x_cota_largo] × [techo_y … piso_y]
```

*Ejemplo Scooptram ST14:* largo 10 865 mm medidos entre x=683 y x=1042 (359 pt) → escala **30.26 mm/pt**; alto 2 601 mm → **85.9 pt**; piso en y=536.8 → **techo en y=450.9**. Recortar por fuera de esa caja arrastra la **pose de descarga** (balde levantado).

**Paso 4 — SILUETA POR UNIÓN DE FIGURAS RELLENAS (no flood-fill).**
Dibujar **cada figura del equipo rellena y con trazo grueso**; la **unión** de todas es sólida **por construcción**. Así **no puede salir entrecortada**: no hay relleno por inundación que se fugue por las aperturas del contorno. Las demás capas (arcos, terreno) se componen aparte, **sin mezclarse**.

**Paso 5 — VERIFICAR contra la lista de componentes (obligatorio).**
Un check automático mide cada componente; si falta uno, **no se exporta**. Ver §5.

---

## 3. Reglas de oro (destiladas de los errores)

1. **Rellenar primero, borrar cotas después.** Si borras la cota antes de rellenar, abres el contorno y el relleno se fuga.
2. **La posición NO distingue cota de máquina.** La cota se mide *hasta el extremo real* del equipo (la altura hasta el techo, el largo hasta las ruedas, el piso hasta el punto de contacto): **coinciden en el extremo**. Distinguir por: la auxiliar **se va al margen** (donde están los números) o **cruza todo el marco**; la del equipo **se queda en su cúmulo**.
3. **La forma tampoco distingue.** En planta el **boom y la viga son horizontales** y las **ruedas son rectángulos**: borrar "todo lo horizontal/vertical" borra partes reales.
4. **Nunca borrar una figura por su bbox si ese rectángulo pisa el equipo.** Los rellenos gris claro no superan el umbral de trazo: se ignoran solos.
5. **Proteger las primitivas conocidas.** Las ruedas se marcan como zona intocable y se re-cierran; una cota que las cruza no puede morderlas.
6. **Componentes superpuestos:** cuando las figuras se cruzan, clasificar por sus **extremos** (una parte tiene ambos extremos dentro del equipo; una cota tiene un extremo en un número/margen) y rasterizar **por capa separada**.
7. **Trazos finos y punteados (arcos):** no rescatarlos del raster — **redibujarlos desde el vector** con el grosor que se quiera.
8. **Regla práctica que generaliza bien:** una **cota es un segmento recto puro** (`ancho==0` o `alto==0`) y largo; las partes del equipo son trazos con ancho **y** alto (curvas, diagonales, contornos). Funcionó en el Scooptram (108 cotas removidas sin tocar la máquina). Verificar siempre con el check.
9. **Sellar el contorno antes de rellenar:** si el dibujo tiene aperturas, el relleno se fuga y deja huecos → **cierre morfológico** previo.

---

## 4. Lista de componentes — Jumbo (Boomer S1)

| Componente | Subpartes |
|---|---|
| Chasis articulado | Sección trasera (power pack) · articulación central (giro ~40°) · sección delantera |
| Tren de rodaje | 4 neumáticos (2 ejes × 2 lados) · ejes |
| Cabina | ROPS/FOPS (techo + postes) |
| Boom (brazo BUT) | Pivote/base · cilindros · articulaciones |
| Viga de avance (feed) | Cuna/soporte · centralizador |
| Perforadora (rock drill COP) | Percusión/rotación · shank/adaptador |
| Barreno + broca | — |
| Auxiliares | Carretes (agua, cable, manguera) · estabilizadores/gatas · motor + bomba hidráulica |

> **Sin el boom no es un jumbo.** Cada equipo nuevo necesita su propia lista antes de empezar.

---

## 5. Verificación automática (el check)

La revisión **no es "míralo a ojo" al final**: va **dentro** del proceso. El script mide y **solo exporta si pasa**:

- **Por componente:** cobertura mínima en la zona de cada parte (chasis, boom, viga, perforadora, barreno…). Si una da 0% → una figura se borró de más.
- **Invariantes de forma:**
  - **Ruedas redondas** (≥98% del disco relleno) — caza el corte por una cota que cruza.
  - **Despeje abierto** (el hueco bajo el chasis no debe estar relleno) — caza confundir la línea del piso.
  - **Techo presente** — caza borrar el techo con la cota de altura.
  - **Una sola pieza** conexa y **bbox** dentro de lo esperado.
- **Proporción oficial (el check más potente):** el **aspecto** de la silueta (largo/alto en píxeles) debe coincidir con **largo/alto del catálogo**, con desvío **< 8%**. Caza recortes mal hechos y **poses equivocadas**. *Ejemplo:* con el balde levantado el aspecto daba **3.75** contra **4.18** oficial (−10%) → falla; ya calibrado da **4.18 (desvío 0.1%)**.
- **Apoya en el piso:** la silueta debe tocar la línea de terreno (si "flota", el recorte está mal).
- **REVISIÓN DE LA IMAGEN (obligatoria, dentro del loop):** los checks numéricos no bastan — hay que **mirar el resultado** y compararlo con el original. El check automático que hace de "ojo":
  **cobertura** = *(tinta de las figuras clasificadas como máquina que queda cubierta por la silueta)* **≥ 98 %**. Si baja, se borraron partes del equipo. *Ejemplo real: la planta del Scooptram dio **32.7 %** → faltaban dos tercios de la máquina.*
  Complementos: **1 sola pieza**, aspecto vs. catálogo, apoya en el piso. Y una **inspección visual** del render (o de su vista ASCII si no se puede abrir la imagen) antes de dar por buena la silueta.
- **EL LOOP REGENERA (no solo avisa):** si la revisión **no procede**, el script **vuelve a generar** con otros parámetros (grosor de trazo, cierre, apertura) y revisa de nuevo — automáticamente, hasta que pase. Solo entonces exporta. Si ninguna combinación pasa, se queda con la mejor y **lo declara**; nunca entrega en silencio algo que falló.

```
para cada combinación de parámetros:
    silueta = generar(parámetros)
    ok, fallas = revisar(silueta)        # números + IMAGEN (cobertura ≥98%)
    si ok:  exportar; terminar
    si no:  seguir con la siguiente combinación   ← REGENERAR
si ninguna pasó: usar la mejor y REPORTAR las fallas
```

- **Loop:** generar → **revisar (números + imagen)** → **regenerar** → revisar… hasta 0 fallas.

**Diagnóstico visual:** el script genera una imagen que **colorea qué figura clasificó como qué** (rojo = se borra, verde = arco, azul = equipo). Revisarla **antes** de dar por buena la silueta.

---

## 6. REGISTRO DE ERRORES (para mejorar el proceso)

Errores reales cometidos generando estas imágenes, su causa y la corrección. **Cada uno se convirtió en una regla o en un check.**

| # | Error | Causa raíz | Corrección / prevención |
|---|---|---|---|
| 1 | Reconstruir el equipo "a mano" | Dibujar de memoria en vez de usar la fuente | Usar **el vector real** del catálogo; rellenar su contorno, no redibujar |
| 2 | Una rueda salió mordida | Una **cota cruzaba el neumático**; se borró por banda de píxeles | **Proteger las ruedas** como zona intocable + invariante "rueda redonda" |
| 3 | El fondo salió plano (sin despeje) | La **línea del piso** encerraba el hueco bajo el chasis y el relleno lo llenó | Borrar la **figura del suelo** antes de rellenar + invariante "despeje abierto" |
| 4 | Se borró el **techo** de la cabina | Regla por posición ("todo lo de arriba es cota"); pero la cota de altura **llega hasta el techo** | Clasificar por **margen/marco**, no por posición + invariante "techo presente" |
| 5 | Faltó la **viga de avance** en planta | Regla "borrar todo lo horizontal = cota"; la viga **es horizontal** | No borrar por forma: conservar lo **pegado al cúmulo** del equipo |
| 6 | El boom quedó **desconectado** del chasis | Se borró la **cuña gris por su bbox**, y ese rectángulo **pisaba el chasis delantero** | No borrar por bbox lo que se superpone; los grises claros se ignoran solos |
| 7 | No se veían los **radios de giro** | Trazo de **0.25 pt y punteado** → invisible al rasterizar | **Redibujar los arcos desde el vector** con trazo grueso (1.6 pt) |
| 8 | Ruido de puntos sueltos | Restos de flechas y cotas fragmentadas | Descartar componentes por debajo de un umbral de área |
| 9 | Verificar "a ojo" al final | La revisión estaba fuera del proceso | **Check automático por componente**, y no exportar si falla |
| 10 | La silueta salió **con huecos** (Scooptram) | El **contorno del equipo tenía aperturas**: el relleno se fugó hacia adentro | **Cierre morfológico (7×7) antes de rellenar**. No todos los fabricantes dibujan el contorno cerrado: hay que sellarlo |
| 11 | Recorté la máquina por la mitad | Elegí el área de la vista "a ojo" | **Mapear la página primero** (histograma de densidad de figuras por franja) para separar las vistas y hallar sus límites reales |
| 12 | **La figura de referencia salió pixelada** | La exporté como **PNG rasterizado** siendo el original **vectorial** | Exportar la referencia en **SVG**, reconstruido con **solo las figuras de esa vista** (no toda la página: eso pesa 14 MB). PNG solo como respaldo, a alta resolución |
| 13 | En planta se rellenó el **área barrida** en vez de la máquina | La "cuña" de barrido está **pegada** a la máquina; sus bordes son **rectas diagonales**, y mi regla solo quitaba rectas H/V puras | Ampliar la regla: **una figura de un solo segmento recto (cualquier orientación) y largo = línea de construcción/cota** → se resta. Además, restar la **envolvente** por render preciso, nunca por bbox |
| 14 | La silueta salió **entrecortada** | El **flood-fill** de un raster se fuga por cada apertura del contorno y deja trozos sueltos | **Construir la silueta por UNIÓN DE FIGURAS RELLENAS** (vector): cada path se dibuja relleno + trazo grueso y su unión es sólida **por construcción**. Se elimina el flood-fill como método |
| 15 | El equipo salió con el **balde levantado** | El dibujo del catálogo **superpone dos poses** (transporte y descarga) y mi recorte "a ojo" tomó parte de la pose alta | **Calibrar la caja con las cotas oficiales** (Paso 3 bis) + **check de proporción** contra largo/alto del catálogo. Regla: *un dibujo de especificación suele mostrar varias posiciones; hay que decidir cuál se quiere y acotarla con las cotas, no a ojo* |
| 16 | En la **figura de referencia** corté la segunda pose (balde levantado) | Usé el mismo recorte estrecho de la silueta; la pose de descarga sube hasta y≈311 y yo empezaba en y=380 | La **referencia debe mostrar TODAS las poses y cotas** (es el dibujo del fabricante). Silueta y referencia tienen **recortes distintos**: la silueta se acota a **una** pose; la referencia abarca **todo el dibujo**. Si otra vista invade la franja, excluirla **por figura**, no por recorte |
| 17 | Entregué la silueta sin **mirar la imagen** | El loop solo tenía checks numéricos | Meter la **revisión de imagen dentro del loop**: check de **cobertura ≥98 %** contra las figuras clasificadas como máquina + inspección visual del render antes de dar por buena |
| 18 | El loop **avisaba pero no corregía** | La revisión reportaba la falla y el script seguía igual | El loop debe **REGENERAR** con otros parámetros cuando no procede, y repetir hasta pasar. Si ninguna combinación pasa, usar la mejor y **declararlo** |
| 19 | **Mi propia métrica estaba mal**: marcaba "área inventada 27 %" en siluetas correctas | Medía los píxeles de la silueta *lejos de los trazos*; pero **una silueta es sólida y su interior no tiene trazos** — penalizaba el relleno legítimo | Medir el desborde contra la **región de la máquina** (contorno de la tinta **relleno**), no contra la cercanía a los trazos. Lección: **validar también los checks**, no solo el resultado |
| 20 | **El check de cobertura se puede "engañar" rellenando de más** | Una silueta que cubre TODO da 96.8 % de cobertura y parece buena; salió un **triángulo macizo** (el área barrida) en vez de la máquina | La cobertura **sola no basta**: hay que acompañarla de un límite de **desborde** y, sobre todo, de **acotar la máquina** (caja/región calibrada). Y **mirar la imagen**: el número no distingue una máquina de una mancha |
| 21 | Al dejar de borrar diagonales, metí las **líneas de construcción dentro de la clase "máquina"** | Corregí un error (se comía el chasis) creando otro: la cuña de barrido pasó a contar como equipo, y **los dos checks quedaron ciegos** | Clasificar por **pertenencia a la caja de la máquina** + descartar figuras descomunales (`w>150 pt` o `h>150 pt`), en vez de por forma. Lección: **al corregir un error, revisar que no se rompa la clasificación** |
| 22 | Traté la **"cuña" de barrido como una figura de sombreado** y peleé con ella durante ~10 intentos | En realidad **era una COTA**: sus tres bordes son las rectas de los radios **R 6644 / R 3402 / R 7255** | Aplicar la **regla maestra** (cota = número + sus rectas). Lección: **antes de inventar reglas geométricas, preguntarse qué SIGNIFICA cada trazo en el plano** |
| 23 | Mi umbral de aceptación quedó **obsoleto** al mejorar la limpieza | El rango "cobertura 55–88 %" suponía que quedaban cotas dentro; ya limpias, la cobertura legítima **sube a ~90 %** y el check la rechazaba | **Recalibrar los checks cuando cambia el método**: un umbral es válido solo para el pipeline con el que se ajustó |
| 24 | Pedí a la IA una **escena realista** de galería (roca, túnel en 3D) | Interpreté "que se vean piso y paredes" como ambientación pictórica | El entregable **siempre es vista plana**: piso y paredes son **líneas del plano** + achurado a plumilla del lado de la roca |
| 25 | Al agregar el contexto, **la corrección de proporción quedó midiendo la escena** en vez del equipo | Cambié el pipeline y el check siguió igual (mismo patrón del #19) | Separar equipo y roca por **saturación** (equipo en pastel, roca en gris) y aplicar el factor `objetivo ÷ aspecto_del_equipo` a toda la escena |
| 26 | **El contexto cambia el sesgo del modelo** | Sin galería comprimía el perfil (2.97–3.35 vs 3.90); con galería lo **estiró** a 4.42 | Nunca asumir que un ajuste de estilo es "solo estético": **revalidar la proporción cada vez que cambia el prompt** |

**Patrón común de los errores 2–6:** intentar separar **dos cosas co-ubicadas** (cota vs. equipo) usando **posición o forma**. No se puede: la cota se mide *hasta* el equipo. Hay que usar un rasgo que sí las distinga (a dónde va el extremo).

---

## Los dos estados de una imagen, y por qué no deben frenarte

`imagenes.csv` guarda un `estado` por imagen. Solo hay dos que importan:

| Estado | Qué significa | ¿Entra a la lámina? |
|---|---|---|
| **verificada** | La proporción **se midió** contra las cotas del catálogo, o el esquema se midió contra su lienzo. Es medición, no opinión | **Sí.** Es la barra del `CLAUDE.md` |
| **aprobada** | Además, el instructor líder la firmó | Sí, y es la que exige `--estricto` |

**Verificada ya basta.** Antes el generador exigía la firma y, cuando faltaba, el PPT salía **sin figuras y sin decirlo**: el aviso quedaba entre otras líneas y las láminas se armaban vacías. Eso ya no pasa — lo verificado entra, y el aviso dice cuáles faltan firmar.

**Firmar es un comando, no un trámite:**

```
python aprobar_imagenes.py SI          firma todas las verificadas de la carrera
python aprobar_imagenes.py SI --ver    solo muestra cuáles firmaría
```

Estampa quién firma —el instructor líder de esa carrera— y la fecha. **No revisa nada ni toca archivos**: la revisión es la verificación, que ya pasó. Lo que no está verificado no lo toca, y lo dice.

**Y cuando el entregable va a revisión de dirección:**

```
python generar_ppt.py SI-SGCSSMA-S1 --estricto
```

Ahí sí, solo entran las firmadas.

---

## 7. Dónde vive el trabajo

- **Pruebas y generación:** `C:\Users\LEGION\Claude\Imagenes-ppt\<equipo>\` (fuera del proyecto).
- **Contenido por equipo:** el PDF del catálogo (fuente), la(s) vista(s) en vector, la silueta (PNG con transparencia + SVG editable) y el script generador.
- **Al usarlas:** la figura del fabricante va **con su cita**; la silueta va en los diagramas de proceso.

---

*Relacionado: §07 (PPT 004A/004B) · §08 (criterios de calidad).*

## Qué imagen va en cada lámina

Vale para EOM, PM y SI por igual, y para cualquier tipo de imagen: silueta, esquema, fotografía o plano.

### El criterio: **la imagen muestra lo que el título promete**

No lo que el título **menciona**. Si la lámina se llama *«sacar el material»*, la imagen tiene que mostrar material saliendo — no el equipo que lo saca, quieto y en corte de catálogo.

**La prueba: tapar el título.** Se cubre y se mira solo la imagen. ¿Sugiere de qué habla la lámina?

- Un scooptram quieto sugiere *«el scooptram»* → sirve para una lámina sobre el equipo.
- Un scooptram con la cuchara metida en el material sugiere *«carguío»* → sirve para la operación.

Si la imagen sugiere una lámina distinta de la suya, está puesta **por relación**, no por criterio.

### Qué imagen pide cada tipo de contenido

| La lámina enseña | Necesita | Ejemplo |
|---|---|---|
| **un objeto** — qué es un perno | el objeto aislado y legible | silueta · render de catálogo |
| **una operación** — cómo se carga | la **acción en curso** | fotografía del equipo trabajando |
| **un criterio** — cuándo va cada uno | esquema comparativo | los sostenimientos según RMR |
| **una secuencia** — en qué orden | esquema de flujo | ventilar · desatar · limpiar · sostener |
| **una condición** — dónde, con qué medidas | sección, plano o corte | la labor con sus cotas y servicios |

> **El error más fácil de cometer es usar imagen de objeto para una lámina de operación**, y ocurre porque las imágenes de objeto son las que abundan: los catálogos están llenos de equipos quietos y vacíos de equipos trabajando. En PM pasa igual con las chancadoras y las celdas de flotación; en SI, con los EPP fotografiados en el estante en vez de puestos en la faena.

### Lo que no cuenta como imagen

- **Un documento** —ficha, tabla de datos, formato— no se muestra: se lee. Poner una ficha donde falta imagen es rellenar el hueco.
- **Un equipo quieto** donde la lámina enseña una operación.
- **Una imagen de otro tema**, aunque sea del mismo curso.

### Cómo se hace verificable

La lámina declara **qué debe mostrar** su imagen, con verbo:

```
SACAR EL MATERIAL       →  "scooptram cargando material roto en el frente"
SOSTENER LA LABOR       →  "labor con pernos y malla ya instalados"
PERNO, MALLA Y CUADROS  →  "los cuatro sostenimientos comparados por RMR"
```

`revisar_ppt.py` imprime esa frase junto a la imagen colocada, en el bloque **PARA MIRAR**. La pertinencia no se puede medir —es de lo que hay que mirar— pero sí se puede **exigir declarada**, y entonces contrastarla es leer dos líneas en vez de juzgar a ojo si «pega».

**Y tiene un efecto de lado que importa más que el control:** obliga a escribir qué hace falta **antes** de buscar. Sin la frase, uno busca imágenes del tema y elige la mejor que aparece. Con la frase, busca algo concreto — y sabe cuándo no lo encontró, en vez de conformarse.

> **La regla de «toda lámina de Adquisición lleva imagen» necesita este segundo filtro.** Sin él empuja justo a lo contrario de lo que pretende: a rellenar el hueco con lo primero que se relacione con el tema.
