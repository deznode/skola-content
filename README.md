# Skola Samples

Tutorial companion code for [Skola.dev](https://skola.dev) educational content.

## Repository Structure

This repository contains code samples organized by topic to accompany Skola tutorials and reference materials.

### Tutorials (Hands-on, Step-by-Step)

These topics include both **starter scaffolding** (`initial/`) and **complete solutions** (`complete/`).

| Topic | Description | Language |
|-------|-------------|----------|
| [intro-python](./intro-python/) | Introduction to Python programming | Python |
| [java-swing-events](./java-swing-events/) | Event handling in Java Swing | Java |
| [jdbc-postgresql](./jdbc-postgresql/) | Database connectivity with JDBC and PostgreSQL | Java |
| [swing-foundations](./swing-foundations/) | Java Swing fundamentals | Java |
| [swing-layout-managers](./swing-layout-managers/) | Layout management in Java Swing | Java |

### References (Cheatsheets & Examples)

These topics contain complete working examples only.

| Topic | Description | Type |
|-------|-------------|------|
| [kubernetes](./kubernetes/) | Kubernetes configuration examples | Cheatsheet |
| [tailwind-css](./tailwind-css/) | Tailwind CSS utility examples | Cheatsheet |
| [rag-strategies](./rag-strategies/) | RAG implementation patterns | Reference |

## Usage

### For Tutorials

1. **Clone the starter code** to follow along:
   ```bash
   git clone https://github.com/deznode/skola-samples.git
   cd skola-samples/{topic}/initial
   ```

2. **Reference the complete solution** when needed:
   ```bash
   cd skola-samples/{topic}/complete
   ```

### For References

Browse the `examples/` folder for working code snippets:
```bash
cd skola-samples/{topic}/examples
```

## Folder Structure

```
skola-samples/
├── {tutorial-topic}/
│   ├── README.md           # Setup instructions, prerequisites
│   ├── initial/            # Starter scaffolding with TODOs
│   └── complete/           # Full working solution
│
└── {reference-topic}/
    ├── README.md           # Overview and usage
    └── examples/           # Working code examples
```

## Contributing

When adding new samples:

1. **Tutorials**: Create both `initial/` and `complete/` versions
   - `complete/` is the source of truth
   - `initial/` is derived from `complete/` with implementation stripped and TODOs added

2. **References**: Create only the `examples/` folder with working code

3. **Always include** a `README.md` with:
   - Prerequisites
   - Setup instructions
   - Learning objectives (for tutorials)

## License

MIT License - See individual topic folders for specific licensing if applicable.

---

**Nôs ta kriâ djunta!** (We build together!)
