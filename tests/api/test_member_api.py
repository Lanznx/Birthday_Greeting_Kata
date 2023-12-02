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
    assert "member_id" in response_data


def test_member_creation_with_missing_data():
    member_data = {
        "first_name": "John",
        # "last_name" is missing
        "gender": "Male",
        "date_of_birth": str(date.today()),
        "email": "john.doe@example.com",
    }

    response = client.post("/member/", json=member_data)

    assert response.status_code == 422
    assert "detail" in response.json()


def test_member_creation_with_future_birth_date():
    future_date = str(date.today().replace(year=date.today().year + 1))
    member_data = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "Male",
        "date_of_birth": future_date,
        "email": "john.doe@example.com",
    }

    response = client.post("/member/", json=member_data)

    assert response.status_code == 422
    assert "detail" in response.json()


def test_member_creation_with_invalid_email():
    member_data = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "Male",
        "date_of_birth": str(date.today()),
        "email": "invalid-email",
    }

    response = client.post("/member/", json=member_data)

    assert response.status_code == 422
    assert "detail" in response.json()
