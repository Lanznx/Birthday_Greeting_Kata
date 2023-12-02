from datetime import date
from pydantic import BaseModel, EmailStr, constr, Field, field_validator


class Member(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    gender: str
    date_of_birth: date = Field(..., description="Date of Birth in 'YYYY-MM-DD' format")
    email: EmailStr

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, value: date):
        if value > date.today():
            raise ValueError("Date of Birth cannot be in the future")
        return value

    @property
    def age(self) -> int:
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

    def is_birthday(self, today) -> bool:
        return (
            today.month == self.date_of_birth.month
            and today.day == self.date_of_birth.day
        )
