# -*- coding: utf-8 -*-
"""Esquemas de la sesión 2 de EOM · Fundamentos mecánicos de equipos mineros.

Sistema hidráulico y sistema de enfriamiento. Son los QUINCE que se dibujan;
la ruta de la sesión no está aquí porque vive en `fmeq/comun/` y sirve a las
diez sesiones.

LO QUE NO SE DIBUJA. El punto clave 1 pide «corte de un cilindro de doble
efecto» y el 2 «esquema de la válvula de retención». Un corte es geometría:
dibujarlo es inventarlo (regla 3). Lo que va aquí es el RECORRIDO del aceite
como flujo de bloques nombrados, y lo que hace cada uno. La pieza por dentro,
cuando haga falta, saldrá del corte del fabricante.

La curva de viscosidad sí se dibuja: es una escala numérica, y las escalas no
tienen cuerpo que fotografiar.

Métrica del §11: lienzo de 1500 px de ancho, cuerpo de 52 px, sin bbox_inches.
Van SIN título dentro: el título lo pone la lámina.

Uso:  python gen_esquemas_fmeq_s2.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, guardar, lienzo, nota,
)
from gen_esquemas_s1_sesion import _caja, _celda, _redonda  # noqa: E402
from gen_esquemas_fmeq_s1 import (  # noqa: E402
    _banda, _cabecera, _flecha_abajo, _flecha_der,
)

CARPETA = "fmeq/s2/"
ROJO = "#C0392B"          # solo lo que está mal, y con moderación (§11)
ROJO_CLARO = "#F7E4E1"    # el fondo de esa columna, para que el rojo no grite


def _guardar(fig, nombre):
    guardar(fig, CARPETA + nombre)


# ═══════════════════════════════════════════ 1 · de dónde venimos
def de_donde():
    """El puente de la S1 a la S2: dos sistemas en la misma máquina."""
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _cabecera(ax, 3, H * 0.72, 45, H * 0.13, "SESIÓN 1 · TREN DE POTENCIA", AZUL)
    _cabecera(ax, 52, H * 0.72, 45, H * 0.13, "SESIÓN 2 · CIRCUITO HIDRÁULICO", VERDE)
    pares = [("la fuerza que MUEVE el equipo", "la fuerza que LEVANTA y SOSTIENE"),
             ("motor, transmisión, ruedas", "bomba, válvula, cilindro"),
             ("se corta cuando algo patina", "sigue ahí con el motor apagado")]
    y = H * 0.70
    alto = H * 0.135
    for a, b in pares:
        y -= alto + 1.0
        _celda(ax, 3, y, 45, alto, a, CLARO, MARINO, tam=NOTA * 0.90)
        _celda(ax, 52, y, 45, alto, b, CLARO, MARINO, tam=NOTA * 0.90)
    _banda(ax, H * 0.05, H * 0.12, "Los dos viven en la misma máquina, y se revisan distinto")
    _guardar(fig, "fmeq-s2_de-donde.png")


# ═══════════════════════════════════════════ 2 · el recorrido del aceite
def circuito():
    """Tanque, bomba, válvula y cilindro, con el retorno por el filtro."""
    ASP = 1.20
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    cajas = [("TANQUE", GRIS, "guarda el aceite"),
             ("BOMBA", AZUL, "lo toma y lo mueve"),
             ("VÁLVULA", MORADO, "decide a qué lado va"),
             ("CILINDRO", VERDE, "lo vuelve movimiento")]
    # Cuatro cajas y tres huecos tienen que caber en 100 unidades menos los
    # márgenes: con 22,5 de ancho la cuarta —CILINDRO— salía cortada.
    x, w, hueco = 3.5, 21.0, 3.0
    for nombre, color, det in cajas:
        _redonda(ax, x, H * 0.60, w, H * 0.20, color)
        ax.text(x + w / 2, H * 0.70, nombre, ha="center", va="center", family=F,
                fontsize=NOTA * 0.95, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, H * 0.53, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.85, color=MARINO)
        if x < 70:
            _flecha_der(ax, x + w + 0.4, H * 0.70, 2.2)
        x += w + hueco

    # el retorno, por debajo
    ax.annotate("", xy=(4.0, H * 0.36), xytext=(93.0, H * 0.36),
                arrowprops=dict(arrowstyle="-|>", color=GRIS, linewidth=2.4))
    ax.text(50, H * 0.30, "el aceite del otro lado retorna al tanque por el filtro",
            ha="center", va="center", family=F, fontsize=NOTA * 0.88, color=GRIS)

    _celda(ax, 3, H * 0.14, 94, H * 0.11,
           "La válvula de alivio limita la presión máxima del circuito",
           CLARO, MARINO, tam=NOTA * 0.92)
    _banda(ax, H * 0.02, H * 0.09, "El vástago sale cuando entra aceite por la cámara mayor")
    _guardar(fig, "fmeq-s2_circuito.png")


# ═══════════════════════════════════════════ 3 · caudal y presión
def caudal_presion():
    """Las dos magnitudes del circuito, y por qué el aceite sostiene."""
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.46, 45, H * 0.38, AZUL)
    ax.text(25.5, H * 0.74, "CAUDAL", ha="center", va="center", family=F,
            fontsize=FUERTE * 1.05, fontweight="bold", color=BLANCO)
    ax.text(25.5, H * 0.62, "cuánto aceite se mueve", ha="center", va="center",
            family=F, fontsize=NOTA * 0.90, color=BLANCO)
    ax.text(25.5, H * 0.52, "sin caudal\nno hay movimiento", ha="center", va="center",
            family=F, fontsize=NOTA * 0.90, color=BLANCO, linespacing=1.3)

    _redonda(ax, 52, H * 0.46, 45, H * 0.38, VERDE)
    ax.text(74.5, H * 0.74, "PRESIÓN", ha="center", va="center", family=F,
            fontsize=FUERTE * 1.05, fontweight="bold", color=BLANCO)
    ax.text(74.5, H * 0.62, "con cuánta fuerza empuja", ha="center", va="center",
            family=F, fontsize=NOTA * 0.90, color=BLANCO)
    ax.text(74.5, H * 0.52, "sin presión\nno hay fuerza", ha="center", va="center",
            family=F, fontsize=NOTA * 0.90, color=BLANCO, linespacing=1.3)

    _celda(ax, 3, H * 0.26, 94, H * 0.14,
           "El aceite no se comprime: por eso empuja, y por eso sostiene",
           CLARO, MARINO, tam=CUERPO * 0.92)
    _banda(ax, H * 0.06, H * 0.13, "Las dos hacen falta: una mueve, la otra hace fuerza")
    _guardar(fig, "fmeq-s2_caudal-presion.png")


# ═══════════════════════════════════════════ 4 · lo que retiene la carga
def retencion():
    """Qué pasa en el circuito cuando el motor se apaga con la carga arriba."""
    ASP = 1.05
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = [("EL MOTOR SE APAGA", "la bomba deja de dar caudal", AZUL),
             ("LA VÁLVULA DE RETENCIÓN CIERRA", "el aceite queda encerrado", MORADO),
             ("EL ACEITE ENCERRADO NO SE COMPRIME", "la carga se queda arriba", VERDE),
             ("ESA PRESIÓN ATRAPADA TIENE NOMBRE", "energía residual", AMBAR)]
    y = H * 0.90
    alto = H * 0.135
    for titulo, det, color in pasos:
        tinta = MARINO if color == AMBAR else BLANCO
        _redonda(ax, 3, y - alto, 94, alto, color)
        ax.text(50, y - alto * 0.36, titulo, ha="center", va="center", family=F,
                fontsize=NOTA * 0.92, fontweight="bold", color=tinta)
        ax.text(50, y - alto * 0.72, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, color=tinta)
        if color != AMBAR:
            _flecha_abajo(ax, 50, y - alto - 0.6, 3.0)
        y -= alto + 4.2
    _banda(ax, H * 0.03, H * 0.10, "Apagar el equipo le quita el caudal, no la presión")
    _guardar(fig, "fmeq-s2_retencion.png")


# ═══════════════════════════════════════════ 5 · por dónde sale
def energia_residual():
    """La energía atrapada sale por donde se abra primero: dos formas."""
    ASP = 1.25
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    ax.text(50, H * 0.90, "La energía sale por donde se abra primero", ha="center",
            va="center", family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    _cabecera(ax, 3, H * 0.70, 45, H * 0.12, "POR EL MANDO", VERDE)
    _cabecera(ax, 52, H * 0.70, 45, H * 0.12, "POR LA UNIÓN", ROJO)
    pares = [("se alivia de a poco", "se libera todo de golpe"),
             ("la carga baja controlada", "la carga cae"),
             ("es lo que manda el manual", "la carga cae sin aviso")]
    y = H * 0.68
    alto = H * 0.13
    for a, b in pares:
        y -= alto + 1.0
        _celda(ax, 3, y, 45, alto, a, CLARO, MARINO, tam=NOTA * 0.92)
        _celda(ax, 52, y, 45, alto, b, ROJO_CLARO, MARINO, tam=NOTA * 0.92)
    _banda(ax, H * 0.05, H * 0.11, "Aflojar una unión con la carga arriba libera todo de golpe")
    _guardar(fig, "fmeq-s2_energia-residual.png")


# ═══════════════════════════════════════════ 6 · el aceite y la temperatura
def viscosidad():
    """Escala: qué le pasa al aceite según dónde esté la temperatura."""
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    tramos = [("FRÍO", MORADO, "espeso:\ncuesta moverlo"),
              ("RANGO DEL MANUAL", VERDE, "el que el circuito\nnecesita"),
              ("CALIENTE", ROJO, "delgado:\npasa por las holguras")]
    x, w = 3.0, 30.6
    for nombre, color, det in tramos:
        _redonda(ax, x, H * 0.52, w, H * 0.16, color)
        ax.text(x + w / 2, H * 0.60, nombre, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, fontweight="bold", color=BLANCO)
        ax.text(x + w / 2, H * 0.38, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO, linespacing=1.35)
        x += w + 1.6
    ax.annotate("", xy=(96, H * 0.76), xytext=(4, H * 0.76),
                arrowprops=dict(arrowstyle="-|>", color=GRIS, linewidth=2.4))
    ax.text(50, H * 0.85, "temperatura del aceite", ha="center", va="center",
            family=F, fontsize=NOTA, color=GRIS)
    _banda(ax, H * 0.10, H * 0.14,
           "El enfriador es lo que mantiene el aceite dentro del rango")
    _guardar(fig, "fmeq-s2_viscosidad.png")


# ═══════════════════════════════════════════ 7 · la deriva
def deriva():
    """Por qué una carga baja sola, y qué prueba que baje."""
    ASP = 1.30
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = ["el aceite caliente está más delgado",
             "pasa por holguras que en frío sellaba",
             "esa fuga interna hace que la carga baje sola"]
    y = H * 0.80
    alto = H * 0.115
    for i, t in enumerate(pasos):
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 11, alto, AZUL)
        ax.text(8.5, y + alto / 2, str(i + 1), ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(17, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO)
        y -= alto + 1.4
    _redonda(ax, 3, H * 0.22, 94, H * 0.15, MARINO)
    ax.text(50, H * 0.295, "Bajar sola con la máquina apagada se llama DERIVA",
            ha="center", va="center", family=F, fontsize=CUERPO, fontweight="bold",
            color=BLANCO)
    _banda(ax, H * 0.05, H * 0.12, "La deriva prueba que el circuito todavía tiene presión")
    _guardar(fig, "fmeq-s2_deriva.png")


# ═══════════════════════════════════════════ 8 · bajar la carga
def secuencia():
    """Los tres primeros pasos, antes de apagar."""
    ASP = 1.35
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = [("1", "Se baja la carga al piso, si el equipo lo permite", VERDE),
             ("2", "Si no baja, se apoya sobre un soporte mecánico firme", AZUL),
             ("3", "Recién entonces se apaga y se corta el arranque", MORADO)]
    y = H * 0.74
    alto = H * 0.155
    for n, t, color in pasos:
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 12, alto, color)
        ax.text(9, y + alto / 2, n, ha="center", va="center", family=F,
                fontsize=FUERTE * 1.1, fontweight="bold", color=BLANCO)
        ax.text(18, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.95, color=MARINO)
        y -= alto + 1.6
    _banda(ax, H * 0.06, H * 0.13, "La carga apoyada no depende del aceite para quedarse")
    _guardar(fig, "fmeq-s2_secuencia.png")


# ═══════════════════════════════════════════ 9 · aliviar y bloquear
def bloqueo_orden():
    """Los pasos que siguen, y por qué el orden no se negocia."""
    ASP = 1.20
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = [("4", "Se alivia la presión con el mando, no con la unión", VERDE),
             ("5", "Se bloquea y se señaliza antes de que alguien se acerque", AZUL),
             ("6", "Quien bloquea guarda la llave hasta terminar", MORADO)]
    y = H * 0.76
    alto = H * 0.145
    for n, t, color in pasos:
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 12, alto, color)
        ax.text(9, y + alto / 2, n, ha="center", va="center", family=F,
                fontsize=FUERTE * 1.1, fontweight="bold", color=BLANCO)
        ax.text(18, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO)
        y -= alto + 1.4
    _redonda(ax, 3, H * 0.20, 94, H * 0.14, MARINO)
    ax.text(50, H * 0.27, "El orden importa: aliviar después de abrir llega tarde",
            ha="center", va="center", family=F, fontsize=CUERPO, fontweight="bold",
            color=BLANCO)
    _banda(ax, H * 0.04, H * 0.12, "DS 024-2016-EM · artículo 346: bloqueo y señalización")
    _guardar(fig, "fmeq-s2_bloqueo-orden.png")


# ═══════════════════════════════════════════ 10 · la ficha del caso
def caso_ficha():
    """Los hechos del caso, sin la respuesta."""
    ASP = 1.16
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.80, 94, H * 0.15, AZUL)
    ax.text(50, H * 0.895, "Sostenimiento y Servicios de Interior Mina S.A.C.",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            fontweight="bold", color=BLANCO)
    ax.text(50, H * 0.833, "Plataforma elevadora · cruzada en el único acceso al frente",
            ha="center", va="center", family=F, fontsize=NOTA * 0.9, color=BLANCO)

    hechos = [("ANOCHE", "el motor se apagó con la canastilla\narriba, a cuatro metros veinte"),
              ("EL ACEITE", "quedó caliente: la máquina\ntrabajó toda la tarde"),
              ("ESTA MAÑANA", "la canastilla amaneció treinta\ncentímetros más abajo"),
              ("EL OPERADOR NUEVO", "propone aflojar la manguera\n«ya no debe tener presión»")]
    y = H * 0.63
    alto = H * 0.135
    for rot, det in hechos:
        _celda(ax, 3, y, 32, alto, rot, CLARO, GRIS, negrita=True, tam=NOTA * 0.82)
        _celda(ax, 36, y, 61, alto, det, BLANCO, MARINO, tam=NOTA * 0.88)
        y -= alto + 1.0
    nota(ax, H * 0.055, "La guardia entra a las siete.")
    _guardar(fig, "fmeq-s2_caso-ficha.png")


# ═══════════════════════════════════════════ 11 · antes de resolver
def antes_de_resolver():
    """La pregunta que abre, y lo que aprieta."""
    ASP = 1.60
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.58, 94, H * 0.30, MARINO)
    ax.text(50, H * 0.73, "La máquina está apagada desde anoche.\n"
                          "¿Qué sostiene la canastilla a cuatro metros veinte?",
            ha="center", va="center", family=F, fontsize=CUERPO * 0.95,
            fontweight="bold", color=BLANCO, linespacing=1.4)
    fichas = [("30 cm", "bajó sola, sin que\nnadie la tocara"),
              ("LAS SIETE", "entra la guardia por\nese único acceso"),
              ("UNA MANGUERA", "es lo que el operador\nnuevo quiere aflojar")]
    x = 3
    for grande, det in fichas:
        _redonda(ax, x, H * 0.14, 30.5, H * 0.36, CLARO)
        ax.text(x + 15.25, H * 0.41, grande, ha="center", va="center", family=F,
                fontsize=CUERPO, fontweight="bold", color=AZUL)
        ax.text(x + 15.25, H * 0.26, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO, linespacing=1.35)
        x += 32.2
    _guardar(fig, "fmeq-s2_antes-de-resolver.png")


# ═══════════════════════════════════════════ 12 · el encargo
def encargo():
    """Las cuatro filas de la hoja en blanco."""
    ASP = 1.10
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    filas = ["El recorrido del aceite, del tanque al cilindro, con sus componentes",
             "Qué retiene la carga con el motor apagado, y qué prueba que la retiene",
             "Qué explica que la canastilla bajara sin que nadie la tocara",
             "La secuencia para acercarse, en orden, y qué pasa si se altera"]
    y = H * 0.76
    alto = H * 0.145
    for i, t in enumerate(filas):
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 12, alto, AZUL)
        ax.text(9, y + alto / 2, str(i + 1), ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(17, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.88, color=MARINO)
        y -= alto + 1.2
    _banda(ax, H * 0.05, H * 0.11, "Una hoja en blanco por equipo · 40 minutos")
    _guardar(fig, "fmeq-s2_encargo.png")


# ═══════════════════════════════════════════ 13 · cómo trabajamos
def como_trabajamos():
    """Los pasos del trabajo en equipo, en orden."""
    ASP = 1.40
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    pasos = [("1", "Dibujen el recorrido del aceite antes de discutir nada", AZUL),
             ("2", "Respondan qué sostiene la carga ahora mismo, apagada", MARINO),
             ("3", "Expliquen los treinta centímetros con lo que saben", VERDE),
             ("4", "Escriban la secuencia numerada, del primer paso al último", MORADO)]
    y = H * 0.78
    alto = H * 0.145
    for n, t, color in pasos:
        _redonda(ax, 3, y, 94, alto, CLARO)
        _redonda(ax, 3, y, 11, alto, color)
        ax.text(8.5, y + alto / 2, n, ha="center", va="center", family=F,
                fontsize=FUERTE, fontweight="bold", color=BLANCO)
        ax.text(16, y + alto / 2, t, ha="left", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO)
        y -= alto + 1.2
    _banda(ax, H * 0.06, H * 0.13, "Equipos de 3 · 40 minutos · expone uno por equipo")
    _guardar(fig, "fmeq-s2_como-trabajamos.png")


# ═══════════════════════════════════════════ 14 · la puesta en común
def puesta_comun():
    """El orden de la sustentación y el formato de la respuesta."""
    ASP = 1.20
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    ax.text(50, H * 0.90, "Dos minutos por equipo", ha="center", va="center",
            family=F, fontsize=CUERPO, fontweight="bold", color=MARINO)
    partes = [("AFIRMACIÓN", AZUL, "qué sostiene\nla canastilla"),
              ("APOYO", VERDE, "qué hecho del caso\nlo prueba"),
              ("PREGUNTA", MORADO, "lo que todavía\nfalta saber")]
    x = 3
    for nombre, color, det in partes:
        _redonda(ax, x, H * 0.40, 30.5, H * 0.40, CLARO)
        _redonda(ax, x, H * 0.68, 30.5, H * 0.12, color)
        ax.text(x + 15.25, H * 0.74, nombre, ha="center", va="center", family=F,
                fontsize=NOTA, fontweight="bold", color=BLANCO)
        ax.text(x + 15.25, H * 0.54, det, ha="center", va="center", family=F,
                fontsize=NOTA * 0.92, color=MARINO, linespacing=1.35)
        x += 32.2
    _banda(ax, H * 0.10, H * 0.13, "Empezamos por la secuencia, y comparamos el orden")
    _guardar(fig, "fmeq-s2_puesta-comun.png")


# ═══════════════════════════════════════════ 15 · el puente
def puente_s3():
    """Adónde va esto: la sesión siguiente y el colaborativo del bloque."""
    ASP = 1.45
    fig, ax = lienzo(ASP)
    H = 100 / ASP

    _redonda(ax, 3, H * 0.56, 45, H * 0.32, AZUL)
    ax.text(25.5, H * 0.80, "LA PRÓXIMA SESIÓN", ha="center", va="center",
            family=F, fontsize=NOTA * 0.92, fontweight="bold", color=BLANCO)
    ax.text(25.5, H * 0.66, "Scooptram y minetruck:\nsus componentes críticos\ny el formato de pre-uso",
            ha="center", va="center", family=F, fontsize=NOTA * 0.90, color=BLANCO,
            linespacing=1.4)
    _redonda(ax, 52, H * 0.56, 45, H * 0.32, AMBAR)
    ax.text(74.5, H * 0.80, "AL CIERRE DEL BLOQUE", ha="center", va="center",
            family=F, fontsize=NOTA * 0.92, fontweight="bold", color=MARINO)
    ax.text(74.5, H * 0.66, "TC1: hay un operador\ndebajo de un equipo,\ny hay que decidir",
            ha="center", va="center", family=F, fontsize=NOTA * 0.90, color=MARINO,
            linespacing=1.4)
    ax.text(50, H * 0.34, "Hoy aprendiste que una máquina apagada sigue teniendo energía.\n"
                          "En el TC1 esa energía va a estar sobre la cabeza de alguien.",
            ha="center", va="center", family=F, fontsize=NOTA, color=MARINO,
            linespacing=1.4)
    nota(ax, H * 0.12, "Antes de la próxima clase: el recurso autónomo del EVA.")
    _guardar(fig, "fmeq-s2_puente-s3.png")


if __name__ == "__main__":
    print("Esquemas de EOM-FMEQ-S2 · Sistema hidráulico y enfriamiento\n")
    for f in (de_donde, circuito, caudal_presion, retencion, energia_residual,
              viscosidad, deriva, secuencia, bloqueo_orden, caso_ficha,
              antes_de_resolver, encargo, como_trabajamos, puesta_comun, puente_s3):
        f()
    print("\n15 esquemas en 04_Recursos-graficos/EOM/esquemas/fmeq/s2/")
