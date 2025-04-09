from app.models import UserCreate, UserProfile, UserBase, UserProfileUpdate
from userService.app.utils.utils import upload_file_to_blob
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional
from fastapi import HTTPException, status
from jose import JWTError, jwt
import os

# Dummy database (in a real-world app, we will connect to a database)
fake_users_db = {}

# Security and JWT setup
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Utility function to hash passwords
def hash_password(password: str):
    return pwd_context.hash(password)


# Utility function to verify hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Function to create JWT token
def create_access_token(data: dict):
    exp = (datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = data.copy()
    to_encode.update({"exp": exp})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Create User Service (register user)
def create_user(user: UserCreate):
    # Check if user already exists
    if user.email in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
            )

    hashed_password = hash_password(user.password)
    new_user = UserBase(
        id=len(fake_users_db) + 1,
        email=user.email,
        username=user.username,
        created_at=datetime.utcnow()
        )
    fake_users_db[user.email] = {"user": new_user, "password": hashed_password}
    return new_user


# Authenticate User (login)
def authenticate_user(email: str, password: str):
    user_record = fake_users_db.get(email)
    if user_record is None \
            or not verify_password(password, user_record["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
            )
    return user_record["user"]


# Update User Profile (update bio and/or profile picture)
def update_user_profile(user_id: int, user_profile: UserProfileUpdate):
    user_record = fake_users_db.get(user_id)
    if user_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
            )

    # Update the user profile details here
    user_profile_data = user_record["user"]
    if user_profile.bio:
        user_profile_data.bio = user_profile.bio
    if user_profile.profile_picture_url:
        user_profile_data.profile_picture_url \
            = user_profile.profile_picture_url
    return user_profile_data
