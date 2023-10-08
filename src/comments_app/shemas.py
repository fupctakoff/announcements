from pydantic import BaseModel


class CommentBase(BaseModel):
    text: str


class Comment(CommentBase):
    owner_id: int
    announcement_id: int
