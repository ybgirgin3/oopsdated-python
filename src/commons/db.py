import datetime
from typing import Union, Dict

from src.commons import session
from src.models import repo as m_repo, user as m_user


class DBProcess:
    """
    USAGE:
    In [3]: from src.models import repo
    In [4]: from src.commons import DBProcess
    In [5]: dbp = DBProcess(repo.Repo)
    In [6]: dbp.read()
    Out[6]: repos # str

    """

    # m = {"repo": repo.Repo, "user": user.User}

    def __init__(self, model: Union[m_repo.Repo, m_user.User]) -> None:
        self.model = model

    def read(self, filters: dict = True) -> Union[m_repo, m_user]:
        with session() as sess:
            # create object from json

            result = sess.query(self.model).where(filters).all()

            return result

    def create(self, data: dict) -> Union[m_repo, m_user]:
        with session() as sess:
            try:
                now = datetime.datetime.today()
                data["created_at"] = now
                data["updated_at"] = now

                obj = self.model(**data)
                sess.add(obj)
                sess.commit()

                return obj
            except Exception as e:
                raise e

    def update(self, id: int, data: dict) -> Union[m_repo, m_user]:
        with session() as sess:
            try:
                # find one
                # url must be unique
                result = self.read(filters="")

                data["updated_at"] = datetime.datetime.today()
                result.update(data)

                obj = self.model(**data)
                sess.add(obj)
                sess.commit()

                return obj

            except Exception as e:
                raise e
