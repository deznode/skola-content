# Changelog — tailwind-from-scratch

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/tailwind-from-scratch/`,
trace_id `Skola-course-tailwind-from-scratch-20260513-000000`). Hand-edits to this published
copy are recorded under their own dated heading.

## [2026-07-07] — hand-edit

### Changed
- Removed `test_only: true` from `course.yaml`. User decision: it's fine to promote the course to production now — visibility will be gated via the admin portal instead of keeping the whole course out of the catalog. `code/m3-resort-brava` and the microlearn units remain outstanding and can be added in a follow-up publish without re-gating.

### Fixed
- Lessons `22-modu-sukuru` and `23-tailwind-cli-v4`: fixed a `<CodeDiff note="...">` attribute that embedded a backslash-escaped double quote (`\"`), which JSX plain-attribute strings don't support as an escape — it desynced the tag parser and Velite dropped both lessons from the catalog (404 at runtime). Swapped the inner quotes to single quotes; no meaning change. See deznode/skola-content#9.

## [2026-07-07] — publish

### Added
- Initial publish of the full course **Fundamentus di Tailwind CSS v4** — 4 modules, 26 lessons (Kriolu), Tailwind v4.3.
- Module 1 — Komesa ku Tailwind v4 (L01–03): what Tailwind is, dev environment, first sandbox with the v4 Play CDN.
- Module 2 — Stilu i Vizual (L04–12): utility-first basics through filters/masks, using the `bg-color/opacity` slash modifier and other v4-current patterns.
- Module 3 — Layout i Movimentu (L13–22): interactivity/variants, responsive design, container queries, Flexbox/Grid, 3D transforms/animation, `@theme`, dark mode via `@custom-variant`.
- Module 4 — Anbienti di Produsan (L23–26): Tailwind CLI v4, `@theme` deep-dive, v4 directives/functions, Vite/Webpack/PostCSS build tooling.
- 26 `quiz.yaml` + 26 `exercises.yaml` sidecars (code / debug / explore / reflect / predict kinds).
- 11 corpus-verified, calibrated infographics (blueprint style), embedded live in their lessons.
- Kriolu cheatsheet covering the full v3→v4 migration surface.
- Code samples for Module 1 (sandbox), Module 2 (Resort Brava start), and Module 4 (Vite production build).

### Known gaps (tracked for a follow-up publish)
- `code/m3-resort-brava/` (Module 3 continuity of the running Resort Brava example) not yet authored.
- Microlearn (4 units: video script / micro-blog / SEO / thumbnail brief per module) deferred, not part of this publish.
- Course marked `test_only: true` in `course.yaml` pending the above.
