# -*- coding: utf-8 -*-
r"""Extrae del manual del fabricante las figuras de equipo del curso FMEQ.

EL MÉTODO ES «EXTRACCIÓN», NO «HÍBRIDO»
    El PDF del fabricante se abre con PyMuPDF, se localiza la figura por su
    caja en la página y se renderiza a 600 dpi. **No pasa por ningún modelo**:
    lo que se ve es el dibujo del fabricante, recortado y nada más. Por eso no
    hace falta la clave de API, y por eso no hay nada que verificar contra las
    cotas: la proporción es la del original.

    El camino híbrido —silueta redibujada con estilo uniforme— sigue estando
    disponible (§10) y es el que se usó para el jumbo Boomer S1 y el scooptram
    ST14. Se hace después, si se quiere homogeneizar el set.

DE DÓNDE SALEN LOS PDF
    De `Entrada/…/3. Recursos para sesiones/`, que es material del propio curso.
    Los nombres traen delante un número de Scribd, y **un re-subido de Scribd no
    es fuente** (regla 3). Lo que hace válida la fuente es el DOCUMENTO: cada uno
    de los que se usan aquí lleva dentro su número de documento del fabricante,
    y así se cita —no como «Scribd»—. Los que no lo llevan no se usan.

RUTAS LARGAS
    `Entrada/` pasa de los 260 caracteres de Windows: se abre con el prefijo
    \\?\ o `os.listdir` falla sin decir por qué.

Uso:  python extraer_fmeq_figuras.py [s3 s4 …]
"""
import os
import sys

import pymupdf
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RECURSOS = os.path.join(
    RAIZ, 'Entrada', 'Exploración y operación minera CICLO II',
    '02. Fundamentos mecánicos de equipos mineros',
    '3. Sesiones y PPTS', '3. Recursos para sesiones')
SALIDA = os.path.join(RAIZ, '04_Recursos-graficos', 'EOM', 'esquemas', 'fmeq')
LARGO = '\\\\?\\'
DPI = 600
ANCHO = 1500          # el lienzo del §11

# Cada figura declara de dónde sale y qué caja de la página ocupa. La caja se
# localiza mirando el texto que rodea a la figura, no a ojo sobre el render.
FIGURAS = {
    's3': [
        dict(archivo='fmeq-s3_scooptram-componentes.png',
             pdf='Sesión06/624157701-9852-1836-56m-Operators-Manual-ST7-and-ST7LP.pdf',
             pagina=8, caja=(66.0, 162.0, 530.0, 540.0),
             que='Los diez componentes del scooptram numerados sobre la máquina, '
                 'con su leyenda: cabina, bastidor de energía, brazo, cilindro '
                 'estabilizador, cucharón, radiador, compartimiento de servicio y '
                 'los dos ejes.',
             fuente='Atlas Copco. «Scooptram ST7 y ST7LP — Manual del operador», '
                    'MP No. 9852 1836 56m (2016-02), cap. 2 «Componentes del vehículo».'),
        dict(archivo='fmeq-s3_minetruck-componentes.png',
             pdf='Sesión08/517515623-3563092619-1-en-US-MT2010-Operation.pdf',
             pagina=6, caja=(80.0, 198.0, 512.0, 548.0),
             que='Los nueve componentes del minetruck rotulados de A a I sobre la '
                 'máquina, con su leyenda: puesto del operador, bastidor de energía, '
                 'eje delantero, articulación, cilindro de dirección, bastidor de '
                 'carga, traba de articulación, tolva y eje trasero.',
             fuente='Epiroc. «Minetruck 2010 — Operation», No. 3563092619.1 en-US '
                    '(2017-03-31), cap. 2.1.1 «Vehicle Components».'),
        dict(archivo='fmeq-s3_minetruck-labor.png',
             pdf='Sesión08/460578054-Minetruck-MT65.pdf',
             pagina=0, caja=(0.0, 190.0, 595.0, 640.0),
             que='Un minetruck cargado avanzando por una labor subterránea, con el '
                 'operador en la cabina y las luces encendidas. Es el estímulo de la '
                 'rutina de Conexión: muestra hechos y ningún juicio.',
             fuente='Epiroc. «Minetruck MT65 — Underground truck with 65-tonne load '
                    'capacity», folleto de producto, portada.'),
    ],
}


def extraer(clave):
    destino = os.path.join(SALIDA, clave)
    os.makedirs(destino, exist_ok=True)
    for f in FIGURAS[clave]:
        origen = os.path.join(RECURSOS, *f['pdf'].split('/'))
        doc = pymupdf.open(LARGO + origen)
        pix = doc[f['pagina']].get_pixmap(dpi=DPI, clip=pymupdf.Rect(*f['caja']))
        ruta = os.path.join(destino, f['archivo'])
        pix.save(ruta)
        doc.close()

        im = Image.open(ruta)
        if im.width != ANCHO:
            im = im.resize((ANCHO, round(im.height * ANCHO / im.width)), Image.LANCZOS)
            im.save(ruta)
        print('  %-42s %4dx%4d · asp %.2f' % (f['archivo'], im.width, im.height,
                                              im.width / im.height))
        print('     %s' % f['fuente'])


if __name__ == '__main__':
    claves = sys.argv[1:] or sorted(FIGURAS)
    for c in claves:
        print('\nFiguras de %s' % c.upper())
        extraer(c)
