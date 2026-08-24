# -*- coding: utf-8 -*-
"""Genera Visor.html a partir de los CSV.

POR QUE UN GENERADOR Y NO UN HTML A MANO
    El visor anterior tenia los datos EMBEBIDOS: al cambiar un CSV quedaba
    desactualizado sin avisar. Ahora se regenera con un comando y siempre
    refleja la base.

LOS TRES NIVELES
    1. Lista de cursos, filtrable por carrera.
    2. El curso: capacidad, indicadores y sus sesiones, cada una con su
       aprendizaje esperado, sus puntos clave y su evaluacion.
    3. La sesion: el guion lamina por lamina, con momento, minutaje y la
       imagen que le toca.

Uso:  python generar_visor.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
# COMUNES: viven en la raiz. La ficha oficial de los 35 cursos y el catalogo
# de imagenes y equipos son unicos, para que una silueta se pueda reusar.
COMUNES = ["cursos", "imagenes", "equipos"]
# POR CARRERA: cada lider trabaja SU carpeta y no puede pisar a los otros.
POR_CARRERA = ["capacidades", "indicadores", "sesiones", "contenidos", "casos",
               "evaluaciones", "bloques", "rubricas", "observaciones", "laminas",
               "contenido_imagen", "valoraciones", "actividades", "curso_detalle"]
CARRERAS = ["EOM", "SI", "PM"]


def leer(ruta: Path) -> list[dict]:
    if not ruta.exists():
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


datos = {t: leer(RAIZ / f"{t}.csv") for t in COMUNES}
for t in POR_CARRERA:                      # se juntan las tres para la vista global
    datos[t] = [f for c in CARRERAS for f in leer(RAIZ / c / f"{t}.csv")]
TABLAS = COMUNES + POR_CARRERA

HTML = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Diseño instruccional — CETEMIN</title>
<style>
 :root{--tinta:#1c2430;--suave:#5b6675;--linea:#e2e6eb;--fondo:#f6f7f9;
       --acento:#17545e;--aviso:#b4541a;--ok:#2d6a4f}
 *{box-sizing:border-box}
 body{margin:0;font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;
      color:var(--tinta);background:var(--fondo)}
 header{background:var(--acento);color:#fff;padding:14px 22px}
 header b{font-size:17px}
 header span{opacity:.75;margin-left:10px;font-size:13px}
 .cols{display:grid;grid-template-columns:270px 1fr;min-height:calc(100vh - 52px)}
 aside{background:#fff;border-right:1px solid var(--linea);overflow:auto;max-height:calc(100vh - 52px)}
 main{padding:22px 26px;overflow:auto;max-height:calc(100vh - 52px)}
 .filtros{display:flex;gap:4px;padding:10px;border-bottom:1px solid var(--linea);flex-wrap:wrap}
 .filtros button{border:1px solid var(--linea);background:#fff;border-radius:6px;
      padding:4px 10px;cursor:pointer;font-size:13px}
 .filtros button.on{background:var(--acento);color:#fff;border-color:var(--acento)}
 .curso{padding:9px 14px;border-bottom:1px solid #f1f3f5;cursor:pointer;font-size:14px}
 .curso:hover{background:#f0f4f5}
 .curso.on{background:#e6eef0;border-left:3px solid var(--acento);padding-left:11px}
 .curso small{display:block;color:var(--suave);font-size:12px}
 .modulo{padding:7px 14px;background:#fafbfc;font-size:11px;letter-spacing:.5px;
      text-transform:uppercase;color:var(--suave);border-bottom:1px solid var(--linea)}
 h1{font-size:21px;margin:0 0 4px}
 h2{font-size:16px;margin:26px 0 10px;padding-bottom:5px;border-bottom:2px solid var(--linea)}
 .meta{color:var(--suave);font-size:13px;margin-bottom:16px}
 .caja{background:#fff;border:1px solid var(--linea);border-radius:8px;padding:14px 16px;margin-bottom:12px}
 .ind{font-size:13px;padding:6px 0;border-bottom:1px dashed var(--linea)}
 .ind b{color:var(--acento)}
 .ses{background:#fff;border:1px solid var(--linea);border-radius:8px;margin-bottom:9px;overflow:hidden}
 .ses>div:first-child{padding:11px 14px;cursor:pointer;display:flex;gap:10px;align-items:flex-start}
 .ses>div:first-child:hover{background:#f7f9fa}
 .n{background:var(--acento);color:#fff;border-radius:5px;padding:2px 8px;font-size:12px;font-weight:600;flex-shrink:0}
 .n.ev{background:var(--aviso)}
 .ae{font-size:13.5px}
 .ae small{display:block;color:var(--suave);margin-top:3px;font-size:12.5px}
 .detalle{display:none;padding:0 14px 14px;border-top:1px solid var(--linea)}
 .detalle.on{display:block}
 .sub{font-size:12px;text-transform:uppercase;letter-spacing:.4px;color:var(--suave);margin:14px 0 6px}
 ul{margin:0;padding-left:18px}
 li{margin:3px 0;font-size:13.5px}
 table{width:100%;border-collapse:collapse;font-size:13px}
 th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--linea);vertical-align:top}
 th{color:var(--suave);font-weight:600;font-size:11.5px;text-transform:uppercase}
 .mom{border-radius:4px;padding:1px 7px;font-size:11.5px;white-space:nowrap;color:#fff}
 .m-conexion{background:#4c6ef5}.m-adquisicion{background:#0b7285}
 .m-aplicacion{background:#2d6a4f}.m-discusion{background:#9c6644}.m-reflexion{background:#5f3dc4}
 .val{font-size:13px;padding:5px 0}
 .val b{font-family:ui-monospace,monospace}
 .si{color:var(--ok)}.no{color:var(--aviso)}
 .vacio{color:var(--suave);font-style:italic;font-size:13.5px}
</style></head><body>
<header><b>Diseño instruccional — Escuela de Minería</b><span id="hdr"></span></header>
<div class="cols"><aside><div class="filtros" id="filtros"></div><div id="lista"></div></aside>
<main id="main"></main></div>
<script>
const D = __DATOS__;
const $ = (s)=>document.querySelector(s);
const esc = (t)=>(t||"").replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
let carrera = "Todas", cursoSel = null;

const porCurso = (t,id)=> (D[t]||[]).filter(r=>r.curso_id===id);
const sesionesDe = (id)=> porCurso("sesiones",id).sort((a,b)=>+a.nro_sesion-+b.nro_sesion);
const contenidosDe = (sid)=> (D.contenidos||[]).filter(r=>r.sesion_id===sid);
const laminasDe = (sid)=> (D.laminas||[]).filter(r=>r.sesion_id===sid).sort((a,b)=>+a.orden-+b.orden);
const imagen = (iid)=> (D.imagenes||[]).find(r=>r.imagen_id===iid);

function pintarLista(){
  const cs = D.cursos.filter(c=> carrera==="Todas" || c.sigla===carrera);
  const mods = {};
  cs.forEach(c=> (mods[c.modulo||"—"] = mods[c.modulo||"—"]||[]).push(c));
  $("#lista").innerHTML = Object.entries(mods).map(([m,l])=>
    `<div class="modulo">${esc(m)}</div>` + l.map(c=>{
      const n = sesionesDe(c.curso_id).length;
      return `<div class="curso ${c.curso_id===cursoSel?'on':''}" onclick="verCurso('${c.curso_id}')">
        ${esc(c.nombre_curso)}<small>${c.sigla} · ${c.horas_total} h · ${n?n+' sesiones':'solo ficha'}</small></div>`;
    }).join("")).join("");
  $("#hdr").textContent = `${cs.length} cursos`;
}

function validar(id){
  const ses = sesionesDe(id), ev = porCurso("evaluaciones",id);
  const conts = ses.flatMap(s=>contenidosDe(s.sesion_id));
  const inds = (D.indicadores||[]).filter(i=> porCurso("capacidades",id).some(c=>c.capacidad_id===i.capacidad_id));
  const peso = ev.reduce((a,e)=>a+(parseFloat(e.peso)||0),0);
  const sinAE = ses.filter(s=>s.tipo_sesion==="adquisicion" && !s.aprendizaje_esperado).length;
  const indSinUso = inds.filter(i=> !conts.some(c=>c.indicador_id===i.indicador_id)).length;
  const lam = ses.flatMap(s=>laminasDe(s.sesion_id));
  const ESQUELETO = 10, TEORIA_MAX = 13;   // formato fijo del PPT 004A
  const excedidas = ses.filter(x=>laminasDe(x.sesion_id).length > 34).length;
  const teoriaMal = ses.filter(x=>laminasDe(x.sesion_id)
      .filter(y=>y.momento==="adquisicion").length > TEORIA_MAX).length;
  const malMin = ses.filter(s=>{const l=laminasDe(s.sesion_id);
      return l.length && l.reduce((a,x)=>a+(+x.minutos||0),0)!==135;}).length;
  const imgSinVer = lam.filter(l=>l.imagen_id && (imagen(l.imagen_id)||{}).estado!=="verificada").length;
  return [
    ["Los pesos de evaluación suman 100 %", ev.length? Math.round(peso)===100 : null, `${peso} %`],
    ["Toda sesión de adquisición tiene aprendizaje esperado", sinAE===0, `${sinAE} sin`],
    ["Todo contenido apunta a un indicador válido",
       conts.length? conts.every(c=>inds.some(i=>i.indicador_id===c.indicador_id)) : null, `${conts.length} contenidos`],
    ["Cada indicador se trabaja en algún contenido", inds.length? indSinUso===0 : null, `${indSinUso} sin trabajar`],
    ["Cada sesión suma 135 min", lam.length? malMin===0 : null, `${malMin} fuera`],
    ["Ninguna sesión pasa de 34 diapositivas", lam.length? excedidas===0 : null, `${excedidas} exceden`],
    ["La teoría no pasa de 13 diapositivas", lam.length? teoriaMal===0 : null, `${teoriaMal} exceden`],
    ["Ninguna lámina usa una imagen sin verificar", lam.length? imgSinVer===0 : null, `${imgSinVer} sin verificar`],
  ];
}

function verCurso(id){
  cursoSel = id; pintarLista();
  const c = D.cursos.find(x=>x.curso_id===id);
  const caps = porCurso("capacidades",id);
  const inds = (D.indicadores||[]).filter(i=>caps.some(x=>x.capacidad_id===i.capacidad_id));
  const ses = sesionesDe(id);
  const casos = porCurso("casos",id);
  const obs = porCurso("observaciones",id);

  let h = `<h1>${esc(c.nombre_curso)}</h1><div class="meta">${esc(c.carrera)} · ${esc(c.modulo)} ·
    Ciclo ${c.ciclo} · ${c.horas_total} h · ${c.creditos} cr · ${c.tipo}</div>`;

  if(caps.length){
    h += `<h2>Capacidad e indicadores</h2><div class="caja">`;
    caps.forEach(k=> h += `<div style="margin-bottom:8px">${esc(Object.values(k).slice(-1)[0])}</div>`);
    inds.forEach((i,n)=> h += `<div class="ind"><b>IND-${n+1}</b> · ${esc(Object.values(i).slice(-1)[0])}</div>`);
    h += `</div>`;
  }

  h += `<h2>Validaciones</h2><div class="caja">` + validar(id).map(([t,ok,d])=>
    `<div class="val">${ok===null?'<span style="color:#adb5bd">○</span>':
      ok?'<span class="si">✔</span>':'<span class="no">✘</span>'} ${t}
      <b style="color:var(--suave);font-size:12px"> ${d}</b></div>`).join("") + `</div>`;

  h += `<h2>Sesiones</h2>`;
  if(!ses.length) h += `<div class="vacio">Este curso tiene solo la ficha: aún no se ha detallado el diseño.</div>`;
  ses.forEach(s=>{
    const cts = contenidosDe(s.sesion_id), lms = laminasDe(s.sesion_id);
    const ev = s.tipo_sesion!=="adquisicion";
    h += `<div class="ses"><div onclick="this.nextElementSibling.classList.toggle('on')">
      <span class="n ${ev?'ev':''}">S${s.nro_sesion}</span>
      <div class="ae"><b>${esc(s.tema)}</b><small>${esc(s.aprendizaje_esperado)}</small></div></div>
      <div class="detalle">`;
    if(cts.length){
      h += `<div class="sub">Puntos clave</div><ul>` +
        cts.map(x=>`<li>${esc(x.contenido)}</li>`).join("") + `</ul>`;
    }
    const caso = casos.find(k=>k.bloque_id===s.bloque_id);
    if(ev && caso) h += `<div class="sub">Evaluación · caso del bloque</div>
      <div style="font-size:13.5px">${esc(Object.values(caso).slice(-2)[0])}</div>`;
    if(lms.length){
      const tot = lms.reduce((a,x)=>a+(+x.minutos||0),0);
      const dia = lms.length;   // una fila = una diapositiva
      h += `<div class="sub">Guion del PPT — ${dia} diapositivas · ${tot} min
</div>
        <table><tr><th>#</th><th>Tipo</th><th>Momento</th><th>min</th><th>Diapositiva</th><th>Imagen</th></tr>` +
        lms.map(l=>{
          const im = imagen(l.imagen_id);
          return `<tr><td>${l.orden}</td>
            <td><b style="font-size:11.5px">${esc(l.tipo||"")}</b></td>
            <td>${l.momento? `<span class="mom m-${l.momento}">${l.momento}</span>`:""}</td>
            <td>${l.minutos}</td>

            <td><b>${esc(l.titulo)}</b><br><span style="color:var(--suave)">${esc(l.texto)}</span></td>
            <td>${im? esc(im.tema)+(im.estado==="verificada"?' <span class="si">✔</span>':' <span class="no">sin verificar</span>')
                    : '<span style="color:#ced4da">—</span>'}</td></tr>`;
        }).join("") + `</table>`;
    }
    h += `</div></div>`;
  });

  if(obs.length){
    h += `<h2>Observaciones registradas</h2><div class="caja">` + obs.map(o=>{
      const v = Object.values(o);
      return `<div class="val">${o.estado==="corregido"?'<span class="si">✔</span>':'<span class="no">●</span>'}
        <b style="font-size:12px">${esc(o.tipo)}</b> ${esc(v[v.length-2])}</div>`;
    }).join("") + `</div>`;
  }
  $("#main").innerHTML = h;
}

$("#filtros").innerHTML = ["Todas","EOM","SI","PM"].map(c=>
  `<button onclick="carrera='${c}';document.querySelectorAll('.filtros button').forEach(b=>b.classList.remove('on'));event.target.classList.add('on');pintarLista()"
   class="${c==='Todas'?'on':''}">${c}</button>`).join("");
pintarLista();
$("#main").innerHTML = `<h1>Elige un curso</h1><div class="meta">
  La lista de la izquierda tiene los cursos técnicos de las tres carreras.
  Al abrir uno se ven su capacidad, sus sesiones y —si está detallado— el guion de cada PPT.</div>`;
</script></body></html>"""

salida = RAIZ / "Visor.html"
salida.write_text(HTML.replace("__DATOS__", json.dumps(datos, ensure_ascii=False)),
                  encoding="utf-8")
print(f"Visor.html regenerado ({salida.stat().st_size // 1024} KB)")
for t in TABLAS:
    print(f"  {t:<18} {len(datos[t]):>4} filas")
