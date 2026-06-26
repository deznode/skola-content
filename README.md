<!--
title: Kontiudu Skola
slug: readme
language: kea
-->

![Kontiudu Skola.dev](./assets/banner-kea.svg)

**🇨🇻 Kriolu** · [🇵🇹 Portugues](./README.pt.md) · [🇬🇧 English](./README.en.md)

# Kontiudu Skola.dev

Kontiudu edukativu i izenplus di kódiku pa [Skola.dev](https://skola.dev) — pa nsina programasan, dizenvolvimentu cloud-native, i IA na Kriolu Kabuverdianu.

## Strutura di Repozitóriu

Es repozitóriu ten **kontiudu publikadu i finalizadu**, organizadu pa kursu. Kontiudu é kriadu através di pipeline [skola-research](https://github.com/deznode/skola-research) i é publikadu li komu rezultadu públiku.

Tudu kontiudu é organizadu na **modu Kursu** — kursu struturadu ku módulu, lisan individual, i material di apoiu, baxu `courses/{slug}/`.

### Kursu

| Kursu | Lisan | Língua | Diskrisan |
|-------|-------|--------|-----------|
| [intro-python](./courses/intro-python/) | 32 | kea | Introdusan kompletu a Python (prinsipianti) |
| [web-foundations](./courses/web-foundations/) | 19 | kea | Fundamentus di web: HTML i CSS (prinsipianti) |

### Blog

| Lokal | Diskrisan |
|-------|-----------|
| [blog/drafts/](./blog/drafts/) | Postu di blog na progresu |
| [blog/published/](./blog/published/) | Postu di blog publikadu |

## Strutura di Kursu

Kada kursu ta sigi es leiaute:

```
courses/{slug}/
├── course.yaml                # Manifestu di kursu (módulu, lisan, metadadus)
├── cheatsheet-{lang}.md       # Cheatsheet di referénsia (un pa kada língua)
├── lessons/                   # Lisan individual
│   └── {lessonSlug}/
│       ├── kea.mdx            # Lisan na Kriolu
│       └── pt.mdx             # Lisan na Portugues (si ten)
├── code/                      # Izenplu di kódiku (neutru di língua)
│   ├── start/                 # Skeletu inisial ku TODOs
│   └── final/                 # Solusan kompletu ki ta funsiona
├── infographics/              # Asetu vizual (PNGs)
├── microlearn/                # Kontiudu kurtu
│   ├── video-scripts/         # Skript di vídeu 60-90s
│   ├── micro-blogs/           # Postu di 100-250 palavra
│   ├── seo/                   # Metadadus SEO (YAML)
│   └── thumbnails/            # Brief di thumbnail
├── manifest.md                # Inventáriu di asetu publikadu
└── CHANGELOG.md               # Istóriku di mudansas
```

**Relasan xavi**: `code/final/` é fonti di verdadi. `code/start/` ta deriva di el, ku implementasan tiradu i TODOs adisionadu.

## Uzu

### Pa Studanti

Klona es repozitóriu pa pega tudu kontiudu i kódiku:

```bash
git clone https://github.com/deznode/skola-content.git
cd skola-content
```

#### Sigi un Kursu

1. Navega pa kursu i kumesa ku primeru lisan:
   ```bash
   cd courses/intro-python/lessons/01-o-ki-e-python
   cat kea.mdx
   ```

2. Sigi lisons pa órden — kada diretóriu ten un númeru

3. Uza kódiku inisial djuntu ku lisons:
   ```bash
   cd courses/intro-python/code/start
   ```

4. Odja solusan kompletu kantu bu meste:
   ```bash
   cd courses/intro-python/code/final
   ```

#### Uza Cheatsheet

Referénsia rápidu pa un kursu interu:
```bash
cat courses/intro-python/cheatsheet-kea.md
```

## Suporti di Língua

- **Prinsipal**: Kriolu Kabuverdianu (`kea`)
- **Sekundáriu**: Portugues (`pt`), Inglés (`en`)

Kontiudu é kriadu primeru na Kriolu, ku tradusan ta sigi dipos. Palavras tekniku ta fika na Inglés kantu ka ten tradusan diretu.

## Kontribui

### Adisiona un Kursu Nobu

1. Kria diretóriu di kursu baxu `courses/`:
   ```bash
   mkdir -p courses/{slug}/lessons
   ```

2. Kria `course.yaml` ku metadadus di kursu (títulu, módulu, lisan)

3. Kria fitxeru di lisan: `courses/{slug}/lessons/{lessonSlug}/kea.mdx`
   - Kada lisan ta meste frontmatter: `title`, `language`, `courseSlug`, `lessonSlug`

4. Adisiona izenplus di kódiku na `code/start/` i `code/final/`
   - `code/final/` é fonti di verdadi
   - `code/start/` ta deriva ku implementasan tiradu i TODOs adisionadu

5. Adisiona material di apoiu konfórmi nesesáriu:
   - `cheatsheet-kea.md` — Referénsia rápidu pa kursu interu
   - `infographics/` — Diagrama vizual (PNG)
   - `microlearn/` — Kontiudu kurtu (skript di vídeu, micro-blog)

6. Kria `manifest.md` ku lista di tudu asetu publikadu

### Nomeasan di Fitxeru

- Lisan: `courses/{slug}/lessons/{lessonSlug}/{lang}.mdx`
- Cheatsheet: `courses/{slug}/cheatsheet-{lang}.md`
- Postu di blog: `blog/{status}/{date}-{slug}.mdx`

## Lisensa

Lisensa MIT.

---

**Nu ta kria djuntu!**
