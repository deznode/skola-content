# {{COURSE_TITLE}}

{{BRIEF_DESCRIPTION}}

## Kuzé ki Bu Ta Prendi

{{LEARNING_OBJECTIVES}}

## Pre-rekizitus

{{PREREQUISITES}}

## Estrutura di Kursu

```
courses/{{COURSE_SLUG}}/
├── course.yaml
├── cheatsheet-{{LANG}}.md
├── lessons/
│   ├── {{LESSON_1_SLUG}}/
│   │   └── {{LANG}}.mdx
│   ├── {{LESSON_2_SLUG}}/
│   │   └── {{LANG}}.mdx
│   └── ...
├── code/
│   ├── start/                 # Skafólding ku TODO
│   └── final/                 # Solusons kompletu
├── infographics/              # Imajen edukatival
└── microlearn/                # Konteúdu kurtu
```

## Módulus

{{MODULES_TABLE}}

## Manera di Uza

### Pa Prinsipianti (Rekomendadu)

1. **Kumesa ku primeiru lison** — Abri `lessons/{{LESSON_1_SLUG}}/{{LANG}}.mdx`
2. **Segui lisons na orden** — Kada diretóriu di lison tem un fixeru `.mdx`
3. **Uza kódigu di start** — Troka komentáriu TODO ku bu implementason
4. **Kompara ku solusons** — Xeka `code/final/` si bu fikâ prisu

### Pa Referénsia Rápidu

- **Cheatsheet**: `cheatsheet-{{LANG}}.md` — Referénsia di kursu interu
- **Slides**: `slides-{{LANG}}/` — Kori `pnpm dev` pa prezentason

## Kódigu

### Kumesa ku skafólding

```bash
cd code/start
{{START_COMMAND}}
```

### Solusons kompletu

```bash
cd code/final
{{FINAL_COMMAND}}
```

{{#DOCKER_SECTION}}
### Bazi di dadus lokal

```bash
cd code/docker
docker compose up -d
```
{{/DOCKER_SECTION}}

{{#SLIDES_SECTION}}
## Prezentason Slides

```bash
cd slides-{{LANG}}
pnpm install
pnpm dev          # Servidor lokal na http://localhost:3030
pnpm build        # Kompila pa HTML státiku
pnpm export-pdf   # Esporta pa PDF
```
{{/SLIDES_SECTION}}

## Rekursus Adisional

- **Cheatsheet**: [`cheatsheet-{{LANG}}.md`](cheatsheet-{{LANG}}.md)
- **Infografikus**: [`infographics/`](infographics/)
{{#HAS_SLIDES}}- **Prezentason**: [`slides-{{LANG}}/`](slides-{{LANG}}/){{/HAS_SLIDES}}
{{#HAS_MICROLEARN}}- **Mikrolearn**: [`microlearn/`](microlearn/){{/HAS_MICROLEARN}}

## Problema Komun

{{TROUBLESHOOTING}}

---

*Skola.dev - Nu ta kria djuntu!*
