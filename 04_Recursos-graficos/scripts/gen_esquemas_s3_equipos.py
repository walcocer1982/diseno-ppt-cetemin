# -*- coding: utf-8 -*-
"""Esquemas de la sesión 3 · Equipos, materiales y controles por operación.

QUÉ SE DIBUJA AQUÍ Y QUÉ NO
    Lo FÍSICO —un jumbo, un scooptram, un perno— no se dibuja: entra por
    fotografía citada o por silueta hecha del catálogo (§10). Aquí van las
    RELACIONES, que es lo que esta sesión enseña: qué equipo va con qué
    operación, qué separa lo mecanizado de lo convencional, y qué controla el
    técnico en cada paso. Nada de eso tiene cuerpo, así que se tabula.

    Los modelos y capacidades que aparecen —Sandvik DD321, CAT R1600G,
    Penberty GSA HD, barretillas de 4 a 12 pies— salen de la tesis de Raura,
    apartados 2.6 y 2.7. No hay ninguna cifra inventada.

Uso:  python gen_esquemas_s3_equipos.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

from gen_esquemas_s1_yacimiento import (  # noqa: E402
    AMBAR, AZUL, BLANCO, CLARO, CUERPO, F, FUERTE, GRIS, MARINO, MORADO,
    NOTA, PROPORCION, VERDE, guardar, lienzo, nota,
)

ROJO = "#C0392B"


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


# ══════════════════════════════ 10 · el equipo de cada operación
def equipo_por_operacion():
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 4, H - 11, [28, 34, 32], 12,
               ["OPERACIÓN", "EQUIPO", "INSUMO"],
               [["Perforación", "jumbo o jackleg", "barrenos y brocas"],
                ["Voladura", "cargador de ANFO", "emulsión y fanel"],
                ["Carguío", "scooptram", "—"],
                ["Acarreo", "camión de bajo perfil", "—"],
                ["Sostenimiento", "empernador", "pernos y malla"]])
    _txt(ax, 50, y - 9, "Un equipo no hace dos operaciones distintas.\n"
                        "Cambiar de equipo cambia el rendimiento, no la operación.")
    nota(ax, 4, "Modelos reales de la unidad: Sandvik DD321, CAT R1600G, Penberty GSA HD.")
    return guardar(fig, "s3_equipo-por-operacion.png")


# ═══════════════════════ 11 · qué separa lo mecanizado de lo convencional
def mecanizado_convencional():
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 4, H - 11, [26, 34, 34], 12,
               ["", "CONVENCIONAL", "MECANIZADO"],
               [["Quién lo mueve", "la persona", "un motor"],
                ["Perforación", "jackleg con pierna", "jumbo de dos brazos"],
                ["Limpieza", "winche y rastrillo", "scooptram"],
                ["Sección que pide", "poca", "mucha"],
                ["Rendimiento", "bajo", "alto"]])
    _txt(ax, 50, y - 9, "El mecanizado rinde más y exige más sección.\n"
                        "El convencional entra donde el otro no cabe.")
    nota(ax, 4, "La elección no es de gusto: la decide lo que la labor admite.")
    return guardar(fig, "s3_mecanizado-convencional.png")


# ══════════════════════════════ 12 · el control de cada operación
def control_por_operacion():
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 4, H - 11, [28, 38, 28], 12,
               ["OPERACIÓN", "QUÉ CONTROLA EL TÉCNICO", "SI FALLA"],
               [["Perforación", "paralelismo y longitud", "sobrerotura"],
                ["Voladura", "carga y amarre", "tiro fallado"],
                ["Carguío", "que el frente quede limpio", "queda material"],
                ["Acarreo", "el destino del material", "mineral al botadero"],
                ["Sostenimiento", "torque y traslape", "el techo cede"]],
               destacar={(4, 1)})
    _txt(ax, 50, y - 9, "El control es lo que se comprueba antes de seguir.\n"
                        "Sin él, la operación se dio por hecha, no por buena.")
    nota(ax, 4, "Cada control deja un dato que va al reporte de guardia.")
    return guardar(fig, "s3_control-por-operacion.png")


# ═════════════════════ 13 · qué decide si un equipo entra a una labor
def que_admite_la_labor():
    fig, ax = lienzo(1.30)
    H = 100 / 1.30
    filtros = [("SECCIÓN", "¿cabe y puede maniobrar?", AZUL),
               ("ENERGÍA", "¿tiene con qué funcionar?", VERDE),
               ("RECORRIDO", "¿hace falta acarreo aparte?", MORADO)]
    y = H - 20
    for nom, preg, col in filtros:
        _caja(ax, 6, y, 30, 15, col)
        _txt(ax, 21, y + 7.5, nom, CUERPO - 3, BLANCO, bold=True)
        _txt(ax, 40, y + 7.5, preg, CUERPO - 3, MARINO, ha="left")
        y -= 19
    _txt(ax, 50, y - 4, "Las tres se leen en la ficha de la labor,\nantes de pedir nada.")
    nota(ax, 4, "Un equipo que no cabe no es lento: ahí es inservible.")
    return guardar(fig, "s3_que-admite-la-labor.png")


# ═══════════════════════════ 14 · las dos labores del caso, comparadas
def dos_labores():
    fig, ax = lienzo()
    H = 100 / PROPORCION
    y = _tabla(ax, 4, H - 11, [26, 34, 34], 12,
               ["", "RAMPA 340", "GALERÍA 285"],
               [["Sección", "4,00 × 3,50 m", "2,10 × 1,50 m"],
                ["Energía", "tendida al frente", "no hay"],
                ["Ventilación", "manga de 32 pulg", "manga de 12 pulg"],
                ["RMR", "62", "34"],
                ["Al echadero", "80 m", "35 m con rieles"]])
    _txt(ax, 50, y - 9, "Las cinco operaciones son las mismas en las dos.\n"
                        "Lo que cambia es con qué se hacen.")
    nota(ax, 4, "Datos de la ficha de cada labor.")
    return guardar(fig, "s3_dos-labores.png")


# ═══════════════════════════════════ 15 · el desate, en las dos
def desate_en_las_dos():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    _caja(ax, 6, H - 26, 40, 17, CLARO)
    _txt(ax, 26, H - 13, "RAMPA 340", CUERPO - 3, MARINO, bold=True)
    _txt(ax, 26, H - 20, "scaler mecanizado\no barretillas", CUERPO - 4, MARINO)
    _caja(ax, 54, H - 26, 40, 17, CLARO)
    _txt(ax, 74, H - 13, "GALERÍA 285", CUERPO - 3, MARINO, bold=True)
    _txt(ax, 74, H - 20, "barretillas,\nsiempre dos personas", CUERPO - 4, MARINO)
    _caja(ax, 20, H - 50, 60, 16, AMBAR)
    _txt(ax, 50, H - 42, "EL DESATE VA EN LAS DOS", CUERPO - 2, MARINO, bold=True)
    _txt(ax, 50, H - 58, "No es una operación del ciclo: es una condición.\n"
                         "Cambia el equipo, no la obligación.")
    nota(ax, 4, "D.S. 024-2016-EM · Art. 218: dos juegos de cuatro barretillas por labor.")
    return guardar(fig, "s3_desate-en-las-dos.png")


# ══════════════════════════════════════════ armazón de la sesión
def ruta():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    tramos = [("CONEXIÓN", 20, AZUL), ("ADQUISICIÓN", 45, VERDE),
              ("APLICACIÓN", 40, MORADO), ("DISCUSIÓN", 20, AMBAR),
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
    _txt(ax, 50, y - 12, "135 minutos. El caso se trabaja en la Aplicación.")
    return guardar(fig, "s3_ruta.png")


def de_donde_venimos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, CLARO)
    _txt(ax, 23, y + 4, "SESIÓN 2", CUERPO - 3, GRIS, bold=True)
    _txt(ax, 23, y - 4, "qué se hace\ny en qué orden", CUERPO - 3, MARINO)
    _caja(ax, 59, y - 11, 36, 22, AZUL)
    _txt(ax, 77, y + 4, "SESIÓN 3", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 77, y - 4, "con qué se hace\ny qué se controla", CUERPO - 3, BLANCO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "Ya sabemos las cinco y su orden.\nHoy, con qué se hace cada una.")
    return guardar(fig, "s3_de-donde-venimos.png")


def cuadro_encargo():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    anchos = [32, 30, 30]
    y, alto = H - 9, 12
    x = 4
    for w, t in zip(anchos, ["DE LA LISTA", "RAMPA 340", "GALERÍA 285"]):
        ax.add_patch(Rectangle((x, y), w, alto, facecolor=MARINO, edgecolor=BLANCO, lw=2))
        _txt(ax, x + w / 2, y + alto / 2, t, CUERPO - 4, BLANCO, bold=True)
        x += w
    for i in range(4):
        y -= alto
        x = 4
        for w in anchos:
            ax.add_patch(Rectangle((x, y), w, alto, facecolor=BLANCO, edgecolor=GRIS, lw=1.2))
            x += w
    _txt(ax, 50, y - 10, "Se MARCA, no se escribe.\nAl lado de cada marca, el porqué en una palabra.")
    nota(ax, 4, "En parejas · 20 minutos · una sola lista por pareja.")
    return guardar(fig, "s3_cuadro-encargo.png")


def como_trabajamos():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    pasos = [("1", "Lean la ficha", "sección, energía\ny recorrido"),
             ("2", "Marquen", "una columna\npor labor"),
             ("3", "Justifiquen", "una palabra:\npor qué ese")]
    for i, (n, t, sub) in enumerate(pasos):
        x = 5 + i * 32
        _caja(ax, x, H * 0.34, 30, 26, AZUL if i < 2 else AMBAR)
        _txt(ax, x + 15, H * 0.34 + 20, n, FUERTE, BLANCO if i < 2 else MARINO, bold=True)
        _txt(ax, x + 15, H * 0.34 + 13, t, CUERPO - 3, BLANCO if i < 2 else MARINO, bold=True)
        _txt(ax, x + 15, H * 0.34 + 5, sub, CUERPO - 5, BLANCO if i < 2 else MARINO)
    _txt(ax, 50, H * 0.34 - 12, "Parejas · 20 minutos · una lista marcada")
    return guardar(fig, "s3_como-trabajamos.png")


def puesta_en_comun():
    fig, ax = lienzo(1.35)
    H = 100 / 1.35
    pasos = ["Empecemos por la perforación de cada una",
             "¿Qué cambió, el equipo o la operación?",
             "¿Qué dato de la ficha lo decidió?",
             "Hay una fila igual en las dos:\n¿cuál, y por qué?"]
    y, alto = H - 11, 13
    for i, t in enumerate(pasos, 1):
        col = AMBAR if i == 4 else MARINO
        ax.add_patch(Circle((11, y - alto / 2 + 2), 4.2, facecolor=col))
        _txt(ax, 11, y - alto / 2 + 2.3, str(i), CUERPO - 3,
             BLANCO if i < 4 else MARINO, bold=True)
        _txt(ax, 19, y - alto / 2 + 2, t, CUERPO - 4, MARINO, ha="left")
        y -= alto
    _txt(ax, 50, y - 5, "Al responder: «yo digo… porque…».")
    nota(ax, 4, "La cuarta la cierra el instructor: el desate va en toda labor.")
    return guardar(fig, "s3_puesta-en-comun.png")


def puente():
    fig, ax = lienzo(1.70)
    H = 100 / 1.70
    y = H * 0.52
    _caja(ax, 5, y - 11, 36, 22, AZUL)
    _txt(ax, 23, y + 4, "HOY", CUERPO - 3, BLANCO, bold=True)
    _txt(ax, 23, y - 4, "con qué se hace\ncada operación", CUERPO - 3, BLANCO)
    _caja(ax, 59, y - 11, 36, 22, AMBAR)
    _txt(ax, 77, y + 4, "SESIÓN 4", CUERPO - 3, MARINO, bold=True)
    _txt(ax, 77, y - 4, "qué método se aplica\ny por qué ese", CUERPO - 3, MARINO)
    ax.annotate("", xy=(57, y), xytext=(43, y),
                arrowprops=dict(arrowstyle="-|>", color=MARINO, lw=2.4, mutation_scale=20))
    _txt(ax, 50, y - 20, "El TC1 pedirá las dos cosas juntas:\nla operación y el equipo que le toca.")
    return guardar(fig, "s3_puente.png")


if __name__ == "__main__":
    for f in (equipo_por_operacion, mecanizado_convencional, control_por_operacion,
              que_admite_la_labor, dos_labores, desate_en_las_dos, ruta,
              de_donde_venimos, cuadro_encargo, como_trabajamos, puesta_en_comun, puente):
        print(" ", f())
