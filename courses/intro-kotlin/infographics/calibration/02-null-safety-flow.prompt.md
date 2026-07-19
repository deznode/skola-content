# Infographic prompt — 02-null-safety-flow (declutter pass)

- **Topic:** intro-kotlin lesson 04 (booleans-and-null-safety) — null safety: safe call, if-check, unguarded crash, Elvis operator
- **Style:** `skola-sketch` — matches the course's existing hand-drawn marker aesthetic. Tightened anti-defect constraints baked in from the start, per the discipline established this session.
- **Status:** promoted
- **Corrections log:** none needed — first-pass render was clean (all 13 labels correct, no stray decoration, no illustrated mascot/musician). Promoted directly (`02-null-safety-flow-sketch_0_20260718_221619.jpg` → `../02-null-safety-flow.jpg`).
- **Source:** replaces `infographics/02-null-safety-flow.jpg`, referenced from `lessons/04-booleans-and-null-safety/kea.mdx` (image markdown line ~125). This is a **declutter pass, not a concept redesign** — the original 3-panel-comparison + Elvis-strip structure is a legitimate advance organizer (it previews all 3 null-handling paths before the lesson walks through each individually in separate `AnnotatedCode` blocks), so the structure is kept. The only defect found in the original was a stray, unexplained guitarist doodle in the bottom-right corner with no connection to null safety — this pass exists specifically to eliminate that class of unrelated decoration. All Kriolu text below is reused verbatim from the existing lesson content and the current image's own alt text (already-published, vetted phrasing).

## Concept test note

Same structure as the original: one top box introducing a nullable variable, 3 side-by-side panels (safe call, if-check, unguarded/crash), one bottom strip for the Elvis operator. The only change is discipline: every mark in the image must trace to a listed label — no stray mascots, no unexplained doodles, no decoration for decoration's sake.

## Prompt

One infographic, single scene, plain warm background matching the course's existing hand-drawn marker style.

**Top box:** contains the code `var mensajen: String? = null` and beneath it the phrase `un valor ki pode guarda null`.

**Three side-by-side panels below the top box, each a distinct color-coded column:**
1. **Teal panel**, header `Txamada sigura ?.` — contains the code `mensajen?.length` and beneath it `Devolve null sen kebra programa`.
2. **Ocean-blue panel**, header `Verifika ku if` — contains the code `if (mensajen != null)` and beneath it `Uza valor só dipos di verifikasan != null`.
3. **Coral panel**, header `Sen trata null` — contains the code `mensajen.length` and beneath it `NullPointerException (NPE) — Kotlin ta bloka na kompilasan`.

**Bottom strip, spanning the full width:** contains the header `Operador Elvis ?: — un valor padron kuandu é null` and beneath it the code `val tamanhu = mensajen?.length ?: 0`.

**Title (verbatim):** `Nulidadi Sigura: Kaminhu pa Trata null`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `var mensajen: String? = null` | code in the top box |
| `un valor ki pode guarda null` | phrase beneath the top-box code |
| `Txamada sigura ?.` | header of panel 1 (teal) |
| `mensajen?.length` | code in panel 1 |
| `Devolve null sen kebra programa` | text beneath panel 1's code |
| `Verifika ku if` | header of panel 2 (ocean-blue) |
| `if (mensajen != null)` | code in panel 2 |
| `Uza valor só dipos di verifikasan != null` | text beneath panel 2's code |
| `Sen trata null` | header of panel 3 (coral) |
| `mensajen.length` | code in panel 3 |
| `NullPointerException (NPE) — Kotlin ta bloka na kompilasan` | text beneath panel 3's code |
| `Operador Elvis ?: — un valor padron kuandu é null` | header of the bottom strip |
| `val tamanhu = mensajen?.length ?: 0` | code in the bottom strip |

**Bottom strip:** described above (Elvis operator).

## HARD CONSTRAINTS — the model MUST NOT violate these

1. Render every label above EXACTLY as specified, exact casing and punctuation, including every `?`, `.`, `!`, `:`, and parenthesis. No other text may appear anywhere in the image beyond the title and the 13 labels listed.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text. Do not translate any Kriolu word toward Portuguese or English, and do not alter any code token.
3. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles, and specifically NO illustrated character, mascot, musician, or any figure of any kind anywhere in the image. Every mark must be one of: the 4 boxes/panels, their contained text, the connecting structure between top box and the 3 panels, or the bottom strip.
4. Panel 1 is teal-dominant, panel 2 is ocean-blue-dominant, panel 3 is coral-dominant — do not swap or mix these between panels.
5. Do not add a checkmark/X/skull icon or any other symbol beyond simple, minimal iconography directly reinforcing each panel's outcome (a small checkmark for panel 1, a small lock/checkmark for panel 2, a small warning/error icon for panel 3) — these icons must be simple glyphs, not illustrated scenes, and must carry no additional text.
6. No grid lines, ruled lines, or graph-paper texture in the background beyond the course's established warm cream texture.
7. No callout arrows pointing at individual punctuation marks or single characters.
8. Do not duplicate the title, do not duplicate any label.
9. No title banner beyond the specified title text itself — do not add a style-name label anywhere (e.g. do not render text like "Skola Chalk Sketch").
10. Count carefully before finishing: the entire image must contain exactly one instance of each of the 13 labels.
11. No unrelated corner decorations beyond the course's established tape-corner motif, if used consistently with the other infographics in this course.
12. No box, frame, or pill-shape background around the title text.

## Verification checklist (per candidate)

- [ ] Title verbatim: `Nulidadi Sigura: Kaminhu pa Trata null`
- [ ] All 13 labels present, verbatim, correctly placed, each exactly once
- [ ] 3 panels correctly color-coded (teal / ocean-blue / coral), each with its own header, code, and outcome text
- [ ] Top box and bottom strip both present and correctly labeled
- [ ] NO illustrated character, mascot, musician, or unexplained figure anywhere — this is the specific defect being fixed
- [ ] No other unrelated decoration, no invented text, no watermarks
