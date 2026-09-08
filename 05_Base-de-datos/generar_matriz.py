# -*- coding: utf-8 -*-
"""Matriz de distribución y seguimiento de un curso, desde la base de datos.

    python 05_Base-de-datos/generar_matriz.py EOM-SOST
    python 05_Base-de-datos/generar_matriz.py EOM-METEXP

Escribe 01_Matriz-de-distribucion.xlsx en la carpeta Curso<n>_ del curso, dentro
de 03_Entregables-diseño, con el formato de la matriz de SI-SGCSSMA, que sirvió
de modelo.

Nada se escribe aquí: la capacidad, los indicadores, el reparto de sesiones y el
avance de cada paso del §13 se leen de los CSV. Así el Excel muestra el estado
real y no una intención.
"""
from __future__ import print_function

import csv
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) < 2:
    sys.exit(u"USO · python 05_Base-de-datos/generar_matriz.py <CURSO-ID>   "
             u"por ejemplo EOM-SOST")

CURSO = sys.argv[1].strip().upper()
CARRERA = CURSO.split(u"-")[0]
BASE = os.path.join(RAIZ, u"05_Base-de-datos", CARRERA)
if not os.path.isdir(BASE):
    sys.exit(u"ABORTA · no existe la carpeta de la carrera %s" % CARRERA)

NEGRO = u"FF1A1918"
GRIS = u"FF5E5D59"
FONDO = u"FFF5F4EF"
VERDE = u"FF2E7D32"
ROJO = u"FFB3261E"
BORDE = Border(*[Side(style=u"thin", color=u"FFBFBDB6")] * 4)

COLS = [u"BLOQUE", u"SESIÓN", u"TIPO", u"IND.", u"TEMA", u"APRENDIZAJE ESPERADO",
        u"CASO", u"COTEJO", u"PUNTOS CLAVE", u"PPT"]
ANCHOS = [11, 9, 13, 16, 34, 52, 9, 9, 14, 10]


def leer(nombre, carpeta=BASE):
    ruta = os.path.join(carpeta, nombre)
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def corto(texto, n=60):
    texto = u" ".join((texto or u"").split())
    return texto if len(texto) <= n else texto[:n - 1] + u"…"


def barra(hechos, total, ancho=30):
    llenos = 0 if not total else int(round(ancho * hechos / float(total)))
    return u"▉" * llenos + u"·" * (ancho - llenos)


def _carpeta_curso(curso):
    """03_Entregables-diseño/Curso<n>_<Nombre>, respetando la que ya exista.

    Un curso puede tener mas de una carpeta que termine igual —por ejemplo
    "Curso1_Metodos-de-explotacion" y "EOM-Metodos-de-explotacion"—: conviven a
    proposito y la matriz va siempre a la que empieza por "Curso<n>_".
    """
    import re
    import unicodedata
    salida = os.path.join(RAIZ, u"03_Entregables-diseño")
    nfkd = unicodedata.normalize("NFKD", curso[u"nombre_curso"])
    slug = u"".join(c for c in nfkd if not unicodedata.combining(c)).replace(u" ", u"-")
    slug = re.sub(r"[^A-Za-z0-9\-]", u"", slug)
    if os.path.isdir(salida):
        cand = [h for h in sorted(os.listdir(salida))
                if os.path.isdir(os.path.join(salida, h))
                and u"".join(c for c in unicodedata.normalize("NFKD", h)
                             if not unicodedata.combining(c)).lower().endswith(slug.lower())]
        conpref = [h for h in cand if re.match(r"^Curso\d+_", h)]
        if conpref:
            return os.path.join(salida, conpref[0])
        if cand:
            return os.path.join(salida, cand[0])
    return os.path.join(salida, u"Curso_%s" % slug)


