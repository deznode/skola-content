# QA Sandbox — Published Assets

**Published:** 2026-06-18
**Source:** topics/qa-sandbox/

## Files

| File | Type | Count |
|------|------|-------|
| course.yaml | Course manifest | 1 |
| lessons/{NN}-{slug}/kea.mdx | Lessons (Kriolu) | 8 |
| lessons/{NN}-{slug}/en.mdx | Lessons (English, L1–L2 only) | 2 |
| lessons/{NN}-{slug}/quiz.yaml | Quiz sidecars | 8 |
| lessons/{NN}-{slug}/code-examples.yaml | CodeExample sidecars (L3, L4, L5) | 3 |
| lessons/{NN}-{slug}/exercises.yaml | Exercise sidecars (L7, L8) | 2 |
| infographics/* | Infographics (JPEG) | 1 |
| microlearn-kea/{unitSlug}/ | Microlearn unit bundles | 1 |

## Notes

- `course.yaml` is hand-maintained for this test bed (carries `video_url`, `content_type`, and `en` translations not present in `content.json`) — preserved as-is, not regenerated.
- `test_only: true` — excluded from default `pnpm gen:catalog` discovery and the catalog-drift-guard hook; never reaches prod.
- L4 (`callouts-and-figure`) CodeExample marker corrected to `position={1}` per pedagogy review (2026-06-17).
