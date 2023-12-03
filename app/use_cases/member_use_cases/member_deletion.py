from app.use_cases.ports.member_repository import IMemberRepository


class MemberDeletionUseCase:
    def __init__(self, member_repository: IMemberRepository):
        self.member_repository = member_repository

    def delete_member(self, member_id: str) -> int:
        member = self.member_repository.get_member(member_id)
        if member is None:
            raise ValueError(f"Member with id {member_id} does not exist")
        member_id = self.member_repository.delete_member(member_id)
        return member_id
