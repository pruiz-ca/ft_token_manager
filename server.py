#!/usr/bin/env python3
import os
import uvicorn

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response, Depends
from utils import validate_request
from router import router

load_dotenv()
X_SECRET = os.getenv("X-SECRET")
PORT = int(os.getenv("PORT"))
SSL_CERT = os.getenv("SSL_CERT")
SSL_KEY = os.getenv("SSL_KEY")

app = FastAPI()

app.include_router(router, dependencies=[Depends(validate_request)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["X-Secret"],
)

@app.middleware("http")
async def catch_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return Response(f"error {e}", status_code=500)


def main():
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True, ssl_certfile=SSL_CERT, ssl_keyfile=SSL_KEY)

if __name__ == "__main__":
    main()
