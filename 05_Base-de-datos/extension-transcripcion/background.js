// Boton de la barra: guarda la transcripcion del video abierto.
//
// No hace NINGUNA peticion a YouTube. Lee el panel de transcripcion que ya esta
// en la pantalla y lo guarda como archivo. Por eso funciona aunque la API este
// devolviendo 429: no hay nada que bloquear, porque no se pide nada.
//
// El archivo sale como  Canal_Titulo-del-video_<id>.txt
// El id va al final y no se quita: es la clave con la que videos.csv y
// videos_yt.py identifican el video, y dos canales pueden subir el mismo
// titulo. Pero puesto al final se lee de izquierda a derecha y se reconoce.

const CARPETA = "cetemin-transcripciones";
const ESPERA_MAX = 20000;   // ms que se aguarda a que carguen las lineas

// Esta funcion se inyecta en la pagina de YouTube y corre alli.
async function extraer() {
  const espera = (ms) => new Promise((r) => setTimeout(r, ms));
  const segmentos = () =>
    document.querySelectorAll("ytd-transcript-segment-renderer");
  const panelAbierto = () =>
    !!document.querySelector("ytd-transcript-renderer, ytd-transcript-search-panel-renderer");

  const LIMITE = 20000;

  // Solo se pulsa el boton si el panel NO esta abierto: si ya lo esta, el clic
  // lo cerraria en vez de abrirlo.
  if (!panelAbierto()) {
    const candidatos = [
      ...document.querySelectorAll("button, tp-yt-paper-button, yt-button-shape button"),
    ];
    const boton = candidatos.find((b) => {
      const t =
        ((b.getAttribute("aria-label") || "") + " " + (b.textContent || "")).toLowerCase();
      return t.includes("transcripci") || t.includes("transcript");
    });
    if (!boton) {
      return {
        codigo: "SIN_BOTON",
        error:
          "Este video no ofrece transcripción: no encuentro el botón " +
          "«Mostrar transcripción» en la descripción.\n\n" +
          "El canal no puso subtítulos. Descarta este video, o transcribe el " +
          "audio con faster-whisper si vale mucho la pena.",
      };
    }
    boton.click();
  }

  // Se aguarda a que aparezcan las lineas, comprobando; no un tiempo fijo.
  // Un video largo o una conexion lenta tardan mas que unos pocos segundos.
  const t0 = Date.now();
  while (segmentos().length === 0 && Date.now() - t0 < LIMITE) {
    await espera(300);
  }

  const segs = segmentos();

  // Los dos fallos no son el mismo y no deben decir lo mismo.
  if (segs.length === 0) {
    if (panelAbierto()) {
      return {
        codigo: "PANEL_VACIO",
        error:
          "El panel de transcripción está abierto pero YouTube no cargó el " +
          "texto.\n\nPrueba a recargar la página (F5), abrir la transcripción " +
          "y volver a pulsar.\n\nSi sigue vacío, es este video en concreto: " +
          "pasa sobre todo con los que tienen doblaje automático. Cambia de " +
          "video antes que de método.",
      };
    }
    return {
      codigo: "PANEL_CERRADO",
      error:
        "No se abrió el panel de transcripción.\n\nÁbrelo a mano: en la " +
        "descripción del video, botón «Mostrar transcripción». Luego vuelve " +
        "a pulsar aquí.",
    };
  }

  const lineas = [];
  for (const s of segs) {
    const t = s.querySelector(".segment-timestamp, [class*='segment-timestamp']");
    const x = s.querySelector(".segment-text, [class*='segment-text']");
    if (!t || !x) continue;
    const marca = t.textContent.trim();
    const texto = x.textContent.replace(/\s+/g, " ").trim();
    if (marca && texto) lineas.push(`${marca}  ${texto}`);
  }

  if (lineas.length === 0) {
    return {
      codigo: "SIN_LINEAS",
      error:
        "Encontré el panel y sus bloques, pero no pude leer el texto.\n\n" +
        "Probablemente YouTube cambió el diseño del panel. Avisa para " +
        "ajustar la extensión.",
    };
  }

  const id = new URL(location.href).searchParams.get("v") || "video";
  const titulo = (
    document.querySelector("h1 yt-formatted-string, h1")?.textContent || ""
  ).trim();
  const canal = (
    document.querySelector("ytd-channel-name a")?.textContent || ""
  ).trim();

  // Idioma: copiar un video en ingles sin cambiar el idioma del panel es el
  // error facil de cometer, asi que se registra cual estaba activo.
  const pie = document.querySelector("ytd-transcript-footer-renderer");
  const idioma = pie ? pie.textContent.replace(/\s+/g, " ").trim() : "";

  // Las lineas de cabecera empiezan por '#' y videos_yt.py las ignora, salvo
  // `video_id`, de donde saca el id sin que haya que teclearlo.
  const cabecera = [
    `# video_id: ${id}`,
    `# url: https://youtu.be/${id}`,
    `# titulo: ${titulo}`,
    `# canal: ${canal}`,
    idioma ? `# pista: ${idioma}` : "# pista: (sin selector visible)",
    `# copiado: ${new Date().toISOString().slice(0, 10)}`,
    `# lineas: ${lineas.length}`,
    "#",
    "# Esto es material del canal. Al cuadernillo va una SINTESIS NUESTRA con",
    "# marcas de tiempo, no este texto tal cual (ver §16).",
    "",
  ];

  return {
    id,
    titulo,
    canal,
    idioma,
    n: lineas.length,
    contenido: cabecera.concat(lineas).join("\n"),
  };
}

