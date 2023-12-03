from fastapi.testclient import TestClient
from app.main import app
from datetime import date

client = TestClient(app)


def test_send_birthday_greetings_v1():
    today = date.today()
    request_data = {"current_date": today.isoformat()}

    response = client.post("/greeting/v1/birthday", json=request_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Birthday greetings sent successfully"
    assert isinstance(response_data["greetings"], list)
    if response_data["greetings"]:
        greeting = response_data["greetings"][0]
        assert "recipient_email" in greeting
        assert "subject" in greeting
        assert "message" in greeting
