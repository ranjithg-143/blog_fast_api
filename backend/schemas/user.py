from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)


class UserView(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_orm = True
