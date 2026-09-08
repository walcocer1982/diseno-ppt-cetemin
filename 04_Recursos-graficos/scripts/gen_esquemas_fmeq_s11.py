# -*- coding: utf-8 -*-
"""Esquemas de la sesión 11 de EOM · Fundamentos mecánicos de equipos mineros.

Mantenimiento preventivo. Es la sesión que cierra la segunda mitad del
indicador 2 —verificar que el preventivo y el programado estén realizados y
registrados— y la que cierra el arco que abrió la S2: allí el cilindro que no
sostiene se descubre por física; aquí, por papeles.

Todo lo que va aquí son documentos, plazos y cuentas: nada con cuerpo.

Uso:  python gen_esquemas_fmeq_s11.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_esquemas_fmeq_comun import (  # noqa: E402
    AMBAR, AZUL, MARINO, MORADO, ROJO, VERDE, _salida, antes_de_resolver,
    dos_columnas, ficha_caso, lista_numerada, puente, puesta_comun, tres_fichas,
)

G = _salida("fmeq/s11/")


# ═══════════════════════════════════ 1 · de dónde venimos
def de_donde():
    dos_columnas(
        G, "fmeq-s11_de-donde.png", "LA SESIÓN PASADA", "ESTA SESIÓN",
        [("miramos, probamos y medimos\nel equipo", "leemos lo que dicen\nsus papeles"),
         ("el margen que le queda\na un freno", "el mantenimiento que\nle toca y el que le debe"),
         ("la máquina estaba delante", "la máquina puede estar\ntrabajando ahora mismo")],
        pie="Hay hallazgos que no se ven mirando la máquina", asp=1.40)


# ═══════════════════════════════════ 2 · preventivo y programado
def preventivo_programado():
    dos_columnas(
        G, "fmeq-s11_preventivo-programado.png", "PREVENTIVO", "PROGRAMADO",
        [("lo manda el fabricante", "lo planifica la unidad"),
         ("por horas de horómetro\no por frecuencia", "para un periodo:\nesta semana, este mes"),
         ("se identifica con la sigla PM\ny su número de horas",
          "incluye el preventivo que toca\ny el correctivo ya planificado")],
        rotulos=["QUIÉN LO MANDA", "CON QUÉ REGLA", "CÓMO SE RECONOCE"],
        pie="Uno viene del manual; el otro, del programa de la unidad", asp=1.15)


# ═══════════════════════════════════ 3 · se cumplen por separado
def por_separado():
    lista_numerada(
        G, "fmeq-s11_por-separado.png",
        ["Los dos se cumplen o no se cumplen por separado",
         "Estar al día en uno no dice nada del otro",
         "Un equipo con el PM firmado puede deber un correctivo"],
        cierre="Preguntar por uno solo deja media verificación",
        pie="Se piden los dos, siempre, y se leen uno contra el otro", asp=1.30)


# ═══════════════════════════════════ 4 · qué prueba cada documento
def dos_documentos():
    dos_columnas(
        G, "fmeq-s11_dos-documentos.png", "LA CARTILLA DEL EQUIPO",
        "EL PROGRAMA DE LA UNIDAD",
        [("prueba el preventivo,\ncon su fecha", "prueba lo planificado\ndel periodo"),
         ("lleva la firma de quien lo hizo\ny el horómetro",
          "muestra la fecha prevista\ny si el trabajo se ejecutó"),
         ("dice qué se hizo", "dice qué se debía hacer")],
        pie="Cada documento prueba una cosa, y solo esa", asp=1.20)


# ═══════════════════════════════════ 5 · media verificación
def media_verificacion():
    lista_numerada(
        G, "fmeq-s11_media-verificacion.png",
        ["Un trabajo que reaparece semana a semana no se ejecutó",
         "Pedir un documento y no el otro deja media verificación",
         "Lo que no está en ninguno de los dos, no está"],
        pie="El hallazgo aparece al comparar, no al leer uno solo", asp=1.40)


# ═══════════════════════════════════ 6 · la cuenta del horómetro
def horometro():
    tres_fichas(
        G, "fmeq-s11_horometro.png", "La cuenta que decide si está vencido",
        [("LA CARTILLA", AZUL, "cada cuántas horas\ntoca el servicio", "el intervalo"),
         ("EL HORÓMETRO", VERDE, "cuántas horas lleva\nel equipo ahora", "la lectura de hoy"),
         ("LA DIFERENCIA", AMBAR, "lo que falta\no lo que ya pasó", "el margen")],
        pie="Pasado el intervalo, el servicio está vencido, no pendiente", asp=1.15)


# ═══════════════════════════════════ 7 · lo que no se ve mirando
def no_se_ve():
    lista_numerada(
        G, "fmeq-s11_no-se-ve.png",
        ["Un preventivo vencido no se ve mirando la máquina",
         "La fecha sola no basta: manda el horómetro",
         "Anotar el horómetro en cada pre-uso hace visible el vencimiento"],
        pie="Lo que no se anota, no se vence: se descubre tarde", asp=1.40)


# ═══════════════════════════════════ 8 · el trabajo que se reprograma
def reprogramado():
    lista_numerada(
        G, "fmeq-s11_reprogramado.png",
        ["Un trabajo que se reprograma tres veces ya es un hallazgo",
         "Se reporta el trabajo, su fecha original y cuántas veces se movió",
         "Lo que el operador viene anotando sostiene el reporte",
         "Una anotación repetida en el cuaderno vale como evidencia"],
        pie="Tres semanas seguidas no es demora: es un trabajo sin dueño",
        asp=1.15)


# ═══════════════════════════════════ 9 · hasta dónde llega el técnico
def hasta_donde():
    dos_columnas(
        G, "fmeq-s11_hasta-donde.png", "LE TOCA AL TÉCNICO", "NO LE TOCA AL TÉCNICO",
        [("que el trabajo deje\nde ser invisible", "decidir la prioridad\ndel trabajo"),
         ("reportar a mantenimiento\ny al turno entrante", "reprogramarlo\npor su cuenta"),
         ("dejar escrito lo que vio", "decidir si el equipo\nse repara hoy")],
        pie="El técnico hace visible; la decisión es de mantenimiento",
        asp=1.30, color_der=MORADO)


# ═══════════════════════════════════ 10 a 15 · el armazón
def caso():
    ficha_caso(
        G, "fmeq-s11_caso-ficha.png",
        "Servicios Integrales de Mantenimiento Minero S.A.C.",
        "Camión 12 · flota de camiones de la unidad",
        [("LA CARTILLA", "firmada y al día: el PM-500 se le hizo\nhace cuarenta horas de horómetro"),
         ("EL PROGRAMA", "trae un trabajo que no es preventivo:\ncambio del cilindro de levante de tolva"),
         ("HACIA ATRÁS", "el mismo trabajo aparece en las tres\nsemanas anteriores, reprogramado"),
         ("EL OPERADOR", "viene anotando hace un mes que la tolva\nbaja sola cuando la deja levantada")],
        pie_nota="El supervisor dice que el equipo está al día.")


def antes():
    antes_de_resolver(
        G, "fmeq-s11_antes-de-resolver.png",
        "Si el preventivo está al día, ¿el equipo está al día?",
        [("40 HORAS", "es lo que lleva el camión\ndesde el último PM"),
         ("TRES VECES", "se reprogramó el mismo\ntrabajo, semana a semana"),
         ("UN MES", "lleva el operador anotando\nque la tolva baja sola")])


def encargo():
    lista_numerada(
        G, "fmeq-s11_encargo.png",
        ["Qué es preventivo y qué es programado, y en qué se diferencian",
         "En qué documento se comprueba cada uno",
         "Qué dice cada documento sobre el camión 12",
         "Si el camión está al día o no, y qué se reporta"],
        pie="Una hoja en blanco por equipo · 40 minutos", asp=1.15)


def como_trabajamos():
    lista_numerada(
        G, "fmeq-s11_como-trabajamos.png",
        ["Separen los dos mantenimientos antes de mirar los papeles",
         "Digan qué prueba cada documento, y qué no puede probar",
         "Comparen el programa de las cuatro semanas, no el de esta",
         "Escriban la conclusión con el dato que la sostiene"],
        pie="Equipos de 3 · 40 minutos · expone uno por equipo", asp=1.35)


def puesta():
    puesta_comun(
        G, "fmeq-s11_puesta-comun.png",
        [("AFIRMACIÓN", AZUL, "está al día\no no lo está"),
         ("APOYO", VERDE, "qué documento\nlo demuestra"),
         ("PREGUNTA", MORADO, "lo que todavía\nfalta saber")],
        "Empezamos por los equipos que respondieron distinto")


def puente_tc2():
    puente(
        G, "fmeq-s11_puente-tc2.png",
        "LA PRÓXIMA SESIÓN", "El trabajo colaborativo:\ncuatro equipos de un tajo\ny una decisión por cada uno",
        "CIERRA EL BLOQUE 2", "TC2: un equipo que arranca\nbien y no debería\nestar trabajando",
        "Hoy encontraste un hallazgo sin tocar la máquina.\n"
        "En el TC2 vas a hacerlo con cuatro equipos y sus registros.",
        pie="Antes de la próxima clase: el recurso autónomo del EVA.")


if __name__ == "__main__":
    print("Esquemas de EOM-FMEQ-S11 · Mantenimiento preventivo\n")
    for f in (de_donde, preventivo_programado, por_separado, dos_documentos,
              media_verificacion, horometro, no_se_ve, reprogramado, hasta_donde,
              caso, antes, encargo, como_trabajamos, puesta, puente_tc2):
        f()
    print("\n15 esquemas en 04_Recursos-graficos/EOM/esquemas/fmeq/s11/")
