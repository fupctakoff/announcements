from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers
from src.announcements_app.shemas import AnnouncementCreate, AnnouncementSchema
from src.users_app.routers import app as users_router
from src.announcements_app.repository import AnnouncementRepository
from src.database.models import User
from src.users_app.user_manager import get_user_manager
from src.users_app.authentication_backend import auth_backend

app = FastAPI()

app.include_router(users_router)


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user()


@app.get('/announcements_list')
async def get_list_announcements(response: AnnouncementRepository = Depends()):
    return await response.get_list_announcements()


@app.get('/create_announcement_type')
async def create_announcement_type(name: str, response: AnnouncementRepository = Depends()):
    return await response.create_announcement_type(name)


@app.get('/create_announcement', status_code=201)
async def create_announcement(user: User = Depends(current_user), data: AnnouncementCreate = Depends(), response: AnnouncementRepository = Depends()):
    return await response.create_announcement(user.id, data)


@app.get('/detail_announcement')
async def get_announcement_detail(id: int, response: AnnouncementRepository = Depends()):
    return await response.get_announcement_detail(id)


@app.get('/delete_announcement')
async def delete_announcement(id: int, user: User = Depends(current_user), response: AnnouncementRepository = Depends()):
    return await response.delete_announcement(id, user)
