# Infographic prompt — 07-interface-cast-diagram (blueprint style test)

- **Topic:** intro-kotlin lesson 10 (interfaces-and-abstract-classes) — 3-level hierarchy + up-casting/down-casting
- **Style:** `blueprint` — testing this preset for the first time on real course content, same rationale as `06-inheritance-tree.prompt.md`. This diagram is a genuine 3-level type hierarchy with directional casting relationships — exactly the "architecture, schema, protocol" content `05_Templates.md` recommends blueprint for.
- **Status:** calibration (not promoted — pilot test only)
- **Corrections log:** none yet — first pass.
- **Source:** replaces `infographics/07-interface-cast-diagram.jpg`, referenced from `lessons/10-interfaces-and-abstract-classes/kea.mdx` (image markdown line ~51). Concept unchanged — style test, not a redesign; the original 3-level hierarchy with bidirectional casting arrows already synthesizes 4 separate preceding code examples well. All Kriolu/code text below is reused verbatim from the existing lesson content and the current image's own alt text.

## Concept test note

Same discipline note as `06-inheritance-tree.prompt.md`: blueprint's light grid guides are permitted and expected here (not forbidden the way sketch-style grids were). What stays forbidden is inventing new callouts or annotations beyond the labels listed — blueprint's earlier failure mode (unauthorized explanatory callouts) must not repeat.

## Prompt

One infographic, single scene, on a blueprint's light off-white or light blue-grey background with light grid guides — the schematic technical-diagram look, not a cold dark-navy engineering drawing.

**Three boxes, stacked vertically, top to bottom:**
1. Top: `interface Alugavel`, containing (monospace): `fun calculaPresu(dias: Int): Double`
2. Middle: `open class Veikulu : Alugavel`, containing (monospace): `override fun calculaPresu(dias: Int): Double`
3. Bottom: `class Karu : Veikulu`

**A downward connector** from the top box to the middle box, labeled `implementa` (friendly sans-serif). **A second downward connector** from the middle box to the bottom box, labeled `erda di Veikulu` (friendly sans-serif).

**One upward arrow in ocean-blue (`#0077B6`)**, running from the bottom box (`Karu`) directly up to the top box (`Alugavel`), bypassing the middle box visually (drawn alongside/beside the 3 boxes, not through them), labeled `automatikamenti i sen risku` (up-casting).

**One downward arrow in coral (`#FF595E`)**, running from the top box (`Alugavel`) directly down to the bottom box (`Karu`), alongside the 3 boxes on the opposite side from the blue arrow, labeled with three small badges positioned along the arrow reading `as`, `is`, and `as?`, plus the text `risku di ClassCastException` (down-casting).

**Title (verbatim):** `Up-casting i Down-casting: Alugavel, Veikulu, Karu`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `interface Alugavel` | header of the top box |
| `fun calculaPresu(dias: Int): Double` | line inside the top box |
| `implementa` | connector between top and middle boxes |
| `open class Veikulu : Alugavel` | header of the middle box |
| `override fun calculaPresu(dias: Int): Double` | line inside the middle box |
| `erda di Veikulu` | connector between middle and bottom boxes |
| `class Karu : Veikulu` | header of the bottom box |
| `automatikamenti i sen risku` | the ocean-blue upward arrow (up-casting) |
| `as` | first badge on the coral downward arrow |
| `is` | second badge on the coral downward arrow |
| `as?` | third badge on the coral downward arrow |
| `risku di ClassCastException` | text alongside the coral downward arrow |

**Bottom strip:** *(not used)*

## HARD CONSTRAINTS — the model MUST NOT violate these

1. Render every label above EXACTLY as specified, exact casing and punctuation, including every `:`, `(`, `)`, `.`, and `?`. No other text may appear anywhere in the image beyond the title and the 12 labels listed.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text or code. Do NOT add explanatory annotations, leader-line callouts, or side notes beyond what's listed — this is the specific failure mode blueprint showed on character portraits and must not repeat here.
3. All class/interface/method signatures (everything in the 3 boxes) render in MONOSPACE. The title, `implementa`, `erda di Veikulu`, `automatikamenti i sen risku`, and `risku di ClassCastException` render in a friendly geometric sans-serif, NOT monospace. The `as`/`is`/`as?` badges render in monospace (they are code operators).
4. Light grid guides in the background are permitted and expected (blueprint's native look) — but must stay light/subtle, never dark or dominant.
5. Exactly 3 boxes, stacked vertically in the order Alugavel (top), Veikulu (middle), Karu (bottom) — do not reorder, do not merge boxes.
6. The blue up-casting arrow goes directly from Karu to Alugavel (bypassing Veikulu visually) — NOT from Karu to Veikulu, and NOT from Veikulu to Alugavel. The coral down-casting arrow goes directly from Alugavel to Karu, on the opposite side of the boxes from the blue arrow.
7. The `as`, `is`, `as?` badges must be three SEPARATE small badges along the coral arrow, each exactly once — not merged into one badge, not repeated.
8. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles, no illustrated characters or mascots.
9. Background must be light off-white or light blue-grey — NOT dark or cold navy.
10. Do not duplicate the title, do not duplicate any label.
11. Count carefully before finishing: the entire image must contain exactly one instance of each of the 12 labels.
12. No callout arrows pointing at individual punctuation marks or single characters, beyond the two directional casting arrows themselves.
13. No title banner or style-name label beyond the specified title text itself.
14. No box, frame, or pill-shape background around the title text beyond what's specified for the 3 class boxes and the `as`/`is`/`as?` badges.

## Verification checklist (per candidate)

- [ ] Title verbatim: `Up-casting i Down-casting: Alugavel, Veikulu, Karu`
- [ ] All 12 labels present, verbatim, correctly placed, each exactly once
- [ ] 3 boxes stacked correctly: Alugavel / Veikulu / Karu, top to bottom, with `implementa` and `erda di Veikulu` connectors
- [ ] Blue up-casting arrow: Karu → Alugavel directly, bypassing Veikulu visually
- [ ] Coral down-casting arrow: Alugavel → Karu directly, with 3 separate `as`/`is`/`as?` badges
- [ ] Code/signatures in monospace; title/connectors/arrow-labels in friendly sans-serif (badges in monospace)
- [ ] Light grid guides present but subtle, light background, not dark
- [ ] No unauthorized extra callouts/annotations, no unrelated decoration, no invented text, no watermarks
