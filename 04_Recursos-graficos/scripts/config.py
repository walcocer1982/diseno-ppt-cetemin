# -*- coding: utf-8 -*-
"""Carga la configuracion desde el archivo .env

Uso desde cualquier script de la carpeta:

    from config import cliente, MODELO_IMAGEN
    r = cliente().images.edit(...)

La clave NUNCA se escribe en el codigo: vive solo en .env (que esta en .gitignore).
"""
import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ENV = RAIZ / ".env"


def cargar_env(ruta: Path = ENV) -> dict:
    """Lee el .env sin depender de librerias externas."""
    datos = {}
    if not ruta.exists():
        return datos
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        k, v = linea.split("=", 1)
        v = v.strip().strip('"').strip("'")
        if v:
            datos[k.strip()] = v
            os.environ.setdefault(k.strip(), v)
    return datos


_ENV = cargar_env()

API_KEY = os.environ.get("OPENAI_API_KEY", "")
MODELO_IMAGEN = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")


def revisar() -> tuple[bool, str]:
    """Comprueba que la clave este presente y con pinta valida."""
    if not API_KEY:
        return False, (f"Falta OPENAI_API_KEY.\n"
                       f"   Abre {ENV} y pega la clave despues del '='.")
    if not API_KEY.startswith("sk-"):
        return False, "La clave no empieza con 'sk-': revisa que este completa."
    if len(API_KEY) < 40:
        return False, "La clave parece incompleta (muy corta)."
    return True, f"OK  clave cargada (...{API_KEY[-6:]})  modelo={MODELO_IMAGEN}"


def cliente():
    """Devuelve el cliente de OpenAI ya autenticado."""
    ok, msg = revisar()
    if not ok:
        raise RuntimeError(msg)
    from openai import OpenAI
    kw = {"api_key": API_KEY}
    if os.environ.get("OPENAI_ORG_ID"):
        kw["organization"] = os.environ["OPENAI_ORG_ID"]
    if os.environ.get("OPENAI_PROJECT"):
        kw["project"] = os.environ["OPENAI_PROJECT"]
    return OpenAI(**kw)


if __name__ == "__main__":
    ok, msg = revisar()
    print(("[OK]   " if ok else "[FALTA] ") + msg)
    print(f"\n.env ubicado en: {ENV}")
    print(f"variables leidas: {list(_ENV.keys()) or '(ninguna)'}")
