# -*- coding: utf-8 -*-
"""Los cuestionarios de verificación de Métodos de explotación: lectura, prueba y clave.

    python generar_cv.py CV1          (desde 05_Base-de-datos/)
    python generar_cv.py CV2
    python generar_cv.py              (los dos)

Escribe, dentro de la carpeta del curso, en «Recursos de evaluacion/<CV>/»:

    <CV> (lectura).pdf         el cuadernillo que el estudiante lee — 90 minutos
    <CV> (cuestionario).pdf    las 20 preguntas — 45 minutos, sin respuestas
    <CV> (clave).pdf           la misma prueba con la respuesta y por qué falla cada distractor

QUÉ ES UN CV Y QUÉ NO
    Un cuestionario de verificación vale 5 % y verifica LECTURA: que el estudiante
    leyó y entendió el cuadernillo del bloque. No es el examen parcial —ese cruza
    todo el bloque— ni el colaborativo, que se sustenta. Por eso las veinte
    preguntas se responden ENTERAS con el cuadernillo: ninguna pide un dato que
    no esté ahí.

DE DÓNDE SALE EL CUADERNILLO
    De las fuentes que el curso ya cita y que están registradas en imagenes.csv y
    en casos.csv, y que el PDF 02_Fuentes-por-sesion.pdf lista con su código. Cada
    apartado cierra con la fuente de lo que afirma. NO se inventa contenido: lo que
    no está verificado en la base, no entra.

    F1  Ccaso Yucasi, E. I. (2018), tesis UNAP — U.M. Raura (Minsur), §2.6 y §2.7
    F3  U.M. Parcoy, Consorcio Minero Horizonte — tesis UNSAAC vía INGEMMET (TE0380)
    F4  Tesis UAP — Mina Constancia (Hudbay), carguío y acarreo con ControlSense
    F5  Tesis UNDAC — Cerro Lindo (Nexa Resources)
    F6  D.S. 024-2016-EM, Reglamento de Seguridad y Salud Ocupacional en Minería

EL CONTENIDO VIVE AQUÍ, NO EN EL PDF
    Igual que los cinco criterios de cotejo_excel.py: se corrige en este archivo y
    se vuelve a generar. Editar el PDF no sirve, se pierde en la siguiente corrida.

EL REPARTO
    CV1 — bloque 1, sesiones 1 a 5. Indicadores 1 y 2.
    CV2 — bloque 2, sesiones 7 a 11. Indicadores 2 y 3.
"""
from __future__ import print_function

import csv
import os
import re
import sys
import unicodedata

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSO = u"EOM-METEXP"

MARINO = colors.HexColor("#0D2632")
AZUL = colors.HexColor("#167FB9")
GRIS = colors.HexColor("#6C7A82")
CLARO = colors.HexColor("#EEF1F3")
AMBAR = colors.HexColor("#FFC505")
VERDE = colors.HexColor("#2E7D32")
BLANCO = colors.white

T = u"tabla"   # marca de bloque: ("tabla", cabecera, filas)


