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

        // TODO: Implementa o UPDATE.
        //   1. Kria Connection i PreparedStatement (try-with-resources)
        //   2. pstmt.setString(1, "ana.lima@skola.dev")
        //   3. pstmt.setInt(2, 1)
        //   4. Kori pstmt.executeUpdate() i imprimi o númeru di linha atualizadu
    }
}
