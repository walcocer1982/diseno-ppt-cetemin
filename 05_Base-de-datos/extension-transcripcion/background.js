// Boton de la barra: guarda la transcripcion del video abierto.
//
// No hace NINGUNA peticion a YouTube. Lee el panel de transcripcion que ya esta
// en la pantalla y lo guarda como archivo. Por eso funciona aunque la API este
// devolviendo 429: no hay nada que bloquear, porque no se pide nada.

const CARPETA = "cetemin-transcripciones";

// Esta funcion se inyecta en la pagina de YouTube y corre alli.
async function extraer() {
  const espera = (ms) => new Promise((r) => setTimeout(r, ms));

  const segmentos = () =>
    document.querySelectorAll("ytd-transcript-segment-renderer");

  // Si el panel no esta abierto, se intenta abrir buscando el boton por su
  // texto -- sirve con la interfaz en espanol y en ingles.
  if (segmentos().length === 0) {
    const candidatos = [...document.querySelectorAll("button, tp-yt-paper-button, yt-button-shape button")];
    const boton = candidatos.find((b) => {
      const t = ((b.getAttribute("aria-label") || "") + " " + (b.textContent || "")).toLowerCase();
      return t.includes("transcripci") || t.includes("transcript");
    });
    if (boton) {
      boton.click();
      for (let i = 0; i < 20 && segmentos().length === 0; i++) await espera(300);
    }
  }

  const segs = segmentos();
  if (segs.length === 0) {
    return {
      error:
        "No encuentro la transcripcion. Abrela a mano: en la descripcion del " +
        "video, boton 'Mostrar transcripcion'. Luego vuelve a pulsar aqui.",
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
    return { error: "El panel esta abierto pero no pude leer las lineas." };
  }

  const id = new URL(location.href).searchParams.get("v") || "video";
  const titulo = (document.querySelector("h1 yt-formatted-string, h1")?.textContent || "").trim();
  const canal = (document.querySelector("ytd-channel-name a")?.textContent || "").trim();

  // Idioma: si el panel trae selector, se avisa de cual esta activo. Copiar un
  // video en ingles sin cambiar el idioma es el error facil de cometer.
  const selector = document.querySelector(
    "ytd-transcript-footer-renderer #label, ytd-transcript-footer-renderer yt-dropdown-menu"
  );
  const idioma = selector ? selector.textContent.replace(/\s+/g, " ").trim() : "";

  // Las lineas de cabecera empiezan por '#' y videos_yt.py las ignora: solo
  // lee las que tienen marca de tiempo.
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
    idioma,
    n: lineas.length,
    contenido: cabecera.concat(lineas).join("\n"),
  };
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
    aviso(tab.id, res ? res.error : "No obtuve nada.");
    return;
  }

  const url =
    "data:text/plain;charset=utf-8," + encodeURIComponent(res.contenido);

  chrome.downloads.download(
    {
      url,
      filename: `${CARPETA}/${res.id}.txt`,
      saveAs: false,
      conflictAction: "overwrite",
    },
    () => {
      const err = chrome.runtime.lastError;
      if (err) {
        aviso(tab.id, "No se pudo guardar: " + err.message);
        return;
      }
      aviso(
        tab.id,
        `Guardado: Descargas\\${CARPETA}\\${res.id}.txt\n` +
          `${res.n} líneas` +
          (res.idioma ? `\nPista: ${res.idioma}` : "") +
          `\n\nSi el video es en inglés y querías español, cambia el idioma en ` +
          `el panel de transcripción y vuelve a pulsar.\n\n` +
          `Cargar con:\n  python videos_yt.py pegar ${res.id} <archivo>`
      );
    }
  );
});
