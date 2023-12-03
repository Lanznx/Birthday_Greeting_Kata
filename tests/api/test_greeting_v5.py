from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_send_birthday_greetings_v5():
    request_data = {"current_date": "2023-08-08"}

    response = client.post("/greeting/v5/birthday", json=request_data)

    if response.status_code == 200:
        response_data = response.json()
        assert response_data["message"] == "Birthday greetings sent successfully"
        assert isinstance(response_data["greetings"], list)
        greeting = response_data["greetings"][0]
        assert "recipient_email" in greeting
        assert "subject" in greeting and greeting["subject"] == "Happy birthday!"
        assert "message" in greeting
    elif response.status_code == 404:
        response_data = response.json()
        assert response_data["detail"] == "No birthdays found today."
