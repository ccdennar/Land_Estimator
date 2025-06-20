from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('models/regression_model.pkl')

@app.post("/predict")
async def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"predicted_value": float(prediction[0])}