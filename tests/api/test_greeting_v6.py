from fastapi.testclient import TestClient
from xml.etree import ElementTree as ET
from app.main import app

client = TestClient(app)


def test_send_birthday_greetings_v6():
    request_data = {"current_date": "2023-08-08"}

    response = client.post("/greeting/v6/birthday", json=request_data)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        assert root.tag == "root"

        message = root.find("message").text
        assert message == "Birthday greetings sent successfully"

        greetings = root.find("greetings")
        assert greetings is not None
        for greeting in greetings:
            assert greeting.find("recipient_email").text is not None
            assert greeting.find("subject").text == "Happy birthday!"
            assert greeting.find("message").text.startswith("Happy birthday, dear")

    elif response.status_code == 404:
        root = ET.fromstring(response.content)
        assert root.tag == "root"
        message = root.find("message").text
        assert message == "No birthdays found today"

        greetings = root.find("greetings")
        assert len(greetings) == 0
    else:
        assert False, f"Unexpected status code {response.status_code}"
