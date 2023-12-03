from app.use_cases.ports.greeting_service import IGreetingService
from app.use_cases.dtos.birthday_greeting_dto import BirthdayGreetingDTOV2


class GreetingServiceV2(IGreetingService):
    def generate_greeting_message(self, member) -> str:
        if member.gender == "Male":
            return f"Happy birthday, dear {member.first_name}!\nWe offer special discount 20% off for the following items:\nWhite Wine, iPhone X"
        elif member.gender == "Female":
            return f"Happy birthday, dear {member.first_name}!\nWe offer special discount 50% off for the following items:\nCosmetic, LV Handbags"

    def send_greeting(self, member, message) -> BirthdayGreetingDTOV2:
        return BirthdayGreetingDTOV2(
            recipient_email=member.email,
            subject="Happy birthday!",
            message=message,
        )
