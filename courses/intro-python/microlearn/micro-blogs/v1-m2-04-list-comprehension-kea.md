# List Comprehension — Kria Lista na Un Linja Só
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Imagina bo kre filtra un lista. Na lugar di skrévi loop inteiru, Python ta permite kria lista novu na **un linja só** ku list comprehension.

```python
# Manera tradisionál (4 linjas)
notis = [85, 42, 91, 67, 38, 78, 95]
aprovadu = []
for n in notis:
    if n >= 50:
        aprovadu.append(n)
print(aprovadu)  # [85, 91, 67, 78, 95]

# List comprehension (1 linja!)
aprovadu = [n for n in notis if n >= 50]
print(aprovadu)  # [85, 91, 67, 78, 95]
```

**Anatomia:** `[expresun for item in iterável if kondisun]`

Más ezemplu:

```python
# Transforma: nomi pa maiúskula
nomis = ["maria", "djon", "ana"]
maiúskulas = [n.upper() for n in nomis]
print(maiúskulas)  # ['MARIA', 'DJON', 'ANA']

# Kria: kuadradu di 1 a 5
kuadradu = [x ** 2 for x in range(1, 6)]
print(kuadradu)  # [1, 4, 9, 16, 25]
```

**Takeaway**: List comprehension = `for` + `if` + expresun, tudu na un linja. Más Pythonic, más rápidu, más limpu.

**Prósimu**: Tuplas — Kolesoens ki ka muda
