package com.codinglab;

import java.time.Instant;
import java.util.List;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication
public class App implements CommandLineRunner {
    private final DemoMessageRepository repository;
    private final ConfigurableApplicationContext context;

    public App(DemoMessageRepository repository, ConfigurableApplicationContext context) {
        this.repository = repository;
        this.context = context;
    }

    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }

    @Override
    public void run(String... args) {
        repository.ensureSchema();

        if (args.length == 0) {
            System.out.println("REST API started. Endpoints under /api/messages");
            printCliHelp();
            return;
        }

        int exitCode = 0;
        try {
            handleCli(args);
        } catch (Exception ex) {
            exitCode = 1;
            System.err.println("CLI error: " + ex.getMessage());
        }

        final int finalExitCode = exitCode;
        SpringApplication.exit(context, () -> finalExitCode);
    }

    private void handleCli(String[] args) {
        String command = args[0].toLowerCase();
        switch (command) {
            case "list" -> printMessages(repository.findAll());
            case "add" -> {
                String message = resolveMessageArg(args);
                DemoMessage created = repository.create(message);
                System.out.printf("Added message #%d: %s%n", created.id(), created.message());
            }
            case "delete" -> {
                long id = resolveIdArg(args);
                boolean removed = repository.deleteById(id);
                if (removed) {
                    System.out.println("Deleted message #" + id);
                } else {
                    System.out.println("No message found for id=" + id);
                }
            }
            default -> throw new IllegalArgumentException("Unknown command: " + command);
        }
    }

    private static String resolveMessageArg(String[] args) {
        String envMessage = System.getenv("CLI_MESSAGE");
        if (envMessage != null && !envMessage.isBlank()) {
            return envMessage;
        }
        if (args.length >= 2 && !args[1].isBlank() && !args[1].startsWith("--")) {
            return args[1];
        }
        return "Hello from Java CLI at " + Instant.now();
    }

    private static long resolveIdArg(String[] args) {
        String value = null;
        if (args.length >= 2 && !args[1].startsWith("--")) {
            value = args[1];
        }
        if (value == null || value.isBlank()) {
            value = System.getenv("CLI_ID");
        }
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("delete requires an id argument or CLI_ID env var");
        }
        return Long.parseLong(value);
    }

    private static void printMessages(List<DemoMessage> messages) {
        if (messages.isEmpty()) {
            System.out.println("No messages found.");
            return;
        }
        System.out.println("demo_messages:");
        for (DemoMessage m : messages) {
            System.out.printf("- #%d | %s | %s%n", m.id(), m.message(), m.createdAt());
        }
    }

    private static void printCliHelp() {
        System.out.println("CLI commands:");
        System.out.println("  list");
        System.out.println("  add [message]");
        System.out.println("  delete <id>");
    }
}
