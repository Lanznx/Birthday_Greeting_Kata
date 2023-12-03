from app.use_cases.ports.member_repository import IMemberRepository
from app.use_cases.ports.greeting_service import IGreetingService
from app.use_cases.dtos.birthday_greeting_dto import (
    BirthdayGreetingDTOV1,
    BirthdayGreetingDTOV2,
    BirthdayGreetingDTOV3,
)
from datetime import date
from typing import List, Union


class SendBirthdayGreetingUseCase:
    def __init__(
        self, member_repository: IMemberRepository, greeting_service: IGreetingService
    ):
        self.member_repository = member_repository
        self.greeting_service = greeting_service

    def execute(
        self, today: date
    ) -> List[
        Union[
            BirthdayGreetingDTOV1,
            BirthdayGreetingDTOV2,
            BirthdayGreetingDTOV3,
        ]
    ]:
        greetings = []
        members = self.member_repository.get_members_with_birthday_today(today)
        for member in members:
            message = self.greeting_service.generate_greeting_message(member)
            if not message:
                continue
            greeting = self.greeting_service.send_greeting(member, message)
            greetings.append(greeting)

        return greetings
