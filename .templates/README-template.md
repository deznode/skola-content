# {{TOPIC_TITLE}}

{{BRIEF_DESCRIPTION}}

## Kuzé ki Bu Ta Prendi

{{LEARNING_OBJECTIVES}}

## Pre-rekizitus

- Java 21+ instaladu (JDK)
- Docker pa kori bazi di dadus lokal
- Maven pa kompila i kori ezénplus

## Setup Rápidu

### 1. Kumesa bazi di dadus

```bash
cd code/docker
docker compose up -d
```

### 2. Kompila projetu

```bash
cd code/start   # pa prinsipianti (ku TODO)
# ou
cd code/final   # pa solusons kompletu
mvn compile
```

### 3. Kori un ezénplu

```bash
mvn exec:java -Dexec.mainClass="{{MAIN_CLASS_EXAMPLE}}"
```

## Estrutura di Projetu

```
{{TOPIC_SLUG}}/
├── README.md                    # Es fixeru
├── {{LANG}}/                    # Konteúdu skritu ({{LANG_NAME}})
│   ├── tutorial.mdx             # Tutorial pasu-a-pasu
│   ├── cheatsheet.md            # Referénsia rápidu
│   ├── infographics/            # Imajen edukatival
│   └── slides/                  # Prezentason Slidev
└── code/
    ├── docker/                  # Anbiente lokal (Docker Compose)
    │   ├── docker-compose.yml   # Konfigurason di servisu
    │   └── init/                # Script di inizializason
    ├── start/                   # Skafólding ku TODO (pa prinsipianti)
    │   ├── pom.xml              # Maven konfigurason
    │   └── src/                 # Kódigu ku TODO pa implementa
    ├── final/                   # Solusons kompletu
    │   ├── pom.xml
    │   └── src/                 # Kódigu implementadu
    └── projects/                # Projetu prátiku (dezafiu)
        └── {{PROJECT_NAME}}/    # {{PROJECT_DESCRIPTION}}
```

## Manera di Uza

### Pa Prinsipianti (Rekomendadu)

1. **Kumesa ku `code/start/`** - Skafólding ku TODO
2. **Segui tutorial** - Abri `{{LANG}}/tutorial.mdx` i segui pasu-a-pasu
3. **Implementa kada ezénplu** - Troka komentáriu TODO ku bu kódigu
4. **Kompara ku solusons** - Xeka `code/final/` si bu fikâ prisu

### Pa Referénsia Rápidu

- **Cheatsheet**: `{{LANG}}/cheatsheet.md` - Sintaxi i padron komun
- **Slides**: `{{LANG}}/slides/` - Kori `pnpm dev` pa prezentason

## Ezénplus

{{EXAMPLES_TABLE}}

### Kori ezénplu individualmenti

```bash
cd code/final  # ou code/start
mvn compile exec:java -Dexec.mainClass="{{EXAMPLE_CLASS}}"
```

## Dezafiu: {{CHALLENGE_NAME}}

{{CHALLENGE_DESCRIPTION}}

```bash
cd code/projects/{{CHALLENGE_SLUG}}
mvn compile exec:java -Dexec.mainClass="{{CHALLENGE_MAIN_CLASS}}"
```

## Prezentason Slides

```bash
cd {{LANG}}/slides
pnpm install
pnpm dev          # Servidor lokal na http://localhost:3030
pnpm build        # Kompila pa HTML státiku
pnpm export-pdf   # Esporta pa PDF
```

## Rekursus Adisional

- **Tutorial kompletu**: [`{{LANG}}/tutorial.mdx`]({{LANG}}/tutorial.mdx)
- **Cheatsheet**: [`{{LANG}}/cheatsheet.md`]({{LANG}}/cheatsheet.md)
- **Prezentason**: [`{{LANG}}/slides/`]({{LANG}}/slides/)
- **Infografikus**: [`{{LANG}}/infographics/`]({{LANG}}/infographics/)

## Problema Komun

### Docker ka ta inisia

```bash
# Verifica si Docker ta kori
docker info

# Si ka ta, kumesa Docker Desktop primeru
```

### Konexon ku bazi falha

```bash
# Verifica si kontener ta kori
docker ps

# Verifica logs
cd code/docker
docker compose logs postgres
```

### Maven ka ta enkontra klasi

```bash
# Kompila projetu primeru
mvn compile

# Verifica si bu sta na pasta serti (code/start ou code/final)
pwd
```

### Porta 5432 ja ta uzadu

```bash
# Para servisu PostgreSQL lokal si nesesáriu
# Linux/Mac:
sudo lsof -i :5432

# Ou muda porta na docker-compose.yml
```

---

*Skola.dev - Nôs ta kriâ djunta!*
