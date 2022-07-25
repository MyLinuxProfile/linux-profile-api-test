from fastapi import Request
from sqlalchemy.orm import Session

from fastapi.responses import Response
from app.core.mysql import ControllerUser


def validate_token(req: Request, db: Session):
    """Validate Token
    """
    email = req.headers.get("email")
    token = req.headers.get("x-token")

    operation = ControllerUser(db)
    query_token = operation.get_token(email=email, token=token)

    if not token:
        return Response(status_code=401)

    if not query_token:
        return Response(status_code=401)

    return query_token.id
