from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers
from src.announcements_app.shemas import AnnouncementCreate, AnnouncementSchema
from src.users_app.routers import app as users_router
from src.announcements_app.routers import app as announcements_router
from src.announcements_app.repository import AnnouncementRepository
from src.database.models import User
from src.users_app.user_manager import get_user_manager
from src.users_app.authentication_backend import auth_backend
from src.users_app.repository import RoleRepository

app = FastAPI()

app.include_router(users_router)
app.include_router(announcements_router, prefix='/announcement',
                   tags=['working with announcements'])
