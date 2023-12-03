from app.use_cases.ports.greeting_service import IGreetingService
from app.use_cases.dtos.birthday_greeting_dto import BirthdayGreetingDTOV4


class GreetingServiceV4(IGreetingService):
    def generate_greeting_message(self, member):
        return f"Happy birthday, dear {member.first_name}, {member.last_name}!"

    def send_greeting(self, member, message) -> BirthdayGreetingDTOV4:
        return BirthdayGreetingDTOV4(
            recipient_email=member.email,
            subject="Happy birthday!",
            message=message,
        )
