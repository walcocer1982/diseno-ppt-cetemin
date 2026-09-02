# -*- coding: utf-8 -*-
"""Revisa el PPT YA GENERADO: mide lo medible y senala que hay que mirar.

POR QUE SOBRE EL ARCHIVO Y NO SOBRE LOS CSV
    Los fallos que aparecieron en la sesion 1 —siete laminas mostrando el mismo
    texto, una lamina con el texto de otra— NO se ven en la base: los CSV
    estaban bien. Se ven en el resultado. Es la diferencia entre revisar la
    receta y probar el plato.

LOS DOS NIVELES
    MEDIDO   palabras, texto repetido, imagen presente, desbordes, tipografia,
             minutos, notas del orador. Sale de leer el .pptx.
    MIRADO   que la imagen CORRESPONDA al tema, el ritmo visual, si un esquema
             queda ilegible al reducirse. Ninguna medicion caza que la lamina
             «La guardia» llevara un equipo de transporte: la imagen estaba,
             tenia fuente y estaba bien colocada — pero era de otra sesion.

    Por eso el script no solo mide: deja la LISTA DE LO QUE HAY QUE MIRAR, para
    revisar seis laminas senaladas y no veinticuatro a ciegas.

Uso:  python revisar_ppt.py EOM-METEXP-S1
"""
from __future__ import annotations

import re
import sys
import warnings
from collections import defaultdict
from pathlib import Path

warnings.filterwarnings("ignore")
from pptx import Presentation
from pptx.util import Emu

from generar_ppt import RAIZ, leer, sin_tildes, destino

import sys

# La consola de Windows viene en cp1252 y revienta con "✘" o "·".
# Sin esto el script hace su trabajo y muere al IMPRIMIRLO. Ya paso.
for _f in (sys.stdout, sys.stderr):
    try: _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass


MAX_PALABRAS = 90        # por encima, muro de texto (error #5 del §08)
MAX_TRIANGULACION = 120  # DECISION de Jorge Canchiz, 2026-09-02: la lamina se queda como
                         # esta. Recortarla obligaria a quitar algo que el formato oficial
                         # pide. Era el unico aviso que quedaba en la S1 y la S3.
                         # la triangulacion es densa POR DISEÑO (§07): muestra
                         # aprendizaje, puntos clave y evaluacion de un vistazo,
                         # y por eso NO cuenta como muro de texto
W_IN, H_IN = 13.333, 7.5
MARCA = "Oswald"


def texto_de(s) -> str:
    return " ".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame).strip()


def normalizar(t: str) -> str:
    return re.sub(r"\s+", " ", sin_tildes(t).lower())[:120]


