from fastapi import APIRouter, HTTPException, status, Depends
from app.use_cases.member_use_cases.member_creation import (
    MemberCreationUseCase,
)
from app.use_cases.dtos.member_dto import MemberInputDTO, MemberOutputDTO
from app.use_cases.ports.member_repository import IMemberRepository
from app.infra.dependencies import get_member_repository

member_routes = APIRouter(tags=["member"], prefix="/member")


@member_routes.post("/", status_code=status.HTTP_201_CREATED)
def member_creation(member: MemberInputDTO):
    try:
        member_repository: IMemberRepository = get_member_repository()
        use_case = MemberCreationUseCase(member_repository)
        member_id = use_case.add_member(member)
        return MemberOutputDTO(
            message="Member created successfully", member_id=member_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
