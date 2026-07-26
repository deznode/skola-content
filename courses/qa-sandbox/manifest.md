# QA Sandbox — Published Assets

**Published:** 2026-07-25
**Source:** topics/qa-sandbox/

## Files

| File | Type | Count |
|------|------|-------|
| course.yaml | Course manifest | 1 |
| lessons/{NN}-{slug}/kea.mdx | Lessons (Kriolu) | 24 |
| lessons/{01,02}-*/en.mdx | Lessons (English) | 2 |
| lessons/**/quiz.yaml | Quiz sidecars | 7 |
| lessons/**/exercises.yaml | Exercise sidecars | 1 |
| lessons/**/code-examples.yaml | Code-example sidecars | 4 |
| lessons/19-*/traces.yaml | Execution-trace sidecars | 1 |
| lessons/19-*/diagrams.yaml | Diagram sidecars (arch/walkthrough/sequence) | 1 |
| lessons/19-*/configs.yaml | Config-tree sidecars | 1 |
| lessons/19-*/memory.yaml | Memory-diagram sidecars | 1 |
| lessons/19-*/algos.yaml | Algorithm-visualizer sidecars | 1 |
| infographics/* | Infographics | 1 |
| microlearn-kea/{unitSlug}/ | Microlearn unit bundles | 1 |

## Structure

9 modules (one per learning-content-core README family + M1 layouts + M7 spec-063
new components + M9 spec-078 chrome props), 24 lessons, exhaustively exercising all
registered components and their variants. Anchored 04-callouts-and-figure
(parity-drift-gate fixture). `test_only: true` — excluded from prod catalog
discovery.

M7 (`learning-components-063`) adds the spec-063 net-new tags: 18-teaching-blocks
(`FileTree`, `AnalogyCard`, `MisconceptionConfront`, `FadingExample`),
19-systems-diagrams (`ExecutionTrace`, `ArchitectureDiagram`, `SystemWalkthrough`,
`SequenceDiagram`, `ConfigTree`, `MemoryDiagram`, `AlgorithmVisualizer` via
`traces`/`diagrams`/`configs`/`memory`/`algos` sidecars), and 20-web-tools
(`LivePreview`, `BoxModel`). The 05-tenta-gosi-kinds exercises append the new
practice kinds (`predict`, interactive `debug` `bugLine`, `reflect`
`code`+`modelPoints`, `hints[]` ladder).

M9 (`inline-chrome-078`) covers the two block-chrome *props* rather than new tags —
the dimension the registry-completeness backstop cannot see, since it only asserts
that a tag appears somewhere. 23-inline-chrome-blend exercises `chrome="inline"`
across eight inline-prop components; 24-accent-rule-optout exercises
`showAccentRule={false}` across seven components spanning five families, including
two sidecar-backed ones (`Quiz`, `CodeExample`) so the prop is proven outside the
inline-props-only subset.
