from fastapi.testclient import TestClient
from app.main import app
from datetime import date

client = TestClient(app)


def test_member_creation():
    member_data = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "Male",
        "date_of_birth": str(date.today()),
        "email": "john.doe@example.com",
    }

    response = client.post("/member/", json=member_data)

    assert response.status_code == 201

    response_data = response.json()
    assert response_data["message"] == "Member created successfully"
    assert "user_id" in response_data
