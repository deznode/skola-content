# Changelog — web-foundations

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/web-foundations/`,
trace_id `Skola-course-web-foundations-20260513`). Hand-edits to this published copy are
recorded under their own dated heading.

## [2026-07-27] — publish

### Added
- Course cover `cover.jpg` — the Santiago frame (stone arch, half bare stone /
  half lime render). Published from the 3584×1184 master, downsampled to 1920×634
  and re-encoded at q80 (261 KB); this cover needed two steps down the quality
  ladder to fit the 300 KB budget.
- `image_url: cover.jpg` in `course.yaml` — required for the cover to render at
  all. skola.dev types that field as Velite's `s.image()`, so an undeclared
  `cover.jpg` ships nothing (spec 083 FR-001).

### Removed
- `test_only: true` (and its now-incorrect comment block) from `course.yaml`.
  **Deliberate promotion to production**, reversing the 2026-06-26 hand-edit
  below. The flag's real effect was to exclude the course from default
  `pnpm gen:catalog` discovery, the `catalog-drift-guard` hook and
  `task content:status` — so content edits silently never reached prod. The SQL
  has in fact lived in `db/migration` (not `db/seed/dev`) since 2026-06-28,
  seeded `status='draft'`, so the comment block's instructions were stale on both
  counts. Learner visibility remains gated by the runtime publish control
  (spec 060/061): the generator still emits `status='draft'` and an admin
  promotes it.

Lessons, sidecars, code and infographics are byte-identical to the previous
publish — verified across all 57 files. Content is unchanged.

## [2026-06-26] — hand-edit

### Changed
- Marked course `test_only: true` in `course.yaml` so it stays out of production (db/migration) and loads only in `local`/`test` profiles via `db/seed/dev`, until the course is ready to ship. Not durable across `/skola:pipeline-publish` — re-add after any republish.

## [2026-06-26] — publish (revision)

### Changed
- M1 L01 "Kumo Web ta funsiona": cut request→response redundancy so the infographic carries the 4-step sequence; reframed the Internet≠Web lead as a curiosity hook (`…ki sin. Ma nau.`) with a roads/islands analogy callout (`fiu`/`strada`/`kez`); removed `**bold**`/`` `code` `` markup that leaked as literal characters in the `<GlossaryText>` body (companion `learning-content-core` fix renders that subset going forward).

## [2026-06-26] — publish

### Added
- Initial publish of the full course **Fundamentus di Web: HTML i CSS** — 5 modules, 19 lessons (Kriolu).
- Module 1 — Introduson na Web (L01–03): how the web works, dev environment, first HTML page.
- Module 2 — Fundamentus di HTML (L04–07): document structure, text elements, images/links, semantics.
- Module 3 — Fundamentus di CSS (L08–13): syntax, text/color, selectors, inheritance, box model, DevTools.
- Module 4 — Layouts (L14–17): Flexbox (1D), Flexbox page layout, CSS Grid (2D), grid positioning.
- Module 5 — Projetu Final: Visita Kabu Verdi (L18–19): CV tourism landing page capstone (HTML + CSS).
- 19 `quiz.yaml` + 19 `exercises.yaml` sidecars (code / debug / reflect kinds).
- Cheatsheet (`cheatsheet-kea.md`), 11 infographics, and two code projects (`blog-adilson`, `projetu-kabu-verdi`) with `start/` + `final/`.

### Fixed
- Normalized two exercise slugs to kebab-case (`skrebe-pajina-semantika`, `preve-inheri-o-nau`) and added missing `language` to two M5 reflect exercises — required by publish-time sidecar validation.
