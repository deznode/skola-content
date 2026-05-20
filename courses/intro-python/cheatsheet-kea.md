# Python Cheatsheet — Introdusun Konpletu a Python

**Lingua:** kea (Kabuverdianu) | **Python:** 3.13+ | **Doc version:** 1.0.0 | **Validadu na:** 2026-04-21

> **Pa ken?** Prinsipiantes absolutu — estudantes Kabuverdianu ki sta kumesa programa ku Python.
> **Kumo uza:** Referensia rápidu pa konsulta durante kursu. Kopia e kola kódikus diretu pa bo editor.

---

## Índisi

1. [Setup e Ambiente](#1-setup-e-ambiente)
2. [Variáveis e Tipu di Dadus](#2-variáveis-e-tipu-di-dadus)
3. [Strings](#3-strings)
4. [Operadoris](#4-operadoris)
5. [Kondisionais](#5-kondisionais)
6. [Loops](#6-loops)
7. [Listas](#7-listas)
8. [Tuplas](#8-tuplas)
9. [Disionárius](#9-disionárius)
10. [Konjuntus (Sets)](#10-konjuntus-sets)
11. [Funsoens](#11-funsoens)
12. [Lambda, Map e Filter](#12-lambda-map-e-filter)
13. [Funsoens Inkorporadus Úteis](#13-funsoens-inkorporadus-úteis)
14. [Jeneradorus](#14-jeneradorus)
15. [Módulus e Pakotis](#15-módulus-e-pakotis)
16. [Ambiente Virtual e pip](#16-ambiente-virtual-e-pip)
17. [Operasoens ku Ficheru](#17-operasoens-ku-ficheru)
18. [Tratamentu di Erru](#18-tratamentu-di-erru)
19. [Annotasoens di Tipu](#19-annotasoens-di-tipu)
20. [Testu ku pytest](#20-testu-ku-pytest)
21. [Klasis e Objetis (OOP)](#21-klasis-e-objetis-oop)
22. [Eransa](#22-eransa)
23. [Polimorfismu e Abstrasun](#23-polimorfismu-e-abstrasun)
24. [Enkapsolamentu e @property](#24-enkapsolamentu-e-property)
25. [Métodus Mádjiku e Sobrekarga](#25-métodus-mádjiku-e-sobrekarga)
26. [Dataclasses](#26-dataclasses)
27. [Komprehensions (Rezumu)](#27-komprehensions-rezumu)
28. [Errus Komun e Kumo Rezolvé](#28-errus-komun-e-kumo-rezolvé)

---

## 1. Setup e Ambiente

### Instala Python

```bash
# Windows: Bai python.org → Download → IMPORTANTE: Marka "Add python.exe to PATH"!

# macOS: Bai python.org → Download .pkg
# (Ka uza Homebrew — e tene problemas ku upgrades silensiozu)

# Linux (Ubuntu/Debian):
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

### Verifica Instalasun

```bash
python --version        # Python 3.13.x
pip --version           # pip 24.x
```

### VS Code Setup

1. Instala extension **ms-python.python**
2. Abri pasta di projetu → VS Code deteta `.venv` automátiku
3. Seleta interpreter: klika na versun Python na barra di status

### Primeiro Programa

```python
print("Ola, Mundu!")     # Bo primeiro programa Python!
print("Nu ta kria djuntu!")
```

---

## 2. Variáveis e Tipu di Dadus

### Deklara Variáveis

```python
nomi = "Maria"          # str  — textu
idadi = 25              # int  — numeru interu
altura = 1.68           # float — numeru desimal
é_estudanti = True      # bool — True ou False
```

### Regras di Nomi

| Válidu | Inválidu | Razun |
|--------|----------|-------|
| `nomi` | `2nomi` | Ka pode kumesa ku numeru |
| `_privadu` | `nomi-kompletu` | Ka pode tene `-` (ífen) |
| `nota_final` | `class` | Ka pode uza palavra reservadu |

### Konversun di Tipu

```python
# str → int/float
idadi = int("25")            # 25
presu = float("9.99")       # 9.99

# int/float → str
textu = str(25)              # "25"

# input() SENPRI retorna string!
idadi = int(input("Bo idadi: "))
```

### type() — Verifica Tipu

```python
print(type(nomi))        # <class 'str'>
print(type(idadi))       # <class 'int'>
print(type(é_estudanti)) # <class 'bool'>
```

### 4 Tipus Báziku

| Tipu | Ezemplu | Uzu |
|------|---------|-----|
| `int` | `42`, `-10`, `0` | Kontadoris, idadi, kantidadi |
| `float` | `3.14`, `-0.5` | Presus, nota, medidas |
| `str` | `"Maria"`, `'Ola'` | Nomi, textu, mensajen |
| `bool` | `True`, `False` | Kondison, flag, validason |

---

## 3. Strings

### Kria Strings

```python
nomi = "Djon"
frase = 'Nu ta kria djuntu!'
multilinha = """
Praia é kapital
di Kabu Verdi.
"""
```

### Métodus di String

| Métudu | Ezemplu | Resultadu |
|--------|---------|-----------|
| `.upper()` | `"djon".upper()` | `"DJON"` |
| `.lower()` | `"DJON".lower()` | `"djon"` |
| `.capitalize()` | `"djon silva".capitalize()` | `"Djon silva"` |
| `.title()` | `"djon silva".title()` | `"Djon Silva"` |
| `.strip()` | `"  ola  ".strip()` | `"ola"` |
| `.split()` | `"Djon Ana Maria".split()` | `["Djon", "Ana", "Maria"]` |
| `"x".join()` | `"-".join(["2026","04","21"])` | `"2026-04-21"` |
| `.replace()` | `"ola".replace("o","O")` | `"Ola"` |
| `.find()` | `"Kabu Verdi".find("Verdi")` | `5` |
| `.count()` | `"banana".count("a")` | `3` |
| `.startswith()` | `"Python".startswith("Py")` | `True` |
| `.isdigit()` | `"123".isdigit()` | `True` |

### Slicing

```python
nomi = "Amilka"
nomi[0]       # "A"         — primeiro karakter
nomi[-1]      # "a"         — últimu karakter
nomi[1:4]     # "mil"       — di 1 até 3
nomi[:3]      # "Ami"       — primeru 3
nomi[::2]     # "Alk"       — keda 2
nomi[::-1]    # "aklimA"    — reversu
```

### f-strings (Formatason)

```python
nomi = "Maria"
idadi = 22
print(f"Nha nomi é {nomi} e N tene {idadi} anu.")

# Expresoens dentu di {}
presu = 150.5
print(f"Presu: {presu:.2f} ECV")   # "Presu: 150.50 ECV"

# Debug rápidu (Python 3.8+)
nota = 18.5
print(f"{nota=}")                    # "nota=18.5"
```

---

## 4. Operadoris

### Aritmetiku

| Operador | Nomi | Ezemplu | Resultadu |
|----------|------|---------|-----------|
| `+` | Adisun | `10 + 3` | `13` |
| `-` | Subtrasun | `10 - 3` | `7` |
| `*` | Multiplikasun | `10 * 3` | `30` |
| `/` | Divizun (float!) | `10 / 3` | `3.333...` |
| `//` | Divizun interu | `10 // 3` | `3` |
| `%` | Módulu (restu) | `10 % 3` | `1` |
| `**` | Exponensiasun | `2 ** 5` | `32` |

### Komparasun

| Operador | Signifikadu | Ezemplu | Resultadu |
|----------|-------------|---------|-----------|
| `==` | Igual | `5 == 5` | `True` |
| `!=` | Diferenti | `5 != 3` | `True` |
| `>` | Maior ki | `5 > 3` | `True` |
| `<` | Menor ki | `5 < 3` | `False` |
| `>=` | Maior ou igual | `5 >= 5` | `True` |
| `<=` | Menor ou igual | `5 <= 3` | `False` |

### Lójiku

| Operador | Signifikadu | Ezemplu | Resultadu |
|----------|-------------|---------|-----------|
| `and` | I (ambos True) | `True and False` | `False` |
| `or` | Ou (un True txega) | `True or False` | `True` |
| `not` | Nega (inverte) | `not True` | `False` |

---

## 5. Kondisionais

### if / elif / else

```python
idadi = 20

if idadi < 13:
    print("Fidju")
elif idadi < 18:
    print("Adolesenti")
else:
    print("Adultu")
```

### Kondisional Aninhadu

```python
numeru = int(input("Mete un numeru: "))

if numeru > 0:
    print("Pozitivu")
    if numeru % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
elif numeru == 0:
    print("Zeru")
else:
    print("Negativu")
```

### match/case (Python 3.10+)

```python
operasun = input("Skolhe (+, -, *, /): ")

match operasun:
    case "+":
        print("Adisun")
    case "-":
        print("Subtrasun")
    case "*":
        print("Multiplikasun")
    case "/":
        print("Divizun")
    case _:
        print("Operasun inválidu")
```

### Ternary (un linha)

```python
idadi = 20
status = "adultu" if idadi >= 18 else "menor"
```

---

## 6. Loops

### for ku range()

```python
# range(stop)
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# range reversu
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
    print(i)
```

### for ku koleson

```python
nomi = "Ana"
for letra in nomi:
    print(letra)             # A, n, a

ilhas = ["Santiago", "Santo Antão", "Fogo"]
for ilha in ilhas:
    print(ilha)
```

### while

```python
kontador = 0
while kontador < 5:
    print(kontador)
    kontador += 1            # Ka skexi inkrementa!
```

### break, continue, pass

```python
# break — sai di loop
for i in range(10):
    if i == 5:
        break                # Para na 5
    print(i)                 # 0, 1, 2, 3, 4

# continue — pula iterasun atual
for i in range(10):
    if i % 2 == 0:
        continue             # Pula pares
    print(i)                 # 1, 3, 5, 7, 9

# pass — ka fazi nada (placeholder)
for i in range(5):
    pass                     # TODO: implementa dipós
```

### for-else

```python
# else roda SÓMENTE si loop ka teve break
for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(f"{n} é primu")
```

---

## 7. Listas

### Kria e Asesa

```python
frutas = ["manga", "banana", "papaia", "laranja"]

frutas[0]       # "manga"      — primeiro
frutas[-1]      # "laranja"    — últimu
frutas[1:3]     # ["banana", "papaia"]
frutas[::-1]    # lista reversu
```

### Métodus di Lista

| Métudu | Uson | Ezemplu |
|--------|------|---------|
| `.append(x)` | Junta na final | `frutas.append("koko")` |
| `.insert(i, x)` | Inseri na pozisun | `frutas.insert(0, "melun")` |
| `.remove(x)` | Tira primeiro x | `frutas.remove("banana")` |
| `.pop()` | Tira e retorna últimu | `ultimo = frutas.pop()` |
| `.pop(i)` | Tira na pozisun i | `frutas.pop(0)` |
| `.sort()` | Ordena (in-place) | `frutas.sort()` |
| `.reverse()` | Reversa (in-place) | `frutas.reverse()` |
| `.index(x)` | Atxa pozisun di x | `frutas.index("manga")` |
| `.count(x)` | Konta okurensias | `frutas.count("banana")` |
| `.clear()` | Limpa tudu | `frutas.clear()` |
| `len()` | Tamañu | `len(frutas)` |

### List Comprehension

```python
# [expresun for item in iterável if kondisun]
kuadradus = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pares = [n for n in range(20) if n % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

maiuskula = [nomi.upper() for nomi in ["maria", "djon", "ana"]]
# ["MARIA", "DJON", "ANA"]
```

---

## 8. Tuplas

### Kria e Uza

```python
kores = ("azul", "verdi", "amarelu")
kores[0]         # "azul"
kores[-1]        # "amarelu"
# kores[0] = "branku"  # TypeError! Tupla é IMUTÁVEL

len(kores)       # 3
"azul" in kores  # True
```

### Packing e Unpacking

```python
# Packing (automátiku)
koordenadas = 14.9, -23.5     # tupla!

# Unpacking
latitude, longitude = koordenadas

# Star unpacking
primeiro, *meiu, ultimu = (1, 2, 3, 4, 5)
# primeiro=1, meiu=[2, 3, 4], ultimu=5
```

### Kuandu Uza Tupla vs Lista?

| Tupla `()` | Lista `[]` |
|------------|-----------|
| Dadus ki ka muda (koordenadas, kores RGB) | Dadus ki muda (tarefas, karrinhu di kompra) |
| Mais rápidu na memória | Mais métodus disponível |
| Pode uza kumo xavi di dict | Ka pode uza kumo xavi di dict |

---

## 9. Disionárius

### Kria e Asesa

```python
estudanti = {
    "nomi": "Amilka",
    "idadi": 20,
    "ilha": "Santiago",
    "nota": 17.5
}

estudanti["nomi"]                  # "Amilka"
estudanti.get("email", "N/A")     # "N/A" (sem KeyError)
```

### Modifika

```python
estudanti["nota"] = 18.0          # atualiza
estudanti["email"] = "amilka@mail.cv"  # junta novu
del estudanti["ilha"]             # elimina
```

### Métodus Prinsipal

| Métudu | Retorna |
|--------|---------|
| `.keys()` | Tudu xavis |
| `.values()` | Tudu valoris |
| `.items()` | Pares (xavi, valor) |
| `.get(k, default)` | Valor ou default |
| `.copy()` | Kópia independenti |
| `.update(other)` | Merge ku otru dict |

### Itera Sobri Dict

```python
for xavi, valor in estudanti.items():
    print(f"{xavi}: {valor}")
```

### Dict Comprehension

```python
kuadradus = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Kontador di frekensia
palavras = ["python", "é", "legal", "python", "é"]
frek = {}
for p in palavras:
    frek[p] = frek.get(p, 0) + 1
# {"python": 2, "é": 2, "legal": 1}
```

### Merge di Disionárius

```python
base = {"nomi": "Maria", "idadi": 25}
extra = {"ilha": "Fogo", "idadi": 26}
mergedu = {**base, **extra}
# {"nomi": "Maria", "idadi": 26, "ilha": "Fogo"}  — últimu ganha
```

---

## 10. Konjuntus (Sets)

### Kria

```python
ilhas = {"Santiago", "Fogo", "Santo Antão", "Sal"}
di_lista = set([1, 2, 2, 3, 3])    # {1, 2, 3} — auto-deduplika
vaziu = set()                        # KA {}  (es é dict vaziu!)
```

### Operasoens Prinsipal

```python
ilhas.add("Brava")                   # junta
ilhas.remove("Sal")                  # tira (KeyError si ka existe)
ilhas.discard("Sal")                 # tira (sem error si ka existe)
"Santiago" in ilhas                  # True — verifikasun rápidu O(1)
```

### Operasoens Matemátiku

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b      # {1, 2, 3, 4, 5, 6}  — union
a & b      # {3, 4}               — intersection
a - b      # {1, 2}               — diferensa
a ^ b      # {1, 2, 5, 6}         — simétrika (só un ou otru)
```

### Deduplika Lista

```python
ku_duplikadus = [1, 2, 2, 3, 3, 3]
sem_duplikadus = list(set(ku_duplikadus))    # [1, 2, 3]
```

### Set Comprehension

```python
pares = {x for x in range(20) if x % 2 == 0}
```

---

## 11. Funsoens

### Defini e Txama

```python
def saudason(nomi):
    """Saudason personalizadu."""
    print(f"Ola, {nomi}! Tudo dretu?")

saudason("Djina")    # Ola, Djina! Tudo dretu?
```

### Parámetrus

```python
# Parámetru ku valor default
def saudason(nomi, lingua="kea"):
    if lingua == "kea":
        print(f"Ola, {nomi}!")
    elif lingua == "pt":
        print(f"Olá, {nomi}!")

saudason("Maria")              # Ola, Maria!
saudason("Maria", "pt")       # Olá, Maria!
```

### return

```python
def soma(a, b):
    return a + b

resultadu = soma(10, 5)        # 15
```

### *args e **kwargs

```python
# *args — argumentus pozisionais variáveis (tupla)
def soma_tudu(*numeros):
    return sum(numeros)

soma_tudu(1, 2, 3, 4)         # 10

# **kwargs — argumentus di nomi variáveis (dict)
def fixa_perfil(**dados):
    for xavi, valor in dados.items():
        print(f"{xavi}: {valor}")

fixa_perfil(nomi="Ana", idadi=22, ilha="Sal")
```

### Rekursun

```python
def fatorial(n):
    if n == 0:
        return 1               # kazu bazi
    return n * fatorial(n - 1)

fatorial(5)                    # 120
```

---

## 12. Lambda, Map e Filter

### Lambda

```python
# lambda argumentus: expresun
dobru = lambda x: x * 2
dobru(5)                       # 10

soma = lambda a, b: a + b
soma(3, 4)                     # 7
```

### map()

```python
numeros = [1, 2, 3, 4, 5]

# Aplika funsan a kada elementu
kuadradus = list(map(lambda x: x**2, numeros))
# [1, 4, 9, 16, 25]

# Ku funsan normal
nomis = ["maria", "djon", "ana"]
maiuskula = list(map(str.upper, nomis))
# ["MARIA", "DJON", "ANA"]
```

### filter()

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtra elementus ki satisfaz kondisun
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4, 6, 8, 10]

# Filtra di lista di disionárius
estudantis = [
    {"nomi": "Maria", "nota": 16},
    {"nomi": "Djon", "nota": 11},
    {"nomi": "Ana", "nota": 18},
]
aprovadus = list(filter(lambda e: e["nota"] >= 14, estudantis))
```

> **Dika:** `map()` e `filter()` retorna objetus lazy — uza `list()` pa vê resultadus.

---

## 13. Funsoens Inkorporadus Úteis

| Funsun | Uson | Ezemplu |
|--------|------|---------|
| `enumerate()` | Loop ku índisi | `for i, x in enumerate(lista)` |
| `zip()` | Itera paralelu | `for n, s in zip(nomis, notas)` |
| `sorted()` | Lista ordenadu (novu) | `sorted(lista, reverse=True)` |
| `any()` | Algun True? | `any(n > 10 for n in nums)` |
| `all()` | Tudu True? | `all(n > 0 for n in nums)` |
| `isinstance()` | Verifica tipu | `isinstance(x, int)` |
| `len()` | Tamañu | `len("Maria")` → `5` |
| `sum()` | Soma | `sum([1, 2, 3])` → `6` |
| `min()` / `max()` | Mínimu / Máximu | `max([4, 7, 2])` → `7` |
| `abs()` | Valor absolutu | `abs(-5)` → `5` |
| `round()` | Arredonda | `round(3.14159, 2)` → `3.14` |

### enumerate() — Substitui range(len(...))

```python
ilhas = ["Santiago", "Fogo", "Sal"]

# Ka fazi es:
for i in range(len(ilhas)):
    print(f"{i}: {ilhas[i]}")

# Fazi es:
for i, ilha in enumerate(ilhas):
    print(f"{i}: {ilha}")
```

### zip() — Itera Paralelu

```python
nomis = ["Maria", "Djon", "Ana"]
notas = [18, 15, 17]

for nomi, nota in zip(nomis, notas):
    print(f"{nomi}: {nota}")
# Maria: 18
# Djon: 15
# Ana: 17
```

---

## 14. Jeneradorus

### Generator Expression

```python
# Kumo list comprehension, ma ku () — lazy, poupa memória
kuadradus = (x**2 for x in range(1000000))  # ka aloka tudu na memória
next(kuadradus)    # 0
next(kuadradus)    # 1
```

### Generator Function ku yield

```python
def kontador_infinitu(inicio=0):
    n = inicio
    while True:
        yield n           # "pausa" e retorna valor
        n += 1

gen = kontador_infinitu(1)
next(gen)    # 1
next(gen)    # 2
next(gen)    # 3
```

> **Kuandu uza?** Kuandu bo tene dadus GRANDI ki ka kabe na memória, ou kuandu bo presis procesá un elementu di kada ves.

---

## 15. Módulus e Pakotis

### Import

```python
# Import módulu interu
import math
math.sqrt(16)                  # 4.0

# Import funsan spesífiku
from math import sqrt, pi
sqrt(25)                       # 5.0

# Import ku alias
import datetime as dt
gosi = dt.datetime.now()
```

### Stdlib Úteis

| Módulu | Uson | Ezemplu |
|--------|------|---------|
| `math` | Matemátika | `math.sqrt(16)`, `math.pi` |
| `random` | Alatóriu | `random.randint(1, 10)`, `random.choice(lista)` |
| `os` | Sistema operasional | `os.getcwd()`, `os.path.exists(f)` |
| `json` | JSON | `json.dumps(dict)`, `json.loads(str)` |
| `csv` | Ficheru CSV | `csv.reader(f)`, `csv.writer(f)` |
| `datetime` | Data e ora | `datetime.now()`, `timedelta(days=1)` |
| `re` | Regex | `re.search(r"\d+", textu)` |

### Pakoti Personalizadu

```
nha_pakoti/
    __init__.py         # fazi diretóriu virá pakoti
    matematika.py       # def soma(a, b): return a + b
    utilidades.py       # def saudason(nomi): ...
```

```python
from nha_pakoti.matematika import soma
from nha_pakoti.utilidades import saudason
```

---

## 16. Ambiente Virtual e pip

### Workflow Kompletu

```bash
# 1. Kria ambiente virtual
python -m venv .venv

# 2. Ativa
source .venv/bin/activate       # macOS / Linux
.venv\Scripts\activate          # Windows (cmd)
.venv\Scripts\Activate.ps1     # Windows (PowerShell)

# 3. Verifica — prompt mostra (.venv)
which python                    # deve aponta pa .venv/

# 4. Instala pakotis
pip install requests

# 5. Salva dependensias
pip freeze > requirements.txt

# 6. Desativa
deactivate
```

### Reproduzi na Otru Makina

```bash
# Na makina novu:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **IMPORTANTE:** SENPRI ativa `.venv` antis di `pip install`. Si bo instala sem venv, pakoti vai pa sistema global e pode kria konfliktu!

---

## 17. Operasoens ku Ficheru

### Lé Ficheru

```python
# Lé tudu
with open("dados.txt", "r") as f:
    konteúdu = f.read()

# Lé linha por linha
with open("dados.txt", "r") as f:
    for linha in f:
        print(linha.strip())
```

### Skrevi Ficheru

```python
# Skrevi (KUIDADU — apaga konteúdu existenti!)
with open("saida.txt", "w") as f:
    f.write("Primeira linha\n")

# Junta na final (preserva konteúdu)
with open("saida.txt", "a") as f:
    f.write("Linha novu\n")
```

### Modus di Ficheru

| Modu | Ason | Konteúdu Existenti |
|------|------|--------------------|
| `"r"` | Lé | Preserva (default) |
| `"w"` | Skrevi | **APAGA tudu!** |
| `"a"` | Junta | Preserva |
| `"r+"` | Lé + skrevi | Preserva |
| `"w+"` | Skrevi + lé | **APAGA tudu!** |
| `"rb"` / `"wb"` | Binário | Pa imajen, PDF, etc. |

### Kaminhu di Ficheru

```python
import os

os.path.join("pasta", "ficheru.txt")   # kaminhu korretu pa kel OS
os.path.exists("ficheru.txt")          # True / False
os.path.isfile("ficheru.txt")          # True si é ficheru
os.path.isdir("pasta")                 # True si é pasta
os.listdir(".")                         # lista konteúdu di pasta
```

> **REGRA:** SENPRI uza `with open(...)` — e fecha ficheru automátiku, mesmu si tene erru!

---

## 18. Tratamentu di Erru

### try / except / else / finally

```python
try:
    numeru = int(input("Mete un numeru: "))
    resultadu = 100 / numeru
except ValueError:
    print("Exi ka é un numeru válidu!")
except ZeroDivisionError:
    print("Ka pode dividi pa zeru!")
except Exception as e:
    print(f"Erru: {e}")          # catch-all (SENPRI últimu)
else:
    print(f"Resultadu: {resultadu}")  # só roda si ka teve erru
finally:
    print("Fin di operasun")          # SENPRI roda
```

### Exsesoens Komun

| Exsesun | Kuandu Acontesi |
|---------|-----------------|
| `SyntaxError` | Kódiku mal skrevedu |
| `NameError` | Variável ka existe |
| `TypeError` | Operasun ku tipu eradu (`"5" + 5`) |
| `ValueError` | Valor inválidu (`int("abc")`) |
| `IndexError` | Índisi fora di ranja |
| `KeyError` | Xavi ka existe na dict |
| `FileNotFoundError` | Ficheru ka existe |
| `ZeroDivisionError` | Divizun pa zeru |
| `AttributeError` | Métudu/atributu ka existe |

### raise — Lansa Exsesun

```python
def saka_dineru(balansa, montanti):
    if montanti > balansa:
        raise ValueError(f"Saldo insufisienti: {balansa} ECV")
    return balansa - montanti
```

### Exsesun Personalizadu

```python
class SaldoInsufisentiError(Exception):
    def __init__(self, balansa, montanti):
        self.balansa = balansa
        self.montanti = montanti
        super().__init__(
            f"Ka pode saka {montanti} ECV — saldo: {balansa} ECV"
        )

# Uzu:
raise SaldoInsufisentiError(500, 1000)
```

### Lé Traceback (Erru)

```
Traceback (most recent call last):
  File "programa.py", line 5, in <module>     ← UNDI acontesi
    resultadu = 100 / 0                        ← LINÑA ku erru
ZeroDivisionError: division by zero            ← O KI acontesi
```

> **Dika:** Lé traceback di **baxu pa sima** — últimu linha é o erru, linhas di sima mostra kaminhu.

---

## 19. Annotasoens di Tipu

### Báziku

```python
# Variáveis
nomi: str = "Maria"
idadi: int = 25
nota: float = 17.5
ativu: bool = True
```

### Funsoens

```python
def saudason(nomi: str) -> str:
    return f"Ola, {nomi}!"

def soma(a: int, b: int) -> int:
    return a + b

def busca_estudanti(id: int) -> dict | None:    # Python 3.10+
    """Retorna estudanti ou None si ka atxa."""
    ...
```

### Koleson

```python
def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

def kontador(textu: str) -> dict[str, int]:
    ...
```

> **IMPORTANTE:** Type hints é pa **umanus e feramentas** (IDE, mypy) — Python ka verifica na runtime!

---

## 20. Testu ku pytest

### Instala

```bash
pip install pytest
```

### Skrevi Testis

```python
# test_matematika.py
def soma(a, b):
    return a + b

def test_soma_pozitivu():
    assert soma(2, 3) == 5

def test_soma_negativu():
    assert soma(-1, -1) == -2

def test_soma_zeru():
    assert soma(0, 0) == 0
```

### Roda Testis

```bash
pytest                      # roda tudu testis
pytest test_matematika.py   # ficheru spesífiku
pytest -v                   # verbose — mostra kada testu
```

> **Filosofia:** Skrevi testu PRIMERU, implementa DIPÓS, verifica SENPRI.

---

## 21. Klasis e Objetis (OOP)

### Kria Klasi

```python
class KontaBankáriu:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def deposita(self, montanti: float):
        self.saldo += montanti
        print(f"Depositadu {montanti} ECV. Saldo: {self.saldo} ECV")

    def saka(self, montanti: float):
        if montanti > self.saldo:
            print("Saldo insufisienti!")
        else:
            self.saldo -= montanti
            print(f"Sakadu {montanti} ECV. Saldo: {self.saldo} ECV")

# Uzu:
konta = KontaBankáriu("Maria", 5000)
konta.deposita(1500)      # Saldo: 6500 ECV
konta.saka(2000)          # Saldo: 4500 ECV
```

### Anatomia di Klasi

```python
class NomiKlasi:
    def __init__(self, param1, param2):    # Constructor
        self.atributu1 = param1            # Variável di instansia
        self.atributu2 = param2

    def métudu(self):                      # Métudu di instansia
        return self.atributu1
```

> **LEMBRA:** `self` é referensia pa instansia atual — SENPRI primeru parámetru di métudus.

---

## 22. Eransa

### Eransa Simples

```python
class Animal:
    def __init__(self, nomi: str):
        self.nomi = nomi

    def fala(self) -> str:
        return "..."

class Katxor(Animal):
    def __init__(self, nomi: str, rasa: str):
        super().__init__(nomi)          # txama constructor di pai
        self.rasa = rasa

    def fala(self) -> str:              # override
        return f"{self.nomi} ta fazi Woof!"

class Gatu(Animal):
    def fala(self) -> str:
        return f"{self.nomi} ta fazi Miau!"

rex = Katxor("Rex", "Labrador")
print(rex.fala())       # Rex ta fazi Woof!
print(rex.rasa)         # Labrador
```

### Eransa Múltiplu

```python
class Animal:
    def __init__(self, nomi):
        self.nomi = nomi

class Animali:
    def __init__(self, donu):
        self.donu = donu

class Katxor(Animal, Animali):
    def __init__(self, nomi, donu):
        Animal.__init__(self, nomi)      # txamada direta pa múltiplu
        Animali.__init__(self, donu)

rex = Katxor("Rex", "Djon")
```

> **Dika:** Uza `super()` pa eransa simples; `Klasi.__init__(self, ...)` pa eransa múltiplu.

---

## 23. Polimorfismu e Abstrasun

### Polimorfismu

```python
def mostra_area(forma):
    """Funson polimórfiku — aseta kualker forma ku .area()."""
    print(f"Área: {forma.area()}")

class Retangulu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura

class Sírkulu:
    def __init__(self, raiu):
        self.raiu = raiu
    def area(self):
        return 3.14159 * self.raiu ** 2

mostra_area(Retangulu(4, 5))    # Área: 20
mostra_area(Sírkulu(3))         # Área: 28.27...
```

### Klasi Abstratu (ABC)

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        """Tudu forma DEVE implementa es métudu."""
        pass

    def deskribi(self) -> str:           # métudu normal (erdadu)
        return f"Forma ku área {self.area()}"

class Retangulu(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura

# Forma()         # TypeError! Ka pode instansia klasi abstratu
r = Retangulu(4, 5)
print(r.deskribi())  # Forma ku área 20
```

---

## 24. Enkapsolamentu e @property

### Nível di Asesu

| Prefixu | Tipu | Asesu |
|---------|------|-------|
| `self.nomi` | Públiku | Di kualker lugar |
| `self._nomi` | Protejidu | Klasi + filhos (konvensun) |
| `self.__nomi` | Privadu | Só klasi (name mangling) |

### @property — Getter/Setter Modernu

```python
class Estudanti:
    def __init__(self, nomi: str, nota: float):
        self._nomi = nomi
        self._nota = nota

    @property
    def nota(self) -> float:
        """Getter — asesa kumo atributu, ka kumo métudu."""
        return self._nota

    @nota.setter
    def nota(self, valor: float):
        """Setter — valida antis di atribui."""
        if 0 <= valor <= 20:
            self._nota = valor
        else:
            raise ValueError("Nota deve sé entre 0 e 20")

    @property
    def nomi(self) -> str:
        return self._nomi

# Uzu — paresi atributu, ma tene validasun:
maria = Estudanti("Maria", 16)
print(maria.nota)        # 16 (getter)
maria.nota = 18          # (setter — valida)
# maria.nota = 25        # ValueError!
```

---

## 25. Métodus Mádjiku e Sobrekarga

### Métodus Mádjiku Prinsipal

| Métudu | Kuandu Roda | Ezemplu |
|--------|-------------|---------|
| `__init__` | Kria objetu | `obj = Klasi(...)` |
| `__str__` | `print(obj)`, `str(obj)` | Saída pa umanu |
| `__repr__` | `repr(obj)`, terminal | Saída pa developer |
| `__len__` | `len(obj)` | Tamañu |
| `__getitem__` | `obj[i]` | Indexasun |
| `__contains__` | `x in obj` | Membership |
| `__eq__` | `obj1 == obj2` | Igualdadi |
| `__lt__` | `obj1 < obj2` | Menor ki |
| `__add__` | `obj1 + obj2` | Adisun |
| `__sub__` | `obj1 - obj2` | Subtrasun |
| `__mul__` | `obj1 * obj2` | Multiplikasun |

### Sobrekarga di Operador — Ezemplu Kompletu

```python
class Vetor:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, otru):
        return Vetor(self.x + otru.x, self.y + otru.y)

    def __sub__(self, otru):
        return Vetor(self.x - otru.x, self.y - otru.y)

    def __mul__(self, eskalar):
        return Vetor(self.x * eskalar, self.y * eskalar)

    def __eq__(self, otru):
        return self.x == otru.x and self.y == otru.y

    def __str__(self):
        return f"Vetor({self.x}, {self.y})"

    def __repr__(self):
        return f"Vetor(x={self.x}, y={self.y})"

v1 = Vetor(2, 3)
v2 = Vetor(4, 5)
print(v1 + v2)     # Vetor(6, 8)
print(v1 - v2)     # Vetor(-2, -2)
print(v1 * 3)      # Vetor(6, 9)
print(v1 == v2)    # False
```

---

## 26. Dataclasses

### Antis (Manual)

```python
class Estudanti:
    def __init__(self, nomi: str, idadi: int, nota: float):
        self.nomi = nomi
        self.idadi = idadi
        self.nota = nota

    def __repr__(self):
        return f"Estudanti(nomi={self.nomi!r}, idadi={self.idadi}, nota={self.nota})"

    def __eq__(self, otru):
        return (self.nomi == otru.nomi and
                self.idadi == otru.idadi and
                self.nota == otru.nota)
```

### Dipós (ku @dataclass)

```python
from dataclasses import dataclass

@dataclass
class Estudanti:
    nomi: str
    idadi: int
    nota: float

# __init__, __repr__, __eq__ skrevedu automátiku!
maria = Estudanti("Maria", 22, 17.5)
print(maria)         # Estudanti(nomi='Maria', idadi=22, nota=17.5)
```

### Opsons Úteis

```python
@dataclass(frozen=True)         # imutável (kumo tupla)
class Puntu:
    x: float
    y: float

@dataclass(order=True)          # jera <, >, <=, >=
class Nota:
    valor: float
    estudanti: str
```

---

## 27. Komprehensions (Rezumu)

| Tipu | Sintaxi | Resultadu |
|------|---------|-----------|
| List | `[x**2 for x in range(5)]` | `[0, 1, 4, 9, 16]` |
| Dict | `{x: x**2 for x in range(5)}` | `{0:0, 1:1, 2:4, ...}` |
| Set | `{x % 3 for x in range(10)}` | `{0, 1, 2}` |
| Generator | `(x**2 for x in range(5))` | objeto lazy |

### Ku Kondisun

```python
# Filtra pares
[x for x in range(10) if x % 2 == 0]

# Transforma + filtra
[nomi.upper() for nomi in nomis if len(nomi) > 3]

# Dict filtrado
{k: v for k, v in estudantis.items() if v >= 14}
```

---

## 28. Errus Komun e Kumo Rezolvé

| Erru | Kauza | Soluson |
|------|-------|---------|
| `IndentationError` | Indentasun eradu | Uza 4 espasus (ka tab) |
| `NameError: name 'x' is not defined` | Variável ka existe | Verifica nomi e eskopiu |
| `TypeError: can only concatenate str to str` | Mistura tipu | Uza `str()` ou f-string |
| `TypeError: 'NoneType' object is not subscriptable` | Funsun ka retorna nada | Verifica `return` |
| `IndexError: list index out of range` | Índisi fora di lista | Verifica `len()` antis |
| `KeyError: 'nomi'` | Xavi ka existe na dict | Uza `.get(key, default)` |
| `ModuleNotFoundError` | Pakoti ka instaladu | `pip install pakoti` (dentu di .venv) |
| `FileNotFoundError` | Ficheru ka existe | Verifica kaminhu ku `os.path.exists()` |
| `def f(x, data=[])` | Default mutável partilhadu | Uza `data=None`, dps `data = data or []` |
| `except:` (sem tipu) | Kapta tudu inkluindu Ctrl+C | SENPRI kapta exsesun spesífiku |

---

## Tabela Rápidu: Estruturas di Dadus

| Feature | List `[]` | Tuple `()` | Dict `{}` | Set `{}` |
|---------|-----------|------------|-----------|----------|
| Ordenadu | Sim | Sim | Sim (3.7+) | Nun |
| Mutável | Sim | Nun | Valoris sim | Sim |
| Duplikadus | Permiti | Permiti | Xavis úniku | Ka permiti |
| Indexasun | Pozisun | Pozisun | Xavi | Nun |
| Comprehension | Sim | Nun | Sim | Sim |
| Slicing | Sim | Sim | Nun | Nun |
| Uzu típiku | Koleson ki muda | Dadus fixu | Mapamentu | Valores úniku |

---

## Tabela Rápidu: 4 Pilaris di OOP

| Pilar | Mekanismu | Pal ki é |
|-------|-----------|----------|
| **Klasis/Objetis** | `class`, `__init__`, `self` | Kria blueprints pa objetis |
| **Eransa** | `super()`, klasi filhu | Reusa kódiku di klasi pai |
| **Polimorfismu** | Override, ABC | Mesmu métudu, komportamentu diferenti |
| **Enkapsolamentu** | `_`, `__`, @property | Proteje dadus, kontrola asesu |

---

## Versioning & Manutensun

* **Doc version:** 1.0.0
* **Validadu na:** 2026-04-21
* **Python version:** 3.13+
* **Risku di drift:** Mudansas na PEP 750 (t-strings), novu sintaxi na 3.14+
* **Revalidasun:**
  - [ ] Verifica changelog di Python pa novu versun
  - [ ] Roda ezemplus di kódiku
  - [ ] Verifica sintaxi di flag e métudu
