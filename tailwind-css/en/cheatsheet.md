# Tailwind CSS v4 Cheat Sheet

**Persona/Use Context:** Intermediate developers adopting Tailwind CSS v4 for daily work
**Tested/Assumptions:** Tailwind CSS v4.0+, Node.js 18+, Vite or PostCSS, modern browsers (Chrome 111+, Firefox 128+, Safari 16.4+)

## Do / Don't Summary

| Do | Don't |
|----|-------|
| Use `@theme` directive for design tokens | Use `tailwind.config.js` (deprecated pattern) |
| Use `@import "tailwindcss"` single import | Use `@tailwind base/components/utilities` |
| Let Tailwind auto-detect content via `.gitignore` | Manually configure content paths unless needed |

---

## 1) Quick Start / Installation

### Vite Plugin (Recommended)

```bash
# 1. Install
npm install tailwindcss @tailwindcss/vite
```

```js
// 2. vite.config.js
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
})
```

```css
/* 3. src/app.css - Single line, that's it */
@import "tailwindcss";
```

### PostCSS Method

```bash
npm install tailwindcss @tailwindcss/postcss
```

```js
// postcss.config.js
export default {
  plugins: ["@tailwindcss/postcss"],
}
```

```css
/* src/app.css */
@import "tailwindcss";
```

---

## 2) V4-Specific Features

### The `@theme` Directive

Define design tokens directly in CSS. All values become CSS custom properties AND generate utility classes.

```css
@import "tailwindcss";

@theme {
  /* Colors - generates bg-brand, text-brand, border-brand, etc. */
  --color-brand: #3b82f6;
  --color-brand-dark: #1e40af;

  /* Spacing - generates p-18, m-18, gap-18, w-18, etc. */
  --spacing-18: 4.5rem;

  /* Font families - generates font-display */
  --font-display: "Inter", sans-serif;

  /* Breakpoints - generates md:, lg:, etc. */
  --breakpoint-3xl: 1920px;

  /* Border radius - generates rounded-pill */
  --radius-pill: 9999px;

  /* Shadows - generates shadow-soft */
  --shadow-soft: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

### The `@utility` Directive

Create custom utilities with full variant support (hover, responsive, dark mode).

```css
@utility content-auto {
  content-visibility: auto;
}

@utility scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }
}

/* With functional values */
@utility tab-* {
  tab-size: --value(--tab-size-*, integer, [integer]);
}
```

Usage: `<div class="content-auto hover:scrollbar-hide">`

### The `@custom-variant` Directive

Create custom variants for conditional styling.

```css
/* Dark mode with class toggle (replaces darkMode: 'class' in v3) */
@custom-variant dark (&:where(.dark, .dark *));

/* Custom states */
@custom-variant hocus (&:hover, &:focus);
@custom-variant group-hocus (:merge(.group):hover &, :merge(.group):focus &);

/* Attribute-based */
@custom-variant aria-current (&[aria-current="page"]);
```

Usage: `<a class="hocus:text-blue-500 aria-current:font-bold">`

### The `@source` Directive

Add content sources beyond auto-detection (for packages outside your repo).

```css
@import "tailwindcss";

@source "../node_modules/@acme/ui-components";
@source "../content/**/*.md";
```

### Automatic Content Detection

v4 automatically scans all files not in `.gitignore`. No `content` array needed.

**Excludes by default:**
- Everything in `.gitignore`
- Binary files (images, videos, fonts, zips)
- `node_modules/` (unless using `@source`)

---

## 3) Core Utility Classes

### Layout - Flexbox

| Utility | CSS | Notes |
|---------|-----|-------|
| `flex` | `display: flex` | |
| `inline-flex` | `display: inline-flex` | |
| `flex-row` | `flex-direction: row` | Default |
| `flex-col` | `flex-direction: column` | |
| `flex-row-reverse` | `flex-direction: row-reverse` | |
| `flex-col-reverse` | `flex-direction: column-reverse` | |
| `flex-wrap` | `flex-wrap: wrap` | |
| `flex-nowrap` | `flex-wrap: nowrap` | Default |
| `flex-1` | `flex: 1 1 0%` | Grow and shrink, ignore initial size |
| `flex-auto` | `flex: 1 1 auto` | Grow and shrink, consider initial size |
| `flex-initial` | `flex: 0 1 auto` | Shrink but don't grow |
| `flex-none` | `flex: none` | Prevent grow/shrink |
| `grow` | `flex-grow: 1` | |
| `grow-0` | `flex-grow: 0` | |
| `shrink` | `flex-shrink: 1` | |
| `shrink-0` | `flex-shrink: 0` | Prevent shrinking |

#### Flex Alignment

| Utility | CSS | Use For |
|---------|-----|---------|
| `justify-start` | `justify-content: flex-start` | Main axis start |
| `justify-center` | `justify-content: center` | Main axis center |
| `justify-end` | `justify-content: flex-end` | Main axis end |
| `justify-between` | `justify-content: space-between` | Equal space between |
| `justify-around` | `justify-content: space-around` | Equal space around |
| `justify-evenly` | `justify-content: space-evenly` | Truly equal spacing |
| `items-start` | `align-items: flex-start` | Cross axis start |
| `items-center` | `align-items: center` | Cross axis center |
| `items-end` | `align-items: flex-end` | Cross axis end |
| `items-baseline` | `align-items: baseline` | Text baseline align |
| `items-stretch` | `align-items: stretch` | Default - fill height |
| `self-auto` | `align-self: auto` | |
| `self-start` | `align-self: flex-start` | Override parent items |
| `self-center` | `align-self: center` | |
| `self-end` | `align-self: flex-end` | |

**Common Pattern - Centering:**
```html
<div class="flex items-center justify-center h-screen">
  Perfectly centered
