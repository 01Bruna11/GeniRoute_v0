import joblib
import pandas as pd

model = joblib.load("model/atraso_predictor.pkl")

def predict_delay(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return round(prediction, 2)
