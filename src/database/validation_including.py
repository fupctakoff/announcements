from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse


async def validation(id: int, some_class, session: AsyncSession) -> JSONResponse | None:
    obj = await session.execute(select(some_class).where(some_class.id == id))
    if obj.scalars().one_or_none() is None:
        return JSONResponse({'detail': f'Невозможно найти элемент {id} объекта {some_class}'}, status_code=404)
