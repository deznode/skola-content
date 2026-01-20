---
theme: default
title: Java Swing Layout Managers Deep Dive
info: |
  ## Chapter 2: Layout Managers Deep Dive
  Professional Desktop Development with Java Swing

  Master fluid, responsive UI designs using BorderLayout, GridBagLayout, and the nested panels strategy.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Layout Managers Deep Dive

## Chapter 2: Professional Desktop Development with Java Swing

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Move beyond absolute positioning to fluid, responsive designs
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-50">Duration: 3.5 Hours</span>
</div>

<!--
Welcome to Chapter 2 where we'll master Layout Managers. By the end, you'll be able to create responsive UIs that adapt to different screen sizes, font scalings, and localizations.
-->

---
transition: fade-out
---

# The Problem: Absolute Positioning

Why `setLayout(null)` is an **anti-pattern**

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-4 bg-red-900 bg-opacity-20 rounded">

### Font Scaling
On Windows with 125% text scaling, the text "Submit" overflows the hardcoded button width.

</div>

<div class="p-4 bg-red-900 bg-opacity-20 rounded">

### Localization
German text is typically **30% longer** than English. Hardcoded layouts break when translated.

</div>

<div class="p-4 bg-red-900 bg-opacity-20 rounded">

### Resizability
If the user maximizes the window, components stay stuck in the top-left corner.

</div>

</div>

```java
// DON'T DO THIS!
frame.setLayout(null);
button.setBounds(10, 10, 80, 30);  // Hardcoded pixels = brittle code
```

<!--
Absolute positioning seems easy at first, but it creates a maintenance nightmare. When you hardcode pixel positions, your UI breaks under real-world conditions like different DPI settings, translations, or window resizing.
-->

---

# The Solution: Layout Managers

Express **intent** rather than **pixels**

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### Pixel-Based (Bad)
```java
button.setBounds(10, 10, 100, 30);
label.setBounds(10, 50, 200, 20);
```
- Fragile
- Doesn't scale
- Platform-dependent

</div>

<div>

### Intent-Based (Good)
```java
panel.add(button, BorderLayout.NORTH);
panel.add(label, BorderLayout.CENTER);
```
- Flexible
- Adapts automatically
- Cross-platform

</div>

</div>

<div class="mt-8 p-4 bg-green-900 bg-opacity-20 rounded">

**Key Insight**: Layout Managers let you describe *where* components should go relative to each other, not *exactly* where in pixels.

</div>

<!--
The paradigm shift is moving from "put this at x=10, y=50" to "put this in the center" or "put this below that". The layout manager handles the math.
-->

---

# BorderLayout

<div class="grid grid-cols-2 gap-8">

<div>

### The Default for JFrame

BorderLayout divides the container into **5 zones**:

| Zone | Behavior |
|------|----------|
| **NORTH/SOUTH** | Respect height, force width |
| **EAST/WEST** | Respect width, force height |
| **CENTER** | Consumes **all** remaining space |

```java
frame.add(toolbar, BorderLayout.NORTH);
frame.add(sidebar, BorderLayout.WEST);
frame.add(editor, BorderLayout.CENTER);
```

</div>

<div>

![BorderLayout Anatomy](../infographics/01-borderlayout-anatomy.png)

</div>

</div>

<!--
BorderLayout is the most commonly used layout manager. Think of NORTH as a toolbar area, WEST as a sidebar, and CENTER as your main content area. The CENTER zone is greedy - it takes all remaining space.
-->

---

# BorderLayout in Action

A typical application structure

```java {all|3-4|6-8|10-11|13-15|all}
public class MainWindow extends JFrame {
    public MainWindow() {
        // BorderLayout is the default for JFrame
        setLayout(new BorderLayout());

        // NORTH: Toolbar - full width, preferred height
        JToolBar toolbar = createToolbar();
        add(toolbar, BorderLayout.NORTH);

        // WEST: Navigation sidebar - preferred width, full height
        add(createSidebar(), BorderLayout.WEST);

        // CENTER: Main content - takes ALL remaining space
        JTextArea editor = new JTextArea();
        add(new JScrollPane(editor), BorderLayout.CENTER);

        // SOUTH: Status bar - full width, preferred height
        add(new JLabel("Ready"), BorderLayout.SOUTH);
    }
}
```

<!--
Notice how we don't specify any sizes! BorderLayout figures out how to divide the space. The toolbar gets its preferred height, the sidebar its preferred width, and the editor fills everything else.
-->

---

# FlowLayout & GridLayout

Simple layouts for simple needs

<div class="grid grid-cols-2 gap-8">

<div>

![Layout Comparison](../infographics/02-layout-comparison.png)

</div>

<div>

### FlowLayout (JPanel default)
```java
JPanel buttonBar = new JPanel(); // FlowLayout by default
buttonBar.add(new JButton("OK"));
buttonBar.add(new JButton("Cancel"));
buttonBar.add(new JButton("Apply"));
```

