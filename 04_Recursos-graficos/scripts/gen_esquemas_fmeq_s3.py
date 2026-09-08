# -*- coding: utf-8 -*-
"""Esquemas de la sesión 3 de EOM · Fundamentos mecánicos de equipos mineros.

Partes críticas del scooptram y del minetruck. Es la primera sesión del molde
«…reconociéndolos en el formato de pre-uso», y su caso va un paso más allá: en
vez de llenar el formato, el estudiante VERIFICA EL FORMATO MISMO.

LAS DOS MÁQUINAS NO SE DIBUJAN AQUÍ. Sus componentes salen del manual del
fabricante por extracción —`extraer_fmeq_figuras.py`—, que es lo que manda la
regla 3. Aquí están las trece láminas que sí se dibujan: comparativas, listas
y el armazón de la sesión.

Uso:  python gen_esquemas_fmeq_s3.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_esquemas_fmeq_comun import (  # noqa: E402
    AZUL, MARINO, MORADO, ROJO, ROJO_CLARO, VERDE, _salida, antes_de_resolver,
    dos_columnas, ficha_caso, lista_numerada, puente, puesta_comun,
)

G = _salida("fmeq/s3/")


# ═══════════════════════════════════ 1 · de dónde venimos
def de_donde():
    dos_columnas(
        G, "fmeq-s3_de-donde.png", "LAS DOS SESIONES ANTERIORES", "ESTA SESIÓN",
        [("los sistemas: potencia\ny circuito hidráulico", "los equipos que los llevan\nadentro"),
         ("valían para cualquier equipo", "el scooptram y el minetruck,\nuno por uno"),
         ("qué hace cada sistema", "qué componente falla\ny qué se revisa")],
        pie="De los sistemas a las máquinas que los montan", asp=1.40)


# ═══════════════════════════════════ 2 · qué hace cada componente
def funcion_componentes():
    lista_numerada(
        G, "fmeq-s3_funcion-componentes.png",
        ["El cilindro de levante sostiene la carga mientras está arriba",
         "El cilindro de volteo controla el ángulo con que se descarga",
         "La articulación central transmite el giro entre las dos mitades",
         "Cada componente crítico tiene una función y un modo de fallar"],
        pie="Saber qué hace es lo que dice qué mirar cuando falla", asp=1.15)


# ═══════════════════════════════════ 3 · los dos frenos
def frenos():
    dos_columnas(
        G, "fmeq-s3_frenos.png", "FRENO DE PARQUEO", "FRENO DE SERVICIO",
        [("sujeta el equipo detenido", "detiene el equipo en movimiento"),
         ("trabaja sin presión:\nlo aplica un resorte", "trabaja con presión:\nla presión lo suelta"),
         ("si falla, el equipo\nse mueve solo", "si falla, el equipo\nno se detiene")],
        pie="Crítico es el componente que detiene la actividad si falla",
        asp=1.25, color_izq=MORADO, color_der=AZUL)


# ═══════════════════════════════════ 4 · carguío y acarreo
def carguio_acarreo():
    dos_columnas(
        G, "fmeq-s3_carguio-acarreo.png", "EQUIPO DE CARGUÍO", "EQUIPO DE ACARREO",
        [("levanta y voltea la carga", "la traslada, no la levanta del piso"),
         ("cuchara con sus cilindros\nde volteo", "tolva con su cilindro\nde levante"),
         ("el scooptram del caso", "el minetruck del caso")],
        rotulos=["QUÉ HACE", "CON QUÉ", "QUIÉN ES"],
        pie="Lo que no comparten es lo que hacen con la carga", asp=1.20)


# ═══════════════════════════════════ 5 · lo que comparten
def comparten():
    dos_columnas(
        G, "fmeq-s3_comparten.png", "LO QUE COMPARTEN", "LO QUE NO",
        [("tren de potencia", "la cuchara y sus cilindros de volteo"),
         ("frenos y neumáticos", "la tolva y su cilindro de levante"),
         ("articulación central", "lo que hacen con la carga")],
        pie="Confundir uno con otro cambia qué hay que revisar", asp=1.30)


# ═══════════════════════════════════ 6 · el hueco tiene dos direcciones
def componente_linea():
    dos_columnas(
        G, "fmeq-s3_componente-linea.png", "UN COMPONENTE SIN LÍNEA",
        "UNA LÍNEA SIN COMPONENTE",
        [("no se revisa nunca", "se marca sin mirar nada"),
         ("el operador lo anota al margen,\nsi se acuerda", "queda «conforme» algo\nque el equipo no tiene"),
         ("el hueco se ve en la máquina", "el hueco se ve en el papel")],
        pie="Cada componente crítico debe tener su línea, y cada línea su componente",
        asp=1.20, color_izq=ROJO, color_der=ROJO, fondo_der=ROJO_CLARO)


# ═══════════════════════════════════ 7 · el formato se hace por equipo
def formato_por_equipo():
    lista_numerada(
        G, "fmeq-s3_formato-por-equipo.png",
        ["El formato se hace por equipo, no por flota entera",
         "Un formato genérico deja huecos en los dos sentidos",
         "Lo que el operador anota al margen debería tener casilla"],
        cierre="Un formato que sirve para catorce equipos no sirve para ninguno",
        pie="El margen del papel es la lista de lo que le falta al formato",
        asp=1.30)


# ═══════════════════════════════════ 8 a 13 · el armazón
def caso():
    ficha_caso(
        G, "fmeq-s3_caso-ficha.png",
        "Operación y Mantenimiento de Equipo Pesado S.A.C.",
        "Catorce equipos en la unidad · un solo formato de pre-uso para todos",
        [("EL DEL MINETRUCK", "completo, firmado, todas las líneas conforme,\n"
                              "y entre ellas «cilindros de volteo de cuchara»"),
         ("EL DEL SCOOPTRAM", "completo, y al margen, escrito a mano:\n"
                              "«el freno de parqueo tarda en soltar»"),
         ("EL FORMATO", "lo armó el prevencionista el año pasado\npara toda la flota"),
         ("A LAS ONCE", "el jefe de seguridad los quiere\ncon el formato corregido")],
        pie_nota="Hace dos años, en otra unidad, un scooptram se movió solo en la rampa.")


def antes():
    antes_de_resolver(
        G, "fmeq-s3_antes-de-resolver.png",
        "Si todas las líneas están marcadas conforme,\n¿el equipo está conforme?",
        [("CATORCE", "equipos con el mismo\nformato impreso"),
         ("UNA LÍNEA", "marcada conforme sobre\nalgo que no existe"),
         ("UN MARGEN", "escrito a mano donde\nno había casilla")])


def encargo():
    lista_numerada(
        G, "fmeq-s3_encargo.png",
        ["Los componentes críticos del scooptram y los del minetruck, en dos columnas",
         "Al costado de cada uno, qué hace",
         "Qué líneas del formato no corresponden al equipo que las tiene, y por qué",
         "Qué componente crítico se queda sin línea, y qué pasa si nadie lo revisa"],
        pie="Una hoja en blanco por equipo · 40 minutos", asp=1.05)


def como_trabajamos():
    lista_numerada(
        G, "fmeq-s3_como-trabajamos.png",
        ["Armen la lista de componentes antes de abrir el formato",
         "Recién entonces comparen: componente por componente, línea por línea",
         "Marquen lo que sobra y lo que falta, en dos colores distintos",
         "Escriban qué pasa si el que falta no se revisa nunca"],
        pie="Equipos de 3 · 40 minutos · expone uno por equipo", asp=1.35)


def puesta():
    puesta_comun(
        G, "fmeq-s3_puesta-comun.png",
        [("AFIRMACIÓN", AZUL, "qué le sobra y qué\nle falta al formato"),
         ("APOYO", VERDE, "qué componente\nlo demuestra"),
         ("PREGUNTA", MORADO, "lo que todavía\nfalta saber")],
        "Empezamos por el componente que se quedó sin línea")


def puente_s4():
    puente(
        G, "fmeq-s3_puente-s4.png",
        "LA PRÓXIMA SESIÓN", "Jumbo, simba y empernador:\ntres máquinas parecidas\nque no se revisan igual",
        "AL CIERRE DEL BLOQUE", "TC1: cinco equipos\nen una labor, y un formato\ncon más ítems de los necesarios",
        "Hoy corregiste un formato para dos equipos.\n"
        "En el TC1 vas a usar uno que ya viene con líneas de más.",
        pie="Antes de la próxima clase: el recurso autónomo del EVA.")


if __name__ == "__main__":
    print("Esquemas de EOM-FMEQ-S3 · Partes críticas del scooptram y el minetruck\n")
    for f in (de_donde, funcion_componentes, frenos, carguio_acarreo, comparten,
              componente_linea, formato_por_equipo, caso, antes, encargo,
              como_trabajamos, puesta, puente_s4):
        f()
    print("\n13 esquemas en 04_Recursos-graficos/EOM/esquemas/fmeq/s3/")
    print("Las dos figuras de equipo salen de extraer_fmeq_figuras.py")