# ══════════════════════════════════════════════════ EL CUADERNILLO · CV1
CV1 = {
    "titulo": u"El frente y su ciclo",
    "subtitulo": u"Cuadernillo de lectura del bloque 1 · sesiones 1 a 5",
    "minutos_lectura": 90,
    "minutos_prueba": 45,
    "secciones": [
     (u"1 · La veta, sus cajas y lo que miden", [
      u"Un cuerpo mineralizado no flota solo en la roca: está encerrado entre dos "
      u"paredes, que se llaman <b>cajas</b>. La que queda encima es la <b>caja techo</b> "
      u"y la de abajo, la <b>caja piso</b>. La caja techo va siempre del lado hacia el "
      u"que la veta se inclina.",
      u"La <b>potencia</b> es el espesor de la veta medido entre sus dos cajas, y se "
      u"mide <b>perpendicular a las cajas</b>, nunca en horizontal. Es un dato "
      u"geológico: lo que el yacimiento mide, no lo que la mina decide. El "
      u"<b>buzamiento</b> es la inclinación de la veta respecto de la horizontal: una "
      u"veta de 70° está casi parada; una de 20°, tendida.",
      u"La <b>forma del cuerpo</b> dice cómo se presenta el mineral. Las tres más "
      u"comunes son la veta —angosta y larga—, el manto —una capa extendida— y el "
      u"cuerpo, que ocupa un gran volumen. Forma, potencia y buzamiento se leen "
      u"<b>antes</b> de decidir cualquier otra cosa.",
      u"Y hay tres medidas que se confunden con facilidad, y confundirlas es el error "
      u"más común del curso:",
      (T, [u"LA MEDIDA", u"QUÉ ES", u"QUIÉN LA DECIDE"],
       [[u"Potencia", u"lo que mide la veta entre sus cajas", u"la geología"],
        [u"Ancho de minado", u"lo que se rompe en el disparo", u"la mina"],
        [u"Sección", u"la excavación por donde circulan personas y equipo", u"la mina"]]),
      u"El ancho de minado <b>nunca</b> es menor que la potencia, y casi siempre es "
      u"mayor: hay que dejar espacio para trabajar. Romper solo la potencia deja la "
      u"labor sin sección para operar. Una veta de 1,20 m no da una labor de 1,20 m.",
     ], u"F7 · F8 (formas del cuerpo, dominio público) · F1 §2.6"),

     (u"2 · La calidad de la roca y hasta dónde se puede abrir", [
      u"El <b>RMR</b> es la nota del macizo rocoso, de 0 a 100. A menor RMR, peor "
      u"calidad y menos estabilidad: por encima de 60 la roca es buena; por debajo de "
      u"30, mala. El dato viene del <b>mapeo geomecánico</b>, no del criterio del "
      u"maestro, y <b>no cambia</b> con el ancho que se decida abrir: es una condición "
      u"del terreno.",
      u"La ficha de una labor declara <b>dos</b> RMR: el de las cajas y el del mineral. "
      u"Pueden ser muy distintos entre sí, y el que manda para decidir cuánto se abre "
      u"es el de las <b>cajas</b>, porque son ellas las que sostienen el hueco.",
      u"Con ese número se entra a la <b>tabla geomecánica de la labor</b>, que el "
      u"Art. 33 del D.S. 024-2016-EM obliga a publicar en cada labor, firmada por "
      u"ingeniero colegiado y con su vigencia. La tabla cruza la calidad de la roca "
      u"con dos aberturas y con el sostenimiento, y trae además el <b>tiempo de "
      u"autosoporte</b>: cuánto aguanta esa abertura sin moverse.",
      u"Las dos aberturas no son la misma cosa, y confundirlas es lo que precede a una "
      u"caída de caja:",
      (T, [u"LA COLUMNA", u"QUÉ DICE"],
       [[u"Abertura sin sostener", u"lo que el terreno aguanta él solo"],
        [u"Abertura que habilita", u"lo que se puede abrir con el sostenimiento puesto"]]),
      u"El <b>sostenimiento pasivo</b> —cuadros de madera, cimbras— recibe la carga "
      u"cuando la roca ya se movió. El <b>activo</b> —pernos Hydrabolt, shotcrete— "
      u"trabaja con la roca antes de que se mueva. Con el mismo RMR, el activo permite "
      u"abrir mucho más. Y la forma importa: una bóveda en arco reparte la carga mejor "
      u"que un techo recto.",
     ], u"F3 (tabla geomecánica de labor) · F6 (D.S. 024-2016-EM, Art. 33)"),

     (u"3 · El ciclo de minado: cinco operaciones, en un orden", [
      u"Una <b>operación unitaria</b> transforma o desplaza el material de la labor. "
      u"Tiene su propio equipo, su propio insumo y su propio producto, y se puede medir "
      u"sola: metros perforados, toneladas movidas. Si al material no le pasa nada, no "
      u"es una operación unitaria.",
      u"Son cinco, y este es el orden en que se ejecutan:",
      (T, [u"OPERACIÓN", u"QUÉ HACE", u"QUÉ ENTREGA"],
       [[u"1 · Perforación", u"abre los taladros", u"taladros listos para cargar"],
        [u"2 · Voladura", u"rompe la roca", u"material suelto en el piso"],
        [u"3 · Carguío", u"levanta el material roto", u"el equipo cargado"],
        [u"4 · Acarreo", u"lo lleva al echadero o a superficie", u"el frente libre"],
        [u"5 · Sostenimiento", u"sujeta techo y cajas", u"la labor lista para perforar"]]),
      u"El orden no es una costumbre: <b>cada paso necesita al anterior</b>. Sin "
      u"taladros no hay dónde poner el explosivo; sin disparo no hay material que "
      u"cargar; sin carguío el frente queda tapado; sin acarreo la cámara se llena y el "
      u"scooptram se detiene. Y el sostenimiento va sobre roca limpia y desatada, nunca "
      u"sobre desmonte, porque el perno no ancla. Terminado el sostenimiento el frente "
      u"vuelve a estar listo para perforar: <b>el ciclo es un círculo</b>, y cada vuelta "
      u"avanza la labor lo que midió el disparo.",
      u"Hay tres cosas que acompañan al ciclo entero y que <b>no</b> son operaciones "
      u"unitarias: <b>ventilar, desatar y regar</b>. Ninguna transforma ni desplaza el "
      u"material; previenen un daño. Meterlas en la lista del ciclo es el error más "
      u"común al llenar un reporte. El reglamento manda desatar antes, durante y "
      u"después de perforar, y también antes y después de la voladura; el desatado "
      u"manual va con dos personas, una desata y otra vigila; y está prohibido entrar al "
      u"frente hasta que los gases bajen del límite.",
     ], u"F1 §2.6 (operaciones unitarias, U.M. Raura) · F6 (D.S. 024-2016-EM)"),

     (u"4 · El equipo, el material y el control de cada operación", [
      u"Cada operación tiene su equipo y su insumo. El <b>jumbo</b> perfora los "
      u"taladros de forma mecanizada y la <b>jackleg</b> hace lo mismo a mano; el "
      u"<b>cargador neumático</b> mete el explosivo en el taladro; el <b>scooptram</b> "
      u"levanta el material roto y lo lleva a la cámara; el <b>camión de bajo perfil</b> "
      u"lo saca hasta el echadero; el <b>empernador</b> coloca perno y malla. Un equipo "
      u"no hace dos operaciones distintas del ciclo, y cambiar de equipo no cambia la "
      u"operación: cambia el rendimiento.",
      u"El equipo <b>convencional</b> lo mueve la persona; el <b>mecanizado</b>, un "
      u"motor. El mecanizado rinde más y exige más sección para entrar; el convencional "
      u"entra donde el mecanizado no cabe. El <b>winche con rastrillo</b> limpia donde "
      u"el scooptram no puede maniobrar. Un equipo diésel necesita además ventilación "
      u"que diluya sus gases, y el empernador mecanizado pide altura libre sobre el "
      u"techo.",
      u"Cada operación consume además un material propio y medible, y tiene un "
      u"<b>control</b> que el técnico comprueba antes de seguir:",
      (T, [u"OPERACIÓN", u"MATERIAL", u"CONTROL DEL TÉCNICO"],
       [[u"Perforación", u"barrenos y brocas", u"paralelismo y longitud del taladro"],
        [u"Voladura", u"explosivo y accesorios", u"carga por taladro y amarre"],
        [u"Sostenimiento", u"pernos, malla, cemento o resina", u"torque del perno y traslape de la malla"]]),
      u"Sin el control, la operación se dio por hecha pero no por buena. Y la elección "
      u"del equipo no es de gusto: la decide <b>lo que la labor admite</b> —su sección, "
      u"la energía disponible y el recorrido hasta el echadero—. Un equipo que no cabe "
      u"no es lento: es inservible ahí, y pedir el equipo equivocado detiene la guardia "
      u"entera. Antes de pedir se lee la ficha de la labor.",
     ], u"F1 §2.6 y §2.7 (equipos y sostenimiento, U.M. Raura) · F9 (catálogos Epiroc)"),

     (u"5 · Los métodos se reconocen por sus labores", [
      u"Un método de explotación se reconoce por las <b>labores</b> que necesita. La "
      u"<b>rampa</b> da acceso al cuerpo y baja pegada a la caja piso; el "
      u"<b>subnivel</b> es un acceso horizontal desde el que se perfora; la "
      u"<b>chimenea</b> comunica dos niveles y da cara libre al disparo; el <b>corte</b> "
      u"es una rebanada horizontal que se saca y se rellena; la <b>galería de "
      u"transporte</b> y el <b>crucero</b> sacan el mineral por abajo. Cada labor cuesta "
      u"preparación antes de producir una tonelada.",
      u"Cuatro datos deciden qué método admite un yacimiento: <b>forma, potencia, "
      u"buzamiento y RMR</b>. Con potencia grande y cajas firmes el tajeo aguanta sin "
      u"relleno; con veta angosta hay que sacar el mineral rebanada por rebanada. Por "
      u"encima de 60° de buzamiento el mineral roto baja solo por gravedad. Con cajas de "
      u"RMR bajo el tajeo no se sostiene solo. El método no se elige por costumbre: lo "
      u"admite el terreno, y <b>el mismo yacimiento puede pedir dos métodos en dos "
      u"zonas</b>.",
      (T, [u"", u"TAJEO SIN RELLENO", u"CORTE Y RELLENO"],
       [[u"el hueco", u"queda vacío hasta terminar", u"se rellena corte a corte"],
        [u"exige", u"cajas competentes y buzamiento alto", u"tolera cajas malas y veta angosta"],
        [u"rendimiento", u"mayor, menos selectivo", u"menor, selectivo"],
        [u"madera", u"casi no consume", u"consume mucha más"]]),
      u"Lo que cambia entre un método y otro <b>no es el ciclo</b>: son las labores y el "
      u"sostenimiento. Y para atribuirle un método a un plano se leen primero las "
      u"labores y después la ficha: un indicio que aparece en los dos métodos no decide "
      u"nada, hay que buscar el que solo puede darse en uno. La ficha confirma lo que la "
      u"labor ya sugirió, y si las dos se contradicen se vuelve a leer el plano. El "
      u"nombre del método se escribe al final, no al principio.",
     ], u"F5 (Cerro Lindo, tesis UNDAC) · F2 (tesis UNSAAC) · F1 §2.6"),

     (u"6 · Ninguna labor se recibe en cero", [
      u"Una guardia toma el ciclo donde lo dejó la anterior: <b>toda labor se recibe a "
      u"mitad del ciclo</b>. El estado se lee en el frente, no en el reporte, y el "
      u"estado manda sobre lo que diga el programa del día.",
      u"Lo que se ve dice en qué operación se quedó la guardia anterior, y con eso se "
      u"sabe cuál continúa:",
      (T, [u"LO QUE SE ENCUENTRA", u"DE DÓNDE VIENE", u"QUÉ CONTINÚA"],
       [[u"humos, nadie ha entrado", u"un disparo reciente", u"el carguío"],
        [u"material roto en el piso", u"la voladura", u"el carguío"],
        [u"limpio, techo sin asegurar", u"el acarreo terminado", u"el sostenimiento"],
        [u"malla y pernos al tope", u"el sostenimiento terminado", u"la perforación"]]),
      u"Cuidado con una trampa: <b>ventilar y desatar no son la operación que "
      u"continúa</b>. Van antes del carguío, pero la operación que se nombra en el "
      u"reporte es la del ciclo, no la tarea que la habilita.",
      u"Saltarse un paso no adelanta: <b>detiene el que viene después</b>. Perforar "
      u"sobre material sin limpiar deja el frente sin cara libre; sostener sobre "
      u"desmonte deja el perno sin anclaje; cargar sin ventilar expone a la cuadrilla a "
      u"los gases. Un frente detenido lo está toda la guardia, no un rato, y el costo lo "
      u"paga la guardia siguiente.",
      u"El reporte de guardia se llena con <b>lo que se recibe</b>, no con lo que se "
      u"piensa hacer. Si el parte anterior no alcanza para decidir, se anota <b>qué dato "
      u"falta</b>: anotarlo vale más que suponerlo, porque un reporte firmado sobre un "
      u"supuesto es de quien firma, y el que entra responde por lo que aceptó sin "
      u"observar. Sin firma, el reporte de guardia no vale.",
     ], u"F1 §2.6 (ciclo de la U.M. Raura) · F6 (D.S. 024-2016-EM)"),
    ],
}


