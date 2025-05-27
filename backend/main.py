from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Latency API is running"}

@app.post("/predict-latency")
def predict_latency(data: dict):
    # TODO: Add ML model logic
    return {"latency_ms": 42, "anomaly": False}
