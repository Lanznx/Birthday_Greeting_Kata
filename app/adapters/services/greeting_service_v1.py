from app.use_cases.ports.greeting_service import IGreetingService
from app.use_cases.dtos.birthday_greeting_dto import BirthdayGreetingDTOV1


class GreetingService(IGreetingService):
    def generate_greeting_message(self, member):
        return f"Happy birthday, dear {member.first_name}!"

    def send_greeting(self, member, message) -> BirthdayGreetingDTOV1:
        return BirthdayGreetingDTOV1(
            recipient_email=member.email,
            subject="Happy birthday!",
            message=message,
        )
