# Module 2: FlowLayout & BoxLayout Quick Start

**Duration**: 5 minutes
**Focus Keyword**: Java FlowLayout BoxLayout comparison
**Target Audience**: Java developers learning Swing GUI

---

## Video Script

### [0:00-0:30] Hook

**VISUAL**: Row of buttons that wraps beautifully on resize vs vertical toolbar with perfect spacing

**NARRATION**:
"You've mastered BorderLayout for your main window structure. But what about that row of buttons at the bottom? Or that vertical toolbar on the side? Today, I'll show you two lightweight layouts that handle these cases perfectly: FlowLayout and BoxLayout."

---

### [0:30-1:30] FlowLayout: The Text Wrapper

**VISUAL**: Animation of buttons flowing like text in a paragraph

**NARRATION**:
"Think of FlowLayout like text in a word processor. Components go left to right. When the container runs out of width, they wrap to the next line.

Here's the beautiful part: FlowLayout is the DEFAULT for JPanel. You don't even need to set it."

**VISUAL**: Code appearing line by line

```java
JPanel buttonBar = new JPanel(); // FlowLayout by default!
buttonBar.add(new JButton("OK"));
buttonBar.add(new JButton("Cancel"));
buttonBar.add(new JButton("Apply"));
```

"Add your buttons. That's it. FlowLayout respects each button's preferred size and arranges them automatically."

**VISUAL**: Window resizing, buttons wrapping

"Watch what happens when I resize. The buttons stay together, wrapping when needed. Perfect for button bars and toolbar rows."

---

### [1:30-2:30] FlowLayout Alignment Options

**VISUAL**: Three button bars with LEFT, CENTER, RIGHT alignment

**NARRATION**:
"FlowLayout has one more trick. You can control alignment.

FlowLayout.LEFT pushes buttons to the left edge. Great for action buttons in a dialog.

FlowLayout.CENTER, the default, centers everything. Good for splash screens.

FlowLayout.RIGHT pushes to the right. Perfect for those OK/Cancel buttons at the bottom of a form."

```java
// Right-aligned button bar
JPanel buttonBar = new JPanel(new FlowLayout(FlowLayout.RIGHT));
buttonBar.add(new JButton("Cancel"));
buttonBar.add(new JButton("OK"));
```

---

### [2:30-4:00] BoxLayout: The Stacker

**VISUAL**: Vertical sidebar being built component by component

**NARRATION**:
"Now let's talk BoxLayout. While FlowLayout flows horizontally and wraps, BoxLayout stacks components in a single line - either vertical or horizontal - with NO wrapping.

Here's the setup. Notice BoxLayout requires the container as the first argument."

```java
JPanel sidebar = new JPanel();
sidebar.setLayout(new BoxLayout(sidebar, BoxLayout.Y_AXIS));
```

"Y_AXIS means vertical stacking. X_AXIS would be horizontal.

Now here's where BoxLayout gets powerful: spacing control.

Use createVerticalStrut for a fixed gap - say, 10 pixels between buttons.

Use createVerticalGlue for elastic spacing that absorbs extra space."

**VISUAL**: Animation showing strut as rigid bar, glue as spring

```java
sidebar.add(new JButton("Dashboard"));
sidebar.add(Box.createVerticalStrut(10));  // Fixed 10px gap
sidebar.add(new JButton("Reports"));
sidebar.add(Box.createVerticalGlue());     // Absorbs extra space
sidebar.add(new JButton("Settings"));
```

"With glue at the bottom, my top buttons stay grouped together, and Settings gets pushed to the bottom when the window grows."

---

### [4:00-4:30] When to Use Which

**VISUAL**: Decision table appearing

**NARRATION**:
"Here's your cheat sheet.

Use FlowLayout when you want buttons to wrap - like a button bar or toolbar that adapts to width.

Use BoxLayout when you want precise vertical stacking with controlled spacing - like a sidebar or vertical toolbar.

And remember: FlowLayout is the JPanel default. BoxLayout needs explicit setup."

| Need | Use |
|------|-----|
| Row of buttons that wraps | FlowLayout |
| Vertical sidebar with spacing | BoxLayout |
| Horizontal toolbar, no wrap | BoxLayout (X_AXIS) |

---

### [4:30-5:00] Call to Action

**VISUAL**: Code challenge on screen

**NARRATION**:
"Your challenge: Build a dialog with a FlowLayout button bar at the bottom and a BoxLayout sidebar on the left. Combine them using BorderLayout as your container.

Next video: GridBagLayout - the most powerful layout manager for complex forms. Subscribe so you don't miss it."

---

## Micro-Blog Post

### Stop Using GridLayout for Everything

Two underrated Swing layouts that solve 80% of your component arrangement needs:

**FlowLayout** (JPanel default)
- Components flow left-to-right like text
- Wraps to next line when out of space
- Perfect for button bars

```java
JPanel buttons = new JPanel(); // FlowLayout is default!
buttons.add(new JButton("OK"));
buttons.add(new JButton("Cancel"));
```

**BoxLayout** (Manual setup required)
- Stacks in one direction, NO wrapping
- Strut = fixed spacing
- Glue = elastic spacing

```java
JPanel sidebar = new JPanel();
sidebar.setLayout(new BoxLayout(sidebar, BoxLayout.Y_AXIS));
sidebar.add(new JButton("Home"));
sidebar.add(Box.createVerticalGlue()); // Push next items down
sidebar.add(new JButton("Settings"));
```

**The pattern**: Use FlowLayout for rows that adapt. Use BoxLayout for stacks that don't wrap.

Stop overthinking. These two layouts handle buttons, toolbars, and sidebars beautifully.

#Java #Swing #FlowLayout #BoxLayout #GUIDesign

---

## SEO Metadata

```yaml
title: "Java FlowLayout vs BoxLayout: When to Use Each Layout Manager"
description: "Learn the difference between FlowLayout (wrapping button rows) and BoxLayout (precise vertical stacking) in Java Swing. Includes code examples and decision guide."
keywords:
  - Java FlowLayout tutorial
  - Java BoxLayout example
  - FlowLayout vs BoxLayout
  - Swing button bar layout
  - Java vertical layout
  - Box.createVerticalGlue
canonical_url: /tutorials/java-swing/flowlayout-boxlayout-comparison
og_image: /presentations/swing-layout-managers/infographics/02-layout-comparison.png
```

---

## Thumbnail Brief

**Concept**: Side-by-side layout comparison

**Left panel**:
- FlowLayout visualization
- Buttons flowing and wrapping
- Arrow showing wrap behavior
- Text: "FlowLayout"

**Right panel**:
- BoxLayout visualization
- Vertical stack with visible struts/glue
- Spring icon for glue
- Text: "BoxLayout"

**Main text**: "Flow vs Box Layout"
**Subtitle**: "When to use each"

**Style**: Clean comparison, whiteboard aesthetic

**Colors**: Blue and orange panels on dark background