# ══════════════════════════════════════════════════ EL CUADERNILLO · CV2
CV2 = {
    "titulo": u"El terreno, el equipo y el reporte",
    "subtitulo": u"Cuadernillo de lectura del bloque 2 · sesiones 7 a 11",
    "minutos_lectura": 90,
    "minutos_prueba": 45,
    "secciones": [
     (u"1 · La tabla de la labor trae dos aberturas", [
      u"En la entrada de cada labor hay clavada una <b>tabla geomecánica</b>, firmada "
      u"por ingeniero colegiado y con la vigencia del mes. La obliga el Art. 33 del "
      u"D.S. 024-2016-EM, y no es decorativa: es la que dice cuánto se puede abrir ese "
      u"terreno.",
      u"La tabla cruza la calidad de la roca con <b>dos</b> aberturas y con el "
      u"sostenimiento que corresponde. Un ejemplo de tabla real:",
      (T, [u"CALIDAD · RMR", u"SIN SOSTENER", u"SOSTENIMIENTO", u"HABILITA"],
       [[u"Regular A · 51-60", u"5,00 m", u"pernos sistemáticos", u"8,00 m"],
        [u"Regular B · 41-50", u"3,50 m", u"pernos + malla", u"10,00 m"],
        [u"Mala A · 31-40", u"3,00 m", u"shotcrete + Hydrabolt", u"12,00 m"],
        [u"Mala B · 21-30", u"2,00 m", u"shotcrete + cimbras", u"6,00 m"]]),
      u"La primera abertura es <b>lo que el terreno aguanta solo</b>. La segunda es "
      u"<b>lo que habilita el sostenimiento</b> aplicado. Sostener no asegura el hueco: "
      u"lo <b>habilita</b>, y por eso con el mismo RMR el sostenimiento activo permite "
      u"abrir mucho más.",
      u"La tabla declara además el RMR de las <b>cajas</b> y el del <b>mineral</b>, que "
      u"casi nunca coinciden. La abertura se decide con el de las cajas: son ellas las "
      u"que aguantan el hueco.",
      u"El trabajo del técnico es comparar, con números y no a ojo, la <b>potencia</b> "
      u"de la veta contra la abertura que corresponde. Si la potencia cabe sin sostener, "
      u"se rompe. Si la supera, no se abre hasta sostener. Y si supera incluso la "
      u"abertura habilitada, no se abre de una vez: se saca por <b>realces</b>. Abrir "
      u"más de lo que la tabla admite es lo que precede a una caída de caja.",
     ], u"F3 (U.M. Parcoy, TE0380) · F6 (D.S. 024-2016-EM, Art. 33)"),

     (u"2 · El equipo también pone un límite", [
      u"El terreno pone el límite de arriba; el equipo pone el de abajo. En una unidad "
      u"<b>mecanizada</b> no se mina por debajo de <b>2,40 m</b>, porque por menos no "
      u"entran el jumbo ni el scooptram. Una veta más angosta que ese mínimo obliga a "
      u"romper caja.",
      u"El desmonte que entra con el mineral es <b>dilución</b>. Cuando la impone el "
      u"ancho mínimo de minado, la dilución es <b>forzada</b>: no es un error del "
      u"maestro. Y de ahí sale un resultado que sorprende: <b>el tramo más angosto es el "
      u"que más desmonte produce</b>, porque el ancho no baja del mínimo y todo lo que "
      u"falta es caja.",
      u"Más allá del ancho, una labor le exige <b>cinco</b> cosas al equipo que va a "
      u"trabajar en ella, y si una sola no se cumple el equipo no trabaja ahí:",
      (T, [u"LA EXIGENCIA", u"ES"],
       [[u"Sección", u"el hueco por donde entra y maniobra"],
        [u"Gradiente", u"la pendiente que sube o baja cargado"],
        [u"Energía", u"la que necesita: diésel o red"],
        [u"Vía", u"rieles donde los hay; calzada y radio de giro donde no"],
        [u"Piso", u"firmeza y drenaje para pararse y frenar"]]),
      u"Cada línea la impone un equipo distinto, y <b>ninguno manda en las cinco a la "
      u"vez</b>: el ancho lo impone el más ancho, el alto el más alto, la gradiente el "
      u"que menos sube cargado, la energía el único que pide red. Un valor sin el equipo "
      u"anotado al lado es un valor copiado, y lo que no se exige por escrito no se "
      u"reclama después.",
      u"Una rampa <b>positiva</b> sube desde el nivel y la carga sale bajando; una "
      u"<b>negativa</b> baja hasta el nivel y la carga sale subiendo. La sección no "
      u"cambia con el sentido —el equipo mide lo mismo—, pero la gradiente sí: subiendo "
      u"es tracción y bajando es freno. En la U.M. Raura la gradiente de rampa es del "
      u"<b>12 %</b>, y se da «para que fluya el agua y para ayudar a que el transporte no "
      u"realice esfuerzos mayores». El agua corre siempre hacia abajo: en la positiva "
      u"sale sola por la boca, en la negativa se junta en el fondo, y eso obliga a "
      u"cuneta con salida y bombeo.",
     ], u"F1 §2.6 (gradiente del 12 %, textual) · F9 (catálogos Epiroc)"),

     (u"3 · Qué equipo entra en cada labor", [
      u"Las labores subterráneas no piden lo mismo. El <b>frente</b> es el fondo de una "
      u"labor que avanza; el <b>tajeo</b> es donde se saca mineral y no donde se avanza; "
      u"la <b>rampa</b> comunica niveles y por ella circula todo el equipo; la "
      u"<b>chimenea</b> es vertical o inclinada y casi no admite equipo. Cada una tiene "
      u"su sección y su gradiente propias.",
      u"La labor no se adapta al equipo: <b>el equipo se elige por la labor</b>, y antes "
      u"de asignar se lee su ficha. Como regla general:",
      (T, [u"EL EQUIPO", u"FRENTE", u"TAJEO", u"RAMPA", u"CHIMENEA"],
       [[u"Jumbo", u"sí", u"sí", u"sí", u"no"],
        [u"Scooptram", u"sí", u"sí", u"sí", u"no"],
        [u"Winche de arrastre", u"no", u"sí", u"no", u"no"],
        [u"Camión de bajo perfil", u"no", u"no", u"sí", u"no"]]),
      u"Un equipo puede servir en dos labores y fallar en una tercera, y <b>que falle en "
      u"una no lo inhabilita en las demás</b>. Generalizar «este equipo no sirve» es "
      u"respuesta equivocada. Lo que se dice es dónde entra, dónde no, y <b>qué exigencia "
      u"es la que falla</b>: un equipo que no cabe no es lento, es inservible ahí.",
      u"Una desviación se prueba con el número de la ficha del equipo contra el de la "
      u"ficha de la labor, puestos uno al lado del otro. Sin ese dato, la observación no "
      u"se sostiene. Un programa firmado <b>se devuelve observado, no se desobedece</b>, "
      u"y se observa solo lo que no procede: observar de más cuesta lo mismo que no "
      u"observar, porque las máquinas esperan igual mientras se discute. Lo que está "
      u"bien también se aprueba por escrito, la labor que queda sin equipo posible se "
      u"declara, y la observación lleva firma y fecha.",
     ], u"F1 §2.6 y §2.7 (labores y flota de U.M. Raura)"),

     (u"4 · El mismo ciclo, a cielo abierto", [
      u"A cielo abierto <b>no hay frente ni tajeo: hay banco</b>. El banco es el escalón "
      u"desde donde se extrae el material, y su altura la fija el diseño del talud, no la "
      u"guardia. La <b>rampa</b> comunica los bancos y por ella sale todo. El "
      u"<b>botadero</b> recibe el desmonte, lo que no tiene ley; el <b>pad</b> y el "
      u"<b>stock</b> reciben mineral; la <b>chancadora</b> es la entrada de planta.",
      u"El ciclo también empieza perforando, y los equipos son los mismos en función y "
      u"distintos en tamaño:",
      (T, [u"OPERACIÓN", u"LA HACE", u"EN LA LABOR"],
       [[u"Perforación", u"perforadora sobre orugas, taladros de 11\"", u"el banco"],
        [u"Voladura", u"camión fábrica, con ANFO", u"el banco"],
        [u"Carguío", u"pala hidráulica, cuchara de 27 m³", u"el banco"],
        [u"Acarreo", u"camión minero de 240 t", u"la rampa, hasta su destino"]]),
      u"De las <b>cinco</b> operaciones del ciclo subterráneo, arriba hay <b>cuatro</b>: "
      u"el <b>sostenimiento no aparece</b>, porque no hay techo que sostener. La "
      u"estabilidad la da el <b>diseño del talud</b> —ángulo, altura de banco y berma—, "
      u"que se decide antes de la guardia y no durante. Perforación y voladura sí "
      u"existen, y con más explosivo: suponer que a cielo abierto no se vuela es el error "
      u"más común. El ciclo se acorta, pero no cambia de naturaleza.",
      u"El parte de guardia de superficie trae las mismas cinco filas. Cada fila se llena "
      u"con el <b>equipo</b> y la <b>labor</b> donde ocurrió; la que no ocurrió queda "
      u"vacía con el porqué al margen, porque una fila vacía sin explicación es un parte "
      u"incompleto. El <b>acarreo</b> es la única fila con más de un destino. Y lo que no "
      u"cambia el estado del material —regar la vía, emparejar el piso— <b>no es "
      u"operación unitaria</b>: va abajo, en servicios de mina. Meterlo en el ciclo "
      u"reporta la guardia por debajo de lo que fue.",
     ], u"F4 (Mina Constancia, tesis UAP)"),

     (u"5 · Los pases, el destino y el reporte de desviaciones", [
      u"Un <b>pase</b> es una cucharada de la pala dentro de la tolva del camión. "
      u"Cuántos pases llenan un camión sale de dos capacidades: la cuchara se mide en "
      u"metros cúbicos y la tolva en toneladas, y la <b>densidad</b> del material "
      u"convierte una en otra. La ficha del camión declara con cuántos pases se llena; en "
      u"Mina Constancia, el CAT 793F de 240 toneladas «puede cargarse de manera efectiva "
      u"con 5 pases».",
      u"Un pase de menos deja el camión a media carga <b>toda la guardia</b>, y lo que se "
      u"pierde por viaje se multiplica por todos los viajes. El camión sale igual de lleno "
      u"a la vista.",
      u"Del banco no sale un solo material: salen varios, y la <b>ley de corte</b> los "
      u"separa. Sobre la ley de corte es mineral y va a chancadora o a stock; bajo la ley "
      u"de corte es desmonte y va al botadero. El destino lo marca geología <b>antes</b> "
      u"de que la pala cargue. Y aquí está lo importante:",
      (T, [u"SI SE EQUIVOCA EL DESTINO", u"LO QUE PASA", u"EN EL TONELAJE"],
       [[u"mineral al botadero", u"se pierde la ley", u"no se nota"],
        [u"desmonte a chancadora", u"ensucia la alimentación de planta", u"no se nota"]]),
      u"Cada camión tiene además su ruta y su condición de piso. La ficha declara la "
      u"limitación y el clima decide si aplica: en Constancia, el Hitachi EH4000 «tiene "
      u"problemas de derrapamiento en condiciones adversas (pistas mojadas con lluvia, "
      u"granizo)». Un equipo fuera de su ruta deja de hacer sus viajes, y los viajes que "
      u"no se hicieron son toneladas que no salieron: asignar mal no rompe el equipo, "
      u"rompe el programa.",
      u"El <b>reporte de desviación</b> no es un descargo de producción. Cada desviación "
      u"lleva tres cosas: <b>qué pasó, con qué dato se prueba y qué se pide corregir</b>, "
      u"y la cuenta que la sostiene se escribe al pie. Sin el dato que la prueba, la "
      u"desviación no se sostiene. Hay desviaciones que <b>no restan toneladas y se "
      u"reportan igual</b> —un mineral mandado al botadero no resta tonelaje: resta "
      u"ley—, porque lo que no se reporta se repite la guardia siguiente. Lleva firma y "
      u"fecha: reportar es la última operación del técnico, no la opcional.",
     ], u"F4 (Mina Constancia, tesis UAP — pases y derrapamiento, textual)"),
    ],
}