</div>
```

### Layout - Grid

| Utility | CSS | Notes |
|---------|-----|-------|
| `grid` | `display: grid` | |
| `inline-grid` | `display: inline-grid` | |
| `grid-cols-<n>` | `grid-template-columns: repeat(n, minmax(0, 1fr))` | n = 1-12 or any number in v4 |
| `grid-rows-<n>` | `grid-template-rows: repeat(n, minmax(0, 1fr))` | |
| `col-span-<n>` | `grid-column: span n / span n` | Span n columns |
| `col-start-<n>` | `grid-column-start: n` | Start at line n |
| `col-end-<n>` | `grid-column-end: n` | End at line n |
| `row-span-<n>` | `grid-row: span n / span n` | |
| `col-span-full` | `grid-column: 1 / -1` | Span all columns |

**v4 Dynamic Values:** `grid-cols-15`, `grid-rows-7` work without config (any integer).

**Common Pattern - Responsive Grid:**
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
  <div>Item 4</div>
</div>
```

### Layout - Positioning

| Utility | CSS |
|---------|-----|
| `static` | `position: static` |
| `relative` | `position: relative` |
| `absolute` | `position: absolute` |
| `fixed` | `position: fixed` |
| `sticky` | `position: sticky` |

#### Position Offsets

| Utility | CSS | Notes |
|---------|-----|-------|
| `inset-0` | `inset: 0` | All sides |
| `inset-x-0` | `left: 0; right: 0` | Horizontal |
| `inset-y-0` | `top: 0; bottom: 0` | Vertical |
| `top-<n>` | `top: calc(var(--spacing) * n)` | |
| `right-<n>` | `right: calc(var(--spacing) * n)` | |
| `bottom-<n>` | `bottom: calc(var(--spacing) * n)` | |
| `left-<n>` | `left: calc(var(--spacing) * n)` | |
| `top-1/2` | `top: 50%` | Fractional |
| `-top-4` | `top: -1rem` | Negative prefix |

**Common Pattern - Centered Absolute:**
```html
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
  Centered overlay
</div>
```

### Spacing - Padding & Margin

**Base unit:** `--spacing: 0.25rem` (4px). Utilities multiply this value.

| Utility | CSS | Value |
|---------|-----|-------|
| `p-0` | `padding: 0` | 0 |
| `p-1` | `padding: 0.25rem` | 4px |
| `p-2` | `padding: 0.5rem` | 8px |
| `p-4` | `padding: 1rem` | 16px |
| `p-6` | `padding: 1.5rem` | 24px |
| `p-8` | `padding: 2rem` | 32px |
| `px-<n>` | `padding-left/right` | Horizontal |
| `py-<n>` | `padding-top/bottom` | Vertical |
| `pt-<n>` | `padding-top` | Top only |
| `pr-<n>` | `padding-right` | Right only |
| `pb-<n>` | `padding-bottom` | Bottom only |
| `pl-<n>` | `padding-left` | Left only |
| `ps-<n>` | `padding-inline-start` | Logical start (RTL-aware) |
| `pe-<n>` | `padding-inline-end` | Logical end (RTL-aware) |

**Margin:** Same pattern with `m-`, `mx-`, `my-`, `mt-`, `mr-`, `mb-`, `ml-`, `ms-`, `me-`

**Auto margin:**
| Utility | Use Case |
|---------|----------|
| `mx-auto` | Center block horizontally |
| `ml-auto` | Push to right |
| `mr-auto` | Push to left |

**v4 Dynamic Values:** `p-17`, `m-23` work without config (any integer multiplies `--spacing`).

### Spacing - Gap

| Utility | CSS |
|---------|-----|
| `gap-<n>` | `gap: calc(var(--spacing) * n)` |
| `gap-x-<n>` | `column-gap: ...` |
| `gap-y-<n>` | `row-gap: ...` |

```html
<div class="flex gap-4">...</div>
<div class="grid grid-cols-3 gap-x-8 gap-y-4">...</div>
```

### Typography

#### Font Family

| Utility | CSS |
|---------|-----|
| `font-sans` | `font-family: ui-sans-serif, system-ui, sans-serif, ...` |
| `font-serif` | `font-family: ui-serif, Georgia, Cambria, ...` |
| `font-mono` | `font-family: ui-monospace, SFMono-Regular, ...` |

#### Font Size

| Utility | Size | Line Height |
|---------|------|-------------|
| `text-xs` | 0.75rem (12px) | 1rem |
| `text-sm` | 0.875rem (14px) | 1.25rem |
| `text-base` | 1rem (16px) | 1.5rem |
| `text-lg` | 1.125rem (18px) | 1.75rem |
| `text-xl` | 1.25rem (20px) | 1.75rem |
| `text-2xl` | 1.5rem (24px) | 2rem |
| `text-3xl` | 1.875rem (30px) | 2.25rem |
| `text-4xl` | 2.25rem (36px) | 2.5rem |
| `text-5xl` | 3rem (48px) | 1 |
| `text-6xl` | 3.75rem (60px) | 1 |
| `text-7xl` | 4.5rem (72px) | 1 |
| `text-8xl` | 6rem (96px) | 1 |
| `text-9xl` | 8rem (128px) | 1 |

