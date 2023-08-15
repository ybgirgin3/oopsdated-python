import datetime
import uuid

from pydantic import BaseModel, Field


class User(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    created_at: str = datetime.datetime.now()
    updated_at: str = datetime.datetime.now()
