# Kual Estrutura di Dadus Bo Debe Uza?
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Python tene 4 estruturas di dadus báziku. Kada un tene si forsa. Desidi rápidu ku es guia:

```python
# LIST — kolesoens ordenadu ki muda
karrinhu = ["pun", "leiti", "banana"]
karrinhu.append("ovu")  # Bo podi adisiona!

# TUPLE — kolesoens ordenadu ki KA muda
kordenadas = (14.93, -23.51)  # Latitudi, Longitudi di Praia
# kordenadas[0] = 15.0  # TypeError! Ka podi muda!

# DICT — pares xavi:valor
estudanti = {"nomi": "Carla", "nota": 88}
print(estudanti["nomi"])  # Carla

# SET — elementus únikis (sin duplikadus)
ilhas_vizitadu = {"Sal", "Santiago", "Sal", "Fogo"}
print(ilhas_vizitadu)  # {'Sal', 'Santiago', 'Fogo'}
```

**Kumo skoji:**
- Bo presiza **orden + mudar**? → `list`
- Bo presiza **orden + ka muda**? → `tuple`
- Bo presiza **xavi → valor**? → `dict`
- Bo presiza **elementus únikis**? → `set`

| | Ordenadu | Mutável | Duplikadus | Sintaxi |
|---|---|---|---|---|
| list | Si | Si | Si | `[]` |
| tuple | Si | Nau | Si | `()` |
| dict | Si* | Si | Xavis: Nau | `{}` |
| set | Nau | Si | Nau | `{}` |

**Takeaway**: `list` pa más kazu. `tuple` pa dadus fixu. `dict` pa mapear. `set` pa únikis.

**Prósimu**: Kazus real ku estruturas di dadus
