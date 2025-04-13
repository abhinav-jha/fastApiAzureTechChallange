from pydantic import BaseModel
from typing import Optional

# Define a lightweight version of UserResponse from the User microservice
class AuthorInfo(BaseModel):
    id: int
    username: Optional[str]
    email: Optional[str]

# Shared base for Post
class PostBase(BaseModel):
    title: str
    content: str

# For creating a post (no id or author yet)
class PostCreate(PostBase):
    user_id: int  # Needed to link the post to a user

# For reading a post (with id and author details)
class PostResponse(PostBase):
    id: int
    user_id: int
    author: Optional[AuthorInfo] = None  # Nested user info (from user microservice)

    class Config:
        orm_mode = True
        


