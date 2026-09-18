# CodeLab Hub – Complete Project Guide

Welcome to **CodeLab Hub**, a consolidated workspace for learning projects, infrastructure work, and small applications. This guide helps you navigate and understand the organized structure.

---

## 📚 Quick Navigation

### Practice & Learning
- **[practice/languages/](practice/languages/)** – Multi-language coding exercises (C++, Go, Java, JavaScript, PHP, Python)

### Application Projects
- **[apps/](apps/)** – Small app prototypes and tools

### Infrastructure & DevOps
- **[devops/](devops/)** – Kubernetes, CI/CD pipelines, Terraform, and lab environments

### Machine Learning Operations
- **[mlops/](mlops/)** – ML workflows, model training, and serving

### Archives
- **[archives/](archives/)** – Legacy and reference work

### Separate Projects
- **[learning-terraform/](../learning-terraform/)** – Forked Terraform learning repo (independent project)

---

## 📂 Detailed Breakdown

### 1. Practice & Learning

**Location:** `practice/languages/`

Multi-language learning exercises organized by programming language:

| Language | Status | Key Contents |
|----------|--------|--------------|
| **C++** | Active | Beginner exercises, scratch files separated |
| **Go** | Active | Introductory examples |
| **Java** | Active | Spring Boot REST API + CLI demo (real project) |
| **JavaScript** | Active | LeetCode-style challenges |
| **PHP** | Active | Ready for new exercises |
| **Python** | Active | Teamtreehouse + paging-mission-control challenge |

**Quick Start:**
- Browse any language folder for exercises and projects
- Check each language's README for specific guidance
- Python has scratch files separated in `Teamtreehouse/scratch/` for reference-only material

---

### 2. Applications

**Location:** `apps/`

Small, standalone application prototypes:

- **camera-app/** – React-based barcode scanner prototype
  - Main file: `barcode-scanner.jsx`
  - Status: Needs real scanner integration
  - Next: Wire to actual barcode scanning library (html5-qrcode, jsQR, etc.)

---

### 3. DevOps & Infrastructure

**Location:** `devops/`

Infrastructure code, cluster configuration, and automation:

#### git-pipeline/
CI/CD pipeline experiments with Kubernetes and Terraform
- Includes: Java app example, K8s manifests, pipeline scripts
- Next: Document full pipeline flow, add GitHub Actions or GitLab CI

#### kubernetes-cka/
Kubernetes CKA exam prep materials
- Collection of YAML manifests organized by concept
- Covers: Pods, Deployments, ConfigMaps, Secrets, Networking, Storage
- Next: Organize files by concept folder, create a lab runbook

#### terraform/
Terraform Infrastructure-as-Code workspace
- Includes: Dev container setup for consistent environments
- Next: Add actual Terraform configurations (pick a provider: AWS, Azure, GCP)

#### zarf-testing/
Local Kubernetes lab environment setup
- Scripts for k3s cluster management
- Launchers for different programming language environments
- Next: Document the lab setup and tear-down process

---

### 4. Machine Learning Operations

**Location:** `mlops/`

End-to-end ML workflow examples:

- **mlops-quickstart-mlflow/** – MLflow-based training and serving
  - Includes: Docker Compose, training/inference code, test suite
  - Next: Run locally, validate training and serving flow, document steps

---

### 5. Archives

**Location:** `archives/`

Older or transitional work kept for reference. Review periodically and decide whether items should be restored to active sections or removed.

---

## 🚀 Getting Started by Interest

### "I want to practice coding"
→ Go to `practice/languages/` and pick a language  
→ Each language folder has a README with current exercises  
→ Python and Java have the most complete examples

### "I want to explore infrastructure"
→ Browse `devops/` sections  
→ Start with **kubernetes-cka** for learning concepts  
→ Try **terraform** for IaC hands-on work  
→ Use **zarf-testing** for local k3s lab environment

### "I want to build an app"
→ Check `apps/camera-app` for a React prototype  
→ This is a template showing component structure; needs real functionality

### "I want to learn MLOps"
→ Go to `mlops/mlops-quickstart-mlflow/`  
→ Follow the README for setup and local validation

---

## 📋 Recommended Next Actions

### By Section Priority

1. **Python Practice** (High value)
   - Test and validate all Teamtreehouse exercises
   - Document any failures or environment setup needs
   - Create a runbook for running the paging-mission-control challenge

2. **Java Project** (Complete & testable)
   - Verify it builds and runs locally
   - Test REST API endpoints
   - Document build, test, and run commands

3. **Kubernetes Lab** (Learning focused)
   - Organize manifests into concept folders
   - Create a guided lab progression
   - Document how to deploy and verify each example

4. **MLOps Workflow** (Experimental)
   - Run the training and serving flow locally
   - Document expected outputs and metrics
   - Add a quick reference for MLflow commands

5. **Git Pipeline** (Structural)
   - Document the full pipeline from commit to deployment
   - Add GitHub Actions or GitLab CI example
   - Create a test harness

---

## 🔧 Common Tasks

### Run a Practice Exercise
```bash
# C++
cd practice/languages/cpp
g++ filename.cpp -o filename.exe
./filename.exe

# Python
cd practice/languages/python
python script.py

# Java
cd practice/languages/java
mvn clean compile
mvn exec:java -Dexec.mainClass="com.codinglab.App"
```

### Start a Local Lab
```bash
cd devops/zarf-testing
# Review README for setup steps
# Use launchers/python.ps1, launchers/go.ps1, etc.
```

### Explore Kubernetes
```bash
cd devops/kubernetes-cka
# Pick a manifest and review it
# Deploy to local cluster (minikube, kind, k3s)
kubectl apply -f filename.yaml
```

---

## 📖 Repository Standards

- Each section has a **README.md** with overview and suggested next work
- Each major project includes setup and usage instructions
- **Practice files** are organized by language under `practice/languages/`
- **Scratch/draft files** are in `*/scratch/` folders, separate from active exercises
- **Git history** is preserved and clean—view logs to understand project evolution

---

## 🔗 Related Documentation

- [Main Repository README](README.md)
- [Project Restructure Plan](project-restructure-plan.md) (historical planning document)

---

## 📝 Notes

- The **learning-terraform** repo at the root level is a separate, forked project kept independent from the main CodeLab Hub
- All major projects are committed to Git; your work is version-controlled
- Use the suggested next actions in each section's README to guide your exploration

---

**Last Updated:** 2026-09-18  
**Status:** Organized and documented. Ready for active use and validation.
