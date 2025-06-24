import joblib
from get_weather import fetch_weather

def predict_outfit(weather):
    model = joblib.load("models/outfit_model.pkl")
    le = joblib.load("models/label_encoder.pkl")

    X_input = [[weather["temp"], weather["humidity"], weather["wind_speed"]]]
    y_pred = model.predict(X_input)[0]
    return le.inverse_transform([y_pred])[0]
