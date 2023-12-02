from typing import List
from datetime import date
from app.entities.member import Member
from app.use_cases.ports.member_repository import IMemberRepository


class MySQLMemberRepository(IMemberRepository):
    def create_member(self, member: Member) -> Member:
        return 1233

    def get_members_with_birthday_today(self, today: date) -> List[Member]:
        pass
