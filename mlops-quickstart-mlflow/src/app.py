from fastapi import FastAPI
from pydantic import BaseModel
import joblib, os, numpy as np

MODEL_PATH = os.getenv("MODEL_PATH", "models/iris_rf.pkl")

class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(feat: Features):
    if not os.path.exists(MODEL_PATH):
        return {"error": f"model not found at {MODEL_PATH}. Train first."}
    model = joblib.load(MODEL_PATH)
    X = np.array([[feat.sepal_length, feat.sepal_width, feat.petal_length, feat.petal_width]])
    pred = int(model.predict(X)[0])
    return {"prediction": pred}
