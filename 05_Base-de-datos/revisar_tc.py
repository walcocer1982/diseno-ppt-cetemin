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

        # 7-8 · bloque y producto. Las casos A y B A/B NO aplican al colaborativo:
        # son de los casos de sesion (decision del 01/09/2026).
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
