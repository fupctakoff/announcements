from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from src.database.models import User
from src.users_app.authentication_backend import auth_backend
from src.users_app.schemas import UserRead, UserCreate
from fastapi_users import FastAPIUsers
from src.users_app.user_manager import get_user_manager
from src.users_app.repository import UsersRepository


app = APIRouter()

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(active=True, superuser=True)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["users"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["users"],
)


@app.patch("/set_admin_from_admin", tags=["users"], status_code=200)
async def appointment_as_administrator(
    user_id: int,
    admin: User = Depends(current_user),
    response: UsersRepository = Depends()
) -> JSONResponse:
    return await response.give_administrator_rights(user_id, admin)


@app.post("/create_role", tags=["users"], status_code=201)
async def create_role(
    name: str,
    response: UsersRepository = Depends()
) -> JSONResponse:
    return await response.create_role(name)

# Данный эндпоинт предназначен для удобства создания первого администратора (без использования чистого sql)


@app.patch("/set_admin_from_user", tags=["users"])
async def __appoint_me_as_admin(
    user: User = Depends(current_user),
    response: UsersRepository = Depends()
) -> JSONResponse:
    return await response._set_admin(user.id)
