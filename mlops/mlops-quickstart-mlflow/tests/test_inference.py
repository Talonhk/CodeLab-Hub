import joblib
import pytest
from fastapi.testclient import TestClient
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from src.app import app


@pytest.fixture()
def client(tmp_path, monkeypatch):
    data = load_iris()
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(data.data, data.target)

    model_path = tmp_path / "iris_rf.pkl"
    joblib.dump(model, model_path)
    monkeypatch.setenv("MODEL_PATH", str(model_path))

    return TestClient(app)


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_endpoint(client):
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )

    assert response.status_code == 200
    assert response.json()["prediction"] in {0, 1, 2}


def test_predict_returns_error_when_model_missing(monkeypatch):
    monkeypatch.setenv("MODEL_PATH", "models/does-not-exist.pkl")
    client = TestClient(app)

    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"error": "model not found at models/does-not-exist.pkl. Train first."}
