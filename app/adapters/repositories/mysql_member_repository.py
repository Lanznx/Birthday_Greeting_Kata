from sqlalchemy import extract
from typing import List
from datetime import date
from app.entities.member import Member
from app.use_cases.ports.member_repository import IMemberRepository
from app.infra.db.mysql.model import MemberModel
from app.infra.db.mysql.database import SessionLocal


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

    def get_member(self, member_id: str) -> Member:
        with SessionLocal() as session:
            session_member = session.query(MemberModel).filter_by(id=member_id).first()
            if session_member is None:
                return None
            return self._convert_to_member(session_member)

    def delete_member(self, member_id: str) -> int:
        with SessionLocal() as session:
            session_member = session.query(MemberModel).filter_by(id=member_id).first()
            if session_member is None:
                return None
            session.delete(session_member)
            session.commit()
            return session_member.id

    def _convert_to_member(self, member_model: MemberModel) -> Member:
        return Member(
            first_name=member_model.first_name,
            last_name=member_model.last_name,
            gender=member_model.gender,
            date_of_birth=member_model.date_of_birth,
            email=member_model.email,
        )

    def get_members_with_birthday_today(self, today: date) -> List[Member]:
        with SessionLocal() as session:
            session_members = (
                session.query(MemberModel)
                .filter(
                    extract("month", MemberModel.date_of_birth) == today.month,
                    extract("day", MemberModel.date_of_birth) == today.day,
                )
                .all()
            )

            return [
                self._convert_to_member(session_member)
                for session_member in session_members
            ]
