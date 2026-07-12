# Changelog — intro-kotlin

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/intro-kotlin/`,
trace_id `Skola-course-intro-kotlin-rollback-20260519`). Hand-edits to this
published copy are recorded under their own dated heading.

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
