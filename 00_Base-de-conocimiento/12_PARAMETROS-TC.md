# Parámetros para definir un Trabajo Colaborativo

> **Para quién.** Los tres instructores líderes —EOM, PM, SI—. Sirve para los **70 TC** del programa (35 cursos × 2), no solo para Métodos de explotación.
>
> **De dónde sale.**
> - Latorre Ariño, M. (2018). *Destrezas, procesos mentales y técnicas metodológicas · Metodología activa*. Universidad Marcelino Champagnat, Lima.
> - Cobo Gonzales, G. y Valdivia Cañotte, S. (2017). *El estudio de casos*. Instituto de Docencia Universitaria, **PUCP**. ISBN 978-612-47489-1-2. Ver `00_Base-de-conocimiento/06_casos-rubricas-evaluacion.md`.
> - Las reglas propias de CETEMIN (§06, §08).

---

## La fórmula

Latorre define una actividad de aprendizaje así:

```
ACTIVIDAD = DESTREZA + CONTENIDO ESPECÍFICO + TÉCNICA METODOLÓGICA + ACTITUD
                                                                   (mini-competencia)
```

**Un TC es una actividad grande.** Si le falta cualquiera de los cuatro, no se puede evaluar bien:

- sin **destreza** → no se sabe qué habilidad mental se está desarrollando
- sin **contenido** → es un ejercicio vacío
- sin **técnica metodológica** → el estudiante no sabe *cómo* hacerlo
- sin **actitud** → no hay nada colaborativo, solo trabajo repartido

La técnica metodológica se reconoce porque entra con un conector: *a través de, por medio de, mediante, haciendo, utilizando, siguiendo*.

---

## Los 14 parámetros

| # | Parámetro | Qué responde | Dónde vive hoy |
|---|---|---|---|
| 1 | **Destreza** | qué habilidad mental desarrolla | ⚠️ no se registra |
| 2 | **Procesos mentales** | los pasos de esa destreza | ⚠️ no se registra |
| 3 | **Contenido específico** | sobre qué material | `casos.csv · descripcion` |
| 4 | **Técnica metodológica** | cómo lo hace el estudiante | ⚠️ implícito en `producto` |
| 5 | **Actitud** | qué conducta colaborativa exige | ⚠️ implícito en los roles |
| 6 | **Indicador** | qué se evalúa | `casos.csv · indicador_id` |
| 7 | **Bloque y sesiones** | cuándo se dan pautas y cuándo se sustenta | `casos.csv · bloque_id` |
| 8 | **Producto** | qué entrega, con qué formato y duración | `casos.csv · producto` |
| 9 | **Roles** | de qué responde cada integrante | `casos.csv · producto` |
| 10 | ~~Variantes A / B~~ | **no aplica al colaborativo** — ver §13 | solo en casos de sesión |
| **11** | **Formato narrativo** | el caso se cuenta como historia, no como ficha | ⚠️ no se registra |
| **12** | **Entregable real de mina** | qué documento de trabajo entrega | ⚠️ no se registra |
| **13** | **Fuente real** | de qué tesis salen los datos | ⚠️ no se registra |
| **14** | **Presupuesto de tiempo** | 2 h · 4 estudiantes | ⚠️ no se registra |

**Nueve de los catorce no se registran en ninguna parte.** Es el hallazgo principal de este documento: hoy la destreza y la fuente de un TC viven en la cabeza de quien lo redactó.

---

## Las cuatro reglas de redacción

Son las que más cuesta cumplir y las que más se notan cuando faltan.

### 1 · Se escribe como historia, en párrafos corridos

Nada de viñetas, fichas técnicas ni datos en tabla dentro del enunciado. El estudiante tiene que **extraer** la información del relato, igual que en la mina la saca de lo que ve y de lo que le cuentan.

Con los datos ordenados en viñetas, el alumno se salta los tres primeros pasos de *Identificar* —percibir, reconocer características, relacionar con lo que sabe— y solo ejecuta el cuarto. **El formato del enunciado decide qué procesos mentales se activan.**

### 2 · Los datos técnicos van sí o sí

Que sea narrativo **no significa vago**. Cuando el relato describe la veta, tienen que estar la forma, la potencia, el rumbo, el buzamiento, el RMR, la longitud y la ley. Sin cifras no hay nada que reconocer.

