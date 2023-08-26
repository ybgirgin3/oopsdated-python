from ariadne import ObjectType, QueryType

from src.commons.db import DBProcess
from src.models import user

dbp = DBProcess(model=user.User)

# Map resolver functions to Query fields using QueryType
query = QueryType()


# Map resolver functions to custom type fields using ObjectType
repo = ObjectType("User")


@query.field("user")
def resolve_user(*_):
    return dbp.read()
