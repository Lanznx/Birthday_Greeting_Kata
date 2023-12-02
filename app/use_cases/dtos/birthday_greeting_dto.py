from pydantic import BaseModel


class BirthdayGreetingDTO(BaseModel):
    recipient_email: str
    subject: str
    message: str
