package dev.skola.jdbc;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.sql.*;

/**
 * JDBC PostgreSQL Tutorial - Complete Solution
 * Demonstrates database connectivity and CRUD operations.
 */
public class JdbcDemo {
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/skola_db";
    private static final String DB_USER = "skola";
    private static final String DB_PASSWORD = "skola";

    private final HikariDataSource dataSource;

    public JdbcDemo() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl(DB_URL);
        config.setUsername(DB_USER);
        config.setPassword(DB_PASSWORD);
        config.setMaximumPoolSize(10);
        this.dataSource = new HikariDataSource(config);
    }

    public void initializeDatabase() throws SQLException {
        String createTableSQL = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """;

        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute(createTableSQL);
            System.out.println("Table 'users' created or already exists.");
        }
    }

    public void insertUser(String name, String email) throws SQLException {
        String insertSQL = "INSERT INTO users (name, email) VALUES (?, ?)";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(insertSQL, Statement.RETURN_GENERATED_KEYS)) {
            pstmt.setString(1, name);
            pstmt.setString(2, email);
            int affectedRows = pstmt.executeUpdate();

            if (affectedRows > 0) {
                try (ResultSet rs = pstmt.getGeneratedKeys()) {
                    if (rs.next()) {
                        System.out.println("Inserted user with ID: " + rs.getLong(1));
                    }
                }
            }
        }
    }

    public void listUsers() throws SQLException {
        String selectSQL = "SELECT id, name, email, created_at FROM users ORDER BY id";

        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(selectSQL)) {

            System.out.println("\n=== Users ===");
            while (rs.next()) {
                System.out.printf("ID: %d, Name: %s, Email: %s, Created: %s%n",
                    rs.getLong("id"),
                    rs.getString("name"),
                    rs.getString("email"),
                    rs.getTimestamp("created_at"));
            }
        }
    }

    public void updateUser(long id, String newName) throws SQLException {
        String updateSQL = "UPDATE users SET name = ? WHERE id = ?";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(updateSQL)) {
            pstmt.setString(1, newName);
            pstmt.setLong(2, id);
            int affectedRows = pstmt.executeUpdate();
            System.out.println("Updated " + affectedRows + " row(s).");
        }
    }

    public void deleteUser(long id) throws SQLException {
        String deleteSQL = "DELETE FROM users WHERE id = ?";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(deleteSQL)) {
            pstmt.setLong(1, id);
            int affectedRows = pstmt.executeUpdate();
            System.out.println("Deleted " + affectedRows + " row(s).");
        }
    }

    public void demonstrateTransaction() throws SQLException {
        Connection conn = null;
        try {
            conn = dataSource.getConnection();
            conn.setAutoCommit(false);

            // Insert two users in a transaction
            String insertSQL = "INSERT INTO users (name, email) VALUES (?, ?)";
            try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
                pstmt.setString(1, "Transaction User 1");
                pstmt.setString(2, "tx1@example.com");
                pstmt.executeUpdate();

                pstmt.setString(1, "Transaction User 2");
                pstmt.setString(2, "tx2@example.com");
                pstmt.executeUpdate();
            }

            conn.commit();
            System.out.println("Transaction committed successfully.");
        } catch (SQLException e) {
            if (conn != null) {
                conn.rollback();
                System.out.println("Transaction rolled back due to error: " + e.getMessage());
            }
            throw e;
        } finally {
            if (conn != null) {
                conn.setAutoCommit(true);
                conn.close();
            }
        }
    }

    public void close() {
        if (dataSource != null) {
            dataSource.close();
        }
    }

    public static void main(String[] args) {
        JdbcDemo demo = new JdbcDemo();
        try {
            demo.initializeDatabase();

            // CRUD operations
            demo.insertUser("Maria Silva", "maria@skola.dev");
            demo.insertUser("João Santos", "joao@skola.dev");
            demo.listUsers();

            demo.updateUser(1, "Maria Santos Silva");
            demo.listUsers();

            // Transaction demo
            demo.demonstrateTransaction();
            demo.listUsers();

        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            e.printStackTrace();
        } finally {
            demo.close();
        }
    }
}
