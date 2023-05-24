from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.router import user_router
from app.common.config import settings

app = FastAPI()


@app.get("/healthcheck")
async def healthcheck() -> object:
    return {"status", "ok"}


app.include_router(user_router.router, prefix="/users", tags=["User"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)
