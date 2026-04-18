# 🚀 Customer Churn Prediction System (End-to-End ML Project)

## 📌 Overview
This project is an end-to-end machine learning system designed to predict customer churn using real-world telecom data.

It covers the full ML lifecycle:
- Data preprocessing & feature engineering  
- Model training using scikit-learn  
- Pipeline creation to avoid data leakage  
- API development with FastAPI  
- Deployment on cloud (Render)  

👉 The system provides **real-time churn predictions via a live API**

---

## 🌍 Live Demo

🔗 API Docs (Swagger UI):  
https://churn-prediction-system-1-zffv.onrender.com/docs

---

## ⚙️ Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- FastAPI  
- Uvicorn  
- Docker  
- Render (Cloud Deployment)  
- Streamlit (Frontend UI)  

---

## 🧠 Problem Statement

Customer churn is a critical problem for subscription-based businesses.  
This project predicts whether a customer will churn based on behavioral and service usage features.

---

## 📊 Dataset

- Telco Customer Churn Dataset (Kaggle)  
- Features include:
  - Tenure  
  - Monthly Charges  
  - Contract Type  
  - Internet Service  
  - Payment Method  

---

## 🔧 Feature Engineering

Key engineered features:

- **AvgMonthlySpend**  
  → Captures customer spending behavior over time  

- **TenureGroup**  
  → Helps model non-linear churn patterns across customer lifecycle  

---

## 🤖 Model

- Algorithm: **Random Forest Classifier**  
- Used `Pipeline` and `ColumnTransformer` for:
  - Scaling numerical features  
  - Encoding categorical features  
- Prevents data leakage and ensures reproducibility  

---

## 📈 Model Performance

- ROC-AUC: ~0.83  
- Balanced performance across churn and non-churn classes  
- Custom threshold used to improve recall for churn class  

---

## 🧩 System Architecture
User → Streamlit UI → FastAPI → ML Pipeline → Prediction


---

## 🚀 API Endpoints

### `GET /`
Health check

### `POST /predict`
Returns churn prediction

#### Example Input:
```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70,
  "TotalCharges": 350
}
```

## 🐳 Docker Support

The application is containerized using Docker for consistent and reproducible deployment.

---

## 💡 Key Learnings

- Building production-ready ML pipelines  
- Handling real-world data inconsistencies  
- Designing APIs for ML models  
- Deploying ML systems to cloud platforms  
- Structuring end-to-end data science projects  

---

## 📌 Future Improvements

- Hyperparameter tuning  
- Model explainability (SHAP / LIME)  
- Enhanced UI for better user experience  
- Monitoring and logging  

---

## 👨‍💻 Author

**Sarthak Gandhi**  
 
