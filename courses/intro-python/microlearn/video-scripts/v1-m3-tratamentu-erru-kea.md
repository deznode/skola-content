# try/except — Trata Erru Komu un Pro
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
Bo programa krasha e bo ka sabi pamodi? try/except ta pega erru ANTES ki és destrui bo programa!

## 2) Core Concept
`try` ta tenta izekuta kódiku. Si da erru, `except` ta pega e trata. `else` roda si tudu koré bon. `finally` roda SENPRI — perfetu pa limpa rekursus.

## 3) Show It
```python
# Sin tratamentu — programa KRASHA!
# resultado = 10 / 0  # ZeroDivisionError!

# Ku tratamentu — programa SOBREVIVE!
def dividi(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erru: ka podi dividi pa zero!")
        return None
    except TypeError:
        print("Erru: uza só númerus!")
        return None
    else:
        print(f"Resultadu: {resultado}")
        return resultado
    finally:
        print("Operasun terminadu.")

dividi(10, 3)
# Output:
# Resultadu: 3.3333333333333335
# Operasun terminadu.

dividi(10, 0)
# Output:
# Erru: ka podi dividi pa zero!
# Operasun terminadu.
```

## 4) Takeaway
`try` = tenta, `except` = si da erru, `else` = si tudu bon, `finally` = SENPRI roda. Senpri pega exseson espesífiku!

## 5) CTA
Tenta agora: skrévi un programa ki pidi un númeru a utilizador e trata ValueError si és skrévi textu!

---
**B-roll notes**: Animasun di "rede di seguránsa" dibaxu di trapezista → kódiku na terminal → programa ki krasha SIN try → programa ki sobrevive KU try
**End card**: "Prósimu: Type Hints — Anotasoens di Tipu"
