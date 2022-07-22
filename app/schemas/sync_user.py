from typing import Optional
from app.schemas.base_schema import BaseSchema


class SchemaSyncUserBase(BaseSchema):
    user_id: Optional[str] = None
    profile_id: Optional[str] = None


class SchemaSyncUserCreate(SchemaSyncUserBase):
    pass


class SchemaSyncUser(SchemaSyncUserBase):
    id: int

