from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()

@router.get("/users")
def read_users():
    """Read Users
    """
    return Response(status_code=401)
