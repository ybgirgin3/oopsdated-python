from pydantic import BaseModel
from typing import Optional


class IRepo(BaseModel):
    id: int
    name: str
    owner: str
    url: str


class IRepoUpdate(BaseModel):
    name: Optional[str]
    owner: Optional[str]
    url: Optional[str]
