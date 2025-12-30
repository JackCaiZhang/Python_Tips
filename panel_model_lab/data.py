import numpy as np
import pandas as pd

def load_data(n=2000):
    np.random.seed(42)

    X = np.random.normal(0, 1, (n, 3))
    coef = np.array([3.5, -2.0, 1.2])

    noise = np.random.normal(0, 1.5, n)
    y = X @ coef + noise

    df = pd.DataFrame(X, columns=["feature_1", "feature_2", "feature_3"])
    df["target"] = y

    return df