La diferencia está en **dónde** aparecen: repartidos en la conversación y en el orden en que un jefe de mina los diría, no en una ficha ordenada.

### 3 · El riesgo y la incertidumbre nunca se rotulan

**No se escribe «Lo que está en juego», «La incertidumbre», «El riesgo».** Si se rotula, el estudiante lee la etiqueta y deja de buscar.

Van **dentro de la historia**, como iría en la vida real:

| En vez de rotular… | Se cuenta |
|---|---|
| «Lo que está en juego: caída de rocas» | *«El mes pasado un equipo hizo el requerimiento mirando solo la primera hoja del informe. Se cayó una caja en el tajeo cuatro. No hubo gente debajo de milagro.»* |
| «La incertidumbre: hay dos valores de RMR» | *«Le dio RMR 41 y lo clasificó Clase III. Al pie, escrito a mano, una corrección: menos cinco. RMR 32. Al costado, subrayada, la palabra "incompetente".»* |

El riesgo se cuenta como **anécdota**; la incertidumbre, como **detalle contradictorio** que el relato deja pasar sin comentario.

### 4 · Nunca se nombra la respuesta

Si el caso pide identificar el método, **el relato no dice el nombre de ningún método** — describe cómo se trabaja. Y tampoco se advierte al estudiante que no lo va a encontrar: eso también es rotular.

---

## Las tres características PUCP de un buen caso

| | Qué exige | Cómo se comprueba |
|---|---|---|
| **Realismo** | *«el caso debe presentar una situación relevante propia de la carrera»*. Ayudan las especificaciones técnicas, los personajes y los detalles | ¿hay cifras reales, un jefe de mina con nombre, un plano sobre la mesa? |
| **Incertidumbre** | *«permite distintas soluciones entre las cuales es válido el debate»* | **si tiene una sola respuesta correcta, no es caso: es ejercicio** |
| **Riesgo** | *«las decisiones impactarán, aunque sea de manera ficticia, en la salud, el bienestar o la supervivencia»* | ¿qué se pierde si lo hacen mal? |

### Cómo se formula: empezar por la respuesta

Antes de redactar nada, **escribir el guion de lo que el estudiante debe decir al exponer**, con sus palabras:

```
GUION ESPERADO
   ↓ ¿qué necesita saber para decir esto?   → el contenido de la Adquisición
   ↓ ¿qué necesita ver?                     → las imágenes que hacen falta
   ↓ ¿qué situación lo obliga a decirlo?    → el caso
   ↓ ¿qué comprueba que lo dijo bien?       → los criterios
```

**Por qué en ese orden:** el caso escrito primero tiende a pedir lo que suena interesante, no lo que el estudiante puede responder con lo enseñado. Escribir la respuesta primero deja a la vista lo que falta enseñar.

> **El reto está en reconstruir, no en subir de nivel.** Un caso puede ser exigente sin salirse del verbo del indicador: *identificar* un método que nadie nombró, a partir de la evidencia, es difícil y sigue siendo identificar. Subir a *diagnosticar* o *recomendar* no lo hace más retador — lo hace inevaluable.

---

## El anclaje en fuente real

**Los datos no se inventan.** Cada TC se arma sobre una **mina real descrita en una tesis de repositorio peruano** — UNAP, UNSAAC, UNI, UNCP, UNDAC, PUCP, ALICIA-Concytec.

**Pero la mina no se nombra en el enunciado.** Si se nombra, el estudiante busca la tesis y encuentra la respuesta en dos minutos. El relato usa los datos reales sobre una mina sin identificar —*«una mina aurífera del sur de Ica»*—.

**La tesis se revela al cerrar la sustentación**, y ahí cambia de función: deja de ser la respuesta y pasa a ser la **comprobación**.

> «Todo lo que leyeron es real. Es la veta Farallón de la mina SMRL Las Bravas N°2. Ábranla y comparen su reporte con lo que dice la tesis. Donde no coincidan, expliquen por qué.»

**Elegir tesis con tensión.** Las mejores son las que documentan un **cambio de método** o un **trade-off** entre dos: traen la incertidumbre incorporada, sin que haya que fabricarla.

**Verificar la fuente antes de usarla.** Una tesis real tiene inconsistencias. La de la veta Farallón da el buzamiento como 45°, 55° y 60° en tres lugares distintos. Se elige uno, se declara cuál, y **se le dice al estudiante al final** — aprender a contrastar una fuente es parte del trabajo.

