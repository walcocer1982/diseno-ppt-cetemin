# -*- coding: utf-8 -*-
"""Mide la EFICIENCIA de un PPT: cuántas diapositivas sobran y por qué.

EL PROBLEMA
    Al armar un PPT a mano se agregan diapositivas de más casi siempre, y
    cuando la sesión no cierra en 135 min se sacrifica la reflexión final
    (errores #4 y #8 del §08). "Tiene muchas slides" es una impresión; esto
    lo convierte en un número y señala DÓNDE está el exceso.

LAS TRES FORMAS DE DESPERDICIO (medibles)

  1. FRAGMENTACIÓN — el mismo título repetido en diapositivas seguidas.
     Es el desperdicio más común: un tema que cabía en una lámina se parte en
     tres o cuatro. (En la sesión 1 de Métodos: "TIPO DE LABORES SUBTERRÁNEAS"
     ocupa 4 diapositivas seguidas y "¿QUÉ ES LA MINERÍA?" otras 3.)

  2. MURO DE TEXTO — más de ~55 palabras en una diapositiva (error #5).
     No sobra la diapositiva: sobra el texto, y suele indicar que ahí hay
     material para dos láminas o para el plan de sesión, no para proyectar.

  3. DIAPOSITIVA HUECA — sin texto propio ni imagen que aporte.

Uso:  python analizar_ppt.py <archivo.pptx | carpeta>
"""
from __future__ import annotations

import html
import re
import sys
import zipfile
from pathlib import Path

PRESUPUESTO = 34        # tope del formato 004A (§07)
ESQUELETO = 10          # portada, subportada, 5 divisores, AE, ruta, tapa
MURO = 55               # palabras a partir de las cuales es muro de texto


# El LAYOUT identifica la funcion de cada diapositiva mejor que su texto, PERO
# el numero de layout CAMBIA entre plantillas: en la de PM el slideLayout8 son
# las subportadas y en la nueva es la TAPA. Por eso el mapa se declara POR
# PLANTILLA y se elige por el nombre del diseno, no por su numero.
MAPAS = {
    # plantilla vigente — 04_Recursos-graficos/comun/plantilla/
    "cetemin-2026": {
        "slideLayout1":  "portada",
        "slideLayout2":  "triangulacion",     # y subportada de sesion
        "slideLayout6":  "tema",              # «TITLE»: panel + imagen
        "slideLayout10": "subportada",        # las 5 de momento
        "slideLayout8":  "tapa",              # «TAPA FINAL»
        "slideLayout13": "contenido",
    },
    # PPT antiguos de PM y EOM
    "pm-eom-2024": {
        "slideLayout1":  "portada",
        "slideLayout8":  "subportada",
        "slideLayout12": "aprendizaje",
        "slideLayout11": "tapa",
    },
}

def mapa_de(z) -> dict:
    """La plantilla vigente se reconoce porque tiene un diseno «TAPA FINAL»."""
    import re as _re
    for n in z.namelist():
        if _re.match(r"ppt/slideLayouts/slideLayout\d+\.xml$", n):
            if b"TAPA FINAL" in z.read(n):
                return MAPAS["cetemin-2026"]
    return MAPAS["pm-eom-2024"]

LAYOUTS = MAPAS["pm-eom-2024"]      # se reemplaza al abrir cada archivo
MOMENTOS = ("CONEXIÓN", "ADQUISICIÓN", "APLICACIÓN", "DISCUSIÓN", "REFLEXIÓN")


def leer_slides(pptx: Path) -> list[dict]:
    global LAYOUTS
    z = zipfile.ZipFile(pptx)
    LAYOUTS = mapa_de(z)
    nombres = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                     key=lambda s: int(re.search(r"(\d+)", s.split("/")[-1]).group(1)))
    out = []
    for n in nombres:
        i = int(re.search(r"(\d+)", n.split("/")[-1]).group(1))
        x = z.read(n).decode("utf-8")
        textos = [html.unescape(t) for t in re.findall(r"<a:t>(.*?)</a:t>", x)]
        txt = " ".join(" ".join(textos).split())
        rel = f"ppt/slides/_rels/slide{i}.xml.rels"
        crudo = z.read(rel).decode("utf-8") if rel in z.namelist() else ""
        imgs = len(set(re.findall(r"image\d+", crudo)))
        lay = re.search(r"slideLayouts/(slideLayout\d+)\.xml", crudo)
        tipo = LAYOUTS.get(lay.group(1) if lay else "", "contenido")
        # la subportada de SESION es la que nombra la sesion y la unidad didactica
        if tipo == "contenido" and re.search(r"sesi[oó]n\s*n[°º]", txt, re.I) and "Unidad" in txt:
            tipo = "subportada-sesion"
        titulo = next((t.strip() for t in textos if len(t.strip()) > 3), "")
        out.append(dict(n=i, titulo=titulo, texto=txt, palabras=len(txt.split()),
                        imgs=imgs, tipo=tipo))
    return out


def normaliza(t: str) -> str:
    t = re.sub(r"[^\wáéíóúñ ]", " ", t.lower())
    return " ".join(t.split())[:45]


