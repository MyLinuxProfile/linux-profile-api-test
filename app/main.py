import os

from fastapi import FastAPI, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from sqlalchemy.orm import Session

from app.controller import ControllerUser, ControllerSyncUser
from app.schemas.sync_user import SchemaSyncUser
from app.schemas.user import SchemaUser

from app.database.mysql import get_db
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

