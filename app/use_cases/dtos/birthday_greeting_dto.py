from pydantic import BaseModel
from datetime import date


class BirthdayGreetingInputDTO(BaseModel):
    current_date: date


# v1
class BirthdayGreetingDTOV1(BaseModel):
    recipient_email: str
    subject: str
    message: str


class BirthdayGreetingOutputDTOV1(BaseModel):
    message: str
    greetings: list[BirthdayGreetingDTOV1]


# v2
class BirthdayGreetingDTOV2(BaseModel):
    recipient_email: str
    subject: str
    message: str


class BirthdayGreetingOutputDTOV2(BaseModel):
    message: str
    greetings: list[BirthdayGreetingDTOV2]


# v3
class BirthdayGreetingDTOV3(BaseModel):
    recipient_email: str
    subject: str
    message: str
    picture_url: str


class BirthdayGreetingOutputDTOV3(BaseModel):
    message: str
    greetings: list[BirthdayGreetingDTOV3]


# v4
class BirthdayGreetingDTOV4(BaseModel):
    recipient_email: str
    subject: str
    message: str


class BirthdayGreetingOutputDTOV4(BaseModel):
    message: str
    greetings: list[BirthdayGreetingDTOV4]
