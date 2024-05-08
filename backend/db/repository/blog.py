from db.models.blog import Blog
from schemas.blog import BlogCreate, BlogUpdate
from sqlalchemy.orm import Session


def create_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def update_blog(id: int, blog: BlogUpdate, author_id: int, db: Session):
    blog_obj = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        return
    blog_obj.title = blog.title
    blog_obj.content = blog.content
    db.add(blog_obj)
    db.commit()
    return blog_obj


def delete_blog(id: int, author_id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        return {"error": f"Could not find blog with id {id}"}
    blog.delete()
    db.commit()
    return {"msg": f"Successfully deleted blog with id {id}"}


def view_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs
