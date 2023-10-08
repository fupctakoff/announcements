
from fastapi.responses import JSONResponse
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.database.models import Role, User
from src.database.db_utils import get_async_session
from src.users_app.schemas import UserRead


class RoleRepository:

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session

    async def _is_admin(self, user: UserRead) -> bool | None:
        admin_id = await self._get_admin_role_id()
        if user.role_id == admin_id:
            return True

    async def _get_admin_role_id(self) -> int:
        obj = await self.session.execute(select(Role.id).where(Role.name == 'admin'))
        response = obj.scalars().one()
        return response

    async def _get_user_role_id(self) -> int:
        obj = await self.session.execute(select(Role.id).where(Role.name == 'user'))
        response = obj.scalars().one()
        return response

    async def give_administrator_rights(self, user_id: int, admin: User) -> JSONResponse:
        if not await self._is_admin(admin):
            return JSONResponse({"detail": "Forbidden"}, status_code=403)
        admin_id = await self._get_admin_role_id()
        await self.session.execute(update(User).where(User.id == user_id).values(role_id=admin_id))
        await self.session.commit()
        return JSONResponse({'detail': True}, status_code=200)