def revisar(sesion_id: str, ppt_ruta=None) -> int:
    carrera = sesion_id.split("-")[0]
    laminas = sorted([l for l in leer(RAIZ / carrera / "laminas.csv")
                      if l["sesion_id"] == sesion_id], key=lambda r: int(r["orden"]))
    ses = next(s for s in leer(RAIZ / carrera / "sesiones.csv") if s["sesion_id"] == sesion_id)
    curso = next(c for c in leer(RAIZ / "cursos.csv") if c["curso_id"] == ses["curso_id"])
    # una sola regla de ruta, la de generar_ppt: el revisor mira lo que el generador escribe
    ppt = Path(ppt_ruta) if ppt_ruta else destino(carrera, ses, curso)
    if not ppt.exists():
        raise SystemExit(f"No existe el PPT: {ppt}\n       Genéralo antes con generar_ppt.py")

    prs = Presentation(ppt)
    imgs_reg = {i["imagen_id"]: i for i in leer(RAIZ / "imagenes.csv")}
    fallos, mirar = [], []
    cuerpos, lineas = {}, {}

    for i, s in enumerate(prs.slides, 1):
        l = laminas[i - 1] if i <= len(laminas) else {}
        titulo = l.get("titulo") or l.get("tipo", "")
        t = texto_de(s)
        pal = len(t.split())
        imgs = [sh for sh in s.shapes if sh.shape_type == 13]

        if l.get("tipo") == "triangulacion":
            for rotulo in ("APRENDIZAJE PREVISTO", "PUNTOS CLAVES", "EVALUACIÓN",
                           "Al finalizar la sesión podremos…"):
                t = t.replace(rotulo, "")
            pal = len(t.split())
        # La lamina de cotejo no es prosa: es una tabla de referencia, siempre la misma,
        # que el alumno lee por su linea. Contarle palabras como a un muro no dice nada.
        if l.get("tipo") == "cotejo":
            continue
        techo = MAX_TRIANGULACION if l.get("tipo") == "triangulacion" else MAX_PALABRAS
        if pal > techo:
            fallos.append(f"{i} · {titulo} — muro de texto ({pal} palabras, máx {techo})")

        # El defecto contrario al muro de texto: la lamina flaca. Una lamina de
        # tema con menos de tres ideas propias deja al instructor sin de que
        # hablar durante sus minutos (§07: "una lamina vacia es falta de
        # contenido, no de diseno").
        if l.get("tipo") == "tema" and l.get("idea", "").strip():
            r = l["idea"].replace(",", "-").split("-")
            try:
                n_ideas = int(r[-1]) - int(r[0]) + 1
            except ValueError:
                n_ideas = 0
            if 0 < n_ideas < 3:
                fallos.append(f"{i} · {titulo} — lámina flaca: {n_ideas} idea(s), el molde son 3 a 4")

        # el cuerpo sin el titulo: si dos laminas dicen lo mismo, una sobra
        cuerpo = normalizar(t.replace(titulo, "", 1))
        if len(cuerpo) > 30:
            if cuerpo in cuerpos:
                fallos.append(f"{i} · {titulo} — MISMO TEXTO que la lámina {cuerpos[cuerpo]}")
            else:
                cuerpos[cuerpo] = i

        # y la repeticion parcial: una linea suelta compartida entre laminas
        for ln in (x.strip() for x in t.split(chr(10))):
            if len(ln) < 25 or ln == titulo:
                continue
            k = normalizar(ln)
            if k in lineas and lineas[k] != i:
                fallos.append(f"{i} · {titulo} — repite una línea de la lámina {lineas[k]}: «{ln[:46]}…»")
            else:
                lineas.setdefault(k, i)

        # Una lamina que ANUNCIA una imagen y no la trae deja la actividad rota.
        # Paso en la S1 de SI: la lamina del Veo-Pienso-Me pregunto decia "mira
        # la fotografia" y no habia fotografia. La regla vieja solo exigia
        # imagen en Adquisicion, asi que el fallo pasaba limpio.
        anuncia = re.search(r"(mira|observa|revisa|analiza)[^.]{0,40}"
                            r"(la |esta |el |este )?(fotograf|imagen|esquema|figura|cuadro|foto)",
                            (l.get("texto", "") or "").lower())
        if anuncia and not l.get("imagen_id", "").strip():
            fallos.append(f"{i} · {titulo} — ANUNCIA una imagen que la lámina no tiene")

        # el texto de la lamina tiene que ser el suyo.
        # OJO: normalizar() recorta a 120 caracteres — util para indexar lineas,
        # ruinoso aqui. En una subportada con la unidad didactica delante, el
        # texto propio caia fuera del recorte y la lamina se marcaba sin fallo.
        propio = normalizar(l.get("texto", ""))
        completo = re.sub(r"\s+", " ", sin_tildes(t).lower())
        if propio and len(propio) > 30 and propio[:60] not in completo:
            fallos.append(f"{i} · {titulo} — el texto proyectado NO es el de la lámina")

        if l.get("momento") == "adquisicion" and l.get("tipo") in ("tema", "contenido"):
            im = imgs_reg.get(l.get("imagen_id", ""), {})
            if not imgs:
                fallos.append(f"{i} · {titulo} — SIN IMAGEN (regla de Adquisición)")
            else:
                pide = l.get("que_muestra", "").strip()
                if pide:
                    lleva = im.get("descripcion", "(sin descripción)")[:80]
                    mirar.append(f"{i} · {titulo}  |  debe mostrar: {pide}  |  lleva: {lleva}")
                else:
                    mirar.append(f"{i} · {titulo} — SIN `que_muestra` declarado: "
                                 f"no hay contra qué contrastar la imagen")

        for sh in s.shapes:
            x, y = Emu(sh.left or 0).inches, Emu(sh.top or 0).inches
            w, h = Emu(sh.width or 0).inches, Emu(sh.height or 0).inches
            if x < -0.05 or y < -0.05 or x + w > W_IN + 0.05 or y + h > H_IN + 0.05:
                fallos.append(f"{i} · {titulo} — un elemento se sale del lienzo")
                break

        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.font.name and r.font.name != MARCA:
                        fallos.append(f"{i} · {titulo} — tipografía «{r.font.name}», debería ser {MARCA}")
                        break
                break
            break

        if l.get("tipo") in ("tema", "contenido") and not (
                s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip()):
            fallos.append(f"{i} · {titulo} — sin notas del orador")

    por_momento = defaultdict(int)
    for l in laminas:
        por_momento[l.get("momento", "")] += int(l.get("minutos") or 0)
    total = sum(por_momento.values())
    if total != 135:
        fallos.append(f"la sesión suma {total} min, no 135")

    # dos laminas seguidas con el mismo diseno se leen como una sola
    seguidas = [f"{i}-{i+1}" for i in range(1, len(laminas))
                if laminas[i - 1].get("tipo") == laminas[i].get("tipo") == "tema"
                and (i % 2 == 0)]
    if seguidas:
        mirar.append(f"pares con el mismo diseño: {', '.join(seguidas[:4])} — ¿se distinguen?")

    print(f"\n{'='*68}\nREVISIÓN · {ppt.name}\n{len(prs.slides)} diapositivas · {total} min\n{'='*68}")
    print("\nMEDIDO")
    if fallos:
        for f in fallos:
            print(f"  ✘  {f}")
    else:
        print("  OK  sin fallos medibles")
    print(f"  ·  minutos: " + " · ".join(f"{m[:4]} {v}'" for m, v in por_momento.items() if m))
    print("\nPARA MIRAR")
    for m in mirar or ["  (nada señalado)"]:
        print(f"  →  {m}")
    print()
    return len(fallos)


if __name__ == "__main__":
    # El PPT ya no vive siempre en la ruta por defecto: cada carrera organiza su
    # carpeta de entregables. Se admite  revisar_ppt.py <sesion_id> [ruta.pptx]
    args = sys.argv[1:]
    sid = args[0] if args else "EOM-METEXP-S1"
    ruta = next((Path(a) for a in args[1:] if a.lower().endswith(".pptx")), None)
    n = revisar(sid, ruta)
    sys.exit(1 if n else 0)
