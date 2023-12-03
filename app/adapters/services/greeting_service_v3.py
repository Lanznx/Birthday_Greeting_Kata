from app.use_cases.ports.greeting_service import IGreetingService
from app.use_cases.dtos.birthday_greeting_dto import BirthdayGreetingDTOV3
from app.use_cases.ports.picture_service import IPictureService


class GreetingServiceV3(IGreetingService):
    def __init__(self, picture_service: IPictureService):
        self.picture_service = picture_service

    def generate_greeting_message(self, member):
        if member.age > 49:  # i define "age over 49" as "> 49"
            return f"Happy birthday, dear {member.first_name}!"

    def send_greeting(self, member, message) -> BirthdayGreetingDTOV3:
        return BirthdayGreetingDTOV3(
            recipient_email=member.email,
            subject="Happy birthday!",
            message=message,
            picture_url=self.picture_service.get_picture_url(),
        )
