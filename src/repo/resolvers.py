from ariadne import ObjectType, QueryType

# Map resolver functions to Query fields using QueryType
query = QueryType()


# Map resolver functions to custom type fields using ObjectType
repo = ObjectType("Repo")


# alias for queries
@repo.field("fullname")
def resolve_repo_fullname(repo, *_):
    return "%s/%s" % (repo["owner"], repo["name"])


# seed
@query.field("repos")
def resolve_repo(*_):
    return [
        {
            "name": "react-native",
            "owner": "Facebook",
            "url": "https://www.github.com/facebook/react-native",
        },
    ]
