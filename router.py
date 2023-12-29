import os

from fastapi import APIRouter, HTTPException

from utils import request_token

INTRA_AUTH_URL = os.getenv("INTRA_CLIENT_UID")
INTRA_CLIENT_UID = os.getenv("INTRA_CLIENT_UID")
INTRA_CLIENT_SECRET = os.getenv("INTRA_CLIENT_SECRET")
INTRA_REDIRECT_URI = os.getenv("INTRA_REDIRECT_URI")


router = APIRouter(prefix="/token")


@router.post("/access")
async def get_intra_token(code: str = None):
    if code is None or code == "":
        raise HTTPException(status_code=400, detail="Missing code")

    payload = {
        "client_id": INTRA_CLIENT_UID,
        "client_secret": INTRA_CLIENT_SECRET,
        "redirect_uri": INTRA_REDIRECT_URI,
        "grant_type": "authorization_code",
        "code": code,
    }

    token = request_token(payload)
    return token


@router.post("/refresh")
async def refresh_intra_token(refresh_token: str = None):
    if refresh_token is None or refresh_token == "":
        raise HTTPException(status_code=400, detail="Missing refresh_token")

    payload = {
        "client_id": INTRA_CLIENT_UID,
        "client_secret": INTRA_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    token = request_token(payload)
    return token
