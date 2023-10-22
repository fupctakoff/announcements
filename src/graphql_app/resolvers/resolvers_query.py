from ariadne import QueryType
from src.database.models import Event, EventType
from sqlalchemy import select
from src.database.db_utils import get_async_session

query = QueryType()


@query.field("get_full_event")
async def resolve_get_full_event(_, info, id: int):
    awaitable_session = anext(get_async_session())
    session = await awaitable_session
    statement = select(Event.id, Event.title, Event.content, Event.dresscode, EventType.name).join(
        Event.type).where(
        Event.id == id)
    data = await session.execute(statement)
    await session.close()
    result = tuple(data)
    if result:
        return {
            'id': result[0][0],
            'name': result[0][1],
            'content': result[0][2],
            'dresscode': result[0][3],
            'type': result[0][4],
        }
    return result


@query.field("get_event")
async def resolve_get_event(_, info, id: int):
    return id

@query.field("get_event_type")
async def resolve_get_event_type(_, info, id: int):
    return id
