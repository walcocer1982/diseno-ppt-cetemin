# -*- coding: utf-8 -*-
"""Esquemas de la sesión 1 de SI-IMPAMB: aspecto, impacto y control.

POR QUÉ NO PASA POR EL MODELO
    Son esquemas conceptuales —cajas y texto—, no equipos. La regla del §10
    (nunca texto→imagen) aplica a EQUIPOS: ahí el modelo inventaría geometría.
    Un esquema se dibuja, sale idéntico cada vez y se corrige en una línea.

QUÉ DIBUJA
    Las nueve figuras de las láminas de tema de la S1:
      s1_entra-sale                 PK1 · láminas 11
      s1_como-se-nombra             PK1 · lámina 12
      s1_hay-aspecto                PK1 · lámina 13
      s1_actividad-aspecto-impacto  PK2 · lámina 14
      s1_dentro-fuera               PK2 · lámina 15
      s1_confundirlos               PK2 · lámina 16
      s1_sobre-que-actua            PK3 · lámina 17
      s1_faja-o-via                 PK3 · lámina 18
      s1_parece-control             PK3 · lámina 19

    El ejemplo de las tres primeras es neutro —el lavado de un equipo— a
    propósito: si el esquema usara la planta de concreto o el taller de
    estructuras, estaría resolviendo el caso antes de que el equipo lo lea.

Uso:  python gen_esquemas_impamb_s1.py
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
                      foto, credito, cadena, fichas_foto, caso,
                      hoja, relato, hitos, narracion)

FOTOS = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "fotos")


def f(nombre):
    return os.path.join(FOTOS, nombre)


# Las atribuciones van EN la lámina: son documentos públicos de terceros (§10).
CR_UNICON = ("Fotografías: Unión de Concreteras S.A., «Reporte de Sostenibilidad» "
             "2016 y 2017. Documentos públicos, mostrados como ejemplo de clase.")
CR_ANTAMINA = ("Fotografía: Compañía Minera Antamina, «Reporte de Sostenibilidad 2024». "
               "Documento público, mostrado como ejemplo de clase.")
CR_MIXTO = ("Fotografías: Compañía Minera Antamina, «Reporte de Sostenibilidad 2024»; "
            "Equans Perú, «Reporte de Sostenibilidad 2024»; Unión de Concreteras S.A., "
            "«Reporte de Sostenibilidad 2017». Documentos públicos, ejemplo de clase.")

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ── PK1 · el aspecto es lo que sale de la actividad ────────────────────────
def entra_sale():
    """Las dos caras de una misma actividad. Ejemplo neutro: lavar un equipo.

    La foto va arriba y el balance debajo: primero se ve la actividad, después se
    lee qué deja. Foto de taller ajeno a los dos casos, a propósito."""
    im, d = lienzo(2660)
    y = foto(im, d, f("taller-llanta-equipo.png"), 50, 50, W - 100, 720,
             "EL EQUIPO: lo que se lava al terminar el turno")
    y = comparativa(d, "LO QUE ENTRA", "LO QUE SALE", [
        (["Agua"], ["Equipo limpio"]),
        (["Detergente"], ["Agua con grasa y sólidos"]),
        (["Energía eléctrica"], ["Envase vacío del detergente"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "El aspecto es lo que entra y lo que sale; el impacto, el cambio que eso produce",
          px=CUE)
    credito(d, y + 190, CR_ANTAMINA)
    return guardar(im, "s1_entra-sale.png", DEST)


def como_se_nombra():
    """El aspecto se nombra con un sustantivo de acción, no con la cosa."""
    im, d = lienzo(2060)
    y = franjas(d, [
        ("ASÍ SE NOMBRA", ["Generación de residuo peligroso",
                           "Consumo de agua",
                           "Emisión de material particulado"], TEAL),
        ("ASÍ NO", ["Aceite usado", "El caño abierto", "Polvo"], ROJO),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Un sustantivo de acción, no la cosa ni la escena", px=CUE)
    return guardar(im, "s1_como-se-nombra.png", DEST)


def hay_aspecto():
    """Cuatro actividades para decidir si generan aspecto o no.

    Se mira, no se lee: la pregunta «¿hay aspecto?» se resuelve viendo qué entra y
    qué sale de la escena, y para eso hay que ver la escena. Las cuatro son ajenas
    a los dos casos."""
    im, d = lienzo(2500)
    y = fichas_foto(im, d, [
        ("Manipular un reactivo en el laboratorio", f("taller-mantenimiento.png")),
        ("Mover material con el montacargas", f("almacen-montacargas.png")),
        ("Revisar un tablero eléctrico sin desmontarlo", f("tablero-electrico.png")),
        ("Firmar el parte de la guardia", f("parte-de-guardia.png")),
    ], y=50, alto=600, cols=2, pie="¿hay aspecto?")
    banda(d, y + 20, 140, "Si no entra ni sale nada, no hay aspecto que registrar", px=CUE)
    credito(d, y + 190, CR_MIXTO)
    return guardar(im, "s1_hay-aspecto.png", DEST)


def actividad_aspecto_impacto():
    """La cadena de causa y efecto, en tres eslabones.

    Antes eran tres bandas apiladas, y apilar dice «tres cosas». La lámina enseña
    que UNA CAUSA A LA OTRA, así que la forma tiene que ser una cadena con flechas.

    El eslabón del medio va en ámbar y sin fotografía a propósito: el aspecto es
    justo lo que no se ve —el efluente saliendo— y por eso hay que saber nombrarlo.
    Esa ausencia es la lámina."""
    im, d = lienzo(2040)
    y = cadena(im, d, [
        ("LA ACTIVIDAD", GRIS, "Lo que se hace: lavar el equipo",
         f("taller-llanta-equipo.png")),
        ("EL ASPECTO", AZUL2, "Lo que interactúa con el ambiente: generación de efluente",
         "no se ve: hay que nombrarlo"),
        ("EL IMPACTO", TEAL, "El cambio que ese aspecto causa: alteración del agua",
         f("cuerpo-de-agua.png")),
    ], y=60, alto=760)
    banda(d, y + 20, 140, "Uno causa al otro: sin aspecto no hay impacto", px=CUE)
    credito(d, y + 190, CR_MIXTO)
    return guardar(im, "s1_actividad-aspecto-impacto.png", DEST)


def dentro_fuera():
    """Dónde ocurre cada uno, y por qué eso decide sobre cuál se puede actuar.

    El límite de la operación no se explica: se ve. La foto es una planta con su
    cerco, y la línea que separa el adentro del afuera está en la imagen."""
    im, d = lienzo(2660)
    y = foto(im, d, f("planta-concreto.png"), 50, 50, W - 100, 720,
             "LA OPERACIÓN: la planta, y todo lo que ocurre dentro de ella")
    y = comparativa(d, "DENTRO DE LA OPERACIÓN", "FUERA DE ELLA", [
        (["Ocurre el aspecto"], ["Ocurre el impacto"]),
        (["La empresa manda aquí"], ["La empresa ya no manda"]),
        (["Se puede intervenir"], ["Solo queda reparar"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "Por eso el control se pone dentro, no fuera", px=CUE)
    credito(d, y + 190, CR_UNICON)
    return guardar(im, "s1_dentro-fuera.png", DEST)


def confundirlos():
    """Qué cambia en la matriz según se distingan o no."""
    im, d = lienzo(1780)
    y = comparativa(d, "SI SE CONFUNDEN", "SI SE DISTINGUEN", [
        (["Se registra el daño como si fuera la causa"], ["Se registra la causa y su efecto"]),
        (["El control se pone donde ya pasó"], ["El control se pone donde se origina"]),
        (["El aspecto sigue generando"], ["El aspecto se reduce"]),
    ], y=50)
    banda(d, y + 20, 140, "Confundirlos pone el control en el lugar equivocado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s1_confundirlos.png", DEST)


# ── PK3 · el control actúa sobre el aspecto ────────────────────────────────
def sobre_que_actua():
    """Las dos cosas que se llaman control y no son lo mismo."""
    im, d = lienzo(2060)
    y = franjas(d, [
        ("CONTROL DE ORIGEN", ["Actúa sobre el aspecto",
                               "Antes de que el cambio ocurra",
                               "Reduce lo que sale"], AZUL2),
        ("MITIGACIÓN", ["Actúa sobre el impacto",
                        "Después de que el cambio ocurrió",
                        "No reduce lo que sale"], GRIS),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Las dos hacen falta; solo una es control del aspecto", px=CUE)
    return guardar(im, "s1_sobre-que-actua.png", DEST)


def faja_o_via():
    """El mismo polvo, dos intervenciones distintas.

    La foto va arriba y es UNA SOLA a propósito: es el mismo polvo el que se
    responde de dos maneras. Si fueran dos fotos, parecerían dos problemas."""
    im, d = lienzo(2660)
    y = foto(im, d, f("via-afirmada-polvo.png"), 50, 50, W - 100, 720,
             "EL ASPECTO: material particulado que se levanta al transitar")
    y = comparativa(d, "CUBRIR LA FAJA", "REGAR LA VÍA", [
        (["Sobre el aspecto"], ["Sobre el impacto"]),
        (["Ya no se levanta polvo"], ["El polvo se levanta igual"]),
        (["Deja de generarse"], ["Se asienta lo que ya salió"]),
    ], y=y + 40)
    banda(d, y + 20, 140, "Regar es necesario y no sustituye a cubrir", px=CUE)
    credito(d, y + 190, CR_ANTAMINA)
    return guardar(im, "s1_faja-o-via.png", DEST)


def parece_control():
    """Cuatro medidas para decidir sobre cuál de los dos actúa cada una.

    Aquí sí se usa el mundo del caso, y a propósito: la cuarta es la cisterna que
    Ernesto enseña en cada visita. La lámina 18 acaba de enseñar que regar es
    mitigación; esta hace que lo apliquen a la medida de la que el caso presume."""
    im, d = lienzo(2500)
    y = fichas_foto(im, d, [
        ("Encerrar la pila de agregado", f("agregado-cargador.png")),
        ("Reusar en la planta el agua de lavado", f("cuerpo-de-agua.png")),
        ("Sembrar árboles en el límite del terreno", f("revegetacion-limite.png")),
        ("Regar la carretera tres veces al día", f("via-afirmada-polvo.png")),
    ], y=50, alto=600, cols=2, pie="¿sobre cuál actúa?")
    banda(d, y + 20, 140, "Un control vistoso puede dar un aspecto por resuelto sin tocarlo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    credito(d, y + 190, CR_MIXTO)
    return guardar(im, "s1_parece-control.png", DEST)


# ── las de apoyo: conexión, aplicación, discusión y reflexión ──────────────
# Mismo molde que `gen_esquemas_si_s1.py` del curso 1: todo dentro de cuadros,
# una banda de cierre con la idea que hay que llevarse, y el dato de tiempo al pie.

def curso_en_una_lamina():
    """Los dos bloques del curso y su colaborativo. Cuarenta y ocho horas, no noventa
    y seis: este curso tiene DOS bloques de cinco sesiones, no cuatro de seis."""
    im, d = lienzo(2030)
    y = franjas(d, [
        ("BLOQUE 1", ["Sesiones 1 a 5", "Aspectos e impactos", "Cierra con el TC1"], AZUL2),
        ("BLOQUE 2", ["Sesiones 7 a 11", "Manejo de residuos", "Cierra con el TC2"], TEAL),
    ], im, y=60, alto=360)
    banda(d, y + 20, 130, "Doce sesiones  ·  cuarenta y ocho horas", px=CUE)
    banda(d, y + 175, 120, "Lo ambiental primero se identifica y después se maneja",
          px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s1_curso-en-una-lamina.png", DEST)


def evaluacion():
    """Qué se califica y cuánto pesa."""
    im, d = lienzo(2030)
    y = franjas(d, [
        ("TC1", ["Matriz de aspectos e impactos", "Cinco criterios  ·  de 5 a 20"], AZUL2),
        ("TC2", ["Informe de manejo de residuos", "Cinco criterios  ·  de 5 a 20"], TEAL),
        ("SESIÓN", ["Lista de cotejo  ·  cinco criterios de 0 a 4", "No lleva nota"], GRIS),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "La suma de los cinco criterios ES la nota del equipo", px=CUE,
          fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s1_evaluacion.png", DEST)


def ruta_s1():
    """Los cinco momentos de esta sesión, con lo que se hace en cada uno."""
    im, d = lienzo(2600)
    y = franjas(d, [
        ("CONEXIÓN", ["Mirar una operación y decir qué sale de ella"], GRIS),
        ("ADQUISICIÓN", ["Aspecto, impacto, y sobre cuál actúa el control"], AZUL2),
        ("APLICACIÓN", ["Cuatro pasos sobre el relato de una empresa"], TEAL),
        ("DISCUSIÓN", ["Contrastar el control que cada equipo dio por bueno"], MORADO),
        ("REFLEXIÓN", ["Antes pensaba… ahora pienso…"], GRIS),
    ], im, y=60, alto=360)
    banda(d, y + 20, 130, "Lo que se mira al principio es lo que se sabe nombrar al final", px=CUE)
    return guardar(im, "impamb_s1_ruta.png", DEST)


def encargo():
    """La hoja que el equipo entrega, vacía y con sus encabezados.

    Las cuatro columnas son los cuatro pasos del caso, en el mismo orden y con las
    mismas palabras: si la lámina los reformula, el equipo trabaja sobre una consigna
    y se le califica por otra."""
    im, d = lienzo(2200)
    y = hoja(d, ["LO QUE SALE", "EL CAMBIO QUE PRODUCE",
                 "EL CONTROL QUE YA EXISTE", "¿SOBRE CUÁL ACTÚA?"],
             [["El polvo de la faja", "Aire cargado en la carretera", "", ""],
              ["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""]], y=60, alto_fila=175, muestra=1)
    banda(d, y + 24, 140, "La fila que se quede sin control es la respuesta del paso 4",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 184, 120, "Se describe lo que hay, no se propone lo que falta", px=NOTA)
    return guardar(im, "impamb_s1_encargo.png", DEST)


def ficha_caso_a():
    """El caso A, tal como está escrito en el diseño de sesión: cuatro párrafos.

    No se resume ni se trocea. El relato es el instrumento (§12): el equipo recibe
    SOLO esto, y lo que tiene que hacer es reconstruir qué pasa a partir de la
    historia. Una lista de hechos sueltos convierte el ejercicio en «busca el dato»."""
    AN = 2100
    im = Image.new("RGB", (AN, 1200), BLANCO)
    d = ImageDraw.Draw(im)
    narracion(d, "CASO A",
        "Concretos y Agregados del Centro S.A.C.  ·  planta de concreto premezclado",
        ["El lunes llegó el aviso: el jueves de la próxima semana el cliente hace su "
         "visita de verificación ambiental, y el contrato de suministro se renueva o no "
         "según ese informe. Son 180 m³ de concreto al día para la obra de la mina.",
         "Ernesto Alvarado lleva siete meses como jefe de planta. Una faja lleva el "
         "agregado de la tolva al mezclador y va descubierta: cuando corre, se levanta "
         "una nube que el viento arrastra hacia la carretera y hacia las tres casas del "
         "otro lado. Los vecinos ya reclamaron dos veces por escrito.",
         "Al terminar el turno se lavan los ocho mixers. El agua sale con cemento y "
         "arena, corre por una zanja hasta un pozo de sedimentación y el pozo se limpia "
         "los viernes. El mes pasado se colmató un miércoles y el agua siguió de largo "
         "hasta la acequia de riego; el regante del sector vino a reclamar y se le pagó "
         "el jornal perdido. No se anotó en ninguna parte.",
         "Contra el polvo, la planta compró una cisterna que riega la carretera tres "
         "veces al día. Ernesto la muestra en cada visita: es lo primero que enseña. La "
         "faja sigue descubierta."], color=AZUL2, y=50, ancho_total=AN)
    return guardar(im, "impamb_s1_caso-a.png", DEST)


def ficha_caso_b():
    """El caso B, los mismos cuatro párrafos del diseño de sesión."""
    AN = 2100
    im = Image.new("RGB", (AN, 1200), BLANCO)
    d = ImageDraw.Draw(im)
    narracion(d, "CASO B",
        "Estructuras Metálicas y Montaje S.A.C.  ·  taller de habilitación de estructuras",
        ["El viernes 22 se entrega la estructura del techo de la sala de bombas, y el "
         "cliente hace la inspección ambiental del taller el mismo día que recibe. Son "
         "34 toneladas habilitadas en seis semanas.",
         "Delia Ccopa lleva cinco meses como supervisora. El taller trabaja con cuatro "
         "puestos de soldadura y dos esmeriles de banco. Cuando los cuatro puestos están "
         "encendidos, el humo se acumula bajo la calamina y baja hasta la altura de la "
         "puerta; el taller colinda con el patio de una escuela.",
         "De la habilitación salen retazos de plancha y viruta, que se juntan en una "
         "esquina del patio sobre tierra. Cuando llueve, del montón corre un agua rojiza "
         "que se mete bajo el cerco. En marzo un vecino reclamó que se le manchó el muro; "
         "se le pintó el muro y no se registró.",
         "Contra el humo, el taller instaló dos extractores en el techo. Delia los "
         "enciende antes de que llegue cualquier visita. Los puestos de soldadura siguen "
         "sin cortina ni campana."], color=TEAL, y=50, ancho_total=AN)
    return guardar(im, "impamb_s1_caso-b.png", DEST)


def a_trabajar():
    """Solo los datos de organización: los que no están en ninguna otra lámina."""
    im, d = lienzo(1460)
    y = hitos(d, [("4", "integrantes por equipo"),
                  ("28", "minutos de trabajo"),
                  ("2", "minutos de sustentación por equipo")], y=60, alto=320)
    banda(d, y + 26, 140, "Solo el relato: sin plantilla, sin anexos y sin norma",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s1_a-trabajar.png", DEST)


def formato_discusion():
    """El formato de la sustentación: afirmación, apoyo y pregunta."""
    im, d = lienzo(2060)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Este control actúa sobre el aspecto, o sobre el impacto"], AZUL2),
        ("APOYO", ["Y lo sostenemos en lo que el relato dice que pasa"], TEAL),
        ("PREGUNTA", ["¿Qué salida se queda sin control en el caso del otro equipo?"], MORADO),
    ], im, y=60, alto=360)
    banda(d, y + 20, 140, "Empezamos por el control que la empresa enseña primero",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "impamb_s1_discusion.png", DEST)


def reflexion():
    """Las tres consignas del cierre, cada una en su cuadro."""
    im, d = lienzo(2080)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que controlar un impacto era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Qué control de tu trabajo actúa sobre el daño ya hecho?"], TEAL),
    ], im, y=60, alto=360)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "impamb_s1_reflexion.png", DEST)


def mural_entrada():
    """La lámina de «Veo · Pienso · Me pregunto»: una foto y tres preguntas.

    Va SIN rótulos sobre la foto a propósito: si la lámina ya dice dónde mirar, la
    dinámica se acabó antes de empezar. Los rótulos aparecen en la 11, no aquí."""
    # 620 de foto + tres bandas de 240 con su separación + la atribución no caben
    # en 1400: la tercera banda y el crédito se dibujaban fuera del lienzo y
    # `guardar` los recortaba sin avisar. El alto se calcula, no se estima.
    ALTO_F, ALTO_B, SEP = 620, 360, 30
    im, d = lienzo(50 + ALTO_F + 40 + 3 * (ALTO_B + SEP) + 200)
    y = foto(im, d, f("mixer-en-planta.png"), 50, 50, W - 100, ALTO_F)
    y = franjas(d, [
        ("VEO", ["¿Qué está pasando en esta operación?"], GRIS),
        ("PIENSO", ["¿Qué sale de ella hacia el entorno?"], AZUL2),
        ("ME PREGUNTO", ["¿Qué cambia afuera por lo que sale?"], TEAL),
    ], im, y=y + 40, alto=ALTO_B)
    credito(d, y + 20, CR_UNICON)
    return guardar(im, "impamb_s1_mural-entrada.png", DEST)


FIGURAS = [entra_sale, como_se_nombra, hay_aspecto,
           actividad_aspecto_impacto, dentro_fuera, confundirlos,
           sobre_que_actua, faja_o_via, parece_control,
           # las de apoyo, que el curso 1 tiene y a esta sesión le faltaban
           curso_en_una_lamina, evaluacion, ruta_s1, mural_entrada, encargo,
           ficha_caso_a, ficha_caso_b, a_trabajar, formato_discusion, reflexion]

if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    print("Esquemas de SI-IMPAMB · S1")
    print("   destino: %s" % DEST)
    for fn in FIGURAS:
        print("   %s" % os.path.basename(str(fn())))
    if AVISOS:
        print(" · AVISOS — texto que no cupo en su caja:")
        for a in AVISOS:
            print("   !! %s" % a)
    else:
        print(" · Sin avisos: todo el texto cupo en su caja.")
