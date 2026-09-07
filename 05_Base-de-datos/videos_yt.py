# -*- coding: utf-8 -*-
"""Videos de YouTube para los recursos de aprendizaje autonomo.

    LA DOCTRINA ESTA EN  00_Base-de-conocimiento/16_RECURSOS-AUTONOMOS-Y-VIDEO.md

Ahi viven los criterios de admision de un video, el reparto de los 90 min, como
se verifica y por que. Aqui NO se repiten: cuando el mismo criterio se escribe
en dos sitios se desincronizan en silencio, que es justo lo que paso con el
"dos CV al 5 %" del §14, escrito a la vez en la doctrina y dentro de
cotejo_excel.py. Si cambias un criterio, cambialo en el §16.

Lo que este script hace, y lo que NO:

    MIDE. Imprime senales para descartar rapido -- duracion, ritmo, silencios,
    deicticos -- y contrasta el vocabulario del aprendizaje esperado contra la
    transcripcion.

    NO APRUEBA. Quien firma `verificado_por` es el instructor lider, despues de
    ver el video. Lo que el numero no caza -- los rotulos en pantalla, que no
    estan en la transcripcion, la calidad de la animacion, piezas de mas o de
    menos -- se ve mirando.

    Y NO ESCRIBE EL ANEXO. `anexo` saca un BORRADOR para reescribir. La sintesis
    del cuadernillo es nuestra, no una copia del video (§16).

Antes de usarlo, la regla que mas ahorra y que no esta en el codigo:
VER PRIMERO EN EL NAVEGADOR, BAJAR DESPUES. Buscar y ver es gratis y descarta el
80 % en diez segundos. Solo se baja la transcripcion de los 2 o 3 finalistas, y
solo si `videos.csv` no la tiene ya. Con ese orden un CV cuesta 3 o 4 consultas.

Defensas contra el bloqueo de YouTube (que es POR IP -- de ahi que la cuota vaya
por instructor, cada uno en su maquina), por orden de eficacia:

    - cache obligatoria: nada se pide dos veces
    - una pasada por video, no tres llamadas sueltas
    - cuota diaria por instructor (CUOTA_DIA)
    - pausa de 3-6 s con variacion aleatoria
    - freno duro al primer bloqueo: insistir alarga la sancion

La cache y el contador van a 01_Insumos/, que no se versiona: material del canal
y datos de una maquina. Al repo van `videos.csv` -- la verificacion, que es lo
que se comparte -- y la sintesis dentro del cuadernillo.

Uso:
    python videos_yt.py bajar <URL|id> [<URL|id> ...]   baja y cachea
    python videos_yt.py evaluar <id> [--sesion SES]     senales + contraste
    python videos_yt.py anexo <id> [--min 0:30-3:00]    borrador de sintesis
    python videos_yt.py pegar <id> <archivo.txt>        salida de emergencia
    python videos_yt.py revisar                         siguen vivos los enlaces?
    python videos_yt.py cuota                           cuanto queda hoy
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import random
import re
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAIZ = BASE.parent
CACHE = RAIZ / "01_Insumos" / "transcripciones"
CUOTA_ARCHIVO = CACHE / "_cuota.json"
VIDEOS = BASE / "videos.csv"

PAUSA = (3.0, 6.0)   # segundos entre peticiones, con variacion aleatoria
CUOTA_DIA = 20       # consultas por dia y por instructor (= por IP)
AVISO = 12           # a partir de aqui se avisa de lo que queda
TOPE_CORRIDA = 15    # videos por invocacion

# Errores del subtitulo automatico en vocabulario tecnico. Se corrigen ANTES de
# que el texto llegue al cuadernillo: un error aqui viaja al banco de preguntas
# y de ahi al estudiante. Ampliar conforme aparezcan.
GLOSARIO = {
    r"\bcut and film\b": "cut and fill",
    r"\bsublevels?\s+stoking\b": "sublevel stoping",
    r"\bor bodies\b": "ore bodies",
}

DEICTICOS = re.compile(
    r"\b(aqu[ií]|ac[aá]|vemos|veamos|observam\w*|observen|noten|fij[eé]nse|"
    r"esta (figura|imagen|animaci\w+|diapositiva|l[aá]mina)|se muestra|"
    r"como se (ve|observa|aprecia)|"
    r"en (la|el) (figura|imagen|esquema|gr[aá]fico|l[aá]mina)|"
    r"we (can )?see|as (you can )?see|as shown|here we|this (figure|image|slide))\b",
    re.I,
)


# --- cuota -----------------------------------------------------------------

def cuota_estado() -> tuple[int, int]:
    """(gastadas hoy, restantes). El contador se reinicia cada dia."""
    hoy = dt.date.today().isoformat()
    if CUOTA_ARCHIVO.exists():
        d = json.loads(CUOTA_ARCHIVO.read_text(encoding="utf-8"))
        if d.get("fecha") == hoy:
            return d.get("consultas", 0), max(0, CUOTA_DIA - d.get("consultas", 0))
    return 0, CUOTA_DIA


def cuota_gastar(n: int = 1):
    hoy = dt.date.today().isoformat()
    gastadas, _ = cuota_estado()
    CACHE.mkdir(parents=True, exist_ok=True)
    CUOTA_ARCHIVO.write_text(
        json.dumps({"fecha": hoy, "consultas": gastadas + n}), encoding="utf-8"
    )


def cuota_exigir(n: int = 1):
    gastadas, quedan = cuota_estado()
    if quedan < n:
        raise SystemExit(
            f"\nCuota diaria agotada ({gastadas}/{CUOTA_DIA} consultas hoy).\n"
            "  No es un capricho: el bloqueo de YouTube es por IP, y esta cuota\n"
            "  es lo que mantiene tu IP limpia. Se reinicia manana.\n"
            "  Si de verdad hace falta hoy: el boton 'Mostrar transcripcion' de\n"
            "  YouTube y luego `python videos_yt.py pegar <id> <archivo.txt>`,\n"
            "  que no toca la red.\n"
        )
    if quedan <= CUOTA_DIA - AVISO:
        print(f"  [cuota] quedan {quedan} consultas hoy")


# --- utilidades ------------------------------------------------------------

def salida_utf8():
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace")


def id_de(txt: str) -> str:
    """Acepta URL completa, URL corta, /shorts/, /embed/ o el id pelado."""
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", txt)
    if m:
        return m.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", txt):
        return txt
    raise SystemExit(f"No reconozco el video: {txt}")


def ruta_cache(vid: str) -> Path:
    return CACHE / f"{vid}.json"


def leer_cache(vid: str):
    p = ruta_cache(vid)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def guardar_cache(vid: str, datos: dict):
    CACHE.mkdir(parents=True, exist_ok=True)
    ruta_cache(vid).write_text(json.dumps(datos, ensure_ascii=False, indent=1),
                               encoding="utf-8")


def corregir(texto: str) -> tuple[str, list[str]]:
    aplicados = []
    for patron, bueno in GLOSARIO.items():
        nuevo, n = re.subn(patron, bueno, texto, flags=re.I)
        if n:
            aplicados.append(f"{patron} -> {bueno}  ({n})")
            texto = nuevo
    return texto, aplicados


def mmss(seg: float) -> str:
    return f"{int(seg) // 60}:{int(seg) % 60:02d}"


def a_segundos(t: str) -> int:
    partes = [int(x) for x in t.strip().split(":")]
    return sum(v * 60 ** i for i, v in enumerate(reversed(partes)))


# --- descarga --------------------------------------------------------------

def bajar(vid: str, traducir: str | None = "es") -> dict:
    """UNA pasada por video: pistas + original + traduccion, y se cachea.

    Si ya esta en cache no toca la red ni gasta cuota.
    """
    ya = leer_cache(vid)
    if ya:
        return ya

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api._errors import (
            IpBlocked, RequestBlocked, TranscriptsDisabled, NoTranscriptFound,
        )
    except ImportError:
        raise SystemExit("Falta la libreria:  pip install youtube-transcript-api")

    cuota_exigir(2)
    api = YouTubeTranscriptApi()

    try:
        lista = api.list(vid)
        pistas = [{"idioma": t.language_code, "auto": t.is_generated,
                   "traducible": t.is_translatable} for t in lista]

        pista = None
        for pref in (["es", "es-419", "es-PE"], ["en", "en-US", "en-GB"]):
            try:
                pista = lista.find_transcript(pref)
                break
            except Exception:
                continue
        if pista is None:
            pista = next(iter(lista), None)
        if pista is None:
            raise SystemExit(f"{vid}: no tiene ninguna pista de subtitulos.")

        frag = [{"t": f.start, "d": f.duration, "txt": f.text}
                for f in pista.fetch()]
        cuota_gastar(2)

        datos = {"video_id": vid, "pistas": pistas,
                 "idioma": pista.language_code, "auto": pista.is_generated,
                 "fragmentos": frag, "traducido": None,
                 "bajado": dt.date.today().isoformat()}

        # La traduccion es lo que resuelve el video en ingles: YouTube la sirve
        # igual que el menu "Traducir automaticamente" de la pagina.
        if (traducir and not pista.language_code.startswith(traducir)
                and pista.is_translatable
                and any(x.language_code == traducir
                        for x in pista.translation_languages)):
            cuota_exigir(1)
            time.sleep(random.uniform(*PAUSA))
            datos["traducido"] = [{"t": f.start, "d": f.duration, "txt": f.text}
                                  for f in pista.translate(traducir).fetch()]
            cuota_gastar(1)

        guardar_cache(vid, datos)
        return datos

    except (IpBlocked, RequestBlocked) as e:
        raise SystemExit(
            f"\nYouTube bloqueo la IP al pedir {vid}.\n"
            "  NO reintentes ahora: insistir alarga la sancion. Espera un rato.\n"
            "  Mientras tanto:\n"
            "    yt-dlp --write-auto-subs --sub-langs \"es,en\" --skip-download "
            f"https://youtu.be/{vid}\n"
            "    o el boton 'Mostrar transcripcion' en YouTube y luego\n"
            f"    python videos_yt.py pegar {vid} <archivo.txt>\n"
        ) from e
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        raise SystemExit(
            f"{vid}: el canal no ofrece subtitulos utilizables.\n"
            "  Si el video vale la pena, transcribe el audio con faster-whisper."
        ) from e


def frags(datos: dict, es: bool = True):
    """Los fragmentos en espanol si los hay; si no, los originales."""
    if es and datos.get("traducido"):
        return datos["traducido"]
    return datos["fragmentos"]


def senales(datos: dict) -> dict:
    f = frags(datos)
    if not f:
        return {}
    dur = f[-1]["t"] + f[-1]["d"]
    texto = " ".join(x["txt"] for x in f)
    huecos = [b["t"] - (a["t"] + a["d"]) for a, b in zip(f, f[1:])
              if b["t"] - (a["t"] + a["d"]) > 2.0]
    pal = len(texto.split())
    deic = len(DEICTICOS.findall(texto))
    return {"duracion": dur, "palabras": pal,
            "pal_min": pal / (dur / 60) if dur else 0,
            "silencios": len(huecos),
            "pct_silencio": sum(huecos) / dur * 100 if dur else 0,
            "deicticos": deic,
            "deic_10min": deic / (dur / 600) if dur else 0}


# --- subcomandos -----------------------------------------------------------

def cmd_bajar(args):
    ids = [id_de(x) for x in args.videos]
    if len(ids) > TOPE_CORRIDA:
        raise SystemExit(
            f"Tope de {TOPE_CORRIDA} videos por corrida (pediste {len(ids)}).\n"
            "  Antes de bajar en bloque: mirar si ya estan en videos.csv, y ver\n"
            "  los candidatos en el navegador. Bajar a ciegas es lo que bloquea."
        )
    nuevos = 0
    for i, vid in enumerate(ids):
        estaba = ruta_cache(vid).exists()
        d = bajar(vid, traducir=args.traducir)
        s = senales(d)
        tr = " +es" if d.get("traducido") else ""
        print(f"  {vid}  {'cache ' if estaba else 'BAJADO'}  "
              f"{d['idioma']}{tr:4s} {s['duracion']/60:5.1f} min  "
              f"{s['palabras']:5d} palabras")
        if not estaba:
            nuevos += 1
            if i < len(ids) - 1:
                time.sleep(random.uniform(*PAUSA))
    gastadas, quedan = cuota_estado()
    print(f"\n  {nuevos} nuevos · cuota hoy {gastadas}/{CUOTA_DIA} "
          f"(quedan {quedan})\n  cache: {CACHE}")


def aprendizaje(sesion_id: str):
    for car in ("EOM", "PM", "SI"):
        p = BASE / car / "sesiones.csv"
        if not p.exists():
            continue
        with p.open(encoding="utf-8-sig", newline="") as fh:
            for fila in csv.DictReader(fh):
                if fila.get("sesion_id") == sesion_id:
                    return fila.get("aprendizaje_esperado"), car
    return None, None


def cmd_evaluar(args):
    vid = id_de(args.video)
    d = leer_cache(vid) or bajar(vid)
    s = senales(d)

    print("=" * 70)
    print(f"  {vid}    https://youtu.be/{vid}")
    print(f"  pistas: {[(p['idioma'], 'auto' if p['auto'] else 'MANUAL') for p in d['pistas']]}")
    print(f"  usada:  {d['idioma']}" +
          ("  (traducida al espanol)" if d.get("traducido") else ""))
    print()

    ok = s["duracion"] <= 15 * 60
    print(f"  duracion ....... {s['duracion']/60:6.1f} min   "
          f"{'OK' if ok else 'PASA DE 15 -> asignar solo un tramo'}")
    print(f"  ritmo .......... {s['pal_min']:6.0f} palabras/min")
    print(f"  silencios >2s .. {s['silencios']:6d}     "
          f"({s['pct_silencio']:.1f} % del video)")
    juicio = ("animacion producida" if s["deic_10min"] < 2
              else "PROBABLE CLASE CON DIAPOSITIVAS -> descartar")
    print(f"  deicticos ...... {s['deicticos']:6d}     "
          f"({s['deic_10min']:.1f} por 10 min)  {juicio}")

    texto = " ".join(x["txt"] for x in frags(d))
    _, arreglos = corregir(texto)
    print(f"  glosario ....... {len(arreglos):6d} correcciones"
          + (":" if arreglos else ""))
    for a in arreglos:
        print(f"                   {a}")

    if args.sesion:
        ae, car = aprendizaje(args.sesion)
        if ae:
            print(f"\n  APRENDIZAJE ESPERADO · {args.sesion} ({car})")
            print(f"    {ae}\n")
            claves = sorted(set(re.findall(r"\w{5,}", ae.lower())))
            bajo = texto.lower()
            hit = {w: bajo.count(w) for w in claves if bajo.count(w)}
            if hit:
                print(f"  vocabulario del aprendizaje presente en el video: {hit}")
            else:
                print("  NINGUNA palabra del aprendizaje esperado aparece en el")
                print("  video. Revisar bien antes de enlazarlo.")
        else:
            print(f"\n  (no encontre la sesion {args.sesion} en EOM/PM/SI)")

    print("\n  Esto MIDE, no aprueba. Falta verlo: los rotulos en pantalla que el")
    print("  subtitulo no recoge, la calidad de la animacion, piezas de mas o de")
    print("  menos. Quien firma `verificado_por` es el instructor lider.")


def cmd_anexo(args):
    """Borrador de la sintesis con marcas de tiempo.

    Sale un BORRADOR para reescribir, no un anexo terminado: la sintesis del
    cuadernillo es nuestra, no una copia del video.
    """
    vid = id_de(args.video)
    d = leer_cache(vid) or bajar(vid)
    ini, fin = 0.0, float(10 ** 9)
    if args.min:
        a, _, b = args.min.partition("-")
        ini, fin = a_segundos(a), a_segundos(b)

    f = [x for x in frags(d) if ini <= x["t"] < fin]
    if not f:
        raise SystemExit("Ese tramo no tiene texto. Revisa el rango.")

    print("### Anexo — qué muestra el video, minuto a minuto\n")
    print(f"<!-- {vid} · tramo {mmss(ini)}–{mmss(f[-1]['t'])} -->")
    print("<!-- BORRADOR. Reescribir con tus palabras y en español: esto es una")
    print("     síntesis nuestra, no una copia del video. Añadir los RÓTULOS que")
    print("     aparecen en pantalla y que el subtítulo no recoge. -->\n")

    paso, bloque, marca = 30, [], ini
    for x in f + [None]:
        if x is None or x["t"] >= marca + paso:
            if bloque:
                txt, _ = corregir(" ".join(bloque))
                print(f"- **{mmss(marca)}** · {txt.strip()}")
            if x is None:
                break
            marca += paso * max(1, int((x["t"] - marca) // paso))
            bloque = []
        bloque.append(x["txt"])


def cmd_pegar(args):
    """Salida de emergencia: el boton 'Mostrar transcripcion' de YouTube.

    Formato esperado, una linea por marca:    0:14  texto del fragmento
    No toca la red ni gasta cuota.
    """
    vid = id_de(args.video)
    crudo = Path(args.archivo).read_text(encoding="utf-8", errors="replace")
    frag = []
    for ln in crudo.splitlines():
        m = re.match(r"\s*(\d{1,2}:\d{2}(?::\d{2})?)\s+(.+)", ln)
        if m:
            frag.append({"t": float(a_segundos(m.group(1))), "d": 3.0,
                         "txt": m.group(2).strip()})
    if not frag:
        raise SystemExit("No reconoci ninguna marca de tiempo. Esperaba lineas "
                         "del tipo '0:14  texto del fragmento'.")
    guardar_cache(vid, {"video_id": vid, "pistas": [], "idioma": "pegado",
                        "auto": True, "fragmentos": frag, "traducido": None,
                        "bajado": dt.date.today().isoformat()})
    print(f"  {vid}: {len(frag)} fragmentos guardados en cache, sin tocar la red.")


def cmd_revisar(args):
    """Antes de cada ciclo: siguen vivos los enlaces?

    Un video que el canal borro deja el CV sin fuente. Por eso se revisa ANTES
    de que empiece el ciclo y no cuando un alumno reclama.
    """
    if not VIDEOS.exists():
        raise SystemExit(f"No existe {VIDEOS.name}: todavia no hay videos "
                         "registrados.")
    import urllib.request
    with VIDEOS.open(encoding="utf-8-sig", newline="") as fh:
        filas = list(csv.DictReader(fh))
    print(f"  {len(filas)} videos registrados\n")
    caidos = 0
    for fila in filas:
        vid = fila.get("video_yt_id", "")
        url = ("https://www.youtube.com/oembed?url=https://youtu.be/"
               f"{vid}&format=json")
        try:
            with urllib.request.urlopen(url, timeout=10):
                estado = "vivo"
        except Exception:
            estado = "CAIDO -> reemplazar"
            caidos += 1
        print(f"  {vid}  {estado:22s} {fila.get('titulo', '')[:44]}")
        time.sleep(random.uniform(*PAUSA))
    print(f"\n  {caidos} caidos de {len(filas)}")


def cmd_cuota(args):
    gastadas, quedan = cuota_estado()
    print(f"  hoy: {gastadas}/{CUOTA_DIA} consultas · quedan {quedan}")
    n = len(list(CACHE.glob("*.json"))) - (1 if CUOTA_ARCHIVO.exists() else 0)
    print(f"  en cache: {max(0, n)} transcripciones (esas no gastan nada)")


def main(argv=None) -> int:
    salida_utf8()
    p = argparse.ArgumentParser(
        description="Videos de YouTube para los recursos autonomos.")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("bajar", help="baja y cachea transcripciones")
    b.add_argument("videos", nargs="+")
    b.add_argument("--traducir", default="es",
                   help="idioma destino de la traduccion, o 'no'")
    b.set_defaults(f=cmd_bajar)

    e = sub.add_parser("evaluar", help="senales para decidir si el video sirve")
    e.add_argument("video")
    e.add_argument("--sesion", help="contrastar con el aprendizaje esperado")
    e.set_defaults(f=cmd_evaluar)

    a = sub.add_parser("anexo", help="borrador de sintesis con marcas de tiempo")
    a.add_argument("video")
    a.add_argument("--min", help="tramo, p.ej. 0:30-3:00")
    a.set_defaults(f=cmd_anexo)

    g = sub.add_parser("pegar", help="cargar transcripcion copiada de YouTube")
    g.add_argument("video")
    g.add_argument("archivo")
    g.set_defaults(f=cmd_pegar)

    r = sub.add_parser("revisar", help="comprobar que los enlaces siguen vivos")
    r.set_defaults(f=cmd_revisar)

    c = sub.add_parser("cuota", help="cuantas consultas quedan hoy")
    c.set_defaults(f=cmd_cuota)

    args = p.parse_args(argv)
    if getattr(args, "traducir", None) == "no":
        args.traducir = None
    args.f(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
