from fastapi import FastAPI, Request
from config import USER_SERVICE_URL, POST_SERVICE_URL  # Import URLs from config
import httpx

app = FastAPI()

# Proxy for User service
@app.api_route("/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def user_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{USER_SERVICE_URL}/users/{path}",
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()

# Proxy for Post service
@app.api_route("/posts/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def post_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{POST_SERVICE_URL}/posts/{path}",
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()
