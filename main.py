from fastapi import FastAPI
from src.users_app.routers import app as users_router
from src.announcements_app.routers import app as announcements_router
from src.comments_app.routers import app as comments_router
from src.events_app.routers import app as events_router
from src.graphql_app.routers import app as graphql_router

app = FastAPI()

app.mount('/graphql', graphql_router)
app.include_router(users_router)
app.include_router(announcements_router, prefix='/announcement',
                   tags=['working with announcements'])
app.include_router(comments_router, prefix='/comment', tags=['comments block'])
app.include_router(events_router, prefix='/events')