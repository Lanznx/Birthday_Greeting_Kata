import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import date

client = TestClient(app)


class TestMemberLifecycle:
    member_id = None

    def test_member_creation(self):
        member_data = {
            "first_name": "John",
            "last_name": "Doe",
            "gender": "Male",
            "date_of_birth": "1990-01-01",
            "email": "unique.email111@example.com",
        }
        response = client.post("/member/", json=member_data)
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["message"] == "Member created successfully"
        TestMemberLifecycle.member_id = response_data["member_id"]

    def test_member_deletion(self):
        if TestMemberLifecycle.member_id is None:
            pytest.skip("Skipping deletion test as no member was created")
        assert TestMemberLifecycle.member_id is not None
        delete_response = client.delete(f"/member/{TestMemberLifecycle.member_id}")
        assert delete_response.status_code == 200
        delete_response_data = delete_response.json()
        assert delete_response_data["message"] == "Member deleted successfully"
        assert delete_response_data["member_id"] == TestMemberLifecycle.member_id

    def test_member_creation_with_future_birth_date(self):
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

    def test_member_creation_with_invalid_email(self):
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
