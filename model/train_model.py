import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    df = pd.read_csv("synthetic_data.csv")

    features = [
        "hora",
        "volume_pedidos",
        "chuva",
        "dia_jogo",
        "feriado",
        "transito_nivel",
    ]

    X = df[features]
    y = df["atraso_min"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "model/atraso_predictor.pkl")

    print("Modelo treinado e salvo com sucesso.")


if __name__ == "__main__":
    train_model()
