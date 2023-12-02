from datetime import date
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


def test_member_is_birthday():
    member = Member(
        first_name="John",
        last_name="Doe",
        gender="Male",
        date_of_birth="1990-01-01",
        email="john.doe@example.com",
    )
    # 假設今天是 1 月 1 日
    assert member.is_birthday(date(2023, 1, 1)) is True
    # 假設今天是 1 月 2 日
    assert member.is_birthday(date(2023, 1, 2)) is False
