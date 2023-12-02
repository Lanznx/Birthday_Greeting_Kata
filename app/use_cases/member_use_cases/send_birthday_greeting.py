from app.use_cases.ports.member_repository import IMemberRepository
from app.use_cases.ports.greeting_service import IGreetingService


class SendBirthdayGreetingUseCase:
    def __init__(
        self, member_repository: IMemberRepository, greeting_service: IGreetingService
    ):
        self.member_repository = member_repository
        self.greeting_service = greeting_service

    def execute(self):
        members = self.member_repository.get_members_with_birthday_today()
        for member in members:
            message = self.greeting_service.generate_greeting_message(member)
            self.greeting_service.send_greeting(member, message)
