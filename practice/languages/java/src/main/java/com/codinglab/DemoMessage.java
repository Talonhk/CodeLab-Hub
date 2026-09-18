package com.codinglab;

import java.sql.Timestamp;

public record DemoMessage(long id, String message, Timestamp createdAt) {
}
