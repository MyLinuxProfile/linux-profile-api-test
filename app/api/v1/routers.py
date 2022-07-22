from fastapi import APIRouter
from app.api.v1.endpoints import profiles
from app.api.v1.endpoints import sync_users
from app.api.v1.endpoints import users


v1 = APIRouter()
v1.include_router(profiles.router, tags=["Profiles"])
v1.include_router(sync_users.router, tags=["SyncProfiles"])
v1.include_router(users.router, tags=["Users"])



