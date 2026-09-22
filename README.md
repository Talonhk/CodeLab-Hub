# CodeLab Hub

CodeLab Hub is my personal engineering workspace for building, testing, and documenting software, DevOps, Kubernetes, infrastructure, and MLOps projects.

This repository reflects hands-on work across the software lifecycle: application development, automated testing, containerization, CI/CD, Kubernetes deployment, infrastructure automation, troubleshooting, and production-oriented validation.

My focus is not simply getting something to run, but understanding how it works, how it fails, and how to make it easier to test, deploy, troubleshoot, and maintain.

## Quick navigation

- `apps/` - Small application prototypes
- `devops/` - Kubernetes, CI/CD, Terraform, and lab automation
- `mlops/` - MLflow-based model workflows and API serving
- `practice/` - Language practice and coding exercises
- `archives/` - Legacy and reference material

## Featured projects

### Kubernetes Engineering Lab
**Location:** `devops/zarf-testing/`

A local Kubernetes engineering environment built around k3d and containerized development workflows.

Current work includes:

- Kubernetes cluster and namespace management
- Deployment validation and controlled apply workflows
- PowerShell automation for cluster operations
- Dev Container-based engineering environment
- Multi-language container environments
- Kubernetes service discovery and application deployment
- Validation, rollout checks, and restore workflows
- Troubleshooting and operational documentation

This lab is being used to deepen hands-on experience with Kubernetes-based software delivery and secure, repeatable engineering workflows.

---

### Python API and MLOps Service
**Location:** `mlops/mlops-quickstart-mlflow/`

A containerized Python project demonstrating a simplified model lifecycle from training through API-based inference.

Technologies and concepts include:

- Python
- FastAPI
- pytest
- MLflow
- Docker
- Kubernetes
- GitLab CI
- Model training and inference
- Health and prediction endpoints
- Automated API testing
- Environment-based configuration

The project has been validated through a containerized workflow, including training, inference, model artifact creation, and API smoke tests.

---

### CI/CD and Infrastructure Lab
**Location:** `devops/git-pipeline/`

An engineering lab for exploring automated build, test, infrastructure, and deployment workflows.

Current areas include:

- CI/CD pipeline design
- Kubernetes deployment manifests
- Terraform infrastructure examples
- Deployment automation
- Java application integration
- Pipeline testing and validation

This area is actively being developed as a broader commit-to-deployment workflow.

---

### Kubernetes CKA Lab
**Location:** `devops/kubernetes-cka/`

Hands-on Kubernetes exercises supporting deeper understanding of Kubernetes administration and application deployment.

Topics include:

- Pods and Deployments
- ConfigMaps and Secrets
- Resource requests and limits
- Namespaces and quotas
- Volumes and persistent storage
- Networking
- Init containers
- Multi-container workloads
- Services

The lab is also supporting ongoing Certified Kubernetes Administrator preparation.

## Quick start

```powershell
# Clone and move into the workspace
git clone <your-repo-url>
cd CodeLab-Hub

# Review key docs
Get-Content README.md
Get-Content PROJECTS.md
```

## Common run examples

```powershell
# C++
cd practice/languages/cpp
g++ .\fizzBuzz.cpp -o .\fizzBuzz.exe
.\fizzBuzz.exe

# Python
cd ..\python
python .\<script>.py

# Go
cd ..\go
go run .\main.go
```

## Technologies

### Software development

- Python
- Go
- Java
- JavaScript
- C++
- SQL
- REST APIs
- FastAPI
- Automated testing

### DevOps and platform engineering

- Git
- GitLab CI/CD
- Jenkins
- Docker
- Kubernetes
- Helm
- Terraform
- Infrastructure as Code
- Dev Containers
- Linux
- PowerShell
- Bash

### Observability and reliability

- Grafana
- Prometheus
- Splunk
- Logging
- Monitoring
- Troubleshooting
- Deployment validation
- Reliability-focused automation

### MLOps

- MLflow
- Model training and inference
- Model artifact handling
- Containerized model serving
- Kubernetes deployment
- API testing

## Repository structure

```text
CodeLab-Hub/
|
|-- apps/
|   `-- Small application prototypes
|
|-- devops/
|   |-- git-pipeline/
|   |-- kubernetes-cka/
|   |-- terraform/
|   `-- zarf-testing/
|
|-- mlops/
|   `-- mlops-quickstart-mlflow/
|
|-- practice/
|   `-- languages/
|       |-- cpp/
|       |-- go/
|       |-- java/
|       |-- javascript/
|       |-- php/
|       `-- python/
|
`-- archives/
	`-- Legacy and reference material
```

## Engineering approach

This repository is intentionally used as an engineering laboratory.

Projects generally follow a progression of:

1. Build or reproduce the problem.
2. Understand the system and dependencies.
3. Validate expected behavior.
4. Identify failure conditions.
5. Automate repetitive work.
6. Add testing and verification.
7. Document the solution and troubleshooting process.
8. Refactor or expand the project as understanding improves.

That process reflects the troubleshooting-focused approach used throughout software, DevOps, infrastructure, and technical support experience.

## Learning and practice

The `practice/` area contains coding exercises and smaller experiments across several programming languages.

These files are intentionally separated from larger engineering projects so that learning exercises, scratch work, and production-oriented projects remain easy to distinguish.

Current validated environments include:

- Python
- Go
- C++

Additional Java, JavaScript, and PHP work is maintained as part of ongoing development and experimentation.

## Current development

Current areas of focus include:

- Expanding Go development beyond introductory exercises into service-based applications
- Strengthening automated test coverage
- Improving Kubernetes lab validation
- Building more complete CI/CD workflows
- Expanding containerized development environments
- Deepening Kubernetes administration knowledge
- Continuing MLOps experimentation with model serving and deployment
- Improving documentation and reproducibility across projects

## Working conventions

- Keep active work in the appropriate domain folder.
- Keep scratch and exploratory work separated where possible.
- Add or update local README files when introducing non-obvious workflows.
- Prefer small, focused commits by topic.

## Important note on `learning-terraform`

`learning-terraform/` is intentionally kept as a separate forked project and is not merged into the main hub structure.

## Repository purpose

CodeLab Hub is not intended to represent a single finished product.

It is a working engineering environment that demonstrates continuous learning, experimentation, troubleshooting, validation, and improvement across software development and platform engineering technologies.

## Related docs

- `PROJECTS.md` for the complete section-by-section project guide
- `project-restructure-plan.md` for historical restructuring context
