# Infographic prompt — 01-numeric-conversion-pipe (concept pilot, replaces 01-numeric-type-ladder)

- **Topic:** intro-kotlin lesson 03 (variables-types-and-text) — numeric type widening/narrowing conversion
- **Style:** `skola-sketch` — matches the course's existing hand-drawn marker aesthetic (consistency with the 4 infographics not being touched this round). Tightened anti-defect constraints (11-16 below) baked in from the start, per the discipline established on the 2026-07-18 Character Bible v1 refresh session.
- **Status:** promoted
- **Corrections log:** none needed — first-pass render was clean against the full checklist (all 10 labels correct, pipe visibly and monotonically widens, consistent segment coloring, single forward/reverse arrow pair, no unrelated decoration). Promoted directly (`01-numeric-conversion-pipe-sketch_0_20260718_203507.jpg` → `../01-numeric-type-ladder.jpg`, filename kept unchanged so the existing lesson markdown reference doesn't need updating).
- **Source:** replaces `infographics/01-numeric-type-ladder.jpg`, referenced from `lessons/03-variables-types-and-text/kea.mdx` (image markdown line ~73). Concept redesign: the original "ladder" is being replaced with a "Widening Pipe" — the pipe visibly widens through the 4 stages, making the widening direction the primary visual read, since the immediately-following `<AnnotatedCode>` component already walks through the exact same conversion sequence line-by-line — this infographic should give the big-picture shape, not duplicate that code trace. All Kriolu text below is reused verbatim from the existing lesson content and the current image's own alt text (already-published, vetted phrasing) — no new Kriolu was authored for this prompt.

## Concept test note

A single pipe, drawn left-to-right, that visibly widens across 4 segments (Int → Long → Float → Double) — width itself encodes "more capacity." A bold forward arrow along the top labeled `amplia` (widen) shows the natural/automatic direction. A separate, visually secondary reverse arrow beneath the pipe carries the narrowing warning — direction and consequence should be readable from shape alone, before a viewer reads any text.

## Prompt

One infographic, single scene, plain warm background matching the course's existing hand-drawn marker style — no scene beyond the pipe diagram itself, no characters, no mascots.

A single pipe/tube drawn horizontally left to right, made of 4 connected segments that **visibly and continuously widen** from left (narrowest) to right (widest) — like a real pipe increasing in diameter, not 4 equal-sized boxes. Segment widths in increasing order: `Int` (narrowest) → `Long` → `Float` → `Double` (widest). Each segment is outlined in midnight navy (`#001F3F`) with an ocean-blue (`#0077B6`) fill — a single consistent color across all 4 segments (do not vary the fill color per segment; width alone encodes the size difference).

Each segment is labeled with its type name, placed inside or directly on the segment. At each of the 3 joints between segments, a small label sits on the joint showing the conversion call used at that step.

A single bold forward arrow in teal (`#2A9D8F`) runs along the top of the pipe, left to right, spanning its full length, with the word `amplia` labeled once near the arrow (not repeated at each segment).

Beneath the pipe, a single thinner reverse arrow in coral (`#FF595E`), running right to left, points back toward `Int`. Below this reverse arrow, one warning strip (coral-tinted background, navy text) contains the two lines of warning text specified below.

**Title (verbatim):** `Konversan Numériku: Int → Long → Float → Double`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `Int` | leftmost (narrowest) pipe segment |
| `Long` | second pipe segment |
| `Float` | third pipe segment |
| `Double` | rightmost (widest) pipe segment |
| `toLong()` | the joint between the `Int` and `Long` segments |
| `toFloat()` | the joint between the `Long` and `Float` segments |
| `toDouble()` | the joint between the `Float` and `Double` segments |
| `amplia` | the single forward teal arrow along the top of the pipe |
| `Sentidu kontráriu: ta trunka, ka aredonda` | first line of the bottom warning strip |
| `9.9.toInt() → 9` | second line of the bottom warning strip (exact characters, including the arrow `→`) |

**Bottom strip:** the two warning-strip lines above, stacked, inside one coral-tinted strip beneath the reverse arrow.

## HARD CONSTRAINTS — the model MUST NOT violate these

1. Render every label above EXACTLY as specified, in the exact casing and punctuation shown (including parentheses `()` and the arrow `→`). No other text may appear anywhere in the image beyond the title, the 10 labels listed, and nothing else.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text. Do not translate any Kriolu word toward Portuguese or English, and do not translate any code token.
3. The pipe MUST visibly widen across all 4 segments, monotonically, left to right — a viewer must be able to tell the size order (`Int` < `Long` < `Float` < `Double`) from width alone, without reading the labels. Do NOT render 4 equal-sized segments or boxes.
4. All 4 pipe segments share the SAME fill color (ocean blue `#0077B6`) and the same navy (`#001F3F`) outline — do not vary the segment color; only width encodes size.
5. Exactly one forward arrow (teal, `amplia` label once) and exactly one reverse arrow (coral, no separate label beyond what's in the warning strip) — do not add a second forward arrow, do not add per-segment direction arrows.
6. No decorative elements that do not carry the labels above — no stars, no gears, no sparkle marks, no unrelated doodles, no unexplained mascot/character illustrations (e.g. no musician, no random figure) anywhere in the image. Every mark in the image must be either the pipe, the two arrows, the warning strip, or one of the listed text labels.
7. No grid lines, ruled lines, or graph-paper texture in the background.
8. No callout arrows pointing at individual punctuation marks or single characters.
9. Do not duplicate the title, do not duplicate any label.
10. Colorblind-safe: the forward/reverse contrast must also be distinguishable by arrow direction and position (top vs. bottom of the pipe), not by color alone.
11. No title banner beyond the specified title text itself — do not add a second decorative header, do not add a style-name label (e.g. do not render text like "Skola Chalk Sketch" anywhere).
12. No extra grid/notebook-paper ruling beyond the course's established warm cream background texture.
13. No unrelated corner decorations (stars, wavy border flourishes) beyond the course's established tape-corner motif, if used consistently with the other 4 untouched infographics — if in doubt, omit corner decoration entirely rather than inventing new flourishes.
14. No callout arrows connecting labels to the wrong token — every label must sit directly on or immediately beside the exact token it names.
15. No box, frame, or pill-shape background around the title text beyond what's specified for the warning strip.
16. The warning strip must contain exactly the two lines specified and nothing else — no extra explanatory sentence, no restating of the title.

## Verification checklist (per candidate)

- [ ] Title verbatim: `Konversan Numériku: Int → Long → Float → Double`
- [ ] All 10 labels present, verbatim, correctly placed (4 type names, 3 conversion calls, `amplia`, 2 warning lines)
- [ ] Pipe visibly and monotonically widens left to right across 4 segments — size order readable from shape alone
- [ ] All 4 segments same navy outline + ocean-blue fill — no per-segment color variation
- [ ] Exactly one teal forward arrow (top, `amplia`) and one coral reverse arrow (bottom, pointing to the warning strip)
- [ ] No unrelated decoration — no stars/gears/doodles/mascots not tied to a listed label
- [ ] No invented text, no translated/altered Kriolu or code tokens, no watermarks
- [ ] No title banner/style-name text beyond the specified title
