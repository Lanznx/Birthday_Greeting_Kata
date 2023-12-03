from abc import ABC, abstractmethod
from datetime import date
from typing import List
from app.entities.member import Member


class IMemberRepository(ABC):
    @abstractmethod
    def get_member(self, member_id: str) -> Member:
        pass

    @abstractmethod
    def create_member(self, member: Member) -> int:
        pass

    @abstractmethod
    def delete_member(self, member_id: str) -> int:
        pass

    @abstractmethod
    def get_members_with_birthday_today(self, today: date) -> List[Member]:
        pass
