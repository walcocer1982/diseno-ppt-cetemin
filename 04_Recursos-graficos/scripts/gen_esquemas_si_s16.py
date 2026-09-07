# -*- coding: utf-8 -*-
"""Esquemas de la sesión 16 de SI-SGCSSMA · compras y contratación externa · 8.1.4 · 8.4

Lo legal sale del §15, verificado el 2026-09-04:
  Ley 29783 art. 68 · la empresa principal garantiza el sistema y el deber de
  prevención de todos los que están en sus instalaciones, verifica los seguros y
  vigila el cumplimiento — y si no lo hace es RESPONSABLE SOLIDARIA
  Ley 29783 art. 69 · quien suministra equipos o sustancias responde de que no
  sean fuente de peligro, y de que manuales y avisos estén en castellano

Uso:  python gen_esquemas_si_s16.py
"""
from __future__ import annotations

import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "04_Recursos-graficos", "comun"))
from esquemas import (W, TIT, CUE, NOTA, AZUL, AZUL2, TEAL, MORADO, AMBAR, GRIS, ROJO,
                      GRISC, BLANCO, lienzo, guardar, banda, franjas, comparativa,
                      caso, filas_letra, tabla, cen, izq)

DEST = os.path.join(RAIZ, "04_Recursos-graficos", "SI", "esquemas")

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def ruta():
    im, d = lienzo(1620)
    filas_letra(d, [
        ("20'", "CONEXIÓN", "El file de un contratista, tal como está en recepción", AZUL2),
        ("45'", "ADQUISICIÓN", "Qué se exige al comprar y de quién es la responsabilidad", TEAL),
        ("40'", "APLICACIÓN", "Tu caso: dos empresas que compraron por precio", MORADO),
        ("20'", "DISCUSIÓN", "Qué faltó exigir, y quién responde", AMBAR),
        ("10'", "REFLEXIÓN", "Lo que te llevas de hoy", GRIS),
    ], y=50, alto=280, sep=30)
    return guardar(im, "ruta-de-aprendizaje_s16.png", DEST)