**Use case**: Row of buttons that wrap when needed

### GridLayout
```java
JPanel keypad = new JPanel(new GridLayout(4, 3));
for (int i = 1; i <= 9; i++) {
    keypad.add(new JButton(String.valueOf(i)));
}
```

**Use case**: Calculator keypad, uniform grids

**Limitation**: All cells are the same size!

</div>

</div>

<!--
FlowLayout is like text in a word processor - it flows left to right and wraps. GridLayout creates a perfect grid where every cell is identical. Good for keypads but not for forms.
-->

---

# BoxLayout

Vertical stacking with precise control

```java {all|2-3|5-7|9-10|12|all}
JPanel sidebar = new JPanel();
// BoxLayout requires the container as first argument
sidebar.setLayout(new BoxLayout(sidebar, BoxLayout.Y_AXIS));

// Add components
sidebar.add(new JButton("Dashboard"));
sidebar.add(new JButton("Reports"));
sidebar.add(new JButton("Settings"));

// Fixed spacing (10 pixels)
sidebar.add(Box.createVerticalStrut(10));

// Elastic spacing (pushes everything above it up)
sidebar.add(Box.createVerticalGlue());
```

<div class="mt-4 p-4 bg-blue-900 bg-opacity-20 rounded">

| Spacer | Description |
|--------|-------------|
| `Box.createVerticalStrut(10)` | Fixed 10px gap |
| `Box.createVerticalGlue()` | Elastic - absorbs extra space |
| `Box.createRigidArea(new Dimension(10, 10))` | Fixed box |

</div>

<!--
BoxLayout is perfect for toolbars and sidebars. The key insight is glue vs struts: struts are fixed size spacers, glue is like a spring that absorbs extra space.
-->

---

# The Nested Panels Strategy

Complex UIs = Simple layouts nested together

<div class="text-center mb-4">

**Don't use one complex layout. Use multiple simple layouts!**

</div>

```
┌─────────────────────────────────────────────────────┐
│                     HEADER (FlowLayout)             │  ← BorderLayout.NORTH
├─────────────┬───────────────────────────────────────┤
│   SIDEBAR   │                                       │
│  (BoxLayout)│           CENTER                      │  ← BorderLayout.CENTER
│             │        (ScrollPane)                   │
│  Dashboard  │                                       │
│  Reports    │                                       │
│  Settings   │                                       │
│     ↕       │                                       │
│   [Glue]    │                                       │
├─────────────┴───────────────────────────────────────┤
│                    STATUS BAR                       │  ← BorderLayout.SOUTH
└─────────────────────────────────────────────────────┘
```

<!--
This is the secret to maintainable Swing UIs. Instead of trying to position every component with one giant GridBagLayout, break your UI into logical sections. Each section uses the simplest layout that works for it.
-->

---

# Code: Composite UI

Putting it all together

```java {all|1-2|4-7|9-14|16-18|all}
// Main container uses BorderLayout
JPanel mainPanel = new JPanel(new BorderLayout());

// 1. The Header (North) - FlowLayout for left-aligned content
JPanel headerPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
headerPanel.add(new JLabel("User: Admin"));
mainPanel.add(headerPanel, BorderLayout.NORTH);

// 2. The Sidebar (West) - BoxLayout for vertical stacking
JPanel sidebar = new JPanel();
sidebar.setLayout(new BoxLayout(sidebar, BoxLayout.Y_AXIS));
sidebar.add(new JButton("Dashboard"));
sidebar.add(Box.createVerticalStrut(10));  // 10px gap
sidebar.add(new JButton("Reports"));
sidebar.add(Box.createVerticalGlue());      // Push up
mainPanel.add(sidebar, BorderLayout.WEST);

// 3. The Content (Center) - Always wrap in JScrollPane!
JTextArea contentArea = new JTextArea("Report Data...");
mainPanel.add(new JScrollPane(contentArea), BorderLayout.CENTER);
```

<!--
Study this pattern carefully. Main panel is BorderLayout. Header uses FlowLayout. Sidebar uses BoxLayout with glue. Center content is wrapped in JScrollPane. This is the template for 90% of desktop applications.
-->

---

# GridBagLayout: The Power Tool

When you need maximum flexibility

<div class="grid grid-cols-2 gap-4">

<div>

![GridBagLayout Constraints](../infographics/03-gridbag-constraints.png)

</div>

<div>

### When to Use
- Complex forms with label/input pairs
- Components that span multiple columns
- Non-uniform cell sizes needed
- Precise control over spacing and alignment

### Key Concept
Each component gets a **GridBagConstraints** object that defines:
- Where it goes (`gridx`, `gridy`)
- How big it is (`gridwidth`, `gridheight`)
- How it stretches (`fill`, `weightx`, `weighty`)
- Where it anchors (`anchor`)
- How much padding (`insets`)

