# Lambda, Map e Filter — Transforma Dadus na Un Linja
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Ás bes bo ka presiza un funson inteiru — só un espresun rápidu. Lambda é funson sin nomi, na un linja só.

```python
# Funson normal
def dobru(x):
    return x * 2

# Mesmu kuza ku lambda
dobru = lambda x: x * 2
print(dobru(5))  # 10
```

**Kombina ku `map()` e `filter()`:**

```python
presus = [500, 1200, 800, 350, 2000]

# map — aplika funson a TUDU elementu
ku_iva = list(map(lambda p: p * 1.15, presus))
print(ku_iva)
# [575.0, 1380.0, 920.0, 402.5, 2300.0]

# filter — filtra elementus ki pasa kondisun
karus = list(filter(lambda p: p > 1000, presus))
print(karus)
# [1200, 2000]
```

```python
# Pipeline: filtra + transforma
nomis = ["maria", "djon", "ana", "amilka", "gil"]
longus = list(map(str.upper, filter(lambda n: len(n) > 3, nomis)))
print(longus)
# ['MARIA', 'DJON', 'AMILKA']
```

**Takeaway**: `lambda` = funson rápidu. `map` = transforma tudu. `filter` = guarda só ki pasa. Kombina pa pipelines poderozu!

**Prósimu**: Funsoens inkorporadus úteis — enumerate, zip, sorted
