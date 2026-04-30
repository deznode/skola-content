---
theme: default
title: Fixerus na Python
---

# Fixerus na Python

Smoke slide deck for spec 021 publish assets verification.

---

## Lê un fixeru

```python
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

---

## Skrebe na un fixeru

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Olá!\n")
```
