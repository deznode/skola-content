# Changelog — intro-kotlin

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/intro-kotlin/`,
trace_id `Skola-course-intro-kotlin-rollback-20260519`). Hand-edits to this
published copy are recorded under their own dated heading.

## [2026-07-19] — hand-edit (infographic refresh)

### Changed
- All 6 infographics (numeric-type-ladder, null-safety-flow, recursion-call-stack,
  inheritance-tree, interface-cast-diagram, sealed-vs-open-hierarchy) replaced with
  cleaner, more deliberate visuals, following the calibration discipline established
  on the 2026-07-18 Character Bible v1 session:
  - numeric-type-ladder: widening-pipe concept, complements the `<AnnotatedCode>`
    walkthrough that follows instead of duplicating it
  - null-safety-flow: same 3-path structure, decluttered (removed a stray
    unrelated doodle)
  - recursion-call-stack: trimmed the arithmetic trace that duplicated the
    adjacent code comment, kept the unique stack visual
  - inheritance-tree, interface-cast-diagram: re-executed in `blueprint` style
    (schematic diagrams, not character portraits — a better content-style match)
  - sealed-vs-open-hierarchy: closed-vs-open boundary concept, fixes the
    original's unbalanced empty-space defect
- Alt text on the two lessons whose infographic concept changed (03, 11) updated
  to match; `02`/`04`/`06`/`07`'s alt text needed no change (concepts unchanged)

### Note
- Each infographic's `infographics/calibration/*.prompt.md` is the source of
  truth with a full corrections log; generation history (including two
  rejected concepts) is kept alongside for reference

## [2026-07-12] — publish (kriolu fixes)

### Changed
- Course title normalized: `Introdusaun ba Kotlin` → `Introdusan a Kotlin`
  (ALUPEC `-saun`→`-san` per native review; preposition `ba`→`a` to match the
  intro-python/intro-jdbc corpus convention — `ba` was the sole outlier)
- Singular `-saun`→`-san` throughout the manifest: `programasan` (description),
  `Programasan Orientada pa Objetu` (OOP module title). Plural `-sons` forms
  (`funsons`, `koleksons`) left as the author's correct convention.
- L1 (what-is-kotlin): `seguru` → `siguru` (Portuguese-root outlier vs the
  corpus `sigur-` root)
- L11: closing line title reference updated to match

## [2026-07-12] — publish (first publish since rollback)

### Added
- 11 lessons across 5 modules (Basics & Types, Control Flow, Functions,
  Collections, OOP) with quiz/exercises sidecars on all 11 and code-examples
  sidecars on 10 (the environment-setup lesson has none)
- 6 infographics (numeric-type-ladder, null-safety-flow, recursion-call-stack,
  inheritance-tree, interface-cast-diagram, sealed-vs-open-hierarchy), embedded
  inline in their lessons
- Universal character cast (Telma/Zeca/Sara/Nando) applied course-wide

### Changed
- Curriculum scope deepened twice post-draft: Elvis operator, break/continue,
  companion object, basic fun-declaration syntax, plus `==`/`===`, vararg,
  secondary constructors/init blocks, `readLine()`, `?.let{}`, Array vs List
- Full-course Kriolu ALUPEC lexical audit (all 11 lessons + sidecars)

### Deferred
- Cheatsheet, slides, code samples, and microlearn deliverables are not yet
  authored — this publish covers lessons + infographics only. `#3`
  (if/when decision tree) and `#5` (List/Set/Map comparison) infographics were
  intentionally skipped as redundant with existing `<CompareTable>`/`<AnnotatedCode>`.

### Note
- Published without a formally-approved Review gate (`pipeline.review.status`
  was `pending` at publish time) — an explicit, informed decision, not an
  oversight.
