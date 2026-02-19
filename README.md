# 📉 Customer Churn Predictor

This application predicts customer churn based on metrics like tenure and monthly charges, using a Random Forest model trained on the Telco Customer Churn dataset.

## ✨ Features

*   **Churn Prediction**: Predicts if a customer is likely to leave ("Yes" or "No").
*   **Confidence Score**: Provides the probability of churn.
*   **Simple Input**: Only requires `Tenure` (months) and `Monthly Charges` ($).

## 🚀 How to Run

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/customer-churn-predictor.git
    cd customer-churn-predictor
    ```

2.  **Ensure Dataset Exists**:
    Place `customer_churn.csv` in the root directory.

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App**:
    ```bash
    python app.py
    ```

5.  **Open in Browser**:
    Go to `http://127.0.0.1:5003`

## ☁️ Deployment

Ready for deployment on platforms like Render or Heroku using the included `Procfile`.