def puente():
    im, d = lienzo(1150)
    y = franjas(d, [
        ("VIMOS", ["Cómo se controla un proceso propio", "Con su criterio y su rastro"], AZUL2),
        ("HOY", ["Qué pasa cuando el proceso lo hace otro", "Y quién responde si algo sale mal"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 150, "El trabajo sale de la empresa. La responsabilidad, no del todo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_puente.png", DEST)


def estimulo():
    """El file del contratista tal como esta. Solo hechos, y una fecha al pie."""
    im, d = lienzo(1000)
    d.rectangle([50, 50, W - 50, 800], outline=(200, 206, 210), width=4)
    d.rectangle([54, 54, W - 54, 196], fill=AZUL)
    izq(d, 90, 76, "FILE DEL CONTRATISTA", 50, BLANCO, True, ancho=W - 200)
    izq(d, 90, 136, "Servicios de limpieza  ·  archivado en recepción", 38, BLANCO,
        ancho=W - 200)
    campos = [("SCTR", "Vigente hasta el 31 de mayo"),
              ("REGLAMENTO", "Recibido, copia impresa"),
              ("PERSONAL", "Relación de 34 trabajadores"),
              ("RECEPCIÓN", "12 de febrero"),
              ("ÚLTIMA REVISIÓN", "—")]
    y = 236
    for etq, val in campos:
        d.rounded_rectangle([90, y, 500, y + 94], 12, fill=GRISC)
        cen(d, 90, y + 25, 410, etq, 40, GRIS, True)
        izq(d, 530, y + 23, val, CUE, AZUL, ancho=W - 590)
        y += 106
    banda(d, 850, 130, "Hoy es 15 de setiembre", px=CUE)
    return guardar(im, "s16_estimulo.png", DEST)


def que_pide_comprar():
    im, d = lienzo(1010)
    y = tabla(d, ["ISO 45001  ·  8.1.4", "ISO 14001  ·  8.1", "ISO 9001  ·  8.4"], [
        ([["Procesos de compra que aseguren el cumplimiento"],
          ["Controlar los procesos contratados"],
          ["Control de lo suministrado externamente"]], "", None, None),
    ], [50, 530, 1010, W - 50], y=50)
    banda(d, y + 30, 150, "Las tres piden lo mismo con otras palabras: que lo de afuera se controle",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_que-pide-comprar.png", DEST)


def producto_servicio_proceso():
    im, d = lienzo(1330)
    y = franjas(d, [
        ("PRODUCTO", ["Un insumo, un equipo, una sustancia"], AZUL2),
        ("SERVICIO", ["Limpieza, vigilancia, mantenimiento, transporte"], TEAL),
        ("PROCESO", ["Una parte del trabajo que se hace afuera"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 160, "Comprar barato y controlar poco no es ahorro: es riesgo trasladado",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_producto-servicio.png", DEST)


def evaluar():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("CRITERIOS", ["Se fijan primero, y la seguridad entra ahí"], AZUL2),
        ("ANTES", ["Se evalúa antes de contratar, no después de firmar"], TEAL),
        ("DESPUÉS", ["Se reevalúa mirando cómo se desempeñó"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Y se guarda la evidencia: sin registro, la evaluación no ocurrió",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_evaluar.png", DEST)


def reevaluar():
    im, d = lienzo(1010)
    y = comparativa(d, "NO ALCANZA", "SÍ ALCANZA", [
        (["Pedir los papeles al entrar"], ["Verificar que sigan vigentes"]),
        (["Archivarlos en recepción"], ["Revisarlos con una fecha de corte"]),
        (["Aprobado una vez, aprobado siempre"], ["Si el desempeño baja, sale de la lista"]),
    ], y=50)
    banda(d, y + 20, 150, "Un documento vencido en el file es peor que no tenerlo: parece control",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_reevaluar.png", DEST)


def principal_1():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("SISTEMA", ["Un SGSST para todos los que están en el centro de labores",
                     "Ley 29783, artículo 68 a)"], AZUL2),
        ("PREVENCIÓN", ["El deber de prevención de todo ese personal", "Artículo 68 b)"], TEAL),
        ("SEGUROS", ["Verificar la contratación de los seguros de cada empleador",
                     "Artículo 68 c)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "Incluye a quien presta servicios, a los practicantes, visitantes y usuarios",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_principal-1.png", DEST)


def solidaria():
    im, d = lienzo(1230)
    y = franjas(d, [
        ("VIGILA", ["Que sus contratistas cumplan la normativa de seguridad",
                    "Ley 29783, artículo 68 d)"], AZUL2),
        ("Y SI NO", ["La empresa principal es responsable solidaria",
                     "Frente a los daños e indemnizaciones"], ROJO),
    ], im, y=60, alto=330)
    banda(d, y + 20, 160, "Lo dice la ley con esas palabras. No es pedir papeles: es responder con ellos",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_solidaria.png", DEST)


def comunicar_1():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("QUÉ", ["Qué se compra y con qué requisitos, antes de empezar"], AZUL2),
        ("SEGURIDAD", ["Van dentro de la especificación de compra",
                       "DS 005, artículo 84 a)"], TEAL),
        ("AMBIENTE", ["Los requisitos ambientales, y qué hacer con lo que sobra"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "En la especificación, no en un correo aparte ni en una conversación",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_comunicar-1.png", DEST)


def comunicar_2():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("COMPETENCIA", ["Qué se le exige a su gente, y cómo se comprobará"], AZUL2),
        ("ANTES", ["Todo eso se identifica antes de la adquisición",
                   "DS 005, artículo 84 b)"], TEAL),
        ("Y ANTES", ["Y se cumple antes de utilizar el bien o el servicio",
                     "DS 005, artículo 84 c)"], MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "Antes de usarlo, no antes de la auditoría. Lo que no se comunicó no se exige",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_comunicar-2.png", DEST)


def no_se_traslada():
    im, d = lienzo(1300)
    y = franjas(d, [
        ("ALCANCE", ["El proceso contratado sigue dentro del sistema"], AZUL2),
        ("REPARTO", ["Se define qué controla cada uno, y se escribe"], TEAL),
        ("RIESGO", ["El control se ajusta a lo que ese proceso puede causar"], MORADO),
    ], im, y=60, alto=300)
    banda(d, y + 20, 150, "Se puede contratar el trabajo. No se puede contratar la responsabilidad",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_no-se-traslada.png", DEST)


def art_69():
    im, d = lienzo(1360)
    y = franjas(d, [
        ("NO DAÑAR", ["Lo que suministra no debe ser fuente de peligro",
                      "Ley 29783, artículo 69 a)"], AZUL2),
        ("INFORMAR", ["Información y capacitación de instalación, uso y mantenimiento",
                      "Artículo 69 b) y c)"], TEAL),
        ("EN CASTELLANO", ["Manuales y avisos de peligro, traducidos", "Artículo 69 d)"],
         MORADO),
    ], im, y=60, alto=310)
    banda(d, y + 20, 160, "Una hoja de datos en otro idioma no cumple, y el deber es del que la entrega",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_art-69.png", DEST)


def encargo():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("PASO 1", ["Qué faltó comunicar o verificar", "Y qué artículo lo manda"], AZUL2),
        ("PASO 2", ["De quién es la responsabilidad", "Y qué dejarían establecido"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "Las dos empresas compraron y contrataron mirando el precio",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    banda(d, y + 175, 120, "Equipos de 4  ·  30 min de trabajo  ·  2 min por equipo", px=NOTA)
    return guardar(im, "s16_encargo.png", DEST)


def ficha_caso_a():
    im, d = lienzo(2130)
    y = caso(d, "CASO A", "Administradora de Centro Comercial Los Portales S.A.C.  ·  40 propios y 180 de seis contratistas",
        ["H1 · La limpieza, la seguridad y el mantenimiento los hacen empresas contratistas",
         "H2 · A cada contratista se le pide, antes de entrar, copia del SCTR y de su reglamento interno",
         "H3 · Los documentos se archivan en recepción y no se vuelven a mirar",
         "H4 · El SCTR de la empresa de limpieza venció en mayo. Estamos en septiembre",
         "H5 · La selección del contratista de mantenimiento se decidió solo por precio",
         "H6 · No hay criterio escrito de seguridad para elegir contratistas",
         "H7 · En julio un operario de limpieza se cayó de una escalera en el patio de comidas",
         "H8 · La administradora sostiene que «ese trabajador no es de nosotros»"],
        color=AZUL2, y=50, alto=210)
    banda(d, y + 24, 140, "Los 180 trabajan todos los días dentro del centro comercial",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_caso-a.png", DEST)


def ficha_caso_b():
    im, d = lienzo(2130)
    y = caso(d, "CASO B", "Envases y Plásticos del Norte S.A.C.  ·  fábrica de envases  ·  95 trabajadores",
        ["H1 · En abril se compró una extrusora usada, importada",
         "H2 · La orden de compra especifica capacidad, voltaje y plazo de entrega",
         "H3 · No especifica ningún requisito de seguridad ni de resguardos",
         "H4 · La máquina llegó con los manuales en inglés",
         "H5 · Llegó también con dos resguardos desmontados",
         "H6 · El proveedor dice que los resguardos «se retiraron para el transporte»",
         "H7 · La hoja de datos de seguridad del desmoldante nuevo está en portugués",
         "H8 · Compras evalúa a sus proveedores por precio, plazo y calidad del producto"],
        color=TEAL, y=50, alto=210)
    banda(d, y + 24, 140, "La extrusora ya está instalada y produciendo",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_caso-b.png", DEST)


def a_trabajar():
    im, d = lienzo(1160)
    y = franjas(d, [
        ("ENTREGAN", ["Lo que faltó exigir o verificar", "Con el artículo que lo manda"], AZUL2),
        ("Y ADEMÁS", ["De quién es la responsabilidad", "Y qué exigirían la próxima vez"], TEAL),
    ], im, y=60, alto=320)
    banda(d, y + 20, 130, "30 minutos de trabajo  ·  equipos de 4", px=CUE)
    banda(d, y + 175, 120, "Después, 2 minutos por equipo", px=NOTA, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_a-trabajar.png", DEST)


def formato_discusion():
    im, d = lienzo(1270)
    y = franjas(d, [
        ("AFIRMACIÓN", ["Aquí faltó exigir esto, antes de contratar"], AZUL2),
        ("APOYO", ["Y lo sostenemos en el artículo que lo manda"], TEAL),
        ("PREGUNTA", ["Si pasa algo mañana, ¿quién responde?"], MORADO),
    ], im, y=60, alto=290)
    banda(d, y + 20, 150, "Dos minutos por equipo. Empezamos por quién responde",
          px=CUE, fondo=AMBAR, tinta=AZUL)
    return guardar(im, "s16_discusion.png", DEST)


def reflexion():
    im, d = lienzo(1290)
    y = franjas(d, [
        ("ANTES", ["Antes pensaba que el trabajador de la contratista era…"], GRIS),
        ("AHORA", ["Ahora pienso que…"], AZUL2),
        ("PREGUNTA", ["¿Quién verifica los papeles de los que entran a tu planta?"], TEAL),
    ], im, y=60, alto=300)
    banda(d, y + 20, 130, "Se escribe, no se dice: dos minutos", px=CUE)
    return guardar(im, "s16_reflexion.png", DEST)


def main() -> int:
    print("Esquemas de SI-SGCSSMA · sesión 16")
    for fn in (ruta, puente, estimulo, que_pide_comprar, producto_servicio_proceso,
               evaluar, reevaluar, principal_1, solidaria, comunicar_1, comunicar_2,
               no_se_traslada, art_69, encargo, ficha_caso_a, ficha_caso_b, a_trabajar,
               formato_discusion, reflexion):
        fn()
    print("   destino: %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
