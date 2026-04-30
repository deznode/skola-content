---
trace_id: Skola-micro_blog-smoke-019-2026-04-29-fixerus-na-python-le-un-fixeru-di-tekstu
topic: smoke-019
module: fixerus-na-python
lesson: le-un-fixeru-di-tekstu
kind: micro_blog
language: kea
generated_at: 2026-04-29T14:31:46.858Z
---

# 📄 Aprende kumu lê fikserus di tekstu na Python — na Kabuverdianu!

Fikserus di tekstu é un di kes ferramentus más fundamentais na programason. Na Python, tres linhas di kódigo é sufisientes pa abri, lê, é txada un fikxeru di forma **100% segura**.

---

## A Fórmula Básika

```python
with open("mensajen.txt", "r", encoding="utf-8") as f:
    for linha in f.readlines():
        print(linha.strip())
```

Kel kódigo ta fazi trés kuzas importantes:
1. **Abri** fikxeru na modu leitura (`"r"`)
2. **Lê** kada linha kumu lista
3. **Txada otomatikamenti** — grasas a `with`

---

## Purkê `encoding="utf-8"` é Obrigatóriu?

Si bu ta skrebe na Kabuverdianu, bu ta uza letras kuma `ã`, `ê`, `ç`, `ó`. Sem `encoding="utf-8"`, Python ta podi mosta kes karatéris mal — sóbretudo na Windows.

**Régia simples:** sempri mete `encoding="utf-8"`. Puntu final.

---

## `read()` ou `readlines()`?

- `read()` → volta **totu fikxeru** kumu un string — bon pa fikserus pikininus
- `readlines()` → volta **lista di linhas** — bon pa prosesa linha a linha
- `readline()` → volta **un sô linha** — bon pa lê inkrementalmente

---

## A Armadilha Más Komun

Skisi `.strip()` ta deixa `\n` na kabo di kada linha, ki ta krea linhas brankas extra na saída. Un simples `.strip()` ta resolve!

---

💡 **Kel ki bu ta aprendê na próxima lisaun:** kumu **skrebe é juntar** tekstu na fikserus — kum `"w"` é `"a"` modus. Sigi na frenti!

---

🔗 *Kel lisaun fazi parti di "Fixerus na Python" — un módulu di kursus Skola pa aprendedóris di nível basiku.*

#Python #Kabuverdianu #Programason #FileIO #Skola
