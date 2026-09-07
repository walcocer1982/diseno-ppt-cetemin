# -*- coding: utf-8 -*-
"""Esquemas de la sesión 3 de SI-IMPAMB: condición, momento y requisito legal.

LO QUE MANDA EN EL CONTENIDO LEGAL
    Las láminas 14 a 19 no se redactan de memoria. Salen del marco legal verificado
    del curso, contrastado contra el texto publicado:

      art. 31.2 Ley 28611  el ECA es referente obligatorio en el diseño y aplicación
                           de todos los instrumentos de gestión ambiental
      art. 31.1            el ECA mide el cuerpo receptor: aire, agua, suelo
      art. 31.4            no se sanciona por ECA sin demostrar causalidad
      art. 32.1            el LMP caracteriza un efluente o una emisión, y su
                           cumplimiento es exigible legalmente al titular

EL EJEMPLO NEUTRO
    Las láminas de tema usan un caldero y una descarga genéricos, no la textilera ni
    la conservera de los casos. Misma regla que en la S1 y la S2: un esquema que use
    el caso lo resuelve antes de que el equipo lo lea.

Uso:  python gen_esquemas_impamb_s3.py
"""
from __future__ import annotations

import os
import sys

from PIL import Image, ImageDraw

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      fichas, cen, izq, AVISOS,
                      foto, credito, cadena, fichas_foto, hoja, hitos, narracion)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")
FOTOS = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "fotos")


def f(nombre):
    return os.path.join(FOTOS, nombre)


CR_ANTAMINA = ("Fotografía: Compañía Minera Antamina, «Reporte de Sostenibilidad 2024». "
               "Documento público, mostrado como ejemplo de clase.")
CR_UNICON = ("Fotografía: Unión de Concreteras S.A., «Reporte de Sostenibilidad» 2016 y "
             "2017. Documento público, mostrado como ejemplo de clase.")
CR_SIDER = ("Fotografía: Empresa Siderúrgica del Perú S.A.A. (Gerdau Siderperú), «Reporte de "
            "Sostenibilidad 2024». Documento público, mostrado como ejemplo de clase.")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ── PK1 · la condición y el momento cambian el registro ───────────────────
def en_que_condicion():
    """Las tres condiciones, con el mismo equipo en cada una."""
    im, d = lienzo(2500)
    y = foto(im, d, f("taller-llanta-equipo.png"), 50, 50, W - 100, 700,
             "EL MISMO EQUIPO, TRES CIRCUNSTANCIAS DISTINTAS")
    y = franjas(d, [
        ("NORMAL", ["La operación tal como está prevista", "El equipo funcionando"], TEAL),
        ("ANORMAL", ["Previsible, pero no rutina", "Arranque, parada, limpieza, mantenimiento"], AMBAR),
        ("EMERGENCIA", ["No previsto", "Derrame, incendio, rotura, rebose"], ROJO),
    ], im, y=y + 40, alto=360)
    banda(d, y + 20, 140, "La condición dice en qué circunstancia ocurre la actividad", px=CUE)
    credito(d, y + 190, CR_ANTAMINA)
    return guardar(im, "impamb_s3_en-que-condicion.png", DEST)


