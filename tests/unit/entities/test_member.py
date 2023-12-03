from datetime import timedelta, date
import pytest
from app.entities.member import Member


def test_member_creation():
    member = Member(
        first_name="John",
        last_name="Doe",
        gender="Male",
        date_of_birth="1990-01-01",
        email="john.doe@example.com",
    )
    assert member.first_name == "John"
    assert member.last_name == "Doe"
    assert member.gender == "Male"
    assert member.date_of_birth == date(1990, 1, 1)
    assert member.email == "john.doe@example.com"


def test_member_age():
    member = Member(
        first_name="John",
        last_name="Doe",
        gender="Male",
        date_of_birth="1990-01-01",
        email="john.doe@example.com",
    )
    # 假設今天是 2023 年，則年齡應為 33 歲
    assert member.age == 33


def test_future_birth_date():
    future_date = date.today() + timedelta(days=1)
    with pytest.raises(ValueError) as excinfo:
        Member(
            first_name="Jane",
            last_name="Doe",
            gender="Female",
            date_of_birth=future_date,
            email="jane.doe@example.com",
        )
    assert "Date of Birth cannot be in the future" in str(excinfo.value)


def test_invalid_email():
    with pytest.raises(ValueError):
        Member(
            first_name="John",
            last_name="Doe",
            gender="Male",
            date_of_birth="1990-01-01",
            email="invalid-email",
        )


def test_invalid_name():
    with pytest.raises(ValueError):
        Member(
            first_name="",  # Invalid first name
            last_name="Doe",
            gender="Male",
            date_of_birth="1990-01-01",
            email="john.doe@example.com",
        )

    with pytest.raises(ValueError):
        Member(
            first_name="John",
            last_name="",
            gender="Male",
            date_of_birth="1990-01-01",
            email="john.doe@example.com",
        )
