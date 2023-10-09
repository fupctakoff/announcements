from typing import Optional
from fastapi_users.schemas import BaseUser, BaseUserUpdate, CreateUpdateDictModel
from pydantic import EmailStr


class UserRead(BaseUser[int]):
    name: str
    role_id: Optional[int] = None


class UserCreate(CreateUpdateDictModel):
    name: str
    email: EmailStr
    password: str


class UserUpdate(BaseUserUpdate):
    name: str
