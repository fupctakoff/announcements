from pydantic import BaseModel


class CommentBase(BaseModel):
    id: int
    text: str


class Comment(CommentBase):
    owner_id: int
    announcement_id: int
