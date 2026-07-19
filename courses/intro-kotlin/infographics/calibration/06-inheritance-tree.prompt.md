# Infographic prompt — 06-inheritance-tree (blueprint style test)

- **Topic:** intro-kotlin lesson 09 (classes-properties-and-inheritance) — inheritance between Veikulu and Karu
- **Style:** `blueprint` — testing this preset for the first time on real course content (previously only tested on character portraits, where it lost for reasons specific to that content type: unauthorized callouts + an inappropriate grid background on a person). `05_Templates.md`'s own guidance recommends blueprint specifically for "architecture, schema, protocol, reference content" once a learner is past the very first basics — this is a genuine structural class diagram, exactly that content type, and lesson 9 is well past the course's opening lessons.
- **Status:** promoted
- **Corrections log:** r1 was mostly clean but had two issues: (1) monospace-looking title instead of friendly sans-serif; (2) 3 extra unlabeled routing arrows beyond the single `erda di` connector. r2 (after adding constraints 12-13) fixed BOTH of those — title is now clearly rounded sans-serif, and only one `erda di` connector remains — but introduced a much larger regression: it interpreted the "Labels — Points to" table as an instruction to draw an external callout box with a leader-line arrow FOR EVERY label (both box headers, every property/method line, and the warning strip), so every single label now appears twice. Root cause: the "Labels" table format was being read as "add a leader-line callout," when the intent is "this text is the content that appears directly at that location, once." Constraint 0 (new, placed first) added to state this explicitly. r3 confirmed the fix and is the promoted image (`06-inheritance-tree-blueprint-r3_0_20260719_083801.jpg` → `../06-inheritance-tree.jpg`). A parallel "family-traits" metaphor concept (`06-inheritance-family-traits.prompt.md`, reusing the Skola metaphor library's `inheritance-as-family-traits` entry) was also piloted as a comparison — it rendered cleanly on the first try, but the user preferred this blueprint version after comparing both.
- **Source:** replaces `infographics/06-inheritance-tree.jpg`, referenced from `lessons/09-classes-properties-and-inheritance/kea.mdx` (image markdown line ~228). Concept unchanged — this is a style test, not a redesign; the original box-arrow-box structure with the "erda di" connector already reads clearly. All Kriolu/code text below is reused verbatim from the existing lesson content and the current image's own alt text.

## Concept test note

Unlike the sketch-style prompts this session, blueprint's native aesthetic INCLUDES light grid guides as part of its intended schematic look (per `05_Templates.md` and the preset's own style guidance) — so this prompt does NOT forbid grid lines the way the sketch-style prompts did. What stays forbidden is INVENTING new content: extra callouts, extra annotations, or explanatory text beyond what's listed below. Blueprint style must not repeat blueprint's earlier character-portrait failure mode (unauthorized explanatory callouts) — every leader-line/callout in this image must point at one of the listed labels, nothing else.

## Prompt

One infographic, single scene, on a blueprint's light off-white or light blue-grey background with light grid guides — the schematic technical-diagram look, not a cold dark-navy engineering drawing.

**Top box**, labeled `open class Veikulu`, containing (each on its own line, monospace):
- `matrikula: String`
- `presuPerDia: Double`
- `open fun mostraDetalis()`

**A single downward arrow/connector** from the top box to the bottom box, with a leader-line label reading `erda di` (in the friendly sans-serif, not monospace).

**Bottom box**, labeled `class Karu`, containing (each on its own line, monospace):
- `numeruPortas: Int = 4`
- `: Veikulu(matrikula, presuPerDia)`
- `override fun mostraDetalis()`

**Bottom warning strip**, spanning the full width beneath both boxes, in a coral-tinted panel: `Skise di open ka ta kria un bug ki bu ta diskubri só dipos — el ta para kompilasan imediatamenti`

