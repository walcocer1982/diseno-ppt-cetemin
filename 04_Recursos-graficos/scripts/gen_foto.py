# -*- coding: utf-8 -*-
"""Limpia una fotografia de operacion para usarla en el PPT.

QUE HACE Y QUE NO
    Parte de una FOTO REAL —de tesis o de archivo propio— y solo le quita lo
    que estorba: circulos y flechas que el autor puso para su propio texto,
    marcas de agua, bordes. Nada mas.

    NO inventa la labor. Una mina generada de cero puede traer un sostenimiento
    imposible o una seccion que no existe, y aqui no hay cotas contra las cuales
    medirlo — a diferencia de las siluetas de equipo (§10). Y es justo la lamina
    donde el estudiante mira para observar la realidad.

    Por eso el prompt es de LIMPIEZA, no de creacion, y la foto conserva su
    fuente y su cita en imagenes.csv.

Uso:  python gen_foto.py ../EOM/fotos/_tesis_p58_296.png frente-perforacion
"""
from __future__ import annotations

import sys
from pathlib import Path

from config import cliente, MODELO_IMAGEN

PROMPT = (
    "Clean up this real photograph of an underground mine heading. "
    "Remove the red annotation circle and any other drawn marks or arrows added on top. "
    "Keep everything else exactly as it is: the rock face, the drilling jumbo, "
    "the mesh support, the blue layout marks, the hoses and the lighting. "
    "Do not add, move or invent any element. Improve exposure and clarity only."
)


def limpiar(referencia: Path, nombre: str, tam: str = "1536x1024") -> Path:
    salida = referencia.parent / f"{nombre}.png"
    with open(referencia, "rb") as fh:
        r = cliente().images.edit(model=MODELO_IMAGEN, image=[fh], prompt=PROMPT,
                                  size=tam, quality="high")
    import base64
    salida.write_bytes(base64.b64decode(r.data[0].b64_json))
    return salida


if __name__ == "__main__":
    ref = Path(sys.argv[1])
    nombre = sys.argv[2] if len(sys.argv) > 2 else ref.stem.lstrip("_")
    if not ref.exists():
        raise SystemExit(f"No existe la referencia: {ref}")
    print(f"Modelo: {MODELO_IMAGEN}\nReferencia: {ref.name}")
    f = limpiar(ref, nombre)
    print(f"  -> {f.resolve().relative_to(Path(__file__).resolve().parents[2])}  ({f.stat().st_size // 1024} KB)")
