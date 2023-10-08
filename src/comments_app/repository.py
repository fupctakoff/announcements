
import asyncio
from typing import List
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Bundle
from src.comments_app.shemas import CommentBase
from src.database.models import Announcement, Comment, User
from src.database.validation_including import validation
from src.database.db_utils import get_async_session
from src.users_app.repository import RoleRepository


class CommentRepository:

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session

    async def create_comment(self, announcement_id: int, user_id: int, text: str) -> JSONResponse:
        completed_validation = await asyncio.create_task(validation(announcement_id, Announcement, self.session))
        if completed_validation:
            return completed_validation
        new_obj = Comment(text=text, owner_id=user_id,
                          announcement_id=announcement_id)
        self.session.add(new_obj)
        await self.session.commit()
        return JSONResponse({'detail': True}, status_code=201)

    async def delete_comment(self, id: int, user: User, is_admin: RoleRepository = Depends()):
        completed_validation = await asyncio.create_task(validation(id, Comment, self.session))
        if completed_validation:
            return completed_validation
        data = await self.session.execute(select(Comment).where(Comment.id == id))
        obj = data.scalars().one()
        if user.id == obj.owner_id or await is_admin._is_admin(user):
            await self.session.execute(delete(Comment).where(Comment.id == id))
            await self.session.commit()
            return JSONResponse({'message': f'Комментарий {obj.text} успешно удален.'}, status_code=200)
        return JSONResponse({'message': 'Forbidden'}, status_code=403)

    async def get_list_comments(self, announcement_id: int) -> List[CommentBase]:
        a = await self.session.execute(
            select(Comment.text).join(Announcement.comments).where(Announcement.id == announcement_id))
        result = a.scalars().all()
        return [CommentBase(text=row) for row in result]
