import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class MonetizationModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        """Train the revenue prediction model."""
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, features):
        """Predict revenue score."""
        features = np.array(features).reshape(1, -1)
        return self.model.predict(features)[0]

    def evaluate(self, X_test, y_test):
        """Return RMSE score."""
        predictions = self.model.predict(X_test)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        return rmse

    def save(self, path="model.pkl"):
        """Save trained model."""
        joblib.dump(self.model, path)

    def load(self, path="model.pkl"):
        """Load saved model."""
        self.model = joblib.load(path)
        return self.model


if __name__ == "__main__":
    print("Model module loaded.")