# -*- coding: utf-8 -*-
"""Rehace la matriz de distribución de un curso desde la base de datos.

PARA QUÉ
    La matriz dice en su encabezado que se genera desde la base, pero hasta ahora
    se editaba a mano celda por celda, y por eso se desincronizaba en silencio.
    Con esto se rehace de un comando cada vez que la base cambia.

        python generar_matriz.py SI-SGCSSMA

QUÉ REESCRIBE
    · el bloque de indicadores de logro
    · las dos filas de los colaborativos (destreza, producto, caso, rúbrica)
    · todas las filas de sesión: bloque, tipo, indicador, tema, aprendizaje
      esperado, tributa, y el color de fila según el indicador dominante
    · las columnas derivadas: caso A, caso B, cotejo, puntos clave y PPT,
      contadas de casos.csv, listas_cotejo.csv, contenidos.csv y laminas.csv
    · la leyenda, el avance y la nota de estructura al pie

LO QUE NO TOCA
    La CAPACIDAD. Baja del 7A y se edita a mano, con su registro en
    observaciones.csv. Tampoco toca el formato: respeta anchos, bordes y
    estilos del archivo, porque lo edita en sitio y no lo rehace.

CÓMO SE UBICA
    No usa números de fila fijos: busca las filas por su rótulo (BLOQUE,
    IND-1, LEYENDA, ② Aprendizajes esperados). Si no encuentra un ancla,
    se detiene sin escribir.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import PatternFill

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

RAIZ = Path(__file__).resolve().parent
REPO = RAIZ.parent

# color de fila segun el indicador dominante (el primero de la lista)
COLOR = {1: "FFF2CC", 2: "DEEBF7", 3: "FCE4D6", 4: "E2EFDA"}
GRIS, VERDE, AMBAR, AMBAR2 = "D9D9D9", "C6EFCE", "F8CBAD", "FFEB9C"

# rotulo, clausulas y rango de sesiones de cada indicador  ·  solo SI-SGCSSMA
ROTULO = {
    "SI-SGCSSMA": {
        1: ("Fundamento", "cláusulas 1 a 5", ""),
        2: ("Planificación", "cláusulas 6 y 7",
            " · aquí entra la normativa nacional como requisito legal (6.1.3)"),
        3: ("Operación", "cláusula 8", ""),
        4: ("Evaluación", "cláusulas 9 y 10", " · aquí se evalúa el cumplimiento legal (9.1.2)"),
    }
}
NOTA_ESTRUCTURA = {
    "SI-SGCSSMA": (
        "ESTRUCTURA — el curso sigue la estructura de alto nivel de las ISO (Anexo SL). "
        "Bloque 1 = cláusulas 4 a 7 · Bloque 2 = cláusulas 8 a 10. Los indicadores se reparten por tramo de "
        "cláusula y no por norma: cinco sesiones y seis puntos de rúbrica cada uno, sin solapes "
        "(OBS-SI-SGCSSMA-14). CONVENCIÓN DE NOMBRES: el nombre de la sesión es el asunto, después la cláusula, "
        "y entre paréntesis las normas cuando esa cláusula no está en las tres. SIN PARÉNTESIS = la cláusula es "
        "la misma en la ISO 9001, la ISO 14001 y la ISO 45001; se enseña como punto clave de la S1. "
        "PUNTOS CLAVE = momentos de la sesión, en etiqueta corta; entre 3 y 5 por sesión.")
}


def leer(carpeta: Path, nombre: str) -> list[dict]:
    ruta = carpeta / nombre
    if not ruta.exists():
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def ubicar_matriz(curso_id: str) -> Path:
    candidatos = [p for p in REPO.glob("03_Entregables-diseño/**/03_Matriz-de-distribucion.xlsx")
                  if curso_id in p.parent.name]
    if len(candidatos) != 1:
        raise SystemExit("No encuentro una sola matriz para %s (halle %d)" % (curso_id, len(candidatos)))
    return candidatos[0]


def fila_de(ws, texto: str, col: int = 1, exacto: bool = True) -> int | None:
    for r in range(1, ws.max_row + 1):
        v = ws.cell(r, col).value
        if v is None:
            continue
        v = str(v).strip()
        if (v == texto) if exacto else v.startswith(texto):
            return r
    return None


def pintar(ws, fila, cols, hexcol):
    pf = PatternFill("solid", start_color=hexcol, end_color=hexcol)
    for c in cols:
        ws.cell(fila, c).fill = pf


def barra(x: float, ancho: int = 30) -> str:
    llenos = int(round(x * ancho))
    return "▉" * llenos + "·" * (ancho - llenos)


def generar(curso_id: str) -> Path:
    carrera = None
    for r in leer(RAIZ, "cursos.csv"):
        if r["curso_id"] == curso_id:
            carrera = r["sigla"]
    if not carrera:
        raise SystemExit("El curso %s no esta en cursos.csv" % curso_id)
    datos = RAIZ / carrera

    ses = {int(r["nro_sesion"]): r for r in leer(datos, "sesiones.csv") if r["curso_id"] == curso_id}
    if not ses:
        raise SystemExit("No hay sesiones de %s en %s/sesiones.csv" % (curso_id, carrera))
    # Solo los indicadores DE ESTE CURSO. indicadores.csv no tiene columna de curso:
    # el curso va dentro del id, IND-<curso>-<n>. Sin este filtro, la clave era el
    # numero final y el IND-SI-IMPAMB-1 pisaba al IND-SI-SGCSSMA-1: la matriz mostraba
    # los indicadores de otro curso encima de las sesiones de este.
    prefijo = "IND-%s-" % curso_id
    indic = {int(r["indicador_id"].rsplit("-", 1)[-1]): r["descripcion"]
             for r in leer(datos, "indicadores.csv")
             if r["indicador_id"].startswith(prefijo)}
    if not indic:
        raise SystemExit("No hay indicadores de %s en %s/indicadores.csv"
                         % (curso_id, carrera))
    # Las tablas de la carrera guardan las filas de TODOS sus cursos. Se filtran AQUI,
    # al leer, y no en cada uso: basta olvidar un uso para que se cuele otro curso, y
    # eso ya ocurrio dos veces --el contador de avance sumaba sesiones ajenas, y los
    # indicadores de SI-IMPAMB se escribieron encima de los de SI-SGCSSMA--.
    suyo = {r["sesion_id"] for r in ses.values()}
    casos = [c for c in leer(datos, "casos.csv") if c.get("curso_id") == curso_id]
    cotejo = [c for c in leer(datos, "listas_cotejo.csv") if c.get("sesion_id") in suyo]
    conten = [c for c in leer(datos, "contenidos.csv") if c.get("sesion_id") in suyo]
    lams = [l for l in leer(datos, "laminas.csv") if l.get("sesion_id") in suyo]
    rubs = [r for r in leer(datos, "rubricas.csv") if r.get("curso_id") == curso_id]

    xls = ubicar_matriz(curso_id)
    wb = openpyxl.load_workbook(xls)
    ws = wb.active

    f_ses = fila_de(ws, "BLOQUE", 1)
    f_ind = fila_de(ws, "IND-1", 1)
    f_tc = fila_de(ws, "TRABAJO", 1)
    f_av = fila_de(ws, "② Aprendizajes esperados", 1, exacto=False)
    f_ley = fila_de(ws, "LEYENDA", 1, exacto=False)
    f_nota = fila_de(ws, "ESTRUCTURA", 1, exacto=False) or fila_de(ws, "TRIBUTA A", 1, exacto=False)
    if None in (f_ses, f_ind, f_av, f_ley):
        raise SystemExit("No reconozco el formato de la matriz: falta un ancla")
    f_ses += 1

    # ── indicadores de logro
    for i in sorted(indic):
        ws.cell(f_ind + i - 1, 2).value = indic[i]

    # ── los dos colaborativos
    if f_tc:
        mios = [c for c in casos if c.get("alcance") == "colaborativo"
                and c.get("curso_id") == curso_id]
        for k, caso in enumerate(sorted(mios, key=lambda c: c["caso_id"])):
            r = f_tc + 1 + k
            n = len([x for x in rubs if x["caso_id"] == caso["caso_id"]])
            ws.cell(r, 1).value = caso["caso_id"].split("-")[-1]
            ws.cell(r, 2).value = caso.get("destreza") or "—"
            ws.cell(r, 3).value = caso.get("producto", "")[:400]
            ws.cell(r, 11).value = "único" if not caso.get("caso_a") else "A y B"
            ws.cell(r, 12).value = "%d de 5" % n

    # ── las filas de sesion
    for n in sorted(ses):
        r = f_ses + n - 1
        s = ses[n]
        ids = [int(x.split("-")[-1]) for x in s["indicador_id"].split(";") if x.strip()]
        evalua = s["tipo_sesion"] == "evaluacion"
        ws.cell(r, 1).value = "Bloque %s" % s["bloque_id"][-1]
        ws.cell(r, 2).value = "S%d" % n
        ws.cell(r, 3).value = "Evaluación" if evalua else "Adquisición"
        ws.cell(r, 4).value = " · ".join("IND-%d" % i for i in ids)
        ws.cell(r, 5).value = s["tema"]
        ws.cell(r, 6).value = s["aprendizaje_esperado"].strip() or "— pendiente —"
        ws.cell(r, 7).value = s["tributa"].strip() or "—"
        pintar(ws, r, range(1, 8), GRIS if evalua else COLOR[ids[0]])
        if evalua:
            pintar(ws, r, range(8, 13), GRIS)
            for c in range(8, 13):
                ws.cell(r, c).value = "—"
            ws.cell(r, 6).fill = PatternFill("solid", start_color=AMBAR, end_color=AMBAR)
            continue
        sid = s["sesion_id"]
        caso = next((c for c in casos if c.get("sesion_id") == sid), None)
        npk = len([c for c in conten if c.get("sesion_id") == sid])
        nlam = len([l for l in lams if l.get("sesion_id") == sid])
        ncot = len([c for c in cotejo if c.get("sesion_id") == sid])
        vals = ["✔" if caso and caso.get("caso_a") else "—",
                "✔" if caso and caso.get("caso_b") else "—",
                str(ncot) if ncot else "—",
                "%d pk" % npk if npk else "—",
                "%d láms" % nlam if nlam else "—"]
        for i, v in enumerate(vals):
            c = ws.cell(r, 8 + i)
            c.value = v
            col = VERDE if v != "—" else AMBAR
            c.fill = PatternFill("solid", start_color=col, end_color=col)

    # ── leyenda
    rot = ROTULO.get(curso_id)
    if rot:
        for i in sorted(rot):
            nombre, clausulas, extra = rot[i]
            cuenta = sum(1 for s in ses.values() if s["tipo_sesion"] == "adquisicion"
                         and i in [int(x.split("-")[-1]) for x in s["indicador_id"].split(";") if x.strip()])
            rango = [n for n in sorted(ses) if ses[n]["tipo_sesion"] == "adquisicion"
                     and int(ses[n]["indicador_id"].split(";")[0].split("-")[-1]) == i]
            tramo = "S%d–S%d" % (rango[0], rango[-1]) if rango else "—"
            ws.cell(f_ley + i, 1).value = nombre
            ws.cell(f_ley + i, 1).fill = PatternFill("solid", start_color=COLOR[i], end_color=COLOR[i])
            ws.cell(f_ley + i, 2).value = "IND-%d — %s · %s · %s · %d sesiones%s" % (
                i, nombre, clausulas, tramo, cuenta, extra)

    # ── avance sobre las sesiones de adquisicion
    adq = [n for n in ses if ses[n]["tipo_sesion"] == "adquisicion"]
    # Solo las sesiones DE ESTE CURSO. Las tablas de la carrera guardan tambien las de
    # los otros cursos: sin este filtro, una sesion de SI-IMPAMB sumaba al avance de
    # SI-SGCSSMA y la matriz declaraba una sesion mas de las que habia.
    mias = {ses[n]["sesion_id"] for n in adq}

    def suyas(filas, campo=None):
        return [f for f in filas if f.get("sesion_id") in mias and (not campo or f.get(campo))]

    metricas = [
        sum(1 for n in adq if ses[n]["aprendizaje_esperado"].strip()),
        len(suyas(casos, "caso_a")),
        len(suyas(casos, "caso_b")),
        len({c["sesion_id"] for c in suyas(cotejo)}),
        len({c["sesion_id"] for c in suyas(conten)}),
        len({l["sesion_id"] for l in suyas(lams)}),
    ]
    for k, hechas in enumerate(metricas):
        r = f_av + k
        frac = hechas / len(adq)
        ws.cell(r, 2).value = barra(frac)
        ws.cell(r, 11).value = "%d de %d" % (hechas, len(adq))
        c = ws.cell(r, 12)
        c.value = frac
        col = VERDE if frac == 1 else AMBAR2
        c.fill = PatternFill("solid", start_color=col, end_color=col)

    # ── nota de estructura
    if f_nota and curso_id in NOTA_ESTRUCTURA:
        ws.cell(f_nota, 1).value = NOTA_ESTRUCTURA[curso_id]

    try:
        wb.save(xls)
    except PermissionError:
        raise SystemExit("La matriz esta abierta en Excel. Cierrala y vuelve a correr.")

    print("%s  ·  %d sesiones  ·  %s" % (curso_id, len(ses), xls.name))
    etiquetas = ["aprendizajes esperados", "caso A", "caso B", "listas de cotejo", "puntos clave", "PPT"]
    for etq, hechas in zip(etiquetas, metricas):
        print("   %-24s %d de %d" % (etq, hechas, len(adq)))
    return xls


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    generar(sys.argv[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
