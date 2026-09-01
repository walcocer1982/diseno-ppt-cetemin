# -*- coding: utf-8 -*-
"""Genera el PPT de una sesion a partir de laminas.csv.

LA BASE MANDA
    Cada fila de laminas.csv es UNA DIAPOSITIVA — tambien la portada, las
    subportadas y la tapa, no solo el contenido. Su columna `tipo` dice que
    diseno de la plantilla le toca.

    Cambiar el PPT = cambiar el CSV y volver a generar. Nunca al reves.

LA PLANTILLA
    04_Recursos-graficos/comun/plantilla/PLANTILLA-CETEMIN_sesion.pptx
    Va vacia y trae la marca montada: se COPIA, no se edita.

Uso:  python generar_ppt.py EOM-METEXP-S1
"""
from __future__ import annotations

import csv
import shutil
import sys
import unicodedata
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

RAIZ = Path(__file__).resolve().parent
GRAF = RAIZ.parent / "04_Recursos-graficos"
PLANTILLA = GRAF / "comun/plantilla/PLANTILLA-CETEMIN_sesion.pptx"
MARCA, FONDOS = GRAF / "comun/marca", GRAF / "comun/fondos"

# que diseno de la plantilla usa cada tipo de diapositiva (§07)
DISENO = {
    "portada":            "slideLayout3",
    "subportada-sesion":  "slideLayout2",
    "subportada-momento": "slideLayout10",
    "triangulacion":      "slideLayout2",
    "tema":               "slideLayout6",
    "contenido":          "slideLayout13",
    "cotejo":             "slideLayout13",
    "tapa":               "slideLayout3",
}
ILEGALES = tuple(':*?"<>|/\\')
AZUL, AMBAR, BLANCO = RGBColor(0x0D,0x26,0x32), RGBColor(0xFF,0xC5,0x05), RGBColor(0xFF,0xFF,0xFF)
W, H = Inches(13.333), Inches(7.5)


def leer(ruta: Path) -> list[dict]:
    with open(ruta, encoding="utf-8-sig", newline="") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def sin_tildes(t: str) -> str:
    """Nombre de archivo sin tildes ni ñ.

    Windows y Git no coinciden en cómo codifican una tilde, y el resultado es
    que "Métodos" y "Metodos" acaban siendo DOS carpetas para el mismo curso.
    Ya pasó una vez.
    """
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    for c in ILEGALES:                 # no pueden ir en un nombre de archivo Windows
        t = t.replace(c, "")
    return "-".join(t.split()).strip("-")


def puntos_de(sesion_id: str, carrera: str) -> list[dict]:
    return [c for c in leer(RAIZ / carrera / "contenidos.csv") if c["sesion_id"] == sesion_id]


def punto_de(l: dict, sesion_id: str, carrera: str) -> dict | None:
    """El punto clave que desarrolla esta lamina.

    Se busca por `contenido_id`, NO por parecido de titulo. Emparejar por
    titulo hacia que renombrar una lamina la dejara muda sin avisar: paso con
    cuatro laminas de la Adquisicion al ampliarla.
    """
    cid = l.get("contenido_id", "").strip()
    if not cid:
        return None
    pk = next((p for p in puntos_de(sesion_id, carrera) if p["contenido_id"] == cid), None)
    if pk is None:
        # Una lamina NO puede crear un punto clave. Cuando falta, la salida no
        # es inventarlo: es cambiar la lamina o pedir que se apruebe el
        # contenido. Asi se rompio la cadena que produjo «La guardia».
        raise SystemExit(f"ERROR · la lamina «{l['titulo']}» apunta a {cid}, "
                         f"que no existe en contenidos.csv de {sesion_id}. "
                         f"Una lamina no crea contenido: corrige la lamina "
                         f"       Una lamina no crea contenido: corrige la lamina "
                         f"o carga el punto clave con su `origen` y su aprobacion.")
    return pk


