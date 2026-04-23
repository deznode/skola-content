# Operadoris di Python — Más ki Soma e Subtrasun
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Python tene operadoris ki vai txeu alen di `+` e `-`. Konxe 3 familias:

```python
# ARITMÉTIKU — kalkula
presu = 500
iva = presu * 0.15       # 75.0
total = presu + iva       # 575.0
troku = 1000 // 575       # 1 (divisun intéru)
restu = 1000 % 575        # 425 (restu)
kuadradu = 5 ** 2         # 25 (poténsia)
```

```python
# KOMPARASUN — kompara (retorna True/False)
idadi = 20
print(idadi >= 18)    # True
print(idadi == 25)    # False
print(idadi != 25)    # True
```

```python
# LÓJIKU — kombina kondison
tene_bilheti = True
idadi = 16

# and: AMBOS deve ser True
print(tene_bilheti and idadi >= 18)  # False

# or: PELO MENUS un deve ser True
print(tene_bilheti or idadi >= 18)   # True

# not: inverte
print(not tene_bilheti)  # False
```

**Takeaway**: `//` pa divisun intéru, `%` pa restu, `**` pa poténsia. `and`/`or`/`not` pa kombina kondison.

**Prósimu**: Kondisionais — if/elif/else
