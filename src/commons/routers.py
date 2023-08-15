from typing import Union

from fastapi import Request

from src.db import db_service
from src.models import repo, user


class CommonRouteController:
    def __init__(self, table) -> None:
        self.table = table

    async def _findall(self, req: Request, limit: int = 10):
        # return 'generic find all'
        return db_service.find_all(request=req,
                                   tablename=self.table,
                                   limit=limit)

    async def _findone(self, req: Request, _id: str):
        # return 'generic find one'
        return db_service.find_by_id(request=req,
                                     _id=_id,
                                     tablename=self.table)

    async def _update_one(self,
                          req: Request,
                          _id: str,
                          body: Union[repo.Repo, user.User]):
        # return 'generic update one'
        return db_service.update(request=req,
                                 _id=_id,
                                 tablename=self.table,
                                 body=body)

    async def _create(self, req: Request, body: Union[repo.Repo, user.User]):
        # return 'generic create'
        return db_service.create(request=req,
                                 tablename=self.table,
                                 body=body)

    async def _delete_one(self, req: Request, _id: str):
        # return 'generic delete one'
        return db_service.delete_by_id(request=req,
                                       tablename=self.table,
                                       _id=_id)
