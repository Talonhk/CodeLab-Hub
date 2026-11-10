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

## Standard startup pattern (recommended)

Use the repo-backed startup scripts so each language folder can start required services and open its container shell consistently.

From `practice/languages`:

```powershell
.\start-services.ps1 -Action up
.\start-services.ps1 -Action status
.\start-services.ps1 -Action restart
```

From any language folder:

```powershell
.\start.ps1
```

This pattern keeps startup logic version-controlled in this repository and backed up to GitHub.

## Natural command aliases

If you want command-style prompts like "do some Java work", use:

```powershell
dosome java
do-work python
```

Install/update those aliases with:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\install-language-aliases.ps1
```
