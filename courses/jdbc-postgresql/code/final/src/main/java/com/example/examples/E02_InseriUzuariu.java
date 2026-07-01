package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * Ezénplu 02: Inseri dadus (CREATE).
 * Demonstra PreparedStatement ku placeholder (?), setString(), i executeUpdate().
 */
public class E02_InseriUzuariu {

    public static void main(String[] args) {
        System.out.println("=== E02: Inseri Uzuáriu (INSERT) ===\n");

        String sql = "INSERT INTO uzuarius (nomi_uzuariu, email) VALUES (?, ?)";

        try (Connection conn = DriverManager.getConnection(
                DatabaseConfig.URL, DatabaseConfig.USER, DatabaseConfig.PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, "Nira Tavares");
            pstmt.setString(2, "nira@skola.dev");

            int linhasAfetadus = pstmt.executeUpdate();
            System.out.println("Inseridu " + linhasAfetadus + " uzuáriu(s).");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
