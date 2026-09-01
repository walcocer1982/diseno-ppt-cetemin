# 05 — Diseño de la sesión (plantillas 003)

El **plan de la sesión** —no el PPT— vive en las plantillas 003. Es donde están las **actividades, el minutaje y los materiales** por momento. El PPT (004) es solo la proyección de este plan.

## Casos A y B según modalidad y tipo

| Plantilla | Modalidad | Tipo de sesión |
|---|---|---|
| **003A** | Sincrónica (**virtual**) | Adquisición |
| **003B** | Sincrónica (**virtual**) | Evaluación de colaborativo |
| **003C** | Dirigida (**presencial**) | Adquisición |
| **003D** | Dirigida (**presencial**) | Evaluación de colaborativo |

El contenido pedagógico (la ruta) es el mismo; cambia el soporte.

## Estructura de la plantilla de sesión de adquisición (003A/003C)

**Datos generales:** Carrera · Curso · N° horas · Instructor · Tipo de sesión · N° horas/bloques.

**Triangulación:** Indicador(es) de logro · Contenido (temario) · Evaluación.

**Ruta de aprendizaje** (tabla: Momento · Actividades formativas · Duración · Materiales y recursos):

| Momento | Qué ocurre (según la plantilla oficial) |
|---|---|
| **CONEXIÓN** | Se establece el logro de aprendizaje de la sesión · se activan saberes previos · se vincula el logro con los ámbitos de aplicación profesional |
| **ADQUISICIÓN** | Se construye el conocimiento (explicaciones, videos, lecturas) · se revisa un caso con guía del instructor · se resuelven dudas conceptuales |
| **APLICACIÓN** | Se pone en práctica en casos similares · se trabaja en equipos para indagar soluciones al caso, con acompañamiento |
| **DISCUSIÓN** | Se analizan las propuestas de solución · discusión guiada con preguntas de profundización que consoliden el conocimiento |
| **REFLEXIÓN** | Se reflexiona (individual/equipo) sobre qué y cómo se aprendió · se comparten aprendizajes y preguntas de cierre |

**Referencias bibliográficas:** Obligatoria · Recomendada.

> **La columna Duración es clave:** es el presupuesto de tiempo que garantiza cerrar la sesión (135 min) sin botar la reflexión. En las plantillas vacías viene "00 min" — llenarla bien es lo que corrige el error #8.

## Estructura de la plantilla de sesión de evaluación (003B/003D)

Mismos datos generales y triangulación. **Ruta de 3 fases** (Fase · Actividades · Bloque · Duración · Materiales):

| Fase | Qué ocurre |
|---|---|
| **PRESENTACIÓN DE TRABAJOS EN EQUIPO** | Los equipos sustentan su propuesta de resolución del caso planteado al inicio del bloque; deben evidenciar los conceptos de las sesiones previas |
| **RETROALIMENTACIÓN DEL INSTRUCTOR** | El instructor revisa, pregunta, comenta y sugiere mejoras; guía la participación de otros estudiantes |
| **REFLEXIÓN Y CIERRE** | Tras todas las presentaciones, se reflexiona sobre lo aprendido y se cierran preguntas |

No tiene adquisición: el trabajo ya se elaboró en el asincrónico previo (ver §06).

## El aprendizaje esperado manda sobre todo lo demás

Vale para EOM, PM y SI por igual. **Láminas, caso, criterios e imágenes existen para servir al aprendizaje esperado de la sesión.** Nada entra porque quede bien, porque llene un hueco o porque sobre espacio.

### Los puntos clave no se inventan para llenar láminas

Si una sesión necesita más diapositivas, se **desarrolla mejor** lo que ya está: un punto clave puede ocupar dos o tres láminas. Lo que no se hace es crear un punto clave por lámina.

> **Caso real.** La sesión 1 de EOM · Métodos de explotación tenía cuatro puntos clave. Al ampliar la Adquisición de 4 a 8 láminas se crearon **cinco puntos clave nuevos**, uno por lámina. Cuatro de ellos —el trazo, el jumbo, el jackleg, la secuencia de encendido— **eran partes de «Perforación» y «Voladura»**, no temas nuevos. Y al reescribir uno se perdió *«Perforación»* como punto clave: quedó sustituido por uno de sus detalles.

**Si una lámina no cabe bajo ningún punto clave existente, sobra la lámina — no falta un punto clave.**

### Agregar un concepto no está prohibido: está condicionado

