# Dev Container Setup

This Dev Container provides a stable control-plane environment for Coding Lab operations while the Kubernetes cluster continues to run on the host.
## Work in progress

This lab is actively being extended to run more of the Kubernetes development workflow inside the Dev Container rather than relying entirely on host-managed tooling.

The current setup uses the Dev Container as the primary control-plane workspace while the local Kubernetes cluster runs through Docker/k3d on the host. Ongoing work is focused on improving containerized cluster management, portability, and repeatability while keeping the environment easy to troubleshoot and validate.

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
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/safe-k8s.ps1 status
```

## Recommended daily flow

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/safe-k8s.ps1 validate
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/safe-k8s.ps1 apply
```

## Java quick run examples

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/launchers/java.ps1 -Mode add -Message "hello from devcontainer"
pwsh -NoProfile -ExecutionPolicy Bypass -File /workspaces/CodeLab-Hub/devops/zarf-testing/launchers/java.ps1 -Mode list
```

