# Lé Errus di Python — Traceback Ka É Bichu!
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Traceback paresi asustadór, ma é bo milhor amigu pa koriji errus. Truque: **lé di baxu pa sima!**

```python
nomi = "Ana"
print(nomi + 10)
```

```
Traceback (most recent call last):
  File "programa.py", line 2, in <module>
    print(nomi + 10)
          ~~~~^~~~
TypeError: can only concatenate str (not "int") to str
```

**Kumo lé (di baxu pa sima):**

1. **Últimu linja** = tipu di erru + mensaji: `TypeError` — ka podi junta str ku int
2. **Linja ku `^`** = exatamenti undi erru sta (Python 3.11+)
3. **`line 2`** = ficheru e linja undi acontesé

**5 errus más komun:**
- `SyntaxError` — bo kódiku tene erru di eskrita
- `NameError` — variável ka esisti
- `TypeError` — tipus inkompatível
- `IndexError` — índisi fora di limiti
- `ZeroDivisionError` — dividi pa zero

**Takeaway**: Traceback é detetive, ka inimigu. Lé di baxu pa sima e koriji!

**Prósimu**: Variáveis e tipu dinámiku
