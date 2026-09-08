# -*- coding: utf-8 -*-
"""Revisa las rubricas: valida la ESTRUCTURA, no el contenido.

EL REPARTO
    El molde es comun a las tres carreras — 5 criterios y 4 niveles (§06) —
    pero **cada trabajo colaborativo tiene su propia rubrica**: los
    descriptores hablan del caso concreto. Son 70 rubricas (35 cursos x 2 TC),
    todas con la misma forma y ninguna con el mismo texto.

    Por eso este script valida lo que es comun y NO redacta descriptores: eso
    es criterio tecnico del instructor.

QUE COMPRUEBA

  1. COBERTURA        cada caso tiene rubrica y cada bloque tiene caso
  2. ESTRUCTURA       5 criterios, 4 niveles, ninguno vacio
  3. DESCRIPTORES     conducta observable, no adjetivos sueltos
                      ("Describe las 5 operaciones con equipos" vs "Excelente")
  4. PROGRESION       los 4 niveles se distinguen entre si
  5. PERTENENCIA      el vocabulario de la rubrica coincide con el del curso.
                      Es la que caza el error real encontrado en Metodos de
                      explotacion: una rubrica de TC2 que evaluaba INGLES.
  6. NOTA VIGESIMAL   5 criterios x 4 puntos = 20. Los criterios pesan IGUAL
                      por diseno: no hay ponderacion. Por eso deben ser
                      exactamente 5 — con 4 o 6 la nota ya no sale sobre 20.
  7. TRAZABILIDAD     cada criterio dice que indicador evalua, y ningun
                      indicador del curso se queda sin evaluar. Los criterios
                      de presentacion y aporte individual van 'transversal':
                      miden desempeno de equipo, no contenido.

Uso:  python revisar_rubricas.py [EOM|PM|SI]
"""
from __future__ import annotations

import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

# La consola de Windows usa cp1252 y este script imprime ✘ (U+2718): sin
# esto revienta con UnicodeEncodeError antes del primer resultado.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent
CRITERIOS_ESPERADOS = 5
NIVELES = ["nivel_4", "nivel_3", "nivel_2", "nivel_1"]
MIN_PALABRAS = 4          # menos que esto es un adjetivo, no un descriptor
MIN_SOLAPE = 0.12         # por debajo, la rubrica no habla del curso

# Los criterios 4 y 5 son los MISMOS en los 70 TC — verificado en las dos
# rubricas oficiales de PM · Matematica: identicos palabra por palabra entre
# el caso 1 y el caso 2. Los criterios 1-3 los nombra el caso.
FIJOS = {"4": "Presentación PPT: contenido y diseño",
         "5": "Presentación oral: dominio y claridad"}

VACIAS = {"excelente", "muy bueno", "bueno", "regular", "malo", "deficiente",
          "satisfactorio", "aceptable", "insuficiente", "si", "no", "logrado",
          "en proceso", "en inicio", "destacado"}


def leer(ruta: Path) -> list[dict]:
    if not ruta.exists():
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def palabras(t: str) -> set[str]:
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return {p for p in re.findall(r"[a-z]{5,}", t)}


