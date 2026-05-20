# Listas na Python — Guarda Tudu na Un Lugár
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
Bo tene sinku ilhas favoritu? Dés notis di prova? Python list ta guarda tudu na un lugár só — e bo podi muda a kualker momentu!

## 2) Core Concept
Lista é kolesoens **ordenadu** e **mutável** di elementus. Bo ta kria ku `[]`, asesa ku índisi (kumesa na 0), e modifika ku métodus komu `append()`, `remove()`, e `sort()`.

## 3) Show It
```python
# Kria un lista
ilhas = ["Santiago", "São Vicente", "Sal", "Fogo"]

# Asesa elementus (índisi kumesa na 0!)
print(ilhas[0])     # Santiago
print(ilhas[-1])    # Fogo (últimu!)

# Adisiona
ilhas.append("Brava")
print(ilhas)
# ['Santiago', 'São Vicente', 'Sal', 'Fogo', 'Brava']

# List comprehension — kria lista na 1 linja!
notis = [85, 42, 91, 67, 55, 78]
aprovadu = [n for n in notis if n >= 50]
print(aprovadu)
# [85, 91, 67, 55, 78]
```

## 4) Takeaway
Lista = kolesoens ki bo podi muda. Índisi kumesa na 0. List comprehension ta kria listas filtradu na un linja só!

## 5) CTA
Tenta gosi: kria lista ku 5 fruta e uza list comprehension pa filtra só kes ku más di 5 letras!

---
**B-roll notes**: Vizualizasun di lista komu kaxas numeradu (0, 1, 2...) → animasun di `append()` ki ta adisiona kaxa → list comprehension ku séta ki ta filtra
**End card**: "Prósimu: Disionárius — Guarda dadus ku xavi"
