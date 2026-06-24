# QA Sandbox — Published Assets

**Published:** 2026-06-24
**Source:** topics/qa-sandbox/

## Files

| File | Type | Count |
|------|------|-------|
| course.yaml | Course manifest | 1 |
| lessons/{NN}-{slug}/kea.mdx | Lessons (Kriolu) | 17 |
| lessons/{01,02}-*/en.mdx | Lessons (English) | 2 |
| lessons/**/quiz.yaml | Quiz sidecars | 6 |
| lessons/**/exercises.yaml | Exercise sidecars | 1 |
| lessons/**/code-examples.yaml | Code-example sidecars | 3 |
| infographics/* | Infographics | 1 |
| microlearn-kea/{unitSlug}/ | Microlearn unit bundles | 1 |

## Structure

6 modules (one per learning-content-core README family + M0 layouts), 17 lessons,
exhaustively exercising all 21 registered components and their variants. Anchored
04-callouts-and-figure (parity-drift-gate fixture). `test_only: true` — excluded
from prod catalog discovery.