def main():
    curso = next((c for c in leer(u"cursos.csv", os.path.dirname(BASE))
                  if c[u"curso_id"] == CURSO), None)
    if curso is None:
        sys.exit(u"ABORTA · no encuentro %s en cursos.csv" % CURSO)

    salida = os.path.join(_carpeta_curso(curso), u"01_Matriz-de-distribucion.xlsx")

    capacidad = next((c[u"descripcion"] for c in leer(u"capacidades.csv")
                      if c[u"curso_id"] == CURSO), u"—")
    caps = {c[u"capacidad_id"] for c in leer(u"capacidades.csv")
            if c[u"curso_id"] == CURSO}
    indicadores = [i for i in leer(u"indicadores.csv")
                   if i[u"capacidad_id"] in caps]
    sesiones = sorted([s for s in leer(u"sesiones.csv") if s[u"curso_id"] == CURSO],
                      key=lambda s: int(s[u"nro_sesion"]))
    casos = leer(u"casos.csv")
    bloques = leer(u"bloques.csv")
    ae_bloque = {b[u"bloque_id"]: b.get(u"aprendizaje_esperado", u"")
                 for b in bloques if b.get(u"curso_id") == CURSO}
    rubricas = leer(u"rubricas.csv")
    contenidos = leer(u"contenidos.csv")
    laminas = leer(u"laminas.csv")
    cotejos = leer(u"listas_cotejo.csv")

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

    def cuenta(filas, sid):
        return sum(1 for f in filas if f.get(u"sesion_id") == sid)

    wb = Workbook()
    ws = wb.active
    ws.title = u"Distribución"
    for col, ancho in zip(u"ABCDEFGHIJ", ANCHOS):
        ws.column_dimensions[col].width = ancho

    def celda(ref, valor, negrita=False, tam=10, color=NEGRO, fondo=None,
              wrap=True, centro=False, borde=False):
        c = ws[ref]
        c.value = valor
        c.font = Font(name=u"Arial", size=tam, bold=negrita, color=color)
        c.alignment = Alignment(wrap_text=wrap, vertical=u"top",
                                horizontal=u"center" if centro else u"left")
        if fondo:
            c.fill = PatternFill(u"solid", fgColor=fondo)
        if borde:
            c.border = BORDE
        return c

    # ------------------------------------------------------------- cabecera
    ws.merge_cells(u"A1:K1")
    celda(u"A1", u"MATRIZ DE DISTRIBUCIÓN Y SEGUIMIENTO", negrita=True, tam=14)
    ws.row_dimensions[1].height = 24
    ws.merge_cells(u"A2:K2")
    celda(u"A2", u"UNIDAD DIDÁCTICA:  %s" % curso[u"nombre_curso"], negrita=True, tam=11)
    ws.merge_cells(u"A3:K3")
    celda(u"A3", u"%s · %s · %s h · %s créditos · %s sesiones · %s bloques"
          % (curso[u"carrera"], curso[u"curso_id"], curso[u"horas_total"],
             curso[u"creditos"], curso[u"nro_sesiones"], curso[u"nro_bloques"]),
          tam=9, color=GRIS)
    ws.merge_cells(u"A4:K4")
    celda(u"A4", u"SE GENERA DESDE LA BASE DE DATOS (python 05_Base-de-datos/"
                 u"generar_matriz.py %s). No se edita a mano" % CURSO + u": se corrige en los CSV "
                 u"y se vuelve a generar.", tam=8, color=GRIS)
    ws.merge_cells(u"A5:K5")
    celda(u"A5", u"ORDEN DE TRABAJO (§13)", negrita=True, tam=9)
    ws.merge_cells(u"A6:K6")
    celda(u"A6", u"indicadores  →  ①TC1 y TC2  →  ②aprendizajes esperados  →  ③el caso "
                 u"de la sesión  →  ④lista de cotejo  →  ⑤puntos clave  →  ⑥PPT",
          tam=9, color=GRIS)

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

    celda(u"A8", u"INDICADORES", negrita=True, tam=9)
    fila = 8
    for n, ind in enumerate(indicadores, start=1):
        ws.merge_cells(u"B%d:J%d" % (fila, fila))
        celda(u"B%d" % fila, u"IND-%d · %s" % (n, ind[u"descripcion"]), tam=9)
        fila += 1

    # --------------------------------------------- ① los dos colaborativos
    fila += 1
    ws.merge_cells(u"A%d:J%d" % (fila, fila))
    celda(u"A%d" % fila, u"①  LOS DOS COLABORATIVOS — de aquí baja todo lo demás",
          negrita=True, tam=10, fondo=FONDO)
    fila += 1
    for ref, txt in zip([u"A", u"B", u"C", u"I", u"J"],
                        [u"TRABAJO", u"DESTREZA", u"PRODUCTO", u"CASO", u"RÚBRICA"]):
        celda(u"%s%d" % (ref, fila), txt, negrita=True, tam=8, fondo=FONDO, borde=True)
    fila += 1
    for n, c in enumerate(sorted(colaborativos, key=lambda x: x[u"caso_id"]), start=1):
        criterios = sum(1 for r in rubricas if r[u"caso_id"] == c[u"caso_id"])
        celda(u"A%d" % fila, u"TC%d" % n, negrita=True, tam=9, borde=True)
        celda(u"B%d" % fila, (c.get(u"destreza") or u"—"), tam=9, borde=True)
        ws.merge_cells(u"C%d:H%d" % (fila, fila))
        celda(u"C%d" % fila, corto(c.get(u"producto"), 150), tam=8, borde=True)
        tiene_var = bool((c.get(u"caso_a") or u"").strip())
        celda(u"I%d" % fila, u"con caso A/B ✘" if tiene_var else u"único",
              tam=9, centro=True, borde=True,
              color=ROJO if tiene_var else VERDE)
        celda(u"J%d" % fila, u"%d de 5" % criterios, tam=9, centro=True, borde=True,
              color=VERDE if criterios == 5 else ROJO)
        ws.row_dimensions[fila].height = 34
        fila += 1
        ae = ae_bloque.get(c.get(u"bloque_id"), u"")
        celda(u"A%d" % fila, u"aprendizaje del bloque", negrita=True, tam=8,
              color=GRIS, borde=True)
        ws.merge_cells(u"B%d:J%d" % (fila, fila))
        celda(u"B%d" % fila, ae or u"— pendiente —", tam=8,
              color=NEGRO if ae else ROJO, borde=True)
        # el aprendizaje del bloque es largo y va en una celda combinada B:K,
        # asi que la fila se dimensiona por su longitud o queda cortado.
        ws.row_dimensions[fila].height = max(34, 13 * (1 + len(ae) // 150))
        fila += 1

    # ------------------------------------------------ ② a ⑥ · las sesiones
    fila += 1
    ws.merge_cells(u"A%d:J%d" % (fila, fila))
    celda(u"A%d" % fila, u"②  a  ⑥  ·  LAS SESIONES — cada columna es un paso del orden "
                         u"de trabajo", negrita=True, tam=10, fondo=FONDO)
    fila += 1
    cab = fila
    for col, txt in zip(u"ABCDEFGHIJ", COLS):
        celda(u"%s%d" % (col, fila), txt, negrita=True, tam=8, fondo=FONDO,
              centro=col not in u"AEF", borde=True)
    fila += 1

    hechos = {u"ae": 0, u"va": 0, u"cot": 0, u"pk": 0, u"ppt": 0}
    adquisicion = 0

    for s in sesiones:
        sid = s[u"sesion_id"]
        es_adq = s[u"tipo_sesion"] == u"adquisicion"
        if es_adq:
            adquisicion += 1
        caso = por_sesion.get(sid, {})
        n_cot = cuenta(cotejos, sid)
        n_pk = cuenta(contenidos, sid)
        n_ppt = cuenta(laminas, sid)
        ae = (s.get(u"aprendizaje_esperado") or u"").strip()
        # Hay caso cuando estan el relato y el encargo. NO se mide por `caso_a`:
        # en EOM el caso de sesion es uno solo (§13 ③), y esa columna guarda las
        # fichas de datos, que no todas las sesiones necesitan.
        va = bool((caso.get(u"descripcion") or u"").strip()
                  and (caso.get(u"producto") or u"").strip())

        if es_adq:
            if ae:
                hechos[u"ae"] += 1
            if va:
                hechos[u"va"] += 1
            if n_cot:
                hechos[u"cot"] += 1
            if n_pk:
                hechos[u"pk"] += 1
            if n_ppt:
                hechos[u"ppt"] += 1

        ind = s.get(u"indicador_id", u"")
        etq = u" · ".join(u"IND-%s" % i.strip()[-1] for i in ind.split(u";") if i.strip())

        valores = [
            (u"A", u"Bloque %s" % s[u"bloque_id"][-1], NEGRO),
            (u"B", u"S%s" % s[u"nro_sesion"], NEGRO),
            (u"C", u"Adquisición" if es_adq else u"Evaluación", NEGRO),
            (u"D", etq, NEGRO),
            (u"E", s.get(u"tema", u""), NEGRO),
            (u"F", ae if ae else u"— pendiente —", NEGRO if ae else ROJO),
            (u"G", u"✔" if va else u"—", VERDE if va else GRIS),
            (u"H", (u"%d" % n_cot) if n_cot else u"—", VERDE if n_cot else GRIS),
            (u"I", (u"%d pk" % n_pk) if n_pk else u"—", VERDE if n_pk else GRIS),
            (u"J", (u"%d láms" % n_ppt) if n_ppt else u"—", VERDE if n_ppt else GRIS),
        ]
        for col, val, color in valores:
            celda(u"%s%d" % (col, fila), val, tam=8, color=color,
                  centro=col in u"BCDGHIJ", borde=True)
        ws.row_dimensions[fila].height = 30
        fila += 1

    ws.freeze_panes = u"A%d" % (cab + 1)

    # ---------------------------------------------------------- el avance
    fila += 1
    ws.merge_cells(u"A%d:J%d" % (fila, fila))
    celda(u"A%d" % fila, u"AVANCE — sobre las %d sesiones de adquisición" % adquisicion,
          negrita=True, tam=10, fondo=FONDO)
    fila += 1
    pasos = [(u"② Aprendizajes esperados", u"ae"), (u"③ Caso de sesión", u"va"),
             (u"④ Listas de cotejo", u"cot"),
             (u"⑤ Puntos clave", u"pk"), (u"⑥ PPT", u"ppt")]
    for etiqueta, clave in pasos:
        n = hechos[clave]
        celda(u"A%d" % fila, etiqueta, tam=9)
        ws.merge_cells(u"B%d:H%d" % (fila, fila))
        celda(u"B%d" % fila, barra(n, adquisicion), tam=9,
              color=VERDE if n == adquisicion else GRIS)
        celda(u"I%d" % fila, u"%d de %d" % (n, adquisicion), tam=9, centro=True,
              color=VERDE if n == adquisicion else NEGRO)
        celda(u"J%d" % fila, round(n / float(adquisicion), 2) if adquisicion else 0,
              tam=9, centro=True, color=GRIS)
        fila += 1

    # ----------------------------------------------------------- leyenda
    fila += 1
    ws.merge_cells(u"A%d:J%d" % (fila, fila))
    celda(u"A%d" % fila, u"LEYENDA", negrita=True, tam=9)
    fila += 1
    for n, ind in enumerate(indicadores, start=1):
        ses = [s for s in sesiones if ind[u"indicador_id"] in s.get(u"indicador_id", u"")
               and s[u"tipo_sesion"] == u"adquisicion"]
        celda(u"A%d" % fila, u"IND-%d" % n, negrita=True, tam=9)
        ws.merge_cells(u"B%d:J%d" % (fila, fila))
        celda(u"B%d" % fila, u"%s  ·  %d sesiones de adquisición"
              % (corto(ind[u"descripcion"], 110), len(ses)), tam=9, color=GRIS)
        fila += 1
    celda(u"A%d" % fila, u"Evaluación", negrita=True, tam=9)
    ws.merge_cells(u"B%d:J%d" % (fila, fila))
    celda(u"B%d" % fila, u"Sustentación de los colaborativos · no llevan aprendizaje "
                         u"esperado propio: sustentan el del bloque (§13)", tam=9, color=GRIS)
    fila += 2
    ws.merge_cells(u"A%d:J%d" % (fila, fila))
    celda(u"A%d" % fila, u"PUNTOS CLAVE — entre 3 y 5 por sesión, todos con su origen "
                         u"declarado.  ·  PPT — presupuesto de 28 a 32 láminas (§11).",
          tam=8, color=GRIS)

    carpeta = os.path.dirname(salida)
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    try:
        wb.save(salida)
    except IOError:
        sys.exit(u"  ! %s está abierto en Excel: ciérralo y vuelve a generar"
                 % os.path.basename(salida))
    print(u"  ✔ %s" % os.path.relpath(salida, RAIZ))
    print(u"    %d sesiones · %d de adquisición · %d colaborativos"
          % (len(sesiones), adquisicion, len(colaborativos)))
    for etiqueta, clave in pasos:
        print(u"    %-28s %d de %d" % (etiqueta, hechos[clave], adquisicion))


if __name__ == "__main__":
    main()
