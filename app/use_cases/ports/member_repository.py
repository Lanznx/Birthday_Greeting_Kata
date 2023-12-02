from abc import ABC, abstractmethod
from typing import List
from app.entities.member import Member


class IMemberRepository(ABC):
    @abstractmethod
    def create_member(self, member: Member) -> Member:
        pass

    @abstractmethod
    def get_members_with_birthday_today(self) -> List[Member]:
        pass
