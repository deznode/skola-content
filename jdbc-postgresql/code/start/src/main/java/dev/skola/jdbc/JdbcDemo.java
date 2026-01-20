package dev.skola.jdbc;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.sql.*;

/**
 * JDBC PostgreSQL Tutorial - Starter Code
 * Complete the TODOs to learn database connectivity.
 */
public class JdbcDemo {
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/skola_db";
    private static final String DB_USER = "skola";
    private static final String DB_PASSWORD = "skola";

    private final HikariDataSource dataSource;

    public JdbcDemo() {
        // TODO: Configure HikariCP connection pool
        // 1. Create a HikariConfig object
        // 2. Set JDBC URL, username, password
        // 3. Set maximum pool size to 10
        // 4. Create HikariDataSource from config
        this.dataSource = null; // Replace with your implementation
    }

    public void initializeDatabase() throws SQLException {
        // TODO: Create the users table if it doesn't exist
        // Table structure:
        //   id SERIAL PRIMARY KEY
        //   name VARCHAR(100) NOT NULL
        //   email VARCHAR(100) UNIQUE NOT NULL
        //   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        //
        // Hint: Use try-with-resources with Connection and Statement
    }

    public void insertUser(String name, String email) throws SQLException {
        // TODO: Insert a new user using PreparedStatement
        // 1. Create INSERT SQL with ? placeholders
        // 2. Use PreparedStatement with RETURN_GENERATED_KEYS
        // 3. Set parameters with setString()
        // 4. Execute update and get generated ID
        // 5. Print the generated ID
    }

    public void listUsers() throws SQLException {
        // TODO: Query and display all users
        // 1. Create SELECT SQL
        // 2. Execute query and iterate ResultSet
        // 3. Print each user's details
    }

    public void updateUser(long id, String newName) throws SQLException {
        // TODO: Update a user's name by ID
        // 1. Create UPDATE SQL with ? placeholders
        // 2. Use PreparedStatement to set parameters
        // 3. Execute and print affected rows
    }

    public void deleteUser(long id) throws SQLException {
        // TODO: Delete a user by ID
        // 1. Create DELETE SQL with ? placeholder
        // 2. Use PreparedStatement to set the ID
        // 3. Execute and print affected rows
    }

    public void demonstrateTransaction() throws SQLException {
        // TODO: Implement a transaction that inserts two users
        // 1. Get connection and set autoCommit to false
        // 2. Insert two users
        // 3. Commit on success
        // 4. Rollback on any error
        // 5. Reset autoCommit to true in finally block
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

            // TODO: Call your CRUD methods here to test
            // demo.insertUser("Maria Silva", "maria@skola.dev");
            // demo.listUsers();
            // ...

            System.out.println("Complete the TODOs to see JDBC in action!");

        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            e.printStackTrace();
        } finally {
            demo.close();
        }
    }
}