def revisar(carrera: str) -> None:
    rubricas = leer(RAIZ / carrera / "rubricas.csv")
    casos = leer(RAIZ / carrera / "casos.csv")
    bloques = leer(RAIZ / carrera / "bloques.csv")
    contenidos = leer(RAIZ / carrera / "contenidos.csv")
    sesiones = leer(RAIZ / carrera / "sesiones.csv")

    print(f"\n{'='*70}\n{carrera} · {len(rubricas)} filas de rúbrica · {len(casos)} casos\n{'='*70}")
    if not rubricas:
        print("  (sin rúbricas cargadas)")
        return

    # vocabulario del curso: temas de sesión + puntos clave
    vocab = defaultdict(set)
    for s in sesiones:
        vocab[s["curso_id"]] |= palabras(s.get("tema", "") + " " + s.get("aprendizaje_esperado", ""))
    for c in contenidos:
        cid = next((s["curso_id"] for s in sesiones if s["sesion_id"] == c["sesion_id"]), None)
        if cid:
            vocab[cid] |= palabras(c.get("contenido", ""))

    por_caso = defaultdict(list)
    for r in rubricas:
        por_caso[r["caso_id"]].append(r)

    # 1 · COBERTURA — solo los colaborativos llevan rubrica de 5 criterios.
    # Los casos de sesion (alcance=sesion) no, y contarlos daba un ✘ falso
    # que acaba ensenando a ignorar el aviso.
    colaborativos = [c for c in casos
                     if c.get("alcance", "colaborativo") == "colaborativo"]
    caso_ids = {c["caso_id"] for c in colaborativos}
    sin_rubrica = caso_ids - set(por_caso)
    huerfanas = set(por_caso) - {c["caso_id"] for c in casos}
    bloques_sin_caso = [b["bloque_id"] for b in bloques
                        if b.get("curso_id") in {c["curso_id"] for c in casos}
                        and not any(c.get("bloque_id") == b["bloque_id"] for c in casos)]
    print(f"\n1 · COBERTURA")
    print(f"   {'OK ' if not sin_rubrica else '✘  '}casos con rúbrica: {len(caso_ids)-len(sin_rubrica)}/{len(caso_ids)}"
          + (f"  → sin rúbrica: {sorted(sin_rubrica)}" if sin_rubrica else ""))
    if huerfanas:
        print(f"   ✘  rúbricas sin caso: {sorted(huerfanas)}")
    if bloques_sin_caso:
        print(f"   ✘  bloques sin caso: {len(bloques_sin_caso)}")

    # 2-5 · por rúbrica
    for caso_id, filas in sorted(por_caso.items()):
        caso = next((c for c in casos if c["caso_id"] == caso_id), None)
        cid = caso["curso_id"] if caso else filas[0].get("curso_id", "")
        print(f"\n── {caso_id}  ({len(filas)} criterios)")
        fallos = []

        # 2b · el molde: los criterios 4 y 5 son literales en los 70 TC
        for n, esperado in FIJOS.items():
            f = next((x for x in filas if x.get("n") == n), None)
            if f and f.get("criterio", "").strip().lower() != esperado.lower():
                fallos.append(f"criterio {n} debería llamarse «{esperado}» "
                              f"y se llama «{f['criterio']}» (§06: los 4 y 5 no se renombran)")

        # 6 · la nota tiene que salir vigesimal
        maximo = sum(int(f.get("puntos_max") or 4) for f in filas)
        if maximo != 20:
            fallos.append(f"la nota máxima da {maximo}, no 20: son {len(filas)} criterios "
                          f"× {filas[0].get('puntos_max','4')} puntos (deben ser 5 × 4)")

        for f in filas:
            n = f.get("n", "?")
            crit = f.get("criterio", "")
            if not crit.strip():
                fallos.append(f"criterio {n}: sin nombre")
            textos = [f.get(k, "").strip() for k in NIVELES]
            if any(not t for t in textos):
                fallos.append(f"criterio {n} «{crit[:28]}»: falta el nivel "
                              + ", ".join(NIVELES[i] for i, t in enumerate(textos) if not t))
                continue
            # 3 · descriptores
            flojos = [NIVELES[i] for i, t in enumerate(textos)
                      if len(t.split()) < MIN_PALABRAS or t.lower().strip(" .") in VACIAS]
            if flojos:
                fallos.append(f"criterio {n} «{crit[:28]}»: {', '.join(flojos)} es un adjetivo, no describe conducta")
            # 4 · progresión
            if len(set(t.lower() for t in textos)) < 4:
                fallos.append(f"criterio {n} «{crit[:28]}»: hay niveles repetidos")

        # 5 · pertenencia
        texto_rub = " ".join(f.get("criterio", "") + " " + " ".join(f.get(k, "") for k in NIVELES)
                             for f in filas)
        pr, pc = palabras(texto_rub), vocab.get(cid, set())
        solape = len(pr & pc) / max(len(pr), 1)
        if pc and solape < MIN_SOLAPE:
            fallos.append(f"solo {solape:.0%} de su vocabulario coincide con el del curso "
                          f"→ ¿es la rúbrica de otro curso?")

        if fallos:
            for x in fallos:
                print(f"   ✘  {x}")
        else:
            print(f"   OK  estructura correcta · vocabulario del curso {solape:.0%}")

    # 7 · TRAZABILIDAD: que los indicadores del curso queden todos evaluados
    indicadores = leer(RAIZ / carrera / "indicadores.csv")
    sin_ind = [r for r in rubricas if not r.get("indicador_id", "").strip()]
    if sin_ind:
        print(f"\n7 · TRAZABILIDAD\n   ✘  {len(sin_ind)} de {len(rubricas)} criterios sin indicador_id")
        return

    cuenta = defaultdict(int)
    for r in rubricas:
        cuenta[r["indicador_id"]] += 1
    total = len(rubricas) * 4
    print(f"\n7 · TRAZABILIDAD  ({total} puntos entre los dos TC)")
    for ind in indicadores:
        i = ind["indicador_id"]
        marca = "OK " if cuenta[i] else "✘  "
        print(f"   {marca}{i}: {cuenta[i]*4:>2} pts · {ind['descripcion'][:52]}…")
    huerf = set(cuenta) - {i["indicador_id"] for i in indicadores} - {"transversal"}
    if huerf:
        print(f"   ✘  criterios que citan un indicador inexistente: {sorted(huerf)}")
    if cuenta["transversal"]:
        print(f"   ·  transversal: {cuenta['transversal']*4} pts — presentación y aporte "
              f"individual, no contenido")


if __name__ == "__main__":
    for c in ([sys.argv[1]] if len(sys.argv) > 1 else ["EOM", "PM", "SI"]):
        revisar(c)
