import os
import httpx

from fastapi import HTTPException, Request

X_SECRET = os.getenv("X-SECRET")
INTRA_AUTH_URL = os.getenv("INTRA_AUTH_URL")


def validate_request(request: Request):
    if request.headers.get("X-Secret") != X_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")


def request_token(payload: dict):
    res = httpx.post(INTRA_AUTH_URL, data=payload)
    if res.status_code != 200:
        raise HTTPException(status_code=500, detail="Token request failed")

    res_json = res.json()
    if res_json["access_token"] is None or res_json["refresh_token"] is None:
        raise HTTPException(status_code=500, detail="Token request failed")

    return res_json
