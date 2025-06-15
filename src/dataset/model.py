import pandas as pd 
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(X_path, y_path, output_path):
    X = pd.read_csv(X_path)
    y = pd.read_csv(y_path)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, output_path)

def test_model(model_path, X_test_path, y_test_path):
    model = joblib.load(model_path)
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path)
    y_pred = model.predict(X_test)

def predict_model(model_path, input_data_path):
    model = joblib.load(model_path)
    X = pd.read_csv(input_data_path)
    return model.predict(X)