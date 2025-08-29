import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness Tracker" in response.data

def test_add_workout(client):
    response = client.post("/add", data={"workout": "Running", "duration": "30"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Running" in response.data
    assert b"30 mins" in response.data

def test_add_invalid_duration(client):
    response = client.post("/add", data={"workout": "Cycling", "duration": "abc"})
    assert response.status_code == 400
    assert b"Duration must be a number" in response.data
