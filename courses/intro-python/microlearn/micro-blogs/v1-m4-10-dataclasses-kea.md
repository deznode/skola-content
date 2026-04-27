# Dataclasses — Klasis Simples sin Boilerplate
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Bo sta kansadu di skrévi `__init__`, `__str__`, `__repr__`, `__eq__` pa kada klasi? `@dataclass` ta fazi tudu pa bo!

```python
# SIN dataclass (tantu kódiku!)
class Estudanti:
    def __init__(self, nomi, ilha, nota):
        self.nomi = nomi
        self.ilha = ilha
        self.nota = nota

    def __repr__(self):
        return f"Estudanti(nomi='{self.nomi}', ilha='{self.ilha}', nota={self.nota})"

    def __eq__(self, other):
        return self.nomi == other.nomi and self.ilha == other.ilha
```

```python
# KU dataclass (limpu!)
from dataclasses import dataclass

@dataclass
class Estudanti:
    nomi: str
    ilha: str
    nota: float = 0.0  # valor default

# Python ta jera __init__, __repr__, __eq__ automátikamenti!
maria = Estudanti("Maria", "Praia", 85.5)
ana = Estudanti("Ana", "São Vicente")

print(maria)
# Estudanti(nomi='Maria', ilha='Praia', nota=85.5)

print(ana.nota)   # 0.0 (default)
print(maria == Estudanti("Maria", "Praia", 85.5))  # True
```

**Kuandu uza:**
- Klasis ki guarda **principalmenti dadus** → `@dataclass`
- Klasis ku lójika kompleksu → klasi tradisionál

**Takeaway**: `@dataclass` ta elimina boilerplate. Defini kampu ku tipu e Python ta jera `__init__`, `__repr__`, `__eq__` pa bo!

**Prósimu**: Parabéns! Bo kaba kursu di Python. Ki tal kria un projetu real?
