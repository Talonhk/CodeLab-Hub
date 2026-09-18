# CodeLab Hub — Local Project Restructure Plan

## Recommended umbrella project name

CodeLab Hub

This name works well because it covers:
- language practice
- infrastructure and DevOps learning
- Kubernetes and CI/CD experiments
- MLOps and model workflows
- small app projects

## Why this structure fits the current workspace

The current folders are not all the same type of project. Some are learning exercises, some are labs, some are infrastructure demos, and some are small app builds. If we leave them as-is, the GitHub repo becomes noisy and hard to maintain.

The best cleanup is to group them by purpose rather than by language alone.

## Proposed project grouping

### 1. Practice / Learning Lab
Purpose: day-to-day coding and algorithm practice.

Suggested folder layout:
- practice/
  - languages/
    - cpp/
    - go/
    - java/
    - javascript/
    - php/
    - python/
  - python-practice/
    - Teamtreehouse/
    - paging-mission-control-master/
  - general/
    - C++/
    - Golang/
    - JavaScript/
    - PHP/
    - Python_coding_practice/

Keep these separate from deployable or lab-focused work.

### 2. DevOps and Kubernetes Lab
Purpose: cluster, deployment, and K8s workflows.

Suggested folder layout:
- devops/
  - kubernetes-lab/
    - Kubernetes-CKA/
    - ZARF_testing/
  - ci-cd/
    - Git pipeline/
  - infrastructure/
    - Terraform/
    - learning-terraform/

This groups automation, cluster operations, and infrastructure exercises together.

### 3. MLOps / AI Project
Purpose: model training, ML pipelines, Docker packaging, and inference.

Suggested folder layout:
- mlops/
  - mlops-quickstart-mlflow/

This should remain independent because it is more application-like and deployment-oriented than a generic coding exercise.

### 4. Application Projects
Purpose: actual user-facing or service-oriented apps.

Suggested folder layout:
- apps/
  - Camera_app/

Anything reusable or user-facing should live here instead of in the general learning folders.

## Recommended repository flow

Before the GitHub cleanup, the workspace should be organized into these major buckets:

- practice/
- devops/
- mlops/
- apps/
- archives/

This keeps the repo readable and prevents mixed concerns from living in the same root.

## Recommended GitHub repo naming

Use the project name:
- CodeLab Hub

Suggested repo names:
- CodeLab-Hub
- code-lab-hub
- devops-practice-hub

Best choice: CodeLab-Hub

It is short, descriptive, and flexible enough to cover both learning and lab work.

## Migration order

1. Split projects by category first.
2. Move code into the correct project bucket.
3. Remove duplicate or stale folders.
4. Clean README files and add one high-level README for each project.
5. Keep a small archive folder for legacy experiments if needed.
6. Then do the final GitHub repository cleanup and push the consolidated structure.

## Recommended final layout

```text
CodeLab-Hub/
  README.md
  practice/
    languages/
    python-practice/
  devops/
    kubernetes-lab/
    ci-cd/
    terraform/
  mlops/
    mlops-quickstart-mlflow/
  apps/
    Camera_app/
  archives/
    legacy/
```

## Decision before moving files

The current workspace should not be cleaned up blindly. The correct approach is:
- keep labs grouped by purpose
- isolate code practice from deployable systems
- keep MLOps and platform engineering in their own project areas

This is the structure I recommend before any repo cleanup and file migration.
