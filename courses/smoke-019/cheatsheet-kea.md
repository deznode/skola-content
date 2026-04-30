# Smoke Topic — Cheatsheet (Kriolu)

**Topic:** Smoke Topic for Spec 021 Publish Assets
**Language:** kea (Kabuverdianu)
**Generated:** 2026-04-30 (manual seed for spec 021 verification)

## Lê un fixeru di tekstu

```python
with open("data.txt", "r", encoding="utf-8") as f:
    contents = f.read()
print(contents)
```

- `with` — fexa fixeru automatikamenti
- `encoding="utf-8"` — pa lê karateris di Kriolu/Português
- `read()` — devolve tudu konteúdu di fixeru
- `readlines()` — devolve un lista, kada linha un elementu

## Skrebe na un fixeru

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Bom dia di Kabu Verde\n")
```

- `"w"` — sobrepoi (apaga konteúdu antigu)
- `"a"` — junta na fim (apend)
- Disémper junta `\n` na fim di kada linha

## Modu di abri fixeru

| Modu | Sentidu |
|------|---------|
| `r` | Lê (default) |
| `w` | Skrebe (sobrepoi) |
| `a` | Junta na fim |
| `r+` | Lê + skrebe |
