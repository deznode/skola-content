# Loops na Python — Repeti Sin Kansera
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
Imagina bo kre printa nomi di 100 estudantis. Bo ta skrévi 100 `print()`? Nau! Loop ta fazi pa bo — un bes só.

## 2) Core Concept
`for` ta itera sobri un sekuénsia (lista, range, string). `while` ta repeti enguantu kondisun é `True`. `break` ta para loop, `continue` ta pula pa prósimu iterasun.

## 3) Show It
```python
# for ku lista
ilhas = ["Santiago", "São Vicente", "Sal"]
for ilha in ilhas:
    print(f"Oi {ilha}!")
# Output:
# Oi Santiago!
# Oi São Vicente!
# Oi Sal!
```

```python
# for ku range
for i in range(1, 6):
    print(f"Lisun {i}")
# Output: Lisun 1, Lisun 2, ... Lisun 5
```

```python
# while ku kontador
tentativas = 3
while tentativas > 0:
    print(f"Bo tene {tentativas} tentativas.")
    tentativas -= 1
# Output:
# Bo tene 3 tentativas.
# Bo tene 2 tentativas.
# Bo tene 1 tentativas.
```

## 4) Takeaway
`for` = kuandu bo sabi kuantu bes repeti. `while` = kuandu bo ka sabi, so kondisun. Nunka skexi `:` e indentasun!

## 5) CTA
Tenta gosi: uza `for` pa printa tabuada di multiplikasun di 7!

---
**B-roll notes**: Animasun di loop (séta ki ta volta) → kódiku na terminal → output aparese linja a linja → mustra `break` ki ta para loop
**End card**: "Prósimu: Listas — bo priméru estrutura di dadus"
