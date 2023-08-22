import strawberry
from bson import ObjectId
from enum import Enum
import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base

@strawberry.enum
class IsUserActive(str, Enum):
    inactive = '0'
    active = '1'


class User(Base):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=True, unique=True)
    email: str = Colun(String, nullable=False)


    # datetime type, auto-generated & required
    created_at: datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.datetime.utcnow)

    # is user active
    is_active: IsUserActive = IsUserActive.active

    repos = relationship('Repo', cascade='all')
