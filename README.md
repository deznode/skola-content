# Skola Content

Educational content and code samples for [Skola.dev](https://skola.dev) - teaching programming, cloud-native development, and AI in Cape Verdean Kriolu.

## Repository Structure

This repository contains both **written content** (tutorials, cheatsheets, blog posts) and **code samples** organized by topic.

### Content Types

| Type | Content Location | Code Location |
|------|------------------|---------------|
| **Tutorials** | `{topic}/{lang}/tutorial.mdx` | `{topic}/code/start/` + `{topic}/code/final/` |
| **Cheatsheets** | `{topic}/{lang}/cheatsheet.md` | `{topic}/code/examples/` |
| **Projects** | N/A | `{topic}/code/projects/{name}/` |
| **Blog** | `blog/` | N/A |

### Tutorials (Hands-on, Step-by-Step)

| Topic | Languages | Description |
|-------|-----------|-------------|
| [intro-python](./intro-python/) | kea | Introduction to Python programming |
| [java-swing-events](./java-swing-events/) | en | Event handling in Java Swing |
| [jdbc-postgresql](./jdbc-postgresql/) | kea | Database connectivity with JDBC and PostgreSQL |
| [swing-foundations](./swing-foundations/) | en | Java Swing fundamentals |
| [swing-layout-managers](./swing-layout-managers/) | en | Layout management in Java Swing |

### References (Cheatsheets & Examples)

| Topic | Languages | Description |
|-------|-----------|-------------|
| [kubernetes](./kubernetes/) | en | Kubernetes configuration cheatsheet |
| [tailwind-css](./tailwind-css/) | en | Tailwind CSS utility cheatsheet |
| [rag-strategies](./rag-strategies/) | en | RAG implementation patterns |

## Usage

### For Students

Clone this repository to get all content and code:

```bash
git clone https://github.com/deznode/skola-content.git
cd skola-content
```

#### Following a Tutorial

1. Navigate to the topic and start with the scaffolding:
   ```bash
   cd intro-python/code/start
   ```

2. Follow along with the written tutorial in `intro-python/kea/tutorial.mdx`

3. Check the complete solution when needed:
   ```bash
   cd intro-python/code/final
   ```

#### Using Cheatsheets

Reference examples alongside the cheatsheet:
```bash
# Read the cheatsheet
cat kubernetes/en/cheatsheet.md

# Browse examples
ls kubernetes/code/examples/
```

## Folder Structure

```
skola-content/
├── {tutorial-topic}/
│   ├── {lang}/                 # Written content (en/, kea/, pt/)
│   │   ├── tutorial.mdx
│   │   ├── infographics/       # Visual assets
│   │   ├── slides/             # Presentation slides
│   │   └── microlearn/         # Short-form content
│   └── code/
│       ├── start/              # Starter scaffolding with TODOs
│       ├── final/              # Complete working solution
│       └── projects/           # Hands-on practice projects
│
├── {reference-topic}/
│   ├── {lang}/
│   │   └── cheatsheet.md
│   └── code/
│       └── examples/           # Working code examples
│
└── blog/
    ├── drafts/
    └── published/
```

## Language Support

- **Primary**: Cape Verdean Kriolu (`kea`)
- **Secondary**: English (`en`), Portuguese (`pt`)

Content is created first in Kriolu, with translations following. Technical terms remain in English when no direct translation exists.

## Contributing

### Adding New Content

1. **Tutorials**: Create both `code/start/` and `code/final/` versions
   - `code/final/` is the source of truth
   - `code/start/` is derived with implementation stripped and TODOs added

2. **References**: Create `code/examples/` with working code

3. **Projects**: Create standalone practice exercises in `code/projects/{name}/`
   - Self-contained projects for students to practice concepts
   - Include README with instructions

4. **Written Content**: Add language-specific folders (`en/`, `kea/`, `pt/`)

5. **Always include**:
   - Clear learning objectives
   - Prerequisites and setup instructions
   - Links between content and code

### File Naming

- Tutorials: `{lang}/tutorial.mdx`
- Cheatsheets: `{lang}/cheatsheet.md`
- Blog posts: `blog/{status}/{date}-{slug}.mdx`

## License

MIT License - See individual topic folders for specific licensing if applicable.

---

**Nos ta kria djunta!** (We build together!)
