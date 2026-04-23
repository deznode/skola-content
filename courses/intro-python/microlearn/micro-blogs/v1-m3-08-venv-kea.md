# Virtual Environments — Kada Projetu ku Si Mundu
Language: Kriolu (KEA)
Audience: Beginner
Format: micro_blog
Topic: Python

Imagina bo tene 2 projetus. Un presiza `requests 2.28`, otru presiza `requests 2.31`. Sin venv, és ta kolidi! Virtual environment ta kria un "mundu" separadu pa kada projetu.

```bash
# 1. Kria ambiente virtual
python -m venv .venv

# 2. Ativa
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate          # Windows

# 3. Instala pakotis (só dentru di .venv!)
pip install requests

# 4. Salva dependénsias
pip freeze > requirements.txt

# 5. Desativa
deactivate
```

```bash
# Otru programador ta reproduzi bo ambiente:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Pronto! Mesmu pakotis, mesmu versoens!
```

**Workflow senpri:**
1. `python -m venv .venv` — kria
2. `source .venv/bin/activate` — ativa
3. `pip install ...` — instala
4. `pip freeze > requirements.txt` — salva
5. `deactivate` — sai

**Takeaway**: Senpri kria `.venv` antes di instala kualker pakoti. `requirements.txt` é reseta di bo projetu!

**Prósimu**: Operasoens ku ficheru — lé e skrévi
