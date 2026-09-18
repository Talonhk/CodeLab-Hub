# MLOps Quickstart (MLflow + Docker + FastAPI + K8s)

A compact, reproducible starter showing **train → track → register → serve → (optionally) deploy**.

## What this shows
- Reproducible training with **MLflow** (params, metrics, artifacts)
- Simple **model registry** pattern (local) and staged promotion idea
- Containerized **training** and **inference** via Docker
- Minimal **FastAPI** service for inference
- Optional **Kubernetes (K8s)** manifests + notes for canary/rollback
- Stub **CI** config (GitLab) for lint/test/build

## Quickstart (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mlflow ui --backend-store-uri sqlite:///mlruns.db --default-artifact-root ./mlruns
python src/train.py --n-estimators 100 --max-depth 3
python src/inference.py --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2
uvicorn src.app:app --reload --port 8000
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json"   -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

## Docker (local)
```bash
docker build -f docker/Dockerfile.train -t mlops-train:latest .
docker run --rm -v $(pwd)/models:/app/models mlops-train:latest
docker build -f docker/Dockerfile.serve -t mlops-serve:latest .
docker run --rm -p 8000:8000 -v $(pwd)/models:/app/models mlops-serve:latest
```

## Kubernetes (kind/minikube)
```bash
kubectl apply -f infra/k8s/deployment.yaml
kubectl apply -f infra/k8s/service.yaml
```

## CI (GitLab)
See `ci/gitlab-ci.yml` for a simple pipeline: lint → test → build images.
