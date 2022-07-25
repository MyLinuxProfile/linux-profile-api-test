from fastapi import APIRouter, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse

from typing import List

from sqlalchemy.orm import Session

from app.core.mysql import ControllerUser
from app.schemas.user import SchemaUser

from app.api.utils import validate_token
from app.database.mysql import get_db
from app.database.nosql import db
from upy_error import format_exception

router = APIRouter()

@router.get("/users", response_model=List[SchemaUser])
def read_users(request: Request, db: Session = Depends(get_db)):
    """Read Users
    """
    authorized = validate_token(request, db)

    if type(authorized) == Response:
        return authorized

    try:
        item = ControllerUser(db=db).get_all()
        json_compatible_item_data = jsonable_encoder(item)

        return JSONResponse(content=json_compatible_item_data)

    except Exception as error:
        print(format_exception(error))