#### Font Weight

| Utility | Weight |
|---------|--------|
| `font-thin` | 100 |
| `font-extralight` | 200 |
| `font-light` | 300 |
| `font-normal` | 400 |
| `font-medium` | 500 |
| `font-semibold` | 600 |
| `font-bold` | 700 |
| `font-extrabold` | 800 |
| `font-black` | 900 |

#### Text Alignment & Style

| Utility | CSS |
|---------|-----|
| `text-left` | `text-align: left` |
| `text-center` | `text-align: center` |
| `text-right` | `text-align: right` |
| `text-justify` | `text-align: justify` |
| `italic` | `font-style: italic` |
| `not-italic` | `font-style: normal` |
| `uppercase` | `text-transform: uppercase` |
| `lowercase` | `text-transform: lowercase` |
| `capitalize` | `text-transform: capitalize` |
| `normal-case` | `text-transform: none` |
| `underline` | `text-decoration: underline` |
| `line-through` | `text-decoration: line-through` |
| `no-underline` | `text-decoration: none` |

#### Letter & Line Spacing

| Utility | CSS |
|---------|-----|
| `tracking-tighter` | `letter-spacing: -0.05em` |
| `tracking-tight` | `letter-spacing: -0.025em` |
| `tracking-normal` | `letter-spacing: 0` |
| `tracking-wide` | `letter-spacing: 0.025em` |
| `tracking-wider` | `letter-spacing: 0.05em` |
| `tracking-widest` | `letter-spacing: 0.1em` |
| `leading-none` | `line-height: 1` |
| `leading-tight` | `line-height: 1.25` |
| `leading-snug` | `line-height: 1.375` |
| `leading-normal` | `line-height: 1.5` |
| `leading-relaxed` | `line-height: 1.625` |
| `leading-loose` | `line-height: 2` |
| `leading-<n>` | `line-height: calc(n * 0.25rem)` |

#### Text Overflow

| Utility | Effect |
|---------|--------|
| `truncate` | Single line with ellipsis |
| `text-ellipsis` | `text-overflow: ellipsis` |
| `text-clip` | `text-overflow: clip` |
| `line-clamp-<n>` | Clamp to n lines with ellipsis |

```html
<p class="truncate">Very long text that will be truncated...</p>
<p class="line-clamp-3">Text clamped to 3 lines...</p>
```

### Colors

v4 uses **OKLCH** color space for more vivid colors on modern displays.

#### Text Colors

| Utility | Effect |
|---------|--------|
| `text-inherit` | Inherit from parent |
| `text-current` | Use `currentColor` |
| `text-transparent` | Transparent |
| `text-black` | `#000` |
| `text-white` | `#fff` |
| `text-<color>-<shade>` | Color palette (e.g., `text-blue-500`) |

**Color palette:** slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose

**Shades:** 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950

#### Opacity Modifier

```html
<p class="text-blue-500/75">75% opacity blue text</p>
<p class="text-blue-500/[.35]">35% opacity (arbitrary)</p>
```

#### Background Colors

Same pattern: `bg-<color>-<shade>` with optional `/opacity`

```html
<div class="bg-slate-100">Light background</div>
<div class="bg-blue-500/50">50% opacity background</div>
<div class="bg-gradient-to-r from-cyan-500 to-blue-500">Gradient</div>
```

#### Border Colors

```html
<div class="border border-gray-300">Default border</div>
<div class="border-2 border-red-500/75">Red with opacity</div>
```

#### Gradients (v4 Enhanced)

| Utility | Direction |
|---------|-----------|
| `bg-linear-to-t` | Bottom to top |
| `bg-linear-to-b` | Top to bottom |
| `bg-linear-to-l` | Right to left |
| `bg-linear-to-r` | Left to right |
| `bg-linear-to-tr` | To top right |
| `bg-linear-to-br` | To bottom right |
| `bg-linear-<angle>` | Specific angle (e.g., `bg-linear-45`) |
| `bg-radial` | Radial gradient |
| `bg-conic` | Conic gradient |

**Note:** `bg-gradient-*` renamed to `bg-linear-*` in v4.

```html
<!-- Linear gradient -->
<div class="bg-linear-to-r from-indigo-500 via-purple-500 to-pink-500">
  Gradient with via color
</div>

<!-- Angled gradient (v4 new) -->
<div class="bg-linear-45 from-cyan-400 to-blue-600">
  45-degree gradient
</div>

<!-- Color interpolation (v4 new) -->
<div class="bg-linear-to-r/oklch from-blue-500 to-green-500">
  OKLCH interpolation (more vivid)
</div>
```

### Sizing

#### Width

| Utility | CSS |
|---------|-----|
| `w-0` | `width: 0` |
| `w-px` | `width: 1px` |
| `w-<n>` | `width: calc(var(--spacing) * n)` |
| `w-auto` | `width: auto` |
| `w-full` | `width: 100%` |
| `w-screen` | `width: 100vw` |
| `w-svw` | `width: 100svw` (small viewport) |
| `w-lvw` | `width: 100lvw` (large viewport) |
| `w-dvw` | `width: 100dvw` (dynamic viewport) |
| `w-min` | `width: min-content` |
| `w-max` | `width: max-content` |
| `w-fit` | `width: fit-content` |
| `w-1/2` | `width: 50%` |
| `w-1/3` | `width: 33.333%` |
| `w-2/3` | `width: 66.667%` |
| `w-1/4` | `width: 25%` |
| `w-3/4` | `width: 75%` |

