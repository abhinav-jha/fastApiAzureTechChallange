from .session import Base, engine
from .models import Post

def init():
    print("Creating database tables... for Post model")
    Base.metadata.create_all(bind=engine)