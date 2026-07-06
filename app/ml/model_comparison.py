import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("dataset/heart.csv")

# Features & Target
X = df.drop("target", axis=1)
y = df["target"]

# ===============================
# Train Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ===============================
# Feature Scaling
# ===============================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ===============================
# Train Logistic Regression
# ===============================

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X_train_scaled, y_train)

# ===============================
# Prediction
# ===============================

y_pred = model.predict(X_test_scaled)

# ===============================
# Evaluation
# ===============================

print("=" * 50)
print("Logistic Regression Performance")
print("=" * 50)

print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score : {f1_score(y_test, y_pred):.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ===============================
# Save Model
# ===============================

os.makedirs("saved_models", exist_ok=True)

joblib.dump(model, "saved_models/heart_model.pkl")
joblib.dump(scaler, "saved_models/scaler.pkl")

print("\nModel Saved Successfully!")
print("Scaler Saved Successfully!")