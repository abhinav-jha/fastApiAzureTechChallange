import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
server = os.getenv("POSTGRES_SERVER_LOCAL")
port = os.getenv("POSTGRES_PORT")
dbname = os.getenv("POSTGRES_DB_USERSERVICE")

# Construct the PostgreSQL URL
DB_URL = f"postgresql://{user}:{password}@{server}:{port}/{dbname}"
# print("********* DB URL *********", DB_URL)  # Remove in production

# SQLAlchemy setup
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
