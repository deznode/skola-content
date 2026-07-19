# Infographic prompt — 06-inheritance-family-traits (metaphor concept pilot, compares against 06-inheritance-tree blueprint)

- **Topic:** intro-kotlin lesson 09 (classes-properties-and-inheritance) — inheritance between Veikulu and Karu, illustrated via the Skola metaphor library's `inheritance-as-family-traits` metaphor
- **Style:** `skola-sketch` — a warm human-story metaphor fits sketch's "everyday metaphor doodle" register better than blueprint's schematic register (per `05_Templates.md`'s own style guidance). Tightened anti-defect constraints baked in from the start, including the "no external callout duplication" fix learned earlier this session on `04`/`06`.
- **Status:** rejected (not promoted) — r1 rendered cleanly against every item on the checklist (correct labels, correct inheritance-direction connections, generic non-branded figures, no callout-duplication defect), but the user's subjective read was "i dont like it that much" after comparing side-by-side with the blueprint version — `06-inheritance-tree.prompt.md` (blueprint) was promoted instead. Kept as a clean historical reference in case a future session wants to revisit metaphor-driven infographics for this course.
- **Corrections log:** none needed — first pass was already clean technically; rejection was a subjective/pedagogical preference call, not a defect.
- **Source:** metaphor text reused verbatim from `skola/assets/metaphors/v1/metaphors.yaml`'s `inheritance-as-family-traits` entry (sourced from intro-python, ADR-0011-blessed for cross-course reuse — adding this Kotlin lesson to that metaphor's `source_lessons[]` is a follow-up if this concept wins). Code-mapping text reused verbatim from the existing `06-inheritance-tree.prompt.md` / lesson content. This is a genuine concept redesign, not a style pass: it bridges the metaphor (builds intuition first) to the actual Kotlin syntax (Veikulu/Karu), rather than showing the code structure alone.

## Concept test note

Top half: the family-traits metaphor — Djina inherits her green eyes from her mother and her height from her father, but also has her own unique trait (talent for playing violin). Bottom half: the same shape mirrored in code — `Veikulu` (parent) passes down to `Karu` (child) via `erda di`, and `Karu` has its own new property (`numeruPortas`) paralleling Djina's own unique trait. The visual parallel structure (inherited + own, in both halves) is the teaching device.

## Prompt

One infographic, single scene, plain warm background matching the course's existing hand-drawn marker style, divided into a top "metaphor" half and a bottom "code" half by a simple horizontal divider line.

**Top half (metaphor):** two small, simple, friendly hand-drawn figures (generic silhouette-style people, no specific facial detail, not photorealistic, not tied to any existing named character) positioned upper-left and upper-right: one labeled `Mai`, one labeled `Pai`. Below and between them, one larger figure labeled `Djina`. A tag reading `ojus verdi di si mai` connects from the `Mai` figure down to `Djina`. A tag reading `altura di si pai` connects from the `Pai` figure down to `Djina`. A third tag, attached directly to `Djina` and not connected to either parent, reads `si talentu pa toka violun` — optionally accompanied by one small simple violin glyph icon (no text on the icon itself). The connecting lines from both parents down to `Djina` are labeled once, together, with the word `erda`.

**Bottom half (code):** one box labeled `open class Veikulu`, one arrow below it labeled `erda di` pointing down to a second box labeled `class Karu`, which has a tag attached to it reading `numeruPortas` (positioned similarly to how Djina's own unique trait tag was attached to her, visually rhyming "her own talent" with "Karu's own new property").

**Title (verbatim):** `Eransa: Veikulu → Karu`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `Mai` | the mother figure, top half |
| `Pai` | the father figure, top half |
| `Djina` | the child figure, top half |
| `ojus verdi di si mai` | tag connecting Mai to Djina |
| `altura di si pai` | tag connecting Pai to Djina |
| `si talentu pa toka violun` | tag attached only to Djina (her own trait) |
| `erda` | the connecting lines from both parents to Djina, labeled once |
| `open class Veikulu` | header of the top code box, bottom half |
| `erda di` | the arrow between the two code boxes, bottom half |
| `class Karu` | header of the bottom code box, bottom half |
| `numeruPortas` | tag attached only to the Karu box (its own new property) |

**Bottom strip:** *(not used)*

## HARD CONSTRAINTS — the model MUST NOT violate these

0. **CRITICAL — read this before anything else:** the "Labels" table above is NOT a list of external callouts or annotations. Each entry's "Label text" is the literal, only content that appears at the location named in "Points to" — rendered ONCE, directly as that figure's name-tag or that box's header/attached-tag, with no separate leader-line callout box duplicating the same text elsewhere in the image. Do NOT draw any label a second time as an external annotation connected by an arrow back to where it "really" belongs — the label IS placed at its target directly, once.
1. Render every label above EXACTLY as specified, exact casing and punctuation. No other text may appear anywhere in the image beyond the title and the 11 labels listed.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text. Do not translate any Kriolu word toward Portuguese or English.
3. The two figures (`Mai`, `Pai`) and the child figure (`Djina`) must be simple, friendly, non-photorealistic sketch-style silhouettes or minimal line figures — no detailed facial features, no specific identifiable character design, no resemblance to any named/branded character from elsewhere in the Skola universe. These are generic, unnamed-beyond-their-label family figures illustrating the metaphor text, nothing more.
4. `ojus verdi di si mai` and `altura di si pai` must each connect clearly to BOTH their source parent AND to `Djina` — the inheritance direction (parent → child) must be visually unambiguous.
5. `si talentu pa toka violun` must connect ONLY to `Djina`, with no connection to either parent — it is her own trait, not inherited.
6. `numeruPortas` must connect ONLY to the `Karu` box, with no connection to the `Veikulu` box — it is Karu's own new property, not inherited from Veikulu.
7. The top (metaphor) and bottom (code) halves must be visually distinct (separated by a clear divider) but the parallel structure between them (inherited traits/properties vs. own unique trait/property) should be visually legible — e.g. similar tag shapes or similar spatial arrangement in both halves.
8. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles beyond the one optional violin glyph (which carries no text).
9. No grid lines, ruled lines, or graph-paper texture in the background beyond the course's established warm cream texture.
10. No callout arrows pointing at individual punctuation marks or single characters.
11. Do not duplicate the title, do not duplicate any label. Count carefully before finishing: the entire image contains exactly one instance of each of the 11 labels.
12. No title banner beyond the specified title text itself — do not add a style-name label anywhere.
13. No box, frame, or pill-shape background around the title text.

## Verification checklist (per candidate)

- [ ] Title verbatim: `Eransa: Veikulu → Karu`
- [ ] All 11 labels present, verbatim, correctly placed, each exactly once
- [ ] Mai/Pai/Djina are simple generic sketch figures — no photorealism, no branded-character resemblance
- [ ] Inherited traits (`ojus verdi di si mai`, `altura di si pai`) connect parent→Djina; `si talentu pa toka violun` connects only to Djina
- [ ] `numeruPortas` connects only to Karu box, not Veikulu box
- [ ] Top (metaphor) and bottom (code) halves clearly divided but visually parallel in structure
- [ ] NO external callout duplication of any label — this is the specific defect class fixed earlier this session
- [ ] No unrelated decoration, no invented text, no watermarks
