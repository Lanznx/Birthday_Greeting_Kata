from pydantic import BaseModel
from datetime import date


class BirthdayGreetingInputDTOV1(BaseModel):
    current_date: date


class BirthdayGreetingDTOV1(BaseModel):
    recipient_email: str
    subject: str
    message: str


class BirthdayGreetingOutputDTOV1(BaseModel):
    message: str
    greetings: list[BirthdayGreetingDTOV1]
