# -*- coding: utf-8 -*-
"""Kit para dibujar los esquemas de las láminas. Común a las tres carreras.

POR QUÉ EXISTE
    El texto dentro de una imagen se reduce cuando la imagen entra en la lámina.
    Lo que decide si se lee no es el tamaño en píxeles sino la RAZÓN entre la
    fuente y el ancho del lienzo:

        pt_proyectado = 6 * px_fuente / px_ancho_lienzo * 72

    Con W = 1500 y cuerpo de 52 px salen 15 pt. Con 24 px sobre 1841 salían 5,6.

CÓMO SE USA
    from esquemas import *

    im, d = lienzo(1200)
    filas_letra(d, [("S", "SEGURIDAD", "Protege del accidente", AZUL2), ...])
    guardar(im, "ssomac_cuatro-letras.png", DEST)

REGLAS
    · un esquema, una idea. Más de 6 bloques o más de 4 líneas por bloque = dos esquemas
    · sin título: el título lo pone la lámina
    · si es estímulo de una rutina, muestra HECHOS y ningún juicio
    · los colores salen de la paleta de abajo, siempre

Requiere Pillow:  python -m pip install pillow
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageChops

# ── el lienzo y los tamaños ───────────────────────────────────────────────
W = 1500                     # ancho fijo: de aquí salen los pt proyectados
TIT, CUE, NOTA = 62, 52, 42  # 17,9 · 15,0 · 12,1 pt

# ── la paleta (§11). Usar siempre estos ───────────────────────────────────
AZUL   = (13, 38, 50)        # #0D2632  texto, cabeceras, bloques de énfasis
AZUL2  = (22, 127, 185)      # #167FB9  primera categoría
TEAL   = (0, 178, 156)       # #00B29C  segunda
MORADO = (80, 82, 169)       # #5052A9  tercera
AMBAR  = (255, 197, 5)       # #FFC505  lo que hay que destacar (texto AZUL encima)
GRIS   = (108, 122, 130)     # #6C7A82  texto secundario
GRISC  = (238, 241, 243)     # #EEF1F3  fondo de bloque
BLANCO = (255, 255, 255)
ROJO   = (192, 57, 43)       # #C0392B  solo lo que está mal. Con moderación

FUENTES = r"C:\Windows\Fonts"   # Arial: es la única instalada en los equipos


# ── utilidades ────────────────────────────────────────────────────────────
def fu(px, bold=False):
    return ImageFont.truetype(os.path.join(FUENTES, "arialbd.ttf" if bold else "arial.ttf"), px)


def an(d, t, f):
    a = d.textbbox((0, 0), t, font=f)
    return a[2] - a[0]


PX_MIN = 44                  # 12,7 pt proyectados: por debajo no se lee al proyectar
AVISOS = []                  # lo que no cupo en su caja. `guardar` lo canta


def _cabe(d, t, f, w):
    return an(d, t, f) <= w


def cen(d, x, y, w, t, px, color, bold=True, margen=30, alto=None):
    """Centra el texto. Si no cabe: baja de punto hasta PX_MIN y despues ENVUELVE.

    Antes bajaba hasta 26 px —7,5 pt proyectados—, que no se lee. Y lo que seguia
    sin caber salia cortado. Ahora ninguna de las dos cosas.
    """
    util = w - margen
    f = fu(px, bold)
    while not _cabe(d, t, f, util) and px > PX_MIN:
        px -= 2
        f = fu(px, bold)
    if _cabe(d, t, f, util):
        d.text((x + (w - an(d, t, f)) / 2, y), t, font=f, fill=color)
        return y + px * 1.25
    lineas = envolver(d, t, px, util, bold)
    if alto and len(lineas) * px * 1.25 > alto:
        AVISOS.append("«%s…» no cabe en su caja ni envuelto" % t[:44])
    for i, l in enumerate(lineas):
        fl = fu(px, bold)
        d.text((x + (w - an(d, l, fl)) / 2, y + i * px * 1.25), l, font=fl, fill=color)
    return y + len(lineas) * px * 1.25


def izq(d, x, y, t, px, color, bold=False, ancho=None):
    """Texto a la izquierda. Con `ancho`, ENVUELVE en vez de salirse de la caja.

    Sin `ancho` se comporta como antes — pero entonces nadie garantiza que quepa,
    y por eso `filas_letra` y `tabla` ahora siempre lo pasan.
    """
    f = fu(px, bold)
    if ancho is None or _cabe(d, t, f, ancho):
        d.text((x, y), t, font=f, fill=color)
        return y + px * 1.25
    px2 = px
    while px2 > PX_MIN and not _cabe(d, t, fu(px2, bold), ancho):
        px2 -= 2
    lineas = envolver(d, t, px2, ancho, bold)
    for i, l in enumerate(lineas):
        d.text((x, y + i * px2 * 1.25), l, font=fu(px2, bold), fill=color)
    return y + len(lineas) * px2 * 1.25


def envolver(d, t, px, ancho, bold=False):
    """Parte el texto en lineas que caben en `ancho`.

    OJO con `bold`: la negrita es mas ancha. Midiendo en redonda un texto que luego se
    dibuja en negrita, la linea se pasa y se corta. Le paso el mismo peso con el que se
    va a dibujar.
    """
    f, lineas, act = fu(px, bold), [], ""
    for p in t.split():
        s = (act + " " + p).strip()
        if an(d, s, f) <= ancho:
            act = s
        else:
            lineas.append(act); act = p
    if act:
        lineas.append(act)
    return lineas


def lienzo(alto):
    im = Image.new("RGB", (W, alto), BLANCO)
    return im, ImageDraw.Draw(im)


def guardar(im, nombre, destino):
    """Recorta el aire sobrante y guarda. Sin recorte el esquema se dibuja
    más pequeño de lo que cabe, porque el hueco se llena por proporción."""
    caja = ImageChops.difference(im, Image.new("RGB", im.size, BLANCO)).getbbox()
    if caja:
        m = 24
        im = im.crop((max(0, caja[0] - m), max(0, caja[1] - m),
                      min(im.width, caja[2] + m), min(im.height, caja[3] + m)))
    os.makedirs(destino, exist_ok=True)
    im.save(os.path.join(destino, nombre), "PNG")
    print("   %-42s %sx%s · cuerpo %.1f pt" % (nombre, im.width, im.height,
                                               6.0 * CUE / im.width * 72))
    # El numero no ve el borde: un esquema puede medir 15 pt y tener una linea
    # cortada. Lo que no cupo se canta aqui, y la lista se vacia para el siguiente.
    for a in AVISOS:
        print("      !! %s" % a)
    del AVISOS[:]
    return im


def banda(d, y, alto, texto, px=NOTA, fondo=GRISC, tinta=AZUL):
    """Franja de cierre con la idea que hay que llevarse."""
    d.rounded_rectangle([50, y, W - 50, y + alto], 18, fill=fondo)
    cen(d, 50, y + (alto - px) / 2 - 6, W - 100, texto, px, tinta)


# ── las siete formas que ya funcionan ──────────────────────────────────────
def filas_letra(d, filas, y=60, alto=280, sep=30):
    """(letra, NOMBRE, detalle, color) — para siglas: SSOMAC, PHVA…"""
    for letra, nombre, det, col in filas:
        d.rounded_rectangle([50, y, W - 50, y + alto], 20, fill=GRISC)
        d.rounded_rectangle([50, y, 300, y + alto], 20, fill=col)
        d.rectangle([260, y, 300, y + alto], fill=col)
        cen(d, 50, y + alto / 2 - 58, 250, letra, 92, AZUL if col == AMBAR else BLANCO)
        # el ancho util es hasta el margen derecho: sin pasarlo, el detalle se cortaba
        util = W - 50 - 350 - 40
        izq(d, 350, y + 62, nombre, TIT, AZUL, True, ancho=util)
        izq(d, 350, y + 155, det, CUE, GRIS, ancho=util)
        y += alto + sep
    return y


def tabla(d, encabezados, filas, cortes, y=60):
    """Comparar por columnas. filas = [([col1...], [col2...], destacado, fondo, tinta)]"""
    x = cortes
    d.rectangle([x[0], y, x[-1], y + 100], fill=AZUL)
    # Los encabezados se miden ANTES de dibujarlos y bajan de punto JUNTOS. Midiendo cada
    # uno por su lado, el que no cabia se envolvia y la segunda linea salia de la banda.
    px = 48
    while px > PX_MIN and any(not _cabe(d, e, fu(px, True), x[i + 1] - x[i] - 30)
                              for i, e in enumerate(encabezados)):
        px -= 2
    for i, e in enumerate(encabezados):
        if not _cabe(d, e, fu(px, True), x[i + 1] - x[i] - 30):
            AVISOS.append("el encabezado «%s» no cabe en su columna ni a %d px" % (e, px))
        cen(d, x[i], y + (100 - px) / 2 - 6, x[i + 1] - x[i], e, px, BLANCO)
    y += 100
    for celdas, destacado, fondo, tinta in filas:
        # una celda larga se envuelve: la fila tiene que crecer con ella
        lineas = max(len(envolver(d, c, CUE, x[j + 1] - x[j] - 64))
                     for j, col in enumerate(celdas) for c in col)
        alto = 60 + max(len(c) for c in celdas) * 66 + (lineas - 1) * 66
        d.rectangle([x[0], y, x[-1], y + alto], fill=BLANCO, outline=(214, 220, 224), width=3)
        if destacado:
            d.rectangle([x[-2] + 14, y + 20, x[-1] - 14, y + alto - 20], fill=fondo)
        for j, col in enumerate(celdas):
            # el ancho de ESA columna, menos los margenes: antes se salia a la de al lado
            util = x[j + 1] - x[j] - 64
            for i, t in enumerate(col):
                izq(d, x[j] + 32, y + (alto - len(col) * 64) / 2 + i * 64, t, CUE, AZUL, ancho=util)
        if destacado:
            cen(d, x[-2], y + alto / 2 - 26, x[-1] - x[-2], destacado, 46, tinta)
        y += alto
    return y


def ciclo(d, cuadrantes, cx, cy, R=560, r=310, centro=None, lista=()):
    """Anillo de cuatro cuadrantes. cuadrantes = [(letra, NOMBRE, ang0, ang1, color)]"""
    for _, _, a0, a1, col in cuadrantes:
        d.pieslice([cx - R, cy - R, cx + R, cy + R], a0 + 3, a1 - 3, fill=col)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANCO)
    for letra, nombre, a0, a1, col in cuadrantes:
        ang = math.radians((a0 + a1) / 2)
        px, py = cx + (R + r) / 2 * math.cos(ang), cy + (R + r) / 2 * math.sin(ang)
        tinta = AZUL if col == AMBAR else BLANCO
        f = fu(84, True); d.text((px - an(d, letra, f) / 2, py - 76), letra, font=f, fill=tinta)
        f = fu(40, True); d.text((px - an(d, nombre, f) / 2, py + 24), nombre, font=f, fill=tinta)
    if centro:
        cen(d, cx - r, cy - 96, 2 * r, centro, 52, AZUL)
        d.line([cx - 130, cy - 24, cx + 130, cy - 24], fill=AMBAR, width=8)
    for i, t in enumerate(lista):
        cen(d, cx - r, cy + 4 + i * 62, 2 * r, t, 46, GRIS, False)


def franjas(d, bloques, im, y=60, alto=330):
    """Niveles apilados. bloques = [(NOMBRE, [cajas], color)]"""
    # La caja blanca medía `alto - 110` fijo y `cen` envuelve por su cuenta: un texto
    # de tres lineas se salia por debajo del blanco y se leia sobre el gris, o se
    # cortaba contra la banda siguiente. Ningun aviso lo cazaba porque el texto SI
    # cabia en su ancho — lo que no cabia era la caja en su banda. Se mide antes.
    faltan = 0
    for _n, cajas, _c in bloques:
        an_caja = (W - 300) / len(cajas) - 26
        for tx in cajas:
            faltan = max(faltan, len(envolver(d, tx, CUE, an_caja - 60)))
    alto = max(alto, 110 + faltan * int(CUE * 1.25) + 46)
    for nombre, cajas, col in bloques:
        d.rounded_rectangle([50, y, W - 50, y + alto], 18, fill=GRISC)
        d.rounded_rectangle([50, y, 190, y + alto], 18, fill=col)
        d.rectangle([150, y, 190, y + alto], fill=col)
        # La etiqueta vertical se dibujaba a 46 px en una banda de 110: una etiqueta
        # de dos palabras se envolvia y la SEGUNDA LINEA CAIA FUERA, cortada y sin
        # aviso. Ahora baja de punto para caber en una linea, admite dos, y canta si
        # ni asi entra.
        ALTO_ETQ, util_etq = 130, alto - 60
        px_etq = 46
        lineas = envolver(d, nombre, px_etq, util_etq, True)
        while len(lineas) > 1 and px_etq > PX_MIN:
            px_etq -= 2
            lineas = envolver(d, nombre, px_etq, util_etq, True)
        # Y AHORA EL LARGO. `envolver` parte por palabras: una palabra sola mas ancha
        # que la banda no se puede partir y salia entera, pisando los bordes por los
        # dos lados. Pasaba con «ME PREGUNTO», donde «PREGUNTO» no cabe en la franja.
        # El alto se comprobaba y el ancho no, asi que no habia aviso: solo se veia.
        while px_etq > PX_MIN and max(an(d, l, fu(px_etq, True)) for l in lineas) > util_etq:
            px_etq -= 2
            lineas = envolver(d, nombre, px_etq, util_etq, True)
        if max(an(d, l, fu(px_etq, True)) for l in lineas) > util_etq:
            AVISOS.append("la etiqueta «%s» es mas larga que su banda incluso a %d px"
                          % (nombre, px_etq))
        if len(lineas) * px_etq * 1.25 > ALTO_ETQ:
            AVISOS.append("la etiqueta «%s» no cabe en su banda ni a %d px" % (nombre, px_etq))
        tx = Image.new("RGB", (alto, ALTO_ETQ), col)
        dt = ImageDraw.Draw(tx)
        y_etq = (ALTO_ETQ - len(lineas) * px_etq * 1.25) / 2
        for i, l in enumerate(lineas):
            fe = fu(px_etq, True)
            dt.text(((alto - an(dt, l, fe)) / 2, y_etq + i * px_etq * 1.25), l, font=fe, fill=BLANCO)
        im.paste(tx.rotate(90, expand=True), (52, y))
        x, ancho = 240, (W - 300) / len(cajas) - 26
        for c in cajas:
            d.rounded_rectangle([x, y + 55, x + ancho, y + alto - 55], 14, fill=BLANCO)
            cen(d, x, y + alto / 2 - 26, ancho, c, CUE, AZUL, False)
            x += ancho + 26
        y += alto + 30
    return y


def comparativa(d, izquierda, derecha, filas, y=50):
    """Antes / después, sin / con. filas = [([izq...], [der...])]"""
    mid = W / 2
    d.rounded_rectangle([50, y, mid - 20, y + 100], 14, fill=ROJO)
    d.rounded_rectangle([mid + 20, y, W - 50, y + 100], 14, fill=TEAL)
    cen(d, 50, y + 24, mid - 70, izquierda, 52, BLANCO)
    cen(d, mid + 20, y + 24, mid - 70, derecha, 52, BLANCO)
    y += 135
    for a, b in filas:
        alto = 40 + max(len(a), len(b)) * 62
        d.rounded_rectangle([50, y, mid - 20, y + alto], 14, fill=GRISC)
        d.rounded_rectangle([mid + 20, y, W - 50, y + alto], 14, fill=(226, 245, 241))
        for i, t in enumerate(a):
            cen(d, 50, y + 20 + i * 62, mid - 70, t, CUE, GRIS, False)
        for i, t in enumerate(b):
            cen(d, mid + 20, y + 20 + i * 62, mid - 70, t, CUE, AZUL, False)
        y += alto + 22
    return y


def caso(d, empresa, ficha, hechos, color=AZUL2, y=60, alto=250, cols=2):
    """La ficha de un caso de sesion: cabecera con la empresa, y los hechos en cajas.

    empresa = "CASO A"   ficha = "Planificacion, recursos y documentacion del SGC"
    hechos  = [texto, ...]  — uno por caja, se envuelven solos

    DOS COLUMNAS por defecto. A una sola, seis parrafos dan una imagen mas alta que ancha,
    y al encajarla en una lamina apaisada el cuerpo se proyecta a 9 pt. Con dos, a 22 pt.
    """
    # la cabecera CRECE con su texto: con una ficha larga, la banda fija de 190 px
    # la cortaba por la mitad y el nombre de la empresa se salia de la caja
    lf = envolver(d, ficha, NOTA, W - 180, bold=True)
    alto_cab = 120 + len(lf) * int(NOTA * 1.3)
    d.rounded_rectangle([50, y, W - 50, y + alto_cab], 18, fill=color)
    cen(d, 50, y + 30, W - 100, empresa, TIT, BLANCO)
    for i, l in enumerate(lf):
        cen(d, 50, y + 112 + i * int(NOTA * 1.3), W - 100, l, NOTA, BLANCO)
    y0 = y + alto_cab + 30

    ancho = (W - 100 - 30 * (cols - 1)) / cols
    util = ancho - 90
    filas = -(-len(hechos) // cols)
    altos = []
    for h in hechos:
        altos.append(max(alto, 70 + len(envolver(d, h, CUE, util)) * 66))
    # todas las cajas de una misma fila comparten alto: si no, la rejilla queda coja
    por_fila = [max(altos[i * cols:(i + 1) * cols] or [alto]) for i in range(filas)]

    for k, h in enumerate(hechos):
        col, fil = k % cols, k // cols
        x = 50 + col * (ancho + 30)
        yy = y0 + sum(por_fila[:fil]) + fil * 24
        caja = por_fila[fil]
        d.rounded_rectangle([x, yy, x + ancho, yy + caja], 16, fill=GRISC)
        d.rounded_rectangle([x, yy, x + 24, yy + caja], 16, fill=color)
        d.rectangle([x + 12, yy, x + 24, yy + caja], fill=color)
        lineas = envolver(d, h, CUE, util)
        for i, l in enumerate(lineas):
            izq(d, x + 60, yy + (caja - len(lineas) * 66) / 2 + i * 66, l, CUE, AZUL)
    return y0 + sum(por_fila) + (filas - 1) * 24


def fichas(d, items, y=50, alto=300, cols=2, pie=None):
    """Elementos numerados a clasificar. items = [texto, ...]

    OJO: el texto se envuelve solo y el salto de linea se trata como un espacio. Poner
    "ROTULO
