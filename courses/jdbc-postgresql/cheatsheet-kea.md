---
title: Java JDBC ku PostgreSQL
slug: jdbc-postgresql
courseSlug: jdbc-postgresql
language: kea
version: 1.0.0
validated_at: 2026-06-28
trace_id: Skola-course-jdbc-postgresql-cheatsheet-20260628
---

# JDBC Cheatsheet — Java ku PostgreSQL

**Língua:** kea (Kabuverdianu) | **Java:** 17+ (LTS) | **Driver:** org.postgresql 42.7.11 | **Doc version:** 1.0.0 | **Validadu na:** 2026-06-28

> **Pa ken?** Dizenvolvedor Java prinsipianti ki ta liga un programa ku PostgreSQL pa primeru bez.
> **Kumo uza:** Referénsia rápidu pa konsulta durante kursu. Kopia i kola kódiku diretu pa bu editor.

---

## Índisi

1. [Setup i URL di konexon](#1-setup-i-url-di-konexon)
2. [Konekta](#2-konekta)
3. [CRUD ku PreparedStatement](#3-crud-ku-preparedstatement)
4. [Le dadus ku ResultSet](#4-le-dadus-ku-resultset)
5. [Transasons](#5-transasons)
6. [Seguransa](#6-seguransa)
7. [Rezolve problema](#7-rezolve-problema)

---

## 1. Setup i URL di konexon

**Dependénsia Maven (`pom.xml`):**

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.11</version>
</dependency>
```

**Anatomia di JDBC URL:**

```
jdbc:postgresql://localhost:5432/nha_bazi
└──┬─┘ └───┬────┘ └───┬───┘ └┬─┘ └──┬───┘
protokolu  tipu      host  porta  nomi di bazi
```

| Parti | Ezénplu | Nota |
|-------|---------|------|
| Protokolu | `jdbc:` | Sénpri es |
| Tipu | `postgresql` | Driver |
| Host | `localhost` | Lokal, ou IP/domíniu |
| Porta | `5432` | Padron di PostgreSQL |
| Bazi | `nha_bazi` | Nomi di bu bazi di dadus |

---

## 2. Konekta

Sénpri uza **try-with-resources** — konexon ta fitxa automatikamenti.

```java
String URL = "jdbc:postgresql://localhost:5432/nha_bazi";
String USER = "nha_uzuariu";
String PASSWORD = "nha_senha";

try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {
    System.out.println("Konektadu!");
} catch (SQLException e) {
    e.printStackTrace();
}
```

---

## 3. CRUD ku PreparedStatement

**Regra di oru:** sénpri `PreparedStatement` ku `?` — nunka konkatena input na SQL. Placeholder `?` ta kumesa na **1**.

| Operasan | Métodu | Ta devolve |
|----------|--------|-----------|
| `SELECT` | `executeQuery()` | un `ResultSet` |
| `INSERT` / `UPDATE` / `DELETE` | `executeUpdate()` | `int` (fila afetadu) |

**Create (INSERT):**

```java
String sql = "INSERT INTO uzuarius (nomi, email) VALUES (?, ?)";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setString(1, "Ana Lima");
    ps.setString(2, "ana@email.cv");
    int linha = ps.executeUpdate();
}
```

**Update:**

```java
String sql = "UPDATE uzuarius SET email = ? WHERE id = ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setString(1, "nobu@email.cv");
    ps.setInt(2, 1);
    ps.executeUpdate();
}
```

**Delete:**

```java
String sql = "DELETE FROM uzuarius WHERE id = ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setInt(1, 1);
    ps.executeUpdate();
}
```

> **Kuidadu:** `UPDATE`/`DELETE` sen `WHERE` ta afeta **TUDU** fila. Verifika `WHERE` ku kuidadu.

---

## 4. Le dadus ku ResultSet

`ResultSet` é un **kursor bibu** pa riba di konexon — **ka** un koleson na memória. A `Connection` debe fika abertu enkuantu bu ta le.

```java
String sql = "SELECT id, nomi, email FROM uzuarius";
try (PreparedStatement ps = conn.prepareStatement(sql);
     ResultSet rs = ps.executeQuery()) {

    while (rs.next()) {                 // false kuandu kaba
        int id = rs.getInt("id");
        String nomi = rs.getString("nomi");
        System.out.println(id + ": " + nomi);
    }
}
```

**Kopia filas pa un `List` (en bez di devolve `ResultSet`):**

```java
List<Uzuariu> lista = new ArrayList<>();
try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
     PreparedStatement ps = conn.prepareStatement(sql);
     ResultSet rs = ps.executeQuery()) {
    while (rs.next()) {
        lista.add(new Uzuariu(rs.getInt("id"), rs.getString("nomi")));
    }
}
return lista;   // konexon fitxadu, mas dadus seguru na lista
```

---

## 5. Transasons

Pa agrupa vários statement nun sô operasan **tudu-ou-nada**:

```java
try {
    conn.setAutoCommit(false);          // kumesa transasan
    // ... vários UPDATE ...
    conn.commit();                      // grava tudu djuntu
} catch (SQLException e) {
    conn.rollback();                    // disfaze TUDU si algun falha
    throw e;
} finally {
    conn.setAutoCommit(true);           // restora o padron
}
```

| Métodu | Kuzé ki ta faze |
|--------|-----------------|
| `setAutoCommit(false)` | Kumesa transasan — nada ta grava te `commit()` |
| `commit()` | Grava tudu mudansa djuntu |
| `rollback()` | Disfaze TUDU si algun pasu falha |

---

## 6. Seguransa

| Faze | Nunka faze |
|------|-----------|
| `PreparedStatement` ku `?` | Konkatena input ku `+` na SQL |
| Kredensial na variável di anbienti | Kredensial na kódiku fonti |
| Permison mínimu pa uzuáriu | `GRANT ALL` pa tudu |
| try-with-resources | Dexa konexon abertu |

```java
String url = System.getenv("DATABASE_URL");
String user = System.getenv("DATABASE_USER");
String pass = System.getenv("DATABASE_PASSWORD");
```

---

## 7. Rezolve problema

| Éru | Kauza | Soluson |
|-----|-------|---------|
| `No suitable driver found` | Driver ka sta na classpath | Djunta `org.postgresql:postgresql:42.7.11` |
| `Connection refused` | Servidor ka ta kore / porta eradu | `pg_isready`; verifika porta 5432 i `pg_hba.conf` |
| `password authentication failed` | Uzuáriu/senha eradu | Testa ku `psql -U uzuariu -d bazi` |
| `too many connections` | Konexon vazadu | try-with-resources na tudu konexon |
| Dadus inkonsistenti dipos di falha | Falta `rollback()` | Nvolvi statement nun transasan |
