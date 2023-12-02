from pydantic import BaseModel, EmailStr
from datetime import date


class MemberInputDTO(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    email: EmailStr
