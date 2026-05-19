# Disionárius — Guarda Dadus ku Xavi
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
Imagina un kadérnu di kontatus: pa kada nomi, bo tene un telefoni. Python dict funsiona igual — xavi ta aponta pa valor!

## 2) Core Concept
Disionáriu (`dict`) é kolesoens di **pares xavi:valor**. Xavis é únikis. Bo ta asesa valóris pela xavi (ka por índisi). É perfetu pa mapea un kuza pa otru.

## 3) Show It
```python
# Kria un disionáriu
estudanti = {
    "nomi": "Ana",
    "ilha": "Santiago",
    "idadi": 20,
    "kursu": "Informátika"
}

# Asesa ku xavi
print(estudanti["nomi"])       # Ana
print(estudanti.get("nota", 0))  # 0 (default si ka esisti)

# Adisiona/muda valores
estudanti["nota"] = 85
estudanti["idadi"] = 21

# Itera sobri pares
for xavi, valor in estudanti.items():
    print(f"{xavi}: {valor}")
# nomi: Ana
# ilha: Santiago
# idadi: 21
# kursu: Informátika
# nota: 85
```

## 4) Takeaway
Dict = kadérnu di kontatus di Python. Xavi ta asesa valor diretamenti — sem busca na lista intéru. Uza `.get()` pa evita erru!

## 5) CTA
Tenta gosi: kria un dict ku dadus di 3 ilhas (nomi, populasun, kapital) e printa informason di kada un!

---
**B-roll notes**: Animasun di kadérnu ki ta abri → xavi:valor ligadu ku séta → mustra `.get()` vs `[]` → itera ku `.items()`
**End card**: "Prósimu: Sets — Konjuntus sin duplikadus"
