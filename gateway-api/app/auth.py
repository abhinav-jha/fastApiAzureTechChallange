from fastapi import Request, HTTPException
import jwt

def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    # decode/verify the JWT (example below)
    payload = jwt.decode(token.split(" ")[1], "secret", algorithms=["HS256"])
    return payload
