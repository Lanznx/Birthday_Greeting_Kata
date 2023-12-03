from typing import List
from datetime import date
from app.entities.member import Member
from app.use_cases.ports.member_repository import IMemberRepository
from app.infra.db.model import MemberModel
from app.infra.db.database import SessionLocal


class MySQLMemberRepository(IMemberRepository):
    def create_member(self, member: Member) -> int:
        with SessionLocal() as session:
            member_model = MemberModel(
                first_name=member.first_name,
                last_name=member.last_name,
                gender=member.gender,
                date_of_birth=member.date_of_birth,
                email=member.email,
            )
            session.add(member_model)
            session.commit()
            session.refresh(member_model)
        return member_model.id

    def get_members_with_birthday_today(self, today: date) -> List[Member]:
        pass