---

## El presupuesto de tiempo

**2 horas · 4 estudiantes.** Es la restricción dura, y el reparto típico:

| | min |
|---|---|
| Leer el relato y extraer los datos | 15 |
| Reconocer / razonar lo que pide el caso | 20 |
| La decisión central del caso, con su justificación | 20 |
| Llenar el entregable | 18 |
| La complicación secundaria | 12 |
| Armar las láminas | 25 |
| Ensayar con roles | 10 |
| **Total** | **120** |

**Dónde se pierde el tiempo:** llenando celdas en blanco. Escribir quince casillas de texto libre es volumen, no dificultad — se lleva media hora y no exige nada.

**La solución: que se llene marcando, no escribiendo.** Entregar la **lista de almacén con distractores** —jumbo y jackleg, pernos y puntales, malla y shotcrete— y que marquen lo que corresponde. Reconocer entre distractores es más exigente que escribir en blanco, es lo que se hace de verdad en almacén, y libera unos doce minutos para la parte que sí piensa.

**Y la regla al revisar el caso:** si la suma pasa de 120, no se agrega exigencia — se **redistribuye**. Se recorta transcripción y se profundiza la decisión.

---

## Ejemplo trabajado · TC1 de Métodos de explotación

| Parámetro | Cómo se resolvió |
|---|---|
| **Destreza** | Identificar |
| **Procesos** | percibir → reconocer características → relacionar con lo previo → nombrar |
| **Contenido** | método aplicado + ciclo de minado + clase de roca |
| **Técnica** | reconociendo el método a partir de cómo se describe el trabajo en el relato |
| **Actitud** | cada integrante responde por su parte ante el equipo |
| **Indicadores** | IND-1 e IND-2 |
| **Narrativo** | siete párrafos, con diálogo del jefe de mina |
| **Entregable** | reporte de reconocimiento de labor + requerimiento de guardia |
| **Fuente** | Incacutipa Mamani (2019), UNAP — revelada al cerrar |
| **Tiempo** | 120 min, con requerimiento por marcado |

**El guion esperado** *(se escribe primero)*: «La veta es angosta, 1,30 m, tabular, inclinada 55°. La roca dio RMR 41, Clase III regular, pero corregida baja a 32, Clase IV mala. Con esa roca y ese ancho no se puede dejar el tajeo abierto: hay que rellenar cada corte antes de subir. Por eso es corte y relleno ascendente, aunque la labor estuviera preparada para almacenamiento provisional…»

**Cómo quedó el riesgo, sin rotular:** *«El mes pasado un equipo hizo el requerimiento mirando solo la primera hoja del informe del geólogo. Se cayó una caja en el tajeo cuatro. No hubo gente debajo de milagro.»*

**Cómo quedó la incertidumbre, sin rotular:** dos valores de RMR en el mismo informe, una labor preparada para un método y trabajada con otro, y una bolsonada donde la veta se abre a 2,00 m cuando el resto del tajeo va a 1,30.

---

## Las reglas duras de CETEMIN

No son criterio del instructor: son constantes del sistema.

| Regla | Por qué |
|---|---|
| **Exactamente 5 criterios de rúbrica × 4 puntos = 20** | con 4 criterios el máximo sería 16 y con 6, 24: la nota deja de ser vigesimal |
| **Los criterios pesan igual** | no hay ponderación; ponderarlos rompe la escala |
| **Criterios 4 y 5 son literales** en los 70 TC | `Presentación PPT: contenido y diseño` · `Presentación oral: dominio y claridad` |
| **Los criterios 1–3 los nombra el caso** | siguen el recorrido entender → resolver → interpretar |
| **La rúbrica no puede pedir más que el indicador** | si el indicador dice *identifica*, la rúbrica no califica *recomienda* |
| **Un rol por integrante** | la nota es del equipo, pero cada uno responde por su parte |
| **El colaborativo NO lleva variantes** | un solo caso para toda la clase: es la evaluación del bloque y todos rinden sobre lo mismo. Las variantes A y B son de los **casos de sesión** (§13) |
| **Sin costos ni productividad** en EOM | no hay curso previo de matemática ni economía (`OBS-13`) |

