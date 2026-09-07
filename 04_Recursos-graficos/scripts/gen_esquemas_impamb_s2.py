# -*- coding: utf-8 -*-
"""Esquemas de la sesión 2 de SI-IMPAMB: entradas, salidas y nivel de detalle.

QUÉ DIBUJA
    Las nueve láminas de tema y las nueve de apoyo. Mismo molde que la S1: todo dentro
    de cuadros, banda de cierre con la idea que hay que llevarse, y el caso EN PROSA.

LA FORMA SIGUE A LO QUE ENSEÑA, no al revés. Por eso no se repite `comparativa` nueve
veces: se usa cuando de verdad hay dos cosas que contrastar, `franjas` cuando hay
niveles apilados, `fichas` cuando el alumno tiene que clasificar, y `narracion` cuando
lo que hay es una historia.

EL EJEMPLO NEUTRO
    Las tres primeras láminas usan el cambio de aceite de un motor, y la S1 usó el
    lavado de un equipo: ninguno de los dos es el comedor ni la lavandería de los casos.
    Es a propósito — un esquema que use el caso lo resuelve antes de que el equipo lo
    lea— y es la misma regla que rige en la S1.

Uso:  python gen_esquemas_impamb_s2.py
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

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ── PK1 · el aspecto está en lo que entra y lo que sale ───────────────────
def entra_sale_s2():
    """El balance de una actividad. Ejemplo neutro: cambiar el aceite de un motor."""
    im, d = lienzo(2000)
    y = foto(im, d, f("taller-llanta-equipo.png"), 50, 50, W - 100, 720,
             "LA ACTIVIDAD: cambiar el aceite de un motor")
    y = comparativa(d, "LO QUE ENTRA", "LO QUE SALE", [
        (["Aceite nuevo"], ["Motor operativo"]),
        (["Filtro y trapos"], ["Aceite usado y filtro"]),
        (["Energía y agua"], ["Trapos con grasa"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "Lo que entra y no sale como producto, sale de alguna otra forma",
          px=CUE)
    credito(d, y + 190, CR_ANTAMINA)
    return guardar(im, "impamb_s2_entra-sale.png", DEST)


def familias():
    """Las cuatro familias de cada lado: para no dejarse ninguna."""
    im, d = lienzo(1700)
    y = franjas(d, [
        ("ENTRA", ["Agua", "Energía", "Insumos y materiales"], AZUL2),
        ("SALE", ["Producto", "Residuo y efluente", "Emisión y ruido"], TEAL),
    ], im, y=60, alto=380)
    banda(d, y + 20, 140, "El producto también es una salida, aunque no sea un aspecto",
          px=CUE)
    banda(d, y + 180, 130, "Lo que la actividad consume es aspecto igual que lo que genera",
          px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_familias.png", DEST)


def donde_mirar():
    """Las cuatro preguntas que se hacen sobre la actividad, una por estado."""
    im, d = lienzo(1700)
    y = fichas(d, [
        "¿Qué sale sólido y quién se lo lleva?",
        "¿Qué sale líquido y por dónde se va?",
        "¿Qué sale al aire y cuándo se nota?",
        "¿Qué se consume aunque no se vea salir?",
    ], y=50, alto=320, cols=2, pie="preguntar por cada estado")
    banda(d, y + 20, 140, "Si algo entra y no se sabe por dónde sale, ahí es donde falta mirar",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_donde-mirar.png", DEST)


# ── PK2 · una actividad son varias tareas por dentro ──────────────────────
def una_linea():
    """Lo que dice la matriz frente a lo que pasa de verdad."""
    im, d = lienzo(2000)
    y = foto(im, d, f("planta-concreto.png"), 50, 50, W - 100, 620,
             "UNA SOLA LÍNEA EN LA MATRIZ: «operación de planta»")
    y = franjas(d, [
        ("LA MATRIZ DICE", ["Una actividad", "Una entrada", "Una salida"], GRIS),
        ("Y POR DENTRO SON", ["Recibir y acopiar", "Dosificar y mezclar",
                              "Cargar y transportar", "Lavar y limpiar"], AZUL2),
    ], im, y=y + 40, alto=380)
    banda(d, y + 20, 140, "Una actividad casi nunca es un solo acto", px=CUE)
    credito(d, y + 190, CR_UNICON)
    return guardar(im, "impamb_s2_una-linea.png", DEST)


def como_se_parte():
    """El criterio de partición: se sigue el proceso."""
    im, d = lienzo(1700)
    y = comparativa(d, "SE PARTE ASÍ", "ASÍ NO", [
        (["Siguiendo el proceso, de principio a fin"], ["Siguiendo el organigrama"]),
        (["Cada tarea con su entrada y su salida"], ["Cada área con su jefe"]),
        (["En el orden en que se hacen"], ["En el orden en que se pagan"]),
    ], y=50)
    banda(d, y + 20, 140, "Se parte por el proceso, no por el turno ni por el área", px=CUE)
    return guardar(im, "impamb_s2_como-se-parte.png", DEST)


def tareas_olvidadas():
    """Las tres tareas que casi nunca llegan a la matriz."""
    im, d = lienzo(1700)
    y = fichas(d, [
        "La limpieza al terminar el turno",
        "El mantenimiento de cada quince días",
        "Lo que se hace cuando algo se avería",
        "Lo que solo pasa en emergencia",
    ], y=50, alto=320, cols=2, pie="¿está en la matriz?")
    banda(d, y + 20, 140, "Una tarea que ocurre cada quince días entra igual que la diaria",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_tareas-olvidadas.png", DEST)


# ── PK3 · el nivel de detalle decide qué aspectos se ven ──────────────────
def al_partirla():
    """La misma operación con una fila y con cinco."""
    im, d = lienzo(1700)
    y = comparativa(d, "CON UNA FILA", "CON CINCO FILAS", [
        (["Se ve un aspecto"], ["Se ven seis o siete"]),
        (["El resto queda sin registrar"], ["Cada tarea con el suyo"]),
        (["Nadie responde por lo que no está"], ["Cada aspecto con su control"]),
    ], y=50)
    banda(d, y + 20, 140, "Lo que no está en la matriz no tiene control ni responsable",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_al-partirla.png", DEST)


def ni_gruesa_ni_fina():
    """Los tres niveles de partición y lo que cuesta cada uno."""
    im, d = lienzo(1900)
    y = franjas(d, [
        ("DEMASIADO GRUESA", ["Una fila para toda la operación", "Esconde casi todo"], ROJO),
        ("EL NIVEL JUSTO", ["Cada tarea con un aspecto propio", "Se puede mantener"], TEAL),
        ("DEMASIADO FINA", ["Una fila por cada movimiento", "Nadie la revisa"], GRIS),
    ], im, y=60, alto=380)
    banda(d, y + 20, 140, "El nivel se decide antes de llenar la matriz, no después", px=CUE)
    return guardar(im, "impamb_s2_ni-gruesa-ni-fina.png", DEST)


def llena_e_incompleta():
    """Una matriz correcta por fuera a la que le falta por dentro."""
    im, d = lienzo(1700)
    y = comparativa(d, "LO QUE SE VE", "LO QUE FALTA", [
        (["Llena, sin casillas en blanco"], ["Las tareas que nadie escribió"]),
        (["Ordenada y con formato"], ["Los aspectos de esas tareas"]),
        (["Firmada y con fecha"], ["El control que les tocaría"]),
    ], y=50)
    banda(d, y + 20, 140, "Una matriz llena, ordenada y firmada puede estar incompleta",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_llena-e-incompleta.png", DEST)


# ── las de apoyo ──────────────────────────────────────────────────────────
def repaso_s1():
    """Lo de la sesión anterior, en una línea."""
    im, d = lienzo(1400)
    y = cadena(im, d, [
        ("LA ACTIVIDAD", GRIS, "Lo que se hace", None),
        ("EL ASPECTO", AZUL2, "Lo que interactúa con el ambiente", None),
        ("EL IMPACTO", TEAL, "El cambio que ese aspecto causa", None),
    ], y=60, alto=560)
    banda(d, y + 20, 140, "Hoy vamos a lo de en medio: cómo se encuentran los aspectos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_repaso.png", DEST)


def ruta_s2():
    """Los cinco momentos de la sesión."""
    im, d = lienzo(2200)
    y = franjas(d, [
        ("CONEXIÓN", ["Mirar una operación y contar cuántas cosas pasan dentro"], GRIS),
        ("ADQUISICIÓN", ["Entradas, salidas y en cuántas tareas se parte una actividad"], AZUL2),
        ("APLICACIÓN", ["Cuatro pasos sobre una matriz de una sola fila"], TEAL),
        ("DISCUSIÓN", ["Qué apareció al partir la actividad de cada caso"], MORADO),
        ("REFLEXIÓN", ["Antes pensaba… ahora pienso…"], GRIS),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "De una línea escrita a las tareas que de verdad se hacen", px=CUE)
    return guardar(im, "impamb_s2_ruta.png", DEST)


def mural_s2():
    """«Veo · Pienso · Me pregunto», sin rótulos sobre la foto."""
    ALTO_F, ALTO_B, SEP = 620, 360, 30
    im, d = lienzo(50 + ALTO_F + 40 + 3 * (ALTO_B + SEP) + 300)
    y = foto(im, d, f("almacen-montacargas.png"), 50, 50, W - 100, ALTO_F)
    y = franjas(d, [
        ("VEO", ["¿Cuántas cosas distintas están pasando aquí?"], GRIS),
        ("PIENSO", ["Si esto fuera una sola fila, ¿qué diría?"], AZUL2),
        ("PREGUNTO", ["¿Qué se quedaría fuera de esa fila?"], TEAL),
    ], im, y=y + 40, alto=ALTO_B)
    credito(d, y + 20, CR_ANTAMINA)
    return guardar(im, "impamb_s2_mural.png", DEST)


def encargo_s2():
    """La hoja que el equipo entrega, vacía y con sus encabezados."""
    im, d = lienzo(2200)
    y = hoja(d, ["LA ACTIVIDAD COMO ESTÁ ESCRITA", "LAS TAREAS QUE LA COMPONEN",
                 "QUÉ ENTRA Y SALE DE CADA TAREA", "QUÉ ASPECTO APARECE"],
             [["Mantenimiento de equipos", "Cambiar el aceite",
               "Entra aceite y filtro · sale aceite usado", "Generación de residuo peligroso"],
              ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
             y=60, alto_fila=175, muestra=1)
    banda(d, y + 24, 140, "Una fila por cada tarea que aparezca al partir la actividad",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 184, 130, "Se describe lo que hay, no se propone lo que falta", px=NOTA)
    return guardar(im, "impamb_s2_encargo.png", DEST)


def caso_a_s2():
    """El caso A en prosa, tal como está en el diseño de sesión."""
    AN = 2100
    im = Image.new("RGB", (AN, 1400), BLANCO)
    d = ImageDraw.Draw(im)
    narracion(d, "CASO A",
        "Servicios de Alimentación Colectiva S.A.C.  ·  comedor industrial  ·  320 raciones al día",
        ["El comedor sirve 320 raciones al día, y el jueves entra la verificación "
         "ambiental del cliente junto con la de sanidad. Es la primera desde que se "
         "renovó el contrato.",
         "Yesenia Mamani lleva cuatro meses como administradora. La matriz que le "
         "dejaron tiene una sola fila para todo lo que pasa en la cocina: la actividad "
         "dice «preparación de alimentos», la entrada dice «insumos», la salida dice "
         "«residuos orgánicos» y el control dice «contenedor con tapa». Está llena, "
         "ordenada y firmada.",
         "En la cocina, sin embargo, pasan varias cosas. Los insumos llegan en cajas de "
         "cartón y bolsas de plástico que se apilan en el patio. Las papas se pelan y se "
         "lavan en una poza cuya agua va directo al desagüe. Se cocina con dos balones "
         "de GLP a la semana. Al terminar el turno se lavan la vajilla y las ollas, y el "
         "agua sale con grasa y detergente. Y cada quince días se cambia el aceite de la "
         "freidora: unos veinte litros que se vacían en un bidón que alguien se lleva.",
         "En julio el desagüe de la cocina se tapó con grasa y el agua salió por la "
         "puerta hacia el patio de secado de ropa. Se destapó con soda cáustica y se "
         "siguió trabajando."], color=AZUL2, y=50, ancho_total=AN)
    return guardar(im, "impamb_s2_caso-a.png", DEST)


def caso_b_s2():
    """El caso B en prosa."""
    AN = 2100
    im = Image.new("RGB", (AN, 1400), BLANCO)
    d = ImageDraw.Draw(im)
    narracion(d, "CASO B",
        "Servicios de Lavandería Industrial S.A.C.  ·  900 prendas por semana",
        ["La lavandería procesa novecientas prendas por semana —mamelucos, casacas y "
         "guantes de la operación— y el cliente anunció que en dos semanas revisa las "
         "matrices de todas sus contratistas.",
         "Aldo Quiñones lleva seis meses como jefe de planta. La matriz que heredó tiene "
         "una sola fila para toda la planta: la actividad dice «lavado de ropa de "
         "trabajo», la entrada dice «agua y detergente», la salida dice «agua residual» "
         "y el control dice «trampa de sólidos a la salida». Está llena, ordenada y "
         "firmada.",
         "En la planta pasan varias cosas. Las prendas llegan en sacos y se clasifican a "
         "mano; las que vienen con aceite van primero a un prelavado con solvente, en "
         "una tina aparte. Después entran a las lavadoras industriales, que consumen "
         "agua y energía. Luego pasan a tres secadoras a gas, cuyos filtros se limpian "
         "cada dos días y sueltan una pelusa que se junta en bolsas. Al final se plancha "
         "y se embala en film plástico.",
         "En marzo se prendió la pelusa acumulada detrás de una secadora. Lo apagaron "
         "con un extintor, se ventiló el local y se siguió trabajando el mismo día."],
        color=TEAL, y=50, ancho_total=AN)
    return guardar(im, "impamb_s2_caso-b.png", DEST)


def a_trabajar_s2():
    """Los datos de organización Y EL REPARTO.

    La rama de `caso` del generador NO dibuja el texto de la lámina cuando hay imagen:
    la figura tiene que llevarlo todo. Con solo los tres números, la lámina se quedaba
    sin decir quién trabaja qué caso ni de qué responde cada integrante."""
    im, d = lienzo(1400)
    y = hitos(d, [("4", "integrantes por equipo"),
                  ("28", "minutos de trabajo"),
                  ("2", "minutos de sustentación")], y=60, alto=320)
    y = franjas(d, [
        ("EL REPARTO", ["La mitad de los equipos trabaja el caso A, la otra mitad el B",
                        "Cada integrante responde por su fila ante el equipo"], AZUL2),
    ], im, y=y + 30, alto=360)
    banda(d, y + 26, 140, "Solo el relato: sin plantilla, sin anexos y sin norma",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_a-trabajar.png", DEST)


def discusion_s2():
    """El formato de la sustentación. Las preguntas del contraste van en el texto de
    la lámina, no aquí: la lámina es de tipo `contenido` y sí las dibuja."""
    im, d = lienzo(1900)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Al partir la actividad aparecieron estos aspectos"], AZUL2),
        ("APOYO", ["Y esta es la tarea de la que sale cada uno"], TEAL),
        ("PREGUNTA", ["¿Qué tarea se les pasó por alto en el otro caso?"], MORADO),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Empezamos por el aspecto que la fila única no registraba",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_discusion.png", DEST)


def reflexion_s2():
    """Las tres consignas del cierre."""
    im, d = lienzo(1900)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que una matriz llena y firmada estaba…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué actividad de tu trabajo cabe en una línea y no debería?"], TEAL),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "impamb_s2_reflexion.png", DEST)


def donde_estamos():
    """Los dos bloques del curso, con la sesión de hoy marcada.

    La figura del curso entero no dice DÓNDE estamos, y esta lámina se llama
    justamente así. La sesión de hoy va en ámbar; las demás, en gris."""
    im, d = lienzo(1500)
    y = franjas(d, [
        ("BLOQUE 1", ["S1 · aspecto e impacto", "S2 · HOY: entradas y salidas",
                      "S3 a S5", "TC1"], AZUL2),
        ("BLOQUE 2", ["S7 a S11 · manejo de residuos", "TC2"], GRIS),
    ], im, y=60, alto=380)
    banda(d, y + 20, 140, "Segunda de cinco: seguimos identificando, todavía no evaluamos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s2_donde-estamos.png", DEST)


FIGURAS = [entra_sale_s2, familias, donde_mirar,
           una_linea, como_se_parte, tareas_olvidadas,
           al_partirla, ni_gruesa_ni_fina, llena_e_incompleta,
           donde_estamos, repaso_s1, ruta_s2, mural_s2, encargo_s2,
           caso_a_s2, caso_b_s2, a_trabajar_s2, discusion_s2, reflexion_s2]

if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    print("Esquemas de SI-IMPAMB · S2")
    print("   destino: %s" % DEST)
    for fn in FIGURAS:
        fn()
    if AVISOS:
        print("\nAVISOS:")
        for a in AVISOS:
            print("   !! %s" % a)
    else:
        print("\nSin avisos: todo el texto cupo en su caja.")
