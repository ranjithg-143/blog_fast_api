from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    content: Optional[str] = None


class BlogView(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_orm = True


class BlogUpdate(BlogCreate):
    pass
