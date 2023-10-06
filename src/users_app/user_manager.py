from typing import Optional, Union
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException
from database.models import User
from database.db_utils import get_user_db
from src.users_app.schemas import UserCreate

USERMANAGER_SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    verification_token_secret = USERMANAGER_SECRET
    verification_token_lifetime_seconds = 600

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 4:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)