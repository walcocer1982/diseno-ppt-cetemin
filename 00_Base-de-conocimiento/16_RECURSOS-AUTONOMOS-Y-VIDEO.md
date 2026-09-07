# 16 — El recurso de aprendizaje autónomo (y el video)

Qué trabaja el estudiante en el bloque asincrónico, antes de las sesiones que ese bloque prepara. Es el material del que salen las preguntas del **Cuestionario de Verificación**, y por eso su calidad decide la del CV.

Este documento reemplaza a lo que hasta el 7 de setiembre de 2026 vivía dentro del docstring de `generar_recursos.py`. **La doctrina vive aquí; los scripts apuntan a este documento y no lo repiten** — cuando el mismo criterio está escrito en dos sitios, se desincronizan en silencio (fue exactamente lo que pasó con el «dos CV al 5 %» del §14).

## El presupuesto, que no se negocia

> **135 min = 90 de recurso + 45 de cuestionario.**

Los 135 son un bloque asincrónico completo (§02). Los cuatro CV en los cursos de 96 h y los dos en los de 48 bajan del **sílabo oficial de admisiones 2024**, que ya los traía al 2,5 % cada uno. No son decisión nuestra y no se tocan.

## El reparto de los 90 lo decide el instructor líder

Y esto sí es decisión nuestra, tomada el 7 de setiembre de 2026.

No hay proporción obligatoria entre lectura, video y autoevaluación. **La pone quien conoce el tema, CV por CV.** Un cuestionario sobre cláusulas ISO puede ser casi todo texto; uno sobre métodos de explotación, mitad video. Un CV puede no llevar video si el tema no lo pide, y otro llevar tres.

Lo único que se verifica es que **los minutos declarados sumen 90**. Es la misma disciplina de la columna Duración del plan de sesión (§05): el presupuesto se respeta, el contenido lo pone el diseñador.

### Por qué se escribió esto

Hasta hoy el §02 decía que el asincrónico era *«lectura previa al CV»*. Esa palabra hizo que el primer curso completo —SI-SGCSSMA— saliera con 90 minutos de texto corrido y nada más. **El instructor no se equivocó: siguió lo que la doctrina decía.**

Y la doctrina estaba mal, porque la plantilla oficial de CETEMIN se llama **«lista de recursos de aprendizaje autónomo» (003B)** — en plural, y sin mencionar la lectura. El video siempre cupo en el sistema oficial. Lo que faltaba era el procedimiento para llenarla, que es este documento.

## El video como fuente, no como adorno

**Las preguntas del CV pueden salir del video.** Para que eso sea legítimo hacen falta dos condiciones.

### 1. El video queda respaldado por una síntesis nuestra

Si el canal borra el video a mitad de ciclo, el estudiante no se puede quedar sin fuente. Por eso cada video lleva en el cuadernillo un **anexo con marcas de tiempo** que dice qué muestra en cada tramo.

Ese anexo es **una síntesis nuestra, no la transcripción literal**. El material es del canal, y aquí manda el mismo criterio que el CV1 aplicó a las normas ISO: se explica lo que dice, no se copia la fuente.

El anexo es además lo que conserva la regla dura del CV:

> Toda pregunta de un CV tiene que poder contestarse **con el cuadernillo y con nada más**.

Con el anexo dentro del cuadernillo, esa regla sigue cumpliéndose aunque el video desaparezca.

**Los rótulos que aparecen en pantalla no están en la transcripción.** «Bolting», «Haulage level» y demás son palabras que el video muestra pero no dice. Se anotan a mano al verificar, o el anexo sale incompleto.

### 2. La pregunta cita el minuto exacto

La columna `fuente` de los bancos absorbe el cambio sin tocar el esquema: donde hoy dice `Cuadernillo CV1 · 1.1`, dirá `Video V-012 · 08:42`.

**El minuto es obligatorio.** Si no se puede señalar, la pregunta no sale del video y se borra. Es lo que permite revisar el banco dentro de un año sin volver a discutirlo.

## Los tres criterios de admisión

| | Criterio | Por qué |
|---|---|---|
| 1 | **Tramo ≤ 15 min** | El *tramo asignado*, no el video entero. De una clase de tres horas se puede recortar un buen tramo de ocho minutos; lo que no cabe en el presupuesto es la clase entera |
| 2 | **Predominio visual** | Animación producida, no clase grabada. Si va a ser alguien hablando, ya tenemos la lectura |
| 3 | **Transcripción utilizable** | Sin transcripción limpia no hay anexo, y sin anexo no hay preguntas |

