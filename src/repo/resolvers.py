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
def resolve_repos(*_, filters):
    print("filter in repos", filters)
    return dbp.read(filters=filters)


# @query.field("repo")
# def resolve_single_repo(_, info, where):
#     print("where in single repo: ", where)
#     # return dbp.read(filter=where)


# ---- MUTATIONS
@mutation.field("create_repo")
def resolver_create(_, info, repo_input):
    """
    __summary__: create resolver for graphql query
    """
    return dbp.create(data=repo_input)


@mutation.field("update_repo")
def resolver_update(_, info, id, update_repo_input):
    print("update repo input type:", type(update_repo_input), "info: ", info)
    # return dbp.update()
