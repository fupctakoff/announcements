from typing import List
from pydantic import BaseModel, ConfigDict
from src.comments_app.shemas import CommentBase


class AnnouncementSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    type_id: int
    owner_id: int


class AnnouncementResponseDetail(AnnouncementSchema):
    content: str
    comments: List[CommentBase]


class AnnouncementCreate(BaseModel):
    title: str
    content: str
    type_id: int