La cadena tiene que cerrar **hacia arriba**:

```
concepto nuevo  →  ¿lo pide el caso para poder resolverse?
                →  ¿el caso sirve al aprendizaje esperado?
```

Si alguna respuesta es no, el concepto sobra. Y si el caso pide algo que el contenido no da, hay **dos** salidas legítimas: cambiar el caso, o pedir que se añada el contenido **y que el instructor líder lo apruebe**. Añadirlo por cuenta propia y seguir no es una de ellas.

> **El error de fondo fue de orden.** Se redactó el caso, de ahí salieron los criterios, uno de ellos evaluaba *el personal del frente*, ningún contenido lo enseñaba — y se creó el punto clave *«La guardia»* para sostenerlo. **El criterio también se había inventado**, y no servía al aprendizaje esperado, que dice *describir operaciones*, no *identificar personal*. El círculo se cerró sin que nada lo tocara desde fuera.

### Cómo se impide, no cómo se recuerda

| Mecanismo | Qué hace |
|---|---|
| **`origen` en `contenidos.csv`** | `oficial` (del temario de la triangulación) o `propuesto` (con quién lo aprobó y cuándo). Un punto clave sin origen es uno que alguien inventó |
| **Una lámina no puede crear contenido** | Si `laminas.csv` apunta a un `contenido_id` inexistente, es **error**. Ampliar láminas no puede tocar `contenidos.csv` |
| **Tope de 3 a 5 puntos clave por sesión** | Es lo que ya pedía el §07 para la triangulación. La sesión 1 llegó a nueve sin que nada avisara |
| **Cada criterio del caso señala su `contenido_id`** | Si señala uno `propuesto`, el caso se apoya en algo que no es del curso |

**La segunda es la única que bloquea; las demás avisan.**

## Rutinas de pensamiento — qué son y cuál va en cada momento

El §08 exige *"una rutina de pensamiento nombrada por momento"*, y esto es el repertorio para cumplirlo.

### Qué es una rutina de pensamiento

Una **rutina de pensamiento** es un procedimiento corto y repetible que obliga al estudiante a hacer visible cómo está razonando. Vienen del proyecto **Visible Thinking de Project Zero (Universidad de Harvard)**.

**Equivalencia de ingeniería:** es un *checklist de razonamiento*. Igual que un protocolo de arranque obliga a verificar en un orden fijo y evita que se salte un paso por confianza, una rutina obliga a pensar en un orden y evita que el estudiante se quede en "sí, entendí".

**Tres rasgos que las definen:**
1. **Pocos pasos**, siempre los mismos — se aprenden una vez y se usan todo el curso.
2. **Producen algo observable**: una frase, un dibujo, una posición tomada. Si no deja rastro, no es rutina.
3. **Se repiten** hasta volverse hábito. Usada una sola vez es una dinámica; usada siempre es una rutina.

> **Lo que NO es una rutina:** "el instructor pregunta y los estudiantes responden". Eso no tiene estructura ni deja evidencia, y es justo lo que el error #1 señala — *el estudiante mira, no piensa*.

### Las categorías oficiales

Project Zero agrupa sus rutinas en **ocho categorías** según para qué sirven: *core* (transversales), introducir y explorar ideas, profundizar en ideas, sintetizar y organizar ideas, investigar objetos y sistemas, toma de perspectiva, controversias y dilemas, y generar posibilidades y analogías.

Las cinco más usadas son **Circle of Viewpoints**, **See-Think-Wonder**, **Compass Points**, **Claim-Support-Question** e **I Used to Think… Now I Think…**

### Qué rutina va en cada momento de la sesión CETEMIN

El emparejamiento entre las categorías de Project Zero y nuestros 5 momentos es el siguiente. **Basta una por momento**; no se acumulan.

| Momento | Minutos | Qué se busca ahí | Rutinas que sirven (con su costo real) |
|---|---|---|---|
| **CONEXIÓN** | 20 | Sacar a la luz lo que el estudiante ya trae | **Veo–Pienso–Me pregunto 12'** · Pienso–Me intriga–Exploro 12' · Puntos cardinales 15' |
| **ADQUISICIÓN** | 45 | Que no se quede en escuchar | **¿Qué te hace decir eso? 0'** (se intercala) · Oración–Frase–Palabra 8' · Afirmación–Apoyo–Pregunta 12' |
| **APLICACIÓN** | 40 | Decidir con criterio y sostenerlo | **Tira y afloja 20'** · Ponerse dentro 15' · Semáforo 10' |
| **DISCUSIÓN** | 20 | Contrastar posiciones distintas | **Afirmación–Apoyo–Pregunta 0'** (estructura la exposición) · Círculo de puntos de vista 18' |
| **REFLEXIÓN** | 10 | Consolidar y hacer consciente el cambio | **Titular 4'** · Antes pensaba… ahora pienso… 7' · Conectar–Ampliar–Desafiar 10' |

