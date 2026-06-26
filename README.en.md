<!--
title: Skola Content
slug: readme
language: en
-->

[🇨🇻 Kriolu](./README.md) · [🇵🇹 Português](./README.pt.md) · **🇬🇧 English**

# Skola Content

Educational content and code samples for [Skola.dev](https://skola.dev) — teaching programming, cloud-native development, and AI in Cape Verdean Kriolu.

## Repository Structure

This repository contains **published, polished content** organized by course. Content is created through the [skola-research](https://github.com/deznode/skola-research) pipeline and published here as the public-facing output.

All content is organized in **Course mode** — structured courses with modules, individual lessons, and supporting materials, under `courses/{slug}/`.

### Courses

| Course | Lessons | Languages | Description |
|--------|---------|-----------|-------------|
| [intro-python](./courses/intro-python/) | 32 | kea | Complete Python introduction (beginner) |
| [web-foundations](./courses/web-foundations/) | 19 | kea | Web foundations: HTML & CSS (beginner) |

### Blog

| Location | Description |
|----------|-------------|
| [blog/drafts/](./blog/drafts/) | Blog posts in progress |
| [blog/published/](./blog/published/) | Published blog posts |

## Course Structure

Every course follows this layout:

```
courses/{slug}/
├── course.yaml                # Course manifest (modules, lessons, metadata)
├── cheatsheet-{lang}.md       # Reference cheatsheet (one per language)
├── lessons/                   # Individual lessons
│   └── {lessonSlug}/
│       ├── kea.mdx            # Kriolu lesson
│       └── pt.mdx             # Portuguese lesson (if available)
├── code/                      # Code samples (language-neutral)
│   ├── start/                 # Starter scaffolding with TODOs
│   └── final/                 # Complete working solution
├── infographics/              # Visual assets (PNGs)
├── microlearn/                # Short-form content
│   ├── video-scripts/         # 60-90s video scripts
│   ├── micro-blogs/           # 100-250 word posts
│   ├── seo/                   # SEO metadata (YAML)
│   └── thumbnails/            # Thumbnail briefs
├── manifest.md                # Published asset inventory
└── CHANGELOG.md               # Change history
```

**Key relationship**: `code/final/` is the source of truth. `code/start/` is derived from it with implementation stripped and TODOs added.

## Usage

### For Students

Clone this repository to get all content and code:

```bash
git clone https://github.com/deznode/skola-content.git
cd skola-content
```

#### Following a Course

1. Navigate to the course and start with the first lesson:
   ```bash
   cd courses/intro-python/lessons/01-o-ki-e-python
   cat kea.mdx
   ```

2. Work through lessons sequentially — each directory is numbered

3. Use the starter code alongside lessons:
   ```bash
   cd courses/intro-python/code/start
   ```

4. Check the complete solution when needed:
   ```bash
   cd courses/intro-python/code/final
   ```

#### Using Cheatsheets

Quick reference for an entire course:
```bash
cat courses/intro-python/cheatsheet-kea.md
```

## Language Support

- **Primary**: Cape Verdean Kriolu (`kea`)
- **Secondary**: Portuguese (`pt`), English (`en`)

Content is created first in Kriolu, with translations following. Technical terms remain in English when no direct translation exists.

## Contributing

### Adding a New Course

1. Create the course directory under `courses/`:
   ```bash
   mkdir -p courses/{slug}/lessons
   ```

2. Create `course.yaml` with course metadata (title, modules, lessons)

3. Create lesson files: `courses/{slug}/lessons/{lessonSlug}/kea.mdx`
   - Each lesson requires frontmatter: `title`, `language`, `courseSlug`, `lessonSlug`

4. Add code samples in `code/start/` and `code/final/`
   - `code/final/` is the source of truth
   - `code/start/` is derived with implementation stripped and TODOs added

5. Add supporting materials as needed:
   - `cheatsheet-kea.md` — Quick reference for the entire course
   - `infographics/` — Visual diagrams (PNG)
   - `microlearn/` — Short-form content (video scripts, micro-blogs)

6. Create `manifest.md` listing all published assets

### File Naming

- Lessons: `courses/{slug}/lessons/{lessonSlug}/{lang}.mdx`
- Cheatsheets: `courses/{slug}/cheatsheet-{lang}.md`
- Blog posts: `blog/{status}/{date}-{slug}.mdx`

## License

MIT License.

---

**Nu ta kria djuntu!** (We build together!)
