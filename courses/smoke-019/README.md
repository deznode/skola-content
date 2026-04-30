# Smoke Topic for Spec 019 Publish Parity

> ⚠️ **Smoke Test Artefact**: This course was created to validate Spec 019 (Publish Parity) pipeline end-to-end. It is not production educational content.

**Slug:** `smoke-019`  
**Language:** Kabuverdianu (`kea`)  
**Level:** Beginner  
**Duration:** ~30 minutes  
**Category:** Programming  

---

## Description

Un kursu di nivel iniciante pa aprendê komo trabadja ku fixerus di tekstu na Python — lê, skrebe, i junta konteúdu — tudu skrita na Kabuverdianu. Kriadu kumu artefatu di smoke-test pa validá parity di publikason na Spec 019.

---

## Prerequisites

Konhesimentu básiku di Python (variáveis, loops, i funsoens). Nun preciza sabê nada di fixerus ántes.

---

## Learning Outcomes

1. Uza `open()` na modu di leitura pa abrí fixerus di tekstu
2. Apliká `read()` i `readlines()` pa buskà konteúdu di fixeru
3. Uza instruson `with` pa fechadu seguru i otomátiku di fixerus
4. Trata kodifikason UTF-8 pa karateres diakritkus do Kriolu/Português
5. Uza modus `"w"` i `"a"` koretamente pa skrebe i juntá konteúdu
6. Evitá trunkamentu axidental di fixeru kuandu junta linhas

---

## Module Structure

### Module 1: Fixerus na Python

| # | Lesson Slug | Duration |
|---|-------------|----------|
| 1 | `le-un-fixeru-di-tekstu` | 15 min |
| 2 | `skrebe-na-un-fixeru` | 15 min |

---

## File Listing

```
courses/smoke-019/
├── course.yaml
├── README.md
├── manifest.md
├── lessons/
│   ├── 01-le-un-fixeru-di-tekstu/
│   │   └── kea.mdx
│   └── 02-skrebe-na-un-fixeru/
│       └── kea.mdx
├── infographics/
│   ├── smoke-019-infographic-01_0_20260429_103500.jpg
│   ├── smoke-019-infographic-02_0_20260429_103527.jpg
│   ├── smoke-019-infographic-03_0_20260429_103541.jpg
│   └── smoke-019-infographic-04_0_20260429_103600.jpg
├── cheatsheet-kea.md
├── slides-kea/
│   ├── package.json
│   └── slides.md
├── microlearn/
│   ├── micro-blogs/
│   │   ├── v1-m1-01-le-un-fixeru-di-tekstu-kea.md
│   │   └── v1-m1-02-skrebe-na-un-fixeru-kea.md
│   ├── thumbnails/
│   │   ├── thumb-m1-01-le-un-fixeru-di-tekstu.md
│   │   └── thumb-m1-02-skrebe-na-un-fixeru.md
│   └── video-scripts/
│       ├── v1-m1-01-le-un-fixeru-di-tekstu-kea.md
│       └── v1-m1-02-skrebe-na-un-fixeru-kea.md
└── code/
    ├── start/
    │   ├── m1-01-le-fixeru/main.py
    │   └── m1-02-skrebe-fixeru/main.py
    └── final/
        ├── m1-01-le-fixeru/main.py
        └── m1-02-skrebe-fixeru/main.py
```
