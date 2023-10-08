from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from src.database.models import User
from src.users_app.authentication_backend import auth_backend
from src.users_app.schemas import UserRead, UserCreate, UserUpdate
from fastapi_users import FastAPIUsers

from src.users_app.user_manager import get_user_manager
from src.users_app.repository import RoleRepository


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


@app.patch("/set_admin", tags=["users"], status_code=200)
async def appointment_as_administrator(
    user_id: int,
    admin: User = Depends(current_user),
    response: RoleRepository = Depends()
) -> JSONResponse:
    return await response.give_administrator_rights(user_id, admin)
