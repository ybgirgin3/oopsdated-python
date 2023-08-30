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
def resolve_repos(_, info, filters: dict = {}):
    """Get Repo/Get Single Repo resolver

    Args:
        _ (_type_): _description_
        info (_type_): _description_
        filters (dict, optional): Filters querying repos. Defaults to {}.

    Returns:
        _type_: type of Repo
    """
    return dbp.read(filters=filters).all()


# ---- MUTATIONS
@mutation.field("create_repo")
def resolver_create(_, info, repo_input):
    """Create Repo Resolver

    Args:
        _ (_type_): _description_
        info : _description_
        repo_input (dict): repo input (must)

    Returns:
        _type_: type of Repo
    """
    return dbp.create(data=repo_input)


@mutation.field("update_repo")
def resolver_update(_, info, id, update_repo_input):
    print("update_repo_input: ", update_repo_input)
    return dbp.update(id, update_repo_input)
