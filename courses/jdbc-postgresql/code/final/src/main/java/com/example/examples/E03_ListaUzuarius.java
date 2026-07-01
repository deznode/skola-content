package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * Ezénplu 03: Le dadus (READ).
 * Demonstra executeQuery(), ResultSet komu kursor, i while (rs.next()).
 */
public class E03_ListaUzuarius {

    public static void main(String[] args) {
        System.out.println("=== E03: Lista Uzuárius (SELECT) ===\n");

        String sql = "SELECT id, nomi_uzuariu, email FROM uzuarius ORDER BY id";

        try (Connection conn = DriverManager.getConnection(
                DatabaseConfig.URL, DatabaseConfig.USER, DatabaseConfig.PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            while (rs.next()) {
                System.out.printf("ID: %d | Uzuáriu: %s | Email: %s%n",
                        rs.getInt("id"),
                        rs.getString("nomi_uzuariu"),
                        rs.getString("email"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