# ══════════════════════════════════════════════════ LAS PREGUNTAS
# (enunciado, [4 alternativas], índice de la correcta, sesión, por qué)
P_CV1 = [
 (u"¿Cómo se mide la potencia de una veta?",
  [u"Perpendicular a las cajas", u"En horizontal, de pared a pared",
   u"A lo largo del eje de la labor", u"Según la inclinación del piso"], 0, u"S1",
  u"La potencia es el espesor entre cajas y se mide perpendicular a ellas, nunca en horizontal."),
 (u"Una veta buza 20°. ¿Cómo está?",
  [u"Tendida", u"Casi vertical", u"Vertical exacta", u"Invertida"], 0, u"S1",
  u"70° es casi vertical; 20° es tendida."),
 (u"La ficha de una labor declara RMR 45 en cajas y 60 en mineral. Para decidir cuánto se puede abrir, ¿cuál manda?",
  [u"El de las cajas", u"El del mineral", u"El promedio de los dos", u"El mayor de los dos"], 0, u"S1",
  u"Las cajas son las que sostienen el hueco."),
 (u"La veta mide 1,20 m. ¿Qué ancho de labor corresponde?",
  [u"Mayor que 1,20 m, para dejar espacio de trabajo", u"Exactamente 1,20 m",
   u"Menor que 1,20 m, para no diluir", u"El que el maestro decida en el frente"], 0, u"S1",
  u"El ancho nunca es menor que la potencia y casi siempre es mayor: romper solo la potencia deja la labor sin sección."),
 (u"¿Qué le pasa al RMR de una labor si se decide abrirla más ancha?",
  [u"No cambia: es una condición del terreno", u"Baja, porque el hueco es mayor",
   u"Sube, si se añade sostenimiento", u"Cambia solo si cambia el buzamiento"], 0, u"S1",
  u"El RMR viene del mapeo geomecánico y no depende de lo que la mina decida abrir."),
 (u"Con el mismo RMR, ¿qué sostenimiento permite abrir más?",
  [u"El activo: pernos Hydrabolt y shotcrete", u"El pasivo: cuadros de madera y cimbras",
   u"Los dos permiten lo mismo", u"Ninguno cambia la abertura admisible"], 0, u"S1",
  u"El activo trabaja con la roca antes de que se mueva; el pasivo recibe la carga después."),
 (u"¿Qué obliga el Art. 33 del D.S. 024-2016-EM?",
  [u"Publicar la tabla geomecánica en cada labor",
   u"Desatar antes y después de la voladura",
   u"Ventilar hasta que los gases bajen del límite",
   u"Firmar el reporte de guardia antes del cambio de turno"], 0, u"S1",
  u"La tabla va publicada, firmada por ingeniero colegiado y con su vigencia."),
 (u"¿Cuál de estas NO es una operación unitaria del ciclo?",
  [u"Regar la vía", u"Perforación", u"Acarreo", u"Sostenimiento"], 0, u"S2",
  u"Regar no transforma ni desplaza el material: es un control permanente."),
 (u"¿Qué condición cumple una operación unitaria?",
  [u"Transforma o desplaza el material de la labor",
   u"Se hace una sola vez por guardia",
   u"La ejecuta siempre equipo mecanizado",
   u"Está escrita en el programa del día"], 0, u"S2",
  u"Además tiene equipo, insumo y producto propios, y se puede medir sola."),
 (u"¿Cuál es el orden correcto del ciclo de minado?",
  [u"Perforación, voladura, carguío, acarreo, sostenimiento",
   u"Perforación, carguío, voladura, sostenimiento, acarreo",
   u"Voladura, perforación, acarreo, carguío, sostenimiento",
   u"Sostenimiento, perforación, voladura, carguío, acarreo"], 0, u"S2",
  u"Cada paso necesita el producto del anterior; el sostenimiento devuelve el frente a la perforación."),
 (u"¿Por qué no se sostiene antes de limpiar el frente?",
  [u"Porque sobre desmonte el perno no ancla",
   u"Porque el sostenimiento va siempre al final del turno",
   u"Porque el empernador no cabe con material en el piso",
   u"Porque primero hay que medir el avance del disparo"], 0, u"S2",
  u"El sostenimiento va sobre roca limpia y desatada."),
 (u"¿Qué manda el reglamento sobre el desatado?",
  [u"Antes, durante y después de perforar, y antes y después de la voladura",
   u"Solo al inicio de la guardia",
   u"Únicamente después de la voladura",
   u"Cuando el supervisor lo indique"], 0, u"S2",
  u"Y el desatado manual va con dos personas: una desata y otra vigila."),
 (u"En una galería angosta de 2,10 × 1,50 m sin energía, ¿qué se usa para perforar?",
  [u"Jackleg", u"Jumbo de dos brazos", u"Empernador mecanizado", u"Cargador neumático"], 0, u"S3",
  u"El convencional entra donde el mecanizado no cabe; además no hay energía tendida."),
 (u"¿Con qué se limpia el material roto donde el scooptram no puede maniobrar?",
  [u"Winche con rastrillo", u"Camión de bajo perfil", u"Empernador", u"Cargador neumático"], 0, u"S3",
  u"Es la salida convencional cuando la sección no admite el scooptram."),
 (u"¿Qué controla el técnico en la perforación?",
  [u"El paralelismo y la longitud del taladro",
   u"El torque del perno y el traslape de la malla",
   u"La carga por taladro y el amarre",
   u"El tiempo de ventilación tras el disparo"], 0, u"S3",
  u"El torque es control de sostenimiento; la carga y el amarre, de voladura."),
 (u"Cambiar el jumbo por una jackleg, ¿qué cambia?",
  [u"El rendimiento, no la operación", u"La operación, no el rendimiento",
   u"El material que se consume", u"El control que hace el técnico"], 0, u"S3",
  u"Un equipo no hace dos operaciones distintas del ciclo."),
 (u"En un plano se ve un hueco grande y vacío entre dos accesos horizontales. ¿Qué método delata?",
  [u"Tajeo sin relleno", u"Corte y relleno ascendente",
   u"Cámaras y pilares", u"Block caving"], 0, u"S4",
  u"En corte y relleno cada corte se rellena antes de sacar el siguiente; el hueco no queda vacío."),
 (u"¿Cuál de los dos métodos consume mucha más madera?",
  [u"Corte y relleno", u"Tajeo sin relleno",
   u"Los dos por igual", u"Ninguno consume madera"], 0, u"S4",
  u"Por eso un requerimiento de madera copiado de una zona a otra deja la segunda sin abastecimiento."),
 (u"Un frente tiene humos y nadie ha entrado. ¿Con qué operación continúa?",
  [u"El carguío", u"El sostenimiento", u"La perforación", u"La ventilación"], 0, u"S5",
  u"Ventilar y desatar van antes, pero no son la operación del ciclo que continúa."),
 (u"El parte de la guardia saliente no alcanza para decidir una labor. ¿Qué se hace?",
  [u"Se marca «falta el dato» y se nombra cuál",
   u"Se supone lo más probable y se firma",
   u"Se deja la fila en blanco sin comentario",
   u"Se copia lo que decía el parte de la guardia anterior"], 0, u"S5",
  u"Un reporte firmado sobre un supuesto es de quien firma."),
]

