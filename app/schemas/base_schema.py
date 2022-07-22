from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base Schema
    """

    class Config:
        orm_mode = True

