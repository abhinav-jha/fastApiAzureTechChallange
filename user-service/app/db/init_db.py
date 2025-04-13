# Import all models to initialize
from .session import Base, engine
from .models import User  

def init():
    print("Creating database tables... for user model")
    Base.metadata.create_all(bind=engine)