P_CV2 = [
 (u"La tabla geomecánica de una labor trae dos aberturas por fila. ¿Qué dice la primera?",
  [u"Lo que el terreno aguanta sin sostener",
   u"Lo que habilita el sostenimiento aplicado",
   u"El ancho mínimo de minado de la unidad",
   u"La sección máxima que admite el equipo"], 0, u"S7",
  u"La segunda columna es la que habilita el sostenimiento."),
 (u"Cajas de RMR 45 y una potencia de 2,00 m. Según la tabla, el terreno admite 3,50 m sin sostener. ¿Qué corresponde?",
  [u"Se rompe: la potencia cabe sin sostener",
   u"No se abre hasta sostener",
   u"Se saca por realces",
   u"Se reduce el ancho a la potencia exacta"], 0, u"S7",
  u"La comparación se hace con números: 2,00 m es menor que 3,50 m."),
 (u"En una unidad mecanizada, ¿por debajo de qué ancho no se mina?",
  [u"2,40 m", u"1,20 m", u"3,50 m", u"4,50 m"], 0, u"S7",
  u"Por menos no entran el jumbo ni el scooptram."),
 (u"Un tramo de veta mide 0,60 m en una unidad mecanizada. ¿Qué ocurre?",
  [u"Se rompe el ancho mínimo y entra caja: dilución forzada",
   u"Se rompe solo 0,60 m para no diluir",
   u"Se cambia a equipo convencional sin más",
   u"Se detiene el tramo hasta que la veta ensanche"], 0, u"S7",
  u"La dilución la impone el equipo, no es un error del maestro."),
 (u"De los tres tramos de una veta, ¿cuál produce más desmonte?",
  [u"El más angosto", u"El más ancho", u"El de menor RMR", u"El de mayor buzamiento"], 0, u"S7",
  u"El ancho no baja del mínimo de minado, así que todo lo que falta de veta es caja."),
 (u"Una veta supera incluso la abertura que habilita el sostenimiento. ¿Qué se hace?",
  [u"No se abre de una vez: se saca por realces",
   u"Se abre igual y se refuerza después",
   u"Se cambia la tabla geomecánica de la labor",
   u"Se reduce el ancho al que el terreno aguanta solo"], 0, u"S7",
  u"Abrir más de lo que la tabla admite es lo que precede a una caída de caja."),
 (u"¿Cuál de estas NO es una de las cinco exigencias que una labor pone al equipo?",
  [u"El rendimiento por guardia", u"La gradiente", u"La energía", u"La condición del piso"], 0, u"S8",
  u"Las cinco son sección, gradiente, energía, vía y piso."),
 (u"Cuatro exigencias se cumplen y una no. ¿El equipo trabaja?",
  [u"No: la que falta manda sobre las otras cuatro",
   u"Sí, con menor rendimiento",
   u"Sí, si la que falta es la vía",
   u"Depende de la antigüedad del equipo"], 0, u"S8",
  u"No se promedian ni se compensan."),
 (u"¿Qué equipo impone el ancho de la hoja de condiciones?",
  [u"El más ancho de los que van a entrar", u"El más pesado",
   u"El que menos sube cargado", u"El que necesita red eléctrica"], 0, u"S8",
  u"El alto lo impone el más alto; la gradiente, el que menos sube cargado."),
 (u"Una rampa pasa de positiva a negativa. ¿Cambia la sección exigida?",
  [u"No: el equipo mide lo mismo en los dos sentidos",
   u"Sí, porque la carga sale subiendo",
   u"Sí, porque cambia el radio de giro",
   u"Solo si cambia también la gradiente"], 0, u"S8",
  u"Lo que cambia con el sentido es lo que la gradiente exige y a dónde va el agua."),
 (u"En una rampa negativa, ¿qué pasa con el agua?",
  [u"Se junta en el fondo y obliga a cuneta con salida y bombeo",
   u"Sale sola por la boca de la rampa",
   u"Se evapora con la ventilación",
   u"No cambia respecto de una rampa positiva"], 0, u"S8",
  u"El agua corre siempre hacia abajo."),
 (u"La ficha de un equipo no trae un dato que la hoja de condiciones pide. ¿Qué se hace?",
  [u"Se solicita y se marca la línea; no se firma en blanco",
   u"Se supone con el valor de un equipo parecido",
   u"Se deja la línea vacía sin más",
   u"Se copia el valor de la hoja anterior"], 0, u"S8",
  u"Lo que no se exige por escrito no se reclama después."),
 (u"Un scooptram sirve en el frente y en el tajeo pero no en la chimenea. ¿Qué significa?",
  [u"Que no entra en la chimenea, y hay que nombrar la exigencia que falla",
   u"Que el equipo no sirve y se devuelve a almacén",
   u"Que la chimenea está mal diseñada",
   u"Que se puede usar igual, más lento"], 0, u"S9",
  u"Que falle en una labor no lo inhabilita en las demás."),
 (u"¿Con qué se prueba una observación a un programa de equipos?",
  [u"El dato de la ficha del equipo contra el de la ficha de la labor",
   u"La experiencia del supervisor de guardia",
   u"El rendimiento histórico del equipo",
   u"La firma del jefe de mina en el programa"], 0, u"S9",
  u"Sin el dato, la observación no se sostiene."),
 (u"Un programa de equipos ya está firmado por el jefe de mina y una asignación no procede. ¿Qué corresponde?",
  [u"Devolverlo observado, a tiempo y por escrito",
   u"Cumplirlo tal como está: ya está firmado",
   u"Cambiar el equipo en el frente sin avisar",
   u"Esperar a la siguiente guardia para plantearlo"], 0, u"S9",
  u"Un programa firmado se devuelve observado, no se desobedece."),
 (u"¿Por qué observar de más cuesta lo mismo que no observar?",
  [u"Porque las máquinas esperan igual mientras se discute",
   u"Porque el jefe de mina no acepta más de tres observaciones",
   u"Porque las observaciones de más no se registran",
   u"Porque obliga a rehacer todo el programa"], 0, u"S9",
  u"Se observa solo lo que no procede."),
 (u"¿Cuál de las cinco operaciones del ciclo subterráneo NO aparece a cielo abierto?",
  [u"El sostenimiento", u"La voladura", u"El carguío", u"El acarreo"], 0, u"S10",
  u"No hay techo que sostener: la estabilidad la da el diseño del talud."),
 (u"La cisterna regó la vía y el tractor emparejó el piso del banco. ¿Dónde se anotan?",
  [u"En servicios de mina, fuera de las filas del ciclo",
   u"En la fila del acarreo",
   u"En la fila del carguío",
   u"En la fila que quedó vacía"], 0, u"S10",
  u"No cambian el estado del material; meterlas en el ciclo reporta la guardia por debajo de lo que fue."),
 (u"La ficha del camión dice que se llena con 5 pases y el reporte anota 4 toda la guardia. ¿Qué significa?",
  [u"El camión viajó a media carga toda la guardia",
   u"La pala trabajó más rápido de lo previsto",
   u"El camión hizo más viajes de los programados",
   u"El dato de la ficha está desactualizado"], 0, u"S11",
  u"Lo que se pierde por viaje se multiplica por todos los viajes."),
 (u"Un polígono con ley por encima de la de corte aparece descargado en botadero. ¿Qué se pierde?",
  [u"La ley: no resta tonelaje, pero el mineral no llega a planta",
   u"Tonelaje del día, que se descuenta del programa",
   u"Nada: el botadero también se contabiliza",
   u"Solo tiempo de ciclo del camión"], 0, u"S11",
  u"El destino equivocado no se ve en el tonelaje del día, y por eso se reporta igual."),
]

