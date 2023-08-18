from typing import List

from fastapi import APIRouter, Request, status

from src.commons.routers import CommonRouteController
from src.models import repo

# commons route controller
crc = CommonRouteController(table='repos')

# define a router
router = APIRouter(prefix='/repo', tags=['repository'])


@router.get('/all', response_description='get all repo', response_model=list[repo.Repo])
async def findall(req: Request):
    """
    __summary__: Find all posts from db
    :param req: Request => GET
    :return: List of posts
    """
    # return await db_service.find_all(req, 10)
    return await crc._findall(req, 10)


@router.get('/find', response_description='get a repo', response_model=repo.Repo)
async def findone(req: Request, id: str):
    """
    ___summary__: Find a Post with given id
    :param req:
    :param id:
    :return: Posts
    """
    # return await db_service.find_by_id(req, id)
    return await crc._findone(req, id)


@router.put('/update/', response_description='update a repo', response_model=repo.UpdatedRepo)
async def update_one(req: Request, id: str, body: repo.UpdatedRepo):
    """
    __summary__: Update a post
    :param req:
    :param id:
    :param post: UpdatePost
    :return: post
    """
    # return await db_service.update_post(req, id, post)
    return await crc._update_one(req, id, body)


@router.post('/create', response_description='create repo', response_model=repo.Repo,
             status_code=status.HTTP_201_CREATED)
async def create(req: Request, body: repo.Repo):
    """
    __summary__: create a post
    :param req:
    :param post:
    :return:
    """
    # return await db_service.create_post(req, post)
    return await crc._create(req, body)


@router.delete('/{id}', response_description='delete a repo')
async def delete_one(req: Request, id: str):
    """
    __summary__: Delete a post by id
    :param: req:
    :param: id:
    :return:
    """
    # return await db_service.delete_by_id(req, id)
    return await crc._delete_one(req, id)
