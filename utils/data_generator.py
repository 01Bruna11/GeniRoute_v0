import pandas as pd
import numpy as np

def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)

    data = {
        "hora": np.random.randint(0, 24, n_samples),
        "volume_pedidos": np.random.randint(10, 300, n_samples),
        "chuva": np.random.choice([0, 1], n_samples),
        "dia_jogo": np.random.choice([0, 1], n_samples),
        "feriado": np.random.choice([0, 1], n_samples),
        "transito_nivel": np.random.randint(1, 6, n_samples),
    }

    df = pd.DataFrame(data)

    # Regra simulada de atraso (ground truth)
    df["atraso_min"] = (
        df["volume_pedidos"] * 0.05
        + df["chuva"] * 10
        + df["dia_jogo"] * 8
        + df["feriado"] * 12
        + df["transito_nivel"] * 6
        + np.random.normal(0, 5, n_samples)
    )

    return df


if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv("synthetic_data.csv", index=False)
    print("Dados sintéticos gerados com sucesso.")
