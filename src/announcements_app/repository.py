import asyncio
from typing import List
from fastapi.responses import JSONResponse
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.announcements_app.shemas import AnnouncementCreate, AnnouncementResponseDetail, AnnouncementSchema
from src.database.models import Announcement, AnnouncementType, User
from src.database.validation_including import validation
from src.database.db_utils import get_async_session


class AnnouncementRepository:

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session

    async def create_announcement_type(self, name: str):
        new_obj = AnnouncementType(name=name)
        self.session.add(new_obj)
        await self.session.commit()
        return True

    async def get_list_announcements(self) -> List[AnnouncementSchema]:
        result = await self.session.execute(select(Announcement).order_by(-Announcement.id))
        data = result.scalars().all()
        return [AnnouncementSchema(title=row.title, type_id=row.type_id, owner_id=row.owner_id) for row in data]

    async def get_announcement_detail(self, id) -> AnnouncementResponseDetail:
        completed_validation = await asyncio.create_task(validation(id, Announcement, self.session))
        if completed_validation:
            return completed_validation
        result = await self.session.execute(select(Announcement).where(Announcement.id == id))
        data = result.scalars().one_or_none()
        return AnnouncementResponseDetail(title=data.title, content=data.content, owner_id=data.owner_id, type_id=data.type_id)

    async def create_announcement(self, user_id, items: AnnouncementCreate = Depends()):
        new_obj = Announcement(
            title=items.title, content=items.content, type_id=items.type_id, owner_id=user_id)
        self.session.add(new_obj)
        await self.session.commit()
        return {'detail': True}

    async def delete_announcement(self, id: int, user: User):
        completed_validation = await validation(id, Announcement, self.session)
        if completed_validation:
            return completed_validation
        data = await self.session.execute(select(Announcement).where(Announcement.id==id))
        obj = data.scalars().one()
        if user.id == obj.owner_id or user.role_id == 2:
            await self.session.execute(delete(Announcement).where(Announcement.id == id))
            await self.session.commit()
            return {'message': f'Объявление {id} успешно удалено.'}
        return JSONResponse({'message': 'Отказано в доступе'}, status_code=403)
