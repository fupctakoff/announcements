from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    name: str
    role: str
    announcemets: int
    comments: int


class UserCreate(schemas.BaseUserCreate):
    name: str
    role: str
    announcemets: int
    comments: int


class UserUpdate(schemas.BaseUserUpdate):
    name: str
    role: str
    announcemets: int
    comments: int