---

## Las destrezas, con sus procesos mentales

Los procesos mentales **no son opcionales**: son los pasos que el estudiante recorre. Si el caso no los permite recorrer, la destreza no se desarrolla.

**Identificar** — *reconocer las características esenciales de algo. Para identificar hay que conocer previamente.*
1. Percibir la información de forma clara → 2. Reconocer las características → 3. Relacionar con los conocimientos previos → 4. Señalar, nombrar

**Ubicar-localizar** — *determinar el emplazamiento de algo.*
1. Percibir → 2. Identificar variables de localización → 3. Aplicar convenciones → 4. Identificar lugares y hechos

**Describir** — *explicar de forma detallada las partes y características de un objeto.*
1. Percibir con claridad → 2. Seleccionar partes esenciales → 3. Ordenar la exposición → 4. Describir con lenguaje apropiado

**Comparar** — *cotejar dos o más objetos para establecer similitudes o diferencias, **usando criterios**.*
1. Percibir → 2. Analizar los objetos → 3. **Identificar los criterios** → 4. Comparar en un organizador gráfico

**Relacionar-asociar** — *establecer conexiones entre objetos o ideas en base a un criterio.*
1. Percibir → 2. Identificar los elementos de conexión → 3. Establecer las relaciones

**Comprobar-verificar** — *confirmar la veracidad o exactitud de algo.*
1. Percibir → 2. Elegir método de verificación → 3. Verificar el resultado

**Explicar** — *dar a conocer con vocabulario adecuado y medios pertinentes.*
1. Percibir y comprender → 2. Identificar ideas principales → 3. Organizar y secuenciar → 4. Seleccionar medio → 5. Explicar

---

## El script

Guardar como `05_Base-de-datos/revisar_tc.py`. Valida lo que hoy se puede comprobar desde los CSV, y avisa de lo que falta.

