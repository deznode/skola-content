# Infographic prompt — 08-sealed-open-boundary (concept pilot, replaces 08-sealed-vs-open-hierarchy)

- **Topic:** intro-kotlin lesson 11 (enum-sealed-classes-and-encapsulation) — sealed class (closed hierarchy) vs open class (extensible hierarchy)
- **Style:** `skola-sketch` — matches the course's existing hand-drawn marker aesthetic. Tightened anti-defect constraints baked in from the start, per the discipline established on the 2026-07-18 Character Bible v1 refresh + this same session's 01/08 iteration.
- **Status:** promoted
- **Corrections log:** r1 confirmed the concept itself lands well (user approved the closed-loop-vs-dashed-loop direction) but had two defects: (1) the `hierarkia open` badge was duplicated — the same recurring "duplicate badge" bug seen earlier this session on the envelope/door concept, now landing on a different label; (2) the gap in the open (right) boundary read as merely "dashed style" rather than an unmistakable break — too subtle. Constraints 5, 9, and 20 tightened: the gap must be explicitly described as a wide, doorway-sized opening (not normal dash spacing), and duplication is called out with a concrete failure example. r2 fixed both (single `hierarkia open` badge, unmistakably wide gap) and is the promoted image (`08-sealed-open-boundary-sketch-r2_0_20260718_211741.jpg` → `../08-sealed-vs-open-hierarchy.jpg`, filename kept unchanged so the existing lesson markdown reference doesn't need updating). Minor known deviation, accepted: title ink renders warm brown with a highlighter-style backing rather than plain navy (constraint 13) — cosmetic only, not worth another regeneration cycle.
- **Source:** replaces `infographics/08-sealed-vs-open-hierarchy.jpg`. Third concept attempt this session: round 1 ("Sealed Envelope vs Open Door," see `08-sealed-envelope-open-door.prompt.md`) reached a technically clean r4 (no duplicate labels, blank wax seal, balanced layout) but the user rejected the underlying concept itself — an illustrated parcel+doorway scene felt like the wrong metaphor regardless of execution quality. This concept is a deliberate reset: a pure abstract set-diagram with NO illustrated objects (no envelope, no door, no puzzle, no furniture) — just the literal shape of a closed set vs an open set, which is the actual mathematical/structural distinction `sealed` vs `open` encodes. Labels reuse the same 6-item set proven achievable without duplication in the prior concept's r4 (title, `Konfirmadu`, `Kansela`, `hierarkia fitxadu`, `Karu`, `hierarkia open`, footer) — only the visual metaphor changes.

## Concept test note

Left side: a solid, unbroken outline (a simple rounded/blobby closed shape, hand-drawn) that fully encloses two labeled tags (`Konfirmadu`, `Kansela`) — the boundary line has NO gap anywhere; it reads as sealed shut purely from the line being unbroken. Right side: the same style of rounded shape, but drawn with a dashed outline that has one clear, visible GAP or opening in its boundary — one labeled tag (`Karu`) sits inside, and just outside the gap, a single small `+` symbol (not a word) sits in the open space beyond the boundary, showing "more can enter here." No parcels, doors, puzzles, or any illustrated object — this is a pure boundary/set diagram, closer to a Concept Map than an illustrated scene.

## Prompt

One infographic, single scene, two-panel side-by-side comparison, plain warm background matching the course's existing hand-drawn marker style. No illustrated objects (no envelope, no door, no puzzle, no furniture, no characters, no silhouettes) — the entire visual content is two boundary shapes, their contained tags, badges, and the footer strip.

**Left panel — sealed:** a solid, unbroken, hand-drawn closed outline (a simple rounded or slightly irregular blob shape, like a hand-drawn circle) in teal (`#2A9D8F`), drawn with a continuous line that has no breaks or gaps anywhere along its perimeter. Two small labeled tags sit fully inside this closed boundary: one reading `Konfirmadu`, one reading `Kansela`. A single badge outside the shape, near it, reads `hierarkia fitxadu`.

**Right panel — open:** the same style of rounded shape, in ocean blue (`#0077B6`), but drawn with a dashed outline that has ONE clear, visible gap in its perimeter — a section where the boundary line simply stops, leaving an opening. One small labeled tag sits inside the shape: `Karu`. Just outside the boundary, positioned in the gap/opening, a single small `+` symbol (a plain plus-sign glyph, not a word) sits in the open space — this is the only non-label mark permitted outside the two required boundary shapes. A single badge outside the shape, near it, reads `hierarkia open`.

**Footer, spanning both panels:** one horizontal strip in island yellow (`#FFC300`) containing the single line of reminder text specified below.

**Title (verbatim):** `sealed class vs open class`

**Labels — the ONLY text/symbols allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `Konfirmadu` | one of the two tags inside the closed (sealed) boundary |
| `Kansela` | the other tag inside the closed (sealed) boundary |
| `hierarkia fitxadu` | badge near the closed boundary |
| `Karu` | the tag inside the open (dashed) boundary |
| `hierarkia open` | badge near the open boundary |
| `+` | a single plus-sign glyph positioned in the gap of the open boundary — this is a symbol, not a word, and is the only exception to "no text beyond the labels listed" |
| `un enum class ka ten subklasses di tudu` | the single footer strip spanning both panels |

**Bottom strip (verbatim):** `un enum class ka ten subklasses di tudu`

## HARD CONSTRAINTS — the model MUST NOT violate these

1. Render every label above EXACTLY as specified, exact casing and punctuation. No other text may appear anywhere in the image beyond the title, the 6 text labels, the single `+` symbol, and nothing else.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text. Do not translate any Kriolu word toward Portuguese or English.
3. Do NOT illustrate any object — no envelope, no parcel, no door, no gate, no puzzle, no furniture, no vault, no shelf, no character, no silhouette, no person of any kind. The only shapes in this image are: the two boundary shapes, the tags/badges, the `+` symbol, the footer strip, and the title.
4. The LEFT boundary (sealed) must be drawn as a CONTINUOUS, UNBROKEN outline — the line must have zero gaps anywhere along its full perimeter. This unbroken-ness is the entire visual signal for "sealed/closed" and must be unambiguous.
5. The RIGHT boundary (open) must be drawn as a DASHED outline with exactly ONE clear, visible gap/opening in its perimeter, IN ADDITION to the normal dashing. This gap must be dramatically wider than the spacing between any two normal dashes — think "doorway-sized opening," roughly as wide as 4-5 individual dash segments combined, a completely blank stretch with no line at all. If a viewer could mistake the gap for just another dash-to-dash space, it is too small — make it obviously, unmistakably wider than that.
6. `Konfirmadu` and `Kansela` must be fully INSIDE the closed left boundary. `Karu` must be fully INSIDE the open right boundary (inside the shape, not in the gap).
7. The `+` symbol must sit OUTSIDE the right boundary shape, positioned at or near the gap in its outline — it must be a plain `+` glyph only, no circle around it, no other characters near it.
8. Do NOT render a third labeled tag anywhere — only `Konfirmadu` and `Kansela` on the sealed side, only `Karu` on the open side.
9. Count carefully before finishing: the ENTIRE image must contain EXACTLY ONE instance of each of the 6 text labels and the `+` symbol — one tag/badge per label, never two badges or two tags carrying the same text anywhere in the image, even in different positions or styles. Concrete failure example to avoid: do NOT draw `hierarkia open` (or any other label) as two separate badges connected by arrows from two directions — draw it as a single badge in a single position, with at most one arrow pointing to it.
10. The two panels must be visually balanced in composition weight — do NOT leave one side mostly blank/empty relative to the other.
11. Sealed side uses teal (`#2A9D8F`) as its dominant accent; open side uses ocean blue (`#0077B6`) as its dominant accent — do not swap or mix these between panels.
12. The footer strip is island yellow (`#FFC300`) background with navy (`#001F3F`) text, spans both panels, and contains ONLY the one line of text specified.
13. All title and label text renders in midnight navy (`#001F3F`) ink — not brown, not any other ink color.
14. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles.
15. No grid lines, ruled lines, or graph-paper texture in the background beyond the course's established warm cream texture.
16. No callout arrows pointing at individual punctuation marks or single characters.
17. Do not duplicate the title.
18. No title banner beyond the specified title text itself — do not add a style-name label anywhere.
19. No box, frame, or pill-shape background around the title text.
20. Each badge (`hierarkia fitxadu`, `hierarkia open`) connects to its boundary shape with AT MOST ONE arrow or leader line — never two arrows from two different badge instances pointing at the same boundary.

## Verification checklist (per candidate)

- [ ] Title verbatim, in navy ink: `sealed class vs open class`
- [ ] All 6 text labels + the `+` symbol present, verbatim, correctly placed, each exactly once
- [ ] Left boundary is fully unbroken/continuous — zero gaps
- [ ] Right boundary is dashed AND has exactly one clear, unmistakable gap
- [ ] `Konfirmadu`/`Kansela` fully inside the closed boundary; `Karu` fully inside the open boundary; `+` outside, at the gap
- [ ] No illustrated objects of any kind — no envelope, door, puzzle, furniture, character, or silhouette
- [ ] Two panels visually balanced — neither side reads as empty/unfinished
- [ ] Sealed = teal, Open = ocean blue, not swapped; footer is island yellow with only its one line
- [ ] No unrelated decoration, no invented text, no watermarks, no duplicate labels
