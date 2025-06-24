import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import json
from datetime import datetime

# Load dataset
df = pd.read_csv("data/outfit_dataset.csv")

# Encode target
le = LabelEncoder()
df["outfit_encoded"] = le.fit_transform(df["outfit"])

X = df[["temp", "humidity", "wind_speed"]]
y = df["outfit_encoded"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/outfit_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

# Save context
context = {
    "model_version": "1.0",
    "accuracy": float(model.score(X_test, y_test)),
    "features": ["temp", "humidity", "wind_speed"],
    "label_map": {str(k): int(v) for k, v in zip(le.classes_, le.transform(le.classes_))},
    "date_trained": datetime.now().isoformat()
}
os.makedirs("context", exist_ok=True)
with open("context/context.json", "w") as f:
    print('DEBUG: context types:')
    for k, v in context.items():
        print(f"{k}: {type(v)}")
    print('DEBUG: label_map:', context["label_map"])
    json.dump(context, f, indent=4)
