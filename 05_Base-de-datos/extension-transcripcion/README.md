# Extensión «Transcripción CETEMIN»

Un botón en el navegador que **guarda la transcripción del video que tienes abierto** en un archivo, listo para cargarlo con `videos_yt.py pegar`.

## Por qué existe

YouTube limita la descarga automática de subtítulos: la API y `yt-dlp` devuelven *429 · demasiadas peticiones* cuando se piden muchos seguidos. Comprobado el 7 de setiembre de 2026 — y el bloqueo es **por dirección de internet**, no por herramienta: las tres vías rebotan igual.

Pero cuando pulsas «Mostrar transcripción», **el texto ya está en tu pantalla**. YouTube ya te lo dio. Esta extensión lee eso y lo guarda.

> **No le pide nada a YouTube.** Por eso funciona aunque la IP esté limitada: no hay ninguna petición que bloquear. Y por eso tampoco gasta cuota.

## Instalar (una sola vez, unos 2 minutos)

1. Abre Chrome y entra a `chrome://extensions`
2. Arriba a la derecha, activa **«Modo de desarrollador»**
3. Pulsa **«Cargar descomprimida»**
4. Elige esta carpeta: `05_Base-de-datos\extension-transcripcion`
5. Aparece «Transcripción CETEMIN». Púlsala en el icono de piezas (🧩) de la barra y fija el alfiler para tenerla siempre a la vista

Si ves un aviso de que es una extensión de desarrollador, es normal: no está publicada en la tienda porque es de uso interno.

### Un ajuste de Chrome que conviene hacer

Entra a `chrome://settings/downloads` y **desactiva «Preguntar dónde guardar cada archivo»**.

Si no, Chrome abre un diálogo de «Guardar como» en cada video y hay que confirmarlo a mano. Con 180 videos, son 180 diálogos. Desactivado, el archivo cae solo y guardar pasa a ser **un clic de verdad**.

## Usar (unos 10 segundos por video)

1. Abre el video en YouTube
2. En la descripción, pulsa **«Mostrar transcripción»**
   *(si se te olvida, la extensión intenta abrirlo sola)*
3. **Si el video está en inglés y lo quieres en español:** en el panel de transcripción, cambia el idioma **antes** de guardar
4. Pulsa el botón de la extensión

Te avisa dónde quedó el archivo:

```
Descargas\cetemin-transcripciones\Epiroc-Underground-Mining_Room-and-pillar-mining-method_Oaxs7EEIp4k.txt
```

**Canal, título y el identificador del video al final.** El identificador tiene que quedarse —es la clave con la que `videos.csv` identifica el video, y dos canales pueden subir el mismo título—, pero puesto al final se lee de izquierda a derecha y reconoces el archivo sin abrirlo.

## Cargarlo al proyecto

```bash
python videos_yt.py pegar "C:\Users\<tu-usuario>\Downloads\cetemin-transcripciones\<archivo>.txt"
```

**No hace falta escribir el identificador:** el script lo saca de la cabecera del archivo. Si alguna vez quieres forzarlo, admite `pegar <id> <archivo>`.

A partir de ahí funciona todo lo demás sin tocar la red:

```bash
python videos_yt.py evaluar <id> --sesion EOM-...-S07
python videos_yt.py anexo   <id> --min 0:30-3:00
```

## El error fácil de cometer

**Copiar un video en inglés sin cambiar el idioma del panel.** El archivo sale en inglés, el anexo sale en inglés, y nadie se entera hasta que un estudiante lo lee.

Por eso el archivo guarda una línea `# pista:` con el idioma que estaba activo, y el aviso al terminar te lo recuerda. Si dice inglés y querías español, cambia el idioma y vuelve a pulsar — se sobrescribe.

## Qué hay en el archivo

Unas líneas de cabecera que empiezan por `#` —id, título, canal, idioma, fecha— y luego una línea por marca de tiempo. `videos_yt.py` ignora la cabecera y solo lee las líneas con hora.

**Ese archivo es material del canal.** Al cuadernillo no va tal cual: va una **síntesis nuestra** con marcas de tiempo. Es el mismo criterio que aplicamos a las normas ISO — se explica lo que dice, no se copia la fuente. Ver [§16](../../00_Base-de-conocimiento/16_RECURSOS-AUTONOMOS-Y-VIDEO.md).

## Si algo falla

Los mensajes distinguen entre los casos, que no son el mismo problema:

| Qué ves | Qué pasa | Qué hacer |
|---|---|---|
| «El panel está abierto pero YouTube no cargó el texto» | El video falló en servir su transcripción | Recarga con F5 y repite. Si sigue vacío, **es ese video**: pasa sobre todo con los que tienen doblaje automático. Cambia de video |
| «No se abrió el panel» | El clic no encontró o no abrió el panel | Ábrelo a mano con «Mostrar transcripción» y vuelve a pulsar |
| «Este video no ofrece transcripción» | El canal no puso subtítulos | Descártalo, o transcribe el audio con `faster-whisper` si vale mucho la pena |
| «No pude leer el texto» | YouTube cambió el diseño del panel | Avisa para ajustar la extensión |
| El texto sale destrozado | Subtítulo automático malo con vocabulario técnico | Busca otro video del mismo tema, o `faster-whisper` |

**Que un video falle no significa que el sistema esté roto.** Comprobado el 7 de setiembre: un video con doblaje automático devolvió el panel vacío, y el siguiente —de Epiroc— funcionó a la primera, con la IP igual de limitada.

## Antes de usarla, recuerda el orden del §16

> **Ver primero, guardar después.**

Buscar y ver candidatos en el navegador es gratis y descarta el 80 % en diez segundos. Solo se guarda la transcripción de los **dos o tres finalistas** de cada cuestionario.
