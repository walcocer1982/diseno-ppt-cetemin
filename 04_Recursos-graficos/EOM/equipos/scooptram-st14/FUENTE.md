# Scooptram ST14 SG — Fuente y entregables

**Equipo:** Scooptram (LHD — *Load, Haul, Dump*), cargador de bajo perfil para minería subterránea.
**Función en el ciclo de minado:** limpieza y acarreo del material volado (después de perforación y voladura).

## Cita de la fuente (obligatoria al usar la figura)

> Fuente: Epiroc. *Scooptram ST14 SG — Technical specification* (9869 0237 01b, 2025-04). Örebro, Suecia. p. 4 (dimensiones y radio de giro).

Las figuras del fabricante se usan **con su marca** y **citadas**, como referencia técnica en material educativo.

## Entregables

| Archivo | Tipo | Uso |
|---|---|---|
| `scooptram_perfil_referencia.png` | **A. Figura del fabricante** (perfil, con cotas) | Sílabo · PPT al **explicar el equipo** |
| `scooptram_planta_referencia.png` | **A. Figura del fabricante** (planta, radio de giro) | Explicar maniobra y espacio requerido en la labor |
| `scooptram_perfil.png` | **B. Silueta** (PNG, fondo transparente) | Diagramas de **proceso** / ciclo de minado |
| `scooptram_perfil.svg` | **B. Silueta** (vector editable) | Recolorear / escalar sin pérdida |
| `st14_spec.pdf` | Catálogo original | Fuente |
| `gen_perfil.py`, `gen_entregables.py` | Scripts | Regenerar |

## Componentes del Scooptram (para el check)

| Componente | Subpartes |
|---|---|
| Chasis articulado | Sección delantera · **articulación central** · sección trasera |
| Balde (bucket) | Cuchilla/GET · brazos de volteo |
| Boom / brazo de levante | Cilindros de levante · cilindro de volteo |
| Tren de rodaje | 4 neumáticos (2 ejes) · ejes |
| Cabina | **ROPS/FOPS** transversal (operador de lado) |
| Grupo motriz | Motor de tracción · motor auxiliar · **batería** (en la SG) o motor diésel |

## Datos técnicos clave (para el sílabo)

- **Capacidad de acarreo:** 14 000 kg · **Balde estándar:** 6.4 m³
- **Fuerza de arranque (hidráulica):** 22 300 kg
- **Peso aproximado:** 42 000 kg (eje delantero 18 400 / trasero 23 600)
- **Motores:** tracción 200 kW · auxiliar 150 kW (ABB, 400 VAC, refrigeración líquida)
- **Batería:** Li-Ion NMC, 300 kWh útiles · carga 0–90% en 1 h 50 min · permite **cambio de batería**
- **Tiempos:** levante 7.6 s · descenso 4.0 s · volteo 3.0 s
- **Seguridad:** cabina certificada **ISO ROPS/FOPS**, limitador de velocidad
- **Ventaja subterránea:** batería-eléctrico → **cero emisiones de diésel** en interior mina (menos ventilación requerida)

## Estado de cada entregable

| Entregable | Estado | Verificación |
|---|---|---|
| `scooptram_perfil.png/.svg` (silueta) | ✅ **Listo** | Aspecto **4.18** vs **4.18** oficial (desvío 0.1 %) · apoya en el piso · sólida (65.6 %) |
| `scooptram_perfil_referencia.svg/.png` | ✅ **Listo** | Incluye **las dos poses** (transporte + descarga) y todas las cotas |
| `scooptram_planta_referencia.svg/.png` | ✅ **Listo** | Vista de radio de giro completa, vectorial |
| `scooptram_planta.png/.svg` (silueta) | ✅ **Listo** | Cobertura **95.7 %** · 1 pieza · **área 25.8 m²** y **9.80 × 6.26 m**, coherente con un LHD de 10.87 m **doblado 44°** |
| `lh514_planta.png` (Sandvik, alterna) | ✅ Listo | Segunda fuente, resuelta por densidad de tinta |

**Cómo se resolvió la planta (era el caso difícil):** el diagrama de "turning radius" dibuja la máquina **articulada** y entrelazada con los arcos y una "cuña" de barrido. Durante ~10 intentos traté esa cuña como sombreado y peleé con ella; **en realidad era una COTA**: sus tres bordes son las rectas de los radios **R 6644 / R 3402 / R 7255**.

Se resolvió con **dos ideas de Walther**:
1. **El scooptram siempre se dibuja girando** → no buscar la máquina recta; extraerla **doblada** (además es más útil: muestra cómo maniobra en la labor).
2. **Regla maestra de las cotas** → *toda cota lleva un número al costado; una recta si es longitud, dos si es ángulo*. Partiendo del número se borran sus rectas. **9 números → 69 rectas removidas**, incluidas las 3 de la cuña.

Complemento: **segmentación por densidad de tinta** (la máquina tiene detalle, el área barrida está vacía).

## Notas del proceso de generación

- Vistas ubicadas en la pág. 4: **planta** (radio de giro, y≈85–366) y **perfil** (y≈441–543).
- **Línea de piso** detectada en `y=536.8` (28 segmentos) — se quita **antes** de rellenar (error #3 del registro).
- **Cotas** = segmentos rectos puros (`w==0` o `h==0`) de más de 18 pt — 108 removidos.
- El contorno del Scooptram tiene **aperturas**: hubo que aplicar **cierre morfológico (7×7)** antes de rellenar, si no el relleno se fuga y deja huecos. *(Diferencia con el jumbo, cuyo contorno estaba cerrado.)*
- Apertura final (9×9) para cortar filamentos de cota pegados al cuerpo.
