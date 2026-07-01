package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * Ezénplu 02: Inseri dadus (CREATE).
 * Demonstra PreparedStatement ku placeholder (?), setString(), executeUpdate().
 */
public class E02_InseriUzuariu {

    public static void main(String[] args) {
        System.out.println("=== E02: Inseri Uzuáriu (INSERT) ===\n");

        String sql = "INSERT INTO uzuarius (nomi_uzuariu, email) VALUES (?, ?)";

        // TODO: Implementa o INSERT.
        //   1. Kria Connection i PreparedStatement (try-with-resources)
        //   2. pstmt.setString(1, "Nira Tavares")  — primeru ?
        //   3. pstmt.setString(2, "nira@skola.dev") — segundu ?
        //   4. Kori pstmt.executeUpdate() i imprimi o númeru di linha
    }
}
