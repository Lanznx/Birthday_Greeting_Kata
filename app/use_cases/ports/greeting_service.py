from abc import ABC, abstractmethod
from app.entities.member import Member


class IGreetingService(ABC):
    @abstractmethod
    def generate_greeting_message(self, member: Member) -> str:
        pass

    @abstractmethod
    def send_greeting(self, member: Member, message: str) -> None:
        pass
