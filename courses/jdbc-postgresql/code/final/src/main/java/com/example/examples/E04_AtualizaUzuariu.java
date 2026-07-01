package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * Ezénplu 04: Atualiza dadus (UPDATE).
 * Demonstra UPDATE ku kláuzula WHERE — sénpri verifika o WHERE!
 */
public class E04_AtualizaUzuariu {

    public static void main(String[] args) {
        System.out.println("=== E04: Atualiza Uzuáriu (UPDATE) ===\n");

        String sql = "UPDATE uzuarius SET email = ? WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(
                DatabaseConfig.URL, DatabaseConfig.USER, DatabaseConfig.PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, "ana.lima@skola.dev");
            pstmt.setInt(2, 1);

            int linhasAfetadus = pstmt.executeUpdate();
            System.out.println("Atualizadu " + linhasAfetadus + " uzuáriu(s).");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
