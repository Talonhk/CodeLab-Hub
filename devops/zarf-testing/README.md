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
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/safe-k8s.ps1 status
```

Then validate/apply as needed:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/safe-k8s.ps1 validate
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/safe-k8s.ps1 apply
```

## Shared services

- MySQL service: mysql.database.svc.cluster.local:3306

## MySQL credentials and local vault

MySQL credentials are stored in Kubernetes Secret `mysql-credentials` and should not be hardcoded in manifests.

Namespace note: Kubernetes secrets are namespace-scoped. The MySQL StatefulSet in `database` and language deployments in `apps` both need a `mysql-credentials` secret in their own namespace.

For Windows local development, credentials are also stored in Windows Credential Manager:

- `CodeLabHub/mysql-root`
- `CodeLabHub/mysql-app`

Read credentials in PowerShell:

```powershell
Import-Module CredentialManager
$root = Get-StoredCredential -Target 'CodeLabHub/mysql-root'
$app = Get-StoredCredential -Target 'CodeLabHub/mysql-app'
$rootUser = $root.UserName
$rootPass = $root.GetNetworkCredential().Password
$appUser = $app.UserName
$appPass = $app.GetNetworkCredential().Password
```

Sync Kubernetes secret from local vault values:

```powershell
Import-Module CredentialManager
$root = Get-StoredCredential -Target 'CodeLabHub/mysql-root'
$app = Get-StoredCredential -Target 'CodeLabHub/mysql-app'

kubectl -n database create secret generic mysql-credentials \
  --from-literal=root-password="$($root.GetNetworkCredential().Password)" \
  --from-literal=app-database='appdb' \
  --from-literal=app-user="$($app.UserName)" \
  --from-literal=app-password="$($app.GetNetworkCredential().Password)" \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl -n apps create secret generic mysql-credentials \
  --from-literal=root-password="$($root.GetNetworkCredential().Password)" \
  --from-literal=app-database='appdb' \
  --from-literal=app-user="$($app.UserName)" \
  --from-literal=app-password="$($app.GetNetworkCredential().Password)" \
  --dry-run=client -o yaml | kubectl apply -f -
```

## Language containers

- python-test -> python
- node-test -> node
- go-test -> Go
- php-test -> PHP
- java-test -> Java
- cpp-test -> C++

These deployments read `DB_NAME`, `DB_USER`, and `DB_PASS` from `apps/mysql-credentials` using `secretKeyRef`.

Quick connectivity verification for all language pods:

```powershell
$deployments = 'python-test','node-test','go-test','php-test','java-test','cpp-test'
foreach ($d in $deployments) {
  kubectl -n apps rollout status deploy/$d --timeout=180s
  kubectl -n apps exec deploy/$d -- bash -lc "echo > /dev/tcp/mysql.database.svc.cluster.local/3306"
  if ($LASTEXITCODE -eq 0) { "$d => OK" } else { "$d => FAIL" }
}
```

## Launchers

Launcher scripts and full usage instructions are documented in:

`launchers/README.md`

Quick start from PowerShell:

```powershell
Set-Location i:\CodeLab-Hub\devops\zarf-testing\launchers
.\python.ps1
.\javascript.ps1
.\go.ps1
.\php.ps1
.\java.ps1
.\cpp.ps1
```

Single entry command:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\open-language.ps1 python
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\open-language.ps1 java -Mode list
```

Optional profile aliases:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\install-language-aliases.ps1
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
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\validate-k8s.ps1
```

Safe wrapper command:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 validate
```

## Apply Manifests

To validate and then apply all lab manifests in a safe order, run:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\apply-k8s.ps1
```

Safe wrapper command:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 apply
```

Optional flags:

- Skip validation: `-SkipValidation`
- Skip rollout checks: `-SkipRolloutCheck`

## K8s Helper Scripts

- `validate-k8s.ps1` - client-side dry-run validation
- `apply-k8s.ps1` - validate, apply, and check rollout status
- `restore-lab.ps1` - restore from `C:\Users\_\coding-lab-backups`
- `safe-k8s.ps1` - wrapper for `validate|apply|restore|status|java-api`
- `open-language.ps1` - route to the correct launcher script
- `install-language-aliases.ps1` - install PowerShell aliases for the language names

## Java API quick start

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 java-api
```

Use this API endpoint directly:

- `http://127.0.0.1:8080/api/messages`

## Snapshot and restore

A healthy cluster snapshot is stored under `C:\Users\_\coding-lab-backups`.

Use the restore script:

```powershell
powershell -ExecutionPolicy Bypass -File .\restore-lab.ps1
```

Or via wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 restore
```

