import streamlit as st
import requests

st.title("📊 Customer Churn Prediction")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider("Tenure (months)", 0, 72)

phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["Yes", "No"])

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

payment = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

monthly = st.number_input("Monthly Charges", value=70.0)
total = st.number_input("Total Charges", value=300.0)

# Predict
if st.button("Predict Churn"):
    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['churn_prediction']}")
        st.info(f"Probability: {result['churn_probability']:.2f}")
    else:
        st.error("Error connecting to API")