CUESTIONARIOS = {
    u"CV1": (CV1, P_CV1, u"Bloque 1 · sesiones 1 a 5",
             u"IND-EOM-METEXP-1 y IND-EOM-METEXP-2"),
    u"CV2": (CV2, P_CV2, u"Bloque 2 · sesiones 7 a 11",
             u"IND-EOM-METEXP-2 y IND-EOM-METEXP-3"),
}
LETRAS = u"abcd"


# ══════════════════════════════════════════════════ maquetación
def E(nombre, **kw):
    base = dict(fontName="Helvetica", fontSize=9.5, leading=13.5, textColor=MARINO,
                spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(nombre, **base)


TITULO = E("titulo", fontName="Helvetica-Bold", fontSize=20, leading=24, spaceAfter=4)
SUB = E("sub", fontSize=10.5, leading=14, textColor=GRIS, spaceAfter=14)
H1 = E("h1", fontName="Helvetica-Bold", fontSize=13, leading=16.5, textColor=AZUL,
       spaceBefore=12, spaceAfter=7)
CUERPO = E("cuerpo", alignment=TA_JUSTIFY)
PIE = E("pie", fontSize=8, leading=11, textColor=GRIS, spaceAfter=2)
CELDA = E("celda", fontSize=8.5, leading=11.5, spaceAfter=0)
CELDA_B = E("celda_b", fontSize=8.5, leading=11.5, fontName="Helvetica-Bold", spaceAfter=0)
PREG = E("preg", fontName="Helvetica-Bold", fontSize=9.5, leading=13, spaceBefore=9,
         spaceAfter=3)
ALT = E("alt", fontSize=9.5, leading=13, spaceAfter=1, leftIndent=14)
OK = E("ok", fontSize=9.5, leading=13, spaceAfter=1, leftIndent=14, textColor=VERDE,
       fontName="Helvetica-Bold")


def tabla(cabecera, filas, anchos=None):
    n = len(cabecera)
    anchos = anchos or [17.0 / n * cm] * n
    datos = [[Paragraph(c, CELDA_B) for c in cabecera]]
    datos += [[Paragraph(c, CELDA) for c in f] for f in filas]
    t = Table(datos, colWidths=anchos, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), MARINO),
        ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CLARO, BLANCO]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFBDB6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def cinta(texto, fondo=CLARO):
    t = Table([[Paragraph(texto, CUERPO)]], colWidths=[17 * cm], hAlign="LEFT")
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), fondo),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                           ("TOPPADDING", (0, 0), (-1, -1), 7),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return t


