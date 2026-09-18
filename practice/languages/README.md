# Coding Lab Repository Layout

This repository is organized by language so each language can map cleanly to its own container and work folder.

## Structure

- languages/cpp
- languages/go
- languages/javascript
- languages/php
- languages/python
- languages/java

## Cluster mapping

- Python workloads: languages/python
- JavaScript workloads: languages/javascript
- Go workloads: languages/go
- PHP workloads: languages/php
- Java workloads: languages/java
- C++ workloads: languages/cpp

The shared MySQL service remains in the cluster namespace `database` and is reachable by service name.
