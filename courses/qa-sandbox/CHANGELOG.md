# Changelog — qa-sandbox

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/qa-sandbox/`,
trace_id `Skola-course-qa-sandbox-sandbox`). Hand-edits to this published copy are
recorded under their own dated heading.

qa-sandbox is the exhaustive `@skola/learning-content-core` component+variant demo
fixture (one lesson family per authoring-doc README section).

## [2026-07-25] — publish

### Added
- M9 `inline-chrome-078` module (2 lessons) covering the block-chrome *props*,
  the dimension `registry-completeness.test.ts` structurally cannot see — it
  asserts only that a tag appears in some fixture, never that a prop does.
  `23-inline-chrome-blend` exercises `chrome="inline"` on eight inline-prop
  components (spec 078, shipped 2026-07-20 with its fixture deferred);
  `24-accent-rule-optout` exercises `showAccentRule={false}` on seven components
  across five families, including two sidecar-backed (`Quiz`, `CodeExample`) via
  new `quiz.yaml` + `code-examples.yaml`, so the prop is proven outside the
  inline-props-only subset. Parity-safe — neither is the L04 fixture the
  drift gate compares.

### Fixed
- `16-compare-and-concept`: four `ConceptDiagram` area accents and one
  `CompareTable` column accent used values outside the closed `Accent` union
  (`orange`/`red`/`green`/`purple`). `ConceptDiagram` silently drops an invalid
  accent to `null` (`isAccent()` guard) and `CompareTable` falls back to `blue`,
  so four of six tiles rendered unaccented and the "Set" column collided with
  "Lista" — while the lesson's stated objective was to demonstrate all six brand
  accents. Now uses the real six (`blue`, `gold`, `teal`, `coral`, `slate`,
  `navy`); prose corrected to match.

### Changed
- Draft/published divergence repaired in `topics/qa-sandbox/` (source of truth):
  `05-tenta-gosi-kinds` (`kea.mdx` + `exercises.yaml`, the four spec-063 W3
  practice exercises), `08-flashcard-and-parsons` (`kea.mdx`, Leitner `deckId` /
  `mode="def-first"` / custom `ratings[]`), and `22-list-treatments` (whole
  lesson) existed only as published copies, never backfilled to drafts. A
  publish would have pruned or reverted all of them. No published content
  changed — the drafts were brought up to match.

## [2026-07-25]

### Added
- M5 `inline-reference` module gains `22-list-treatments`, exercising the
  spec-081 `List` component's five variants (`marker`, `numbered`, `terms`,
  `check`, `tokens`) plus `accent`/`density`/`start`. Gives the
  registry-completeness backstop + parity-drift-gate a render surface for
  `List` (parity-safe — not the L04 fixture the gate compares).

## [2026-06-30]

### Added
- M8 `lesson-toolkit-meta` module + `21-lesson-meta` lesson exercising the three
  lesson_toolkit lesson-meta components: `LessonObjectives`, `Prerequisites`,
  `CourseOutline`. Gives the registry-completeness backstop + parity-drift-gate a
  render surface (parity-safe — not the L04 fixture the gate compares).

## [2026-06-28]

### Added
- M7 `learning-components-063` module + three lessons exercising the spec-063
  net-new components: `18-teaching-blocks` (`FileTree`, `AnalogyCard`,
  `MisconceptionConfront`, `FadingExample`), `19-systems-diagrams`
  (`ExecutionTrace`, `ArchitectureDiagram`, `SystemWalkthrough`,
  `SequenceDiagram`, `ConfigTree` + `traces.yaml`/`diagrams.yaml`/`configs.yaml`
  sidecars), `20-web-tools` (`LivePreview`, `BoxModel`).
- New practice kinds appended to `05-tenta-gosi-kinds/exercises.yaml`: `predict`,
  interactive `debug` (`bugLine`), `reflect` self-explanation (`code` +
  `modelPoints`), and a graduated `hints[]` ladder.

## [2026-06-23] — publish

### Changed
- Republished the exhaustive component+variant demo.
- Normalized Kriolu ALUPEC orthography across lessons and sidecars.

## [2026-06-22] — publish

### Added
- `GlossaryText` + `ParsonsProblem` usage in the L08 fixture (spec 055).
### Changed
- Synced L05 code-teaching widgets from draft (spec 052).

## [2026-06-20]

### Added
- `Steps`-phases, `PlatformTabs`, and `DetailDisclosure` usage in the design showcase.

## [2026-06-19]

### Added
- T2 microlearn fixture (segments/captions/transcript) for `everything-intro`.
- `<Kbd>` keyboard-shortcut section in the design showcase.

## [2026-06-18] — publish

### Changed
- Republished the course.

## [2026-06-16]

### Added
- `unified-design-showcase` lesson.

## [2026-06-11]

### Added
- `practice-blocks` lesson (TentaGosi + QuizSet + Rezumu).

## [2026-06-08]

### Added
- Extended the L04 parity fixture for spec 048 T-09.

## [2026-05-25] — publish (initial)

### Added
- Initial publish: QA Sandbox course with multiple lessons and quizzes in `kea`
  and `en`.
