---
theme: default
title: "Java JDBC ku PostgreSQL"
info: |
  ## Java JDBC ku PostgreSQL
  Gia Konpletu pa Prinsipianti - Skola.dev
language: kea
drawings:
  persist: false
transition: slide-left
mdc: true
css: unocss
---

# Java JDBC ku PostgreSQL

Gia Konpletu pa Prinsipianti

<div class="pt-12">
  <span class="text-xl font-bold text-skola-yellow">Di zeru pa CRUD konpletu na 20 minutu!</span>
</div>

<div class="abs-bl m-6 text-sm text-white opacity-90">
  Skola.dev - Nu ta studa, nu ta kria, nu ta partilha!
</div>

<!--
HOOK [00:00-00:25]
"Bu krê konekta bu aplikason Java ku un bazi di dadus ma bu ka sabe pa undi kumesa?"
-->

---

# Kuzé Nu Ta Kobri

<v-clicks>

- **1.** Konfigura driver JDBC
- **2.** Konekta ku PostgreSQL
- **3.** Tudu operason CRUD ku kódigu real
- **4.** Evita ataki di SQL injection

</v-clicks>

<div class="pt-8">
  <span class="text-sm text-skola-gray">Preparadu? Nu bai!</span>
</div>

<!--
AGENDA [00:25-00:50]
Lista aparese un pa un
-->

---

# Kuzé JDBC?

**JDBC = Java Database Connectivity**

<div class="grid grid-cols-2 gap-8 pt-4">
<div>

Pensa n-el komu **tradutor universal**:

- Bu skrebe Java
- JDBC konverte pa linguajen di bazi
- Bazi manda resposta
- JDBC torna konverte pa Java

</div>
<div>

**Pamodi aprende JDBC?**

- Fundason pa Spring Data, Hibernate
- Debug problema di bazi di dadus
- Kontrolu di nivel baxu kantu meste

</div>
</div>

<div class="pt-6">
  <span class="text-sm text-skola-gray">É komu prende karu manual antis di automátiku!</span>
</div>

<!--
KONTEXTU [00:50-01:40]
"JDBC signifika Java Database Connectivity. É fundason..."
-->

---

# Arkitetura JDBC

<img src="/images/01-jdbc-architecture.jpg" class="h-72 mx-auto rounded shadow-lg" alt="JDBC Architecture" />

<div class="pt-4 text-center">
  <code class="text-lg text-skola-teal">Aplikason Java → JDBC API → Driver → PostgreSQL</code>
</div>

<!--
Diagrama mostrandu kamadus
-->

---

# Pre-Rekizitus

<div class="grid grid-cols-2 gap-12 pt-8">
<div>

**Software Nesesáriu:**

- Java JDK 17+ (N ta uza 21)
- PostgreSQL ta kori
- IDE (VS Code o IntelliJ)

</div>
<div>

**Verifikason:**

```bash
java -version
# java version "21.0.1"

pg_isready
# localhost:5432 - accepting connections
```

</div>
</div>

<div class="pt-8 text-sm text-skola-gray">
  Gias di setup na deskrison di vídeo!
</div>

<!--
PRE-REKIZITUS [01:40-02:10]
Flash rápidu, ka gasta mundu ténpu
-->

---

# Djunta Driver JDBC

**Maven (pom.xml):**

```xml {all|3-5}
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.2</version>
</dependency>
```

<div class="pt-4">

**Sen Maven?** Baxa JAR di jdbc.postgresql.org

</div>

<div class="pt-6 text-sm text-skola-gray">
  Link na deskrison di vídeo!
</div>

<!--
SEKSUN 1 [02:10-03:45]
Mostra pom.xml, destaka dependénsia
-->

---

# URL di Konexon

<img src="/images/02-connection-url.png" class="h-64 mx-auto" alt="JDBC Connection URL" />

<div class="pt-4 grid grid-cols-5 gap-2 text-sm text-center">
  <div><code class="text-skola-ocean">jdbc:</code><br/>Protokolu</div>
  <div><code class="text-skola-teal">postgresql</code><br/>Driver</div>
  <div><code class="text-skola-yellow">localhost</code><br/>Host</div>
  <div><code class="text-skola-teal">5432</code><br/>Porta</div>
  <div><code class="text-skola-coral">nhabazi</code><br/>Bazi</div>
</div>

<!--
Destaka komponenti di URL
-->

---

# Trez Objetu Prinsipal

<img src="/images/03-core-objects-enhanced.png" class="h-80 mx-auto" alt="Core JDBC Objects with Cursor" />

<div class="pt-2 text-sm text-center text-skola-gray">
  Connection → PreparedStatement → ResultSet | Tudu trez debe sera fetxadu!
</div>

<!--
Infográfiku ku kursor di ResultSet
-->

---

# Operason CRUD

| Operason | SQL | Métodu |
|----------|-----|--------|
| **C**reate | `INSERT` | `executeUpdate()` |
| **R**ead | `SELECT` | `executeQuery()` |
| **U**pdate | `UPDATE` | `executeUpdate()` |
| **D**elete | `DELETE` | `executeUpdate()` |

<div class="pt-8">
  <span class="text-sm text-skola-gray">Kuatu operason báziku pa manipula dadus</span>
</div>

<!--
CRUD overview antis di kodifikason
-->

---

# Inseri Dadus (Create)

```java {all|1|3-4|6}
String sql = "INSERT INTO uzuarius (nomi, email) VALUES (?, ?)";

pstmt.setString(1, nomiUzuariu);  // Primeru ?
pstmt.setString(2, email);        // Segundu ?

int linhas = pstmt.executeUpdate();
```

