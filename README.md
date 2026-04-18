# 🚀 Customer Churn Prediction System (End-to-End ML Project)

---

## 🌍 Live Demo

🔗 API Docs (Swagger UI):  
https://churn-prediction-system-1-zffv.onrender.com/docs

---

## 📸 API Demo

![API Demo](https://github.com/user-attachments/assets/6cfea7b3-660d-4b4c-bf07-e0afacf7fcec)

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

## 🔧 Feature Engineering

- **AvgMonthlySpend**  
  → Captures customer spending behavior over time  

- **TenureGroup**  
  → Helps model non-linear churn patterns across customer lifecycle  

---

## 🤖 Model

- Algorithm: **Random Forest Classifier**  

- Used Pipeline and ColumnTransformer for:
  - Scaling numerical features  
  - Encoding categorical features  

- Prevents data leakage and ensures reproducibility  

---

## 📈 Model Performance

- ROC-AUC: ~0.83  
- Balanced performance across churn and non-churn classes  
- Custom threshold used to improve recall for churn class  

---

## 🧠 Key Business Insights

- Customers with **shorter tenure** are more likely to churn  
- **Month-to-month contracts** show higher churn rates  
- Customers using **electronic check payments** have higher churn probability  
- Higher **monthly charges** correlate with increased churn risk  

---

## 🧩 System Architecture

User → Streamlit UI → FastAPI → ML Pipeline → Prediction

---

## 🚀 API Endpoints

### GET /
Health check  

### POST /predict
Returns churn prediction  

---

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
