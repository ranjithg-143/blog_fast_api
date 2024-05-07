from db.repository.user import create_new_user
from db.session import get_db
from fastapi import APIRouter, Depends, status
from schemas.user import UserCreate, UserView
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=UserView, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
