from pydantic import BaseModel, EmailStr, constr, field_validator
from datetime import date
from typing import Union


class MemberInputDTO(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    gender: str
    date_of_birth: date
    email: EmailStr

    @field_validator("date_of_birth")
    def check_date_of_birth(cls, value: date):
        if value > date.today():
            raise ValueError("Date of Birth cannot be in the future")
        return value


class MemberOutputDTO(BaseModel):
    message: str
    member_id: Union[str, int]
