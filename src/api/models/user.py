import strawberry
from bson import ObjectId
from enum import Enum
import datetime

from pydantic import BaseModel, Field, EmailStr


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


@strawberry.enum
class IsUserActive(str, Enum):
    inactive = '0'
    active = '1'


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")  # Model id
    name: str
    email: EmailStr = Field(...)

    # datetime type, auto-generated & required
    created_at: datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.datetime.utcnow)

    # is user active
    is_active: IsUserActive = IsUserActive.active
