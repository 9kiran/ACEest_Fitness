import pytest
from aceest_fitness.app import app

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

def test_add_workout_missing_fields(client):
    response = client.post("/add", data={"workout": "", "duration": ""})
    assert response.status_code == 400
    assert b"Error: Workout and duration required" in response.data

def test_multiple_workouts(client):
    client.post("/add", data={"workout": "Running", "duration": "20"})
    client.post("/add", data={"workout": "Cycling", "duration": "40"})
    response = client.get("/")
    assert b"Running" in response.data
    assert b"Cycling" in response.data

def test_large_duration(client):
    response = client.post("/add", data={"workout": "Swimming", "duration": "300"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"300 mins" in response.data

def test_decimal_duration(client):
    response = client.post("/add", data={"workout": "Yoga", "duration": "45.5"})
    assert response.status_code == 400
    assert b"Duration must be a number" in response.data

def test_workouts_persist_in_memory(client):
    client.post("/add", data={"workout": "Jumping Jacks", "duration": "10"})
    response = client.get("/")
    assert b"Jumping Jacks" in response.data
