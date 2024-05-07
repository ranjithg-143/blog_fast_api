from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from schemas.blog import BlogCreate, BlogUpdate, BlogView
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.blog import create_blog, update_blog, delete_blog, list_blogs, view_blog

router = APIRouter()


@router.post('/blogs', response_model=BlogView, status_code=status.HTTP_201_CREATED)
def create_new_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    blog = create_blog(blog=blog, db=db, author_id=1)
    return blog


@router.put('/blog/{id}', response_model=BlogView)
def modify_blog(id: int, blog: BlogUpdate, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, author_id=1, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.delete("/blog/{id}")
def remove_blog(id: int, db: Session = Depends(get_db)):
    message = delete_blog(id=id, author_id=1, db=db)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return message.get("msg")


@router.get("/blog/{id}", response_model=BlogView)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = view_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.get("/blogs", response_model=List[BlogView])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db)
    return blogs
