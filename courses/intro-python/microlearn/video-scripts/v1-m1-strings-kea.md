# f-strings — Manera Limpu pa Formata Textu
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~60s

## 1) Hook
Para ku konkatenason messy ku `+`! f-strings ta fazi formatason di textu limpu na un linja só.

## 2) Core Concept
f-string é un string ku `f` na kumeso. Bo ta pô variáveis dentu di `{chaves}` e Python ta substitui ku valóris automátikamenti.

## 3) Show It
```python
nomi = "Djon"
ilha = "Fogo"

# Manera antigu (konfuzu)
msg = "Oi, " + nomi + " di " + ilha + "!"
print(msg)
# Output: Oi, Djon di Fogo!

# f-string (limpu!)
msg = f"Oi, {nomi} di {ilha}!"
print(msg)
# Output: Oi, Djon di Fogo!

# Espresun dentu di chaves
presu = 850
print(f"Presu ku IVA: {presu * 1.15:.2f} ECV")
# Output: Presu ku IVA: 977.50 ECV
```

```python
# Truki di debug (Python 3.8+)
idadi = 25
print(f"{idadi=}")
# Output: idadi=25
```

## 4) Takeaway
Pô `f` antes di string, variáveis dentu di `{chaves}` — ka bu mesti más `+` nen `str()`.

## 5) CTA
Tenta gosi: kria un f-string ki printa bo nomi, idadi e ilha na un frazi!

---
**B-roll notes**: Split-screen — kudu skerda ku `+` (rixadu na vermelhu) vs kudu dreitu ku f-string (limpu na verdi) → animasun di `{chaves}` ki ta enxi ku valores
**End card**: "Prósimu: Operadoris — Kalkula ku Python"
