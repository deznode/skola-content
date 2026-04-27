# 4 Pilaris di OOP — Mapa Rápidu
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Programasun Orientadu a Objetu (OOP) tene 4 pilaris. Kada un tene un papél:

```python
# 1. ENKAPSOLAMENTU — proteje dadus
class KontaBankáriu:
    def __init__(self, titulár):
        self.titulár = titulár
        self.__saldu = 0  # privadu!

    @property
    def saldu(self):
        return self.__saldu

    def deposita(self, valor):
        if valor > 0:
            self.__saldu += valor

konta = KontaBankáriu("Maria")
konta.deposita(5000)
print(konta.saldu)  # 5000
# konta.__saldu = -1  # Ka funsiona!
```

```python
# 2. ERANSA — reutiliza kódiku
class Animal:
    def fala(self):
        return "..."

class Gatu(Animal):  # erda di Animal
    def fala(self):
        return "Miau!"

# 3. POLIMORFISMU — mesmu métudu, konportamentu diferenti
animais = [Gatu(), Animal()]
for a in animais:
    print(a.fala())  # Miau! ... 

# 4. ABSTRASUN — skondi komplexidadi
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def área(self):  # OBRIGA filhus implementa!
        pass
```

**Resumu:**
- **Enkapsolamentu** = proteje dadus (`__privadu`, `@property`)
- **Eransa** = reutiliza (`class Filhu(Pai)`)
- **Polimorfismu** = mesmu interfasi, vários konportamentus
- **Abstrasun** = skondi detalhes (ABC, `@abstractmethod`)

**Takeaway**: OOP organiza kódiku na objektus ku dadus protejedu, kódiku reutilizável, e interfasis limpu.

**Prósimu**: Métodus mádjiku — __str__, __repr__, __add__
