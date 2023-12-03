from app.use_cases.ports.member_repository import IMemberRepository
from app.adapters.repositories.mysql_member_repository import MySQLMemberRepository
from app.use_cases.ports.greeting_service import IGreetingService
from app.adapters.services.greeting_service_v1 import GreetingServiceV1
from app.adapters.services.greeting_service_v2 import GreetingServiceV2


def get_member_repository(repo_type: str = "mysql") -> IMemberRepository:
    if repo_type == "mysql":
        return MySQLMemberRepository()


def get_greeting_service(version) -> IGreetingService:
    if version == "v1":
        return GreetingServiceV1()
    elif version == "v2":
        return GreetingServiceV2()
