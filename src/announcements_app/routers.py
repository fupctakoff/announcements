from typing import List
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi_users import FastAPIUsers
from src.announcements_app.shemas import AnnouncementCreate, AnnouncementResponseDetail, AnnouncementSchema
from src.announcements_app.repository import AnnouncementRepository
from src.database.models import User
from src.users_app.user_manager import get_user_manager
from src.users_app.authentication_backend import auth_backend

app = APIRouter()

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user()


@app.post('/create_announcement_type', status_code=201)
async def create_announcement_type(name: str, response: AnnouncementRepository = Depends()) -> bool:
    return await response.create_announcement_type(name)


@app.post('/create_announcement', status_code=201)
async def create_announcement(
    user: User = Depends(current_user),
    data: AnnouncementCreate = Depends(),
    response: AnnouncementRepository = Depends()
) -> JSONResponse:
    return await response.create_announcement(user.id, data)


@app.get('/announcements_list', status_code=200)
async def get_list_announcements(response: AnnouncementRepository = Depends()) -> List[AnnouncementSchema]:
    return await response.get_list_announcements()


@app.get('/detail_announcement', status_code=200)
async def get_announcement_detail(id: int, response: AnnouncementRepository = Depends()) -> AnnouncementResponseDetail:
    return await response.get_announcement_detail(id)


@app.delete('/delete_announcement', status_code=200)
async def delete_announcement(id: int, user: User = Depends(current_user), response: AnnouncementRepository = Depends()) -> JSONResponse:
    return await response.delete_announcement(id, user)
