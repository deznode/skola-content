# Infographic prompt — 04-recursion-call-stack (trim to pure stack visual)

- **Topic:** intro-kotlin lesson 06 (loops-recursion-and-exceptions) — recursion as a call stack
- **Style:** `skola-sketch` — matches the course's existing hand-drawn marker aesthetic. Tightened anti-defect constraints baked in from the start.
- **Status:** promoted
- **Corrections log:** r1 executed the trim correctly but added an unauthorized duplicate: each of the 6 code lines was echoed a SECOND time outside the code box via leader-line arrows. r2 (after adding constraint 14 forbidding duplication) made it WORSE — it interpreted the "Labels — Points to" table as an instruction to draw an external callout box with a leader-line arrow FOR EVERY label, so now every single label appears twice (once correctly in place, once as a redundant callout box). Root cause identified: the "Labels" table format was being read as "add a leader-line callout," when the actual intent is "this exact text is the content that appears directly at that location — there is no separate callout, no leader line, no annotation box." Constraint 0 (new, placed first) and constraint 14 rewritten to state this explicitly and unambiguously. r3 confirmed the fix (no duplication anywhere) and is the promoted image (`04-recursion-call-stack-sketch-r3_0_20260719_083726.jpg` → `../04-recursion-call-stack.jpg`).
- **Source:** replaces `infographics/04-recursion-call-stack.jpg`, referenced from `lessons/06-loops-recursion-and-exceptions/kea.mdx` (image markdown line ~226). Concept trim: the original image's bottom section duplicated an arithmetic expansion trace (`fatorial(3) -> fatorial(2)*3 -> ... -> 6`) that is ALREADY shown verbatim in a plain code-comment block immediately above the image in the lesson (lines 216-224). This redesign drops that redundant trace and keeps only what the image uniquely contributes: the spatial "stack" shape itself — boxes stacking on the way down (calls), unstacking on the way back up (returns) — which text alone cannot convey. All Kriolu text below is reused verbatim from the existing lesson content and the current image's own alt text.

## Concept test note

Keep the code header and the 3 stacked call boxes with their down-arrow ("txomada") and up-arrow ("kaminhu di volta") — this is the image's unique value. Drop the bottom arithmetic-trace footer entirely; it is now redundant with the code-comment block that already precedes the image in the lesson.

## Prompt

One infographic, single scene, plain warm background matching the course's existing hand-drawn marker style.

**Top code box**, monospace, containing exactly these 4 lines:
```kotlin
fun fatorial(numeru: Int): Int {
    if (numeru <= 1) {
        return 1
    }
    return fatorial(numeru - 1) * numeru
}
```

**Below the code box, 3 stacked rectangular boxes, top to bottom:**
1. `fatorial(3)`
2. `fatorial(2)`
3. `fatorial(1)`, with a small tag reading `kazu bazi` attached to this box, and `return 1` shown inside or directly beneath this box.

**Between each pair of adjacent boxes**, a small downward arrow labeled `txomada` (call), showing the descent from `fatorial(3)` to `fatorial(2)` to `fatorial(1)`.

**Alongside the stack** (to one side, e.g. the right), one long upward arrow spanning from the bottom box back up to the top box, labeled `kaminhu di volta` (return path) — this represents the unwinding/return sequence after the base case resolves.

**Title (verbatim):** `Rekursividadi: Pilha di Txomadas`

**Labels — the ONLY text allowed anywhere in the image (verbatim), each pointing to its token:**
| Label text (exact) | Points to |
|--------------------|-----------|
| `fun fatorial(numeru: Int): Int {` | line 1 of the top code box |
| `    if (numeru <= 1) {` | line 2 of the top code box |
| `        return 1` | line 3 of the top code box |
| `    }` | line 4 of the top code box |
| `    return fatorial(numeru - 1) * numeru` | line 5 of the top code box |
| `}` | line 6 of the top code box |
| `fatorial(3)` | top stacked box |
| `fatorial(2)` | middle stacked box |
| `fatorial(1)` | bottom stacked box |
| `return 1` | inside/beneath the bottom stacked box |
| `kazu bazi` | small tag on the bottom stacked box |
| `txomada` | each downward arrow between boxes (same word, used at both arrow positions — see constraint 8) |
| `kaminhu di volta` | the single long upward arrow beside the stack |