def analizar(pptx: Path) -> dict:
    s = leer_slides(pptx)
    total = len(s)

    # 1. fragmentacion: titulos iguales en diapositivas consecutivas
    grupos, actual = [], [s[0]] if s else []
    for a, b in zip(s, s[1:]):
        if normaliza(a["titulo"]) and normaliza(a["titulo"]) == normaliza(b["titulo"]):
            actual.append(b)
        else:
            if len(actual) > 1:
                grupos.append(actual)
            actual = [b]
    if len(actual) > 1:
        grupos.append(actual)
    # de un grupo de N diapositivas con el mismo titulo, 1 se justifica; el resto es exceso
    frag = sum(len(g) - 1 for g in grupos)

    # la TRIANGULACION es densa por diseno (3 zonas): no es muro de texto.
    # Se revisa aparte, con su propio tope de 110 palabras (§07).
    triang = [d for d in s if d["tipo"] == "aprendizaje"
              or re.search(r"aprendizaje (previsto|esperado)", d["texto"], re.I)
              and "PUNTOS CLAVES" in d["texto"].upper()]
    muros = [d for d in s if d["palabras"] > MURO and d not in triang]
    huecas = [d for d in s if d["palabras"] < 4 and d["imgs"] == 0]

    esqueleto = [d for d in s if d["tipo"] != "contenido"]
    subs = [d for d in s if d["tipo"] == "subportada"]
    faltan = [m for m in MOMENTOS if not any(m in d["texto"].upper() for d in subs)]
    return dict(archivo=pptx.name, total=total, exceso=max(0, total - PRESUPUESTO),
                grupos=grupos, frag=frag, muros=muros, huecas=huecas,
                esqueleto=esqueleto, subs=subs, faltan=faltan,
                triang=[d for d in triang if d["palabras"] > 110],
                palabras=sum(d["palabras"] for d in s))


def informe(r: dict) -> None:
    print(f"\n{'='*72}\n{r['archivo']}\n{'='*72}")
    print(f"  {r['total']} diapositivas   (presupuesto {PRESUPUESTO}"
          + (f" · {r['exceso']} de más)" if r["exceso"] else ")"))
    print(f"  {r['palabras']} palabras en total, {r['palabras']//max(r['total'],1)} por diapositiva\n")

    print("  ESTRUCTURA — diapositivas fijas detectadas por su layout:")
    for d in r["esqueleto"]:
        et = {"portada":"portada del programa", "subportada-sesion":"SUBPORTADA de sesión",
              "subportada":"SUBPORTADA de momento", "aprendizaje":"aprendizaje previsto",
              "triangulacion":"triangulación", "tema":"abre-tema",
              "contenido":"contenido", "tapa":"tapa"}.get(d["tipo"], d["tipo"])
        print(f"    {d['n']:>3}. {et:<24} {d['texto'][:40]}")
    print(f"    → {len(r['esqueleto'])} fijas · {len(r['subs'])} subportadas de momento"
          + (f"  ⚠ falta la de {', '.join(r['faltan'])}" if r["faltan"] else ""))
    print()

    if r["grupos"]:
        print(f"  FRAGMENTACION — {r['frag']} diapositivas recuperables:")
        for g in r["grupos"]:
            ns = ", ".join(str(d["n"]) for d in g)
            print(f"    · «{g[0]['titulo'][:52]}» ocupa {len(g)} diapositivas ({ns})")
    if r.get("triang"):
        for d in r["triang"]:
            print(f"  TRIANGULACION recargada — diapositiva {d['n']}: {d['palabras']} palabras (sano: 90-110)")
        print()
    if r["muros"]:
        print(f"\n  MURO DE TEXTO — {len(r['muros'])} diapositivas con más de {MURO} palabras:")
        for d in r["muros"][:6]:
            print(f"    · diapositiva {d['n']}: {d['palabras']} palabras — {d['titulo'][:44]}")
    if r["huecas"]:
        print(f"\n  HUECAS — {len(r['huecas'])}: {', '.join(str(d['n']) for d in r['huecas'])}")

    recuperable = r["frag"]
    if recuperable:
        print(f"\n  >> Uniendo lo fragmentado quedaría en {r['total'] - recuperable} diapositivas.", end="")
        print(" Dentro del presupuesto." if r["total"] - recuperable <= PRESUPUESTO else "")


if __name__ == "__main__":
    obj = Path(sys.argv[1])
    archivos = sorted(obj.glob("*.pptx")) if obj.is_dir() else [obj]
    res = [analizar(f) for f in archivos]
    for r in res:
        informe(r)
    if len(res) > 1:
        print(f"\n{'='*72}\nRESUMEN\n{'='*72}")
        t = sum(x["total"] for x in res)
        f = sum(x["frag"] for x in res)
        m = sum(len(x["muros"]) for x in res)
        print(f"  {len(res)} PPT · {t} diapositivas · {t/len(res):.1f} de media")
        print(f"  {sum(1 for x in res if x['exceso'])} PPT pasan el presupuesto de {PRESUPUESTO}")
        print(f"  {f} diapositivas recuperables por fragmentación ({f*100//max(t,1)} % del total)")
        print(f"  {m} diapositivas con muro de texto")
