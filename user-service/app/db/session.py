import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get environment variables
user = os.getenv("POSTGRES_USER", "blogUser123")
password = os.getenv("POSTGRES_PASSWORD",'blogUser123@@')
server = os.getenv("POSTGRES_SERVER", "postgres-db")  # default to localhost
port = os.getenv("POSTGRES_PORT", "5432")           # default to 5432
dbname = os.getenv("POSTGRES_DB",'user_db')

# Construct DB URL
DB_URL = f"postgresql://{user}:{password}@{server}:{port}/{dbname}"

# Create engine
engine = create_engine(DB_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency function for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