**Height:** Same pattern with `h-`, plus `h-screen`, `h-svh`, `h-lvh`, `h-dvh`

#### Size (Width + Height)

| Utility | CSS |
|---------|-----|
| `size-<n>` | `width: ...; height: ...` |
| `size-full` | `width: 100%; height: 100%` |

```html
<div class="size-12">48px square</div>
<img class="size-full object-cover" src="..." />
```

#### Min/Max Width & Height

| Utility | CSS |
|---------|-----|
| `min-w-0` | `min-width: 0` |
| `min-w-full` | `min-width: 100%` |
| `min-w-min` | `min-width: min-content` |
| `min-w-max` | `min-width: max-content` |
| `min-w-fit` | `min-width: fit-content` |
| `max-w-none` | `max-width: none` |
| `max-w-xs` | `max-width: 20rem` (320px) |
| `max-w-sm` | `max-width: 24rem` (384px) |
| `max-w-md` | `max-width: 28rem` (448px) |
| `max-w-lg` | `max-width: 32rem` (512px) |
| `max-w-xl` | `max-width: 36rem` (576px) |
| `max-w-2xl` | `max-width: 42rem` (672px) |
| `max-w-3xl` | `max-width: 48rem` (768px) |
| `max-w-4xl` | `max-width: 56rem` (896px) |
| `max-w-5xl` | `max-width: 64rem` (1024px) |
| `max-w-6xl` | `max-width: 72rem` (1152px) |
| `max-w-7xl` | `max-width: 80rem` (1280px) |
| `max-w-full` | `max-width: 100%` |
| `max-w-prose` | `max-width: 65ch` (readable) |
| `max-w-screen-sm` | `max-width: 640px` |
| `max-w-screen-md` | `max-width: 768px` |
| `max-w-screen-lg` | `max-width: 1024px` |
| `max-w-screen-xl` | `max-width: 1280px` |
| `max-w-screen-2xl` | `max-width: 1536px` |

**Min/Max Height:** `min-h-0`, `min-h-full`, `min-h-screen`, `min-h-svh`, `min-h-dvh`, `max-h-<n>`, etc.

### Borders

#### Border Width

| Utility | CSS |
|---------|-----|
| `border` | `border-width: 1px` |
| `border-0` | `border-width: 0` |
| `border-2` | `border-width: 2px` |
| `border-4` | `border-width: 4px` |
| `border-8` | `border-width: 8px` |
| `border-t-<n>` | Top border |
| `border-r-<n>` | Right border |
| `border-b-<n>` | Bottom border |
| `border-l-<n>` | Left border |
| `border-x-<n>` | Left + right |
| `border-y-<n>` | Top + bottom |
| `border-s-<n>` | Inline start (RTL-aware) |
| `border-e-<n>` | Inline end (RTL-aware) |

#### Border Radius

| Utility | CSS |
|---------|-----|
| `rounded-none` | `border-radius: 0` |
| `rounded-sm` | `border-radius: 0.125rem` |
| `rounded` | `border-radius: 0.25rem` |
| `rounded-md` | `border-radius: 0.375rem` |
| `rounded-lg` | `border-radius: 0.5rem` |
| `rounded-xl` | `border-radius: 0.75rem` |
| `rounded-2xl` | `border-radius: 1rem` |
| `rounded-3xl` | `border-radius: 1.5rem` |
| `rounded-full` | `border-radius: 9999px` |

**Corner-specific:** `rounded-t-*`, `rounded-r-*`, `rounded-b-*`, `rounded-l-*`, `rounded-tl-*`, `rounded-tr-*`, `rounded-bl-*`, `rounded-br-*`

#### Border Style

| Utility | CSS |
|---------|-----|
| `border-solid` | `border-style: solid` |
| `border-dashed` | `border-style: dashed` |
| `border-dotted` | `border-style: dotted` |
| `border-double` | `border-style: double` |
| `border-hidden` | `border-style: hidden` |
| `border-none` | `border-style: none` |

### Effects

#### Box Shadow

| Utility | Effect |
|---------|--------|
| `shadow-sm` | Small shadow |
| `shadow` | Default shadow |
| `shadow-md` | Medium shadow |
| `shadow-lg` | Large shadow |
| `shadow-xl` | Extra large |
| `shadow-2xl` | Largest |
| `shadow-inner` | Inset shadow |
| `shadow-none` | No shadow |
| `shadow-<color>` | Shadow color (e.g., `shadow-blue-500/50`) |

**v4 New - Inset Shadow & Ring (stackable):**
```html
<div class="shadow-lg inset-shadow-sm inset-ring-1 inset-ring-black/5">
  Multiple layered shadows
</div>
```

#### Opacity

| Utility | CSS |
|---------|-----|
| `opacity-0` | `opacity: 0` |
| `opacity-5` | `opacity: 0.05` |
| `opacity-10` | `opacity: 0.1` |
| `opacity-25` | `opacity: 0.25` |
| `opacity-50` | `opacity: 0.5` |
| `opacity-75` | `opacity: 0.75` |
| `opacity-100` | `opacity: 1` |

