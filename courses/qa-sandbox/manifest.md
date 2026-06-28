# QA Sandbox — Published Assets

**Published:** 2026-06-24
**Source:** topics/qa-sandbox/

## Files

| File | Type | Count |
|------|------|-------|
| course.yaml | Course manifest | 1 |
| lessons/{NN}-{slug}/kea.mdx | Lessons (Kriolu) | 20 |
| lessons/{01,02}-*/en.mdx | Lessons (English) | 2 |
| lessons/**/quiz.yaml | Quiz sidecars | 6 |
| lessons/**/exercises.yaml | Exercise sidecars | 1 |
| lessons/**/code-examples.yaml | Code-example sidecars | 3 |
| lessons/19-*/traces.yaml | Execution-trace sidecars | 1 |
| lessons/19-*/diagrams.yaml | Diagram sidecars (arch/walkthrough/sequence) | 1 |
| lessons/19-*/configs.yaml | Config-tree sidecars | 1 |
| infographics/* | Infographics | 1 |
| microlearn-kea/{unitSlug}/ | Microlearn unit bundles | 1 |

## Structure

7 modules (one per learning-content-core README family + M0 layouts + M7 spec-063
new components), 20 lessons, exhaustively exercising all registered components and
their variants. Anchored 04-callouts-and-figure (parity-drift-gate fixture).
`test_only: true` — excluded from prod catalog discovery.

M7 (`learning-components-063`) adds the spec-063 net-new tags: 18-teaching-blocks
(`FileTree`, `AnalogyCard`, `MisconceptionConfront`, `FadingExample`),
19-systems-diagrams (`ExecutionTrace`, `ArchitectureDiagram`, `SystemWalkthrough`,
`SequenceDiagram`, `ConfigTree` via `traces`/`diagrams`/`configs` sidecars), and
20-web-tools (`LivePreview`, `BoxModel`). The 05-tenta-gosi-kinds exercises append
the new practice kinds (`predict`, interactive `debug` `bugLine`, `reflect`
`code`+`modelPoints`, `hints[]` ladder).
