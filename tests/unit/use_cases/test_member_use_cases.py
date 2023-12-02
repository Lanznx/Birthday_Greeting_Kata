import pytest
import pydantic
from datetime import datetime, timedelta, date
from unittest.mock import Mock
from app.entities.member import Member
from app.use_cases.member_use_cases.member_creation import MemberCreationUseCase
from app.use_cases.ports.member_repository import IMemberRepository
from app.use_cases.dtos.member_dto import MemberInputDTO


@pytest.fixture
def member_repository_mock():
    return Mock(spec=IMemberRepository)


@pytest.fixture
def member_creation_use_case(member_repository_mock):
    return MemberCreationUseCase(member_repository_mock)


def test_add_member(member_creation_use_case, member_repository_mock):
    member_data = MemberInputDTO(
        first_name="John",
        last_name="Doe",
        gender="Male",
        date_of_birth="1990-01-01",
        email="john.doe@example.com",
    )

    member_repository_mock.create_member.return_value = Member(
        **member_data.model_dump()
    )

    new_member = member_creation_use_case.add_member(member_data)

    member_repository_mock.create_member.assert_called_once_with(
        Member(**member_data.model_dump())
    )
    assert new_member.first_name == member_data.first_name
    assert new_member.last_name == member_data.last_name
    assert new_member.gender == member_data.gender
    assert new_member.date_of_birth == member_data.date_of_birth
    assert new_member.email == member_data.email


@pytest.mark.parametrize("email", ["invalid-email", "test@test", ""])
def test_add_member_with_invalid_email(member_creation_use_case, email):
    with pytest.raises(pydantic.ValidationError) as excinfo:
        MemberInputDTO(
            first_name="Invalid",
            last_name="Email",
            gender="Male",
            date_of_birth="1990-01-01",
            email=email,
        )
    assert "value is not a valid email address" in str(excinfo.value)


def test_add_member_with_future_date(member_creation_use_case):
    future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    with pytest.raises(pydantic.ValidationError) as excinfo:
        MemberInputDTO(
            first_name="Future",
            last_name="Date",
            gender="Female",
            date_of_birth=future_date,
            email="future.date@example.com",
        )
    assert "Date of Birth cannot be in the future" in str(excinfo.value)


@pytest.mark.parametrize("first_name, last_name", [("", "Doe"), ("John", "")])
def test_add_member_with_empty_name(member_creation_use_case, first_name, last_name):
    with pytest.raises(pydantic.ValidationError) as excinfo:
        MemberInputDTO(
            first_name=first_name,
            last_name=last_name,
            gender="Male",
            date_of_birth="1990-01-01",
            email="john.doe@example.com",
        )
