from jose import jwt, JWTError
from fastapi import HTTPException, Request
import os
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("JWT_SECRET")


def verify_token(request: Request):
    try:
        token = request.cookies.get("token")
        if not token:
            raise HTTPException(status_code=401, detail="Token not found")
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
