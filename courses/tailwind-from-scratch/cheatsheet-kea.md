---
title: Fundamentus di Tailwind CSS v4
slug: tailwind-from-scratch
courseSlug: tailwind-from-scratch
language: kea
version: 1.0.0
validated_at: 2026-05-14
trace_id: Skola-course-tailwind-from-scratch-20260513-000000
---

# Tailwind CSS Cheatsheet — Fundamentus di Tailwind CSS v4

**Lingua:** kea (Kabuverdianu) | **Tailwind:** v4.3.0+ | **Doc version:** 1.0.0 | **Validadu na:** 2026-05-14

> **Pa ken?** Prinsipiantes i nivel médiu — programadoris ki ta uza Tailwind v4 pa konstrui interface.
> **Kumo uza:** Referensia rápidu pa konsulta durante kursu. Kopia kódigus diretu pa bo projetu — tudu egzemplus testadu ku v4.3.0+.

---

## Índisi

1. [Setup i Anbienti](#1-setup-i-anbienti)
2. [Utility-First — Fundamentus](#2-utility-first--fundamentus)
3. [Kores i Opasidadi](#3-kores-i-opasidadi)
4. [Spacing — Container, Padding, Margin](#4-spacing--container-padding-margin)
5. [Tipografia](#5-tipografia)
6. [Tamanhu — Largura i Altura](#6-tamanhu--largura-i-altura)
7. [Layout — Display i Position](#7-layout--display-i-position)
8. [Fundus, Gradientis i Sombras](#8-fundus-gradientis-i-sombras)
9. [Borduras i Rais](#9-borduras-i-rais)
10. [Filtrus i Máskaras](#10-filtrus-i-máskaras)
11. [Variantis Interativos](#11-variantis-interativos)
12. [Dezenhu Responsivu](#12-dezenhu-responsivu)
13. [Container Queries](#13-container-queries)
14. [Columns](#14-columns)
15. [Flexbox](#15-flexbox)
16. [Grid](#16-grid)
17. [Transisan i Transformasan](#17-transisan-i-transformasan)
18. [Animasan](#18-animasan)
19. [`@theme` — Personalizasan di Tokens](#19-theme--personalizasan-di-tokens)
20. [Modu Sukuru ku `@custom-variant`](#20-modu-sukuru-ku-custom-variant)
21. [Tailwind CLI v4](#21-tailwind-cli-v4)
22. [`@theme` di Profundidade](#22-theme-di-profundidade)
23. [Direktivas i Funsan v4](#23-direktivas-i-funsan-v4)
24. [Bundlers — Vite, Webpack, PostCSS](#24-bundlers--vite-webpack-postcss)
25. [Erros Komun i Kumo Rezolvi](#25-erros-komun-i-kumo-rezolvi)

---

## 1. Setup i Anbienti

### Play CDN (pa testes rápidu) — _Lisan 3_

Pa abri un sandbox sem instala nada:

```html
<!DOCTYPE html>
<html lang="kea">
<head>
  <meta charset="UTF-8" />
  <title>Sandbox di Djonzinho</title>
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-slate-100 p-6">
  <h1 class="text-3xl font-bold text-sky-700">Bon dia, Kabu Verdi!</h1>
</body>
</html>
```

:::callout{type=tip}
CDN é só pa proto­tipu i testes — el ka é otimu pa produsan. Pa projetu real, uza Vite ou Tailwind CLI.
:::

### Tailwind CLI v4 (standalone) — _Lisan 23_

Pa projetu sem bundler (HTML statiku simples):

```bash
# Instala
npm install -D tailwindcss@4 @tailwindcss/cli

# src/style.css
# (só un linha — tudu Tailwind ta vir di un import só)
echo '@import "tailwindcss";' > src/style.css

# Buildu un vez
npx @tailwindcss/cli -i src/style.css -o dist/style.css

# Watch (rebuild automátiku)
npx @tailwindcss/cli -i src/style.css -o dist/style.css --watch

# Produsaun (minify)
npx @tailwindcss/cli -i src/style.css -o dist/style.css --minify
```

### Tailwind ku Vite (rekomendadu) — _Lisan 26_

Pa projetu modernu ku HMR (hot reload) i bundling:

```bash
# Kria projetu Vite
npm create vite@latest meu-site -- --template vanilla
cd meu-site

# Instala Tailwind i plugin Vite
npm install -D tailwindcss@4 @tailwindcss/vite
```

```js
// vite.config.js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

```css
/* src/style.css */
@import "tailwindcss";
```

```js
// src/main.js
import "./style.css";
```

```bash
npm run dev      # localhost:5173, HMR ativu
npm run build    # bundling pa dist/
npm run preview  # preview di buildu produsaun
```

:::callout{type=tip}
Vite é skolha **default** pa novu projetu. PostCSS i Webpack inda ten suporti (ver Seksan 24), ma Vite é más rápidu i konfigurasan é más simples.
:::

---

## 2. Utility-First — Fundamentus

### O ki é "utility-first"? — _Lisan 4_

Bez di skrebe CSS personalizadu pa kada elementu, bo ta kombina ku **klasi pikinin** ki ta faze **un só kuza**:

```html
<!-- Sem Tailwind -->
<button class="meu-botaun">Klika</button>

<style>
  .meu-botaun {
    background-color: #1e40af;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    font-weight: 600;
  }
</style>

<!-- Ku Tailwind -->
<button class="bg-mar-700 text-white px-4 py-2 rounded-md font-semibold">
  Klika
</button>
```

### Vantajens

- **Sem inventa nomi** — Bo ka tene di pensa na "kumo ta xama es klasi?"
- **CSS bundle pikinin** — Tailwind ta jera só klasi ki bo ta uza
- **Konsistensia** — Tudu valor (kor, spacing, fonte) ta ben di un sistema di tokens
- **Faze mudansa lokal** — Mudansa na un elementu ka ta afeta otu

### Estrutura di un klasi utility

```
{propriedadi}-{valor}
{variant}:{propriedadi}-{valor}
{breakpoint}:{propriedadi}-{valor}
```

Egzemplus:
- `bg-blue-500` → `background-color: #3b82f6`
- `hover:bg-blue-700` → muda kor na hover
- `md:text-xl` → text-xl só na ekran ≥ 768px

---

## 3. Kores i Opasidadi

### Palette default — _Lisan 5_

Tailwind ten 26 familias di kor, kada un ku 11 tonalidadis (50–950) — 22 klásiku + 4 novu di v4.2:

```
slate, gray, zinc, neutral, stone
red, orange, amber, yellow, lime
green, emerald, teal, cyan, sky
blue, indigo, violet, purple, fuchsia
pink, rose
mauve, olive, mist, taupe
```

| Klasi             | Resultadu                          |
|-------------------|------------------------------------|
| `bg-blue-500`     | Fundu azul médiu                   |
| `text-red-700`    | Tekstu vermedju sukuru              |
| `border-gray-300` | Bordura sinza klaru                |
| `ring-emerald-500`| Anel di foku verdi                 |

### Opasidadi ku modifikador `/` — _Lisan 5_

Sintaxi di opasidadi ku modifikador `/`:

```html
<div class="bg-black/50">Overlay 50% pretu</div>
<p class="text-red-700/80">Tekstu vermedju 80%</p>
```

| Modifikador | Opasidadi |
|-------------|-----------|
| `/0`        | 0%        |
| `/25`       | 25%       |
| `/50`       | 50%       |
| `/75`       | 75%       |
| `/100`      | 100% (default — ka presiza skrebe) |

Tanbe ta suporta valores arbitráriu: `bg-blue-500/[33%]`, `bg-blue-500/[.27]`.

:::callout{type=tip}
Pa overlays (modais, dropdowns), uza fundu pretu ku opasidadi: `bg-black/50`. Es ta ten kompatibilidadi midjór ki `rgba()` personalizadu.
:::

---

## 4. Spacing — Container, Padding, Margin

### Skala di spacing — _Lisan 6_

Spacing ta segui un skala konsistenti bazeadu na unidadi `0.25rem` (= 4px na default):

| Klasi | Valor   | Pikseis (default) |
|-------|---------|-------------------|
| `p-0` | 0       | 0px               |
| `p-1` | 0.25rem | 4px               |
| `p-2` | 0.5rem  | 8px               |
| `p-3` | 0.75rem | 12px              |
| `p-4` | 1rem    | 16px              |
| `p-6` | 1.5rem  | 24px              |
| `p-8` | 2rem    | 32px              |
| `p-12`| 3rem    | 48px              |
| `p-16`| 4rem    | 64px              |
| `p-24`| 6rem    | 96px              |
| `p-32`| 8rem    | 128px             |

### Padding

| Klasi   | CSS                       |
|---------|---------------------------|
| `p-4`   | `padding: 1rem`           |
| `px-4`  | `padding-inline: 1rem`    |
| `py-4`  | `padding-block: 1rem`     |
| `pt-4`  | `padding-top: 1rem`       |
| `pr-4`  | `padding-right: 1rem`     |
| `pb-4`  | `padding-bottom: 1rem`    |
| `pl-4`  | `padding-left: 1rem`      |
| `ps-4`  | `padding-inline-start`    |
| `pe-4`  | `padding-inline-end`      |

### Margin

Mesmu padran: `m-*`, `mx-*`, `my-*`, `mt-*`, etc. Pa margin negativu, prefiksu `-`:

```html
<div class="-mt-4">Margin top di -1rem</div>
```

### Container — _Lisan 6_

`container` é un klasi spesial ki ta lia max-width a breakpoint:

```html
<div class="container mx-auto px-4">
  <!-- max-width ta mudar nos breakpoints: 640px, 768px, 1024px, 1280px, 1536px -->
</div>
```

:::callout{type=tip}
Sempri kombina `container` ku `mx-auto` pa sentraliza i `px-4` pa pading lateral. Sen es, kontentidu ta kola na borda na ekran pikinin.
:::

### Gap (pa flex/grid)

```html
<div class="flex gap-4">       <!-- gap entre elementus -->
<div class="grid gap-x-4 gap-y-2">  <!-- gap diferenti pa kolumna/linha -->
```

---

## 5. Tipografia

### Tamanhu di tekstu — _Lisan 7_

| Klasi      | Tamanhu (default) | Line-height |
|------------|------------------|-------------|
| `text-xs`  | 0.75rem (12px)   | 1rem        |
| `text-sm`  | 0.875rem (14px)  | 1.25rem     |
| `text-base`| 1rem (16px)      | 1.5rem      |
| `text-lg`  | 1.125rem (18px)  | 1.75rem     |
| `text-xl`  | 1.25rem (20px)   | 1.75rem     |
| `text-2xl` | 1.5rem (24px)    | 2rem        |
| `text-3xl` | 1.875rem (30px)  | 2.25rem     |
| `text-4xl` | 2.25rem (36px)   | 2.5rem      |
| `text-5xl` | 3rem (48px)      | 1           |
| `text-6xl` | 3.75rem (60px)   | 1           |
| `text-7xl` | 4.5rem (72px)    | 1           |

### Pezu (weight)

| Klasi              | CSS                |
|--------------------|--------------------|
| `font-thin`        | `font-weight: 100` |
| `font-light`       | `300`              |
| `font-normal`      | `400`              |
| `font-medium`      | `500`              |
| `font-semibold`    | `600`              |
| `font-bold`        | `700`              |
| `font-extrabold`   | `800`              |
| `font-black`       | `900`              |

### Família di fonte

| Klasi          | CSS                                  |
|----------------|--------------------------------------|
| `font-sans`    | Família sans-serif default           |
| `font-serif`   | Família serif                        |
| `font-mono`    | Família monospace                    |
| `font-display` | Família display personalizadu (via `@theme`) |

### Alinhamentu, tracking, leading

```html
<p class="text-left">      <!-- ta alinha-left -->
<p class="text-center">    <!-- sentralizadu -->
<p class="text-right">
<p class="text-justify">

<p class="leading-tight">    <!-- line-height: 1.25 -->
<p class="leading-normal">   <!-- 1.5 -->
<p class="leading-relaxed">  <!-- 1.625 -->
<p class="leading-loose">    <!-- 2 -->

<p class="tracking-tight">   <!-- letter-spacing: -0.025em -->
<p class="tracking-wide">    <!-- 0.025em -->
<p class="tracking-widest">  <!-- 0.1em -->
```

### Dekorasan

```html
<p class="underline">
<p class="line-through">
<p class="no-underline">
<p class="uppercase lowercase capitalize">
<p class="italic not-italic">
<p class="truncate">           <!-- ... ku overflow -->
<p class="line-clamp-3">       <!-- maks 3 linha + ... -->
```

---

## 6. Tamanhu — Largura i Altura

### Klasi prinsipal — _Lisan 8_

| Klasi      | Resultadu                         |
|------------|-----------------------------------|
| `w-1/2`    | `width: 50%`                      |
| `w-full`   | `width: 100%`                     |
| `w-screen` | `width: 100vw`                    |
| `w-auto`   | `width: auto`                     |
| `w-4`      | `width: 1rem` (skala di spacing)  |
| `w-px`     | `width: 1px`                      |
| `min-w-0`  | `min-width: 0`                    |
| `max-w-md` | `max-width: 28rem`                |
| `h-*`, `min-h-*`, `max-h-*` | mesmu padran pa altura |

### `size-*` (largura + altura djuntu) — _Lisan 8_

```html
<div class="size-16">       <!-- w-16 h-16 -->
<div class="size-full">     <!-- w-full h-full -->
```

### Valores komun

| Klasi        | Persentaji |
|--------------|------------|
| `w-1/2`      | 50%        |
| `w-1/3` `w-2/3` | 33.33% / 66.66% |
| `w-1/4`...`w-3/4` | 25% / 50% / 75% |
| `w-1/5`...`w-4/5` | 20% / 40% / 60% / 80% |
| `w-full`     | 100%       |

### `max-w-*` (max-width)

| Klasi       | Valor |
|-------------|-------|
| `max-w-xs`  | 20rem (320px) |
| `max-w-sm`  | 24rem (384px) |
| `max-w-md`  | 28rem (448px) |
| `max-w-lg`  | 32rem (512px) |
| `max-w-xl`  | 36rem (576px) |
| `max-w-2xl` | 42rem (672px) |
| `max-w-prose` | ~65 karakter (otimu pa leitura) |

---

## 7. Layout — Display i Position

### Display — _Lisan 9_

| Klasi         | CSS                  |
|---------------|----------------------|
| `block`       | `display: block`     |
| `inline-block`| `display: inline-block` |
| `inline`      | `display: inline`    |
| `flex`        | `display: flex`      |
| `inline-flex` | `display: inline-flex` |
| `grid`        | `display: grid`      |
| `inline-grid` | `display: inline-grid` |
| `hidden`      | `display: none`      |
| `contents`    | `display: contents`  |

### Position

| Klasi      | CSS                   |
|------------|-----------------------|
| `static`   | `position: static`    |
| `relative` | `position: relative`  |
| `absolute` | `position: absolute`  |
| `fixed`    | `position: fixed`     |
| `sticky`   | `position: sticky`    |

### Offsets

```html
<div class="absolute top-0 right-0 bottom-0 left-0">  <!-- ku 0 na tudu -->
<div class="absolute inset-0">                         <!-- mesmu kuza -->
<div class="absolute inset-x-0 top-4">                 <!-- left + right = 0 -->
```

### Z-index

| Klasi  | CSS         |
|--------|-------------|
| `z-0`  | `z-index: 0`  |
| `z-10` | `10`          |
| `z-20` | `20`          |
| `z-50` | `50`          |
| `z-auto`| `auto`       |

### Overflow

```html
<div class="overflow-hidden">
<div class="overflow-auto">       <!-- scroll si presiza -->
<div class="overflow-scroll">     <!-- scroll sempri -->
<div class="overflow-x-auto overflow-y-hidden">
```

---

## 8. Fundus, Gradientis i Sombras

### Background — _Lisan 10_

```html
<div class="bg-blue-500">                <!-- kor -->
<div class="bg-[#ff5733]">               <!-- valor arbitráriu -->
<div class="bg-transparent">
<div class="bg-current">                 <!-- ta usa kor di tekstu -->
<div class="bg-[url('/imajen.jpg')] bg-cover bg-center">
```

| Klasi           | CSS                            |
|-----------------|--------------------------------|
| `bg-cover`      | `background-size: cover`       |
| `bg-contain`    | `background-size: contain`     |
| `bg-center`     | `background-position: center`  |
| `bg-no-repeat`  | `background-repeat: no-repeat` |
| `bg-fixed`      | `background-attachment: fixed` |

### Gradientis — _Lisan 10_

```html
<div class="bg-linear-to-r from-blue-500 to-purple-500">
<div class="bg-linear-to-br from-mar-700 via-mar-500 to-sol-500">
<div class="bg-radial from-sol-300 to-mar-700">
<div class="bg-conic from-red-500 via-yellow-500 to-blue-500">
```

| Direksan       | Pa onde |
|-----------------|---------|
| `bg-linear-to-t`  | top    |
| `bg-linear-to-tr` | top-right |
| `bg-linear-to-r`  | right  |
| `bg-linear-to-br` | bottom-right |
| `bg-linear-to-b`  | bottom |
| `bg-linear-to-bl` | bottom-left |
| `bg-linear-to-l`  | left   |
| `bg-linear-to-tl` | top-left |

### Sombras — _Lisan 10_

| Klasi               | Tamanhu        |
|---------------------|---------------|
| `shadow-xs`         | minúskulu     |
| `shadow-sm`         | pikinin       |
| `shadow-md`         | médiu         |
| `shadow-lg`         | grandi        |
| `shadow-xl`         | muitu grandi  |
| `shadow-2xl`        | enormi        |
| `shadow-none`       | sen sombra    |
| `inset-shadow-sm`   | interna       |

```html
<div class="shadow-md hover:shadow-xl">  <!-- sombra na hover -->
<div class="shadow-[0_4px_8px_rgba(0,0,0,0.25)]">  <!-- valor arbitráriu -->
```

---

## 9. Borduras i Rais

### Bordura — _Lisan 11_

**Importanti:** kor default di bordura é `currentColor`. Si bo skrebe `border` sem espesifika kor, ta uza kor di tekstu.

```html
<div class="border">          <!-- 1px, kor = tekstu -->
<div class="border-2">        <!-- 2px -->
<div class="border-4">        <!-- 4px -->
<div class="border-8">        <!-- 8px -->
<div class="border-0">        <!-- 0px -->
<div class="border-mar-500">  <!-- ku kor explisitu -->
<div class="border-t-2 border-b-2">  <!-- só top + bottom -->
```

| Klasi          | Bordura |
|----------------|---------|
| `border-t-*`   | top     |
| `border-r-*`   | right   |
| `border-b-*`   | bottom  |
| `border-l-*`   | left    |
| `border-x-*`   | left + right |
| `border-y-*`   | top + bottom |

### Estilu di bordura

```html
<div class="border-solid">    <!-- default -->
<div class="border-dashed">
<div class="border-dotted">
<div class="border-double">
<div class="border-none">
```

### Rais (border-radius) — _Lisan 11_

| Klasi           | Tamanhu              |
|-----------------|---------------------|
| `rounded-xs`    | muitu pikinin       |
| `rounded-sm`    | pikinin             |
| `rounded-md`    | médiu               |
| `rounded-lg`    | grandi              |
| `rounded-xl`    | muitu grandi        |
| `rounded-2xl`   | enormi              |
| `rounded-3xl`   | gigantiku           |
| `rounded-full`  | sirkulu/píla        |
| `rounded-none`  | sem rais            |

```html
<button class="rounded-md">             <!-- kantos arondiadu -->
<button class="rounded-tl-lg rounded-br-lg">  <!-- só dos kantos -->
<button class="rounded-full">           <!-- pílulu kompletu -->
```

### Outline i ring

```html
<button class="outline-2 outline-mar-500 outline-offset-2">
<button class="ring-2 ring-mar-500 ring-offset-2 ring-offset-white">
```

`ring` é kumo `box-shadow` ma más simples — uzadu muitu pa foku.

---

## 10. Filtrus i Máskaras

### Filtrus — _Lisan 12_

| Klasi      | Blur     |
|------------|----------|
| `blur-xs`  | 4px      |
| `blur-sm`  | 8px      |
| `blur-md`  | 12px     |
| `blur-lg`  | 16px     |
| `blur-xl`  | 24px     |
| `blur-2xl` | 40px     |
| `blur-3xl` | 64px     |
| `blur-none`| 0px      |

```html
<img class="blur-sm hover:blur-none">
<div class="backdrop-blur-md bg-white/30">  <!-- glassmorphism -->
```

### Outros filtrus

| Klasi              | Faze              |
|--------------------|-------------------|
| `brightness-50`    | 50% di klaridadi  |
| `contrast-125`     | 125% di kontrasti |
| `grayscale`        | konverti pa sinza |
| `invert`           | inverti kores     |
| `saturate-200`     | 200% di saturasan |
| `sepia`            | filtru sepia      |
| `hue-rotate-90`    | rota matiz 90°    |
| `drop-shadow-md`   | sombra na elementu (ka box) |

### Máskaras — _Lisan 12_

```html
<div class="mask-linear-to-r mask-from-black mask-to-transparent">
<div class="mask-radial mask-from-white mask-to-transparent">
```

Máskaras ta faze fade ou rekorta elementu segundu un gradient.

---

## 11. Variantis Interativos

### Pseudo-klasi básiku — _Lisan 13_

```html
<button class="bg-mar-500 hover:bg-mar-700 focus:ring-2 active:bg-mar-900">
  Klika
</button>

<input class="border focus:border-mar-500 focus:outline-none disabled:opacity-50">
```

| Variant          | Kuandu ta aplika |
|------------------|------------------|
| `hover:`         | mouse na riba   |
| `focus:`         | elementu fokadu (teklado) |
| `focus-visible:` | foku só ku teklado (ka ku klik) |
| `focus-within:`  | el ou filhu ku foku |
| `active:`        | enkuantu klikadu |
| `disabled:`      | atributu disabled |
| `checked:`       | input/radio markadu |
| `placeholder:`   | estiliza placeholder |
| `read-only:`     | input read-only  |
| `required:`      | input required   |
| `valid:` `invalid:` | validasan di forma |

### Filhus i grupu — _Lisan 13_

```html
<!-- group: pai ku klasi `group`, filhus reagi a hover di pai -->
<a href="#" class="group">
  <h3 class="group-hover:underline">Títulu</h3>
  <p class="group-hover:text-mar-700">Pasaji</p>
</a>

<!-- peer: irmaun ku klasi `peer`, irmaun a depois ta reagi -->
<input class="peer" type="checkbox">
<label class="peer-checked:font-bold">Etiketu</label>
```

### Outros variantis

```html
<div class="first:mt-0 last:mb-0">      <!-- primeru/ultimu filhu -->
<li class="odd:bg-white even:bg-gray-50"> <!-- impar/par -->
<div class="empty:hidden">              <!-- skondi si vaziu -->
<p class="not-first:mt-4">              <!-- tudu menos primeru -->
```

---

## 12. Dezenhu Responsivu

### Breakpoints default — _Lisan 14_

| Prefiksu | Min-width | Tipiku |
|----------|-----------|--------|
| `sm:`    | 640px     | tablet portrait |
| `md:`    | 768px     | tablet         |
| `lg:`    | 1024px    | laptop pikinin |
| `xl:`    | 1280px    | desktop        |
| `2xl:`   | 1536px    | desktop grandi |

Pa ekran mais grandi, persona­liza ku `@theme` (Seksan 19).

### Filosofia: mobile-first — _Lisan 14_

Klasi sem prefiksu ta aplika a **tudu ekran**. Prefiksu ta sobreskreve a partir di kel breakpoint pa riba.

```html
<!-- 1 kolumna na mobile, 2 na tablet, 3 na desktop -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">

<!-- Tekstu kresi ku tamanhu di ekran -->
<h1 class="text-2xl md:text-4xl lg:text-6xl">

<!-- Skondi na mobile, mostra na tablet pa riba -->
<aside class="hidden md:block">
```

:::callout{type=tip}
**Pensa di mobile primeru.** Skrebe versan pa ekran pikinin sem prefiksu, depois adisiona overrides pa ekran maior. Es ta torna kódigu más limpu i bundle más pikinin.
:::

### Variantis max- — _Lisan 14_

Pa orientasan "pa baxu di X": prefiksu `max-{breakpoint}:`

```html
<div class="block max-md:hidden">  <!-- skondi a baxu di md -->
```

---

## 13. Container Queries

### O ki é? — _Lisan 15_

Container queries ta deixa-bo aplika stilu bazeadu na tamanhu di **kontainer pai**, ka di viewport. Útil pa komponenti reutilizavel.

```html
<!-- Marka pai kumo kontainer -->
<div class="@container">
  <!-- Filhu ta reage pa tamanhu di pai, ka di window -->
  <h2 class="@md:text-3xl @lg:text-5xl">Títulu</h2>
  <div class="@md:grid @md:grid-cols-2">...</div>
</div>
```

### Breakpoints di container

| Prefiksu | Min-width |
|----------|-----------|
| `@xs:`   | 20rem (320px) |
| `@sm:`   | 24rem (384px) |
| `@md:`   | 28rem (448px) |
| `@lg:`   | 32rem (512px) |
| `@xl:`   | 36rem (576px) |
| `@2xl:`  | 42rem (672px) |
| `@3xl:`  | 48rem (768px) |
| `@4xl:`  | 56rem (896px) |

### Kontainer nomeadu

Pa skodje kal kontainer ta responde:

```html
<div class="@container/sidebar">
  <article class="@container/card">
    <!-- ta reage spesifikamenti a sidebar -->
    <h3 class="@md/sidebar:text-2xl">Títulu</h3>
  </article>
</div>
```

---

## 14. Columns

### Multi-column layout — _Lisan 16_

CSS Multi-column ta divide kontentidu en kolunas otomatikamenti (kumo jornal):

```html
<div class="columns-2 gap-4">
  <p>Parágrafu un...</p>
  <p>Parágrafu dos...</p>
  <p>Parágrafu trez...</p>
</div>
```

| Klasi          | Kolunas |
|----------------|----------|
| `columns-1`    | 1        |
| `columns-2`    | 2        |
| `columns-3`    | 3        |
| `columns-4`    | 4        |
| `columns-auto` | otomátiku |
| `columns-3xs`  | basadu na largura (16rem) |
| `columns-md`   | (28rem)  |

```html
<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-4">
  <img class="break-inside-avoid" ...>  <!-- ka korta imajen -->
</div>
```

---

## 15. Flexbox

### Setup básiku — _Lisan 17_

```html
<div class="flex">              <!-- organiza → linha horizontal -->
<div class="flex flex-col">     <!-- organiza → koluna vertikal -->
<div class="inline-flex">       <!-- flex inline -->
```

### Direksan i wrap

| Klasi              | CSS                           |
|--------------------|-------------------------------|
| `flex-row`         | direksan horizontal (default) |
| `flex-row-reverse` | invertidu horizontal          |
| `flex-col`         | vertikal                      |
| `flex-col-reverse` | invertidu vertikal            |
| `flex-wrap`        | kebra pa linha nova           |
| `flex-nowrap`      | ka kebra (default)            |

### Justify (eixu prinsipal)

```html
<div class="flex justify-start">    <!-- inísiu (default) -->
<div class="flex justify-center">   <!-- sentru -->
<div class="flex justify-end">      <!-- fin -->
<div class="flex justify-between">  <!-- espasu entre -->
<div class="flex justify-around">   <!-- espasu igual em volta -->
<div class="flex justify-evenly">   <!-- distribusãu uniformi -->
```

### Items (eixu kontráriu)

```html
<div class="flex items-start">     <!-- topu -->
<div class="flex items-center">    <!-- sentru -->
<div class="flex items-end">       <!-- baxu -->
<div class="flex items-stretch">   <!-- ta estika (default) -->
<div class="flex items-baseline">  <!-- linha di base di tekstu -->
```

### Grow i shrink — _Lisan 17_

```html
<div class="flex">
  <div class="grow">Ta okupa espasu disponivel</div>
  <div class="shrink-0">Ta ka enkolhe</div>
</div>
```

| Klasi      | CSS              |
|------------|------------------|
| `grow`     | `flex-grow: 1`   |
| `grow-0`   | `flex-grow: 0`   |
| `shrink`   | `flex-shrink: 1` |
| `shrink-0` | `flex-shrink: 0` |
| `flex-1`   | `flex: 1 1 0%`   |
| `flex-auto`| `flex: 1 1 auto` |
| `flex-none`| `flex: none`     |

### Order

```html
<div class="order-first">  <!-- primeru visualmenti -->
<div class="order-last">   <!-- ultimu -->
<div class="order-2">      <!-- ordem espesífiku -->
```

---

## 16. Grid

### Setup básiku — _Lisan 18_

```html
<div class="grid grid-cols-3 gap-4">
  <div>Items 1</div>
  <div>Items 2</div>
  <div>Items 3</div>
</div>
```

### Kolunas

| Klasi               | Kuadrikula      |
|---------------------|-----------------|
| `grid-cols-1`...`grid-cols-12` | N kolunas iguais |
| `grid-cols-none`    | sem grid template |
| `grid-cols-subgrid` | usa parent's grid |
| `grid-cols-[200px_1fr_auto]` | valores arbitráriu |

### Linhas

```html
<div class="grid grid-rows-3 gap-2">
<div class="grid grid-rows-[auto_1fr_auto]">  <!-- header/main/footer -->
```

### Span

```html
<div class="col-span-2">      <!-- ta okupa 2 kolumnas -->
<div class="col-span-full">   <!-- ta okupa tudu kolumnas -->
<div class="row-span-3">      <!-- ta okupa 3 linhas -->
<div class="col-start-2 col-end-5">  <!-- linhas 2 a 5 -->
```

### Auto-fill / auto-fit

Pa grid responsivu sem media queries:

```html
<div class="grid grid-cols-[repeat(auto-fit,minmax(250px,1fr))] gap-4">
  <!-- Kolumnas ta ajusta automátiku -->
</div>
```

### Alinhamentu (igual a flex)

```html
<div class="grid place-items-center">      <!-- justify-items + items -->
<div class="grid place-content-between">   <!-- pa kuadrikula inteira -->
```

---

## 17. Transisan i Transformasan

### Transisan básiku — _Lisan 19_

```html
<button class="transition duration-300 ease-in-out hover:bg-mar-700">
```

| Propriedadi | Klasi |
|-------------|-------|
| **Tudu propriedadis** | `transition` |
| **Só kor**            | `transition-colors` |
| **Só opasidadi**      | `transition-opacity` |
| **Só transform**      | `transition-transform` |
| **Só sombra**         | `transition-shadow` |
| **Nada**              | `transition-none` |

### Duration

| Klasi          | ms   |
|----------------|------|
| `duration-75`  | 75   |
| `duration-100` | 100  |
| `duration-200` | 200  |
| `duration-300` | 300  |
| `duration-500` | 500  |
| `duration-700` | 700  |
| `duration-1000`| 1000 |

### Easing

| Klasi          | Curva                |
|----------------|----------------------|
| `ease-linear`  | linear               |
| `ease-in`      | start devagar        |
| `ease-out`     | end devagar          |
| `ease-in-out`  | dos ladus devagar    |

### Transformasan 2D

```html
<div class="scale-110">           <!-- 110% -->
<div class="scale-x-50 scale-y-100">
<div class="rotate-45">           <!-- 45° -->
<div class="-rotate-12">          <!-- -12° -->
<div class="translate-x-4">       <!-- desloka 1rem pa right -->
<div class="-translate-y-2">      <!-- pa riba -->
<div class="skew-x-12">           <!-- desviu -->
```

### Transformasan 3D — _Lisan 19_

```html
<div class="perspective-1000 perspective-origin-center">
  <div class="rotate-x-45 rotate-y-30 transform-gpu">
    <!-- rotasan en 3 dimensan -->
  </div>
</div>

<div class="backface-hidden">  <!-- pa kartas ki ta vira -->
```

| Klasi                     | Faze                         |
|---------------------------|------------------------------|
| `perspective-{val}`       | profundidadi 3D              |
| `perspective-origin-{pos}`| pontu di fuga                |
| `rotate-x-{deg}`          | rotasan na eixu X           |
| `rotate-y-{deg}`          | rotasan na eixu Y           |
| `rotate-z-{deg}`          | rotasan na eixu Z (= rotate)|
| `translate-z-{val}`       | move na eixu Z               |
| `transform-style-3d`      | filhus na espasu 3D          |
| `backface-hidden`         | skondi parti di trás         |

### Origem di transformasan

```html
<div class="origin-center">   <!-- default -->
<div class="origin-top-left">
<div class="origin-bottom">
```

---

## 18. Animasan

### Animasan pre-definidu — _Lisan 20_

| Klasi          | Faze                       |
|----------------|----------------------------|
| `animate-spin` | rotasan kontínua (loaders)|
| `animate-ping` | pulsa ku skala + opasidadi |
| `animate-pulse`| fade pa frenti i pa trás   |
| `animate-bounce`| salta vertikalmenti       |
| `animate-none` | sem animasan              |

```html
<svg class="animate-spin h-5 w-5">...</svg>
<span class="relative flex h-3 w-3">
  <span class="animate-ping absolute inset-0 rounded-full bg-mar-400 opacity-75"></span>
  <span class="relative rounded-full h-3 w-3 bg-mar-500"></span>
</span>
```

### Animasan personalizadu ku `@theme` + `@keyframes` — _Lisan 20_

**Sintaxi v4** — define na CSS, ka más na JS config:

```css
@theme {
  --animate-fade-up: fade-up 0.6s ease-out forwards;
  --animate-wiggle: wiggle 1s ease-in-out infinite;
}

@keyframes fade-up {
  0% {
    opacity: 0;
    transform: translateY(1rem);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes wiggle {
  0%, 100% { transform: rotate(-3deg); }
  50% { transform: rotate(3deg); }
}
```

Uza na HTML:

```html
<h1 class="animate-fade-up">Apaeci ku fade pa riba</h1>
<button class="hover:animate-wiggle">Klika i mi ta mexi</button>
```

---

## 19. `@theme` — Personalizasan di Tokens

### Kumo funsiona — _Lisan 21_

`@theme` é onde bo define **tokens di dezenhu** (kores, fontis, breakpoints, spacing, animasan). Kada propriedadi ki bo adisiona ta jera klasi utility automátiku.

```css
@import "tailwindcss";

@theme {
  /* Kor: --color-{nomi}-{nivel} → bg-{nomi}-{nivel}, text-..., etc. */
  --color-mar-50: oklch(0.97 0.02 240);
  --color-mar-500: oklch(0.55 0.18 240);
  --color-mar-900: oklch(0.22 0.10 240);

  /* Fonte: --font-{nomi} → font-{nomi} */
  --font-display: "Crimson Pro", serif;

  /* Spacing: substitui skala kompleta (ô só un valor) */
  --spacing: 0.25rem;  /* default 4px → ku 0.3rem ta krexi pa 4.8px */

  /* Breakpoints: --breakpoint-{nomi} → {nomi}:utility */
  --breakpoint-3xl: 1920px;

  /* Animasan (ver Seksaun 18) */
  --animate-fade-up: fade-up 0.6s ease-out forwards;
}
```

### Kor: skala kompleta

```css
@theme {
  --color-brand-50: oklch(0.97 0.02 240);
  --color-brand-100: oklch(0.93 0.04 240);
  --color-brand-300: oklch(0.75 0.12 240);
  --color-brand-500: oklch(0.55 0.18 240);  /* default */
  --color-brand-700: oklch(0.38 0.16 240);
  --color-brand-900: oklch(0.22 0.10 240);
}
```

Depois ta uza: `bg-brand-500`, `text-brand-700`, `border-brand-300`, etc.

### Kor: só un valor

```css
@theme {
  --color-akento: #f97316;
}
```

Klasi disponivel: `bg-akento`, `text-akento`, `border-akento` (sem nivel).

### Por ki `oklch()`?

`oklch()` é spasu di kor perseptualmenti uniformi — kontrasti ta fika visualmenti más konsistenti ki `hex` ou `rgb`. Tailwind v4 ta uza oklch internamenti.

### Apaga default

Pa apaga un familia di kor default:

```css
@theme {
  --color-amber-*: initial;
}
```

---

## 20. Modu Sukuru ku `@custom-variant`

### Setup di Modu Sukuru — _Lisan 22_

```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```

Es ta defini varianti `dark:` ki ta aplika kuandu klasi `.dark` ta na elementu (ou na un ansestral).

### Uzu

```html
<body class="bg-white text-black dark:bg-gray-900 dark:text-white">
  <nav class="bg-mar-50 dark:bg-mar-900">
    <p class="text-gray-700 dark:text-gray-300">...</p>
  </nav>
</body>
```

### Toggle ku JavaScript vanilla

```html
<button id="toggle-tema">🌗</button>

<script>
  const btn = document.getElementById("toggle-tema");
  const html = document.documentElement;

  // Karega skolha salvadu (ô uza sistema)
  if (localStorage.tema === "dark" ||
      (!("tema" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
    html.classList.add("dark");
  }

  btn.addEventListener("click", () => {
    html.classList.toggle("dark");
    localStorage.tema = html.classList.contains("dark") ? "dark" : "light";
  });
</script>
```

:::callout{type=tip}
Sempri respeita skolha di sistema kumo default — uza `prefers-color-scheme`. Só sobreskreve si vizitanti dja klika na toggle (kuandu `localStorage.tema` egziste).
:::

### Variant alternativu: media query

Pa modu sukuru otomátiku sem botão (segui sistema operativu sempri):

```css
@custom-variant dark (@media (prefers-color-scheme: dark));
```

---

## 21. Tailwind CLI v4

### Komandus prinsipal — _Lisan 23_

```bash
# Buildu un vez
npx @tailwindcss/cli -i src/style.css -o dist/style.css

# Watch (rebuild automátiku kada save)
npx @tailwindcss/cli -i src/style.css -o dist/style.css --watch

# Minify (pa produsaun)
npx @tailwindcss/cli -i src/style.css -o dist/style.css --minify
```

### Flags

| Flag         | Faze                              |
|--------------|-----------------------------------|
| `-i, --input`| fixeru di entrada (geralmenti `style.css`) |
| `-o, --output` | fixeru di saida                |
| `-w, --watch`| rebuilds automátiku na mudansa    |
| `-m, --minify` | komprimi CSS pa produsan       |
| `--cwd`      | diretóriu di trabalhu             |
| `--help`     | mostra ajuda                      |

### `package.json` típiku

```json
{
  "scripts": {
    "dev": "npx @tailwindcss/cli -i src/style.css -o dist/style.css --watch",
    "build": "npx @tailwindcss/cli -i src/style.css -o dist/style.css --minify"
  }
}
```

### Entrada CSS minima

```css
@import "tailwindcss";

/* Bo CSS personalizadu ou tema ta ben li */
@theme {
  /* ... */
}
```

:::callout{type=tip}
Pa projetu HTML statiku simples (Jekyll, Hugo, GitHub Pages), CLI standalone é a midjór skolha. Pa Vite ou framework moderno, ver Seksan 24.
:::

---

## 22. `@theme` di Profundidade

### Sintaxi vs sintaxi inline — _Lisan 24_

```css
/* Bloku @theme (rekomendadu pa konjuntu di tokens) */
@theme {
  --color-mar-500: oklch(0.55 0.18 240);
  --color-mar-700: oklch(0.38 0.16 240);
}

/* Inline (pa un só token) */
@theme inline {
  --color-mar-500: oklch(0.55 0.18 240);
}
```

`@theme inline` ka ta espandi kor pa skala kompleta — útil pa egzemplus pikinin ou pa ka jera tudu klasi extra.

### Personaliza skala di spacing

```css
@theme {
  --spacing: 0.3rem;  /* default = 0.25rem */
  /* Gora p-4 = 1.2rem (vez di 1rem) */
}
```

### Variáveis ku `var()`

Bo pode referensia CSS variables na `@theme`:

```css
:root {
  --kor-bazi: oklch(0.55 0.18 240);
}

@theme {
  --color-mar-500: var(--kor-bazi);
  --color-mar-700: oklch(from var(--kor-bazi) calc(l - 0.15) c h);
}
```

### Tipus di tokens ki Tailwind ta rekonhese

| Prefiksu      | Klasi jeradu          | Egzemplu |
|---------------|-----------------------|----------|
| `--color-*`   | `bg-*`, `text-*`, `border-*`, `ring-*`, `outline-*`, `divide-*` | `--color-mar-500` |
| `--font-*`    | `font-*`              | `--font-display` |
| `--text-*`    | `text-*` (tamanhu)     | `--text-tiny` |
| `--spacing*`  | `p-*`, `m-*`, `gap-*`, `w-*`, `h-*` | `--spacing` |
| `--breakpoint-*`| `sm:`, `md:`, etc.  | `--breakpoint-3xl` |
| `--radius-*`  | `rounded-*`           | `--radius-pill` |
| `--shadow-*`  | `shadow-*`            | `--shadow-card` |
| `--animate-*` | `animate-*`           | `--animate-fade-up` |

---

## 23. Direktivas i Funsan v4

### Lista kompleta di direktivas — _Lisan 25_

| Direktiva             | Pa ki                                    | Egzemplu di uzu |
|-----------------------|------------------------------------------|-----------------|
| `@import "tailwindcss"` | importa tudu Tailwind                  | sempri primeru linha |
| `@theme { ... }`      | defini tokens i jera klasi              | Seksan 19       |
| `@custom-variant`     | kria varianti novu                      | dark mode (Seksan 20) |
| `@source "../path"`   | adisiona path extra pa skaneamentu      | monorepo, packages externu |
| `@source not "..."`   | esklui path di skaneamentu             | sub-projetu sen Tailwind |
| `@source inline("...")` | safelist klasi spesífiku              | klasi jeradu dinamikamenti |
| `@apply`              | kombina klasi ku utilidadis              | Seksan a baxu  |
| `@reference "..."`    | importa tokens sen duplika CSS          | komponenti scoped |
| `@utility nomi { ... }` | kria utilidade personalizadu            | klasi novu reutilizavel |
| `@plugin "nomi"`      | karega plugin                           | raru, só pa plugins |
| `@variant nomi`       | aplika varianti dentru di CSS           | Seksan a baxu  |

### `@apply` — funsiona ma ka rekomendadu

```css
.btn-primáriu {
  @apply bg-mar-700 text-white font-semibold rounded-md px-4 py-2;
  @apply hover:bg-mar-800 focus:ring-2 focus:ring-mar-500;
}
```

:::callout{type=tip}
Uza `@apply` só pa kazu unde bo realmenti **ka pode** uza un komponenti — ex. kombina klasi pa biblioteka di markdown ki ta jera HTML diretu. Pa resta: skrebe utilidadis na HTML i komponentes na React/Vue.
:::

### `@reference` — pa komponenti scoped — _Lisan 25_

Si bo skrebe Vue, Svelte, ou CSS Modules, `@apply` ta da eru pamodi style block é izoladu. Solusan:

```vue
<style scoped>
  @reference "../assets/input.css";

  .botaun-marka {
    @apply bg-mar-700 text-white px-4 py-2 rounded-md;
  }
</style>
```

`@reference` ta importa tokens (pa `@apply` funsiona) sem duplika CSS na output.

### `@source` — kontrola skaneamentu — _Lisan 25_

```css
@import "tailwindcss";

/* Adisiona path extra (default: tudu ficheirus na projetu) */
@source "../packages/ui";
@source "../node_modules/@meu-org/dezenhu";

/* Eskluir path */
@source not "../docs";

/* Safelist klasi spesífiku */
@source inline("text-red-500", "text-green-500");
```

### `@utility` — kria klasi personalizadu — _Lisan 25_

```css
@utility scrollbar-thin {
  scrollbar-width: thin;
}

@utility scrollbar-{kor} {
  scrollbar-color: var(--color-{kor}) transparent;
}
```

Depois: `<div class="scrollbar-thin scrollbar-mar-500">`

### Funsan CSS — _Lisan 25_

```css
.elementu {
  /* Lia un token di tema */
  background: --theme(--color-mar-500);

  /* Aplika opasidadi na kor */
  border-color: --alpha(--theme(--color-mar-500), 50%);

  /* Espresãu di spacing */
  padding: --spacing(4);  /* = 1rem ku default */
}
```

| Funsan | Faze |
|---------|------|
| `--theme(--color-xxx)` | resgata un valor di `@theme` |
| `--alpha(kor, %)`      | adisiona opasidadi |
| `--spacing(n)`         | espresan di spacing |

---

## 24. Bundlers — Vite, Webpack, PostCSS

### Vite (rekomendadu) — _Lisan 26_

Ver Seksan 1 pa setup kompletu. Vantajens:
- Plugin oficial: `@tailwindcss/vite`
- HMR muitu rápidu
- Sem konfigurasan extra di PostCSS

### Webpack + PostCSS — _Lisan 26_

Pa projetu legacy ku Webpack:

```bash
npm install -D tailwindcss@4 @tailwindcss/postcss postcss postcss-loader
```

```js
// postcss.config.js
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

```js
// webpack.config.js (excerpt)
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader", "postcss-loader"],
      },
    ],
  },
};
```

```css
/* src/style.css */
@import "tailwindcss";
```

:::callout{type=tip}
**Importanti:** Tailwind v4 ta inkluí auto-prefixing i CSS imports internamenti — bo ka tene di instala pakotis adisional nem konfigura nada extra na `postcss.config.js`.
:::

---

## 25. Erros Komun i Kumo Rezolvi

### 25.1 — Klasi `dark:` ka funsiona

**Sintoma:** Modu sukuru ka muda nada kuandu bo adisiona `.dark` na `<html>`.

**Kauza:** Falta `@custom-variant dark (...)` na CSS.

**Solusan:**

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

### 25.2 — Bordura aparesi ku kor eradu

**Sintoma:** `<div class="border">` mostra bordura vermedju ou pretu sem razan.

**Kauza:** Kor default di bordura é `currentColor`. Si tekstu é vermedju, bordura tanbe ta vermedju.

**Solusan:** Espesifika kor explisitamenti:

```html
<div class="border border-gray-200">
```

### 25.3 — `@apply` ta da eru "unknown utility"

**Sintoma:** Na Vue, Svelte ou CSS Modules, `@apply` ta lansa eru.

**Kauza:** Style block é izoladu — Tailwind ka ten asesu pa tokens.

**Solusan:** Adisiona `@reference` na topu:

```vue
<style scoped>
  @reference "../assets/input.css";

  .meu-botaun {
    @apply bg-mar-500 text-white;
  }
</style>
```

### 25.4 — Klasi personalizadu di `@theme` ka jera utility

**Sintoma:** Bo defini `--color-marka-500: ...` ma `bg-marka-500` ka funsiona.

**Kauza:** Sintaxi inkorretu — token ten ki segui konvensan (`--color-{nomi}-{nivel}` ou só `--color-{nomi}`).

**Solusan:** Verifika:
- Prefiksu sertu (`--color-*`, `--font-*`, `--spacing*`, etc. — ver Seksan 22)
- Nomi sem espasu nem karakter spesial
- `@theme {}` esta dentru di fixeru ku `@import "tailwindcss"`

### 25.5 — Klasi jeradu dinamikamenti na JavaScript ka aplika

**Sintoma:** Bo faze `el.className = `text-${kor}-500`` na JS, ma stilu ka aparesi.

**Kauza:** Tailwind ta skaneia kódigu statiku — el ka ta atxa klasi konkateneadu na tempu di execusan.

**Solusan (rekomendadu):** Uza un objetu di mapeamentu ku klasi kompletu:

```js
const kores = {
  sukseso: "text-green-500",
  eru:     "text-red-500",
  avizu:   "text-yellow-500",
};
el.className = kores[estadu];
```

**Solusan (alternativu):** Safelist ku `@source inline()`:

```css
@import "tailwindcss";

@source inline("text-red-500", "text-green-500", "text-yellow-500");
```

### 25.6 — Container query (`@md:`) ka funsiona

**Sintoma:** Bo skrebe `<div class="@md:grid-cols-2">` ma layout ka ta mudar.

**Kauza:** Falta `@container` na elementu pai.

**Solusan:** Marka pai kumo kontainer:

```html
<div class="@container">
  <div class="grid @md:grid-cols-2">...</div>
</div>
```

---

## Rekursus

- **Dokumentasan ofisial:** [tailwindcss.com](https://tailwindcss.com)
- **Repositoriu di playgrounds:** [play.tailwindcss.com](https://play.tailwindcss.com)
- **Kursu Skola.dev:** Fundamentus di Tailwind CSS v4 (26 lisans, M1–M4)

---

**Fin di cheatsheet.** Pa eru ou feedback, abri un issue na repositoriu di kursu.
