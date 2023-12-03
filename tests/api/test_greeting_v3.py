from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_send_birthday_greetings_v3():
    request_data = {"current_date": "2023-12-22"}
    response = client.post("/greeting/v3/birthday", json=request_data)

    if response.status_code == 200:
        response_data = response.json()
        assert (
            response_data["message"] == "Birthday greetings sent successfully"
        ), "Response message mismatch"
        assert isinstance(
            response_data["greetings"], list
        ), "Greetings should be a list"

        assert response_data["greetings"]

        for greeting in response_data["greetings"]:
            assert "recipient_email" in greeting
            assert "subject" in greeting
            assert "message" in greeting
            assert "picture_url" in greeting
            assert greeting["picture_url"].startswith("http")
    elif response.status_code == 404:
        response_data = response.json()
        assert response_data["detail"] == "No elder birthdays found today."
