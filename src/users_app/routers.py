from fastapi import Depends, APIRouter
from src.database.models import User
from src.users_app.authentication_backend import auth_backend
from src.users_app.schemas import UserRead, UserCreate, UserUpdate
from fastapi_users import FastAPIUsers

from src.users_app.user_manager import get_user_manager


app = APIRouter()

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route", tags=["auth"])
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"
