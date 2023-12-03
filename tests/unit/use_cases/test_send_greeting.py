import pytest
from datetime import date
from unittest.mock import create_autospec
from app.use_cases.member_use_cases.send_birthday_greeting import (
    SendBirthdayGreetingUseCase,
)
from app.use_cases.ports.member_repository import IMemberRepository
from app.use_cases.ports.greeting_service import IGreetingService
from app.entities.member import Member


@pytest.fixture
def member_repository_mock():
    return create_autospec(IMemberRepository)


@pytest.fixture
def greeting_service_mock():
    return create_autospec(IGreetingService)


@pytest.fixture
def send_birthday_greeting_use_case(member_repository_mock, greeting_service_mock):
    return SendBirthdayGreetingUseCase(member_repository_mock, greeting_service_mock)


def test_send_birthday_greetings(
    send_birthday_greeting_use_case, member_repository_mock, greeting_service_mock
):
    birthday_members = [
        Member(
            first_name="John",
            last_name="Doe",
            gender="Male",
            date_of_birth=date(1990, 1, 1),
            email="john.doe@example.com",
        ),
        Member(
            first_name="Jane",
            last_name="Smith",
            gender="Female",
            date_of_birth=date(1992, 1, 1),
            email="jane.smith@example.com",
        ),
    ]

    today = date(2023, 1, 1)

    member_repository_mock.get_members_with_birthday_today.return_value = (
        birthday_members
    )

    send_birthday_greeting_use_case.execute(today)

    member_repository_mock.get_members_with_birthday_today.assert_called_once()

    for member in birthday_members:
        greeting_service_mock.generate_greeting_message.assert_any_call(member)
        greeting_message = greeting_service_mock.generate_greeting_message.return_value
        greeting_service_mock.send_greeting.assert_any_call(member, greeting_message)
