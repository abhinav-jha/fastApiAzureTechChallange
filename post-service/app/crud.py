from sqlalchemy.orm import Session
from app.db.models import Post
from .schemas import PostCreate


def create_post(db: Session, post: PostCreate) -> Post:
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int) -> Post:
    return db.query(Post).filter(Post.id == post_id).first()


def get_all_posts(db: Session, skip: int = 0, limit: int = 10) -> list[Post]:
    return db.query(Post).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: int, updated_data: PostCreate) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        for field, value in updated_data.dict().items():
            setattr(post, field, value)
        db.commit()
        db.refresh(post)
    return post


def delete_post(db: Session, post_id: int) -> bool:
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
