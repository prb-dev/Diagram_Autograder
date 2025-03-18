from fastapi import HTTPException


def verify_permission(payload):
    if payload.get("role") != "teacher":
        raise HTTPException(status_code=403, detail="Permission denied")
    return payload
