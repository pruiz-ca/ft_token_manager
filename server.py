import uvicorn
from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from router import router
from utils import validate_request

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


@app.get("/status")
def status():
    return {"status": "ok"}


def main():
    uvicorn.run("server:app", host="0.0.0.0", port=3000, reload=True)


if __name__ == "__main__":
    main()
