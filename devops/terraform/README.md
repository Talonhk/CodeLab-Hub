# Terraform Practice

A workspace for Terraform Infrastructure-as-Code exercises and learning.

## Contents

- `.devcontainer/` - Development container setup for consistent Terraform environments
- `Terraform.code-workspace` - VS Code workspace configuration

## Notes

This folder is currently a template or starting point for Terraform exercises. It includes dev container configuration for a reproducible local environment.

## Suggested next work

- Add Terraform configuration files (main.tf, variables.tf, outputs.tf)
- Define the target infrastructure (AWS, Azure, GCP, etc.)
- Create variable definitions and example terraform.tfvars
- Add a README with setup, build, and destroy instructions
- Document the infrastructure topology and design decisions

## Development environment

Use the included .devcontainer setup to get a consistent Terraform environment without manual setup:

```bash
# With VS Code Dev Containers extension:
# Open folder and click "Reopen in Container"
# Or via CLI:
docker build -t terraform-dev .devcontainer/Dockerfile
docker run -it -v $PWD:/workspace terraform-dev
```
