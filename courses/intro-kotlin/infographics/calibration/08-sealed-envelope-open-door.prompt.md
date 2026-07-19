# Infographic prompt — 08-sealed-envelope-open-door (concept pilot, replaces 08-sealed-vs-open-hierarchy)

- **Topic:** intro-kotlin lesson 11 (enum-sealed-classes-and-encapsulation) — sealed class (closed hierarchy) vs open class (extensible hierarchy)
- **Style:** `skola-sketch` — matches the course's existing hand-drawn marker aesthetic. Tightened anti-defect constraints (12-17 below) baked in from the start, per the discipline established on the 2026-07-18 Character Bible v1 refresh session.
- **Status:** calibration (not promoted — pilot test only)
- **Corrections log:** r1 passed its checklist clean, but user feedback: too busy/confusing — specifically too many separate scattered tags on the sealed side (`hierarkia fitxadu`, `mesmu pakoti/módulu`, `ezaustivu sen else` as 3 independent floating sticky notes). Cut to essentials: dropped `mesmu pakoti/módulu` and `ezaustivu sen else` entirely — that nuance is already taught by the `<CompareTable>` and surrounding prose earlier in this same lesson, so this diagram only needs to carry the closed-vs-open shape, one badge per side. r2 fixed the busyness (cleaner, balanced layout) but introduced two new defects: `Kansela` was rendered TWICE (duplicate tag, no matching single `Konfirmadu`+`Kansela` pair) and the wax seal had an invented "S" letter/lock icon not in the label list. Constraints 6 and 18 tightened to explicitly forbid label duplication and any glyph/letter/icon on the wax seal. r3 fixed both r2 defects (Konfirmadu/Kansela each appear once, wax seal is blank) and the layout is clean and balanced — but introduced the same duplication bug on a different label: the `hierarkia fitxadu` badge appeared TWICE (two separate badges with identical text, in two different positions). Constraint 19 added: the whole image must contain exactly one instance of each of the 6 labels, no exceptions. Regenerating as r4.
- **Source:** replaces `infographics/08-sealed-vs-open-hierarchy.jpg`, referenced from `lessons/11-enum-sealed-classes-and-encapsulation/kea.mdx` (image markdown line ~68). Concept redesign: the original two-column layout left the "open" side almost entirely blank, which reads as an unfinished diagram rather than communicating "extensible." This redesign makes openness itself the visual content (a door with room for more to pass through) rather than empty whitespace. This infographic's job is narrower than the `<CompareTable>` that appears earlier in the same lesson (which already covers Enum vs Sealed exhaustively) — this diagram is specifically about the STRUCTURAL shape difference between a closed, finite subclass set (`sealed`) and an open, extensible one (`open`), tied back to the `Veikulu`/`Karu` example from lesson 9. All Kriolu text below is reused verbatim from the existing lesson content and the current image's own alt text (already-published, vetted phrasing) — no new Kriolu was authored for this prompt.

## Concept test note

Left side: a closed, wax-sealed envelope/parcel containing exactly the 2 known subclasses (`Konfirmadu`, `Kansela`) — visually finite and shut, nothing can be added. Right side: an open door/gate, with `Karu` walking through it, and a dashed/translucent silhouette just beyond the doorway suggesting more subclasses could follow — visually extensible, not empty. The asymmetry between "2 fixed items in a sealed box" and "1 known item plus room to grow" is the entire teaching point, and should now be legible from the imagery alone, not from how much whitespace is left over.

## Prompt

One infographic, single scene, two-panel side-by-side comparison, plain warm background matching the course's existing hand-drawn marker style — no characters beyond the two labeled boxes/figures described below (`Konfirmadu`, `Kansela`, `Karu` are simple labeled shapes/tags, not illustrated character portraits).

**Left panel — sealed:** a closed parcel/envelope, wrapped and sealed shut with a wax-seal stamp, drawn in teal (`#2A9D8F`) with navy (`#001F3F`) outline. Two small labeled tags are visible tucked into the sealed envelope's flap, both fully inside the sealed boundary: one reading `Konfirmadu`, one reading `Kansela`. A single small badge near the envelope reads `hierarkia fitxadu` — this is the ONLY explanatory badge on this side, no other floating labels.

**Right panel — open:** an open door or gate frame, drawn in ocean blue (`#0077B6`) with navy outline, standing open (not closed). A single labeled tag reading `Karu` is positioned at the doorway, as if passing through. Just beyond the open doorway, one dashed-outline silhouette (a simple rounded placeholder shape, no facial features, no character detail) suggests another subclass could follow — this dashed shape carries no text label of its own. A small badge near the door reads `hierarkia open`.

**Footer, spanning both panels:** one horizontal strip in island yellow (`#FFC300`) containing the single line of reminder text specified below.