</div>

</div>

<!--
GridBagLayout is like a spreadsheet - components go in cells, and cells can span multiple rows/columns. The constraints object controls everything about how the component behaves in its cell.
-->

---

# GridBagConstraints Breakdown

The 6 essential properties

```java {all|3-4|6-7|9-10|12-13|15-16|18-19|all}
GridBagConstraints gbc = new GridBagConstraints();

// Position: Which cell? (0,0) is top-left
gbc.gridx = 0;  gbc.gridy = 0;

// Spanning: How many cells wide/tall?
gbc.gridwidth = 2;  gbc.gridheight = 1;

// Weight: How much extra space to claim? (0.0 to 1.0)
gbc.weightx = 1.0;  gbc.weighty = 0.0;

// Fill: Should component stretch?
gbc.fill = GridBagConstraints.HORIZONTAL;  // NONE, VERTICAL, BOTH

// Anchor: If it doesn't fill, where does it sit?
gbc.anchor = GridBagConstraints.NORTHWEST;  // 9 positions like a compass

// Insets: Padding around the component (top, left, bottom, right)
gbc.insets = new Insets(5, 10, 5, 10);
```

<div class="mt-4 text-sm opacity-70">

**Pro Tip**: Create one GridBagConstraints, then modify and reuse it for each component.

</div>

<!--
Weight is the trickiest concept. If two components have weightx 0.3 and 0.7, they'll split extra horizontal space 30/70. If both are 0, neither stretches - extra space goes unused.
-->

---

# Decision Checklist

Which Layout Manager Should You Use?

<div class="grid grid-cols-2 gap-8">

<div>

![Layout Decision Flowchart](../infographics/04-layout-decision-flowchart.png)

</div>

<div class="text-lg">

| Question | Answer |
|----------|--------|
| Single central component? | **BorderLayout** |
| Simple row of buttons? | **FlowLayout** |
| Vertical stack with spacing? | **BoxLayout** |
| Uniform grid of items? | **GridLayout** |
| Complex form with labels? | **GridBagLayout** |
| Complex multi-section UI? | **Nested Panels** |

<div class="mt-8 p-4 bg-yellow-900 bg-opacity-20 rounded">

**Remember**: Start simple! Use BorderLayout + nested panels before reaching for GridBagLayout.

</div>

</div>

</div>

<!--
When in doubt, start with BorderLayout. Most applications fit into that NORTH/WEST/CENTER/SOUTH pattern. Only use GridBagLayout when you need precise control over a form-like layout.
-->

---

# Practice Exercise

Build a Settings Dialog

<div class="grid grid-cols-2 gap-8">

<div>

### Requirements

1. Dialog title: "Application Settings"
2. Main area with two tabs:
   - "General" tab
   - "Advanced" tab
3. General tab contains:
   - Username field (label + text input)
   - Theme dropdown (label + combo box)
   - Checkbox: "Show notifications"
4. Button bar at bottom:
   - OK, Cancel, Apply buttons

</div>

<div>

### Hints

```java
// Dialog structure
JDialog dialog = new JDialog(parent, "Settings", true);
dialog.setLayout(new BorderLayout());

// Tabbed pane in CENTER
JTabbedPane tabs = new JTabbedPane();
dialog.add(tabs, BorderLayout.CENTER);

// Button bar in SOUTH
JPanel buttonBar = new JPanel(new FlowLayout(FlowLayout.RIGHT));
buttonBar.add(new JButton("OK"));
// ...
dialog.add(buttonBar, BorderLayout.SOUTH);
```

**Challenge**: Use GridBagLayout inside the General tab for the form fields!

</div>

</div>

<!--
This exercise combines everything we've learned. The dialog uses BorderLayout. The button bar uses FlowLayout. The form inside the tab uses GridBagLayout. Try to implement this yourself before looking at solutions.
-->

---
layout: end
---

# Summary & Next Steps

## Key Takeaways

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### What We Learned
- **Never** use absolute positioning
- **BorderLayout** for main window structure
- **FlowLayout** for button rows
- **BoxLayout** for toolbars and sidebars
- **GridBagLayout** for complex forms
- **Nested panels** for complex UIs

</div>

<div>

### Best Practices
- Always prefer `pack()` over `setSize()`
- Nest panels with simple layouts
- Use GridBagConstraints wisely
- Test with different font scalings
- Consider localization from the start

</div>

</div>

<div class="mt-8 text-center">

### Next: Chapter 3 - Event-Driven Architecture

Learn the **Observer pattern**, **ActionListener**, and **Key Bindings**

</div>

<!--
You now have the foundation for building professional Swing UIs. Remember: start with BorderLayout, add nested panels with simpler layouts, and only reach for GridBagLayout when you need precise form control.
-->