def pie_de(cv, que):
    def dibuja(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(GRIS)
        canvas.drawString(2 * cm, 1.3 * cm,
                          u"%s · Métodos de explotación · %s" % (cv, que))
        canvas.drawRightString(19 * cm, 1.3 * cm, u"%d" % doc.page)
        canvas.setStrokeColor(colors.HexColor("#BFBDB6"))
        canvas.line(2 * cm, 1.8 * cm, 19 * cm, 1.8 * cm)
        canvas.restoreState()
    return dibuja


def documento(ruta, titulo):
    return SimpleDocTemplate(ruta, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                             topMargin=1.9 * cm, bottomMargin=2.4 * cm,
                             title=titulo, author=u"CETEMIN · diseño instruccional")


def _sin_tildes(txt):
    return u"".join(c for c in unicodedata.normalize("NFKD", txt)
                    if not unicodedata.combining(c))


def carpeta_del_curso():
    salida = os.path.join(RAIZ, u"03_Entregables-diseño")
    with open(os.path.join(RAIZ, u"05_Base-de-datos", u"cursos.csv"),
              encoding="utf-8-sig", newline="") as f:
        nombre = next((c[u"nombre_curso"] for c in csv.DictReader(f)
                       if c[u"curso_id"] == CURSO), CURSO)
    slug = re.sub(u"[^A-Za-z0-9\\-]", u"", _sin_tildes(nombre).replace(u" ", u"-"))
    destino = None
    for h in sorted(os.listdir(salida)):
        if os.path.isdir(os.path.join(salida, h)) and \
                _sin_tildes(h).lower().endswith(slug.lower()):
            if re.match(r"^Curso\d+_", h) or destino is None:
                destino = os.path.join(salida, h)
    if destino is None:
        raise SystemExit(u"no encuentro la carpeta del curso")
    return destino


# ══════════════════════════════════════════════════ los tres documentos
def lectura(cv, datos, bloque, dest):
    c = []
    c.append(Paragraph(datos["titulo"], TITULO))
    c.append(Paragraph(u"%s &nbsp;·&nbsp; %s" % (cv, datos["subtitulo"]), SUB))
    c.append(cinta(
        u"<b>Cómo se usa este cuadernillo.</b> Se lee entero antes del cuestionario de "
        u"verificación %s. La lectura toma unos <b>%d minutos</b>; el cuestionario son "
        u"<b>20 preguntas</b> de opción múltiple y se responde en <b>%d minutos</b>. "
        u"<b>Todas las respuestas están aquí dentro</b>: ninguna pregunta pide un dato "
        u"que este cuadernillo no traiga.<br/><br/>"
        u"Al final de cada apartado se indica de qué fuente sale lo que afirma. Las "
        u"fuentes completas, con su enlace, están en el documento "
        u"<i>02_Fuentes-por-sesion.pdf</i> del curso."
        % (cv[-1], datos["minutos_lectura"], datos["minutos_prueba"])))
    for titulo, bloques, fuente in datos["secciones"]:
        partes = [Paragraph(titulo, H1)]
        for b in bloques:
            if isinstance(b, tuple) and b and b[0] == T:
                partes.append(Spacer(1, 3))
                partes.append(tabla(b[1], b[2]))
                partes.append(Spacer(1, 5))
            else:
                partes.append(Paragraph(b, CUERPO))
        partes.append(Paragraph(u"<b>De dónde sale:</b> %s" % fuente, PIE))
        c.append(KeepTogether(partes[:2]))
        c.extend(partes[2:])
    ruta = os.path.join(dest, u"%s (lectura).pdf" % cv)
    doc = documento(ruta, u"%s · %s" % (cv, datos["titulo"]))
    doc.build(c, onFirstPage=pie_de(cv, u"cuadernillo de lectura"),
              onLaterPages=pie_de(cv, u"cuadernillo de lectura"))
    return ruta


def prueba(cv, datos, preguntas, bloque, inds, dest, con_clave):
    c = []
    c.append(Paragraph(u"Cuestionario de verificación %s" % cv[-1], TITULO))
    c.append(Paragraph(u"Métodos de explotación &nbsp;·&nbsp; %s" % bloque, SUB))
    if con_clave:
        c.append(cinta(
            u"<b>CLAVE DEL INSTRUCTOR — no se entrega al estudiante.</b> La respuesta "
            u"correcta va marcada, y debajo de cada pregunta se explica por qué. "
            u"Indicadores: %s. Vale <b>5 %%</b> de la nota del curso." % inds, AMBAR))
    else:
        c.append(cinta(
            u"<b>Instrucciones.</b> 20 preguntas de opción múltiple. Marca <b>una sola</b> "
            u"alternativa por pregunta. Tiempo: <b>%d minutos</b>. Todas se responden con "
            u"el cuadernillo <i>%s (lectura)</i>; no hace falta ningún otro material.<br/><br/>"
            u"Nombre: ______________________________  Fecha: ____________"
            % (datos["minutos_prueba"], cv)))
    c.append(Spacer(1, 6))
    for n, (enunciado, alts, ok, ses, porque) in enumerate(preguntas, 1):
        partes = [Paragraph(u"%d. %s" % (n, enunciado), PREG)]
        for i, a in enumerate(alts):
            marca = u"%s) %s" % (LETRAS[i], a)
            if con_clave and i == ok:
                partes.append(Paragraph(u"%s &nbsp;&nbsp;✔" % marca, OK))
            else:
                partes.append(Paragraph(marca, ALT))
        if con_clave:
            partes.append(Paragraph(u"<b>%s</b> · %s" % (ses, porque), PIE))
        c.append(KeepTogether(partes))
    if con_clave:
        c.append(Spacer(1, 10))
        c.append(Paragraph(u"Respuestas", H1))
        c.append(Paragraph(u" &nbsp;·&nbsp; ".join(
            u"<b>%d</b> %s" % (n, LETRAS[p[2]]) for n, p in enumerate(preguntas, 1)),
            CUERPO))
    nombre = u"%s (clave).pdf" % cv if con_clave else u"%s (cuestionario).pdf" % cv
    ruta = os.path.join(dest, nombre)
    que = u"clave del instructor" if con_clave else u"cuestionario"
    doc = documento(ruta, u"%s · %s" % (cv, que))
    doc.build(c, onFirstPage=pie_de(cv, que), onLaterPages=pie_de(cv, que))
    return ruta


if __name__ == "__main__":
    pedidos = [sys.argv[1].upper()] if len(sys.argv) > 1 else [u"CV1", u"CV2"]
    base = carpeta_del_curso()
    for cv in pedidos:
        if cv not in CUESTIONARIOS:
            raise SystemExit(u"no conozco %s (CV1 o CV2)" % cv)
        datos, preguntas, bloque, inds = CUESTIONARIOS[cv]
        assert len(preguntas) == 20, u"%s tiene %d preguntas, no 20" % (cv, len(preguntas))
        dest = os.path.join(base, u"Recursos de evaluacion", cv)
        if not os.path.isdir(dest):
            os.makedirs(dest)
        for r in (lectura(cv, datos, bloque, dest),
                  prueba(cv, datos, preguntas, bloque, inds, dest, False),
                  prueba(cv, datos, preguntas, bloque, inds, dest, True)):
            print(u"  ✔ %s" % os.path.relpath(r, RAIZ))
        palabras = sum(len(b.split()) for _, bs, _ in datos["secciones"]
                       for b in bs if not isinstance(b, tuple))
        print(u"    %d apartados · ~%d palabras de lectura · %d preguntas"
              % (len(datos["secciones"]), palabras, len(preguntas)))
