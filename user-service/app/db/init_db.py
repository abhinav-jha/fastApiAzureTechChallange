from .session import Base, engine
from app.models import User  # Import all models you want to initialize

def init():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
