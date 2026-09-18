package com.codinglab;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/messages")
public class DemoMessageController {
    private final DemoMessageRepository repository;

    public DemoMessageController(DemoMessageRepository repository) {
        this.repository = repository;
    }

    @GetMapping
    public List<DemoMessage> list() {
        return repository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<DemoMessage> get(@PathVariable long id) {
        DemoMessage row = repository.findById(id);
        if (row == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(row);
    }

    @PostMapping
    public ResponseEntity<DemoMessage> create(@RequestBody MessagePayload payload) {
        if (payload == null || payload.message() == null || payload.message().isBlank()) {
            return ResponseEntity.badRequest().build();
        }
        DemoMessage created = repository.create(payload.message());
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @PutMapping("/{id}")
    public ResponseEntity<DemoMessage> update(@PathVariable long id, @RequestBody MessagePayload payload) {
        if (payload == null || payload.message() == null || payload.message().isBlank()) {
            return ResponseEntity.badRequest().build();
        }
        DemoMessage updated = repository.update(id, payload.message());
        if (updated == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable long id) {
        boolean removed = repository.deleteById(id);
        if (!removed) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.noContent().build();
    }

    public record MessagePayload(String message) {
    }
}