<div class="pt-4">
  <span class="text-skola-coral font-bold">?</span> = Placeholder di parametru (1-indexed)
</div>

<!--
SEKSUN 3 [05:30-08:15]
Destaka placeholders ? i setString
-->

---

# Le Dadus (Read)

```java {all|1|3-5}
ResultSet rs = pstmt.executeQuery();

while (rs.next()) {
    String nomi = rs.getString("nomi_uzuariu");
}
```

<div class="pt-4">
  <code class="text-skola-teal">executeQuery()</code> → ResultSet<br/>
  <code class="text-skola-teal">rs.next()</code> → Move kursor pa prósima linha
</div>

<!--
SEKSUN 4 [08:15-10:15]
-->

---

# ResultSet = Kursor

<div class="text-center pt-4">

```
┌─────────────────────┐
│  Bazi di Dadus     │ ← Konexon bibu
└──────────┬──────────┘
           │
     ┌─────▼─────┐
     │ ResultSet │ ← Kursor aponta pa linha atual
     └───────────┘
```

</div>

<div class="pt-8 grid grid-cols-2 gap-8">
<div>

**Importanti:**
- KA É ArrayList!
- É link bibu ku bazi
- Fetxa Connection = ResultSet móre

</div>
<div>

**Itera:**
```java
while (rs.next()) {
    // prosesa linha
}
// rs.next() = false kantu kaba
```

</div>
</div>

<!--
Konseitu xave di ResultSet
-->

---

# Atualiza i Apaga

<div class="grid grid-cols-2 gap-8">
<div>

**UPDATE:**
```java {all|1|3}
String sql = "UPDATE ... SET ... WHERE id = ?";

pstmt.setInt(1, uzuariuId);
pstmt.executeUpdate();
```

</div>
<div>

**DELETE:**
```java {all|1}
String sql = "DELETE FROM ... WHERE id = ?";

pstmt.setInt(1, uzuariuId);
pstmt.executeUpdate();
```

</div>
</div>

<div class="pt-8 text-center">
  <span class="text-skola-coral font-bold text-xl">Sen WHERE = Afeta TUDU linhas!</span>
</div>

<!--
SEKSUN 5-6 [10:15-13:15]
-->

---

# Seguransa: PreparedStatement

<img src="/images/04-preparedstatement-safety.jpg" class="h-72 mx-auto rounded shadow-lg" alt="SQL Injection Prevention" />

<div class="pt-4 text-center">
  <span class="text-skola-coral">NUNKA</span> konkatena input →
  <span class="text-skola-teal">SÉNPRI</span> uza <code>?</code> placeholders
</div>

<!--
Pontu Importanti - SQL Injection [05:30-08:15]
-->

---

# Rezolve Problema

| Éru | Soluson |
|-----|---------|
| `No suitable driver found` | Verifika dependénsia Maven |
| `Connection refused` | PostgreSQL ta kori? `pg_isready` |
| `Password authentication failed` | Verifika kredensial |
| `Column not found` | Verifika nomi di koluna |

<div class="pt-6 text-sm text-skola-gray">
  Dika: Le mensajen di éru ku atenson - el ta fra kuzé ki é problema!
</div>

<!--
SEKSUN 7 [13:15-14:45]
-->

---

# Rezumu

<v-clicks>

- Konektadu Java ku PostgreSQL ku JDBC
- Realizadu tudu operason CRUD
- Uzadu PreparedStatement pa preveni SQL injection
- Jeri rekursus koretamenti ku try-with-resources

</v-clicks>

<div class="pt-8">
  <span class="text-skola-teal font-bold">Parabéns! Bu da primeru pasu importante!</span>
</div>

<!--
REZUMU [16:30-17:20]
Txekmarks ta aparese
-->

---

# Dezafiu pa Bo

**Konstrui un Livru di Enderesus CLI:**

<div class="grid grid-cols-2 gap-8 pt-4">
<div>

**Tabela `kontatus`:**
- id (SERIAL)
- nomi (VARCHAR)
- telefoni (VARCHAR)
- email (VARCHAR)

</div>
<div>

**Funsons:**
- Djunta kontatu
- Lista tudu
- Buska pa nomi (ILIKE)
- Apaga kontatu

</div>
</div>

<div class="pt-8 text-sm text-skola-gray">
  Poe bu soluson na komentárius!
</div>

<!--
DEZAFIU [17:20-18:10]
-->

---

# Prósimus Pasus

<div class="grid grid-cols-2 gap-8 pt-8">
<div>

**Aprende Mas:**
- HikariCP (Connection Pooling)
- Transakson (commit/rollback)
- Spring Data JPA

</div>
<div>

**Rekursus:**
- Kódigu fonti na GitHub
- Dokumentason PostgreSQL JDBC
- Links na deskrison

</div>
</div>

<div class="pt-12 text-center">
  <span class="text-2xl">Da <span class="text-skola-coral">Like</span> i <span class="text-skola-ocean">Sigi</span> pa mas tutoriais!</span>
</div>

<!--
CTA [18:10-19:00]
-->

---
layout: center
class: text-center
---

# Obrigadu!

<div class="pt-8 text-xl text-skola-yellow">
  Nu ta studa, nu ta kria, nu ta partilha!
</div>

<div class="pt-12 text-lg text-white opacity-90">
  Skola.dev
</div>

<!--
OUTRO [19:00-19:20]
End cards, boton sigi
-->