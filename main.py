from fastapi import FastAPI
from src.users_app.routers import app as users_router
from src.announcements_app.routers import app as announcements_router
from src.comments_app.routers import app as comments_router


app = FastAPI()

app.include_router(users_router)
app.include_router(announcements_router, prefix='/announcement',
                   tags=['working with announcements'])
app.include_router(comments_router, prefix='/comment', tags=['comments block'])
