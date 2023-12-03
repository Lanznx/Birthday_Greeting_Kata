from xml.etree.ElementTree import Element, SubElement, tostring
from app.use_cases.dtos.birthday_greeting_dto import BirthdayGreetingOutputDTOV1
from app.use_cases.ports.presenter import IPresenter


class XmlPresenter(IPresenter):
    def present_birthday_greeting(self, data: BirthdayGreetingOutputDTOV1) -> str:
        root = Element("root")

        message_element = SubElement(root, "message")
        message_element.text = data.message

        greetings_element = SubElement(root, "greetings")
        for greeting in data.greetings:
            greeting_element = SubElement(greetings_element, "greeting")

            recipient_email_element = SubElement(greeting_element, "recipient_email")
            recipient_email_element.text = greeting.recipient_email

            subject_element = SubElement(greeting_element, "subject")
            subject_element.text = greeting.subject

            message_element = SubElement(greeting_element, "message")
            message_element.text = greeting.message

        return tostring(root, encoding="unicode")
