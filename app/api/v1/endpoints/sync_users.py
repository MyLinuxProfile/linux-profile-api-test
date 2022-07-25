from fastapi import APIRouter, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse

from typing import List

from sqlalchemy.orm import Session

from app.core.mysql import  ControllerSyncUser
from app.schemas.sync_user import SchemaSyncUser

from app.api.utils import validate_token
from app.database.mysql import get_db
from app.database.nosql import db
from upy_error import format_exception

router = APIRouter()


@router.get("/sync_profiles", response_model=List[SchemaSyncUser])
def read_profiles(request: Request, db: Session = Depends(get_db)):
    """
    Read Profiles
    """
    authorized = validate_token(request, db)

    if type(authorized) == Response:
        return authorized

    try:
        item = ControllerSyncUser(db=db, user_id=authorized).get_all()
        json_compatible_item_data = jsonable_encoder(item)
    
        return JSONResponse(content=json_compatible_item_data)      

    except Exception as error:
        print(format_exception(error))

