# Coding Lab

This folder contains the local lab environment for the Coding-lab Kubernetes cluster.

## Current cluster

- Cluster name: Coding-lab
- Context: k3d-Coding-lab
- Namespace layout:
  - database
  - apps
  - tools

## Recommended Dev Container Flow

Use the Dev Container as your control-plane workspace, while Kubernetes continues running on host Docker/k3d.

Dev Container config files:

- `.devcontainer/devcontainer.json`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`

After opening this repo in the Dev Container, run:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/safe-k8s.ps1 status
```

Then validate/apply as needed:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/safe-k8s.ps1 validate
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/safe-k8s.ps1 apply
```

## Shared services

- MySQL service: mysql.database.svc.cluster.local:3306

## Language containers

- python-test -> python
- node-test -> node
- go-test -> Go
- php-test -> PHP
- java-test -> Java
- cpp-test -> C++

## Launchers

Launcher scripts and full usage instructions are documented in:

`launchers/README.md`

Quick start from PowerShell:

```powershell
Set-Location i:\Test_Codes\ZARF_testing\launchers
.\python.ps1
.\javascript.ps1
.\go.ps1
.\php.ps1
.\java.ps1
.\cpp.ps1
```

Single entry command:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\open-language.ps1 python
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\open-language.ps1 java -Mode list
```

Optional profile aliases (type the language name directly):

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\install-language-aliases.ps1
```

After opening a new PowerShell terminal, you can run:

```powershell
python
javascript
go
php
java
cpp
```

## Validate Manifests

Before applying changes, run:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\validate-k8s.ps1
```

This performs client-side Kubernetes dry-run validation on all YAML files under `k8s`.

Safe wrapper command:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 validate
```

## Apply Manifests (`apply-k8s.ps1`)

To validate and then apply all lab manifests in a safe order, run:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\apply-k8s.ps1
```

Optional flags:

- Skip validation: `-SkipValidation`
- Skip rollout checks: `-SkipRolloutCheck`

What this script does:

- Validates all manifests under `k8s` (unless `-SkipValidation` is used)
- Applies manifests in dependency-safe order
- Checks rollout status for app and tools deployments (unless `-SkipRolloutCheck` is used)
- Prints final deployment and pod status

Safe wrapper command:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 apply
```

## K8s Helper Scripts

The lab includes these Kubernetes workflow helpers at the top level:

- `validate-k8s.ps1`
  - Validates all YAML manifests under `k8s` using client dry-run.
- `apply-k8s.ps1`
  - Validates manifests, applies them in dependency-safe order, then checks rollout status.
- `restore-lab.ps1`
  - Restores from the latest snapshot under `C:\Users\_\coding-lab-backups`.
- `safe-k8s.ps1`
  - Stable wrapper for `validate|apply|restore|status|java-api` actions.
- `open-language.ps1`
  - Routes a language designator to the correct launcher script.
- `install-language-aliases.ps1`
  - Installs PowerShell profile aliases so typing language names opens the matching container.

Suggested day-to-day flow:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\validate-k8s.ps1
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\apply-k8s.ps1
# or use wrapper actions:
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 validate
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 apply
```

Java API quick start (starts API + port-forward + opens browser):

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 java-api
```

Important endpoint note:

- Use `http://127.0.0.1:8080/api/messages` for this app.
- Root paths like `/` or `/signIn` may come from another local app/session and are not this API.

Verified API test flow:

```powershell
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8080/api/messages"

$body = @{ message = "from-rest-test" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8080/api/messages" -ContentType "application/json" -Body $body

Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8080/api/messages"
```

Optional local port:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 java-api -LocalPort 18080
```

## Snapshot and restore

A healthy cluster snapshot is stored under:

C:\Users\_\coding-lab-backups

Use the restore script:

powershell -ExecutionPolicy Bypass -File .\restore-lab.ps1

or via wrapper:

powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 restore

This script re-applies the latest healthy snapshot, then runs `apply-k8s.ps1` so current manifest changes (resources, readiness probes, rollout settings) are restored too.

Optional flag:

- Skip current manifest re-apply: `-SkipReapplyCurrentManifests`
