from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model and scaler
scaler, model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("inputs")

    if not features or len(features) != 11:
        return jsonify({"error": "Expected 11 input features"}), 400

    X = scaler.transform([features])

    prediction = model.predict(X)[0]
    return jsonify({"output": int(round(prediction))})

if __name__ == "__main__":
    app.run(debug=True)
