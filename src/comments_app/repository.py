import asyncio
from typing import List
from fastapi.responses import JSONResponse
from sqlalchemy import delete, select
from src.comments_app.shemas import CommentBase
from src.database.models import Announcement, Comment, User
from src.database.validation_including import validation
from src.users_app.repository import PermissionRepository


class CommentRepository(PermissionRepository):

    async def create_comment(
        self,
        announcement_id: int,
        user_id: int,
        text: str
    ) -> JSONResponse:
        completed_validation = await asyncio.create_task(validation(announcement_id, Announcement, self.session))
        if completed_validation:
            return completed_validation
        new_obj = Comment(text=text, owner_id=user_id,
                          announcement_id=announcement_id)
        self.session.add(new_obj)
        await self.session.commit()
        return JSONResponse({'detail': True}, status_code=201)

    async def delete_comment(
        self,
        id: int,
        user: User
    ) -> JSONResponse:
        completed_validation = await asyncio.create_task(validation(id, Comment, self.session))
        if completed_validation:
            return completed_validation
        data = await self.session.execute(select(Comment).where(Comment.id == id))
        obj = data.scalars().one()
        if user.id == obj.owner_id or await self._is_admin(user):
            await self.session.execute(delete(Comment).where(Comment.id == id))
            await self.session.commit()
            return JSONResponse({'message': f'Comment {obj.text} successfully deleted.'}, status_code=200)
        return JSONResponse({'message': 'Forbidden'}, status_code=403)

    async def get_list_comments(
        self,
        announcement_id: int
    ) -> List[CommentBase]:
        a = await self.session.execute(
            select(Comment).join(Announcement.comments).where(Announcement.id == announcement_id))
        result = a.scalars().all()
        return [CommentBase(id=row.id, text=row.text) for row in result]
