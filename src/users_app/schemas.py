from fastapi_users.schemas import BaseUser, BaseUserUpdate, CreateUpdateDictModel
from pydantic import BaseModel, EmailStr


class UserRead(BaseUser[int]):
    name: str
    role_id: int


class UserCreate(CreateUpdateDictModel):
    name: str
    email: EmailStr
    password: str


class UserUpdate(BaseUserUpdate):
    name: str