def bajada_de(l: dict, sesion_id: str, carrera: str) -> str:
    """Las ideas de ESTA lamina.

    Si la lamina declara `idea` (1, 2, 3 o `1-2`), toma esa parte del
    desarrollo del punto clave. Sin `idea`, las toma todas. Asi dos laminas
    que comparten punto clave no muestran lo mismo, y el texto sigue viviendo
    en un solo sitio.
    """
    """Las ideas que el instructor tiene que desarrollar en esta lamina.

    Viven SOLO en contenidos.csv (columna `desarrollo`). Tenerlas tambien en
    laminas.csv daba dos versiones del mismo texto y una se quedaba vieja.
    """
    p = punto_de(l, sesion_id, carrera)
    if not p:
        return ""
    if p.get("desarrollo", "").strip():
        ideas = [x.strip() for x in p["desarrollo"].split("|") if x.strip()]
        cual = l.get("idea", "").strip()
        if cual:
            pedidas = []
            for tramo in cual.split(","):
                if "-" in tramo:
                    a, b = tramo.split("-")
                    pedidas += list(range(int(a), int(b) + 1))
                else:
                    pedidas.append(int(tramo))
            ideas = [ideas[i - 1] for i in pedidas if 1 <= i <= len(ideas)]
        return chr(10).join("·  " + x for x in ideas)
    _, _, resto = p["contenido"].partition(":")
    return " · ".join(x.strip() for x in resto.split(",") if x.strip())


def revisar(laminas: list[dict], imgs: dict, sesion_id: str, carrera: str) -> list[str]:
    """En ADQUISICION toda lamina lleva imagen Y contenido. Es regla, no aviso.

    Una lamina de adquisicion sin imagen no ensena nada que no se pueda decir
    hablando; sin contenido deja al instructor sin de que agarrarse. Las dos
    faltas son invisibles en la base y saltan recien al proyectar.
    """
    avisos = []
    for l in laminas:
        if l["momento"] != "adquisicion" or l["tipo"] not in ("tema", "contenido"):
            continue
        if not bajada_de(l, sesion_id, carrera).strip():
            avisos.append(f"{l['titulo']} — SIN CONTENIDO (falta contenido_id o su desarrollo)")
        im = imgs.get(l.get("imagen_id", ""))
        if not im:
            avisos.append(f"{l['titulo']} — SIN IMAGEN")
        elif im.get("estado") != "aprobada":
            avisos.append(f"{l['titulo']} — imagen {im['imagen_id']} entra, pero sin firmar "
                          f"({im.get('estado','?')}) · fírmalas con: python aprobar_imagenes.py {carrera}")
    n = len(puntos_de(sesion_id, carrera))
    if not 3 <= n <= 5:
        avisos.append(f"la sesión tiene {n} puntos clave; el molde son 3 a 5 (§07)")
    sin_origen = [p["contenido_id"] for p in puntos_de(sesion_id, carrera)
                  if not p.get("origen", "").strip()]
    if sin_origen:
        avisos.append(f"puntos clave sin `origen` declarado: {', '.join(sin_origen)}")
    total = sum(int(l["minutos"] or 0) for l in laminas)
    if total != 135:
        avisos.append(f"la sesión suma {total} min, no 135")
    return avisos


def colocar(s, ruta: Path, x, y, w, h) -> None:
    """Encaja la imagen dentro del hueco sin deformarla ni desbordarlo."""
    from PIL import Image
    with Image.open(ruta) as im:
        prop = im.width / im.height
    if prop > w / h:
        ancho, alto = w, w / prop
    else:
        alto, ancho = h, h * prop
    s.shapes.add_picture(str(ruta), Inches(x + (w - ancho) / 2),
                         Inches(y + (h - alto) / 2), Inches(ancho), Inches(alto))


def cuerpo_de(l: dict, act: dict | None) -> str:
    """El texto de la lamina; si no lo trae, la actividad del plan."""
    c = l.get("texto", "")
    return c if c.strip() else (act.get("actividad", "") if act else "")


def nota(s, *bloques: str) -> None:
    """Escribe las notas del orador.

    Lo que se aprendio verificando —por que el desatado no es operacion
    unitaria, por que la periferia sale junta— no puede quedarse solo en
    observaciones.csv: el instructor lo necesita frente a la lamina, y no va a
    abrir un CSV en clase. La diapositiva muestra QUE; la nota dice POR QUE.
    """
    t = "\n\n".join(b.strip() for b in bloques if b and b.strip())
    if t:
        s.notes_slide.notes_text_frame.text = t


# Bandas de tamano acordadas con el instructor lider (31/08/2026): los titulos
# van entre 36 y 40 pt y el cuerpo entre 20 y 24. No es preferencia estetica:
# por debajo de eso el texto no se lee al proyectar en una sesion virtual.
TITULO_MAX, TITULO_MIN = 40, 36
CUERPO_MAX, CUERPO_MIN = 24, 20


