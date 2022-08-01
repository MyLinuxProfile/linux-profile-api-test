import os

from fastapi import FastAPI
from app.api.routers import v1


with open("app/static/docs/api.md", "r", encoding="utf-8") as fh:
    description = fh.read()


app = FastAPI(
        title="LinuxProfile",
        description=description,
        version="0.0.1"
    )


app.include_router(v1, prefix="/v1")


@app.get("/status")
async def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's live"})

