from typing import Optional

from pydantic import BaseModel


class IRepo(BaseModel):
    id: int
    name: str
    owner: str
    url: str


class IRepoUpdate(BaseModel):
    name: Optional[str]
    owner: Optional[str]
    url: Optional[str]
