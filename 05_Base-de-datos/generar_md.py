# -*- coding: utf-8 -*-
"""Genera el guion de la sesion en Markdown: lo que el instructor revisa.

POR QUE EXISTE
    El visor sirve para ver el curso de un vistazo. El MD es el documento de
    VERIFICACION: el instructor lo lee de arriba abajo y firma que la sesion
    esta bien. El PPT deja de ser lo que se revisa y pasa a ser lo que se
    proyecta — si el MD esta bien, el PPT esta bien, porque salen de la misma
    tabla.

SE GENERA, NO SE ESCRIBE
    Hubo un guion escrito a mano que decia 31 diapositivas cuando la base decia
    20. Se desincronizo en silencio. Lo que el instructor revisa tiene que salir
    de la base, igual que el PPT.

EL BLOQUE DE AVISOS
    Al final va lo que la sesion tiene mal. En texto plano se ve de un vistazo
    lo que en el PPT obliga a pasar 25 diapositivas.

Uso:  python generar_md.py EOM-METEXP-S1
"""
from __future__ import annotations

import sys
from pathlib import Path

from generar_ppt import (RAIZ, leer, sin_tildes, bajada_de, punto_de, revisar)

import sys

# La consola de Windows viene en cp1252 y revienta con "✘" o "·".
# Sin esto el script hace su trabajo y muere al IMPRIMIRLO. Ya paso.
for _f in (sys.stdout, sys.stderr):
    try: _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass


MOMENTOS = {"conexion": "CONEXIÓN", "adquisicion": "ADQUISICIÓN", "aplicacion": "APLICACIÓN",
            "discusion": "DISCUSIÓN", "reflexion": "REFLEXIÓN"}


def generar(sesion_id: str) -> Path:
    carrera = sesion_id.split("-")[0]
    laminas = sorted([l for l in leer(RAIZ / carrera / "laminas.csv")
                      if l["sesion_id"] == sesion_id], key=lambda r: int(r["orden"]))
    if not laminas:
        raise SystemExit(f"No hay laminas para {sesion_id}")
    ses = next(s for s in leer(RAIZ / carrera / "sesiones.csv") if s["sesion_id"] == sesion_id)
    curso = next(c for c in leer(RAIZ / "cursos.csv") if c["curso_id"] == ses["curso_id"])
    imgs = {i["imagen_id"]: i for i in leer(RAIZ / "imagenes.csv")}
    inds = {i["indicador_id"]: i for i in leer(RAIZ / carrera / "indicadores.csv")}
    acts = leer(RAIZ / carrera / "actividades.csv") if (RAIZ / carrera / "actividades.csv").exists() else []
    acts = [a for a in acts if a.get("sesion_id") == sesion_id]
    casos = [c for c in leer(RAIZ / carrera / "casos.csv") if c.get("sesion_id") == sesion_id]

    total = sum(int(l["minutos"] or 0) for l in laminas)
    o = [f"# Sesión {ses['nro_sesion']} · {ses['tema']}", "",
         f"**{curso['nombre_curso']}** · {curso['carrera']} · {len(laminas)} diapositivas · **{total} min**", "",
         "> Documento de verificación. Se genera desde la base: para cambiarlo, se cambia el CSV.", "",
         "## Aprendizaje esperado", "", f"> {ses['aprendizaje_esperado']}", ""]
    ind = inds.get(ses.get("indicador_id", ""))
    if ind:
        o += [f"**Indicador** `{ind['indicador_id']}` — {ind['descripcion']}", ""]

    puntos = [c for c in leer(RAIZ / carrera / "contenidos.csv") if c["sesion_id"] == sesion_id]
    o += ["## Puntos clave", ""]
    for p in puntos:
        o.append(f"- `{p['contenido_id']}` **{p['contenido']}**")
        for d in (x.strip() for x in p.get("desarrollo", "").split("|") if x.strip()):
            o.append(f"    - {d}")
    o.append("")

    if casos:
        c = casos[0]
        o += ["## El caso de la sesión", "", f"**{c['caso_id']}**", "", f"> {c['descripcion']}", "",
              f"**Pregunta gatilladora:** {c.get('pregunta_gatilladora','')}", "",
              f"**Producto:** {c.get('producto','')}", ""]

    recursos = [i for i in leer(RAIZ / "imagenes.csv")
                if i["imagen_id"] not in {l.get("imagen_id") for l in laminas}
                and any(i["imagen_id"] in (c.get("recursos", "") or "") for c in casos)]
    if recursos:
        o += ["### Para imprimir y llevar a clase", ""]
        for r in recursos:
            o.append(f"- **{r['imagen_id']}** — `{r['archivo']}`")
            if r.get("descripcion"):
                o.append(f"    {r['descripcion']}")
        o += ["", "> No se proyectan: se entregan a los equipos.", ""]

    o += ["## Ruta de la sesión", ""]
    actual = None
    for l in laminas:
        m = l.get("momento", "")
        if m and m != actual:
            actual = m
            mins = sum(int(x["minutos"] or 0) for x in laminas if x.get("momento") == m)
            o += ["", f"### {MOMENTOS.get(m, m.upper())} · {mins} min", ""]
        if l["tipo"] == "subportada-momento":
            continue
        cab = f"**{l['orden']}. {l['titulo'] or l['tipo']}**"
        if int(l["minutos"] or 0):
            cab += f"  ·  {l['minutos']}'"
        im = imgs.get(l.get("imagen_id", ""))
        if im:
            marca = "✅" if im.get("estado") == "aprobada" else "⚠️"
            cab += f"  ·  {marca} `{im['imagen_id']}`"
        o.append(cab)
        cuerpo = bajada_de(l, sesion_id, carrera) or l.get("texto", "")
        for linea in (x.strip() for x in cuerpo.split("\n") if x.strip()):
            o.append(f"  {linea}")
        a = next((x for x in acts if x.get("momento") == m and x.get("rutina")), None)
        if a and l["tipo"] != "subportada-momento" and a.get("rutina"):
            o.append(f"  *rutina: {a['rutina']}*")
        o.append("")

    avisos = revisar(laminas, imgs, sesion_id, carrera)
    o += ["---", "", "## ⚠ Avisos", ""]
    o += [f"- {a}" for a in avisos] if avisos else ["- ninguno: la sesión está completa"]
    o += ["", "---", "", "## Verificación del instructor", "",
          "- [ ] El aprendizaje esperado corresponde al indicador",
          "- [ ] Los puntos clave alcanzan para responder el caso",
          "- [ ] Toda lámina de Adquisición tiene imagen y contenido",
          "- [ ] Los minutos suman 135",
          "- [ ] Las imágenes están aprobadas", "",
          "**Aprobado por:** ______________________  **Fecha:** ____________", ""]

    salida = (RAIZ.parent / "03_Entregables-diseño" /
              f"{carrera}-{sin_tildes(curso['nombre_curso'])}" /
              f"S{ses['nro_sesion']}_guion.md")
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text("\n".join(o), encoding="utf-8")
    return salida


if __name__ == "__main__":
    f = generar(sys.argv[1] if len(sys.argv) > 1 else "EOM-METEXP-S1")
    print(f.resolve().relative_to(RAIZ.parent))
