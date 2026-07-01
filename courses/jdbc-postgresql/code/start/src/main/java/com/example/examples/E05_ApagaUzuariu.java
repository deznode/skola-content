package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * Ezénplu 05: Apaga dadus (DELETE).
 * Demonstra DELETE ku kláuzula WHERE — sen WHERE ta apaga TUDU linha!
 */
public class E05_ApagaUzuariu {

    public static void main(String[] args) {
        System.out.println("=== E05: Apaga Uzuáriu (DELETE) ===\n");

        String sql = "DELETE FROM uzuarius WHERE id = ?";

        // TODO: Implementa o DELETE.
        //   1. Kria Connection i PreparedStatement (try-with-resources)
        //   2. pstmt.setInt(1, 1)
        //   3. Kori pstmt.executeUpdate() i imprimi o númeru di linha apagadu
    }
}
