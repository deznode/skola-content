# Changelog — intro-python

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/intro-python/`,
trace_id `Skola-course-intro-python-20260420-113000`). Hand-edits to this published copy are
recorded under their own dated heading.

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