// Windows no admite \ / : * ? " < > | en un nombre de archivo, y un nombre
// larguisimo estorba mas de lo que ayuda.
function limpiar(txt, tope) {
  return (txt || "")
    .replace(/[\\/:*?"<>|]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, tope);
}

function aviso(tabId, texto) {
  chrome.scripting.executeScript({
    target: { tabId },
    func: (t) => alert(t),
    args: [texto],
  });
}

chrome.action.onClicked.addListener(async (tab) => {
  if (!tab.url || !tab.url.includes("youtube.com/watch")) {
    aviso(tab.id, "Abre primero la página de un video de YouTube.");
    return;
  }

  let res;
  try {
    const r = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: extraer,
    });
    res = r[0].result;
  } catch (e) {
    aviso(tab.id, "No pude leer la página: " + e.message);
    return;
  }

  if (!res || res.error) {
    aviso(tab.id, res ? res.error : "No obtuve nada de la página.");
    return;
  }

  const canal = limpiar(res.canal, 25);
  const titulo = limpiar(res.titulo, 50);
  const nombre = [canal, titulo, res.id].filter(Boolean).join("_") + ".txt";

  const url = "data:text/plain;charset=utf-8," + encodeURIComponent(res.contenido);

  chrome.downloads.download(
    {
      url,
      filename: `${CARPETA}/${nombre}`,
      saveAs: false,
      conflictAction: "overwrite",
    },
    () => {
      const err = chrome.runtime.lastError;
      if (err) {
        aviso(tab.id, "No se pudo guardar: " + err.message);
        return;
      }
      const enIngles = /ingl[eé]s|english/i.test(res.idioma || "");
      aviso(
        tab.id,
        `Guardado (${res.n} líneas):\n` +
          `Descargas\\${CARPETA}\\${nombre}\n\n` +
          (res.idioma ? `Pista: ${res.idioma}\n` : "") +
          (enIngles
            ? "\nOJO: está en INGLÉS. Si lo querías en español, cambia el " +
              "idioma en el panel de transcripción y vuelve a pulsar — se " +
              "sobrescribe.\n"
            : "") +
          `\nCargar con:\n  python videos_yt.py pegar "<archivo>"`
      );
    }
  );
});
