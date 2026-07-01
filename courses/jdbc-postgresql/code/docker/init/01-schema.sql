-- Schema pa kursu "Java JDBC ku PostgreSQL" — Skola.dev
-- Bazi di dadus: skola_dev (kria automatikamenti pa docker-compose)

-- Tabela di uzuárius (di os ezénplu E01–E05)
CREATE TABLE IF NOT EXISTS uzuarius (
    id SERIAL PRIMARY KEY,
    nomi_uzuariu VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    kriadu_na TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela di kontatus (di o dezafiu: Livru di Enderesus)
CREATE TABLE IF NOT EXISTS kontatus (
    id SERIAL PRIMARY KEY,
    nomi VARCHAR(100) NOT NULL,
    telefoni VARCHAR(20),
    email VARCHAR(100)
);

-- Dadus di izénplu pa testa
INSERT INTO uzuarius (nomi_uzuariu, email) VALUES
    ('Ana Lima', 'ana@skola.dev'),
    ('Tóni Gomes', 'toni@skola.dev');
