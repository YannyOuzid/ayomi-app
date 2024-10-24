import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient
from main import app
import os

@pytest.fixture(scope="module")
def test_db():
    mongo_test_uri = os.getenv("MONGO_TEST_URI", "mongodb://localhost:27017/test_db")
    client = MongoClient(mongo_test_uri)
    db = client.test_db
    yield db
    client.drop_database("test_db")

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def override_get_db():
    return test_db

app.dependency_overrides[override_get_db] = test_db

def test_get_route(client):
    response = client.get("/api/calculator")
    assert response.status_code == 200
    data = response.json()
    assert data == []

def test_post_route(client):
    response = client.post("/api/calculator", json={"equation": [4, 1, '+'], "date": "2024-10-09"})
    assert response.status_code == 200