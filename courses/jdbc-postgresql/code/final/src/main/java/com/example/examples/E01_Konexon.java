package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * Ezénplu 01: Konekta ku bazi di dadus.
 * Demonstra DriverManager.getConnection() + try-with-resources + SELECT version().
 */
public class E01_Konexon {

    public static void main(String[] args) {
        System.out.println("=== E01: Konexon ku Bazi di Dadus ===\n");

        try (Connection conn = DriverManager.getConnection(
                DatabaseConfig.URL, DatabaseConfig.USER, DatabaseConfig.PASSWORD)) {

            System.out.println("Konektadu ku PostgreSQL!");

            try (PreparedStatement pstmt = conn.prepareStatement("SELECT version()");
                 ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    System.out.println("Verson di bazi: " + rs.getString(1));
                }
            }

        } catch (SQLException e) {
            System.err.println("Konexon falha!");
            e.printStackTrace();
        }
    }
}
