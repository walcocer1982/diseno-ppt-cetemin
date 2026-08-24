# Bitácora del prompt

El prompt se mejora en **loop**: se lanza, se mide, se ajusta. Aquí queda **por qué** está cada línea y qué pasó al medirla — incluidas las hipótesis que fallaron.

> **Regla:** antes de quitar una línea de este prompt, búscala en esta tabla. Casi todas están porque algo falló sin ellas. La única línea que se quitó sin costo fue de estilo; las que resuelven ambigüedades del dibujo fuente son irrenunciables.

## El prompt vigente (95 palabras)

```
Redibuja esta imagen fiel al original.
{vista}
El dibujo mide {ratio} veces mas de ancho que de alto: respeta esa proporcion.

Hazla achurada y a color: cada tipo de componente con su propio color y su
propio achurado.

Elimina las lineas de medida, las lineas que forman los angulos, los valores
de los angulos y las medidas horizontales y verticales. Elimina tambien los
logotipos y el texto que no se haya pedido conservar.

Dibuja sobre fondo blanco.
```

Solo cambian `{vista}` y `{ratio}`, declarados por cada dibujo. **La línea de vista es donde se dice qué conservar**, porque eso depende del tipo de imagen: en una máquina la cota es ruido de catálogo, en un plano es el dato.

## Qué se probó y qué pasó

| Cambio | Por qué se hizo | Resultado medido |
|---|---|---|
| Prompt largo → corto (430 → 52 palabras) | Pedido de simplificar | Planta **mejoró**: desvío 3,2 % contra 6,4 % del largo |
| Quitar la línea de proporción | Venía en la simplificación | **Falló**: perfil dio 1,93–2,40 contra control 4,18. Sin ella el modelo llena el lienzo |
| Devolver `{ratio}` | Recuperar la proporción | Perfil volvió a 4,44–4,57. **Aprobado** |
| Exigir "las CUATRO ruedas" en planta | Creí que faltaban ruedas | **Error mío**: la carrocería las tapa en el catálogo. Pedía inventar |
| "SOLO las ruedas que el dibujo deja ver" | Corregir lo anterior | El modelo ya era fiel; la instrucción errónea era la mía |
| "una sola posición (transporte)" | El catálogo dibuja transporte **y** descarga | Sin ella: 3 intentos fallidos, aspecto 2,1 vs 4,18. Con ella: aprobado al primero |
| "elimina logotipos y texto" | Salían la marca Epiroc y "ST14 SG" en una **silueta** | Corregido: el §10 exige silueta sin marca |
| Lienzo configurable por vista | La chancadora en perfil es casi cuadrada (1,06) | Antes se asumía que todo perfil es alargado |
| "conserva los niveles" (planos) | Se perdían NV-4560…NV-4700, que **son** el dato | Recuperados, aprobado en intento 2 |
| "texto que no se haya pedido conservar" | La línea anterior contradecía "elimina el texto" | Contradicción resuelta antes de lanzar |

## Hipótesis descartadas

**Detectar reportes de instrumentación por oscilación por fila.** Supuse que una señal registrada cruzaría el papel más veces que un dibujo. Medido: el plano de la Mina Chupa da **81 cruces/fila** y los reportes de vibración 16–38. Al revés de lo previsto. La métrica sigue calculada en `buscar_planos.py` pero no clasifica.

**Capa de labor dibujada por código** (`_descartado/labor.py`). Funcionaba y era métricamente exacta —el alto del equipo daba 2 603 mm contra 2 601 del catálogo— pero se descartó: las imágenes salían mejor sin piso ni paredes.

## Las contradicciones son el error recurrente

Tres veces en una sesión el prompt acabó pidiendo dos cosas opuestas:

1. "borra los arcos de radio de giro" + "dibuja la trayectoria como arcos discontinuos"
2. "conserva los niveles" + "elimina el texto"
3. "una sola pieza continua" + "cada pieza con su color"

El modelo resuelve una contradicción **omitiendo ambas instrucciones**. Al añadir cualquier línea, releer el prompt completo buscando qué contradice.

## Variante: solo mejorar calidad

Para planos existe `PROMPT_CALIDAD`, que **no redibuja**: solo limpia el escaneo. Son 16 palabras:

```
Mejora la calidad de esta imagen.

Que sea una copia fiel: no cambies nada del dibujo.
```

Dio el mejor resultado métrico de toda la sesión: **1,32 contra un control de 1,33**, aprobado al primer intento. Conserva grilla, cotas, rótulos de zona, `CHIMENEA`, `TR3`, `CT-455` y el recuadro de título.

### El límite: el modelo reescribe el texto

Probado con dos versiones del prompt —60 palabras y 16—, ambas pidiendo explícitamente no cambiar nada:

| Original | Copia |
|---|---|
| TAJEO 326 VACIO | **TAJCO** 326 VACIO |
| DERRUMBE | **DESPLUME** |
| 0.8MPO | 0.8**x**PO |
| NV-4675 | NV-467**0** |

**No es un problema de prompt: es del modelo.** No copia píxeles, regenera la imagen, y al regenerar reinterpreta cada glifo. Ninguna instrucción lo evita.

> **Regla:** la IA sirve cuando el plano **ilustra un concepto**. No sirve cuando el **dato escrito importa** — ahí va el escaneo original citado. Si igual se usa la versión mejorada, hay que verificar los rótulos uno por uno.

## Por tipo de imagen, no por carrera

El prompt no se bifurca por carrera: un molino de PM y un scooptram de EOM se dibujan igual. Lo que cambia es el **tipo**:

| Tipo | Qué necesita |
|---|---|
| Máquina móvil | proporción · vista · una sola posición |
| Equipo fijo | proporción · vista |
| Corte seccionado | partes internas · sin proporción oficial |
| Plano de labor | conservar niveles y rótulos · o `PROMPT_CALIDAD` |
| Diagrama de proceso | **no pasa por el modelo** — Mermaid/D2 |

**SI queda fuera de este pipeline:** sus imágenes (señalética, EPP, layouts, secuencias de procedimiento) no parten de un catálogo ni tienen cotas contra las cuales verificar. Necesita otro camino, aún por definir.
