# Changelog — intro-python

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/intro-python/`,
trace_id `Skola-course-intro-python-20260420-113000`). Hand-edits to this published copy are
recorded under their own dated heading.

## [2026-07-30] — publish

### Changed
- Kriolu lexicon corrections across all 33 lessons, 66 sidecars and the
  cheatsheet, from a review pass over the drafts. Six user rulings: `o ki` →
  `kuze ki` ("what", both interrogative and free-relative senses, 164 sites);
  `koreu` → `kore`; `parecidu` → `paresidu`; `até` → `te`; `pula` → `salta`;
  and `konp-` → `komp-` (65 sites).
- Course title is now **Introdusan Kompletu a Python** (`Konpletu` → `Kompletu`).
  The cheatsheet title and body previously disagreed on this word.
- Kriolu inside code fences is now normalized too — comments and string literals
  in 25 lesson files (83 fixes). Every normalize tier is prose-scoped by design,
  so this text had never been linted; `scripts/audit_codefence_kriolu.py` in
  skola-research now keeps that gap closed.
- Accented boolean identifier prefix `é_` → `e_` across example code
  (`e_par`, `e_palindromu`, `e_forti`, `e_maior_di_idadi`).
- Portuguese article elisions applied case by case: `t'o` → `te` (apostrophe
  elision is ALUPEC-illegal), `os dos` → `kes dos` ("both" — eliding would yield
  the numeral "two" and corrupt the and/or truth table), `Asesu a` → `Asesu pa`
  (dative), and `(o primi X)` → `(ou primi X)` (that `o` was a mangled "or").
- `<CodeCloze>` titles: "Inche spasus" → "Kompleta kódiku". `inche` keeps a
  Portuguese `ch` that papia cannot see — its digraph rule is word-initial only.
- Cheatsheet setup section now distinguishes `python3`/`pip3` (macOS/Linux) from
  `python`/`pip` (Windows); the previous text installed `python3` then told the
  learner to run `python`, which fails on a stock Ubuntu.
- Cheatsheet multiple-inheritance example now mirrors lesson 28's approved
  `Artista`/`Kompozitor` pair, replacing the near-identical `Animal`/`Animali`.

### Fixed
- Mutable-default entry now shows `if data is None: data = []` instead of
  `data = data or []`, which silently discards an intentionally-passed empty list
  — in the entry that teaches the fix.
- `course.yaml` module and lesson slugs realigned with `content.json`
  (`funsoens-*` → `funsons-*`, `operasoens-ficheru` → `operasons-fixeru`,
  `annotasoens-tipu` → `annotasons-tipu`). These pointed at directories that no
  longer exist, so those four lessons would have 404'd.
- Traceback annotation reads `UNDE`/`KUZE KI` rather than `UNDI`/`O KI`.

### Removed
- Four orphaned lesson directories left by the earlier slug rename:
  `16-funsoens-baziku`, `18-funsoens-inkorporadus`, `22-operasoens-ficheru`,
  `24-annotasoens-tipu`.

## [2026-07-30] — hand-edit

### Fixed
- `course.yaml` kea `description`, `prerequisites` and `outcomes` now use the
  canonical Kriolu forms already applied across the intro-python lesson drafts:
  `funsoens` → `funsons` (`-soens` → `-sons` plural), `ficheru` → `fixeru`,
  `Nenhum` → `Ninhun`, `Komprendi` → `Kompriendi`, `Skrebi` → `Skrebe`
  (`-e` infinitive).

  Recorded as a hand-edit rather than a publish rollup because these three
  fields have no draft source in `skola-research` — `content.json` carries only
  module and lesson titles, so `course.yaml` is where they are maintained.

## [2026-07-27] — publish

### Added
- Course cover `cover.jpg` — the Fogo frame (blue/yellow snake in the Python
  two-lobe form on basalt). Published from the 3584×1184 master, downsampled to
  1920×634 and re-encoded at q68 (280 KB); one of the two most heavily
  cross-hatched covers, so it needed the full quality-ladder descent.
- `image_url: cover.jpg` in `course.yaml` — the declaration Velite's `s.image()`
  keys on (spec 083 FR-001).

### Fixed
- `duration_minutes` 480 → 700. The old value was stale and unsupported by any
  source in the topic: `content.json` carries `metadata.estimated_duration:
  "680 min"`, and the 33 lesson durations sum to 700. Adopted the derived sum so
  the card total and the syllabus agree.

Lessons, sidecars, code and infographics are byte-identical to the 2026-07-26
publish — verified across all 96 files (including `25-testu-kodiku-pytest`, whose
draft filename and `content.json` slug differ; the publish loop wildcards the slug
segment, so the pair matches). This entry is a cover delivery plus one metadata fix.