```python
# -*- coding: utf-8 -*-
"""Revisa que cada trabajo colaborativo tenga sus parametros definidos.

Uso:  python revisar_tc.py [EOM|PM|SI]
"""
from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent
CRITERIOS = 5
PUNTOS_TOTAL = 20

# Destrezas de Latorre (2018) admitidas. Ampliar solo con acuerdo de los tres lideres.
DESTREZAS = {
    "identificar", "ubicar-localizar", "describir", "comparar",
    "relacionar-asociar", "comprobar-verificar", "explicar",
    "analizar", "aplicar", "clasificar", "argumentar-fundamentar",
}
# Conectores con que entra una tecnica metodologica (Latorre, p.5)
CONECTORES = ("a traves de", "a través de", "por medio de", "mediante",
              "haciendo", "utilizando", "siguiendo", "comparando",
              "reconociendo", "marcando", "llenando")
# Rotulos que delatan que el riesgo o la incertidumbre se anunciaron
ROTULOS = ("lo que esta en juego", "lo que está en juego", "la incertidumbre",
           "el riesgo es", "donde esta el debate", "dónde está el debate",
           "atencion:", "atención:", "ojo:")


def leer(ruta: Path) -> list[dict]:
    if not ruta.exists():
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def es_narrativo(t: str) -> bool:
    """Un relato tiene frases; una ficha tiene vinetas y campos."""
    vinetas = len(re.findall(r"(?m)^\s*[-*•|]", t)) + t.count(" | ")
    frases = len(re.findall(r"[.!?]\s", t))
    return frases >= 5 and vinetas <= 2


def revisar(carrera: str) -> int:
    casos = [c for c in leer(RAIZ / carrera / "casos.csv")
             if c.get("alcance") == "colaborativo"]
    rubricas = leer(RAIZ / carrera / "rubricas.csv")
    indicadores = {i["indicador_id"] for i in leer(RAIZ / carrera / "indicadores.csv")}

    por_caso = defaultdict(list)
    for r in rubricas:
        por_caso[r["caso_id"]].append(r)

    print(f"\n{'='*68}\n{carrera} · {len(casos)} trabajos colaborativos\n{'='*68}")
    fallos = 0

    for c in casos:
        cid = c["caso_id"]
        print(f"\n── {cid}")
        filas = por_caso.get(cid, [])
        del_caso = 0          # fallos de ESTE caso, no del acumulado

        def mal(msg: str) -> None:
            nonlocal fallos, del_caso
            fallos += 1
            del_caso += 1
            print(f"   x  {msg}")

        desc = (c.get("descripcion") or "")
        bajo = desc.lower()

        # 1-2 · destreza (columna opcional: avisa mientras no exista)
        destreza = (c.get("destreza") or "").strip().lower()
        if not destreza:
            print("   ·  sin destreza declarada (falta la columna 'destreza')")
        elif destreza not in DESTREZAS:
            mal(f"destreza no reconocida: {destreza!r}")

        # 4 · tecnica metodologica: se reconoce por su conector
        tecnica = (c.get("tecnica_metodologica") or c.get("producto") or "").lower()
        if not any(k in tecnica for k in CONECTORES):
            mal("no se ve la tecnica metodologica: falta un conector "
                "(mediante, utilizando, reconociendo, marcando...)")

        # 6 · indicador existente
        inds = [i.strip() for i in (c.get("indicador_id") or "").split(";") if i.strip()]
        if not inds:
            mal("sin indicador_id")
        for i in inds:
            if i not in indicadores:
                mal(f"cita un indicador inexistente: {i}")

        # 7-8 · bloque y producto (las variantes A/B son de los casos de sesion)
        for campo, etq in (("bloque_id", "bloque"), ("producto", "producto")):
            if not (c.get(campo) or "").strip():
                mal(f"sin {etq}")

        # 11 · formato narrativo
        if not es_narrativo(desc):
            mal("el enunciado no parece un relato: pocas frases o demasiadas "
                "vinetas (parametro 11)")

        # 11b · el riesgo y la incertidumbre no se rotulan
        for r in ROTULOS:
            if r in bajo:
                mal(f"rotulo en el enunciado: {r!r} — debe ir dentro de la "
                    "historia (parametro 11)")
                break

        # 13 · fuente real: se busca una cita o un enlace de repositorio
        fuente = (c.get("fuente") or "") + " " + (c.get("recursos") or "") + " " + desc
        if not re.search(r"\(\s*(19|20)\d{2}\s*\)|repositorio\.|tesis\.|alicia\.", fuente, re.I):
            print("   ·  sin fuente real citada (tesis de repositorio) — parametro 13")

        # rubrica: 5 criterios, 20 puntos, ninguno ajeno al indicador del caso
        if len(filas) != CRITERIOS:
            mal(f"{len(filas)} criterios de rubrica, deben ser {CRITERIOS}")
        else:
            total = sum(int(f.get("puntos_max") or 0) for f in filas)
            if total != PUNTOS_TOTAL:
                mal(f"la rubrica suma {total} puntos, debe sumar {PUNTOS_TOTAL}")
            ajenos = {f["indicador_id"] for f in filas} - set(inds) - {"transversal"}
            if ajenos:
                mal(f"criterios que evaluan un indicador ajeno al caso: {sorted(ajenos)}")

        if del_caso == 0:
            print("   OK  parametros completos")

    print(f"\n{carrera}: {fallos} problema(s)\n")
    return fallos


if __name__ == "__main__":
    carreras = [sys.argv[1]] if len(sys.argv) > 1 else ["EOM", "PM", "SI"]
    sys.exit(1 if sum(revisar(c) for c in carreras) else 0)
```

**Qué comprueba:** indicador existente · bloque y producto · rúbrica de 5 criterios que sumen 20 · que ningún criterio evalúe un indicador ajeno al caso · que el enunciado sea narrativo y no una ficha · **que no haya rótulos** de riesgo o incertidumbre · que se cite una fuente de repositorio.

**Lo que no puede comprobar todavía:** la destreza y la técnica, hasta que existan las columnas. El script ya está preparado — cuando se añadan, empieza a validarlas sin tocar el código.

---

## Lo que hay que decidir entre los tres

1. ¿Se añaden a `casos.csv` las columnas **`destreza`**, **`tecnica_metodologica`** y **`fuente`**? Sin ellas el script no valida nueve de los catorce parámetros.
2. ¿Se acepta la lista de **destrezas admitidas**, o se recorta a las que el programa realmente usa?
3. ¿`revisar_tc.py` entra al flujo, junto a `revisar_rubricas.py`?
4. ¿El **presupuesto de 2 h / 4 estudiantes** aplica igual a los cursos de 96 h, o esos llevan un TC más largo?
