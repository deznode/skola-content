# Java JDBC ku PostgreSQL - Referensia Rapidu (v42.7.2)

**Persona/Kontekstu:** Dezenvolvedor Java prinsipianti — buska sintaxi JDBC
**Testadu/Asunson:** Java 17+, PostgreSQL 16, Driver JDBC 42.7.2
**Linguajen:** kea

---

## Golden Path: Konekta i Faze Query

```java
import java.sql.*;

public class JdbcDemo {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/nhaapp";

        try (Connection conn = DriverManager.getConnection(url, "uzuariu", "senha");
             PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM uzuarius WHERE id = ?")) {

            pstmt.setInt(1, 42);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    System.out.println(rs.getString("nomi"));
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

---

## Trez Objetu Prinsipal

| Komponenti | Analogia | Objetivu |
|------------|----------|----------|
| **Connection** | Xamada telefoniku | Abri linha pa bazi di dadus |
| **PreparedStatement** | Mensajen | Leva bu query SQL ku parametrus |
| **ResultSet** | Resposta | Konten dadus ki bazi ta devolve |

---

## URL di Koneksun

```
jdbc:postgresql://localhost:5432/nhaapp
│    │           │         │    │
│    │           │         │    └── Nomi di bazi
│    │           │         └── Porta (5432 = padraun)
│    │           └── Host
│    └── Tipu di bazi
└── Protokolu
```

| Variasun | Ezemplu |
|----------|---------|
| Lokal | `jdbc:postgresql://localhost:5432/nhaapp` |
| Remotu | `jdbc:postgresql://db.ezemplu.com:5432/produsun` |
| Ku SSL | `jdbc:postgresql://localhost:5432/nhaapp?ssl=true` |

---

## CRUD - Operason Prinsipal

### CREATE (Insert)

```java
String sql = "INSERT INTO uzuarius (nomi, email) VALUES (?, ?)";
try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
    pstmt.setString(1, "maria_silva");
    pstmt.setString(2, "maria@ezemplu.com");
    int linhas = pstmt.executeUpdate();  // Devolve numeru di linhas inseridu
}
```

### READ (Select)

```java
String sql = "SELECT id, nomi, email FROM uzuarius WHERE email = ?";
try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
    pstmt.setString(1, "maria@ezemplu.com");
    try (ResultSet rs = pstmt.executeQuery()) {  // Devolve ResultSet
        while (rs.next()) {
            int id = rs.getInt("id");
            String nomi = rs.getString("nomi");
        }
    }
}
```

### UPDATE

```java
String sql = "UPDATE uzuarius SET email = ? WHERE id = ?";
try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
    pstmt.setString(1, "nobu@email.com");
    pstmt.setInt(2, 1);
    int linhas = pstmt.executeUpdate();  // 0 = ninhun linha atualizadu
}
```

### DELETE

```java
String sql = "DELETE FROM uzuarius WHERE id = ?";
try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
    pstmt.setInt(1, 1);
    int linhas = pstmt.executeUpdate();
}
```

---

## PreparedStatement - Setters

| Tipu Java | Metodu | Ezemplu |
|-----------|--------|---------|
| `String` | `setString(pos, val)` | `pstmt.setString(1, "Maria")` |
| `int` | `setInt(pos, val)` | `pstmt.setInt(2, 42)` |
| `long` | `setLong(pos, val)` | `pstmt.setLong(1, 999999L)` |
| `double` | `setDouble(pos, val)` | `pstmt.setDouble(1, 3.14)` |
| `boolean` | `setBoolean(pos, val)` | `pstmt.setBoolean(1, true)` |
| `Date` | `setDate(pos, val)` | `pstmt.setDate(1, Date.valueOf("2024-01-15"))` |
| `Timestamp` | `setTimestamp(pos, val)` | `pstmt.setTimestamp(1, Timestamp.valueOf(...))` |
| `null` | `setNull(pos, type)` | `pstmt.setNull(1, Types.VARCHAR)` |

> Pozisun `?` ta kumesa na **1**, ka na 0.

