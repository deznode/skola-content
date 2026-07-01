package com.example.config;

/**
 * Konfigurason di bazi di dadus pa o kursu JDBC.
 * Os valor li ta korresponde ku docker/docker-compose.yml.
 */
public final class DatabaseConfig {

    // jdbc:postgresql://host:porta/nomi_bazi
    public static final String URL = "jdbc:postgresql://localhost:5432/skola_dev";
    public static final String USER = "skola";
    public static final String PASSWORD = "skola_dev";

    private DatabaseConfig() {
        // Klasi utilitáriu — ka instansia
    }
}