**Arbitrary:** `opacity-[.67]`

#### Ring (Focus Outlines)

| Utility | Effect |
|---------|--------|
| `ring` | 3px ring |
| `ring-0` | No ring |
| `ring-1` | 1px ring |
| `ring-2` | 2px ring |
| `ring-4` | 4px ring |
| `ring-8` | 8px ring |
| `ring-inset` | Inset ring |
| `ring-<color>` | Ring color |
| `ring-offset-<n>` | Ring offset width |
| `ring-offset-<color>` | Ring offset color |

```html
<button class="focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Focused button
</button>
```

---

## 4) Responsive Design

### Breakpoint Prefixes

| Prefix | Min-Width | CSS |
|--------|-----------|-----|
| `sm:` | 640px | `@media (min-width: 640px)` |
| `md:` | 768px | `@media (min-width: 768px)` |
| `lg:` | 1024px | `@media (min-width: 1024px)` |
| `xl:` | 1280px | `@media (min-width: 1280px)` |
| `2xl:` | 1536px | `@media (min-width: 1536px)` |

**Mobile-first:** Unprefixed utilities apply at all sizes. Prefixed utilities apply at that breakpoint AND UP.

```html
<!-- 1 column on mobile, 2 on tablet, 4 on desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
```

### Max-Width Breakpoints

| Prefix | Max-Width | CSS |
|--------|-----------|-----|
| `max-sm:` | 639px | `@media (max-width: 639px)` |
| `max-md:` | 767px | `@media (max-width: 767px)` |
| `max-lg:` | 1023px | `@media (max-width: 1023px)` |
| `max-xl:` | 1279px | `@media (max-width: 1279px)` |
| `max-2xl:` | 1535px | `@media (max-width: 1535px)` |

```html
<!-- Only visible below md breakpoint -->
<div class="max-md:block md:hidden">Mobile only</div>
```

### Breakpoint Ranges

Combine min and max for specific ranges:

```html
<!-- Only visible between md and xl -->
<div class="hidden md:block xl:hidden">Tablet only</div>

<!-- Using min-* and max-* together -->
<div class="md:max-xl:bg-blue-500">Blue only between md and xl</div>
```

### Container Queries (v4 Built-in)

| Prefix | Container Min-Width |
|--------|---------------------|
| `@xs:` | 320px |
| `@sm:` | 384px |
| `@md:` | 448px |
| `@lg:` | 512px |
| `@xl:` | 576px |
| `@2xl:` | 672px |
| `@3xl:` | 768px |
| `@4xl:` | 896px |
| `@5xl:` | 1024px |

**Max-width container queries:** `@max-sm:`, `@max-md:`, etc.

```html
<div class="@container">
  <div class="@md:flex @md:gap-4">
    Flexbox when container is 448px+ wide
  </div>
</div>

<!-- Named containers -->
<div class="@container/sidebar">
  <nav class="@md/sidebar:flex-col">...</nav>
</div>
```

---

## 5) Dark Mode

### Enable Class-Based Dark Mode (v4)

```css
@import "tailwindcss";

/* Enable dark mode via .dark class on html/body */
@custom-variant dark (&:where(.dark, .dark *));
```

### Usage

```html
<!-- Add .dark to root element -->
<html class="dark">
  <body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
    <p class="text-gray-600 dark:text-gray-400">Content</p>
  </body>
</html>
```

### System Preference Dark Mode

Without `@custom-variant`, dark mode follows `prefers-color-scheme`:

```html
<div class="bg-white dark:bg-black">
  Follows system preference
</div>
```

### Common Dark Mode Patterns

```html
<!-- Card with dark mode -->
<div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-6">
  <h2 class="text-gray-900 dark:text-white">Title</h2>
  <p class="text-gray-600 dark:text-gray-400">Description</p>
</div>

<!-- Button with dark mode -->
<button class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-500 text-white">
  Click me
</button>
```

---

## 6) State Variants

### Interactive States

| Variant | CSS Selector | Use Case |
|---------|--------------|----------|
| `hover:` | `:hover` | Mouse over |
| `focus:` | `:focus` | Focused element |
| `focus-visible:` | `:focus-visible` | Keyboard focus only |
| `focus-within:` | `:focus-within` | Child has focus |
| `active:` | `:active` | Being clicked |
| `visited:` | `:visited` | Visited links |
| `target:` | `:target` | URL fragment target |

### Form States

| Variant | CSS Selector | Use Case |
|---------|--------------|----------|
| `disabled:` | `:disabled` | Disabled inputs |
| `enabled:` | `:enabled` | Enabled inputs |
| `checked:` | `:checked` | Checked checkbox/radio |
| `indeterminate:` | `:indeterminate` | Indeterminate checkbox |
| `invalid:` | `:invalid` | Invalid input |
| `valid:` | `:valid` | Valid input |
| `required:` | `:required` | Required field |
| `optional:` | `:optional` | Optional field |
| `read-only:` | `:read-only` | Read-only input |
| `placeholder-shown:` | `:placeholder-shown` | Placeholder visible |
| `autofill:` | `:autofill` | Autofilled by browser |

### Structural States

| Variant | CSS Selector | Use Case |
|---------|--------------|----------|
| `first:` | `:first-child` | First child |
| `last:` | `:last-child` | Last child |
| `only:` | `:only-child` | Only child |
| `odd:` | `:nth-child(odd)` | Odd children |
| `even:` | `:nth-child(even)` | Even children |
| `first-of-type:` | `:first-of-type` | First of type |
| `last-of-type:` | `:last-of-type` | Last of type |
| `empty:` | `:empty` | No children |

