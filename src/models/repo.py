import datetime
import uuid
from typing import Optional, List

from pydantic import BaseModel, Field


class Repo(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    owner: str
    reponame: str
    files: List[str]
    created_at: str = datetime.datetime.now()
    updated_at: str = datetime.datetime.now()

    # person info
    # personId: int
    # person?: Person[];


class UpdatedRepo(BaseModel):
    owner: Optional[str]
    reponame: Optional[str]
    files: Optional[List[str]]
