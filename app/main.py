import os

from fastapi import FastAPI
from app.database.nosql import db

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

@app.get("/status")
async def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's live"})

