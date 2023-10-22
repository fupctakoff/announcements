from ariadne import ObjectType
from src.database.models import Event, EventType
from sqlalchemy import select
from src.database.db_utils import get_async_session

event = ObjectType("Event")


@event.field("title")
async def resolve_get_event_title(id: int, *_):
    awaitable_session = anext(get_async_session())
    session = await awaitable_session
    statement = select(Event.title).where(Event.id == id)
    data = await session.execute(statement)
    await session.close()
    result = tuple(data)
    if result:
        return result[0][0]
    return result


@event.field("content")
async def resolve_get_event_content(id: int, *_):
    awaitable_session = anext(get_async_session())
    session = await awaitable_session
    statement = select(Event.content).where(Event.id == id)
    data = await session.execute(statement)
    await session.close()
    result = tuple(data)
    if result:
        return result[0][0]
    return result


@event.field("dresscode")
async def resolve_get__event_dresscode(id: int, *_):
    awaitable_session = anext(get_async_session())
    session = await awaitable_session
    statement = select(Event.dresscode).where(Event.id == id)
    data = await session.execute(statement)
    await session.close()
    result = tuple(data)
    if result:
        return result[0][0]
    return result


@event.field("event_type")
async def resolve_get_event_eventtype(id: int, *_):
    return id
