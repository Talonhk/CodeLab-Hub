# Coding Lab launchers

Each launcher points to the correct language container and repo folder, then opens an interactive shell in the target pod.

## Prerequisites

- Kubernetes context is set to `k3d-Coding-lab`
- App pods are running in namespace `apps`
- You are running from PowerShell on the host machine

Quick checks:

```powershell
kubectl config current-context
kubectl get pods -n apps
```

## Mapping

- python -> python-test -> /workspace/languages/python
- javascript -> node-test -> /workspace/languages/javascript
- go -> go-test -> /workspace/languages/go
- php -> php-test -> /workspace/languages/php
- java -> java-test -> /workspace/languages/java
- cpp -> cpp-test -> /workspace/languages/cpp

## Launch Commands

From `i:\CodeLab-Hub\devops\zarf-testing\launchers` run:

```powershell
.\python.ps1
.\javascript.ps1
.\go.ps1
.\php.ps1
.\java.ps1
.\cpp.ps1
```

Single language entry script:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\open-language.ps1 python
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\open-language.ps1 java -Mode api
```

From Dev Container, use:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/open-language.ps1 python
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/open-language.ps1 java -Mode api
```

Kubernetes safe wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 validate
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 apply
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 status
```

Java API quick start:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 java-api
```

Use this API endpoint directly:

- `http://127.0.0.1:8080/api/messages`

Quick verification:

```powershell
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8080/api/messages"
$body = @{ message = "from-rest-test" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8080/api/messages" -ContentType "application/json" -Body $body
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8080/api/messages"
```

Use a custom local port if needed:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 java-api -LocalPort 18080
```

Install language aliases in your PowerShell profile:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\install-language-aliases.ps1
```

Then open a new terminal and type the language directly:

```powershell
python
java -Mode list
java -Mode add -Message "hello"
java -Mode delete -Id 1
```

Java one-command modes:

```powershell
.\java.ps1 -Mode api
.\java.ps1 -Mode list
.\java.ps1 -Mode add -Message "Hello from host"
.\java.ps1 -Mode delete -Id 1
```

From Dev Container path:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/launchers/java.ps1 -Mode list
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/launchers/java.ps1 -Mode add -Message "hello"
```

- `-Mode api` starts the Spring Boot REST API in the `java-test` pod.
- `-Mode list|add|delete` runs CLI CRUD commands against `demo_messages`.

## Exit Back To Host

Inside a container shell, run:

```bash
exit
```

## Apply K8s Manifests

When you make Kubernetes manifest changes, use the top-level helper:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\apply-k8s.ps1
```

Optional flags:

- Skip validation: `-SkipValidation`
- Skip rollout checks: `-SkipRolloutCheck`

## Troubleshooting

- If `kubectl` is not found, open the terminal where your Kubernetes tools are installed and on PATH.
- If a launcher fails with pod not found, verify deployment and pod state:

```powershell
kubectl get deploy -n apps
kubectl get pods -n apps
```

- If deployment changes were made recently, validate manifests before apply:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\validate-k8s.ps1
```

- To validate and apply all manifests in one step:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\apply-k8s.ps1
```

- Prefer wrapper form for stable execution:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\safe-k8s.ps1 apply
```

- Full Kubernetes helper script overview is documented in the top-level lab README:

`i:\CodeLab-Hub\devops\zarf-testing\README.md`

- If the cluster is unhealthy, restore the latest known-good state:

```powershell
powershell -ExecutionPolicy Bypass -File i:\CodeLab-Hub\devops\zarf-testing\restore-lab.ps1
```

## Current Status

All six launcher paths were validated with smoke tests and are working.

