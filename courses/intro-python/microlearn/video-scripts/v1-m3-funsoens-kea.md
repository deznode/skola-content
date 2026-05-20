# Funsoens — Skrévi Un Bes, Uza Mil Bes
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
Bo sta kopia-kola mesmu kódiku 5 bes? Para! Funson ta permite bo skrévi un bes só e xama kuantu bes bo kre.

## 2) Core Concept
Funson é un bloku di kódiku ku nomi ki ta fazi un tarefa espesífiku. Bo ta defini ku `def`, pasa dadus via parámetrus, e resebe resultadu ku `return`.

## 3) Show It
```python
# Defini un funson
def saudason(nomi, ilha="Santiago"):
    return f"Oi {nomi} di {ilha}! Nu ta kria djuntu!"

# Xama funson
print(saudason("Maria"))
# Output: Oi Maria di Santiago! Nu ta kria djuntu!

print(saudason("Djon", "Fogo"))
# Output: Oi Djon di Fogo! Nu ta kria djuntu!
```

```python
# Funson ku *args (argumentus variáveis)
def soma_tudu(*numeros):
    return sum(numeros)

print(soma_tudu(10, 20, 30))
# Output: 60

print(soma_tudu(5, 15))
# Output: 20
```

## 4) Takeaway
`def` pa kria, parámetrus pa resebe dadus, `return` pa devolve resultadu. Funson = reutilizasun di kódiku!

## 5) CTA
Tenta gosi: kria un funson `kalkula_media()` ki resebe un lista di notis e retorna média!

---
**B-roll notes**: Animasun di "kaxa" ki ta resebe input e ta sai output → kódiku na terminal → mustra xama ku diferentes argumentus → mustra *args
**End card**: "Prósimu: Lambda, Map e Filter"
