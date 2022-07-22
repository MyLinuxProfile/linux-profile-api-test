from fastapi import APIRouter, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from sqlalchemy.orm import Session

from app.controller import ControllerUser
from app.schemas.user import SchemaUser

from app.database.mysql import get_db
from app.database.nosql import db


router = APIRouter()

@router.get("/users", response_model=List[SchemaUser])
def read_users(request: Request, db: Session = Depends(get_db)):
    """
    Read Users
    """

    try:
        item = ControllerUser(db=db).get_all()
        json_compatible_item_data = jsonable_encoder(item)

        return JSONResponse(content=json_compatible_item_data)

    except Exception as error:
        print(error)
        return None

