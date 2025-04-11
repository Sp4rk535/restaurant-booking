from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_table():
    response = client.post("/tables/", json={"name": "Table 1", "seats": 4, "location": "window"})
    assert response.status_code == 200
    assert response.json()["name"] == "Table 1"

def test_create_reservation_conflict():
    client.post("/tables/", json={"name": "Table 1", "seats": 4, "location": "window"})
    reservation = {
        "customer_name": "John",
        "table_id": 1,
        "reservation_time": "2025-04-12T12:00:00",
        "duration_minutes": 60
    }
    client.post("/reservations/", json=reservation)
    response = client.post("/reservations/", json=reservation)
    assert response.status_code == 400