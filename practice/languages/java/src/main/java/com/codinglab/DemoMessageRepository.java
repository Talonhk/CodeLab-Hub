package com.codinglab;

import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
import org.springframework.stereotype.Repository;

@Repository
public class DemoMessageRepository {
    private final JdbcTemplate jdbc;

    public DemoMessageRepository(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public void ensureSchema() {
        jdbc.execute("""
            CREATE TABLE IF NOT EXISTS demo_messages (
                id INT PRIMARY KEY AUTO_INCREMENT,
                message VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """);
    }

    public List<DemoMessage> findAll() {
        return jdbc.query(
            "SELECT id, message, created_at FROM demo_messages ORDER BY id DESC LIMIT 100",
            (rs, rowNum) -> new DemoMessage(
                rs.getLong("id"),
                rs.getString("message"),
                rs.getTimestamp("created_at")
            )
        );
    }

    public DemoMessage findById(long id) {
        List<DemoMessage> rows = jdbc.query(
            "SELECT id, message, created_at FROM demo_messages WHERE id = ?",
            (rs, rowNum) -> new DemoMessage(
                rs.getLong("id"),
                rs.getString("message"),
                rs.getTimestamp("created_at")
            ),
            id
        );
        return rows.isEmpty() ? null : rows.getFirst();
    }

    public DemoMessage create(String message) {
        KeyHolder keyHolder = new GeneratedKeyHolder();
        jdbc.update(connection -> {
            var ps = connection.prepareStatement(
                "INSERT INTO demo_messages(message) VALUES (?)",
                new String[] { "id" }
            );
            ps.setString(1, message);
            return ps;
        }, keyHolder);

        Number key = keyHolder.getKey();
        if (key == null) {
            throw new IllegalStateException("Failed to create message: missing generated id");
        }
        DemoMessage created = findById(key.longValue());
        if (created == null) {
            throw new IllegalStateException("Failed to load created message");
        }
        return created;
    }

    public DemoMessage update(long id, String message) {
        int changed = jdbc.update("UPDATE demo_messages SET message = ? WHERE id = ?", message, id);
        if (changed == 0) {
            return null;
        }
        return findById(id);
    }

    public boolean deleteById(long id) {
        return jdbc.update("DELETE FROM demo_messages WHERE id = ?", id) > 0;
    }
}
