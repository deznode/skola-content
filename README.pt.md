<!--
title: Conteúdo Skola
slug: readme
language: pt
-->

![Conteúdo Skola.dev](./assets/banner-pt.svg)

[🇨🇻 Kriolu](./README.md) · **🇵🇹 Português** · [🇬🇧 English](./README.en.md)

# Conteúdo Skola.dev

Conteúdo educativo e exemplos de código para [Skola.dev](https://skola.dev) — ensinando programação, desenvolvimento cloud-native e IA em Crioulo Cabo-verdiano.

## Estrutura do Repositório

Este repositório contém **conteúdo publicado e revisto**, organizado por curso. O conteúdo é criado através do pipeline [skola-research](https://github.com/deznode/skola-research) e publicado aqui como o resultado público.

Todo o conteúdo está organizado em **modo Curso** — cursos estruturados com módulos, lições individuais e materiais de apoio, sob `courses/{slug}/`.

### Cursos

| Curso | Lições | Línguas | Descrição |
|-------|--------|---------|-----------|
| [intro-python](./courses/intro-python/) | 32 | kea | Introdução completa ao Python (iniciante) |
| [web-foundations](./courses/web-foundations/) | 19 | kea | Fundamentos da web: HTML e CSS (iniciante) |

### Blog

| Localização | Descrição |
|-------------|-----------|
| [blog/drafts/](./blog/drafts/) | Posts de blog em progresso |
| [blog/published/](./blog/published/) | Posts de blog publicados |

## Estrutura do Curso

Cada curso segue este layout:

```
courses/{slug}/
├── course.yaml                # Manifesto do curso (módulos, lições, metadados)
├── cheatsheet-{lang}.md       # Cheatsheet de referência (um por língua)
├── lessons/                   # Lições individuais
│   └── {lessonSlug}/
│       ├── kea.mdx            # Lição em Crioulo
│       └── pt.mdx             # Lição em Português (se disponível)
├── code/                      # Exemplos de código (neutro de língua)
│   ├── start/                 # Esqueleto inicial com TODOs
│   └── final/                 # Solução completa e funcional
├── infographics/              # Recursos visuais (PNGs)
├── microlearn/                # Conteúdo curto
│   ├── video-scripts/         # Scripts de vídeo 60-90s
│   ├── micro-blogs/           # Posts de 100-250 palavras
│   ├── seo/                   # Metadados SEO (YAML)
│   └── thumbnails/            # Briefs de thumbnail
├── manifest.md                # Inventário de recursos publicados
└── CHANGELOG.md               # Histórico de alterações
```

**Relação-chave**: `code/final/` é a fonte da verdade. `code/start/` é derivado dele, com a implementação removida e TODOs adicionados.

## Utilização

### Para Estudantes

Clona este repositório para obter todo o conteúdo e código:

```bash
git clone https://github.com/deznode/skola-content.git
cd skola-content
```

#### Seguir um Curso

1. Navega até ao curso e começa pela primeira lição:
   ```bash
   cd courses/intro-python/lessons/01-o-ki-e-python
   cat kea.mdx
   ```

2. Trabalha as lições em sequência — cada diretório está numerado

3. Usa o código inicial junto com as lições:
   ```bash
   cd courses/intro-python/code/start
   ```

4. Consulta a solução completa quando precisares:
   ```bash
   cd courses/intro-python/code/final
   ```

#### Usar Cheatsheets

Referência rápida para um curso inteiro:
```bash
cat courses/intro-python/cheatsheet-kea.md
```

## Suporte de Línguas

- **Principal**: Crioulo Cabo-verdiano (`kea`)
- **Secundário**: Português (`pt`), Inglês (`en`)

O conteúdo é criado primeiro em Crioulo, com as traduções a seguir. Os termos técnicos permanecem em Inglês quando não existe tradução direta.

## Contribuir

### Adicionar um Novo Curso

1. Cria o diretório do curso sob `courses/`:
   ```bash
   mkdir -p courses/{slug}/lessons
   ```

2. Cria `course.yaml` com os metadados do curso (título, módulos, lições)

3. Cria os ficheiros de lição: `courses/{slug}/lessons/{lessonSlug}/kea.mdx`
   - Cada lição requer frontmatter: `title`, `language`, `courseSlug`, `lessonSlug`

4. Adiciona exemplos de código em `code/start/` e `code/final/`
   - `code/final/` é a fonte da verdade
   - `code/start/` é derivado com a implementação removida e TODOs adicionados

5. Adiciona materiais de apoio conforme necessário:
   - `cheatsheet-kea.md` — Referência rápida para o curso inteiro
   - `infographics/` — Diagramas visuais (PNG)
   - `microlearn/` — Conteúdo curto (scripts de vídeo, micro-blogs)

6. Cria `manifest.md` com a lista de todos os recursos publicados

### Nomenclatura de Ficheiros

- Lições: `courses/{slug}/lessons/{lessonSlug}/{lang}.mdx`
- Cheatsheets: `courses/{slug}/cheatsheet-{lang}.md`
- Posts de blog: `blog/{status}/{date}-{slug}.mdx`

## Licença

Licença MIT.

---

**Nu ta kria djuntu!** (Construímos juntos!)
