from fastapi.testclient import TestClient
from app.main import app
from datetime import date

client = TestClient(app)


def test_send_birthday_greetings_v2():
    today = date.today()
    request_data = {"current_date": "2023-08-08"}

    response = client.post("/greeting/v2/birthday", json=request_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Birthday greetings sent successfully"
    assert isinstance(response_data["greetings"], list)
    if response_data["greetings"]:
        greeting = response_data["greetings"][0]
        assert "recipient_email" in greeting
        assert "subject" in greeting
        assert "message" in greeting

        if "White Wine, iPhone X" in greeting["message"]:
            assert "20% off" in greeting["message"]
        elif "Cosmetic, LV Handbags" in greeting["message"]:
            assert "50% off" in greeting["message"]