detalle" NO da dos bloques: da "ROTULO detalle" corrido. Para rotulo y
    detalle separados, usa `tabla` de dos columnas.
    """
    ancho = (W - 100 - 40 * (cols - 1)) / cols
    for i, t in enumerate(items):
        x = 50 + (i % cols) * (ancho + 40)
        yy = y + (i // cols) * (alto + 34)
        d.rounded_rectangle([x, yy, x + ancho, yy + alto], 16, fill=GRISC)
        d.rounded_rectangle([x, yy, x + ancho, yy + 12], 16, fill=AZUL2)
        cen(d, x, yy + 40, ancho, str(i + 1), 54, AZUL2)
        cen(d, x, yy + 130, ancho, t, CUE, AZUL, False)
        if pie:
            _w = an(d, pie, fu(40, False)) / 2 + 26
            d.rounded_rectangle([x + ancho / 2 - _w, yy + alto - 84,
                                 x + ancho / 2 + _w, yy + alto - 32], 10, outline=GRIS, width=3)
            cen(d, x, yy + alto - 72, ancho, pie, 40, GRIS, False)
    return y + ((len(items) + cols - 1) // cols) * (alto + 34)


# ── fotografía: lo que el esquema no puede enseñar ────────────────────────
def _cubrir(ruta, w, h):
    """Escala la foto para llenar la caja y recorta el sobrante por el centro.

    Cubrir y no encajar: una foto con banda blanca a los lados delata el montaje.
    Y nunca se deforma — el §10 permite retocar, no estirar."""
    f = Image.open(ruta).convert("RGB")
    k = max(w / f.width, h / f.height)
    f = f.resize((max(1, int(f.width * k)), max(1, int(f.height * k))), Image.LANCZOS)
    x0, y0 = (f.width - w) // 2, (f.height - h) // 2
    return f.crop((x0, y0, x0 + w, y0 + h))


def foto(im, d, ruta, x, y, w, h, etiqueta=None, radio=16):
    """Pega una fotografía en la caja, con esquinas redondeadas como el resto del kit.

    `etiqueta` es una pastilla ámbar apoyada abajo a la izquierda: dice QUÉ se está
    mirando. Sin ella el alumno ve una foto bonita y no sabe dónde poner el ojo."""
    f = _cubrir(ruta, int(w), int(h))
    mask = Image.new("L", f.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, f.width - 1, f.height - 1], radio, fill=255)
    im.paste(f, (int(x), int(y)), mask)
    if etiqueta:
        px = NOTA
        fu_ = fu(px, True)
        ancho = an(d, etiqueta, fu_) + 30
        # si el rótulo no cabe en la foto, baja de punto antes que salirse
        while ancho > w - 24 and px > PX_MIN:
            px -= 2
            fu_ = fu(px, True)
            ancho = an(d, etiqueta, fu_) + 30
        if ancho > w - 24:
            AVISOS.append("la etiqueta «%s» no cabe sobre su foto" % etiqueta)
        ey = y + h - px - 34
        d.rounded_rectangle([x + 14, ey, x + 14 + ancho, ey + px + 20], 8, fill=AMBAR)
        d.text((x + 29, ey + 8), etiqueta, font=fu_, fill=AZUL)
    return y + h


def credito(d, y, texto):
    """La atribución de las fotos, al pie. Se envuelve: nunca se corta una fuente."""
    for i, ln in enumerate(envolver(d, texto, 34, W - 100)):
        izq(d, 50, y + i * 44, ln, 34, GRIS)
    return y + len(envolver(d, texto, 34, W - 100)) * 44


def cadena(im, d, eslabones, y=60, alto=520):
    """A → B → C con flechas. eslabones = [(RÓTULO, color, texto, foto|None)]

    La forma tiene que decir lo que enseña: tres bandas apiladas dicen «tres cosas»;
    una cadena con flechas dice «una causa a la otra», que es el punto de la lámina.
    El cuarto elemento de cada eslabón puede ser: la ruta de una fotografía, un TEXTO
    —que se dibuja en un recuadro ámbar, para el eslabón que no se puede fotografiar
    y hay que saber nombrar— o None, que no dibuja nada.

    Antes, None dibujaba el recuadro ámbar con un texto fijo. Una cadena de tres
    eslabones sin foto salia con el mismo cartel repetido tres veces, diciendo algo
    que solo tenia sentido en una lamina."""
    n = len(eslabones)
    flecha = 78
    ancho = (W - 100 - flecha * (n - 1)) / n
    # El pie se mide ANTES de repartir el alto. Antes se le daban 150 px fijos y el
    # eslabon de texto mas largo se salia de su tarjeta sin que ningun numero lo
    # cazara: la figura se guardaba con la ultima linea por fuera del gris.
    lineas = max(len(envolver(d, e[2], CUE, ancho - 60, False)) for e in eslabones)
    pie = int(lineas * CUE * 1.18) + 46
    alto = max(alto, 86 + 200 + pie)
    x = 50
    for i, (rotulo, col, texto, ruta) in enumerate(eslabones):
        d.rounded_rectangle([x, y, x + ancho, y + alto], 18, fill=GRISC)
        d.rounded_rectangle([x, y, x + ancho, y + 86], 18, fill=col)
        d.rectangle([x, y + 60, x + ancho, y + 86], fill=col)
        cen(d, x, y + 20, ancho, rotulo, 44, BLANCO)
        caja_y, caja_h = y + 104, alto - 104 - pie
        if ruta and str(ruta).lower().endswith((".png", ".jpg", ".jpeg")):
            foto(im, d, ruta, x + 18, caja_y, ancho - 36, caja_h)
        elif ruta:
            d.rounded_rectangle([x + 18, caja_y, x + ancho - 18, caja_y + caja_h], 14, fill=AMBAR)
            cen(d, x + 18, caja_y + caja_h / 2 - 34, ancho - 36, str(ruta), 38, AZUL, False)
        cen(d, x, y + alto - pie + 16, ancho, texto, CUE, AZUL, False)
        if i < n - 1:
            cx, cy = x + ancho + flecha / 2, y + alto / 2
            d.polygon([(cx - 26, cy - 30), (cx + 26, cy), (cx - 26, cy + 30)], fill=AZUL2)
        x += ancho + flecha
    return y + alto


def fichas_foto(im, d, items, y=50, alto=470, cols=2, pie=None):
    """Las fichas de siempre, con fotografía. items = [(texto, ruta), ...]

    Es la forma del ejercicio: el alumno mira la actividad y decide. Leer cuatro
    frases y mirar cuatro fotos no es el mismo ejercicio."""
    ancho = (W - 100 - 40 * (cols - 1)) / cols
    # El pie iba a una altura fija y un rotulo de dos lineas se le montaba encima.
    # Se mide el rotulo mas largo y la tarjeta crece: el recuadro nunca pisa texto.
    lineas = max(len(envolver(d, x[0], CUE, ancho - 60, False)) for x in items)
    alto_txt = int(lineas * CUE * 1.18) + 24
    alto_pie = 76 if pie else 0
    alto_foto = alto - alto_txt - alto_pie - 46
    if alto_foto < 200:
        alto_foto = 200
        alto = alto_foto + alto_txt + alto_pie + 46
    for i, (t, ruta) in enumerate(items):
        x = 50 + (i % cols) * (ancho + 40)
        yy = y + (i // cols) * (alto + 34)
        d.rounded_rectangle([x, yy, x + ancho, yy + alto], 16, fill=GRISC)
        foto(im, d, ruta, x + 16, yy + 16, ancho - 32, alto_foto)
        d.ellipse([x + 30, yy + 30, x + 96, yy + 96], fill=AZUL2)
        cen(d, x + 30, yy + 44, 66, str(i + 1), 42, BLANCO)
        cen(d, x, yy + alto_foto + 34, ancho, t, CUE, AZUL, False)
        if pie:
            py = yy + alto_foto + 30 + alto_txt
            _w = an(d, pie, fu(40, False)) / 2 + 26
            d.rounded_rectangle([x + ancho / 2 - _w, py, x + ancho / 2 + _w, py + 52],
                                10, outline=GRIS, width=3)
            cen(d, x, py + 10, ancho, pie, 40, GRIS, False)
    return y + ((len(items) + cols - 1) // cols) * (alto + 34)


# ── el momento de aplicación: la hoja y el relato ─────────────────────────
def hoja(d, encabezados, filas, y=60, alto_fila=190, muestra=0):
    """La tabla que el equipo va a entregar, vacía y con sus encabezados.

    Sustituye a la lista de pasos. Un paso escrito en una banda dice QUÉ HACER; la
    columna de una tabla dice ADEMÁS DÓNDE VA LO QUE HAGAS, que es lo que un equipo
    con veintiocho minutos necesita saber.

    `muestra` = cuántas filas del principio llevan texto de ejemplo. Las demás van en
    blanco: el formato se enseña, la respuesta no.
    """
    n = len(encabezados)
    ancho = (W - 100) / n
    # Los encabezados bajan de punto JUNTOS, como en `tabla`: si cada uno busca su
    # tamaño, la cabecera queda con cuatro tipografías distintas.
    px = 40
    while px > PX_MIN - 8 and any(not _cabe(d, e, fu(px, True), ancho - 24) for e in encabezados):
        px -= 2
    # Se envuelve UNA vez. Antes se partia aqui a `ancho - 24` y `cen` volvia a partir
    # a `ancho - margen`: la segunda linea de cen caia sobre la tercera mia y el
    # encabezado salia con las palabras superpuestas. Ahora cen envuelve y yo mido
    # con SU mismo util, que es lo unico que garantiza que los dos cuenten igual.
    MARGEN = 26
    alto_cab = 40 + max(len(envolver(d, e, px, ancho - MARGEN, True))
                        for e in encabezados) * int(px * 1.25)
    d.rounded_rectangle([50, y, W - 50, y + alto_cab], 14, fill=AZUL)
    for i, e in enumerate(encabezados):
        cen(d, 50 + i * ancho, y + 20, ancho, e, px, BLANCO, True,
            margen=MARGEN, alto=alto_cab - 30)
    y += alto_cab + 12

    for f in range(len(filas)):
        celdas = filas[f]
        alto = alto_fila
        if f < muestra:
            alto = max(alto_fila, 50 + max(len(envolver(d, c, NOTA, ancho - 56)) for c in celdas) * 52)
        for i in range(n):
            x = 50 + i * ancho
            d.rounded_rectangle([x + 6, y, x + ancho - 6, y + alto], 12,
                                fill=GRISC if f < muestra else BLANCO,
                                outline=(206, 214, 219), width=3)
            if f < muestra and celdas[i]:
                cen(d, x + 6, y + 26, ancho - 12, celdas[i], NOTA, GRIS, False, margen=22)
        y += alto + 12
    return y


def relato(d, empresa, ficha, bloques, color=AZUL2, y=60, px=42):
    """La ficha de un caso: los bloques EN COLUMNA, uno al lado del otro.

    bloques = [(TÍTULO, [hecho, ...]), ...]

    DOS DECISIONES, y las dos vienen de medir:

    1. `caso` pone los hechos en cajas iguales y el relato se pierde: el hecho que
       abre la historia pesa lo mismo que el que la cierra. Aquí van agrupados bajo
       tres títulos —lo que la planta hace, lo que ya pasó, lo que la empresa hizo—
       y el orden de lectura sale solo, sin marcar nada.

    2. VAN EN COLUMNAS, no apilados. La lámina de caso da un hueco de 12,10 x 5,75
       pulgadas: apaisado. Una ficha apilada sale con proporción 0,7 y al encajarla
       se queda en un tercio del ancho de la diapositiva, con dos palmos de vacío a
       cada lado. En columnas la proporción se acerca a 2 y llena el hueco.

    NO lleva banda de cierre a propósito. Rematar con la frase que junta la trampa
    —«la cisterna es lo primero que enseña; la faja sigue descubierta»— entrega hecha
    la contradicción que el equipo tiene que encontrar (§12, regla 4).
    """
    lf = envolver(d, ficha, NOTA, W - 180, bold=True)
    alto_cab = 120 + len(lf) * int(NOTA * 1.3)
    d.rounded_rectangle([50, y, W - 50, y + alto_cab], 18, fill=color)
    cen(d, 50, y + 30, W - 100, empresa, TIT, BLANCO)
    for i, l in enumerate(lf):
        cen(d, 50, y + 112 + i * int(NOTA * 1.3), W - 100, l, NOTA, BLANCO)
    y0 = y + alto_cab + 26

    n = len(bloques)
    ancho = (W - 100 - 26 * (n - 1)) / n
    util = ancho - 76
    # Todas las columnas acaban a la misma altura: la mas larga manda. Si cada una
    # termina donde quiere, la ficha queda dentada por abajo.
    # La banda del titulo CRECE con el titulo, y todas las columnas comparten su alto.
    # Con banda fija de 62 px, «LO QUE LA EMPRESA HIZO» se envolvia y la segunda linea
    # caia fuera del color, en blanco sobre gris: ilegible y sin aviso.
    alto_tit = 22 + max(len(envolver(d, tt, 36, ancho - 40, True))
                        for tt, _ in bloques) * int(36 * 1.3)
    altos = []
    for _, hechos in bloques:
        h = alto_tit + 22
        for x in hechos:
            h += 44 + len(envolver(d, x, px, util)) * int(px * 1.3)
        altos.append(h)
    alto_col = max(altos)

    for i, (titulo, hechos) in enumerate(bloques):
        x = 50 + i * (ancho + 26)
        d.rounded_rectangle([x, y0, x + ancho, y0 + alto_col], 14, fill=GRISC)
        d.rounded_rectangle([x, y0, x + ancho, y0 + alto_tit], 14, fill=color)
        d.rectangle([x, y0 + alto_tit - 22, x + ancho, y0 + alto_tit], fill=color)
        cen(d, x, y0 + 11, ancho, titulo, 36, BLANCO, True, margen=40, alto=alto_tit - 16)
        yy = y0 + alto_tit + 22
        for h in hechos:
            ls = envolver(d, h, px, util, False)
            alto_h = len(ls) * int(px * 1.3) + 30
            d.rounded_rectangle([x + 16, yy, x + ancho - 16, yy + alto_h], 10, fill=BLANCO)
            for k, l in enumerate(ls):
                izq(d, x + 42, yy + 15 + k * int(px * 1.3), l, px, AZUL)
            yy += alto_h + 14
    return y0 + alto_col


def narracion(d, empresa, ficha, parrafos, color=AZUL2, y=60, px=44, cols=2, ancho_total=None):
    """El caso en prosa, a dos columnas. parrafos = [texto, ...]

    Devuelve el borde inferior. Ver el módulo `kit_narracion` para el porqué:
    un relato troceado en cajas deja de leerse como relato.
    """
    AN = ancho_total or W
    lf = envolver(d, ficha, NOTA, AN - 180, bold=True)
    alto_cab = 118 + len(lf) * int(NOTA * 1.3)
    d.rounded_rectangle([50, y, AN - 50, y + alto_cab], 18, fill=color)
    cen(d, 50, y + 28, AN - 100, empresa, TIT, BLANCO)
    for i, l in enumerate(lf):
        cen(d, 50, y + 110 + i * int(NOTA * 1.3), AN - 100, l, NOTA, BLANCO)
    y0 = y + alto_cab + 34

    ancho = (AN - 100 - 60 * (cols - 1)) / cols
    util = ancho - 56
    interlinea = int(px * 1.32)
    hueco = int(px * 0.72)          # aire entre parrafos: menos que una linea entera

    # Cada parrafo se mide entero y se reparte SIN CORTARLO. El reparto busca que las
    # columnas queden parejas: se va llenando y se salta de columna cuando lo que
    # queda del parrafo cabe mejor en la siguiente.
    bloques = [envolver(d, p, px, util) for p in parrafos]
    total = sum(len(b) for b in bloques) + len(bloques) - 1
    objetivo = -(-total // cols)

    columnas, actual, alto_act = [], [], 0
    for b in bloques:
        if actual and alto_act + len(b) > objetivo and len(columnas) < cols - 1:
            columnas.append(actual)
            actual, alto_act = [], 0
        actual.append(b)
        alto_act += len(b) + 1
    columnas.append(actual)
    while len(columnas) < cols:
        columnas.append([])

    alto_col = max(sum(len(b) for b in c) * interlinea + max(0, len(c) - 1) * hueco
                   for c in columnas)
    d.rounded_rectangle([40, y0 - 18, AN - 40, y0 + alto_col + 22], 16, fill=GRISC)
    for i, c in enumerate(columnas):
        x = 50 + i * (ancho + 60)
        yy = y0
        for b in c:
            for l in b:
                izq(d, x + 20, yy, l, px, AZUL)
                yy += interlinea
            yy += hueco
    return y0 + alto_col + 22


def hitos(d, items, y=60, alto=300):
    """Tres o cuatro datos sueltos en horizontal: el número grande y su rótulo debajo.

    Para lo que es puro dato de organización —cuántos, cuánto tiempo, cuánto dura la
    exposición—. Una banda con rótulo girado para decir «28» es desproporcionada.
    """
    n = len(items)
    ancho = (W - 100 - 30 * (n - 1)) / n
    # El rotulo mas largo manda: con alto fijo, «minutos de sustentacion por equipo»
    # se salia de su tarjeta por abajo. Todas comparten alto, o la fila queda coja.
    lineas = max(len(envolver(d, r, CUE, ancho - 26, False)) for _, r in items)
    alto = max(alto, 200 + lineas * int(CUE * 1.25))
    for i, (dato, rotulo) in enumerate(items):
        x = 50 + i * (ancho + 30)
        d.rounded_rectangle([x, y, x + ancho, y + alto], 18, fill=GRISC)
        cen(d, x, y + 46, ancho, dato, 118, AZUL2)
        cen(d, x, y + 190, ancho, rotulo, CUE, AZUL, False, margen=26, alto=alto - 200)
    return y + alto


# ── ejemplo mínimo ────────────────────────────────────────────────────────
if __name__ == "__main__":
    DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ejemplo")
    im, d = lienzo(1290)
    filas_letra(d, [("P", "PLANIFICAR", "Definir qué se quiere y cómo", AZUL2),
                    ("H", "HACER", "Ejecutar lo planificado", TEAL),
                    ("V", "VERIFICAR", "Medir si salió como se esperaba", MORADO),
                    ("A", "ACTUAR", "Corregir y volver a planificar", AMBAR)])
    guardar(im, "ejemplo_phva.png", DEST)
    print("\nSi el cuerpo sale por debajo de 14 pt, hay demasiado contenido: quita, no encojas.")
