# Video Script: Java Swing EDT - The Golden Rule

**Language**: English (EN)
**Duration**: 60-90 seconds
**Platform**: YouTube Shorts / TikTok / Instagram Reels
**Target Audience**: Java beginners learning GUI programming

---

## [0:00-0:10] HOOK + PROBLEM
**Visual**: Frozen Swing app UI, cursor spinning
**Narration**:
"Your Swing app is freezing? Here's the #1 mistake Java beginners make with GUIs..."

---

## [0:10-0:25] EXPLAIN THE PROBLEM
**Visual**: Split screen - main thread vs EDT thread diagram
**Narration**:
"Swing has ONE golden rule: All UI updates MUST happen on the Event Dispatch Thread, not your main thread. Break this rule? UI freezes, race conditions, crashes."

**Text Overlay**: "Main Thread ≠ EDT"

---

## [0:25-0:45] SHOW THE ANTI-PATTERN
**Visual**: Code editor with RED X overlay
**Code Display**:
```java
// ❌ WRONG - On main thread
public static void main(String[] args) {
    JFrame frame = new JFrame("Bad!");
    frame.setVisible(true);  // UI freeze risk!
}
```

**Narration**:
"Here's the wrong way - creating GUI components directly in main. This runs on the wrong thread."

---

## [0:45-1:15] SHOW THE SOLUTION
**Visual**: Code editor with GREEN checkmark
**Code Display**:
```java
// ✅ RIGHT - On EDT
public static void main(String[] args) {
    SwingUtilities.invokeLater(() -> {
        JFrame frame = new JFrame("Perfect!");
        frame.setVisible(true);
    });
}
```

**Narration**:
"The fix? Wrap everything in SwingUtilities.invokeLater. This lambda runs on the EDT. Your UI stays smooth, no freezes, no race conditions."

**Text Overlay**: "Always use invokeLater()"

---

## [1:15-1:25] TAKEAWAY
**Visual**: Golden rule badge animation
**Narration**:
"Remember: ALL Swing code belongs on the EDT. One rule, zero exceptions."

**Text Overlay**: "Golden Rule: EDT for ALL UI code"

---

## [1:25-1:30] CTA
**Visual**: Skola.dev logo + subscribe animation
**Narration**:
"Follow Skola.dev for more Java tutorials that actually make sense!"

**Text Overlay**:
"👉 Follow @skola.dev"
"#JavaSwing #JavaDevelopment #Programming"

---

## Production Notes

### Visual Cues
- **0:10**: Animate thread diagram with arrows showing separation
- **0:25**: Red X appears with error sound effect
- **0:45**: Green checkmark with success chime
- **1:15**: Golden badge pulses 3 times

### Text Overlays (Use Throughout)
- Main thread vs EDT comparison
- Code snippets with syntax highlighting
- Key terms in bold: "invokeLater", "EDT", "Golden Rule"

### Background Music
- Upbeat, tech-themed, low volume
- Increase tempo at solution reveal (0:45)

### Pacing
- Quick cuts between problem and solution
- Hold on code for 8-10 seconds (readable on mobile)
- Fast-paced narration with clear enunciation

---

## Hashtags for Description
#JavaSwing #JavaDevelopment #Programming #LearnJava #CodingTutorial #SoftwareDevelopment #JavaEDT #GUIProgramming #JavaTips #SkolaDev
