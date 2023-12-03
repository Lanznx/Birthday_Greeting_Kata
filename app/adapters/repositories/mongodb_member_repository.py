from typing import List
from datetime import date, datetime
from app.entities.member import Member
from app.use_cases.ports.member_repository import IMemberRepository
from app.infra.db.mongodb.model import MemberDocument
from app.infra.db.mongodb.database import initialize_db
from mongoengine.queryset.visitor import Q

initialize_db()


class MongoDBMemberRepository(IMemberRepository):
    def create_member(self, member: Member) -> str:
        member_doc = MemberDocument(
            first_name=member.first_name,
            last_name=member.last_name,
            gender=member.gender,
            date_of_birth=member.date_of_birth,
            email=member.email,
        )
        member_doc.save()
        return str(member_doc.id)

    def get_member(self, member_id: str) -> Member:
        member_doc = MemberDocument.objects(id=member_id).first()
        if member_doc is None:
            return None
        return self._convert_to_member(member_doc)

    def delete_member(self, member_id: str) -> str:
        member_doc = MemberDocument.objects(id=member_id).first()
        if member_doc is None:
            return None
        member_doc.delete()
        return str(member_doc.id)

    def _convert_to_member(self, member_doc: MemberDocument) -> Member:
        return Member(
            first_name=member_doc["first_name"],
            last_name=member_doc["last_name"],
            gender=member_doc["gender"],
            date_of_birth=member_doc["date_of_birth"],
            email=member_doc["email"],
        )

    def get_members_with_birthday_today(self, today: date) -> List[Member]:
        pipeline = [
            {
                "$match": {
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$month": "$date_of_birth"}, today.month]},
                            {"$eq": [{"$dayOfMonth": "$date_of_birth"}, today.day]},
                        ]
                    }
                }
            }
        ]

        member_docs = MemberDocument.objects.aggregate(pipeline)
        return [self._convert_to_member(member_doc) for member_doc in member_docs]
