import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

# to return
from sqlalchemy.orm import Session

from src.models import repo, user


class UnknownDBError(Exception):
    pass


SQL_ALCHEMY_ENGINES = {
    "oopsdated": create_engine(
        f"sqlite:///{os.getcwd()}/database.db",
        echo=False,
    )
}


def _create_table(db_engine: Engine = SQL_ALCHEMY_ENGINES["oopsdated"]):
    # example usage: _create_table("Sites", SQL_ALCHEMY_ENGINES['sites'])

    # model = getattr(schemas, model)
    # model.__table__.create(db_engine)

    repo.Repo.__table__.create(db_engine)
    user.User.__table__.create(db_engine)


def engine(db_name: str = "oopsdated") -> Engine:
    try:
        return SQL_ALCHEMY_ENGINES[f"{db_name}"]
    except KeyError:
        raise UnknownDBError


def session(db_name: str = "oopsdated") -> Session:
    return Session(engine(db_name), expire_on_commit=False)