**Title (verbatim):** `Eransa: Veikulu → Karu`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `open class Veikulu` | header of the top box |
| `matrikula: String` | line inside the top box |
| `presuPerDia: Double` | line inside the top box |
| `open fun mostraDetalis()` | line inside the top box |
| `erda di` | the connector/arrow between the two boxes |
| `class Karu` | header of the bottom box |
| `numeruPortas: Int = 4` | line inside the bottom box |
| `: Veikulu(matrikula, presuPerDia)` | line inside the bottom box |
| `override fun mostraDetalis()` | line inside the bottom box |
| `Skise di open ka ta kria un bug ki bu ta diskubri só dipos — el ta para kompilasan imediatamenti` | the bottom warning strip |

**Bottom strip (verbatim):** `Skise di open ka ta kria un bug ki bu ta diskubri só dipos — el ta para kompilasan imediatamenti`

## HARD CONSTRAINTS — the model MUST NOT violate these

0. **CRITICAL — read this before anything else:** the "Labels" table below is NOT a list of external callouts or annotations. Each entry's "Label text" is the literal, only content that appears at the location named in "Points to" — rendered ONCE, directly inside/on that element (inside the box it belongs to), with no leader line, no arrow, no separate callout box, and no external duplicate copy of that text anywhere else in the image. Do NOT draw a second box containing the same text connected by an arrow back to the original box — that is a duplication error. The ENTIRE image contains only: the top box (with its 4 lines of content, each appearing once, inside the box), the single `erda di` connector arrow, the bottom box (with its 4 lines of content, each appearing once, inside the box), and the warning strip — nothing else, no callout annotations of any kind, regardless of what blueprint's or any style preset's general "leader-line callout" conventions might otherwise suggest.
1. Render every label above EXACTLY as specified, exact casing and punctuation, including every `:`, `(`, `)`, `.`, and `=`. No other text may appear anywhere in the image beyond the title and the 10 labels listed.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text or code. Do NOT add explanatory annotations, leader-line callouts, or side notes beyond the single `erda di` connector label — this is the specific failure mode blueprint showed on character portraits and must not repeat here.
3. All class/property/method identifiers (everything in the two boxes) render in MONOSPACE. The title, `erda di`, and the warning strip text render in a friendly geometric sans-serif, NOT monospace.
4. Light grid guides in the background are permitted and expected (this is blueprint's native look) — but the grid must stay light/subtle, never dark or dominant, and no other decorative elements may be added beyond the grid, the 2 boxes, the connector, and the warning strip.
5. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles, no illustrated characters or mascots, no icons beyond simple line-art if any (and any icon used must not carry its own text).
6. Background must be light off-white or light blue-grey — NOT dark or cold navy. Boxes and lines are midnight navy on the light background.
7. Do not duplicate the title, do not duplicate any label.
8. Count carefully before finishing: the entire image must contain exactly one instance of each of the 10 labels.
9. No callout arrows pointing at individual punctuation marks or single characters.
10. No title banner or style-name label beyond the specified title text itself.
11. No box, frame, or pill-shape background around the title text beyond what's specified for the two class boxes and the warning strip.
12. There must be EXACTLY ONE connector/arrow between the two boxes — the single `erda di` arrow from the top box to the bottom box. Do NOT add per-property routing arrows or any other connector line between individual lines inside the two boxes — the two boxes connect to each other as whole units, once, not property-by-property.
13. The title text must render in a rounded, friendly geometric sans-serif font that is visually and clearly DIFFERENT from the monospace font used for code — if in doubt, make the title's font unmistakably more rounded/casual than the code font, not a coding/technical typeface.

## Verification checklist (per candidate)

- [ ] Title verbatim: `Eransa: Veikulu → Karu`
- [ ] All 10 labels present, verbatim, correctly placed, each exactly once
- [ ] Class/property/method text in monospace; title/connector/warning text in friendly sans-serif
- [ ] Light grid guides present but subtle, light off-white/blue-grey background, not dark
- [ ] No unauthorized extra callouts/annotations beyond the single `erda di` connector — this is the key blueprint-specific risk being tested
- [ ] No unrelated decoration, no illustrated characters, no invented text, no watermarks
