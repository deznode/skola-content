package com.example.projeto;

import com.example.config.DatabaseConfig;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

/**
 * Dezafiu: Livru di Enderesus (CLI).
 * Konstrui un menu ki ta djunta, lista, buska (ILIKE), i apaga kontatus —
 * tudu ku PreparedStatement.
 */
public class LivruEnderesus {

    public static void main(String[] args) {
        // TODO: Konstrui o livru di enderesus.
        //   1. Konekta ku DatabaseConfig (try-with-resources)
        //   2. Kria a tabela `kontatus` (id, nomi, telefoni, email) si ka izisti
        //   3. Menu loop ku Scanner: 1.Djunta 2.Lista 3.Buska 4.Apaga 5.Sai
        //   4. Buska: WHERE nomi ILIKE ?  ku  "%" + termu + "%"
        //   5. Uza PreparedStatement pa TUDU query
    }
}
