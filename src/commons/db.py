import datetime
from typing import Union
from src.utils import object_as_dict
from sqlalchemy import update


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

    def read(self, filters: dict = {}) -> Union[m_repo.Repo, m_user.User]:
        with session() as sess:
            # create object from json

            # result = sess.query(self.model).where(**filters).all()
            result = sess.query(self.model).filter_by(**filters)

            return result

    def create(self, data: dict) -> Union[m_repo.Repo, m_user.User]:
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

    def update(self, id: int, data: dict) -> Union[m_repo.Repo, m_user.User]:
        with session() as sess:
            try:
                # find one
                # url must be unique
                sess.query(self.model).where(self.model.id == id).update(data)
                sess.commit()

                return self.read(filters={"id": id}).first()

            except Exception as e:
                raise e