### v4 New Variants

| Variant | CSS Selector | Use Case |
|---------|--------------|----------|
| `inert:` | `[inert]` | Inert elements |
| `nth-<n>:` | `:nth-child(n)` | Specific child |
| `nth-last-<n>:` | `:nth-last-child(n)` | From end |
| `in-<name>:` | Implicit group | Like `group-*` without `group` class |
| `not-<variant>:` | `:not()` | Negate variant |
| `starting:` | `@starting-style` | Entry animations |

### Group & Peer Variants

```html
<!-- Group: style child based on parent state -->
<div class="group">
  <span class="group-hover:text-blue-500">Hover parent</span>
</div>

<!-- Named groups -->
<div class="group/card">
  <span class="group-hover/card:underline">...</span>
</div>

<!-- Peer: style sibling based on previous sibling state -->
<input class="peer" />
<span class="peer-invalid:text-red-500">Error message</span>
```

### Data Attributes (v4 Dynamic)

```html
<!-- Boolean data attributes work without config -->
<div data-loading class="data-loading:opacity-50">...</div>
<div data-active class="data-active:bg-blue-100">...</div>

<!-- Value-based -->
<div data-size="lg" class="data-[size=lg]:text-xl">...</div>
```

### ARIA Attributes

```html
<div aria-expanded="true" class="aria-expanded:rotate-180">
  Expand icon
</div>

<div aria-disabled="true" class="aria-disabled:opacity-50">
  Disabled section
</div>
```

---

## 7) Creating Custom Classes

### Using `@apply` (Component Classes)

Use `@layer components` with `@apply` to compose utility classes:

```css
@import "tailwindcss";

@layer components {
  .btn {
    @apply px-4 py-2 rounded-lg font-medium transition-colors;
  }

  .btn-primary {
    @apply btn bg-blue-500 text-white hover:bg-blue-600;
  }

  .btn-secondary {
    @apply btn bg-gray-200 text-gray-800 hover:bg-gray-300;
  }

  .card {
    @apply bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6;
  }

  .input {
    @apply w-full px-4 py-2 border border-gray-300 rounded-lg
           focus:ring-2 focus:ring-blue-500 focus:border-transparent
           dark:bg-gray-800 dark:border-gray-600;
  }
}
```

### When to Use `@apply` vs Inline Utilities

| Use `@apply` | Use Inline Utilities |
|--------------|----------------------|
| Repeated patterns (buttons, cards, inputs) | One-off layouts |
| Multi-element components | Simple styling |
| Framework constraints (no class access) | Rapid prototyping |
| Style variants (btn-primary, btn-secondary) | Responsive variations |

**Recommendation:** Prefer inline utilities. Use `@apply` sparingly for true design system components.

### Using `@theme` for Design Tokens

```css
@import "tailwindcss";

@theme {
  /* Brand colors - generates text-brand, bg-brand, border-brand, etc. */
  --color-brand-50: #eff6ff;
  --color-brand-100: #dbeafe;
  --color-brand-500: #3b82f6;
  --color-brand-600: #2563eb;
  --color-brand-700: #1d4ed8;

  /* Semantic colors */
  --color-success: #22c55e;
  --color-warning: #f59e0b;
  --color-error: #ef4444;

  /* Custom spacing */
  --spacing-18: 4.5rem;
  --spacing-22: 5.5rem;

  /* Custom fonts */
  --font-display: "Cal Sans", sans-serif;
  --font-body: "Inter", sans-serif;

  /* Custom shadows */
  --shadow-card: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-glow: 0 0 20px rgb(59 130 246 / 0.5);

  /* Custom radius */
  --radius-button: 0.5rem;
  --radius-card: 1rem;

  /* Custom breakpoints */
  --breakpoint-xs: 475px;
  --breakpoint-3xl: 1920px;
}
```

Usage:
```html
<div class="bg-brand-500 text-white p-18 rounded-card shadow-card">
  <h1 class="font-display text-3xl">Custom tokens in action</h1>
</div>
```

### Using `@utility` for Custom Utilities

Create utilities with full variant support (hover, responsive, dark mode):

```css
@import "tailwindcss";

/* Simple utility */
@utility content-auto {
  content-visibility: auto;
}

/* Utility with multiple properties */
@utility text-balance {
  text-wrap: balance;
}

@utility scrollbar-thin {
  scrollbar-width: thin;
}

@utility scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }
}

/* Functional utility with values */
@utility text-shadow-* {
  text-shadow: 0 2px 4px var(--tw-shadow-color, rgb(0 0 0 / 0.1));
}
```

Usage:
```html
<div class="content-auto hover:scrollbar-thin">
  <h1 class="text-balance">Long headline that wraps nicely</h1>
</div>
```

### Combining Approaches