def cabe(t, size, w_in, h_in, ls=1.15):
    """Estima si el texto entra en la caja a ese cuerpo.

    Un caracter ocupa ~0.50*size pt de ancho y cada linea ls*1.2*size pt de
    alto. Es estimacion para ELEGIR el tamano, no medida al pixel.
    """
    por_linea = max(1, int(w_in / (0.50 * size / 72.0)))
    lineas = sum(max(1, -(-len(p) // por_linea)) for p in str(t).split(chr(10)))
    return lineas * ls * 1.2 * size / 72.0 <= h_in


def ajustar(t, w_in, h_in, maximo, minimo, ls=1.15):
    """Mayor tamano de la banda con el que el texto cabe; nunca baja del minimo."""
    size = maximo
    while size > minimo and not cabe(t, size, w_in, h_in, ls):
        size -= 1
    return size


def texto(s, x, y, w, h, t, size, color=AZUL, bold=True, al=PP_ALIGN.LEFT, ls=1.15,
          banda=None):
    if banda == 'titulo':
        size = ajustar(t, w, h, TITULO_MAX, TITULO_MIN, ls)
    elif banda == 'cuerpo':
        size = ajustar(t, w, h, CUERPO_MAX, CUERPO_MIN, ls)
    tf = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)).text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for i, linea in enumerate(str(t).split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = linea
        p.alignment = al
        p.line_spacing = ls
        for r in p.runs:
            r.font.size = Pt(size); r.font.bold = bold
            r.font.color.rgb = color; r.font.name = "Oswald"


# ── Los cinco de siempre (§13 ④) ─────────────────────────────────────────
# Cinco items binarios, cuatro puntos cada uno. Identicos en los 35 cursos: lo que
# cambia por sesion es la concrecion del item 1, que vive en listas_cotejo.csv.
COTEJO = [
    ("COMPLETO", "ningún paso del encargo, ninguna fila ni casilla sin resolver"),
    ("CON LOS DATOS DEL CASO", "cada afirmación se apoya en un dato; ninguna sale de suponer"),
    ("CON EL TÉRMINO CORRECTO", "los términos de la sesión aparecen, y bien usados"),
    ("CON EL PORQUÉ", "la norma, la causa o la consecuencia que lo sustenta"),
    ("SUSTENTADO POR TODOS", "cada integrante expone, y responde sobre lo que no expuso"),
]
COTEJO_ESCALA = ("5 de 5   →   20\n"
                 "4 de 5   →   16\n"
                 "3 de 5   →   12\n"
                 "2 de 5   →     8\n"
                 "1 de 5   →     4\n"
                 "0 de 5   →     0")

LISTA = ("aprobada", "verificada")  # la barra del CLAUDE.md: verificada basta para colocarla


def colocable(im: dict | None, estricto: bool = False) -> bool:
    """¿Esta imagen puede ir en la lámina? Verificada basta; con --estricto hace falta la firma."""
    if not im:
        return False
    return im.get("estado") == "aprobada" or (not estricto and im.get("estado") in LISTA)


def destino(carrera: str, ses: dict, curso: dict) -> Path:
    """Donde va el PPT. Manda la carpeta del curso si existe — es donde el equipo los busca.

    Y si ya hay un PPT de esa sesion, se reusa SU nombre: se actualiza el archivo, no se crea
    uno al lado con otro titulo. La regla es del §13: nunca se duplica un entregable.
    """
    base = RAIZ.parent / "03_Entregables-diseño"
    for ciclo in sorted(base.glob(f"{carrera} - Ciclo *")):
        for cur in sorted(ciclo.glob(f"* - {curso['curso_id']} - *")):
            carpeta = cur / "PPT"
            if carpeta.is_dir():
                previos = sorted(carpeta.glob(f"S{ses['nro_sesion']}_*.pptx"))
                if previos:
                    return previos[0]
                return carpeta / f"S{ses['nro_sesion']}_{sin_tildes(ses['tema'][:40])}.pptx"
    return (base / f"{carrera}-{sin_tildes(curso['nombre_curso'])}" /
            f"S{ses['nro_sesion']}_{sin_tildes(ses['tema'][:40])}.pptx")


def generar(sesion_id: str, salida: Path | None = None, estricto: bool = False) -> Path:
    carrera = sesion_id.split("-")[0]
    laminas = sorted([l for l in leer(RAIZ / carrera / "laminas.csv")
                      if l["sesion_id"] == sesion_id], key=lambda r: int(r["orden"]))
    if not laminas:
        raise SystemExit(f"No hay laminas para {sesion_id} en {carrera}/laminas.csv")

    ses = next(s for s in leer(RAIZ / carrera / "sesiones.csv") if s["sesion_id"] == sesion_id)
    curso = next(c for c in leer(RAIZ / "cursos.csv") if c["curso_id"] == ses["curso_id"])
    imgs = {i["imagen_id"]: i for i in leer(RAIZ / "imagenes.csv")}

    salida = salida or destino(carrera, ses, curso)
    salida.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(PLANTILLA, salida)

    prs = Presentation(salida)
    LAY = {l.part.partname.split("/")[-1].replace(".xml", ""): l
           for m in prs.slide_masters for l in m.slide_layouts}

    def nueva(tipo, alterno=False):
        s = prs.slides.add_slide(LAY['slideLayout13' if alterno else DISENO[tipo]])
        for ph in list(s.placeholders):      # fuera los "Haga clic para agregar titulo"
            ph._element.getparent().remove(ph._element)
        return s

    acts = [a for a in leer(RAIZ / carrera / "actividades.csv")
            if a.get("sesion_id") == sesion_id] if (RAIZ / carrera / "actividades.csv").exists() else []

    n_tema = 0
    for l in laminas:
        t = l["tipo"]
        alterno = t == "tema" and (n_tema + 1) % 2 == 0
        s = nueva(t, alterno)

        # Notas del orador: que se hace en este momento (plan 003A) y que hay
        # detras de la imagen que se esta proyectando (imagenes.csv).
        im = imgs.get(l.get("imagen_id", ""))
        # La lamina de tema desarrolla SU punto clave; las demas siguen la
        # actividad del momento. Emparejar todo por momento hacia que la lamina
        # de VOLADURA llevara la nota del ciclo de minado.
        if t == "tema":
            pk = punto_de(l, sesion_id, carrera)
            que = pk["contenido"] if pk else ""
            rutina = ""
        else:
            act = next((a for a in acts if a.get("momento") == l.get("momento")
                        and a.get("rutina")), None) or \
                  next((a for a in acts if a.get("momento") == l.get("momento")), None)
            que = act.get("actividad", "") if act else ""
            rutina = f"Rutina: {act['rutina']}" if act and act.get("rutina") else ""
        nota(s,
             f"[{l['momento'].upper()} · {l['minutos']} min]" if l.get("momento") else "",
             que, rutina,
             (im.get("descripcion", "") if im else ""),
             (f"Fuente de la imagen: {im['fuente']}" if im and im.get("fuente") else ""))

        if t == "portada":
            s.shapes.add_picture(str(FONDOS / "01_portada.jpg"), 0, 0, W, H)
            texto(s, 0.52, 2.94, 5.56, 1.72, curso["nombre_curso"].upper(), 32, BLANCO, True, PP_ALIGN.LEFT, 1.15)
            texto(s, 0.52, 4.56, 6.19, 0.56, l["texto"] or "SEDE ABQ", 20, AMBAR)

        elif t == "tapa":
            s.shapes.add_picture(str(FONDOS / "03_tapa.jpg"), 0, 0, W, H)

        elif t == "subportada-sesion":
            b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.13), Inches(1.45), Inches(0.10), Inches(1.84))
            b.fill.solid(); b.fill.fore_color.rgb = AMBAR; b.line.fill.background()
            texto(s, 0.21, 0.97, 5.72, 2.59, f"Unidad Didáctica\n{curso['nombre_curso'].upper()}",
                  27, AZUL, True, PP_ALIGN.RIGHT)
            texto(s, 6.32, 1.08, 4.91, 1.91, f"{l['titulo']}\n{l['texto'].upper()}", 27)
            texto(s, 2.03, 3.44, 3.90, 0.38, curso["carrera"].upper(), 16, AZUL, False, PP_ALIGN.RIGHT)
            s.shapes.add_picture(str(MARCA / "si_triangulacion-icono.png"), Inches(4.86), Inches(3.90), Inches(2.58))

        elif t == "subportada-momento":
            ico = MARCA / f"si_{l['momento'].upper()}.png"
            if not ico.exists():
                ico = MARCA / f"si_{l['titulo'].replace('Ó','O').replace('Ú','U')}.png"
            if ico.exists():
                s.shapes.add_picture(str(ico), Inches(5.62), Inches(1.83), Inches(2.08), Inches(2.08))
            texto(s, 2.91, 4.43, 7.51, 1.08, l["titulo"], 80, BLANCO, True, PP_ALIGN.CENTER)

        elif t == "triangulacion":
            # Las TRES zonas arrancan a la misma altura. El icono generico de
            # banco de imagenes se fue: no dice nada y desentona con la marca.
            texto(s, 3.80, 0.66, 5.95, 0.72, "APRENDIZAJE PREVISTO", 30, AZUL, True, PP_ALIGN.CENTER)
            texto(s, 1.40, 1.38, 10.36, 1.34,
                  # El aprendizaje esperado baja del indicador y viene en TERCERA
                  # persona ("Describe qué es…"). Con el encabezado antiguo
                  # —"Al finalizar la sesion podremos…"— la frase no concordaba.
                  "Al finalizar la sesión, el estudiante:" + chr(10) + ses["aprendizaje_esperado"],
                  19, AZUL, False, PP_ALIGN.CENTER, 1.20, banda="cuerpo")
            b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.47), Inches(2.72), Inches(10.22), Inches(0.035))
            b.fill.solid(); b.fill.fore_color.rgb = AMBAR; b.line.fill.background()
            for x, titulo in ((0.55, "PUNTOS CLAVES"), (7.20, "EVALUACIÓN")):
                texto(s, x - 0.05, 3.02, 5.25, 0.62, titulo, 26, AZUL, True, PP_ALIGN.LEFT)
            # en esta zona va el TITULO corto del punto clave, no el punto entero
            puntos = [p["contenido"] for p in puntos_de(sesion_id, carrera)]
            texto(s, 0.55, 3.62, 5.25, 2.55,
                  chr(10).join("•  " + p for p in puntos), 13, AZUL, False, PP_ALIGN.LEFT, 1.25,
                  banda="cuerpo")
            caso = next((c for c in leer(RAIZ / carrera / "casos.csv")
                         if c["bloque_id"] == ses["bloque_id"]), None)
            texto(s, 7.20, 3.62, 5.25, 2.55,
                  (caso.get("evaluacion_lamina") or caso.get("producto", "")[:190] if caso
                   else "Actividad de aplicación de la sesión."),
                  15, AZUL, False, PP_ALIGN.LEFT, 1.25, banda="cuerpo")

        elif t == "tema":
            # DOS DISENOS que se turnan. No se puede espejar el panel: viene del
            # fondo del patron, y repintarlo encima tapa la escuadra y el logo.
            # Asi que la variedad es de TIPO, no de lado.
            n_tema += 1
            if n_tema % 2 == 1:
                # A · panel oscuro a la izquierda, imagen a la derecha
                texto(s, 0.43, 1.60, 5.67, 1.60, l["titulo"], 30, BLANCO, True, PP_ALIGN.CENTER, 1.2,
                      banda="titulo")
                b = bajada_de(l, sesion_id, carrera) or l["texto"]
                if b:
                    texto(s, 0.62, 3.35, 5.35, 3.30, b, 14, AMBAR, False, PP_ALIGN.LEFT, 1.30,
                          banda="cuerpo")
                hueco = (6.55, 0.85, 6.15, 5.85)
            else:
                # B · fondo claro en DOS COLUMNAS: imagen a la izquierda, texto
                # a la derecha. El titulo arriba con la imagen debajo dejaba la
                # lamina partida en bandas y la imagen chica.
                texto(s, 6.90, 1.15, 5.90, 1.55, l["titulo"], 30, AZUL, True, PP_ALIGN.LEFT, 1.15,
                      banda="titulo")
                b = bajada_de(l, sesion_id, carrera) or l["texto"]
                if b:
                    texto(s, 6.90, 2.85, 5.85, 3.55, b, 14, AZUL, False, PP_ALIGN.LEFT, 1.30,
                          banda="cuerpo")
                hueco = (0.55, 1.15, 5.90, 5.20)
            im2 = im if colocable(im, estricto) else None
            if im2 and (RAIZ.parent / im2["archivo"]).exists():
                colocar(s, RAIZ.parent / im2["archivo"], *hueco)

        elif t == "cotejo":
            # La misma lamina en las 24 sesiones y en las tres carreras: el alumno
            # se aprende los cinco de tanto verlos. Solo cambia la linea de abajo.
            texto(s, 0.92, 0.62, 11.5, 0.90, "Los cinco de siempre", 28, AZUL, True,
                  PP_ALIGN.CENTER, banda="titulo")
            texto(s, 0.85, 1.52, 8.20, 0.44,
                  "Con cuatro de cinco, apruebas. Con tres, no.", 16, AZUL, True, PP_ALIGN.LEFT)
            texto(s, 0.85, 2.05, 8.20, 3.60,
                  chr(10).join("%d · %s — %s" % (i, n, r) for i, (n, r) in enumerate(COTEJO, 1)),
                  15, AZUL, False, PP_ALIGN.LEFT, 1.45, banda="cuerpo")
            b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(9.45), Inches(2.05),
                                   Inches(0.035), Inches(3.40))
            b.fill.solid(); b.fill.fore_color.rgb = AMBAR; b.line.fill.background()
            texto(s, 9.85, 2.05, 2.70, 3.60, COTEJO_ESCALA, 15, AZUL, False, PP_ALIGN.LEFT, 1.45)
            concrecion = next((c.get("observable", "") for c in leer(RAIZ / carrera / "listas_cotejo.csv")
                               if c.get("sesion_id") == sesion_id), "") \
                if (RAIZ / carrera / "listas_cotejo.csv").exists() else ""
            if concrecion:
                texto(s, 0.85, 5.80, 11.60, 1.00,
                      "Hoy, «completo» es:  " + concrecion, 14, AZUL, False, PP_ALIGN.LEFT, 1.25,
                      banda="cuerpo")
            continue

        else:  # contenido
            con_img = colocable(im, estricto) and (RAIZ.parent / im["archivo"]).exists()
            if con_img:
                # texto a la izquierda, evidencia a la derecha
                texto(s, 0.85, 0.80, 5.60, 1.20, l["titulo"], 26, AZUL, True, PP_ALIGN.LEFT,
                      banda="titulo")
                texto(s, 0.88, 2.15, 5.60, 4.10, cuerpo_de(l, act), 14,
                      AZUL, False, PP_ALIGN.LEFT, 1.35, banda="cuerpo")
                colocar(s, RAIZ.parent / im["archivo"], 6.85, 1.35, 6.00, 4.70)
                continue
            texto(s, 0.92, 0.72, 11.5, 0.95, l["titulo"], 28, AZUL, True, PP_ALIGN.CENTER,
                  banda="titulo")
            cuerpo = l["texto"]
            # En APLICACION la consigna completa vive en el plan de sesion: el
            # instructor tiene que poder leerla tal cual, no resumida.
            # el cuerpo es el de la LAMINA; la consigna completa del plan va a
            # las notas del orador. Preferir la mas larga ponia en la lamina 16
            # el texto de otra actividad.
            if not cuerpo.strip() and act:
                cuerpo = act.get("actividad", "")
            bloques = [b.strip() for b in cuerpo.split(chr(10) + chr(10)) if b.strip()]
            if len(bloques) == 2 and len(cuerpo) > 180:
                # dos bloques: el primero es el dato (a la izquierda, ambar),
                # el segundo la instruccion (a la derecha). Antes se apilaba
                # todo a la izquierda y media lamina quedaba vacia.
                texto(s, 0.95, 2.00, 5.30, 3.60, bloques[0], 16, AZUL, True, PP_ALIGN.LEFT, 1.35,
                      banda="cuerpo")
                b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.45), Inches(2.15),
                                       Inches(0.035), Inches(3.20))
                b.fill.solid(); b.fill.fore_color.rgb = AMBAR; b.line.fill.background()
                texto(s, 6.90, 2.00, 5.60, 3.60, bloques[1], 15, AZUL, False, PP_ALIGN.LEFT, 1.35,
                      banda="cuerpo")
            else:
                largo = len(cuerpo) > 220
                texto(s, 1.4, 1.90, 10.5, 3.90, cuerpo, 15,
                      AZUL, False, PP_ALIGN.LEFT if largo else PP_ALIGN.CENTER, 1.35,
                      banda="cuerpo")

    prs.save(salida)
    for a in revisar(laminas, imgs, sesion_id, carrera):
        print(f"  !!  {a}")
    return salida


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sid = args[0] if args else "EOM-METEXP-S1"
    # Por defecto entra lo VERIFICADO, que es la barra del CLAUDE.md. --estricto exige
    # ademas la firma del instructor lider, para el entregable que se manda a revision.
    estricto = "--estricto" in sys.argv
    f = generar(sid, estricto=estricto)
    p = Presentation(f)
    print(f"{f.relative_to(RAIZ.parent)}\n{len(p.slides)} diapositivas · {f.stat().st_size//1024//1024} MB")
