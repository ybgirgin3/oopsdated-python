from typing import Optional

from pydantic import BaseModel


class IRepo(BaseModel):
    id: int
    name: str
    owner: str
    url: str
    subscribers: list[str]


class IRepoUpdate(BaseModel):
    name: Optional[str]
    owner: Optional[str]
    url: Optional[str]
    subscribers: Optional[list[str]]
