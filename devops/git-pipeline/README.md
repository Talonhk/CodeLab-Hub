# Git Pipeline

CI/CD pipeline experiments and infrastructure-as-code examples for automating deployments.

## Project structure

- `ci-cd/` - Pipeline definitions and Kubernetes deployment configurations
  - Contains Java app example with Terraform infrastructure definitions
  - Kubernetes manifests for service and deployment
  - Pipeline test scripts
- `pipeline-test/` - Test and validation scripts

## Included tech

- Terraform configurations for infrastructure provisioning
- Kubernetes manifests for containerized deployment
- Shell and pipeline scripts for automation
- Java application example (SimpleJavaApp)

## Suggested next work

- Document the full pipeline flow (commit → build → test → deploy)
- Add GitHub Actions or GitLab CI configurations
- Create a local test environment using Docker Compose
- Document secrets management and credential handling
- Add deployment runbook with troubleshooting steps

## Notes

These are experimental setups for learning CI/CD patterns and should be adapted for your specific use case.
