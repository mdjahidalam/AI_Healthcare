# import pandas as pd

# df = pd.read_csv("dataset/heart.csv")

# # print(df.head())

# # print("\n----------------")

# # print(df.info())

# # print("\n----------------")

# # print(df.describe())

# # print("\n----------------")

# # print(df.isnull().sum())

# # print("\n----------------")

# # print(df.columns)
# # print("Duplicate Rows :", df.duplicated().sum())

# # df = df.drop_duplicates()
# # df.to_csv("dataset/heart.csv", index=False)
# print(df.shape)
# print(df["target"].value_counts())
# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.figure(figsize=(12,8))

# sns.heatmap(
#     df.corr(),
#     annot=True,
#     cmap="coolwarm"
# )

# plt.show()

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# ==============================
# Load Dataset
# ==============================

df = pd.read_csv("dataset/heart.csv")

# ==============================
# Features and Target
# ==============================

X = df.drop("target", axis=1)

y = df["target"]

# ==============================
# Train Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==============================
# Feature Scaling
# ==============================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# ==============================
# Models
# ==============================

models = {

    "Logistic Regression":
    LogisticRegression(max_iter=1000),

    "Decision Tree":
    DecisionTreeClassifier(random_state=42),

    "Random Forest":
    RandomForestClassifier(
    n_estimators=500,
    max_depth=8,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
    ),

    "XGBoost":
    XGBClassifier(
        eval_metric="logloss",
        random_state=42
    )
}

# ==============================
# Model Comparison
# ==============================

results = []

for name, model in models.items():

    # Scaling only for Logistic Regression
    if name == "Logistic Regression":

        model.fit(X_train_scaled, y_train)

        predictions = model.predict(X_test_scaled)

    else:

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions
    )

    recall = recall_score(
        y_test,
        predictions
    )

    f1 = f1_score(
        y_test,
        predictions
    )

    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

# ==============================
# Results
# ==============================

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\n========== MODEL COMPARISON ==========\n")

print(results_df.sort_values(
    by="Accuracy",
    ascending=False
))