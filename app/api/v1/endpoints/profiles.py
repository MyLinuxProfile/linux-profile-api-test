from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse

from typing import List
from app.models.nosql.profile import ProfileModel
from app.database.nosql import db

router  = APIRouter()


@router.get("/profiles", response_description="List all profiles", response_model=List[ProfileModel])
async def list_profiles():
    profiles = await db["profiles"].find().to_list(1000)

    return profiles


@router.get("/profiles/{id}", response_description="Get a single profile", response_model=ProfileModel)
async def show_profile(id: str):
    if (profile := await db["profiles"].find_one({"_id": id})) is not None:
        return profile

    raise HTTPException(status_code=404, detail=f"Profile {id} not found")


@router.post("/profiles", response_description="Add new profile", response_model=ProfileModel)
async def create_profile(profile: ProfileModel = Body(...)):
    profile = jsonable_encoder(profile)
    new_profile = await db["profiles"].insert_one(profile)
    created_profile = await db["profiles"].find_one({"_id": new_profile.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_profile)


@router.delete("/profiles/{id}", response_description="Delete a profile")
async def delete_profile(id: str):
    delete_result = await db["profiles"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Profile {id} not found")

