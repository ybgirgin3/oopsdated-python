from typing import Dict

from ariadne import ObjectType, QueryType, MutationType

from src.commons.db import DBProcess
from src.models import repo

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


# ---- MUTATIONS
def resolver_create(_, data: Dict):
    return dbp.create(data=data)
