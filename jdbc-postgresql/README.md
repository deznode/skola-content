# Java JDBC ku PostgreSQL

Tutorial kompletu pa prendi konekta aplikason Java ku bazi di dadus PostgreSQL uzandu JDBC. Aborda konexon, operason CRUD, i prátikas di seguransa kontra SQL injection.

## Kuzé ki Bu Ta Prendi

- Konekta bu aplikason Java ku un bazi di dadus PostgreSQL
- Faze tudu operason CRUD (Create, Read, Update, Delete)
- Skrebi query seguru ki ta privini ataki di SQL injection
- Intendi objetu prinsipal di JDBC: Connection, Statement, ResultSet

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

Isu ta kumesa PostgreSQL 16 na porta 5432 ku:
- **Database**: `skola_dev`
- **User**: `skola`
- **Password**: `skola_dev`

### 2. Kompila projetu

```bash
cd code/start   # pa prinsipianti (ku TODO)
# ou
cd code/final   # pa solusons kompletu
mvn compile
```

### 3. Kori un ezénplu

```bash
mvn exec:java -Dexec.mainClass="com.example.examples.E01_Connection"
```

## Estrutura di Projetu

```
jdbc-postgresql/
├── README.md                    # Es fixeru
├── kea/                         # Konteúdu skritu (Kriolu)
│   ├── tutorial.mdx             # Tutorial pasu-a-pasu
│   ├── cheatsheet.md            # Referénsia rápidu
│   ├── infographics/            # Imajen edukatival
│   │   ├── 01-jdbc-architecture.jpg
│   │   ├── 02-connection-url.png
│   │   ├── 03-core-objects.png
│   │   └── 04-preparedstatement-safety.jpg
│   └── slides/                  # Prezentason Slidev (15 slides)
└── code/
    ├── docker/                  # Anbiente lokal (Docker Compose)
    │   ├── docker-compose.yml   # PostgreSQL 16
    │   └── init/
    │       └── 01-schema.sql    # Tabela users + contacts
    ├── start/                   # Skafólding ku TODO (pa prinsipianti)
    │   ├── pom.xml              # Maven + PostgreSQL driver
    │   └── src/main/java/com/example/
    │       ├── config/
    │       │   └── DatabaseConfig.java
    │       └── examples/
    │           ├── E01_Connection.java
    │           ├── E02_InsertUser.java
    │           ├── E03_SelectUsers.java
    │           ├── E04_UpdateUser.java
    │           └── E05_DeleteUser.java
    ├── final/                   # Solusons kompletu
    │   └── (mésmu estrutura di start/)
    └── projects/
        └── contact-agenda/      # Dezafiu: Ajenda di kontatu CLI
```

## Manera di Uza

### Pa Prinsipianti (Rekomendadu)

1. **Kumesa ku `code/start/`** - Skafólding ku TODO
2. **Segui tutorial** - Abri `kea/tutorial.mdx` i segui pasu-a-pasu
3. **Implementa kada ezénplu** - Troka komentáriu TODO ku bu kódigu
4. **Kompara ku solusons** - Xeka `code/final/` si bu fikâ prisu

### Pa Referénsia Rápidu

- **Cheatsheet**: `kea/cheatsheet.md` - Sintaxi i padron komun
- **Slides**: `kea/slides/` - Kori `pnpm dev` pa prezentason

## Ezénplus

| Fixeru | Konseitu | Deskrison |
|--------|----------|-----------|
| `E01_Connection.java` | Konexon | Konekta ku bazi uzandu `DriverManager` |
| `E02_InsertUser.java` | INSERT | Djunta uzuáriu novu ku `PreparedStatement` |
| `E03_SelectUsers.java` | SELECT | Le dadus ku `ResultSet` |
| `E04_UpdateUser.java` | UPDATE | Atualiza registu esistenti |
| `E05_DeleteUser.java` | DELETE | Elimina registu |

### Kori ezénplu individualmenti

```bash
cd code/final  # ou code/start

# Konexon
mvn exec:java -Dexec.mainClass="com.example.examples.E01_Connection"

# INSERT
mvn exec:java -Dexec.mainClass="com.example.examples.E02_InsertUser"

# SELECT
mvn exec:java -Dexec.mainClass="com.example.examples.E03_SelectUsers"

# UPDATE
mvn exec:java -Dexec.mainClass="com.example.examples.E04_UpdateUser"

# DELETE
mvn exec:java -Dexec.mainClass="com.example.examples.E05_DeleteUser"
```

## Dezafiu: Ajenda di Kontatu

Un projetu prátiku pa aplika tudu ki bu prendi: kria un aplikason CLI pa jeri kontatus.

**Funsionalidadis:**
- Djunta kontatu novu (nomi, telefoni, email)
- Lista tudu kontatus
- Buska kontatu pa nomi
- Atualiza kontatu
- Elimina kontatu

```bash
cd code/projects/contact-agenda
mvn compile exec:java -Dexec.mainClass="com.example.ContactAgendaApp"
```

## Prezentason Slides

Un prezentason di 15 slides ki ta kobri tudu konseitu prinsipal:

```bash
cd kea/slides
pnpm install
pnpm dev          # Servidor lokal na http://localhost:3030
pnpm build        # Kompila pa HTML státiku
pnpm export-pdf   # Esporta pa PDF
```

**Atalhos di tekladu:**
- `P` - Modu presentador ku notas
- `O` - Vista geral di slides
- `F` - Fullscreen

## Rekursus Adisional

- **Tutorial kompletu**: [`kea/tutorial.mdx`](kea/tutorial.mdx)
- **Cheatsheet**: [`kea/cheatsheet.md`](kea/cheatsheet.md)
- **Prezentason**: [`kea/slides/`](kea/slides/)
- **Infografikus**: [`kea/infographics/`](kea/infographics/)

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

# Verifica si bazi ta pronto
docker exec skola_postgres pg_isready -U skola -d skola_dev
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

# Ou muda porta na docker-compose.yml pa 5433:5432
```

### Tabela ka esisti

```bash
# Rekria bazi ku init scripts
cd code/docker
docker compose down -v
docker compose up -d
```

---

*Skola.dev - Nôs ta kriâ djunta!*
