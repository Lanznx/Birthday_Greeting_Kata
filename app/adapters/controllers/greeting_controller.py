from fastapi import APIRouter, HTTPException, status
from app.use_cases.member_use_cases.send_birthday_greeting import (
    SendBirthdayGreetingUseCase,
)
from app.use_cases.ports.member_repository import IMemberRepository
from app.use_cases.ports.greeting_service import IGreetingService
from app.infra.dependencies import get_member_repository, get_greeting_service
from app.use_cases.dtos.birthday_greeting_dto import (
    BirthdayGreetingInputDTO,
    BirthdayGreetingOutputDTOV1,
    BirthdayGreetingOutputDTOV2,
    BirthdayGreetingOutputDTOV3,
)

greeting_routes = APIRouter(tags=["greeting"], prefix="/greeting")


@greeting_routes.post("/v1/birthday", status_code=status.HTTP_200_OK)
def send_birthday_greetings_v1(today: BirthdayGreetingInputDTO):
    try:
        member_repository: IMemberRepository = get_member_repository()
        greeting_service: IGreetingService = get_greeting_service("v1")
        use_case = SendBirthdayGreetingUseCase(member_repository, greeting_service)
        greetings = use_case.execute(today.current_date)
        if not greetings:
            raise HTTPException(status_code=404, detail="No birthdays found today.")
        return BirthdayGreetingOutputDTOV1(
            message="Birthday greetings sent successfully", greetings=greetings
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@greeting_routes.post("/v2/birthday", status_code=status.HTTP_200_OK)
def send_birthday_greetings_v2(today: BirthdayGreetingInputDTO):
    try:
        member_repository: IMemberRepository = get_member_repository()
        greeting_service: IGreetingService = get_greeting_service("v2")
        use_case = SendBirthdayGreetingUseCase(member_repository, greeting_service)
        greetings = use_case.execute(today.current_date)
        if not greetings:
            raise HTTPException(status_code=404, detail="No birthdays found today.")
        return BirthdayGreetingOutputDTOV2(
            message="Birthday greetings sent successfully", greetings=greetings
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@greeting_routes.post("/v3/birthday", status_code=status.HTTP_200_OK)
def send_birthday_greetings_v3(today: BirthdayGreetingInputDTO):
    try:
        member_repository: IMemberRepository = get_member_repository()
        greeting_service: IGreetingService = get_greeting_service("v3")
        use_case = SendBirthdayGreetingUseCase(member_repository, greeting_service)
        greetings = use_case.execute(today.current_date)
        if not greetings:
            raise HTTPException(
                status_code=404, detail="No elder birthdays found today."
            )
        return BirthdayGreetingOutputDTOV3(
            message="Birthday greetings sent successfully", greetings=greetings
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
