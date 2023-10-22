from ariadne import ObjectType
from src.database.models import Event, EventType
from sqlalchemy import select
from src.database.db_utils import get_async_session

eventtype = ObjectType("EventType")


@eventtype.field("event_type")
async def resolve_get_event_type(id: int, *_):
    awaitable_session = anext(get_async_session())
    session = await awaitable_session
    statement = select(EventType.name).where(EventType.id == id)
    data = await session.execute(statement)
    await session.close()
    result = tuple(data)
    if result:
        return result[0][0]
    return result
