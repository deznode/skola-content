# Changelog — jdbc-postgresql

All notable changes to this course are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/). Dates are publish/commit dates.

Each `## [YYYY-MM-DD] — publish` heading is rolled up at publish time from the
draft changes since the previous publish (source of truth: `topics/jdbc-postgresql/`,
trace_id `Skola-course-jdbc-postgresql-rollback-20260519`). Hand-edits to this
published copy are recorded under their own dated heading.

## [2026-07-03] — publish (title rename)

### Changed
- Course title: `Java JDBC ku PostgreSQL: Gia Konpletu pa Prinsipianti` →
  `Java JDBC ku PostgreSQL` (drop the marketing subtitle; match sibling-course
  house style).
- Module title (`jdbc-guide`): `Gia Konpletu di JDBC` → `Fundamentus di JDBC`
  (match the `Fundamentus di …` module pattern).

## [2026-07-02] — publish (components + glossary)

### Added
- L01: inline `<CodeCloze>` "Your turn" mapping the phone-call analogy onto real
  code (blanks = `Connection`/`PreparedStatement`/`ResultSet`), replacing the
  reflect exercise; `[[API]]` and `[[ORM]]` glossary terms.
- L02: `<GlossaryText>` hover-definitions for `driver`, `classpath`, and
  `try-with-resources`.
- L06: `<GlossaryText>` hover-definitions for `connection pooling` and
  `least privilege`.

### Changed
- All 6 lessons: `<QuizSet showHeader={false}>` under the quiz `<SectionHeading>`
  to drop the duplicate section header.

### Fixed
- Kriolu: `órdi`→`órden`; `trazi`/`trazê`→`traze`; `manti`/`mantén`→`mante`
  (-e infinitive convention).

### Removed
- L01 reflect `exercises.yaml` (superseded by the inline `<CodeCloze>`).

## [2026-07-02] — publish

### Changed
- Full Module 1 Kriolu calibration (6 lessons + sidecars): `fetxa`→`fitxa` (close,
  incl. `fitxadu`); `Drena`→`Kopia` for the ResultSet→List pattern; `fila` (not
  `linha`) for DB rows; PT definite-article elisions; `-son`→`-san` singulars; plus
  lexical fixes (`kore`, `unde`, `en bez di devolve`).
- Cheatsheet: same ALUPEC calibration + terminology/clarity pass (`Língua` accent,
  `Verifika WHERE ku kuidadu`, `fila afetadu`).
- L01: authored prose refinements (`papia ku`, `di Java`, `fika guardadu`, `eskolha`).
- `course.yaml` outcomes: `drena`→`kopia`, `transason`→`transasan`, article elision.

## [2026-06-30] — publish

### Added
- Initial course-mode publish of Module 1 (6 lessons): JDBC intro, connecting,
  CRUD with PreparedStatement, ResultSet, transactions, troubleshooting.
- Per-lesson sidecars: quiz (all 6) + exercises (L02–L05).
- Code: starter, solution, and Docker environment.
- Cheatsheet (kea).
- 3 infographics (skola-sketch style): JDBC architecture, JDBC URL anatomy,
  ResultSet cursor — wired into L1 / L2 / L4.

### Changed
- Kriolu normalization: `memória` (not `mimória`) topic-wide; lexical/label
  fixes (kódiku, unde, kore, ou, rejistu); bilingual arrow labels; new
  infographic hook titles.
