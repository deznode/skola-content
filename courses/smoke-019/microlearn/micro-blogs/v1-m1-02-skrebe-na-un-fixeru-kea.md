---
trace_id: Skola-micro_blog-smoke-019-2026-04-29-fixerus-na-python-skrebe-na-un-fixeru
topic: smoke-019
module: fixerus-na-python
lesson: skrebe-na-un-fixeru
kind: micro_blog
language: kea
generated_at: 2026-04-29T14:33:39.326Z
---

# ✍️ Skrebe na Fikserus ku Python — Modu `"w"` kontra `"a"` Esplicadu

Bu ta sabi lê fikserus na Python. Mas kumu ki bu ta **skrebe** neles — sem destrui ki já staba li? Es é a distinsaun ki separa prinsipianti di programadóris segurus.

---

## Dós Modus, Dós Komportamentus

```python
# "w" — PERIGÓZU: sobreskribi tudo!
with open("rejistu.txt", "w", encoding="utf-8") as f:
    f.write("Entrada nova\n")

# "a" — SEGURU: juntar na fin
with open("rejistu.txt", "a", encoding="utf-8") as f:
    f.write("Otra entrada\n")
```

**Regra simples:**
- Bu ta **kria** un fikxeru? → `"w"`
- Bu ta **juntar** na fikxeru? → `"a"`

---

## O `\n` ki Todos Skisi

Diferenti di `print()`, `write()` **nun ta mete** newline otomatikamente. Skisi `\n` é bu ta vê linhas fundidas:

```
❌  Bon diaKomu ki bu sta
✅  Bon dia
    Komu ki bu sta
```

Kel `\n` pikininu ta fazi tódu diferensa!

---

## A Verifikason di Ouru

Depôs di skrebe, sempre verifikadu:

```python
with open("rejistu.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Un leitura rápida ta poupadu di surprezas em produson.

---

## Uza Sempri `encoding="utf-8"`

Si bu ta skrebe na Kabuverdianu — letras kuma `ã`, `ê`, `ç` — sem UTF-8 bu ta armazena lixu. Kel parâmetru é non-negociável.

---

💡 **Prósimu Nivel:** `pathlib.Path`, fikserus CSV, é JSON — kes skon aprofundan kel habilidade.

---

🔗 *Lisaun 2 di "Fixerus na Python" — kursus Skola pa aprendedóris di nível basiku.*

#Python #Programason #Kabuverdianu #FileIO #Skola #Kea
