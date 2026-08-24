# Plantilla oficial del PPT de sesión

**`PLANTILLA-CETEMIN_sesion.pptx`** es el **archivo base** del que sale todo PPT de sesión. No se edita para una clase: se **copia**, se le añaden las diapositivas y se guarda con otro nombre.

Está vacía a propósito — **0 diapositivas, 6 patrones y 16 diseños**. Lo que aporta es la marca: fondos, escuadra amarilla, logo, tipografía y colores ya colocados.

> En PowerPoint esto se llama **plantilla** (o *patrón de diapositivas*). Es lo que evita reconstruir el diseño cada vez.

## El color

El azul de marca se unificó al **`#0D2632`** de la tapa institucional — un azul petróleo, más verdoso que el `#082848` que traían los PPT antiguos.

Se recolorearon las imágenes de fondo de los patrones **conservando la luminosidad de cada píxel**, no aplanando el color: así se mantienen sombras y relieve del logo. Solo se tocaron los píxeles azul oscuro; el amarillo, el blanco y las acreditaciones quedaron intactos.

Por eso el cambio afecta a todas las diapositivas de una vez: la banda superior de las de contenido, el panel del tipo tema, las subportadas y la tapa interna.

## Qué diseño usa cada tipo de diapositiva

| Tipo | Diseño | Qué lleva |
|---|---|---|
| **Portada** | `slideLayout3` + `fondos/01_portada.jpg` | Nombre del **curso** donde el original decía "Reporte semanal", y `SEDE ABQ` en ámbar debajo |
| **Subportada de sesión** | `slideLayout2` | Dos columnas con barra amarilla en `x=6.13`: Unidad Didáctica a la derecha, Sesión N° y tema a la izquierda, ícono grande abajo |
| **Subportada de momento** | `slideLayout3` + fondo `#0D2632` | Ícono en `x=5.62 y=1.83` (2,08″) y **una sola palabra a 80 pt** en `y=4.43` |
| **Triangulación** | `slideLayout2` | Tres zonas: aprendizaje arriba, puntos clave e izquierda, evaluación a la derecha, ícono al centro |
| **Tema** | `slideLayout6` «TITLE» | Panel oscuro con título en `x=0.43 y=2.75` e imagen en `x=7.01 y=2.01` (5,82″) |
| **Contenido** | `slideLayout13` | Título centrado en `y=0.88` y cuerpo debajo |
| **Tapa** | `slideLayout3` + `fondos/03_tapa.jpg` | Logo, QR y redes. Fija |

**Portada y tapa son fijas y obligatorias** en toda presentación.

## Reglas al generar

1. **Copiar la plantilla, nunca editarla.**
2. **Borrar los placeholders heredados** antes de colocar contenido, o sale *"Haga clic para agregar título"* sobre la diapositiva.
3. Al vaciar un PPTX hay que **soltar la relación** de cada diapositiva, no solo quitarla de la lista: si no, las viejas se quedan dentro y el archivo pasa de 2 a 41 MB.
4. Tipografía **Oswald** en títulos (condensada bold). Si no está instalada, PowerPoint la sustituye y se pierde el carácter.

## Referencia

`03_Entregables-diseño/EOM-Metodos-de-explotacion/EJEMPLO_Sesion-01_v2.pptx` — la sesión 1 completa en 16 diapositivas, hecha con esta plantilla.
