from abc import ABC, abstractmethod
from app.entities.member import Member
from app.use_cases.dtos.birthday_greeting_dto import BirthdayGreetingDTOV1
from typing import Union


class IGreetingService(ABC):
    @abstractmethod
    def generate_greeting_message(self, member: Member) -> str:
        pass

    @abstractmethod
    def send_greeting(
        self, member: Member, message: str
    ) -> Union[BirthdayGreetingDTOV1, None]:
        pass
