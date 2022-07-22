from fastapi import APIRouter, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from sqlalchemy.orm import Session

from app.controller import  ControllerSyncUser
from app.schemas.sync_user import SchemaSyncUser

from app.database.mysql import get_db
from app.database.nosql import db

router = APIRouter()


@router.get("/sync_profiles", response_model=List[SchemaSyncUser])
def read_profiles(request: Request, db: Session = Depends(get_db)):
    """
    Read Profiles
    """

    try:
        item = ControllerSyncUser(db=db).get_all()
        json_compatible_item_data = jsonable_encoder(item)
    
        return JSONResponse(content=json_compatible_item_data)      

    except Exception as error:
        print(error)
        return None