### Cómo se mide el predominio visual

Contando **deícticos**: «aquí vemos», «en esta figura», «como se observa», «as you can see». Un narrador que dice «aquí vemos» está señalando una lámina. Un guion escrito para animación no lo necesita.

Medido el 7 de setiembre de 2026 sobre candidatos reales de métodos de explotación:

| Video | Duración | Deícticos |
|---|---|---|
| Epiroc · Room and pillar | 3 min | **0** |
| Epiroc · Cut and fill | 3 min | **0** |
| Epiroc · Sublevel stoping | 3 min | **0** |
| Clase con diapositivas (ES) | 16 min | 26 |
| Clase entera (ES) | 123 min | 140 |

**Umbral: más de 2 deícticos por cada 10 minutos → probable clase grabada, se descarta.**

Es indicio para descartar rápido, **no prueba**. Vale lo mismo que en el §10: medir sirve para lo que el número caza; lo que no caza —la calidad de la animación, los rótulos, piezas de más o de menos— se ve mirando el video.

### La transcripción se comprueba, no se supone

El subtítulo automático de YouTube destroza el vocabulario técnico. Casos reales medidos el mismo día:

- Un video de 87 minutos sobre corte y relleno convertía *cut and fill* en algo irreconocible, cientos de veces. A ojo el video parecía perfectamente bueno.
- La reedición de Epiroc transcribe *«cut and film»* y *«or bodies»*; el original de Atlas Copco de 2016 los escribe bien. **Entre dos versiones del mismo video, manda la que tenga mejor subtítulo.**
- Un video excelente de fabricante tenía subtítulos **solo en ruso**. Sin anexo posible.

Cuando la transcripción no sirva y el video valga la pena, se transcribe el audio con **`faster-whisper`**. Los errores recurrentes se corrigen con el glosario de `videos_yt.py`, **antes** de que el texto llegue al cuadernillo: un error aquí viaja al banco de preguntas y de ahí al estudiante.

### El idioma no es obstáculo

YouTube traduce los subtítulos automáticos, y la API los sirve ya traducidos. Un video en inglés con buena animación vale más que una clase grabada en español.

## Verificación: igual que las imágenes

**Ningún video entra a un cuadernillo sin estar `verificado`** en `videos.csv`, con `verificado_por` y fecha.

El script **mide, no aprueba**. Imprime señales para descartar rápido y contrasta el vocabulario del aprendizaje esperado contra la transcripción. Quien firma es el **instructor líder**, después de ver el video.

### El catálogo es compartido

`videos.csv` va en la **raíz** de `05_Base-de-datos/`, junto a `imagenes.csv` y `equipos.csv` — no en la carpeta de cada carrera. Un video de gestión de riesgos que verifique SI lo enlaza EOM sin volver a verificarlo. Las tres carreras comparten temas, y ese reuso es lo que hace manejable el volumen.

Las **transcripciones crudas no se versionan**: son material del canal y son regenerables. Van a `01_Insumos/transcripciones/`, fuera de Git. Al repositorio van `videos.csv` —la verificación, que es lo que se comparte— y la síntesis dentro del cuadernillo.

## YouTube bloquea por IP: cómo se trabaja sin que pase

El bloqueo **no lo causa el volumen real** —los videos se bajan una sola vez en la vida—, lo causa la exploración: veinte consultas en dos minutos parecen un robot. Ocurrió el 7 de setiembre de 2026 probando candidatos, y de ahí salió este procedimiento.

Como el bloqueo es **por dirección IP** y cada instructor trabaja desde su máquina, la cuota va **por instructor**: es la unidad exacta que YouTube cuenta, y si uno la agota los otros dos siguen trabajando.

### La regla que más ahorra no está en el código

> **Ver primero, bajar después.**

1. **Buscar y ver en el navegador.** Gratis, sin API. Ahí se descarta el 80 %: en diez segundos se ve si es animación o si es alguien hablando frente a diapositivas.
2. **Mirar si `videos.csv` ya lo tiene** verificado por otro instructor.
3. **Solo entonces bajar la transcripción**, y únicamente de los dos o tres finalistas.

Con ese orden, un CV completo cuesta **3 o 4 consultas**, no 20.

