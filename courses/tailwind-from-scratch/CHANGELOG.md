# Changelog — tailwind-from-scratch

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/tailwind-from-scratch/`,
trace_id `Skola-course-tailwind-from-scratch-20260513-000000`). Hand-edits to this published
copy are recorded under their own dated heading.

## [2026-07-07] — publish

### Fixed
- Synced 6 lesson bodies (`01-o-ki-e-tailwind-css`, `02-anbienti-di-dezenvolvimentu`, `18-grid`, `23-tailwind-cli-v4`, `24-theme-di-profundidade`, `25-direktivas-i-funsan-v4`) + 23 `quiz.yaml` + 4 `exercises.yaml` sidecars that had accumulated Kriolu proofread fixes in drafts since the last publish but were never copied over: canonical `kal` → `kual` ("which/what") across quiz/exercise prompts, `otomatikamenti` → `automatikamenti` spelling, and tightened prose in `02-anbienti-di-dezenvolvimentu` (removed filler "Bon notísia" phrasing, dropped an incidental persona reference) plus a missing `<SectionHeading>` added in `01-o-ki-e-tailwind-css`.

## [2026-07-07] — publish

### Added
- `code/m3-resort-brava/{start,final}/` — the missing Module 3 continuity of the running Resort Brava example (interactivity/variants, responsive breakpoints, flexbox, grid, 3D transform hover-lift, `@theme`-driven animation, brand color/font tokens, dark mode). `start/` is the corrected Module 2 handoff state; `final/` layers in Lisan 13, 14, 17–22 (Lisans 15/16 — container queries, columns — intentionally use separate standalone demos per their own lesson text, not Resort Brava).

### Fixed
- `code/m2-resort-brava/final/index.html` was actually the full Module 3 end-state mislabeled as the Module 2 final — it included hover/focus/dark-mode/animation/`@theme` rename classes that Module 2's own 9 lessons never teach. Trimmed it back to what Lisans 4–12 actually build, reconstructed by reading each lesson's own "antis/dipos" narrative; also fixed a reverted email typo (`resorbrava@` → `resortbrava@exemplu.cv`, per Lisan 6's own correction).
- `21-theme-kores-fontes-breakpoints` (lesson + its `exercises.yaml` solution): the hero heading's `CodeDiff`/solution set `text-mar-700`, contradicting the lesson's own stated `amber-* → sol-*` rename mapping (the heading was `amber-600`, sol-domain, before the rename) and contradicting Lisan 22's own illustrative snippet for the same element. Corrected to `text-sol-700`.
- `code/m3-resort-brava/final/index.html` dark-mode toggle `aria-label` had a spelling drift (`"Alterna modu skuru"`) versus the lesson text and the module's own title (`Modu Sukuru`); corrected to `"Alterna modu sukuru"`.

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
