from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from app.db import session, models
from app.db.init_db import init

app = FastAPI()


init()

@app.post("/users/create", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(session.get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(session.get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
