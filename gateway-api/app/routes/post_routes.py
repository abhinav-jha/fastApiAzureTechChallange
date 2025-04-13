from fastapi import APIRouter, Request
from app.config import USER_SERVICE_URL
import httpx

router = APIRouter()

@router.api_route("/posts/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def post_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{POST_SERVICE_URL}/posts/{path}",
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()