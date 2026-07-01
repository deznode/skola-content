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
 * Djunta, lista, buska (ILIKE), i apaga kontatus — tudu ku PreparedStatement.
 */
public class LivruEnderesus {

    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection(
                DatabaseConfig.URL, DatabaseConfig.USER, DatabaseConfig.PASSWORD)) {
            criaTabelaKontatus(conn);
            koriMenu(conn);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    static void criaTabelaKontatus(Connection conn) throws SQLException {
        String sql = """
            CREATE TABLE IF NOT EXISTS kontatus (
                id SERIAL PRIMARY KEY,
                nomi VARCHAR(100) NOT NULL,
                telefoni VARCHAR(20),
                email VARCHAR(100)
            )
            """;
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.executeUpdate();
        }
    }

    static void koriMenu(Connection conn) throws SQLException {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n1. Djunta  2. Lista  3. Buska  4. Apaga  5. Sai");
            String skolha = scanner.nextLine();

            switch (skolha) {
                case "1" -> djuntaKontatu(conn, scanner);
                case "2" -> listaKontatus(conn);
                case "3" -> buskaKontatus(conn, scanner);
                case "4" -> apagaKontatu(conn, scanner);
                case "5" -> { return; }
            }
        }
    }

    static void djuntaKontatu(Connection conn, Scanner scanner) throws SQLException {
        System.out.print("Nomi: ");
        String nomi = scanner.nextLine();
        System.out.print("Telefoni: ");
        String telefoni = scanner.nextLine();
        System.out.print("Email: ");
        String email = scanner.nextLine();

        String sql = "INSERT INTO kontatus (nomi, telefoni, email) VALUES (?, ?, ?)";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, nomi);
            pstmt.setString(2, telefoni);
            pstmt.setString(3, email);
            pstmt.executeUpdate();
            System.out.println("Kontatu djuntadu!");
        }
    }

    static void listaKontatus(Connection conn) throws SQLException {
        String sql = "SELECT id, nomi, telefoni, email FROM kontatus ORDER BY nomi";
        try (PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {
            System.out.println("\n--- Kontatus ---");
            while (rs.next()) {
                System.out.printf("%d. %s | %s | %s%n",
                        rs.getInt("id"),
                        rs.getString("nomi"),
                        rs.getString("telefoni"),
                        rs.getString("email"));
            }
        }
    }

    static void buskaKontatus(Connection conn, Scanner scanner) throws SQLException {
        System.out.print("Buska nomi: ");
        String termu = scanner.nextLine();

        String sql = "SELECT id, nomi, telefoni FROM kontatus WHERE nomi ILIKE ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, "%" + termu + "%");
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("%d. %s - %s%n",
                            rs.getInt("id"),
                            rs.getString("nomi"),
                            rs.getString("telefoni"));
                }
            }
        }
    }

    static void apagaKontatu(Connection conn, Scanner scanner) throws SQLException {
        System.out.print("ID di kontatu pa apaga: ");
        int id = Integer.parseInt(scanner.nextLine());

        String sql = "DELETE FROM kontatus WHERE id = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int apagadu = pstmt.executeUpdate();
            System.out.println(apagadu > 0 ? "Apagadu!" : "Ka atxadu.");
        }
    }
}
