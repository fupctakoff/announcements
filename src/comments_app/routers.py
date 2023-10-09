from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi_users import FastAPIUsers
from src.announcements_app.shemas import AnnouncementCreate, AnnouncementSchema
from src.users_app.routers import app as users_router
from src.announcements_app.routers import app as announcements_router
from src.announcements_app.repository import AnnouncementRepository
from src.database.models import User
from src.users_app.user_manager import get_user_manager
from src.users_app.authentication_backend import auth_backend
from src.comments_app.repository import CommentRepository


app = APIRouter()

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user()


@app.post('/create_comment')
async def create_comment(
    text: str,
    announcement_id: int,
    user: User = Depends(current_user),
    response: CommentRepository = Depends()
) -> None:
    return await response.create_comment(announcement_id, user.id, text)


@app.delete('/delete_comment', status_code=200)
async def delete_comment(
    id: int,
    user: User = Depends(current_user),
    response: CommentRepository = Depends()
) -> JSONResponse:
    return await response.delete_comment(id, user)


@app.get('/list_comments')
async def get_list_comments(announcement_id: int, response: CommentRepository = Depends()):
    return await response.get_list_comments(announcement_id)