**Title (verbatim):** `sealed class vs open class`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `Konfirmadu` | one of the two tags inside the sealed envelope |
| `Kansela` | the other tag inside the sealed envelope |
| `hierarkia fitxadu` | badge near the sealed envelope |
| `Karu` | the tag at the open doorway |
| `hierarkia open` | badge near the open door |
| `un enum class ka ten subklasses di tudu` | the single footer strip spanning both panels |

**Bottom strip (verbatim):** `un enum class ka ten subklasses di tudu`

## HARD CONSTRAINTS — the model MUST NOT violate these

1. Render every label above EXACTLY as specified, exact casing and punctuation. No other text may appear anywhere in the image beyond the title, the 6 labels listed, and nothing else.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text. Do not translate any Kriolu word toward Portuguese or English.
3. The sealed envelope must read as CLOSED/SEALED (wax seal or equivalent closure clearly visible) with BOTH `Konfirmadu` and `Kansela` tags fully contained inside its boundary — nothing may extend outside the envelope's outline.
4. The open door/gate must read as OPEN (visibly ajar or fully open, not closed) with the `Karu` tag at or passing through the doorway.
5. The dashed silhouette beyond the open door is non-negotiable — it is the visual device that turns "empty space" into "room for more," and must be present, but must carry NO text label, NO facial features, and NO character detail — a simple rounded/blank placeholder outline only.
6. Do NOT render a third labeled subclass tag anywhere — only `Konfirmadu` and `Kansela` on the sealed side, only `Karu` on the open side. The dashed silhouette represents "more could come" visually, not a named third subclass. Each of `Konfirmadu` and `Kansela` must appear EXACTLY ONCE, each on its own separate tag — do NOT render either name twice, do NOT render two tags with the same text.
7. The two panels must be visually balanced in composition weight — do NOT leave one side mostly blank/empty relative to the other; both the envelope (left) and the door+silhouette (right) should occupy comparable visual space. Exactly ONE explanatory badge per side (`hierarkia fitxadu` left, `hierarkia open` right) — do NOT add any additional floating labels, sticky notes, or badges beyond what's listed in the labels table.
8. Sealed side uses teal (`#2A9D8F`) as its dominant accent; open side uses ocean blue (`#0077B6`) as its dominant accent — do not swap or mix these between panels.
9. The footer strip is island yellow (`#FFC300`) background with navy text, spans both panels, and contains ONLY the one line of text specified — no restating of other labels.
10. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles, no illustrated character faces/portraits for `Konfirmadu`/`Kansela`/`Karu` (these are simple labeled tags/shapes, not character art).
11. No grid lines, ruled lines, or graph-paper texture in the background beyond the course's established warm cream texture.
12. No callout arrows pointing at individual punctuation marks or single characters.
13. Do not duplicate the title, do not duplicate any label.
14. No title banner beyond the specified title text itself — do not add a style-name label anywhere (e.g. do not render text like "Skola Chalk Sketch").
15. No unrelated corner decorations beyond the course's established tape-corner motif, if used consistently with the other 4 untouched infographics — if in doubt, omit corner decoration entirely rather than inventing new flourishes.
16. No callout arrows connecting labels to the wrong token — every label must sit directly on or immediately beside the exact token it names.
17. No box, frame, or pill-shape background around the title text.
18. The wax seal must be a plain, blank wax-seal stamp shape (a simple round/scalloped seal impression) with NO letter, initial, icon, lock symbol, or any other glyph inside or on it — it is pure texture/closure signal, not a label carrier.
19. Count carefully before finishing: the ENTIRE image must contain EXACTLY ONE instance of each of the 6 labels (`Konfirmadu`, `Kansela`, `hierarkia fitxadu`, `Karu`, `hierarkia open`, and the footer line) — one tag/badge per label, never two badges or two tags carrying the same text anywhere in the image, even in different positions or styles.

## Verification checklist (per candidate)

- [ ] Title verbatim: `sealed class vs open class`
- [ ] All 6 labels present, verbatim, correctly placed — exactly one explanatory badge per side, no extra floating tags
- [ ] Sealed envelope reads as closed/sealed, both tags fully inside its boundary
- [ ] Open door reads as open, `Karu` tag at the doorway, dashed silhouette beyond it (no text/face on the silhouette)
- [ ] No third named subclass tag anywhere
- [ ] Two panels visually balanced — neither side reads as empty/unfinished
- [ ] Sealed = teal dominant, Open = ocean blue dominant, not swapped
- [ ] Footer strip is island yellow, contains only the one specified line
- [ ] No unrelated decoration, no illustrated character faces for the tags, no invented text, no watermarks
- [ ] `Konfirmadu` and `Kansela` each appear exactly once, on separate tags — no duplicate labels
- [ ] Wax seal is blank — no letter/icon/glyph inside it
- [ ] Every one of the 6 labels appears EXACTLY ONCE in the whole image — no badge or tag repeated anywhere
