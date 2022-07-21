from fastapi import APIRouter
from typing import List
from app.models.nosql.profile import ProfileModel
from app.database.nosql import db

router  = APIRouter()

@router.get("/profiles", response_description="List all profiles", response_model=List[ProfileModel])
async def list_profiles():
    students = await db["profiles"].find().to_list(1000)
    return students