---

## ResultSet - Getters

| Metodu | Devolve | Uzu |
|--------|---------|-----|
| `rs.next()` | `boolean` | Move pa prosima linha; `false` kuandu kaba |
| `rs.getString("koluna")` | `String` | Le texto pa nomi di koluna |
| `rs.getInt("koluna")` | `int` | Le interu |
| `rs.getBoolean("koluna")` | `boolean` | Le verdadeiru/falsu |
| `rs.getDate("koluna")` | `Date` | Le data |
| `rs.wasNull()` | `boolean` | Verifica si ultimu valur era NULL |

> Senpri uza nomi di koluna (`rs.getString("nomi")`) invés di pozisun (`rs.getString(1)`).

---

## Metodus di Execusun

| Metodu | Uza Pa | Devolve |
|--------|--------|---------|
| `executeQuery()` | SELECT | `ResultSet` |
| `executeUpdate()` | INSERT, UPDATE, DELETE, CREATE | `int` (linhas afetadus) |

---

## 6 Pitfalls - Erru Komun

| Ka Faze | Porkê | Faze Invés |
|---------|-------|------------|
| `"SELECT * WHERE nomi = '" + input + "'"` | SQL Injection! | Uza `?` ku `PreparedStatement` |
| Fecha `Connection` antis di le `ResultSet` | ResultSet ta mori | Prosesa dentru di try-with-resources |
| Skese fecha Connection/Statement/ResultSet | Vazamentu di rekursus | Senpri uza try-with-resources |
| `UPDATE ... SET email = ?` sen WHERE | Atualiza TUDU linhas! | Senpri verifica WHERE |
| Trata ResultSet komu List | El é kursor vivu, ka kolesun | Kopia dadus pa List dentru di koneksun |
| `catch (Exception e) {}` vaziu | Erru ta pasa skalondidu | Log erru o re-throw |

---

## Rezolve Problema

### "No suitable driver found"

```xml
<!-- Djunta na pom.xml -->
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.2</version>
</dependency>
```

O ku JAR manual:
```bash
java -cp ".:postgresql-42.7.2.jar" JdbcDemo
```

### "Connection refused"

```bash
# Verifica si PostgreSQL ta kori
pg_isready

# Verifica servisu
sudo systemctl status postgresql
```

### "Password authentication failed"

1. Testa kredensial na psql: `psql -U uzuariu -d bazi`
2. Verifica erru di digitasun na kodigo
3. Verifica permisun CONNECT na bazi

---

## Seguransa - Txeklista

- [ ] **Nunka** guarda kredensial na kodigo fonti
- [ ] Uza variavel di ambienti:
  ```java
  String url = System.getenv("DATABASE_URL");
  String user = System.getenv("DATABASE_USER");
  String password = System.getenv("DATABASE_PASSWORD");
  ```
- [ ] Senpri uza `PreparedStatement`, nunka konkatenar input
- [ ] Da uzuarius so permisun ki es prizisa (prinsipiu di minimu privilejiu)

---

## Txeklista pa Produsun

- [ ] Ta uza connection pooling (HikariCP)
- [ ] Kredensial guardadu di forma seguru
- [ ] Tudu query ta uza `PreparedStatement`
- [ ] Tudu rekursus fechadu ku try-with-resources
- [ ] Timeout konfiguradu pa koneksun i query
- [ ] Tratamentu di erru i logging adequadu

---

## Versaun & Manutensun

* **Versaun di doc:** 1.0.0
* **Validadu na:** 2026-01-14
* **Risku di mudansa:** Atualizasun di driver JDBC, mudansa na API di PostgreSQL
* **Txeklista di revalidasun:**
  - [ ] Verifica changelog di driver JDBC
  - [ ] Kori ezemplus di kodigo
  - [ ] Verifica sintaxi di flags

---

## Rekursus

- [Dokumentasun JDBC di PostgreSQL](https://jdbc.postgresql.org/documentation/)
- [HikariCP](https://github.com/brettwooldridge/HikariCP) - Connection pooling pa produsun
