from typing import List
from pydantic import BaseModel, ConfigDict


class AnnouncementSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    type_id: int
    owner_id: int


class AnnouncementResponseDetail(AnnouncementSchema):
    #comments here
    content: str
    pass

class AnnouncementCreate(BaseModel):
    title: str
    content: str
    type_id: int