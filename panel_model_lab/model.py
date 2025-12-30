from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

def train_model(df, alpha=1.0):
    X = df[["feature_1", "feature_2", "feature_3"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return y_test, y_pred, X_test
