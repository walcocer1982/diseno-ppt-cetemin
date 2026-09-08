# -*- coding: utf-8 -*-
"""Aprueba las imagenes de una carrera, de un golpe.

Una imagen VERIFICADA es una imagen cuya proporcion ya se comprobo contra las cotas del
catalogo, o un esquema ya medido. Lo unico que faltaba era la firma del instructor lider.
Este comando la pone: no revisa nada, no cambia archivos, solo estampa quien aprueba y cuando.

    python aprobar_imagenes.py SI                 aprueba todas las verificadas de SI
    python aprobar_imagenes.py SI --ver           solo muestra cuales aprobaria
    python aprobar_imagenes.py SI IMG-SI-PHVA     aprueba solo las que empiecen asi

La firma sale de la tabla de lideres: cada uno firma lo suyo. Si manana cambia un lider,
se cambia aqui y en el CLAUDE.md.
"""
import csv, io, os, sys
from datetime import date

import sys

# La consola de Windows viene en cp1252 y revienta con "✘" o "·".
# Sin esto el script hace su trabajo y muere al IMPRIMIRLO. Ya paso.
for _f in (sys.stdout, sys.stderr):
    try: _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass


RAIZ = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(RAIZ, "imagenes.csv")

LIDER = {"SI": "Jorge Canchiz", "PM": "Harley Pereyra", "EOM": "Erick Salazar"}


def main(argv):
    ver = "--ver" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        raise SystemExit(__doc__)
    carrera = args[0].upper()
    if carrera not in LIDER:
        raise SystemExit("carrera desconocida: %s (esperaba SI, PM o EOM)" % carrera)
    prefijo = args[1] if len(args) > 1 else "IMG-%s-" % carrera
    firma, hoy = LIDER[carrera], date.today().isoformat()

    with io.open(CSV, encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        cols, filas = r.fieldnames, [dict(x) for x in r]

    tocadas, ya, sin_verificar = [], 0, []
    for x in filas:
        if not x["imagen_id"].startswith(prefijo):
            continue
        if x.get("estado") == "aprobada":
            ya += 1
        elif x.get("estado") == "verificada":
            tocadas.append(x["imagen_id"])
            if not ver:
                x["estado"] = "aprobada"
                x["aprobado_por"] = "%s (instructor lider %s) - %s" % (firma, carrera, hoy)
        else:
            sin_verificar.append((x["imagen_id"], x.get("estado") or "sin estado"))

    if not ver:
        with io.open(CSV, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(filas)

    verbo = "se aprobarian" if ver else "aprobadas"
    print("%s: %d %s - firma %s, %s" % (carrera, len(tocadas), verbo, firma, hoy))
    for i in tocadas:
        print("   ", i)
    if ya:
        print("   (%d ya estaban aprobadas)" % ya)
    if sin_verificar:
        print("\nNO se tocan - no estan verificadas todavia:")
        for i, e in sin_verificar:
            print("    %-34s %s" % (i, e))
        print("Verificar es medir, no opinar: primero pasa el control de proporcion.")


if __name__ == "__main__":
    main(sys.argv[1:])
