import strawberry
from enum import Enum
from bson import ObjectId
import datetime
from typing import List
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from src.graphql.models import Base

@strawberry.enum
class IsRepoActive(str, Enum):
    inactive = '0'
    active = '1'


class Repo(Base):
    __tablename__ = 'repos'
    id: int = Column(Integer, primary_key=True, index=True)
    url: str = Column(String, nullable=True)
    files: str = Column(String, nullable=False)     # gotta be list

    # datetime type, auto-generated & required
    created_at: datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.datetime.utcnow)

    # is repo active
    is_active: IsLinkActive = IsLinkActive.active

    def as_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'files': self.files,
            'is_active': self.is_active
        }
