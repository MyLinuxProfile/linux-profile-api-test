from pydantic import BaseModel, Field
from bson import ObjectId
from app.database.nosql import PyObjectId

class ProfileModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    pretty_name: str = Field(...)
    name: str = Field(...)
    version: str = Field(...)
    version_id: str = Field(...)
    version_codename: str = Field(...)
    linux_id: str = Field(...)
    linux_id_like: str = Field(...)
    
    class Config:
        aloow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
                "example": {
                    "pretty_name": "Ubuntu 21.10",
                    "name": "Ubuntu",
                    "version": "21.10 (Impish Indri)",
                    "version_id": "21.10",
                    "version_codename": "21.10 (Impish Indri)",
                    "linux_id": "ubuntu",
                    "linux_id_like": "debian",
                    "info_terminal": [],
                    "info_packages": []
                    }
                }

