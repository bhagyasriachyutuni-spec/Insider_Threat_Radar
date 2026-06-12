import joblib
import pandas as pd

model = joblib.load("models/random_forest.pkl")

feature_cols = [
    'total_emails','total_attachments','avg_email_size',
    'off_hour_emails','weekend_emails',
    'O','C','E','A','N'
]

def predict_user(input_data):
    df = pd.DataFrame([input_data], columns=feature_cols)

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    label = "Suspicious" if pred == 1 else "Normal"
    score = round(prob * 100, 2)

    if score < 40:
        level = "Low"
    elif score < 70:
        level = "Medium"
    else:
        level = "High"

    return label, score, level