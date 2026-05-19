# Eransa — Reutiliza Kódiku di Klasis
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
Bo tene un klasi Animál. Gatu é animál, Katxor é animál — pamodi skrévi tudu di novu? Eransa ta permite bo reutiliza!

## 2) Core Concept
Eransa permite un klasi filhu erda atributus e métodus di klasi pai. Klasi filhu podi adisiona kuza novu ó modifika konportamentu ku `super()` e method overriding.

## 3) Show It
```python
class Animal:
    def __init__(self, nomi, son):
        self.nomi = nomi
        self.son = son

    def fala(self):
        return f"{self.nomi} ta fazi: {self.son}!"

# Klasi filhu ta erda di Animal
class Gatu(Animal):
    def __init__(self, nomi):
        super().__init__(nomi, "Miau")

    def ronrona(self):
        return f"{self.nomi} ta ronrona... prrrr"

class Katxor(Animal):
    def __init__(self, nomi):
        super().__init__(nomi, "Au au")

mingau = Gatu("Mingau")
bobi = Katxor("Bobi")

print(mingau.fala())     # Mingau ta fazi: Miau!
print(mingau.ronrona())  # Mingau ta ronrona... prrrr
print(bobi.fala())       # Bobi ta fazi: Au au!
```

## 4) Takeaway
`class Filhu(Pai)` pa erda. `super().__init__()` pa xama konstrutor di pai. Eransa = reutilizasun másimu!

## 5) CTA
Tenta gosi: kria un klasi `Veíkulu` e dos filhus — `Karu` e `Motu` — kada un ku si métudu espesiál!

---
**B-roll notes**: Diagrama di árvori di família (Pai → Filhus) → kódiku na terminal → mustra ki Gatu tene métodus di Animal + si própirius
**End card**: "Prósimu: Polimorfismu — Mesmu métudu, konportamentu diferenti"
