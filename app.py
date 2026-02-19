import pandas as pd
from flask import Flask, render_template, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

app = Flask(__name__)

model = None

def train_model():
    global model
    try:
        if not os.path.exists('customer_churn.csv'):
            print("Dataset not found! Please place 'customer_churn.csv' in the same directory.")
            return False

        df = pd.read_csv('customer_churn.csv')
        
        # Features & Target used in notebook: tenure, MonthlyCharges
        X = df[['tenure', 'MonthlyCharges']]
        y = df['Churn']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        print("Model trained successfully.")
        return True
    except Exception as e:
        print(f"Error training model: {e}")
        return False

@app.route('/')
def index():
    if model is None:
        train_model()
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        if not train_model():
            return jsonify({'error': 'Model failed to train. Check console.'}), 500

    try:
        data = request.json
        tenure = float(data.get('tenure'))
        monthly_charges = float(data.get('monthly_charges'))
        
        # Prediction
        # Returns ['No'] or ['Yes']
        prediction = model.predict([[tenure, monthly_charges]])[0]
        probability = model.predict_proba([[tenure, monthly_charges]])[0]
        
        # Probability of Churn (Yes is usually index 1 if sorted, let's check classes_)
        # classes_ are usually sorted, so 'No' is 0, 'Yes' is 1.
        churn_prob = probability[1] if model.classes_[1] == 'Yes' else probability[0]
        
        return jsonify({
            'churn_prediction': prediction,
            'churn_probability': f"{churn_prob * 100:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    train_model()
    app.run(debug=True, port=5003)
