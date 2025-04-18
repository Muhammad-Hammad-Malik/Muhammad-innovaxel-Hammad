from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId


# Helper to handle Mongo's _id field with Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Model for reading from DB
class URLModel(BaseModel):
    id: str = Field(alias="shortCode")  # Use shortCode as id
    url: HttpUrl
    shortCode: str
    createdAt: datetime
    updatedAt: datetime
    accessCount: int = 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


# Model for creating a new URL (client-side input)
class URLCreate(BaseModel):
    url: HttpUrl
