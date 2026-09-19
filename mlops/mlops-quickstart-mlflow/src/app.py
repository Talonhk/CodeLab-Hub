#!/usr/bin/env python3

import os

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()


def get_model_path() -> str:
    return os.getenv("MODEL_PATH", "models/iris_rf.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(feat: Features):
    model_path = get_model_path()
    if not os.path.exists(model_path):
        return {"error": f"model not found at {model_path}. Train first."}
    model = joblib.load(model_path)
    X = np.array([[feat.sepal_length, feat.sepal_width, feat.petal_length, feat.petal_width]])
    pred = int(model.predict(X)[0])
    return {"prediction": pred}
