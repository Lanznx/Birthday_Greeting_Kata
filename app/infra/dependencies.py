from app.use_cases.ports.member_repository import IMemberRepository
from app.adapters.repositories.mysql_member_repository import MySQLMemberRepository
from app.use_cases.ports.greeting_service import IGreetingService
from app.use_cases.ports.picture_service import IPictureService
from app.adapters.services.greeting_service_v1 import GreetingServiceV1
from app.adapters.services.greeting_service_v2 import GreetingServiceV2
from app.adapters.services.greeting_service_v3 import GreetingServiceV3
from app.adapters.services.greeting_service_v4 import GreetingServiceV4
from app.adapters.services.picture_service import PictureService


def get_member_repository(repo_type: str = "mysql") -> IMemberRepository:
    if repo_type == "mysql":
        return MySQLMemberRepository()


def get_greeting_service(version) -> IGreetingService:
    if version == "v1":
        return GreetingServiceV1()
    elif version == "v2":
        return GreetingServiceV2()
    elif version == "v3":
        return GreetingServiceV3(get_picture_service())
    elif version == "v4":
        return GreetingServiceV4()


def get_picture_service() -> IPictureService:
    return PictureService()
