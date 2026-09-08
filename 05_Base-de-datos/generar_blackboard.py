# -*- coding: utf-8 -*-
"""Bancos de preguntas -> TXT delimitado por tabuladores, para subir a Blackboard.

Mismo origen que `generar_cuestionarios.py`: `SI/preguntas/*.csv`. Una sola
fuente de verdad, dos salidas.

    .docx  para leer y revisar a ojo (clave resaltada, retroalimentacion, fuente)
    .txt   para que Blackboard lo ingiera de una pasada

FORMATO QUE EXIGE BLACKBOARD (verificado contra la documentacion de Anthology,
2026-09-08):

    MC <TAB> pregunta <TAB> opcion1 <TAB> correct <TAB> opcion2 <TAB> incorrect ...

  - Una pregunta por linea, campos separados por TABULADOR.
  - SIN fila de cabecera y SIN lineas en blanco entre registros.
  - `correct` / `incorrect` van EN INGLES aunque la pregunta este en espanol.
  - Maximo 250 preguntas por archivo (nuestros bancos son de 50).

LO QUE NO VIAJA AL TXT: las columnas `porque` (retroalimentacion) y `fuente`.
El formato de carga no las admite, asi que se quedan en el Word del instructor.
Si alguna vez hacen falta dentro de Blackboard, se pegan a mano al editar la
pregunta en la plataforma.

EL TABULADOR ES EL SEPARADOR, asi que ningun texto puede contener uno: si
aparece, el script se planta en vez de generar un archivo que Blackboard
partiria por la mitad sin avisar.

Uso:  python generar_blackboard.py [CV1 EP ...]      (sin argumentos, todos)
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "05_Base-de-datos" / "SI" / "preguntas"
DEST = (RAIZ / "03_Entregables-diseño" / "SI - Ciclo II"
        / "1 - SI-SGCSSMA - Sistema de gestión de calidad, seguridad, salud y medio ambiente"
        / "Instrumentos de evaluación" / "CUESTIONARIOS Y EXÁMENES" / "TXT para Blackboard")

ORDEN = ["CV1", "CV2", "EP", "CV3", "CV4", "EF"]
OPCIONES = ["a", "b", "c", "d"]

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def limpiar(texto: str, banco: str, fila: int, campo: str) -> str:
    """Un tabulador dentro de un campo rompe el archivo sin que se note."""
    if "\t" in texto or "\n" in texto or "\r" in texto:
        raise SystemExit(
            f"   {banco}, pregunta {fila}: el campo '{campo}' trae un tabulador o "
            f"un salto de linea. Blackboard partiria el registro. Corrigelo en "
            f"SI/preguntas/{banco}.csv antes de volver a generar."
        )
    return texto.strip()


def convertir(banco: str) -> tuple[int, Path]:
    origen = FUENTE / f"{banco}.csv"
    with origen.open(encoding="utf-8-sig", newline="") as fh:
        filas = list(csv.DictReader(fh))

    lineas = []
    for n, q in enumerate(filas, 1):
        clave = q["clave"].strip().lower()
        if clave not in OPCIONES:
            raise SystemExit(f"   {banco}, pregunta {n}: clave '{clave}' no es a, b, c ni d.")
        campos = ["MC", limpiar(q["pregunta"], banco, n, "pregunta")]
        for op in OPCIONES:
            campos.append(limpiar(q[op], banco, n, op))
            campos.append("correct" if op == clave else "incorrect")
        lineas.append("\t".join(campos))

    if len(lineas) > 250:
        raise SystemExit(f"   {banco}: {len(lineas)} preguntas, y Blackboard admite 250 por archivo.")

    DEST.mkdir(parents=True, exist_ok=True)
    destino = DEST / f"{banco}.txt"
    # Sin linea en blanco final: Blackboard la lee como registro vacio.
    destino.write_text("\n".join(lineas), encoding="utf-8")
    return len(lineas), destino


def main(argv) -> int:
    pedidos = [a.upper() for a in argv[1:]] or ORDEN
    bancos = [b for b in ORDEN if b in pedidos]
    if not bancos:
        print("No conozco: %s" % ", ".join(argv[1:]))
        return 1
    print("Bancos para Blackboard · SI-SGCSSMA")
    for banco in bancos:
        n, destino = convertir(banco)
        print(f"   {banco:4s} {n} preguntas · {destino.name}")
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
