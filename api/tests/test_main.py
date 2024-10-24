import pytest
from fastapi.testclient import TestClient
from mongomock import MongoClient
from main import app  

@pytest.fixture(scope="module")
def client():
    app.dependency_overrides[get_db] = lambda: MongoClient()
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="function", autouse=True)
def mock_mongo():
    client = MongoClient()
    app.state.db = client["test_db"]
    yield
    app.state.db.drop_collection("calculator")

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_get_route(client):
    response = client.get("/api/calculator")
    assert response.status_code == 200
    data = response.json()
    assert data == []

def test_post_route(client):
    response = client.post("/api/calculator", json={"equation": [4, 1, '+'], "date": "2024-10-09"})
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == {"equation": "4 1 +", "result": 5, "date":  "2024-10-09"}

def test_get_route_with_data(client):
    response = client.get("/api/calculator")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    data_id = data[0]["id"]
    assert data == [{"id": data_id, "equation": "4 1 +", "result": 5, "date":  "2024-10-09"}]

def test_download_csv(client):
    response = client.get("/api/calculator/csv")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv; charset=utf-8"
    assert "attachment; filename=data.csv" in response.headers["content-disposition"]
    csv_content = response.content.decode("utf-8")
    expected_csv = "Equation,Result,Date\n4 1 +,5,2024-10-09\n"
    assert csv_content == expected_csv

def test_delete_rout(client):
    response = client.get("/api/calculator")
    data = response.json()
    data_id = data[0]["id"]
    delete = client.delete("/api/calculator/" + data_id)
    assert delete.status_code == 200
    assert delete.json() == "Item deleted successfully"