import joblib
import pandas as pd

# Load Model & Scaler
model = joblib.load("saved_models/heart_model.pkl")
scaler = joblib.load("saved_models/scaler.pkl")


def predict_heart(data: dict):

    # Patient ID ko alag rakh lo (database ke liye)
    patient_id = data.pop("patient_id", None)

    # DataFrame banao sirf ML features ke saath
    df = pd.DataFrame([data])

    # Model training ke same order me columns
    df = df[
        [
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal",
        ]
    ]

    # Scale Data
    scaled_data = scaler.transform(df)

    # Prediction
    prediction = model.predict(scaled_data)[0]

    # Probability
    probability = model.predict_proba(scaled_data)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:

        return {
            "prediction": "Heart Disease",
            "risk_level": "High",
            "confidence": confidence
        }

    else:

        return {
            "prediction": "No Heart Disease",
            "risk_level": "Low",
            "confidence": confidence
        }