```css
@import "tailwindcss";

/* 1. Design tokens */
@theme {
  --color-primary: #3b82f6;
  --color-primary-hover: #2563eb;
  --radius-button: 0.5rem;
}

/* 2. Custom variant */
@custom-variant dark (&:where(.dark, .dark *));

/* 3. Custom utility */
@utility animate-fade-in {
  animation: fadeIn 0.3s ease-out;
}

/* 4. Component classes */
@layer components {
  .btn-primary {
    @apply bg-primary text-white px-4 py-2 rounded-button
           hover:bg-primary-hover transition-colors
           focus:ring-2 focus:ring-primary/50;
  }
}

/* 5. Keyframes */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## 8) Quick Reference Tables

### Arbitrary Value Syntax

| Type | Syntax | Example |
|------|--------|---------|
| Spacing | `<utility>-[<value>]` | `p-[13px]`, `m-[2.5rem]` |
| Colors | `<utility>-[<color>]` | `bg-[#1a1a1a]`, `text-[rgb(255,0,0)]` |
| Sizing | `w-[<value>]` | `w-[300px]`, `h-[calc(100vh-80px)]` |
| Position | `top-[<value>]` | `top-[117px]`, `left-[50%]` |
| Font size | `text-[<size>]` | `text-[22px]`, `text-[1.375rem]` |
| Grid | `grid-cols-[<template>]` | `grid-cols-[200px_1fr_200px]` |
| Line height | `leading-[<value>]` | `leading-[1.7]` |
| Z-index | `z-[<value>]` | `z-[999]`, `z-[-1]` |

### CSS Property Reference

| Utility Type | CSS Property | Example |
|--------------|--------------|---------|
| `text-*` | `color` | `text-blue-500` |
| `bg-*` | `background-color` | `bg-slate-100` |
| `border-*` | `border-color` | `border-gray-300` |
| `ring-*` | `box-shadow` (ring) | `ring-blue-500` |
| `divide-*` | `border-color` (children) | `divide-gray-200` |
| `placeholder-*` | `::placeholder color` | `placeholder-gray-400` |
| `outline-*` | `outline-color` | `outline-blue-500` |
| `accent-*` | `accent-color` | `accent-pink-500` |
| `caret-*` | `caret-color` | `caret-blue-500` |
| `fill-*` | `fill` | `fill-current` |
| `stroke-*` | `stroke` | `stroke-blue-500` |

### Common Utility Patterns

```html
<!-- Centered container -->
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

<!-- Aspect ratio -->
<div class="aspect-video">

<!-- Truncate text -->
<p class="truncate">

<!-- Visually hidden (accessible) -->
<span class="sr-only">

<!-- Cover image -->
<img class="w-full h-full object-cover">

<!-- Sticky header -->
<header class="sticky top-0 z-50 bg-white/80 backdrop-blur">

<!-- Skeleton loader -->
<div class="animate-pulse bg-gray-200 rounded h-4 w-3/4">

<!-- Focus ring (accessible) -->
<button class="focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500">

<!-- Disabled state -->
<button class="disabled:opacity-50 disabled:cursor-not-allowed" disabled>
```

---

## 9) Pitfalls & Anti-Patterns

### Don't: Dynamically construct class names

```html
<!-- BAD: Tailwind can't detect these -->
<div class="bg-{{ color }}-500">
<div class={`text-${size}`}>
```

**Why:** Tailwind scans source files for complete class names. Dynamic strings aren't detected.

**Fix:** Use complete class names or safelist:
```html
<!-- GOOD: Use complete classes -->
<div class="{{ color === 'red' ? 'bg-red-500' : 'bg-blue-500' }}">

<!-- Or map to full classes -->
const sizes = { sm: 'text-sm', md: 'text-base', lg: 'text-lg' }
<div class={sizes[size]}>
```

### Don't: Overuse `@apply`

```css
/* BAD: Defeats the purpose of utility-first */
.my-component {
  @apply flex items-center justify-between p-4 bg-white rounded-lg shadow-md
         hover:shadow-lg transition-shadow duration-200 border border-gray-200
         dark:bg-gray-800 dark:border-gray-700;
}
```

**Why:** Creates abstraction without benefit. Hard to modify. Increases CSS size.

**Fix:** Use inline utilities or create meaningful component classes:
```html
<!-- GOOD: Inline for one-off uses -->
<div class="flex items-center justify-between p-4 ...">

<!-- GOOD: Component class for true reuse -->
.card { @apply bg-white rounded-lg shadow-md p-4; }
```

### Don't: Use v3 syntax in v4

```css
/* BAD: v3 syntax */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* BAD: v3 gradient syntax */
<div class="bg-gradient-to-r">
```

**Fix:**
```css
/* GOOD: v4 syntax */
@import "tailwindcss";

/* GOOD: v4 gradient syntax */
<div class="bg-linear-to-r">
```

### Don't: Forget v4 dark mode setup

```html
<!-- BAD: Won't work without @custom-variant -->
<div class="dark:bg-gray-900">
```

**Fix:** Add custom variant if using class-based toggle:
```css
@custom-variant dark (&:where(.dark, .dark *));
```

---

## 10) Debugging / Troubleshooting

### Symptom: Classes not applying

**Likely causes:**
1. File not being scanned
2. Class name dynamically constructed
3. Build not running

**Fast checks:**
```bash
# Check if file is in .gitignore (would be excluded)
git check-ignore src/components/MyComponent.tsx

# Check build output
npx tailwindcss --input ./src/app.css --output ./dist/output.css
```

**Fixes:**
- Add `@source` directive for external packages
- Use complete class names, not dynamic strings
- Restart dev server

### Symptom: Dark mode not working

**Likely causes:**
1. Missing `@custom-variant` for class-based toggle
2. `.dark` class not on root element
3. Conflicting specificity

**Fast checks:**
```css
/* Verify in your CSS */
@custom-variant dark (&:where(.dark, .dark *));
```

```html
<!-- Verify .dark is on html or body -->
<html class="dark">
```

### Symptom: Custom theme values not generating utilities

**Likely causes:**
1. Wrong namespace prefix
2. Syntax error in `@theme`

**Fast checks:**
```css
/* Verify correct namespaces */
@theme {
  --color-*: ...;    /* for bg-*, text-*, border-* */
  --spacing-*: ...;  /* for p-*, m-*, w-*, h-*, gap-* */
  --font-*: ...;     /* for font-* */
  --shadow-*: ...;   /* for shadow-* */
  --radius-*: ...;   /* for rounded-* */
}
```

### Symptom: Vite HMR not updating styles

**Fix:**
```js
// vite.config.js - Ensure plugin is first
export default defineConfig({
  plugins: [
    tailwindcss(), // Should be first
    react(),
  ],
})
```

---

## 11) Production-Ready Example

Complete card component using v4 features:

```css
/* app.css */
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));

@theme {
  --color-brand-500: #6366f1;
  --color-brand-600: #4f46e5;
  --shadow-card: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --radius-card: 0.75rem;
}

@utility line-clamp-* {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: --value(integer);
  overflow: hidden;
}

@layer components {
  .btn {
    @apply inline-flex items-center justify-center px-4 py-2
           font-medium rounded-lg transition-colors
           focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2
           disabled:opacity-50 disabled:cursor-not-allowed;
  }

  .btn-primary {
    @apply btn bg-brand-500 text-white
           hover:bg-brand-600 focus-visible:ring-brand-500;
  }
}
```

```html
<!-- Component usage -->
<article class="@container">
  <div class="bg-white dark:bg-gray-800 rounded-card shadow-card overflow-hidden
              @md:flex @md:gap-6">
    <!-- Image -->
    <div class="@md:w-48 @md:shrink-0">
      <img
        src="/placeholder.jpg"
        alt="Article thumbnail"
        class="w-full h-48 @md:h-full object-cover"
      />
    </div>

    <!-- Content -->
    <div class="p-6 flex flex-col">
      <span class="text-sm text-brand-500 dark:text-brand-400 font-medium">
        Category
      </span>

      <h2 class="mt-2 text-xl font-semibold text-gray-900 dark:text-white
                 group-hover:text-brand-500 transition-colors">
        Article Title Goes Here
      </h2>

      <p class="mt-2 text-gray-600 dark:text-gray-400 line-clamp-2">
        This is a brief description of the article that might be quite long
        but will be clamped to two lines for consistent card heights.
      </p>

      <div class="mt-4 flex items-center gap-4">
        <img
          src="/avatar.jpg"
          alt="Author"
          class="size-10 rounded-full"
        />
        <div>
          <p class="text-sm font-medium text-gray-900 dark:text-white">
            Author Name
          </p>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            Jan 8, 2026
          </p>
        </div>
      </div>

      <div class="mt-auto pt-4">
        <button class="btn-primary">
          Read More
        </button>
      </div>
    </div>
  </div>
</article>
```

---

## 12) v3 to v4 Breaking Changes (Quick Reference)

| v3 | v4 | Notes |
|----|-----|-------|
| `tailwind.config.js` | `@theme` in CSS | JS config still works via `@config` |
| `@tailwind base/components/utilities` | `@import "tailwindcss"` | Single import |
| `content: [...]` | Auto-detected | Uses `.gitignore` heuristics |
| `darkMode: 'class'` | `@custom-variant dark (...)` | In CSS |
| `bg-gradient-to-r` | `bg-linear-to-r` | Renamed |
| `bg-opacity-50` | `bg-black/50` | Use opacity modifier |
| `text-opacity-50` | `text-black/50` | Use opacity modifier |
| `addUtilities()` plugin | `@utility` | CSS-first |
| `addVariant()` plugin | `@custom-variant` | CSS-first |
| Container queries plugin | Built-in | `@container`, `@sm:` |

---

## 13) Versioning & Maintenance Metadata

* **Doc version:** 1.0.0
* **Tailwind version:** v4.0.0 (released January 22, 2025)
* **Validated on:** January 8, 2026
* **Drift risks:**
  - Color palette values may change in minor releases
  - New utilities added frequently
  - Container query breakpoints may be adjusted

### Revalidation Checklist

1. Check [Tailwind CSS Releases](https://github.com/tailwindlabs/tailwindcss/releases) for breaking changes
2. Verify `@theme` namespace syntax against [Theme Variables docs](https://tailwindcss.com/docs/theme)
3. Test `@utility` and `@custom-variant` syntax
4. Confirm breakpoint values in default theme
5. Check for deprecated utilities
6. Verify dark mode setup instructions

---

## 14) Further Reading

* [Tailwind CSS v4.0 Announcement](https://tailwindcss.com/blog/tailwindcss-v4) - Official release notes
* [Installation Guide](https://tailwindcss.com/docs/installation) - Setup for various frameworks
* [Upgrade Guide](https://tailwindcss.com/docs/upgrade-guide) - v3 to v4 migration
* [Theme Variables](https://tailwindcss.com/docs/theme) - `@theme` directive reference
* [Detecting Classes in Source Files](https://tailwindcss.com/docs/detecting-classes-in-source-files) - Content detection and `@source`
