from fastapi import FastAPI
from src.users_app.routers import app as users_router



app = FastAPI()

app.include_router(users_router)