### Las defensas del script

| | Medida |
|---|---|
| 1 | **Caché obligatoria** — nada se pide dos veces |
| 2 | **Una pasada por video** — pistas, transcripción y traducción se resuelven juntas |
| 3 | **Cuota de 20 consultas al día** por instructor |
| 4 | **Pausa de 3–6 s** con variación aleatoria |
| 5 | **Freno duro al primer bloqueo** — insistir alarga la sanción |

### Cuando aun así bloquee

```bash
yt-dlp --write-auto-subs --sub-langs "es,en" --skip-download <URL>
```

O el botón **«Mostrar transcripción»** de la propia página de YouTube, que funciona siempre, y luego `python videos_yt.py pegar <id> <archivo.txt>` — que no toca la red.

### El camino manual, en un clic

Ese paso manual está automatizado en `05_Base-de-datos/extension-transcripcion/` — un botón de Chrome que lee el panel ya abierto y guarda el archivo con el formato que espera `pegar`.

**No hace ninguna petición a YouTube**, porque el texto ya está en la pantalla. Por eso funciona con la IP limitada y no gasta cuota. Instrucciones de instalación en su [README](../05_Base-de-datos/extension-transcripcion/README.md).

> **El error fácil:** guardar un video en inglés sin cambiar el idioma del panel. El archivo, el anexo y el cuadernillo salen en inglés, y nadie se entera hasta que un estudiante lo lee. Por eso el archivo registra la pista activa en su cabecera.

**No correr esto desde una VM en la nube:** esos rangos están bloqueados de entrada.

### Lo comprobado el 7 de setiembre de 2026

Con la IP ya limitada, se midió qué pasa por cada vía:

| Vía | Resultado |
|---|---|
| `youtube-transcript-api` | **429** · demasiadas peticiones |
| `yt-dlp` subtítulos | **429** · la misma puerta |
| `yt-dlp` audio | **403** |
| `yt-dlp` + *impersonation* | **403** igual |
| Portada de YouTube y datos del video | **200**, normal |
| Navegador y panel de transcripción | Perfecto |

**No es la herramienta, es la IP**, y es temporal: 429 significa «ahora no», no «esto no se puede». Conviene reintentar el camino automático de vez en cuando —cuando funciona es gratis e instantáneo—, pero no se puede depender de él. **Por defecto se trabaja con la extensión.**

Cambiar de herramienta no resuelve nada: todas golpean los mismos servidores. Y no se paga por proxies — se alquilarían direcciones de internet para no parecer un robot al pedir un texto que la propia página muestra gratis.

## La herramienta

`05_Base-de-datos/videos_yt.py`

| Subcomando | Qué hace |
|---|---|
| `bajar` | Baja y cachea la transcripción, con traducción al español si hace falta |
| `evaluar` | Señales de admisión + contraste con el aprendizaje esperado de una sesión |
| `anexo` | Borrador de la síntesis con marcas de tiempo, para reescribir |
| `pegar` | Carga una transcripción copiada de YouTube, sin tocar la red |
| `revisar` | Comprueba que los enlaces registrados sigan vivos |
| `cuota` | Cuántas consultas quedan hoy |

**`revisar` se corre antes de cada ciclo.** Un video que el canal borró deja el CV cojo, y hay que enterarse con tiempo de reemplazarlo, no cuando un estudiante reclama. Por eso también conviene **más de un video por tema y de distinto canal**: si uno cae, el tema sigue cubierto.

## Dónde entra en el orden de trabajo

El recurso autónomo se diseña **junto con el cuadernillo, no después**. El CV1 se responde antes de la sesión 1, así que su recurso tiene que existir antes de que el curso empiece. Ver §13.

## Lo que hay que mirar de frente

**El volumen real.** 35 cursos TP dan **90 cuestionarios**; a dos videos cada uno, del orden de 180 videos que alguien tiene que ver y firmar. El script baja una transcripción en dos segundos, pero **la verificación no la hace el script**. El cuello es humano, y el reuso del catálogo compartido es lo que lo alivia.

**No se registran videos sin verificar.** 180 filas sin firmar en el catálogo son 180 mentiras esperando turno.

---

*Levantado el 7 de setiembre de 2026, después de que el primer curso completo (SI-SGCSSMA) saliera con recursos autónomos de solo lectura y de medir ocho candidatos reales de video para EOM.*
