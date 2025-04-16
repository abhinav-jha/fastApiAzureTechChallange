import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
POST_SERVICE_URL = os.getenv("POST_SERVICE_URL")
