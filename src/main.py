from fastapi import FastAPI
from database.models import User
from src.users_app.authentication_backend import auth_backend
from src.users_app.schemas import UserRead, UserCreate, UserUpdate
from fastapi_users import FastAPIUsers

from src.users_app.user_manager import get_user_manager


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

# @app.get('/')
# async def foo():
#     return 2**20


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )


# @app.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}