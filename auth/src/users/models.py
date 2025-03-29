import uuid

from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username: str | Column[str] = Column(String, unique=True, index=True)
    hashed_password: str | Column[str] = Column(String)

    def __init__(self, email, username, hashed_password):
        self.email = email
        self.username = username
        self.hashed_password = hashed_password


class UserSchema(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    hashed_password: str
    exp: int | float
