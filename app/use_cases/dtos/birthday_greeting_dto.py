from pydantic import BaseModel


class BirthdayGreetingDTOV1(BaseModel):
    recipient_email: str
    subject: str
    message: str
