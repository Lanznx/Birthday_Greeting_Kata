from sqlalchemy import Column, Integer, String, Date
from app.infra.db.database import Base


class MemberModel(Base):
    __tablename__ = "Member"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
