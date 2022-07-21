import motor.motor_asyncio

from os import getenv
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(getenv("DATABASE_NOSQL"))
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