### ⚠️ La rutina NO se suma al momento: lo estructura

Es el error de cálculo que hace que la sesión no cierre. Una rutina **no es una actividad extra que se agrega**: es **la forma de hacer** lo que el momento ya tenía que hacer.

| Mal cálculo | Cálculo correcto |
|---|---|
| Conexión 20' + Veo–Pienso–Me pregunto 12' = **32'** ✗ | Conexión 20' = Veo–Pienso–Me pregunto 12' + presentar objetivo y ruta 8' ✓ |
| Aplicación 40' + Tira y afloja 20' = **60'** ✗ | Aplicación 40' = Tira y afloja 20' (así se trabaja el caso) + resolver y redactar 20' ✓ |

Las que cuestan **0 minutos** son las que se intercalan sin ocupar bloque: *¿Qué te hace decir eso?* son 30 segundos cada vez que alguien afirma algo, y *Afirmación–Apoyo–Pregunta* es el formato en que el equipo expone, no un paso previo.

**Regla de presupuesto:** la rutina puede ocupar hasta **⅔ del momento**. Si necesita más, o el momento es demasiado corto o la rutina es demasiado ambiciosa para esa sesión.

**Los tiempos son para un grupo de ~25 estudiantes** e incluyen el trabajo individual **y** la puesta en común. Con grupos de 15 se recorta un tercio; el que se come el tiempo siempre es el compartir, no el escribir.

**Una rutina por sesión, no una por momento.** El §08 pide que cada momento tenga su dinámica nombrada, pero una rutina *completa* por momento no cabe en 135 minutos: serían 12+12+20+18+7 = 69 minutos solo de rutinas. En la práctica: **una rutina fuerte** (Conexión o Aplicación), **una de cierre** corta, y las de coste cero intercaladas.

### Cómo se ven en una clase de minería

**Veo–Pienso–Me pregunto** (Conexión). Se proyecta la foto de un frente después del disparo, sin rótulos. Cada estudiante escribe: qué *veo*, qué *pienso* que pasó, qué me *pregunto*. Separa observar de interpretar, que es exactamente lo que falla al leer un frente.

**¿Qué te hace decir eso?** (Adquisición). Cada vez que un estudiante afirma algo —*"ahí falta sostenimiento"*— el instructor pregunta qué se lo hace decir. Obliga a citar la evidencia, no la intuición.

**Tira y afloja** (Aplicación). Ante la selección de un método: de un lado las razones a favor del corte y relleno, del otro las del sublevel stoping. El equipo debe poner peso a cada lado antes de decidir. Es el §09–S11 del curso en formato de rutina.

**Antes pensaba… ahora pienso…** (Reflexión). Dos frases al cierre. Hace visible el cambio y le da al instructor evidencia real de si la sesión movió algo.

**Titular** (Reflexión). *"Si esta sesión fuera una noticia, ¿cuál sería el titular?"* Obliga a jerarquizar: qué fue lo esencial.

### Cómo se registra

En la plantilla **003**, columna *Actividades formativas*, la rutina va **nombrada**: `Veo–Pienso–Me pregunto (10 min)`, no *"se muestran imágenes y se pregunta"*. Nombrarla es lo que permite verificar el error #1: si la columna no tiene un nombre de rutina, la sesión no lo cumple.

> **Nota sobre la fuente:** las ocho categorías y los nombres de las rutinas son de Project Zero (Harvard). El emparejamiento con los 5 momentos de CETEMIN es propio de este proyecto: Project Zero clasifica por *propósito de pensamiento*, no por momento de clase.

## Lo que la matriz mejorada debe asegurar aquí

- Que cada momento tenga una **dinámica / rutina de pensamiento** nombrada (no "mostrar y preguntar") → corrige #1.
- Que la columna **Duración** sume 135 min y proteja reflexión/cierre → corrige #8.
- Que las actividades tracen al **aprendizaje esperado** → corrige #2 y #3.
