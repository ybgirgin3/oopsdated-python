import datetime
from typing import Union, Dict

from src.commons import session
from src.models import repo, user


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

    def __init__(self, model: Union[repo.Repo, user.User]) -> None:
        self.model = model

    def read(self, filters: Dict = None):
        with session() as sess:
            # create object from json
            _where = True if not filters else filters
            result = sess.query(self.model).where(_where).all()
            return result

    def create(self, data: Dict):
        with session() as sess:
            try:
                now = datetime.datetime.today()
                data["created_at"] = now
                data["updated_at"] = now
                obj = self.model(**data)
                sess.add(obj)
                sess.commit()
                return data
            except Exception as e:
                raise e
