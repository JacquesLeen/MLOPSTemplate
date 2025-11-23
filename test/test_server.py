"""
Testing Module for Model API
"""

from app.server import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_predict():
    response = client.post("/predict/", json={"features": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert "predicted_class" in response.json()