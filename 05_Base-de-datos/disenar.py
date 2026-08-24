# -*- coding: utf-8 -*-
"""Un comando para producir la sesión: genera, revisa y avisa.

PARA QUÉ
    El instructor líder no tiene que recordar tres scripts ni en qué orden.
    Escribe una línea y recibe el PPT, el guion y la lista de lo que falta.

        python disenar.py EOM-METEXP-S1

    Y si la sesión aún tiene imágenes sin aprobar:

        python disenar.py EOM-METEXP-S1 --borrador

QUÉ HACE, EN ORDEN
    1. genera el PPT desde la base       generar_ppt.py
    2. genera el guion de verificación   generar_md.py
    3. revisa el PPT ya generado         revisar_ppt.py

    La revisión corre SOBRE EL ARCHIVO, no sobre los CSV: los fallos aparecen
    en el resultado aunque la base esté bien.

LO QUE NO HACE
    No aprueba nada. Las imágenes y los puntos clave los firma el instructor
    en el guion — la máquina mide, la persona mira.
"""
from __future__ import annotations

import sys
from pathlib import Path

import generar_ppt
import generar_md
import revisar_ppt


def main(sesion_id: str, borrador: bool) -> int:
    print(f"\n{'='*68}\n  {sesion_id}{'   (borrador)' if borrador else ''}\n{'='*68}")

    print("\n1 · PPT")
    ppt = generar_ppt.generar(sesion_id, borrador=borrador)
    print(f"    {ppt.name}")

    print("\n2 · Guion de verificación")
    md = generar_md.generar(sesion_id)
    print(f"    {md.name}")

    print("\n3 · Revisión")
    fallos = revisar_ppt.revisar(sesion_id)

    print(f"{'='*68}")
    if fallos:
        print(f"  {fallos} fallo(s) que corregir EN LA BASE — nunca en el PPT.")
        print(f"  Corrige el CSV y vuelve a correr este comando.")
    else:
        print(f"  Sin fallos medibles. Ahora mira las láminas señaladas arriba")
        print(f"  y firma en {md.name}.")
    print(f"{'='*68}\n")
    return fallos


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit("Uso: python disenar.py EOM-METEXP-S1 [--borrador]")
    sys.exit(1 if main(args[0], "--borrador" in sys.argv) else 0)
