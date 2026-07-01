package com.example.examples;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * Ezénplu 03: Le dadus (READ).
 * Demonstra executeQuery(), ResultSet komu kursor, while (rs.next()).
 */
public class E03_ListaUzuarius {

    public static void main(String[] args) {
        System.out.println("=== E03: Lista Uzuárius (SELECT) ===\n");

        String sql = "SELECT id, nomi_uzuariu, email FROM uzuarius ORDER BY id";

        // TODO: Implementa o SELECT.
        //   1. Kria Connection, PreparedStatement, ResultSet (try-with-resources)
        //   2. Kori pstmt.executeQuery() pa otén o ResultSet
        //   3. while (rs.next()) { ... }
        //   4. Uza rs.getInt("id"), rs.getString("nomi_uzuariu"), rs.getString("email")
    }
}
