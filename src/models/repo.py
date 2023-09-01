import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Repo(Base):
    __tablename__ = "repo"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(String)
    url = Column(String)
    subscribers = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
