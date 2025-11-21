from fastapi import FastAPI
import joblib
import numpy as np


model= joblib.load("app/random_forest_model.joblib")


class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Species Prediction API!"}

@app.post("/predict/")
def predict(data:dict):
    """
    Predict the class of iris species given features.
    Args:
        data (dict): A dictionary containing the features of the iris flower.
    Returns:
        dict: A dictionary containing the predicted class.
    Example input:
        {"features": [5.1, 3.5, 1.4, 0.2]}
    Example output:
        {"predicted_class": "setosa"}
    """
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    predicted_class = class_names[prediction][0]
    return {"predicted_class": predicted_class}