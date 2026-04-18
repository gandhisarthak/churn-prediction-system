from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os



app = FastAPI()

# Load model (simple path)
model = joblib.load("model/churn_pipeline.pkl")


@app.get("/")
def home():
    return {"message": "Churn Prediction API is running 🚀"}

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
def predict(data: CustomerData):
    df = pd.DataFrame([data.dict()])

    df["AvgMonthlySpend"] = df["TotalCharges"] / (df["tenure"] + 1)

    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 60, 100],
        labels=["0-1yr", "1-2yr", "2-4yr", "4-5yr", "5+yr"]
    )

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    }