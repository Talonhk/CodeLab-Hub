# Coding Lab launchers

Each launcher is a small script that points to the correct language container and repo folder.
Each launcher also opens an interactive shell in the target pod with a prompt marker like `[python-test] user@host:/path$`.

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

Use the matching language container for each project folder to avoid mixing code and dependencies.

## Launch Commands

From `i:\Test_Codes\ZARF_testing\launchers` run:

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
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\open-language.ps1 python
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\open-language.ps1 java -Mode api
```

From Dev Container, use:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/open-language.ps1 python
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/open-language.ps1 java -Mode api
```

Kubernetes safe wrapper (recommended for cluster actions):

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 validate
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 apply
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 status
```

Java API one-command quick start (launch API, start port-forward, open endpoint):

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 java-api
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
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 java-api -LocalPort 18080
```

From Dev Container terminal, use the Linux workspace path:

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/safe-k8s.ps1 java-api
```

Install language aliases in your PowerShell profile:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\install-language-aliases.ps1
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
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/launchers/java.ps1 -Mode list
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/ZARF_testing/launchers/java.ps1 -Mode add -Message "hello"
```

- `-Mode api` starts the Spring Boot REST API in the `java-test` pod.
- `-Mode list|add|delete` runs CLI CRUD commands against `demo_messages`.

What each launcher does:

- Changes host directory to the matching repo folder under `i:\Test_Codes\languages\<language>`
- Runs `kubectl exec -it` into the matching deployment in namespace `apps`
- Sets a language-specific prompt marker and opens an interactive Bash shell

## Expected Prompt Markers

- Python: `[python-test] user@host:/path$`
- JavaScript: `[node-test] user@host:/path$`
- Go: `[go-test] user@host:/path$`
- PHP: `[php-test] user@host:/path$`
- Java: `[java-test] user@host:/path$`
- C++: `[cpp-test] user@host:/path$`

## Exit Back To Host

Inside a container shell, run:

```bash
exit
```

This returns you to your local PowerShell session.

## Apply K8s Manifests (`apply-k8s.ps1`)

When you make Kubernetes manifest changes, use the top-level helper:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\apply-k8s.ps1
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
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\validate-k8s.ps1
```

- To validate and apply all manifests in one step:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\apply-k8s.ps1
```

- Prefer wrapper form for stable execution:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\safe-k8s.ps1 apply
```

- Full Kubernetes helper script overview is documented in the top-level lab README:

`i:\Test_Codes\ZARF_testing\README.md`

- If the cluster is unhealthy, restore the latest known-good state:

```powershell
powershell -ExecutionPolicy Bypass -File i:\Test_Codes\ZARF_testing\restore-lab.ps1
```

## Current Status

All six launcher paths were validated with smoke tests (runtime check + MySQL TCP connectivity) and are working.
