import strawberry
from enum import Enum
from bson import ObjectId
import datetime
from pydantic import (
    BaseModel,
    Field,
    AnyHttpUrl
)
from typing import List


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
class IsLinkActive(str, Enum):
    inactive = '0'
    active = '1'


class Repo(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")  # Model id
    url: AnyHttpUrl | None = Field(...)
    files: List[str]

    # datetime type, auto-generated & required
    created_at: datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.datetime.utcnow)

    # is link active
    is_active: IsLinkActive = IsLinkActive.active
