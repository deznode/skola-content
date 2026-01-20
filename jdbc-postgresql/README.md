# JDBC with PostgreSQL

Learn database connectivity using JDBC with PostgreSQL.

## Prerequisites

- Java 21+ (JDK)
- Maven 3.9+
- PostgreSQL 15+ (or Docker)
- IDE with Java support

## Setup

### Database Setup

```bash
# Using Docker
docker run -d \
  --name postgres-jdbc \
  -e POSTGRES_USER=skola \
  -e POSTGRES_PASSWORD=skola \
  -e POSTGRES_DB=skola_db \
  -p 5432:5432 \
  postgres:15

# Or use existing PostgreSQL installation
createdb -U postgres skola_db
```

### Project Setup

```bash
# Navigate to starter code
cd initial/

# Build the project
mvn compile

# Run the application
mvn exec:java
```

## Learning Objectives

By completing this tutorial, you will learn:

- JDBC driver setup and configuration
- Connection management and pooling
- Executing queries with Statement and PreparedStatement
- Handling ResultSets
- Transaction management
- Error handling and resource cleanup

## Structure

```
jdbc-postgresql/
├── initial/                    # Start here - scaffolding with TODOs
│   ├── pom.xml
│   └── src/main/java/dev/skola/jdbc/
└── complete/                   # Reference solution
    ├── pom.xml
    └── src/main/java/dev/skola/jdbc/
```

## Tutorial Link

Follow the full tutorial at: [skola.dev/tutorials/jdbc-postgresql](https://skola.dev/tutorials/jdbc-postgresql)
