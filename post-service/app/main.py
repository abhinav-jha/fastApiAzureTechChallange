from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .schemas import PostCreate, PostResponse
from app.db import session, models
from app.db.init_db import init

app = FastAPI()

init()

@app.post("/posts/", response_model=PostResponse)
def create_new_post(post: PostCreate, db: Session = Depends(session.get_db)):
    return crud.create_post(db, post)


@app.get("/posts/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(session.get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get("/posts/", response_model=list[PostResponse])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(session.get_db)):
    return crud.get_all_posts(db, skip, limit)


@app.put("/posts/{post_id}", response_model=PostResponse)
def update_existing_post(post_id: int, post: PostCreate, db: Session = Depends(session.get_db)):
    updated_post = crud.update_post(db, post_id, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(session.get_db)):
    success = crud.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted successfully"}