def no_rutina():
    """Lo que cambia entre las tres condiciones para un mismo equipo.

    Lleva foto porque la lámina habla de EMISIÓN, y una emisión tiene un sitio por
    donde sale. Que se vea la chimenea ahorra la mitad de la explicación."""
    im, d = lienzo(2100)
    y = foto(im, d, f("planta-chimenea.png"), 50, 50, W - 100, 640,
             "LA EMISIÓN SALE POR AQUÍ")
    y = comparativa(d, "EN MARCHA", "ARRANCANDO O AVERIADO", [
        (["Emisión dentro de lo previsto"], ["Emisión distinta y mayor"]),
        (["Consumo estable"], ["Consumo de arranque o pérdida"]),
        (["Se registra siempre"], ["Se registra aunque dure minutos"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "El aspecto de emergencia se registra aunque no haya ocurrido nunca",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    credito(d, y + 190, CR_SIDER)
    return guardar(im, "impamb_s3_no-rutina.png", DEST)


def antes_ahora_todavia_no():
    """Los tres momentos de la actividad."""
    im, d = lienzo(1900)
    y = franjas(d, [
        ("YA TERMINADA", ["La actividad ya no se hace", "El aspecto sigue en la matriz"], GRIS),
        ("PRESENTE", ["La actividad se hace hoy", "Es la mayor parte de la matriz"], AZUL2),
        ("PROYECTADA", ["Todavía no existe", "Entra al decidirla, no al construirla"], TEAL),
    ], im, y=60, alto=420)
    banda(d, y + 20, 140, "El momento no cambia el aspecto: cambia cuándo hay que responder por él",
          px=CUE)
    return guardar(im, "impamb_s3_antes-ahora.png", DEST)


# ── PK2 · cada aspecto lleva su requisito legal ───────────────────────────
def columna_legal():
    """De dónde sale legalmente la columna de requisitos."""
    im, d = lienzo(1700)
    y = franjas(d, [
        ("LA LEY DICE", ["El ECA es referente obligatorio en el diseño y aplicación",
                         "de todos los instrumentos de gestión ambiental"], AZUL2),
        ("Y LA MATRIZ", ["Es un instrumento de gestión ambiental",
                         "Por eso lleva la columna de requisitos"], TEAL),
    ], im, y=60, alto=380)
    banda(d, y + 20, 140, "Ley 28611, artículo 31.2", px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 180, 130, "No hace falta invocar la ISO para explicar por qué la columna está ahí",
          px=NOTA)
    return guardar(im, "impamb_s3_columna-legal.png", DEST)


def no_crea_el_aspecto():
    """Qué hace y qué no hace el requisito legal."""
    im, d = lienzo(1600)
    y = comparativa(d, "LO QUE EL REQUISITO HACE", "LO QUE NO HACE", [
        (["Vuelve exigible el aspecto"], ["Crear el aspecto"]),
        (["Se busca uno por aspecto"], ["Uno para toda la matriz"]),
        (["Puede haber nacional, sectorial y del cliente"], ["Bastar con el más general"]),
    ], y=50)
    banda(d, y + 20, 140, "El aspecto existe primero; el requisito solo dice quién responde por él",
          px=CUE)
    return guardar(im, "impamb_s3_no-crea.png", DEST)


def norma_que_no_toca():
    """Qué pasa cuando se cita mal, y cómo se escribe bien."""
    im, d = lienzo(1700)
    y = fichas(d, [
        "Sin requisito: el aspecto se gestiona igual",
        "Con la norma equivocada: parece cumplimiento",
        "Con el nombre genérico: no se puede comprobar",
        "Con su norma y su artículo: se puede verificar",
    ], y=50, alto=320, cols=2, pie="¿se puede comprobar?")
    banda(d, y + 20, 140, "Citar la norma equivocada es peor que no citar ninguna",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s3_norma-que-no-toca.png", DEST)


# ── PK3 · ECA y LMP ───────────────────────────────────────────────────────
def dos_numeros():
    """Qué mide cada uno y dónde."""
    im, d = lienzo(2100)
    y = foto(im, d, f("cuerpo-de-agua.png"), 50, 50, W - 100, 620,
             "EL CUERPO RECEPTOR: aquí se mide el ECA")
    y = comparativa(d, "ECA · art. 31", "LMP · art. 32", [
        (["Mide el cuerpo receptor"], ["Mide el efluente o la emisión"]),
        (["Aire, agua o suelo"], ["La chimenea, el tubo, la descarga"]),
        (["Lo que hay afuera"], ["Lo que sale de tu planta"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "Los dos son legales y los dos existen: miden cosas distintas", px=CUE)
    credito(d, y + 190, CR_UNICON)
    return guardar(im, "impamb_s3_dos-numeros.png", DEST)


def si_se_excede():
    """Qué significa exceder cada uno, y de quién es la obligación.

    La foto es la DESCARGA, y hace pareja con la de la lámina anterior, que es el
    cuerpo receptor. Las dos juntas son la distinción que estas dos láminas enseñan."""
    im, d = lienzo(2100)
    y = foto(im, d, f("poza-efluente.png"), 50, 50, W - 100, 640,
             "LA DESCARGA: aquí se mide el LMP")
    y = comparativa(d, "SI SE EXCEDE EL ECA", "SI SE EXCEDE EL LMP", [
        (["Hay riesgo significativo"], ["Causa o puede causar daño"]),
        (["No se sanciona sin causalidad"], ["Es exigible legalmente"]),
        (["Referente del diseño de instrumentos"], ["Obligación directa del titular"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "El LMP es tuyo porque la fuente es tuya", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    credito(d, y + 190, CR_SIDER)
    return guardar(im, "impamb_s3_si-se-excede.png", DEST)


def cual_es_el_tuyo():
    """Cuatro afirmaciones para decidir cuál corresponde."""
    im, d = lienzo(1700)
    y = fichas(d, [
        "«Nuestra descarga cumple el ECA de agua»",
        "«Nuestra descarga está por debajo del LMP»",
        "«El río donde descargamos cumple el ECA»",
        "«El río donde descargamos cumple nuestro LMP»",
    ], y=50, alto=320, cols=2, pie="¿está bien citada?")
    banda(d, y + 20, 140, "La pregunta no es si el número existe: es si es el tuyo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s3_cual-es-el-tuyo.png", DEST)


# ── las de apoyo ──────────────────────────────────────────────────────────
def donde_estamos():
    im, d = lienzo(1600)
    y = franjas(d, [
        ("BLOQUE 1", ["S1 · aspecto e impacto", "S2 · entradas y salidas",
                      "S3 · HOY: condición, momento y ley", "S4 y S5", "TC1"], AZUL2),
        ("BLOQUE 2", ["S7 a S11 · manejo de residuos", "TC2"], GRIS),
    ], im, y=60, alto=380)
    banda(d, y + 20, 140, "Tercera de cinco: seguimos identificando, todavía no evaluamos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s3_donde-estamos.png", DEST)


def repaso_s2():
    im, d = lienzo(1500)
    y = cadena(im, d, [
        ("LA ACTIVIDAD", GRIS, "Se descompone en las tareas que de verdad se hacen", None),
        ("CADA TAREA", AZUL2, "Tiene sus propias entradas y sus propias salidas", None),
        ("EL ASPECTO", TEAL, "Aparece al mirar una por una", None),
    ], y=60, alto=430)
    banda(d, y + 20, 140, "Hoy: el mismo aspecto, registrado distinto según cuándo y cómo ocurre",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s3_repaso.png", DEST)


def ruta_s3():
    im, d = lienzo(2400)
    y = franjas(d, [
        ("CONEXIÓN", ["Mirar una operación y preguntarse cuándo cambia lo que sale"], GRIS),
        ("ADQUISICIÓN", ["Condición, momento y el requisito legal que le aplica a cada aspecto"], AZUL2),
        ("APLICACIÓN", ["Cuatro pasos sobre una planta que está por ser revisada"], TEAL),
        ("DISCUSIÓN", ["Qué norma citó cada empresa, y por qué no era la suya"], MORADO),
        ("REFLEXIÓN", ["Antes pensaba… ahora pienso…"], GRIS),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "El mismo aspecto se escribe distinto según cuándo y bajo qué circunstancia",
          px=CUE)
    return guardar(im, "impamb_s3_ruta.png", DEST)


def mural_s3():
    ALTO_F, ALTO_B, SEP = 620, 360, 30
    im, d = lienzo(50 + ALTO_F + 40 + 3 * (ALTO_B + SEP) + 300)
    y = foto(im, d, f("via-afirmada-polvo.png"), 50, 50, W - 100, ALTO_F)
    y = franjas(d, [
        ("VEO", ["¿Qué está saliendo de esta operación ahora mismo?"], GRIS),
        ("PIENSO", ["¿Sería lo mismo con lluvia, o con un equipo averiado?"], AZUL2),
        ("PREGUNTO", ["¿Y quién dice cuánto es demasiado?"], TEAL),
    ], im, y=y + 40, alto=ALTO_B)
    credito(d, y + 20, CR_ANTAMINA)
    return guardar(im, "impamb_s3_mural.png", DEST)


def encargo_s3():
    im, d = lienzo(2400)
    y = hoja(d, ["EL ASPECTO", "¿EN QUÉ CONDICIÓN?", "¿DE QUÉ MOMENTO?",
                 "¿QUÉ REQUISITO LE APLICA?"],
             [["Emisión del caldero al arrancar", "Anormal", "Presente",
               "El LMP de su emisión"],
              ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
             y=60, alto_fila=175, muestra=1)
    banda(d, y + 24, 140, "Una fila por aspecto, también por los que solo ocurren en emergencia",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 184, 130, "Se describe lo que hay, no se propone lo que falta", px=NOTA)
    return guardar(im, "impamb_s3_encargo.png", DEST)


def caso_a_s3():
    AN = 2100
    im = Image.new("RGB", (AN, 1400), BLANCO)
    d = ImageDraw.Draw(im)
    narracion(d, "CASO A",
        "Textiles y Acabados del Norte S.A.C.  ·  planta de teñido y acabado  ·  4 500 kg de tela al día",
        ["El lunes 14 llega la fiscalización ambiental, y el cliente de exportación pidió "
         "la matriz de aspectos actualizada para ese mismo día.",
         "Milagros Chávez lleva ocho meses como jefa de gestión ambiental. La planta tiñe "
         "en continuo y el agua de los baños sale por una descarga a la red. El caldero se "
         "enciende a las seis y los primeros veinte minutos bota un humo negro que después "
         "se aclara. Al terminar cada partida se lava el equipo con soda, y esa agua sale "
         "más cargada que la del teñido.",
         "Hace dos años se rompió una manguera del baño de teñido y el líquido llegó hasta "
         "la acequia del costado. Se limpió con la cisterna y no se declaró. En la franja "
         "donde se derramó, la tierra sigue con color.",
         "El mes que viene instalan un tanque de igualación para nivelar la descarga. En el "
         "informe que Milagros manda al cliente dice que el agua descargada cumple el ECA "
         "de agua."], color=AZUL2, y=50, ancho_total=AN)
    return guardar(im, "impamb_s3_caso-a.png", DEST)


def caso_b_s3():
    AN = 2100
    im = Image.new("RGB", (AN, 1400), BLANCO)
    d = ImageDraw.Draw(im)
    narracion(d, "CASO B",
        "Conservas y Congelados del Litoral S.A.C.  ·  planta de conservas  ·  18 t de materia prima al día",
        ["El viernes 26 la certificadora del cliente revisa la matriz de aspectos.",
         "Iván Rojas lleva siete meses como supervisor de medio ambiente. La planta cuece y "
         "esteriliza en continuo; el caldero da vapor todo el turno y el efluente de proceso "
         "sale por una descarga al emisor. Al cerrar el turno se lava el circuito con soda "
         "caliente, y ese lavado sale concentrado, distinto del efluente del resto del día.",
         "El invierno pasado la poza de sanguaza rebosó con la lluvia y el agua llegó al "
         "canal de la vía. Se bombeó de vuelta y no se registró en ninguna parte.",
         "Para el próximo año está proyectada una línea de congelado en el terreno de atrás. "
         "Cuando el municipio preguntó por el estado del canal, Iván respondió con el reporte "
         "de monitoreo de su descarga: los valores están por debajo del LMP."],
        color=TEAL, y=50, ancho_total=AN)
    return guardar(im, "impamb_s3_caso-b.png", DEST)


def a_trabajar_s3():
    im, d = lienzo(1400)
    y = hitos(d, [("4", "integrantes por equipo"),
                  ("28", "minutos de trabajo"),
                  ("2", "minutos de sustentación")], y=60, alto=320)
    y = franjas(d, [
        ("EL REPARTO", ["La mitad de los equipos trabaja el caso A, la otra mitad el B",
                        "Cada integrante responde por su fila ante el equipo"], AZUL2),
    ], im, y=y + 30, alto=360)
    banda(d, y + 26, 140, "Solo el relato: sin plantilla, sin anexos y sin norma a la vista",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s3_a-trabajar.png", DEST)


def discusion_s3():
    im, d = lienzo(1900)
    y = franjas(d, [
        ("AFIRMACIÓN", ["A esta descarga le aplica este requisito legal"], AZUL2),
        ("APOYO", ["Y esto es lo que la norma mide, y dónde"], TEAL),
        ("PREGUNTA", ["¿La norma que citó la empresa es la suya?"], MORADO),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Los dos casos se equivocan en direcciones contrarias",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s3_discusion.png", DEST)


def reflexion_s3():
    im, d = lienzo(1900)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que citar una norma en la matriz era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué aspecto de tu trabajo ocurre solo en emergencia?"], TEAL),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "impamb_s3_reflexion.png", DEST)


FIGURAS = [en_que_condicion, no_rutina, antes_ahora_todavia_no,
           columna_legal, no_crea_el_aspecto, norma_que_no_toca,
           dos_numeros, si_se_excede, cual_es_el_tuyo,
           donde_estamos, repaso_s2, ruta_s3, mural_s3, encargo_s3,
           caso_a_s3, caso_b_s3, a_trabajar_s3, discusion_s3, reflexion_s3]

if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    print("Esquemas de SI-IMPAMB · S3")
    for fn in FIGURAS:
        fn()
    if AVISOS:
        print("\nAVISOS:")
        for a in AVISOS:
            print("   !! %s" % a)
    else:
        print("\nSin avisos: todo el texto cupo en su caja.")
