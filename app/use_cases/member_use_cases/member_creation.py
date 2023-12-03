from app.entities.member import Member
from app.use_cases.ports.member_repository import IMemberRepository
from app.use_cases.dtos.member_dto import MemberInputDTO


class MemberCreationUseCase:
    def __init__(self, member_repository: IMemberRepository):
        self.member_repository = member_repository

    def add_member(self, member_data: MemberInputDTO) -> int:
        member = Member(**member_data.model_dump())
        member_id = self.member_repository.create_member(member)
        return member_id
