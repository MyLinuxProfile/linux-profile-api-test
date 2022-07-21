from typing import Optional
from app.schemas.base_schema import BaseSchema


class SchemaUserBase(BaseSchema):
    name: Optional[str] = None
    email: Optional[str] = None
    token: Optional[str] = None


class SchemaUserCreate(SchemaUserBase):
    pass


class SchemaUser(SchemaUserBase):
    id: int