**Bottom strip:** *(not used — the arithmetic expansion trace is intentionally omitted this round; it is redundant with the code-comment block that already precedes this image in the lesson)*

## HARD CONSTRAINTS — the model MUST NOT violate these

0. **CRITICAL — read this before anything else:** the "Labels" table below is NOT a list of external callouts or annotations. Each entry's "Label text" is the literal, only content that appears at the location named in "Points to" — it is rendered ONCE, directly inside/on that element, with no leader line, no arrow, no separate callout box, and no external duplicate copy of that text anywhere else in the image. Do NOT draw a second box containing the same text connected by an arrow back to the original — that is a duplication error, not a valid way to satisfy the label requirement. The ENTIRE image contains only: one top code box (with its 6 lines of code, each appearing once, inside the box), 3 stacked call boxes, 2 "txomada" arrow labels, 1 "kaminhu di volta" arrow label, and the "kazu bazi" tag — nothing else, no callout annotations of any kind.
1. Render every label above EXACTLY as specified, exact casing, indentation, and punctuation (preserve every `(`, `)`, `{`, `}`, `<=`, `-`, `*`, and the exact leading-space indentation on lines 2-5 of the code box). No other text may appear anywhere in the image beyond the title and the labels listed.
2. Do NOT add, invent, translate, paraphrase, "correct," or complete any text or code. Do not add comments, print statements, or extra lines to the code box.
3. Do NOT render the arithmetic expansion trace (`fatorial(3) -> fatorial(2)*3 -> ...`) or any equivalent — that content is intentionally excluded from this version.
4. Exactly 3 stacked boxes (`fatorial(3)`, `fatorial(2)`, `fatorial(1)`) — no more, no fewer. They must visually read as stacked (one below the other, touching or clearly connected), not scattered.
5. The `kazu bazi` tag and `return 1` must both be associated with the BOTTOM box (`fatorial(1)`) only — not with the other two boxes.
6. No decorative elements that do not carry a listed label — no stars, no gears, no sparkle marks, no unrelated doodles, no illustrated characters or mascots.
7. `txomada` appears exactly twice — once at each downward arrow between the 3 boxes (between box 1-2, and between box 2-3) — both instances share the same text but are two distinct, correctly-positioned labels, not a duplication error.
8. `kaminhu di volta` appears exactly ONCE, on a single upward arrow that spans the full stack height alongside it — not repeated per-box.
9. No grid lines, ruled lines, or graph-paper texture in the background beyond the course's established warm cream texture.
10. No callout arrows pointing at individual punctuation marks or single characters.
11. Do not duplicate the title.
12. No title banner beyond the specified title text itself.
13. No box, frame, or pill-shape background around the title text.
14. The code box's content must appear EXACTLY ONCE in the entire image — inside the top code box only, with no external duplicate copy connected by a leader-line/arrow, regardless of what the `skola-sketch` style preset's general "leader-line callout" conventions might otherwise suggest — those conventions do NOT apply to this image. Use the exact hyphen-minus character `-` wherever it appears (e.g. `numeru - 1`) — never an en-dash or em-dash substitute.

## Verification checklist (per candidate)

- [ ] Title verbatim: `Rekursividadi: Pilha di Txomadas`
- [ ] Code box exact, all 6 lines verbatim with correct indentation
- [ ] Exactly 3 stacked boxes, top-to-bottom: `fatorial(3)`, `fatorial(2)`, `fatorial(1)`
- [ ] `kazu bazi` tag + `return 1` both on the bottom box only
- [ ] `txomada` on each of the 2 downward arrows (between boxes); `kaminhu di volta` on the one long upward arrow
- [ ] NO arithmetic expansion trace anywhere — this is the specific trim being tested
- [ ] No unrelated decoration, no illustrated characters, no invented text, no watermarks
