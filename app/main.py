import os

from fastapi import FastAPI
from app.database.nosql import db
from app.api.routers import v1

app = FastAPI(
        title="LinuxProfile",
        description="Linux Profile Project",
        version="0.0.1",
        contact={
            "name": "Fernando Celmer",
            "url": "www.linuxprofile.com",
            "email": "email@fernandocelmer.com",
        }
        )

app.include_router(v1, prefix="/v1")

@app.get("/status")
async def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's live"})

