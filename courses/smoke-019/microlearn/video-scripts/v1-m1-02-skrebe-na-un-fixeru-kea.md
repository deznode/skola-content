---
trace_id: Skola-video_script-smoke-019-2026-04-29-fixerus-na-python-skrebe-na-un-fixeru
topic: smoke-019
module: fixerus-na-python
lesson: skrebe-na-un-fixeru
kind: video_script
language: kea
generated_at: 2026-04-29T14:33:15.483Z
---

# Skript di Vídeu — Skrebe na un Fixeru

**Durason**: ~90 segundus
**Nível**: Principianti
**Língua**: Kabuverdianu (kea)

---

## [00:00 – 00:08] Introduson

> 🎬 *Visual: Ikon di fikxeru ku seta di "skreva" entrandu neli*

**Narason:**
"Na lisaun anterior nos aprendê kumu lê fikserus. Agora nos ta aprendê kumu **skrebe** é **juntar** tekstu na fikserus — dós operasons ki bu ta uza tudu dia."

---

## [00:08 – 00:30] Modu `"w"` — Skreva (ku Avertencia!)

> 🎬 *Visual: Ekran parti — kódigo eskerda, animason di fikxeru direita. Animason: fikxeru existenti ta "apagadu" — afektu visual di destruison — depôs kria novu.*

**Narason:**
"Modu `\"w\"` ta abri un fikxeru pa skreva. Si kel fikxeru já existe... atensiun! Totu konteúdu anterior ta apagadu imediatamente. É pa kel ki nos ta txama el 'modu destrutivu' kuandu bus kun tentu."

> 🎬 *Visual: Kódigo animadu — `with open("resultado.txt", "w", encoding="utf-8") as f:` ku dós `f.write()` khamadus*

"Note ki `write()` nun ta mete `\\n` otomatikamente — bu ta devê meti manualmente na fin di kada liña."

---

## [00:30 – 00:52] Modu `"a"` — Juntar (Seguru)

> 🎬 *Visual: Animason — fikxeru ku konteúdu existenti, é un nova liña ta "pusa" na fin sem apagá retu*

**Narason:**
"Modu `\"a\"` — di 'append', ou 'juntar' — ta adisiona konteúdu na **fin** di fikxeru sen tukâ ki já staba li. El ta kria fikxeru si nun existe, ou ta juntar si já existe. Ideal pa logs é rejistus."

> 🎬 *Visual: Mesmo fikxeru `resultado.txt` — agora ku un nova liña juntada*

---

## [00:52 – 01:10] A Bug Más Famosa — Falta di `\n`

> 🎬 *Visual: Dós skrens lado a lado — "Eradu" vs "Koretu"*

**Narason:**
"El é un di kes bugs más komuns pa principiantis: skisi di mete `\\n` na fin di liña. Sem el, tódu liñas ta funde nuni mesmu bloku di tekstu. Un simples barra-n ta resolve tudo!"

> 🎬 *Visual: Zoom na `\n` ku sirkulasaun animada*

---

## [01:10 – 01:25] Ekzemplu Kompletu

> 🎬 *Visual: Ekran cheiu di kódigo — 3 blokus `with`: skreva, juntar, verifikadu*

**Narason:**
"El é un fluxu típiku: primeiro, kria fikxeru ku `\"w\"`. Depôs, juntar novas entradas ku `\"a\"`. É no fin, lê el ku `\"r\"` pa verifikadu. Trés operasons, mesmu padrón `with`."

---

## [01:25 – 01:30] Resumu é CTA

> 🎬 *Visual: Karta rezumu animadu*

**Narason:**
"Pa resumir: `\"w\"` pa kria/sobreskribi, `\"a\"` pa juntar sen destrui, é sempri `\\n` na fin di kada liña. Agora bu ten tódu habilidades básikus di fikserus na Python. Prósimu nivel — CSV é JSON. Té lógu!"

---

## Notas di Produson

- **Efeitu visual di destruison** pa modu `"w"`: ikóns di ficheiros ku animason flash vermelho antes di desaparecer — reforsa perigo visual
- **Destake di `\n`**: Mostra karatér literalmente renderizadu no side-by-side, não escapado
- **Kódigo**: Sintaks-iluminadu, tema Dracula
- **Legendas**: Kabuverdianu (kea), ativadu pa padrón
