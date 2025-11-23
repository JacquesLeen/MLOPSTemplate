"""
Fixtures for testing the Model API
"""

import pytest
from app.server import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """Create a test client"""
    return TestClient(app)