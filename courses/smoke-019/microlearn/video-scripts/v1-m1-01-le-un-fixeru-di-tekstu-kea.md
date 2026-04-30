---
trace_id: Skola-video_script-smoke-019-2026-04-29-fixerus-na-python-le-un-fixeru-di-tekstu
topic: smoke-019
module: fixerus-na-python
lesson: le-un-fixeru-di-tekstu
kind: video_script
language: kea
generated_at: 2026-04-29T14:31:32.230Z
---

# Skript di Vídeu — Lê un Fixeru di Tekstu

**Durason**: ~90 segundus
**Nível**: Principianti
**Língua**: Kabuverdianu (kea)

---

## [00:00 – 00:08] Introduson

> 🎬 *Visual: Logo Python + ikon di fikxeru di tekstu*

**Narason:**
"Bon dia! Na es lisaun nos ta aprendê kumu ki Python ta abri é lê fikserus di tekstu — di forma sigura, riketu, é ku karatéris kea koretus."

---

## [00:08 – 00:22] Kuzé ki é `open()`?

> 🎬 *Visual: Ekran parti — kódigo na eskuerda, animason di fikxeru na direita*

**Narason:**
"Kuandu bu ta xama `open()`, Python ta volta un ojetu ki nos ta xama 'file handle' — kuma un janela aberta pa kel fikxeru. Bu ta podi lê konteúdu atravês di kel janela."

> 🎬 *Visual: Mosta `f = open("mensajen.txt", "r", encoding="utf-8")`*

"Nota ki nos ta mete trés argumentus: nómi di fikxeru, modu `\"r\"` pa 'ler', é `encoding=\"utf-8\"` — kel últimu é muito importante pa línguas kuma kea."

---

## [00:22 – 00:45] `read()` kontra `readlines()`

> 🎬 *Visual: Tábua di konparasaun animada — `read()` vs `readlines()` vs `readline()`*

**Narason:**
"Python ten trés métudus pa lê fikserus. `read()` ta volta totu konteúdu kumu un string — útis pa fikserus pikininus. `readlines()` ta volta un lista di linhas — melhor pa prosesa linha pa linha. É `readline()` — nota o 's' singuler — ta lê sô un linha di vês."

---

## [00:45 – 01:10] Deklarason `with` — A Manera Segura

> 🎬 *Visual: Diagrama di fluxu — 4 pasos di siklus di vida di `with`*

**Narason:**
"Agora, a manera mais segura di trabadja ku fikserus é atravês di deklarason `with`. El ta garanti ki fikxeru ta txada otomatikamenti — átxi si un eróru akontesi."

> 🎬 *Visual: Kódigo animadu — bloku `with open(...) as f:` ku loop `for linha in f.readlines()`*

"Bu ta vê: abri fikxeru, itera pa kada linha, xama `.strip()` pa tirar espasos i `\\n` di kabo — é fikxeru ta txada sozinhu kuandu bloku fika."

---

## [01:10 – 01:25] Dika Enkodifikason

> 🎬 *Visual: Dós skrens — un ku karatéris estranhus, otru ku tekstu korretu*

**Narason:**
"`encoding=\"utf-8\"` ta garanti ki letras kea kumu `ã`, `ê`, `ó`, é `ç` ta aparese koretu. Skisi kel parâmetru é bu ta vê... lixu na ekran!"

---

## [01:25 – 01:30] Resumu é CTA

> 🎬 *Visual: Buletin list animadu*

**Narason:**
"Pa resumir: uza `open()` ku modu `\"r\"` é `encoding=\"utf-8\"`, sempri dentru di bloku `with`, é eskólhi `readlines()` pa prosesa linha pa linha. Na prósima lisaun — nos ta aprendê kumu **skrebe** é **juntar** na fikserus. Té lógu!"

---

## Notas di Produson

- **Kódigo**: Sintaks-iluminadu, fundi skuru (tema Dracula ou One Dark)
- **Animason**: Karatéris di kea ku tilhis debi mostra koretu na ekran — verifikadu antes di renderizason
- **Legendas**: Kabuverdianu (kea), ativadu pa padrón
- **B-roll**: Skren di terminal ku saída real di Python 3.11+
