# Klasis e Objetis — Kria Bo Própriu Tipu
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~90s

## 1) Hook
Klasi é komu reseta di katchupa — moldi ki ta dize kumu fazi. Objetu é katchupa real na bo pratu!

## 2) Core Concept
Klasi é moldi ki ta defini atributus (dadus) e métodus (asoens). `__init__` é konstrutor ki ta inisializa atributus. `self` é referénsia pa objetu atual.

## 3) Show It
```python
class Estudanti:
    def __init__(self, nomi, ilha, nota):
        self.nomi = nomi
        self.ilha = ilha
        self.nota = nota

    def é_aprovadu(self):
        return self.nota >= 50

    def __str__(self):
        status = "Aprovadu" if self.é_aprovadu() else "Reprovadu"
        return f"{self.nomi} di {self.ilha} — {status} ({self.nota})"

# Kria objetis (instánsias)
maria = Estudanti("Maria", "Praia", 85)
djon = Estudanti("Djon", "Fogo", 42)

print(maria)           # Maria di Praia — Aprovadu (85)
print(djon)            # Djon di Fogo — Reprovadu (42)
print(maria.é_aprovadu())  # True
print(djon.é_aprovadu())   # False
```

## 4) Takeaway
`class` = moldi, `__init__` = konstrutor, `self` = "es objetu aki". Un klasi, vários objetis independentis!

## 5) CTA
Tenta agora: kria un klasi `Ilha` ku nomi, populasun e un métudu ki diz si é grandi (> 50,000 habitantis)!

---
**B-roll notes**: Animasun di moldi di biskoitu → vários biskoitus diferentis (objektus) → kódiku na terminal → kria maria e djon → mustra output diferenti pa kada un
**End card**: "Prósimu: Eransa — Reutiliza kódiku di klasis"
