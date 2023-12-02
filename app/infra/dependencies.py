from app.use_cases.ports.member_repository import IMemberRepository
from app.adapters.repositories.mysql_member_repository import MySQLMemberRepository


def get_member_repository(repo_type: str = "mysql") -> IMemberRepository:
    if repo_type == "mysql":
        return MySQLMemberRepository()
