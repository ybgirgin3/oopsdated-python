from typing import Dict

from ariadne import ObjectType, QueryType, MutationType

from src.commons.db import DBProcess
from src.models import repo
from src.interfaces.repo import IRepo

dbp = DBProcess(model=repo.Repo)

# Map resolver functions to Query fields using QueryType
query = QueryType()
mutation = MutationType()

# Map resolver functions to custom type fields using ObjectType
repo = ObjectType("Repo")


# ---- QUERIES
@query.field("repo")
def resolve_repo(*_):
    return dbp.read()

    # name
    # owner
    # url


# ---- MUTATIONS
@mutation.field("create_repo")
def resolver_create(_, info, repo_input):
    # def resolver_create(_, name: str, owner: str, url: str):
    #     return dbp.create(data={"name": name, "owner": owner, "url": url})
    return dbp.create(data=repo_input)
