from fastapi import FastAPI
import httpx

app = FastAPI()

USER_SERVICE_URL = "http://user-service:80"
POST_SERVICE_URL = "http://post-service:80"
COMMENT_SERVICE_URL = "http://comment-service:80"

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
    return response.json()

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POST_SERVICE_URL}/posts/{post_id}")
    return response.json()
