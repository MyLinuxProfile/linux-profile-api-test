import motor.motor_asyncio

from bson import ObjectId
from settings import NOSQL_DATABASE_URL

client = motor.motor_asyncio.AsyncIOMotorClient(NOSQL_DATABASE_URL)
db = client.linux


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

