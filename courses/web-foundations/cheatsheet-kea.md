---
title: Fundamentus di Web — HTML i CSS
slug: web-foundations
courseSlug: web-foundations
language: kea
version: 1.0.0
validated_at: 2026-05-14
trace_id: Skola-course-web-foundations-20260514-170000
---

# Web Foundations Cheatsheet — HTML i CSS

**Lingua:** kea (Kabuverdianu, ALUPEC) | **Padron:** HTML5 + CSS3 (Flexbox, Grid) | **Versan di dok:** 1.0.0 | **Validadu na:** 2026-05-14

> **Pa ken?** Studanti prinsipianti — kabuverdianu (i otus) ki sta ta komesa kostrui websites statikus ku HTML i CSS.
> **Kumo uza:** Referensia rápidu pa konsulta durante kursu i dipos. Tudu kódiku li ta funsiona — kopia, kola, eksperimenta.

---

## Índisi

1. [Setup di ambienti](#1-setup-di-ambienti)
2. [HTML — strutura di un pajina](#2-html--strutura-di-un-pajina)
3. [Tags di testu](#3-tags-di-testu)
4. [Imajen, atributu i link](#4-imajen-atributu-i-link)
5. [HTML semantiku](#5-html-semantiku)
6. [CSS — sintaksi i liga ku HTML](#6-css--sintaksi-i-liga-ku-html)
7. [Testu i kor na CSS](#7-testu-i-kor-na-css)
8. [Selectors i LVHA](#8-selectors-i-lvha)
9. [Konflitu, specificity i "inheritance"](#9-konflitu-specificity-i-inheritance)
10. [Box model](#10-box-model)
11. [DevTools, Google i debug](#11-devtools-google-i-debug)
12. [Flexbox — un dimensan](#12-flexbox--un-dimensan)
13. [CSS Grid — dos dimensan](#13-css-grid--dos-dimensan)
14. [Pozisiona i alinha na Grid](#14-pozisiona-i-alinha-na-grid)
15. [Capstone — Visita Kabu Verdi](#15-capstone--visita-kabu-verdi)
16. [Errus komun i kumo rezolve](#16-errus-komun-i-kumo-rezolve)
17. [Próximu pasus](#17-próximu-pasus)

---

## 1. Setup di ambienti

### Ferramenta nesesáriu

| Ferramenta | Pa ken serve | Onde baxa |
|---|---|---|
| **VS Code** | Editor di kódiku | code.visualstudio.com |
| **Live Server** (extension) | Auto-refresh na browser | VS Code → Extensions → "Live Server" |
| **Chrome ou Firefox** | Browser + DevTools | google.com/chrome ou mozilla.org |

### Primeru pajina — pasu pa pasu

```bash
# 1. Kria folder di projetu
mkdir minha-pajina && cd minha-pajina

# 2. Kria index.html (na VS Code)
# 3. Klika direitu → "Open with Live Server"
# 4. Browser ta abri http://127.0.0.1:5500
```

### Boilerplate mínimu

```html
<!DOCTYPE html>
<html lang="kea">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Títulu di pajina</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Konteúdu ta entra li</h1>
  </body>
</html>
```

:::callout{type=tip}
**Memoriza es boilerplate.** Bu ta skrebe-l na kada projetu novu. Atalhu na VS Code: skrebe `!` na un ficheru `.html` vaziu i karga `Tab`.
:::

---

## 2. HTML — strutura di un pajina

### Anatomia di un tag

```html
<tag attribute="valor">konteúdu</tag>
<!--   ▲          ▲          ▲       -->
<!--   nomi     atributu   konteúdu  -->
```

### Trez part di un dokumentu HTML

| Part | Pa kuze |
|---|---|
| `<!DOCTYPE html>` | Konta browser ki é HTML5 |
| `<head>` | Metadata — títulu, kor, link pa CSS — ka ta apareci na pajina |
| `<body>` | Konteúdu vizível — testu, imajen, boton, tudu |

### Hierarquia di títulus

```html
<h1>Títulu prinsipál — un pa pajina</h1>
<h2>Subtítulu di seksan</h2>
<h3>Sub-subtítulu</h3>
<h4>...</h4>
<h5>...</h5>
<h6>Mas pinikinhu</h6>
```

**Regra:** **un `<h1>` por pajina**. Mas baxu (h2-h6) pode repeti.

### Void elements (sen closing tag)

```html
<br />        <!-- linha nova (line break) -->
<hr />        <!-- linha horizontal di separasan -->
<img src="..." alt="..." />
<meta charset="UTF-8" />
<link rel="stylesheet" href="style.css" />
<input type="text" />
```

**Konvensan di kursu:** uza forma self-closing `<br />` ku barra. HTML5 ta aseita `<br>` tanbé, ma `<br />` ta funsiona ku Prettier i otru formatadores.

---

## 3. Tags di testu

### Parágrafu i ênfase

```html
<p>Un parágrafu di testu.</p>

<strong>Importanti</strong>          <!-- bold + semantiku -->
<em>Ênfase</em>                      <!-- itáliku + semantiku -->
<b>So bold</b>                       <!-- só vizual, evita -->
<i>So itáliku</i>                    <!-- só vizual, evita -->
```

**Sempri prefere `<strong>` i `<em>`** — el ta da signifikadu, ka so aparesia.

### Lista

```html
<!-- Lista ku marka (•) -->
<ul>
  <li>Mindelo</li>
  <li>Praia</li>
  <li>São Filipe</li>
</ul>

<!-- Lista numeradu (1, 2, 3) -->
<ol>
  <li>Primeru pasu</li>
  <li>Segundu pasu</li>
  <li>Trezeru pasu</li>
</ol>
```

### Sitasan

```html
<blockquote>
  "Kabu Verdi é dês ilhas, un pôvu."
  <cite>— Provérbiu kabuverdianu</cite>
</blockquote>
```

### Kometáriu

```html
<!-- Es ka ta parse na browser. Pa nota ô disliga kódiku temporalmenti. -->
```

### Entidadis HTML

| Símbolu | Entidadi | Uzu |
|---|---|---|
| `<` | `&lt;` | Pa skrebe sinal "mas baxu" sen kuebra HTML |
| `>` | `&gt;` | Pa skrebe sinal "mas grandi" |
| `&` | `&amp;` | Pa skrebe i (ampersand) |
| `©` | `&copy;` | Símbolu di copyright |
| `"` | `&quot;` | Aspas duplu |
| (espasu naun-kuebrável) | `&nbsp;` | Espasu ki ka ta kuebra linha |

---

## 4. Imajen, atributu i link

### Imajen

```html
<img
  src="img/cesaria.jpg"
  alt="Foto di Cesária Évora na palku"
  width="400"
  height="300"
/>
```

**Atributus krítiku:**

| Atributu | Pa kuze | Obrigatóriu? |
|---|---|---|
| `src` | Kaminhu ou URL di imajen | ✓ |
| `alt` | Deskrisan pa akesibilidadi i SEO | ✓ |
| `width` / `height` | Tamanhu — preveni layout shift | rekumendadu |

**Akesibilidadi:** kada `<img />` ten ki ten `alt`. Si imajen é puramenti dekorativu, uza `alt=""` (vaziu eksplisitu).

### Link (âncoras)

```html
<!-- Pa pajina di otru website -->
<a href="https://en.wikipedia.org/wiki/Ces%C3%A1ria_%C3%89vora">Cesária Évora na Wikipedia</a>

<!-- Pa otru pajina di mêsmu projetu -->
<a href="sobre.html">Sobre nos</a>

<!-- Pa un seksan di mêsmu pajina (id) -->
<a href="#ilhas">Salta pa Ilhas</a>

<!-- Pa abri nun aba nova -->
<a href="https://example.cv" target="_blank" rel="noopener">External</a>
```

**Wikipedia URLs:** uza forma persentu-kodifikadu (`Ces%C3%A1ria_%C3%89vora`), ka `Cesária_Évora` diretamente — kel-ultimu pode kuebra na browser bedju.

---

## 5. HTML semantiku

### Elementus di strutura

```html
<header>     <!-- Topu di pajina ô di seksan -->
  <h1>Visita Kabu Verdi</h1>
  <nav>
    <a href="#ilhas">Ilhas</a>
    <a href="#komida">Komida</a>
  </nav>
</header>

<main>       <!-- Konteúdu prinsipál — un por pajina -->
  <article>  <!-- Kontéudu independenti (bloku, artigu, karta) -->
    <h2>Cesária Évora — Reina di Morna</h2>
    <p>...</p>
  </article>

  <aside>    <!-- Konteúdu sekundáriu (sidebar) -->
    <h3>Liga relacionadu</h3>
  </aside>
</main>

<section>    <!-- Agrupamentu temátiku -->
  <h2>Testimonhu</h2>
</section>

<footer>     <!-- Fundu di pajina ô di seksan -->
  <p>&copy; 2026 Visita Kabu Verdi</p>
</footer>
```

### `<section>` vs `<article>` — kuandu uza ken

| Si... | Uza |
|---|---|
| Konteúdu pode sai di pajina i kontinua ten sentidu (post di blog, karta) | `<article>` |
| Konteúdu é un agrupamentu temátiku (seksan di "Ilhas", "Komida") | `<section>` |
| Konteúdu é puramenti pa layout sen signifikadu | `<div>` |

**Regra prátiku:** si bu ta kontextualiza `<article>` ku un títulu próprio, ta funsiona ben.

---

## 6. CSS — sintaksi i liga ku HTML

### Anatomia di un regra

```css
selector {
  property: value;
  property: value;
}
/* ▲          ▲       ▲ */
/* selector  prop    valor */
```

### Trez maneira di liga CSS ku HTML

| Maneira | Sintaksi | Kuandu uza |
|---|---|---|
| **External** (rekumendadu) | `<link rel="stylesheet" href="style.css" />` na `<head>` | Sempri |
| **Internal** | `<style>` na `<head>` | So pa demo rápidu |
| **Inline** | `style="color: red"` direitamenti na tag | Evita — ka skalável |

**Sempri uza external pa projetu real.** Internal i inline = só pa testu temporáriu.

### Onde poi `<link>`

```html
<head>
  <meta charset="UTF-8" />
  <title>Pajina</title>
  <link rel="stylesheet" href="style.css" />   <!-- antes di </head> -->
</head>
```

### Kometáriu CSS

```css
/* Es é un kometáriu. Tudu ki sta dentru ka ta apilika. */
/* Pode okupa
   várias linhas tanbé. */
```

---

## 7. Testu i kor na CSS

### Propriedadi di testu

```css
body {
  font-family: 'Helvetica', Arial, sans-serif;    /* font stack */
  font-size: 16px;                                /* tamanhu */
  font-weight: 400;                               /* peso: 100-900 */
  line-height: 1.5;                               /* altura di linha */
  text-align: center;                             /* left | center | right | justify */
  color: #333;                                    /* kor di testu */
}
```

### Font stack — boa prátika

```css
/* Padron seguru: fonts modernu → fallback → jenériku */
font-family: 'Segoe UI', Roboto, Arial, sans-serif;
```

Si primeru font ka karega, browser ta tenta segundu, terseru, etc.

### Tres maneira di skrebe kor

| Forma | Egzemplu | Kuandu uza |
|---|---|---|
| **Nomi pré-definidu** | `red`, `blue`, `tomato` | So pa demo rápidu |
| **Hex** | `#1098ad`, `#fff` | Padron pa projetu real |
| **RGB / RGBA** | `rgb(16, 152, 173)`, `rgba(16, 152, 173, 0.5)` | Kuandu presisa transparensia |

```css
.box1 { background-color: red; }                /* nomi */
.box2 { background-color: #1098ad; }            /* hex teal */
.box3 { background-color: rgba(0, 0, 0, 0.5); } /* pretu 50% transparenti */
```

### Paleta tipa

```css
:root {
  --primary:   #1098ad;   /* teal */
  --bg:        #f7f0e6;   /* areia */
  --text:      #333;      /* grey sukuru */
  --accent:    #e67e22;   /* laranja morna */
}
```

---

## 8. Selectors i LVHA

### Trez selectors báziku

```css
/* Por tag */
h1 { color: #1098ad; }

/* Por klassi (.) */
.card { padding: 16px; }

/* Por id (#) — só un por pajina */
#main-header { background: #fff; }
```

### Selectors konpinatu

```css
/* Deskendentes (espasu): tudu p dentru di article */
article p { line-height: 1.6; }

/* Fidju diretu (>): so p ki é fidju diretu */
article > p { color: #555; }

/* Múltiplu (vírgula): apilika a tudu */
h1, h2, h3 { font-family: serif; }

/* Atributu */
input[type="email"] { border: 2px solid teal; }

/* Klassi múltiplu (sen espasu) */
.card.featured { border: 2px solid gold; }
```

### Pseudo-classes — LVHA pa links

```css
a:link    { color: blue; }       /* link ki ka foi vizitadu */
a:visited { color: purple; }     /* link ki dja foi vizitadu */
a:hover   { color: red; }        /* kursor por riba */
a:active  { color: orange; }     /* kuandu sta klicadu */
```

:::callout{type=tip}
**Ordi LVHA ten ki sigi.** **L**ink → **V**isited → **H**over → **A**ctive. Mnemónika: **L**a **V**ida es **H**ermosa **A**migu.

Si bu skrebe `:hover` antes di `:visited`, links vizitadu ta sobrepasa hover i `:hover` ka ta funsiona.
:::

### Otru pseudo-classes útil

```css
button:focus { outline: 2px solid teal; }      /* keyboard focus */
li:first-child { font-weight: bold; }          /* primeru item */
li:last-child { border-bottom: none; }         /* últimu item */
li:nth-child(2n) { background: #f7f0e6; }      /* par (zebra) */
```

---

## 9. Konflitu, specificity i "inheritance"

### Kuandu múltiplu regras apilika

Dos koisas ta dizidi ken ganha:

1. **Specificity** — kuan "spesifiku" é selector
2. **Order** — última regra ganha si specificity é igual

### Skala di specificity (di mas fraku pa mas forti)

| Tipu | Pontu |
|---|---|
| Universal (`*`) | 0 |
| Tag (`p`, `h1`) | 1 |
| Klassi (`.btn`), atributu (`[type=email]`), pseudo-classe (`:hover`) | 10 |
| Id (`#header`) | 100 |
| Inline (`style="..."`) | 1000 |
| `!important` | sempri ganha (evita) |

**Regra di adisan:** `article p.featured:hover` = 1 + 1 + 10 + 10 = **22 pontu**.

### Egzemplu di konflitu

```css
p           { color: blue; }       /* 1 pontu */
.intro      { color: red; }        /* 10 pontu */
#main p     { color: green; }      /* 101 pontu — ganha */
```

```html
<div id="main">
  <p class="intro">Es ta keda VERDI.</p>
</div>
```

### "Inheritance"

Algun propriedadi ta erda automatikamenti di pái pa fidju:

| Propriedadi | Erda? |
|---|---|
| `color` | ✓ |
| `font-family`, `font-size`, `font-weight` | ✓ |
| `line-height` | ✓ |
| `text-align` | ✓ |
| `background-color` | ✗ |
| `padding`, `margin`, `border` | ✗ |
| `width`, `height` | ✗ |

**Definí na `body` un vés**, tudu fidju ta inherita.

```css
body {
  font-family: sans-serif;
  color: #333;
  line-height: 1.5;
}
/* Tudu <p>, <h1>, <li> dentru di body ta usa es valores sen ten ki repeti */
```

:::callout{type=tip}
**"Inheritance" é palavra ingles ki nu ta uza diretamenti**, sen tradusan, pamodi é asin ki MDN, Stack Overflow i livru ta uza. Kuandu bu Google probléma di CSS, palavra é **"inheritance"**.
:::

---

## 10. Box model

### Anatomia di un box

```
┌─────────────────────────────────┐
│         margin (sen kor)        │   ← espasu fora di box
│  ┌───────────────────────────┐  │
│  │     border (línha)        │  │
│  │  ┌─────────────────────┐  │  │
│  │  │   padding (dentru)  │  │  │   ← espasu entre border i konteúdu
│  │  │  ┌───────────────┐  │  │  │
│  │  │  │   konteúdu    │  │  │  │
│  │  │  └───────────────┘  │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

### Propriedadi

```css
.box {
  margin: 24px;                  /* fora */
  border: 2px solid #1098ad;
  padding: 16px;                 /* dentru */
  width: 300px;
  height: 200px;
}

/* Shorthand di trez/kuatru valores */
margin: 10px 20px;               /* topu/baxu  skerda/direita */
margin: 10px 20px 30px;          /* topu  s/d  baxu */
margin: 10px 20px 30px 40px;     /* topu direita baxu skerda (clockwise) */
```

### Reset universal — `box-sizing: border-box`

```css
/* Topu di kada folha di stilu */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
```

**Pamodi reset:**

| Sen reset (`content-box`) | Ku reset (`border-box`) |
|---|---|
| `width: 300px` + `padding: 40px` = **380px na pajina** | `width: 300px` + `padding: 40px` = **300px na pajina** |
| Padding ta adisiona a width | Padding ta subtrai di konteúdu |

:::callout{type=tip}
**Aplika `* { box-sizing: border-box }` na topu di kada projetu.** Sen el, kada `padding` ta silensiozamenti kuebra layout di Grid.
:::

### `display` — kumo elementu ta okupa espasu

| Valor | Lojika |
|---|---|
| `block` | Okupa largura kompletu, kuebra linha (`<div>`, `<p>`, `<h1>`) |
| `inline` | So okupa largura di konteúdu, sen kuebra linha (`<span>`, `<a>`) |
| `inline-block` | Inline ma aseita `width`/`height` |
| `none` | Sumi kompletu di pajina |
| `flex` / `grid` | Aktiva sistema di layout (Lisan 14+) |

---

## 11. DevTools, Google i debug

### Atalhus di Chrome DevTools

| Atalhu | Aksan |
|---|---|
| `F12` ou `Cmd+Option+I` (Mac) | Abri DevTools |
| `Cmd+Shift+C` | Aktiva inspeksion ku kursor |
| `Cmd+Shift+M` | Toggle device emulation (mobile) |
| Klika direitu → "Inspect" | Inspekciona elementu spesífiku |

### Painel Elements

| Aba | Pa kuze |
|---|---|
| **Styles** | Mostra tudu regra apilikadu i regra ki ganha |
| **Computed** | Valor final di kada propriedadi |
| **Layout** | Visualizadô di box model |
| **Event Listeners** | Eventus di JavaScript apilikadu |

### Editar inline na DevTools

- Klika nun valor → muda → karega `Tab` ou `Enter` → testa di imediatu
- Atalhu pa keditá kor: klika na kuadradu di kor → palette pop-up
- `Ctrl+Z` ou `Cmd+Z` pa desfazer

**Mudansa na DevTools é so na memória di browser.** Pa salva, kopia regra di volta pa `style.css`.

### Konsulta MDN

```
Format di búska efetivu:
"mdn css <propriedadi>"
"mdn html <tag>"
"mdn javascript <funsan>"
```

Ka uza só "css gradient" — adisiona "mdn" pa filtra fontis fiável.

### Kuandu pedi ajuda na fórum

1. **Reprodusan mínimu** — un demo na CodePen ou JSFiddle ku só problema, sen restu di projetu.
2. **Mensajen di erru kompletu** — kopia eksatu.
3. **Kuze ki bu dja tentativa** — mostra trabadju.
4. **Resultadu esperadu vs aktual** — kompara.

---

## 12. Flexbox — un dimensan

### Aktiva

```css
.container {
  display: flex;       /* fidju ta torna flex items */
}
```

![Flexbox: main axis (horizontal) i cross axis (vertikal), ku justify-content i align-items]

### Dos eixu

| Eixu | Direksan padron | Propriedadi pa alinha |
|---|---|---|
| **Main axis** | Horizontal (skerda → direita) | `justify-content` |
| **Cross axis** | Vertikal (topu → fundu) | `align-items` |

### Propriedadi di container

```css
.container {
  display: flex;
  flex-direction: row;             /* row | row-reverse | column | column-reverse */
  flex-wrap: wrap;                 /* nowrap | wrap — kuebra pa linha nova */
  justify-content: space-between;  /* main axis */
  align-items: center;             /* cross axis */
  gap: 24px;                       /* espasu entre items */
}
```

### Valor di `justify-content` (main axis)

| Valor | Lojika |
|---|---|
| `flex-start` | Items na komesu (padron) |
| `center` | Sentradu |
| `flex-end` | Na fin |
| `space-between` | Espasu entri items, sen na pontas |
| `space-around` | Espasu igual a la roda di kada item |
| `space-evenly` | Espasu kompletamenti igual entri tudu |

### Valor di `align-items` (cross axis)

| Valor | Lojika |
|---|---|
| `stretch` | Stica pa nxe altura (padron) |
| `center` | Sentradu vertikal |
| `flex-start` / `flex-end` | Topu / fundu |
| `baseline` | Alinha pa linha di testu |

### Propriedadi di item

```css
.item {
  flex: 1;                  /* krese pa absorbi espasu sobra */
  flex: 0 0 300px;          /* ka krese, ka enkolhe, baz 300px */
  align-self: flex-end;     /* sobrepasa align-items */
  order: -1;                /* reorganiza vizual sen muda HTML */
}
```

### Shorthand `flex`

```css
flex: <grow> <shrink> <basis>;

flex: 1;            /* = flex: 1 1 0 — absorbi espasu */
flex: 0 0 300px;    /* largura fixu di 300px */
flex: 2;            /* absorbi 2x mas ki items ku flex: 1 */
```

:::callout{type=tip}
**Sentra vertikal + horizontal nun linha:**
```css
.parent { display: flex; justify-content: center; align-items: center; }
```
Antes di Flexbox, kel-li é un di problema mas frustranti di CSS. Gosi é dos linha.
:::

### Padron komun di Flexbox

```css
/* Header: logo skerda, nav direita */
.header { display: flex; justify-content: space-between; align-items: center; }

/* Byline: foto + nomi lado-a-lado */
.author { display: flex; align-items: center; gap: 16px; }

/* Vertical stack ku gap */
.stack { display: flex; flex-direction: column; gap: 16px; }
```

---

## 13. CSS Grid — dos dimensan

### Aktiva

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr 200px;    /* trez kolunas: fix-fluid-fix */
  grid-template-rows: 100px auto 100px;
  gap: 24px;
}
```

### Unidadi `fr` — divisor di espasu sobra

| Egzemplu | Lojika |
|---|---|
| `1fr 1fr` | Dos kolunas igual |
| `1fr 2fr` | Segunda koluna é 2x mas largu ki primeru |
| `200px 1fr` | Primeru fixu 200px, segunda absorbi restu |
| `repeat(5, 1fr)` | 5 kolunas igual (kurtu pa `1fr 1fr 1fr 1fr 1fr`) |

### `repeat()` — kurtu pa pattern repetidu

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);    /* 3 kolunas igual */
}
```

### Grid vs Flexbox — kuandu uza ken

| Pergunta | Uza |
|---|---|
| Layout di "linhas + kolunas djuntu"? (2D) | **Grid** |
| Layout di "só un eixu"? (1D — fila ou koluna) | **Flexbox** |
| Galeria di kartas ku 3 koluna × N linha | Grid |
| Header ku logo skerda + nav direita | Flexbox |
| Sidebar lado-a-lado ku konteúdu prinsipál | Flexbox |
| Tablu di dadus ku múltiplu koluna | Grid |

### Terminolojia di Grid

```
┌──────┬──────┬──────┐
│ cell │ cell │ cell │   ← row 1 (track horizontal)
├──────┼──────┼──────┤
│ cell │ cell │ cell │   ← row 2
└──────┴──────┴──────┘
   ▲      ▲     ▲
   │      │     └── column 3 (track vertikal)
   │      └── column 2
   └── column 1
```

- **Track:** un linha kompletu (horizontal) ou un koluna kompletu (vertikal).
- **Cell:** un kuadradu individual.
- **Gap:** espasu entri tracks.

### DevTools Grid overlay

Painel Elements → klika batch "grid" na un elementu ku `display: grid`. Pajina ta resebi overlay ku **line numbers**.

---

## 14. Pozisiona i alinha na Grid

### Line numbers

Pa un grelha di 4 koluna, ten **5 line numbers**:

```
| line 1 | line 2 | line 3 | line 4 | line 5 |
   col 1    col 2    col 3    col 4
```

**Negativu konta di fin:** `-1` é últimu, `-2` é penúltimu.

### Pozisiona item

```css
.item {
  grid-column: 1 / 3;       /* komesa line 1, fin line 3 → okupa col 1 i 2 */
  grid-row: 2 / 4;          /* komesa line 2, fin line 4 → okupa row 2 i 3 */
}
```

**Line di fin é eksklusivu:** `1 / 3` = ta okupa 1 i 2, **ka 3**.

### Span

```css
.feature { grid-column: span 2; }              /* okupa 2 kolunas, undi item poza */
.banner  { grid-column: 1 / span 3; }          /* komesa col 1, okupa 3 */
```

### Truk mágiku — `1 / -1`

```css
.hero {
  grid-column: 1 / -1;     /* spani tudu largura, sen importa kuantas koluna */
}
```

:::callout{type=tip}
**`grid-column: 1 / -1` é truk mas útil di Grid.** Memoriza-l. Funsiona indipendentamenti di kuantas koluna existi — si bu muda di 3 pa 5 koluna, hero ta kontinua spani tudu.
:::

### Alinhamentu

| Skopu | Horizontal | Vertikal |
|---|---|---|
| **Items dentru di kada cell** (container-level) | `justify-items` | `align-items` |
| **Item individual** (sobrepasa container) | `justify-self` | `align-self` |
| **Tudu grelha dentru di container** | `justify-content` | `align-content` |

```css
.gallery {
  place-items: center;          /* shorthand: justify-items + align-items */
}
```

**⚠ Grid uza `start`/`end`, NAU `flex-start`/`flex-end`.** Flexbox uza `flex-start`. Ka troka.

### Padron Grid komun

```css
/* Galeria responsiva ki kuebra automatikamenti */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

/* Hero ki spani tudu largura na grid */
.hero { grid-column: 1 / -1; }

/* Grid + Flexbox kombinadu — egzemplu kapstone */
.testimonials {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* externa: Grid 3 koluna */
}
.testimonial {
  display: flex;
  flex-direction: column;                 /* interna: Flexbox vertikal */
  align-items: center;
}
```

---

## 15. Capstone — Visita Kabu Verdi

Lisan 18 + 19 ta konstrui un landing page profisional ku 6 seksan, uzando tudu kuze ki bu aprende.

### Strutura di projetu

```
projetu-kabu-verdi/
├── index.html        (Lisan 18 — só strutura)
├── style.css         (Lisan 19 — só stilu)
└── img/              (10 ilhas + komida + 3 testimuñu)
```

### 6 seksons + sistema di layout di kada un

| # | Seksan | Sistema | Pa kuze |
|---|---|---|---|
| 1 | Header + Hero | Flexbox (nav 1D) | Logo skerda, nav direita |
| 2 | Ilhas grid (10 kartas) | **Grid** (5×2) | 5 koluna, 2 linha |
| 3 | Komida (foto + testu) | Flexbox (2 koluna 1D) | Imajen skerda, testu direita |
| 4 | Muzika (3 kartas) | Grid (3×1) | Trez koluna igual |
| 5 | Testimonhu (3 kartas) | **Grid + Flexbox** | Externa Grid, interna Flexbox |
| 6 | Footer | Flexbox (3 koluna 1D) | Kontaktu, sosial, sobre |

### Reset + baz tipográfiku (kompulsóriu)

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: sans-serif;
  color: #333;
  line-height: 1.5;
  background-color: #f7f0e6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}
```

### Personas + lugar di Kabu Verdi (pa egzemplus)

| Persona | Papel | Lugar |
|---|---|---|
| Djássi | Studanti di dev (L3 onwards) | Mindelo |
| Adilson | Donu di "Blog di Adilson" (L4 onwards) | Mindelo |
| Djamila Tavares | Bilineja di artigus (L10 onwards) | Praia |
| Cesária Évora | Sujeitu di artigu (L5–L7) | Mindelo, mundu |
| Manuel Furtado | Revizor di CSS (L9) | — |
| Cesária Lima | Skritora konvidada (L11, L16, L18) | Fogo |
| Mário Évora | Kronista di musika (L16, L18) | Mindelo |
| Kátia | Frontend dev (L13, L16) | Praia |

**Lugar pa egzemplus:** Mindelo (São Vicente), Praia (Santiago), Cidade Velha (Santiago), Pico do Fogo, Santo Antão, Sal, Boa Vista, Brava.

---

## 16. Errus komun i kumo rezolve

### HTML

| Erru | Sintoma | Solusan |
|---|---|---|
| Skesi `alt` na `<img />` | Akesibilidadi kuebradu, SEO penaltí | Sempri adisiona `alt="..."`. Pa imajen dekorativu, `alt=""` vaziu |
| `<div>` por tudu lado | Pajina sen signifikadu semantiku | Uza `<header>`, `<article>`, `<section>`, `<nav>`, `<footer>` undi apilika |
| Múltiplu `<h1>` por pajina | SEO i akesibilidadi penaltí | **Un `<h1>` por pajina**. Otus = h2-h6 |
| Skesi `<link rel="stylesheet">` | CSS ka ta apilika | Konfirma ki `<link>` sta dentru di `<head>` |
| Path eradu na `src` | Imajen kuebradu, sem konsola error | Verifika kaminhu relativu (`img/foto.jpg`, ka `/foto.jpg`) |

### CSS

| Erru | Sintoma | Solusan |
|---|---|---|
| `!important` por tudu lado | Stilus ta sobrepasa otru kaóticamenti | Otimiza specificity (Lisan 11). Reserva `!important` pa kazu raru |
| LVHA ordi eradu | `:hover` ka ta funsiona | Sempri: link → visited → hover → active |
| `align-items` ka sentra | Container ten altura `auto` | Defini altura ou uza pai ku altura |
| Padding ta kuebra largura | Layout di grid ta kuebra | `* { box-sizing: border-box; }` na topu |
| Grid `flex-start` | Erru sintáksi | Grid uza `start`, ka `flex-start` |
| Flexbox `start` | Erru sintáksi | Flexbox uza `flex-start`, ka `start` |
| `display: flex` sketsidu | Items ka ta brinka | Konfirma na DevTools: container ten `display: flex`/`grid` |

### Debug — sequensia rekumendadu

1. **Abri DevTools** (`F12`) → painel Elements.
2. **Inspekciona elementu** ku problema (klika direitu → Inspect).
3. **Le "Styles"** — kuze regra ta apilika? Kuze sta riskado (sobrepasadu)?
4. **Eksperimenta na DevTools** — muda valor inline, ta funsiona?
5. **Kopia volta pa `style.css`** — salva mudansa.
6. **Si inda ka funsiona:** kopia mensajen + Google "mdn css \<propriedadi\>".

---

## 17. Próximu pasus

**Parabéns** — bu kuncluí Fundamentus di Web.

Bu sabe gosi:

- ✓ HTML semantiku (header, nav, article, section, footer)
- ✓ CSS — selectors, specificity, "inheritance", box model
- ✓ Flexbox pa layout di un dimensan
- ✓ CSS Grid pa layout di dos dimensan
- ✓ DevTools, MDN, debug sistemátiku

Bu pode kostrui un website statiku profisional di komesu a fin.

### Pa onde gosi?

| Próximu pasu | Kuze bu ta aprende |
|---|---|
| **JavaScript** (`intro-javascript`) | Pajina **interativu** — klika, animasan, validasan di formuláriu |
| Responsive design | `@media` queries, mobile-first, breakpoints |
| Frameworks (Tailwind, Vue, React) | Konstruir mas rápidu ku abstrasons |
| Deploy gratis | GitHub Pages, Netlify, Cloudflare Pages |

### Posta projetu di kapstone

1. **CodePen** — `codepen.io/pen` → kopia HTML + CSS → publika ku un klike.
2. **GitHub Pages** — komit projetu na GitHub → Settings → Pages → ativa.
3. **Mostra pa amigus i familia.** Es é primeru projetu real — selebra-l.

:::callout{type=tip}
**Skola sta ta prepara `intro-javascript`** — próximu kursu na sekuensia. Ku mêsmu personas familiar (Djássi, Adilson, Djamila, Mário, Cesária Lima, Kátia, Manuel Furtado), mêsmu kultura kabuverdianu, mêsmu kuidadu pedagóji. Ti lá — pratika kel-li li, posta bu website, i nu ta spera-bu na próximu kursu.

**Nu ta studa, nu ta kria, nu ta partilha.**
:::
