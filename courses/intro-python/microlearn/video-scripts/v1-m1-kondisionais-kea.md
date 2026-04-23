# if/elif/else — Fazi Bo Programa Pensa
Language: Kriolu (KEA)
Audience: Beginner
Format: short_video
Topic: Python
Duration/Limit: ~75s

## 1) Hook
"Si sta txobê, nha ta léba garda-txuva." Bo programa tanbé presiza pensa e disidi — ku if/elif/else!

## 2) Core Concept
`if` ta verifica un kondisun. Si é `True`, izekuta bloku. Si nau, `elif` ta txeka más kondison. `else` é planu di reserva — roda si ninhun kondisun da `True`.

## 3) Show It
```python
nota = 85

if nota >= 90:
    print("Exselenti! 🌟")
elif nota >= 70:
    print("Bon trabalhu! 👍")
elif nota >= 50:
    print("Pasou, ma studu más!")
else:
    print("Ka pasou. Tenta otru bes!")

# Output: Bon trabalhu! 👍
```

```python
# Ezemplu prátiku: verifikasun di temperatura
temperatura = 35

if temperatura > 30:
    print("Sta kenti! Bai praia di Kebra Kanela!")
elif temperatura > 20:
    print("Temperatura agradável.")
else:
    print("Sta friu pa Kabu Verdi!")

# Output: Sta kenti! Bai praia di Kebra Kanela!
```

## 4) Takeaway
`if` = pergunta, `elif` = más perguntas, `else` = "si ninhun da sertu". Senpri termina ku `:` e usa 4 espasus di indentasun!

## 5) CTA
Tenta agora: kria un programa ki resebe idadi di un pesoa e diz si é kriansa, adolesenti, ó adultu!

---
**B-roll notes**: Diagrama di fluxu animadu → kódiku na terminal → mustra kada kaminhu ku nota diferenti → output muda konfórmi kondisun
**End card**: "Prósimu: Loops — for e while"
