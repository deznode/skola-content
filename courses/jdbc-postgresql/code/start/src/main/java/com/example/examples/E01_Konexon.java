package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * Ezénplu 01: Konekta ku bazi di dadus.
 * Demonstra DriverManager.getConnection() + try-with-resources.
 */
public class E01_Konexon {

    public static void main(String[] args) {
        System.out.println("=== E01: Konexon ku Bazi di Dadus ===\n");

        // TODO: Kria a konexon uzandu try-with-resources.
        //   1. try (Connection conn = DriverManager.getConnection(
        //          DatabaseConfig.URL, DatabaseConfig.USER, DatabaseConfig.PASSWORD)) { ... }
        //   2. Imprimi "Konektadu ku PostgreSQL!"
        //   3. Kori "SELECT version()" i imprimi rs.getString(1)
        //   4. catch (SQLException e) → imprimi o éru
    }
}
