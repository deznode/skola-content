# Operasoens ku Ficheru — Lé e Skrévi ku `with`
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Python ta permite lé e skrévi fichérus ku faslidadi. Regra di oru: **senpri uza `with`** — el ta fecha ficheru automátikamenti!

```python
# SKRÉVI ficheru
with open("nomis.txt", "w") as f:
    f.write("Maria\n")
    f.write("Djon\n")
    f.write("Ana\n")
# Ficheru fechadu automátikamenti!

# LÉ ficheru
with open("nomis.txt", "r") as f:
    konteúdu = f.read()
    print(konteúdu)
# Maria
# Djon
# Ana
```

```python
# ADISIONA (ka ta apaga ki já esisti)
with open("nomis.txt", "a") as f:
    f.write("Amilka\n")

# LÉ linja a linja
with open("nomis.txt", "r") as f:
    for linja in f:
        print(f"-> {linja.strip()}")
# -> Maria
# -> Djon
# -> Ana
# -> Amilka
```

**Modus di ficheru:**
- `"r"` — lé (default)
- `"w"` — skrévi (apaga tudu!)
- `"a"` — adisiona na final
- `"r+"` — lé + skrévi

**Takeaway**: Senpri uza `with open()` — nunka skexi fecha ficheru. `"w"` apaga tudu, `"a"` adisiona!

**Prósimu**: Tratamentu di erru — try/except
