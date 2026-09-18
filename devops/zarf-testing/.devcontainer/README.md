# Dev Container Setup

This Dev Container provides a stable control-plane environment for Coding Lab operations while the Kubernetes cluster continues to run on the host.

## Included tools

- `kubectl`
- `helm`
- `pwsh`
- Java 21 + Maven
- Python 3
- Node.js 20
- Go
- PHP CLI
- MySQL client

## Open in container

1. Open `devops/zarf-testing` in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. Wait for the build to complete.

## Verify cluster access from container

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/devops/zarf-testing/safe-k8s.ps1 status
```

## Recommended daily flow

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/devops/zarf-testing/safe-k8s.ps1 validate
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/devops/zarf-testing/safe-k8s.ps1 apply
```

## Java quick run examples

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/devops/zarf-testing/launchers/java.ps1 -Mode add -Message "hello from devcontainer"
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/Test_Codes/devops/zarf-testing/launchers/java.ps1 -Mode list
```
