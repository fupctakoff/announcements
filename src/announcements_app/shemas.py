from pydantic import BaseModel, ConfigDict


class AnnouncementSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    type_id: int
    owner_id: int


class AnnouncementResponseDetail(AnnouncementSchema):
    content: str
    # todo
    # comments: dict


class AnnouncementCreate(BaseModel):
    title: str
    content: str
    type_id: int
