from fastapi import APIRouter, Request, Body, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse

from typing import List
from sqlalchemy.orm import Session
from app.api.utils import validate_token
from app.database.mysql import get_db
from app.models.nosql.profile import ProfileModel, UpdateProfileModel
from app.database.nosql import db

router = APIRouter()


def validate(request: Request, myqldb: Session = Depends(get_db)):
    authorized = validate_token(request, myqldb)
    if type(authorized) == Response:
        return authorized


@router.get("/profiles/{id}",
            response_description="Get a single profile",
            response_model=ProfileModel)
async def show_profile(request: Request,
                       id: str, myqldb:
                       Session = Depends(get_db)):

    validate(request, myqldb)
    if (profile := await db["profiles"].find_one({"_id": id})) is not None:
        return profile

    raise HTTPException(status_code=404, detail=f"Profile {id} not found")


@router.put("/profiles/{id}",
            response_description="Update a profile",
            response_model=ProfileModel)
async def update_profile(request: Request,
                         id: str,
                         profile: UpdateProfileModel = Body(...),
                         myqldb: Session = Depends(get_db)):

    validate(request, myqldb)
    profile = {k: v for k, v in profile.dict().items() if v is not None}

    if len(profile) >= 1:
        update_result = await db["profiles"].update_one(
            {"_id": id}, {"$set": profile})

        if update_result.modified_count == 1:
            if (
                updated_profile := await db["profiles"].find_one({"_id": id})
            ) is not None:
                return updated_profile

    if (existing_student := await db["profiles"].find_one({"_id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.post("/profiles",
             response_description="Add new profile",
             response_model=ProfileModel)
async def create_profile(request: Request,
                         profile: ProfileModel = Body(...),
                         myqldb: Session = Depends(get_db)):

    validate(request, myqldb)

    profile = jsonable_encoder(profile)
    new_profile = await db["profiles"].insert_one(profile)
    created_profile = await db["profiles"].find_one(
        {"_id": new_profile.inserted_id})

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=created_profile)


@router.delete("/profiles/{id}", response_description="Delete a profile")
async def delete_profile(request: Request,
                         id: str,
                         myqldb: Session = Depends(get_db)):

    validate(request, myqldb)

    delete_result = await db["profiles"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Profile {id} not found")