## [2026-07-26] — publish

### Changed
- Converted ~310 plain `##`/`###` lesson headings to the `<SectionHeading>` component
  across M1–M4, with `variant`/`seq` carrying the section rhythm.
- Reframed L01 (`o-ki-e-python`) from a tech-career pitch to real-problem framing:
  intro prose, the third learning objective, the "Kabu Verdi" section, and quiz Q3
  (index 2) all now lead with problems Python solves rather than career outcomes.
  L01 also gains a mid-lesson `<QuizSet chrome="inline">` checkpoint.
- Renamed lesson 19 `jeneradorus` → `jeneradoris` (draft, published dir, and
  `course.yaml`); the stale `19-jeneradorus/` directory was pruned.
- Retrofitted lesson metaphors to the ADR-0034 standard set and example casts to the
  ADR-0033 universal cast.
- Added clarifying tip callouts across M1–M4 lessons.
- Cheatsheet: full Kriolu proofread pass.

### Fixed
- `bo` → `bu` clitic corrections across all 33 lessons (the pronoun rule was inverted
  in the earlier sweep).
- `reais` → `real` Portuguese-plural leak.

## [2026-07-04] — publish

### Added
- M4: split the overloaded `eransa` lesson into `eransa` (single inheritance) and a new
  `eransa-multiplu` lesson (multiple inheritance + MRO/C3, isinstance/issubclass) — course
  grows 32 → 33 lessons; downstream M4 lessons renumbered 28→33.
### Changed
- Full Kriolu contextual proofread pass across all four modules (M1 L01–L10, M2 L11–L15,
  M3 L16–L25, M4 L26–L33).
- Deterministic ALUPEC orthography normalization across M1–M4.
- Regenerated all infographics (PNG → JPG, 14 shipped); dropped unused infographic
  `15-python-undi-uzadu`.
- M4 example naming: Táksi → Taxi, Autokarru → Autokaru in the eransa lessons.
### Fixed
- `kal` → `kual` interrogative and assorted eransa Kriolu fixes.
- `poupa` correction; aligned "or" → `ou` in code comments.

## [2026-06-30] — publish

### Changed
- M1 (L01–L10): pedagogy and quiz refinements; component enrichment.
- M2 (L11–L15): pedagogy fixes, load restructures, expanded quizzes and exercises.
- M3 (L16–L25): applied M3 pedagogy fixes; component enrichment.
### Fixed
- Minor typos in code comments and explanations across lessons.

## [2026-06-23] — publish

### Changed
- Republished the full course (Introdusan Konpletu a Python).

## [2026-06-22] — publish

### Changed
- L02 (Instala Python) migrated to shared lesson components.

## [2026-06-21]

### Changed
- Adopted shipped lesson blocks across the course.

## [2026-06-16] — publish

### Changed
- Republished the full course.

## [2026-06-13]

### Added
- Enriched L01–L02 quizzes and sidecars.
### Changed
- Kriolu normalization on L01–L02.

## [2026-06-12] — publish

### Added
- Published L01 interactive components + L01/L02 sidecars.
### Changed
- Kriolu normalization refresh (lessons 03, 04, 07).
- Renamed kondisionais infographic `desizaun` → `desizan`.
### Removed
- Orphaned lesson-02 sidecars with no draft source.

## [2026-06-11] — publish

### Changed
- Republished the full course.

## [2026-06-09] — publish

### Changed
- Republished the full course.

## [2026-06-01] — publish

### Added
- Quiz and code-examples support across lessons.
- Callout boxes emphasizing key concepts (function naming, parameter handling,
  error management, decorators).
### Changed
- Restructured lessons; enhanced tips and best practices.
### Fixed
- MDX syntax in lessons 01, 05, 06.

## [2026-05-20]

### Fixed
- Applied ALUPEC orthography corrections across the course.

## [2026-05-19]

### Fixed
- Typos and phrasing in Kriolu across lessons and microlearn scripts; course
  description clarity.

## [2026-05-16]

### Changed
- Replaced `funsun` with `funsan` across the published course.

## [2026-05-08] — publish

### Added
- Microlearn `brief.mdx` (spec-029).

## [2026-04-27]

### Added
- Infographics across lessons.

## [2026-04-23] — publish (initial)

### Added
- Initial publish: Introdusun Konpletu a Python (32 lessons).
- Platform-required frontmatter on all 32 lessons.
- Numeric prefixes on lesson directories; lesson slugs decoupled from numbering.
### Changed
- Migrated blockquote tips/warnings to `:::callout` directive syntax.
### Fixed
- Escaped bare comparison operators in the operadoris lesson.
- Slogan spelling.
