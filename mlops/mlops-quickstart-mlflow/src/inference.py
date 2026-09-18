import argparse
import joblib
import numpy as np
import os

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model-path", default="models/iris_rf.pkl")
    p.add_argument("--sepal-length", type=float, required=True)
    p.add_argument("--sepal-width", type=float, required=True)
    p.add_argument("--petal-length", type=float, required=True)
    p.add_argument("--petal-width", type=float, required=True)
    return p.parse_args()

def main():
    args = parse_args()
    if not os.path.exists(args.model_path):
        raise FileNotFoundError(f"Model not found: {args.model_path}. Run training first.")

    model = joblib.load(args.model_path)
    X = np.array([[
        args.sepal_length, args.sepal_width,
        args.petal_length, args.petal_width
    ]])
    pred = model.predict(X)[0]
    print(f"prediction={int(pred)}")

if __name__ == "__main__":
    main()
