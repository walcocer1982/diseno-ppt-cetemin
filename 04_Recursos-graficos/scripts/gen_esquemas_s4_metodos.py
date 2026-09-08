# -*- coding: utf-8 -*-
"""Esquemas de la sesión 4 · Métodos de explotación subterránea.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Nada de lo FÍSICO. Ni un tajeo, ni un corte, ni una veta, ni el plano de
    una zona: eso existe, está levantado en algún plano, y dibujarlo sería
    inventarlo (CLAUDE.md, regla 3). Las secciones de los dos métodos ya
    entran al PPT por imágenes de fuente que están aprobadas —IMG-EOM-SLS y
    IMG-EOM-CORTE-RELLENO—, y aquí no se repiten.

    Lo que se dibuja son RELACIONES y ARMAZÓN, que es lo único que no tiene
    cuerpo: las dos tablas comparativas del punto clave 3, el procedimiento de
    lectura del punto clave 4, las FICHAS del caso —que son tablas de números,
    no dibujos de la labor—, la hoja de marcar, la ruta, la puesta en común y
    los dos puentes.

    Las cifras de las fichas son las de la variante A del caso, y caen dentro
    de los rangos verificados de las dos tesis UNDAC citadas en casos.csv.
    No hay ninguna cifra inventada aquí.

NO SE FILTRA LA RESPUESTA
    Las láminas 17 y 18 son de Adquisición, o sea que se proyectan ANTES de
    que las parejas marquen. Por eso enseñan el procedimiento y la regla, y no
    llevan ni un ejemplo tomado de la lista de indicios del caso: si lo
    llevaran, la Aplicación llegaría resuelta desde la lámina. Es el mismo
    motivo por el que se reescribió el punto clave 4.

Uso:  python gen_esquemas_s4_metodos.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, VERDE, guardar, lienzo, nota,
)


def _caja(ax, x, y, w, h, color, r=1.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.2,rounding_size=%.1f" % r,
                                facecolor=color, edgecolor="none"))


def _txt(ax, x, y, t, size=None, color=MARINO, bold=False, ha="center"):
    ax.text(x, y, t, ha=ha, va="center", family=F, fontsize=size or CUERPO,
            color=color, linespacing=1.3, fontweight="bold" if bold else "normal")


def _tabla(ax, x0, y0, anchos, alto, cabecera, filas, destacar=None, tam=None):
    y, x = y0, x0
    for w, t in zip(anchos, cabecera):
        ax.add_patch(Rectangle((x, y), w, alto, facecolor=MARINO, edgecolor=BLANCO, lw=2))
        _txt(ax, x + w / 2, y + alto / 2, t, tam or CUERPO - 4, BLANCO, bold=True)
        x += w
    for i, fila in enumerate(filas):
        y -= alto
        x = x0
        base = CLARO if i % 2 == 0 else BLANCO
        for j, (w, t) in enumerate(zip(anchos, fila)):
            es = destacar and (i, j) in destacar
            ax.add_patch(Rectangle((x, y), w, alto, facecolor=AMBAR if es else base,
                                   edgecolor=BLANCO, lw=2))
            _txt(ax, x + w / 2, y + alto / 2, t, tam or CUERPO - 4, MARINO,
                 bold=(j == 0 or es))
            x += w
    return y


S = chr(10)


# ═══════════════════════════════════════ 15 · qué pasa con el hueco (PC3 · 1-4)
def que_pasa_con_el_hueco():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    y = _tabla(ax, 5, H - 15, [22, 33, 33], 12,
               ["", "TAJEO SIN RELLENO", "CORTE Y RELLENO"],
               [["EL HUECO", "queda vacío hasta" + S + "terminar el tajeo",
                 "se rellena después" + S + "de cada corte"],
                ["LAS CAJAS", "aguantan solas" + S + "la abertura",
                 "no la aguantan:" + S + "el relleno sostiene"],
                ["EXIGE", "cajas competentes" + S + "y buzamiento alto",
                 "nada: trabaja" + S + "con cajas malas"],
                ["SIRVE PARA", "potencia grande", "veta angosta"]],
               tam=CUERPO - 4)
    nota(ax, y - 6, "Los dos sacan el mismo mineral. Cambia qué pasa con el hueco que dejan.")
    return guardar(fig, "s4_que-pasa-con-el-hueco.png")


# ═══════════════════════════════════════ 16 · lo que cambia y lo que no (PC3 · 5-8)
def lo_que_cambia():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _tabla(ax, 5, H - 14, [22, 33, 33], 11,
           ["", "TAJEO SIN RELLENO", "CORTE Y RELLENO"],
           [["RENDIMIENTO", "más", "menos"],
            ["SELECTIVIDAD", "menos selectivo", "selectivo"],
            ["MADERA", "casi no consume", "mucho más"],
            ["RELLENO", "no gasta material", "gasta material"]],
           tam=CUERPO - 4)
    _caja(ax, 5, 1.5, 88, 13, MARINO)
    _txt(ax, 49, 10.6, "LO QUE NO CAMBIA:  el ciclo de minado", CUERPO - 4, AMBAR, bold=True)
    _txt(ax, 49, 5.0, "Las cinco operaciones son las mismas en los dos." + S +
         "Cambian las labores y el sostenimiento.", CUERPO - 6, BLANCO)
    return guardar(fig, "s4_lo-que-cambia.png")


# ═══════════════════════════════════════ 13 · las condiciones de los dos (PC2 · 5-8)
def condiciones_de_los_dos():
    """La tabla de condiciones de LOS DOS MÉTODOS DE ESTA SESIÓN.

    Existían ya IMG-EOM-COND-SLS e IMG-EOM-COND-CORTE-RELLENO, y ninguna sirve
    aquí: la primera contrasta con BLOCK CAVING, que la OBS-25 retiró del curso
    por no hallarse operación peruana que lo aplique, y la segunda contrasta con
    cámaras y pilares, que en esta sesión no se enseña. Meter cualquiera de las
    dos sería proyectar un método del que la clase no va a hablar.

    La fila del buzamiento sale igual en las dos columnas a propósito: es un
    parámetro que NO decide, y prepara el punto clave 4 —un indicio que vale
    para los dos no sirve para atribuir—.
    """
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    y = _tabla(ax, 5, H - 15, [24, 32, 32], 12,
               ["EL TERRENO", "TAJEO SIN RELLENO", "CORTE Y RELLENO"],
               [["Potencia", "grande:" + S + "decenas de metros", "angosta:" + S + "cerca de un metro"],
                ["Buzamiento", "alto: el roto" + S + "baja solo", "alto: el roto" + S + "baja solo"],
                ["Cajas", "competentes:" + S + "aguantan solas", "admite cajas" + S + "de RMR bajo"],
                ["Ancho de minado", "mucho mayor" + S + "que la veta", "parecido a" + S + "la potencia"]],
               destacar=[(1, 1), (1, 2)], tam=CUERPO - 5)
    nota(ax, y - 6, "El buzamiento sale igual en los dos: por sí solo no decide nada.")
    return guardar(fig, "s4_condiciones-de-los-dos.png")


# ═══════════════════════════════════════ 17 · cómo se lee un plano (PC4 · 1-4)
def leer_el_plano():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = [("1", "LAS LABORES", "qué labores hay" + S + "en el plano"),
             ("2", "DESCARTA", "lo que aparece" + S + "en los dos métodos"),
             ("3", "BUSCA", "lo que solo puede" + S + "darse en uno"),
             ("4", "LA FICHA", "recién ahora:" + S + "¿lo confirma?")]
    y, alto = H - 15, 12
    for i, (n, t, sub) in enumerate(pasos):
        col = AMBAR if i == 2 else MARINO
        ax.add_patch(Circle((11, y + alto / 2), 4.6, facecolor=col))
        _txt(ax, 11, y + alto / 2 + 0.3, n, CUERPO - 2, MARINO if i == 2 else BLANCO, bold=True)
        _caja(ax, 18, y, 30, alto, CLARO)
        _txt(ax, 33, y + alto / 2, t, CUERPO - 3, MARINO, bold=True)
        _txt(ax, 52, y + alto / 2, sub, CUERPO - 5, GRIS, ha="left")
        if i < 3:
            ax.annotate("", xy=(11, y - 2.6), xytext=(11, y - 0.4),
                        arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=14))
        y -= alto + 2.5
    nota(ax, y + 6, "Un plano no dice el método: lo dicen sus labores.")
    return guardar(fig, "s4_leer-el-plano.png")


# ═══════════════════════════════════════ 18 · cómo se sostiene la respuesta (PC4 · 5-8)
def sostener_la_respuesta():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    y = H - 15
    bloques = [("LA LABOR SUGIERE", "es lo primero que se lee", AZUL),
               ("LA FICHA CONFIRMA", "los cuatro datos del yacimiento", VERDE),
               ("DOS DATOS BASTAN", "dos bien elegidos, no diez mal elegidos", MORADO)]
    for t, sub, col in bloques:
        _caja(ax, 4, y, 92, 12, col)
        _txt(ax, 26, y + 6, t, CUERPO - 3, BLANCO, bold=True)
        _txt(ax, 58, y + 6, sub, CUERPO - 5, BLANCO, ha="left")
        y -= 15
    _caja(ax, 4, y - 3, 92, 13, AMBAR)
    _txt(ax, 50, y + 6.5, "¿SE CONTRADICEN LA LABOR Y LA FICHA?", CUERPO - 4, MARINO, bold=True)
    _txt(ax, 50, y + 0.5, "Se vuelve a leer el plano. No se elige la que más gusta.",
         CUERPO - 5, MARINO)
    nota(ax, y - 12, "El nombre del método se dice al final, no al principio.")
    return guardar(fig, "s4_sostener-la-respuesta.png")


# ═══════════════════════════════════════ 20 · el problema del planificador
def dos_planos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    _caja(ax, 22, H - 16, 56, 12, MARINO)
    _txt(ax, 50, H - 10, "UN MISMO REQUERIMIENTO DE MADERA", CUERPO - 3, AMBAR, bold=True)
    _txt(ax, 50, H - 21, "aprobado para las dos zonas, sin mirar", CUERPO - 5, GRIS)
    y = H * 0.16
    for x, zona, que in ((5, "ZONA NORTE", "no se usó" + S + "ni un puntal"),
                         (53, "ZONA SUR", "faltó a media guardia:" + S + "dos días parados")):
        _caja(ax, x, y, 42, 24, CLARO)
        _txt(ax, x + 21, y + 17, zona, CUERPO - 3, MARINO, bold=True)
        _txt(ax, x + 21, y + 7.5, que, CUERPO - 5, GRIS)
        ax.annotate("", xy=(x + 21, y + 25.5), xytext=(x + 21, y + 30),
                    arrowprops=dict(arrowstyle="-|>", color=GRIS, lw=2, mutation_scale=14))
    nota(ax, y - 7, "Los dos planos están sobre la mesa. Ninguno dice qué método se aplica.")
    return guardar(fig, "s4_dos-planos.png")


# ═══════════════════════════════════════ 21 y 27 · las fichas de las dos zonas
def las_dos_zonas():
    fig, ax = lienzo(1.10)
    H = 100 / 1.10
    zonas = [
        ("ZONA NORTE",
         "Potencia 20 m  ·  Buzamiento 70°  ·  RMR mineral 55  ·  cajas 65 / 45",
         ["rampa 5,0 × 5,0 pegada a la caja piso  ·  subniveles 5,0 × 4,5 cada 30 m",
          "chimenea de cara libre  ·  tajeos de 30 × 20 × 25 m",
          "galería y crucero por debajo  ·  el hueco entre subniveles está vacío"]),
        ("ZONA SUR",
         "Potencia 1,20 m  ·  Buzamiento 80°  ·  RMR de cajas 45",
         ["cortes horizontales de 3,0 m, uno sobre el otro",
          "chimenea de acceso y servicio  ·  los cortes de abajo, rellenados",
          "galería base al pie de la veta"]),
    ]
    y = H - 12
    for zona, ficha, labores in zonas:
        _caja(ax, 5, y, 90, 9, MARINO)
        _txt(ax, 50, y + 4.5, zona, CUERPO - 3, BLANCO, bold=True)
        yy = y - 7
        _txt(ax, 7, yy, ficha, CUERPO - 5, MARINO, bold=True, ha="left")
        yy -= 6.5
        for d in labores:
            _txt(ax, 7, yy, "·  " + d, CUERPO - 5, GRIS, ha="left")
            yy -= 6.5
        y = yy - 8
    nota(ax, 2.5, "Ninguna de las dos fichas nombra el método. Lo nombran ustedes.")
    return guardar(fig, "s4_las-dos-zonas.png")


# ═══════════════════════════════════════ 22 · la hoja que se marca
def encargo():
    fig, ax = lienzo(1.05)
    H = 100 / 1.05
    indicios = ["el hueco queda vacío",
                "el hueco se rellena después de cada corte",
                "se avanza de abajo hacia arriba en cortes",
                "el mineral se saca por gravedad al nivel de abajo",
                "hace falta chimenea",
                "hacen falta subniveles cada 30 m",
                "las cajas aguantan solas una abertura de 20 m",
                "el ancho de minado se parece a la potencia de la veta",
                "entra equipo mecanizado de gran tamaño",
                "el control es la ley y la dilución corte a corte"]
    nota(ax, H - 4, "Hay indicios que valen para las dos zonas: esos llevan las dos casillas.")
    x0, anchos, alto = 5, [66, 12, 12], 7.4
    y = H - 14
    x = x0
    for w, t in zip(anchos, ["INDICIO", "NORTE", "SUR"]):
        ax.add_patch(Rectangle((x, y), w, alto, facecolor=MARINO, edgecolor=BLANCO, lw=2))
        _txt(ax, x + w / 2, y + alto / 2, t, CUERPO - 5, BLANCO, bold=True)
        x += w
    for i, t in enumerate(indicios):
        y -= alto
        base = CLARO if i % 2 == 0 else BLANCO
        ax.add_patch(Rectangle((x0, y), anchos[0], alto, facecolor=base, edgecolor=BLANCO, lw=2))
        _txt(ax, x0 + 1.6, y + alto / 2, t, CUERPO - 5, MARINO, ha="left")
        for j in (1, 2):
            xc = x0 + sum(anchos[:j])
            ax.add_patch(Rectangle((xc, y), anchos[j], alto, facecolor=base,
                                   edgecolor=BLANCO, lw=2))
            ax.add_patch(Rectangle((xc + anchos[j] / 2 - 2, y + alto / 2 - 2), 4, 4,
                                   facecolor=BLANCO, edgecolor=GRIS, lw=1.4))
    nota(ax, y - 5, "En parejas · 15 minutos · una sola hoja por pareja.")
    return guardar(fig, "s4_encargo.png")


# ═══════════════════════════════════════ 23 · cómo trabajamos
def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean", "las labores de cada" + S + "plano, y su ficha", "4'"),
             ("2", "Marquen", "cada indicio a su zona;" + S + "los de las dos, en las dos", "6'"),
             ("3", "Escriban", "una línea por zona:" + S + "el método y DOS datos", "5'")]
    for i, (n, t, sub, m) in enumerate(pasos):
        x = 5 + i * 32
        col = AZUL if i < 2 else AMBAR
        letra = BLANCO if i < 2 else MARINO
        _caja(ax, x, H * 0.30, 30, 28, col)
        _txt(ax, x + 15, H * 0.30 + 22, n, FUERTE, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 15, t, CUERPO - 3, letra, bold=True)
        _txt(ax, x + 15, H * 0.30 + 7, sub, CUERPO - 6, letra)
        _txt(ax, x + 15, H * 0.30 + 31, m, CUERPO - 5, GRIS, bold=True)
    _txt(ax, 50, H * 0.30 - 11, "Parejas · 15 minutos · una hoja marcada y dos líneas")
    return guardar(fig, "s4_como-trabajamos.png")


# ═══════════════════════════════════════ 26 · la puesta en común
def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["¿Qué labor delató a la zona norte?",
             "¿Qué dato de la ficha lo confirma?",
             "¿Marcaron algún indicio en las dos columnas?",
             "Ese que vale para las dos:" + S + "¿por qué no decide nada?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.4, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             MARINO if i == 4 else BLANCO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 4, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 3, "Al responder: «yo digo… porque…».")
    nota(ax, y - 9, "La cuarta la cierra el instructor: un indicio compartido no prueba nada.")
    return guardar(fig, "s4_puesta-en-comun.png")


# ═══════════════════════════════════════ 28 · el cierre y el puente
def puente():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 4, H - 22, 92, 17, AMBAR)
    _txt(ax, 50, H - 10, "¿Por qué en una zona no se gastó madera y en la otra faltó?",
         CUERPO - 4, MARINO, bold=True)
    _txt(ax, 50, H - 17.5, "la pregunta del planificador · la cierra el instructor",
         CUERPO - 6, MARINO)
    y = H * 0.30
    _caja(ax, 5, y, 40, 22, AZUL)
    _txt(ax, 25, y + 15, "HOY", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 25, y + 7, "qué método se aplica" + S + "y en qué se reconoce", CUERPO - 5, BLANCO)
    _caja(ax, 55, y, 40, 22, MARINO)
    _txt(ax, 75, y + 15, "SESIÓN 5", CUERPO - 3, AMBAR, bold=True)
    _txt(ax, 75, y + 7, "con qué operación sigue" + S + "el frente que dejó otra guardia",
         CUERPO - 5, BLANCO)
    ax.annotate("", xy=(53, y + 11), xytext=(47, y + 11),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    nota(ax, y - 9, "El método ordena las labores. La sesión 5 vuelve al orden de las operaciones.")
    return guardar(fig, "s4_puente.png")


# ═══════════════════════════════════════ armazón de la sesión
def ruta():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    tramos = [("CONEXIÓN", 20, AZUL), ("ADQUISICIÓN", 45, VERDE),
              ("APLICACIÓN", 35, MORADO), ("DISCUSIÓN", 25, AMBAR),
              ("REFLEXIÓN", 10, GRIS)]
    x0, ancho, y, alto = 5, 90, H * 0.42, 13
    x = x0
    for nom, mins, col in tramos:
        w = ancho * mins / 135
        _caja(ax, x, y, w - 0.6, alto, col, r=0.6)
        _txt(ax, x + w / 2, y + alto / 2 + 0.5, "%d'" % mins, CUERPO - 4,
             MARINO if col is AMBAR else BLANCO, bold=True)
        _txt(ax, x + w / 2, y + alto + (6 if mins >= 20 else 13), nom,
             CUERPO - 6, MARINO, bold=True)
        x += w
    _txt(ax, 50, y - 12, "135 minutos. El caso se trabaja en la Aplicación," + S +
         "y las dos zonas se ponen en común en la Discusión.")
    return guardar(fig, "s4_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 3", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "con qué se hace" + S + "cada operación", CUERPO - 3, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 4", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "por qué la labor" + S + "se abre así y no de otra", CUERPO - 3, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "Ya sabemos las cinco operaciones y con qué se hacen." + S +
         "Hoy: qué método las ordena, y en qué se le reconoce.")
    return guardar(fig, "s4_de-donde-venimos.png")


if __name__ == "__main__":
    for f in (de_donde_venimos, ruta, condiciones_de_los_dos, que_pasa_con_el_hueco,
              lo_que_cambia, leer_el_plano, sostener_la_respuesta, dos_planos, las_dos_zonas,
              encargo, como_trabajamos, puesta_en_comun, puente):
        print(" ", f())
