import datetime
from typing import Union

from bson import ObjectId
from fastapi import Request, HTTPException, status
from fastapi.encoders import jsonable_encoder

from src.models.repo import Repo
from src.models.user import User


def _get_collection(request: Request, tablename: str):
    """
    ! will be a private function
    :param request:
    :return:
    """
    return request.app.database[tablename]


def is_exists(request: Request, model: Union[Repo, User], tablename: str):
    _is_exists = None

    if tablename == 'repo':
        _is_exists = {
            'owner': model.get('owner'),
            'reponame': model.get('reponame'),
            'files': model.get('files'),
            'created_at': model.get('created_at')
        }
    if tablename == 'user':
        _is_exists = {
            'name': model.get('name'),
            'email': model.get('email'),
            'created_at': model.get('created_at')
        }

    # tn = 'repo' if body is Repo else 'user'
    # tn = 'repo' if model == Repo else 'user'

    return _get_collection(request, tablename).find_one(
        _is_exists
    )


async def create(request: Request, tablename: str, body: Union[Repo, User]):
    """
    __summary_: create post if not exists
    :param tablename:
    :param body:
    :param request:
    :param post:
    :return: Post | HttpException
    """
    # serialize post object
    body = jsonable_encoder(body)
    # tn = 'repo' if body is Repo else 'user'

    if d := is_exists(request, body):
        """ if data already exists return existing data """
        return d

    new_item = _get_collection(
        request=request, tablename=tablename).insert_one(body)
    return _get_collection(request, tablename).find_one({"_id": new_item.inserted_id})


async def update(request: Request, _id: str, tablename: str, body: Union[Repo, User]):
    """
    __summary__: update post if exists if not raise 404
    :param tablename:
    :param request:
    :param id:
    :param post:
    :return: Post | HttpException
    """

    # tn = 'repo' if body is Repo else 'user'

    body = {k: v for k, v in body.model_dump().items() if v is not None}
    body['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if len(body) >= 1:
        try:
            _get_collection(request, tablename).find_one_and_update(
                {"_id": ObjectId(_id)}, {"$set": body})
            if (existing_item := _get_collection(request, tablename).find_one({"_id": ObjectId(_id)})) is not None:
                return existing_item
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Data Not Found!')


async def find_all(request: Request, tablename: str, limit: int = 10):
    """
    __summary__:
    :param tablename:
    :param request:
    :param limit:
    :return:  List[Posts]
    """
    return list(_get_collection(request, tablename).find(limit=limit))


async def find_by_id(request: Request, tablename: str, _id: str):
    """
    __summary__: find a post by id
    :param tablename:
    :param request:
    :param id:
    :return: Post | HttpException
    """
    if post := _get_collection(request, tablename).find_one({"_id": ObjectId(_id)}):
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='Post Not Found!')


async def delete_by_id(request: Request, tablename: str, _id: str):
    try:
        deleted_post = _get_collection(
            request, tablename).find_one_and_delete({"_id": ObjectId(_id)})
        return f'Post with {_id} deleted successfully'
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
