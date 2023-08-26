from ariadne import load_schema_from_path
from ariadne import make_executable_schema

from src.repo.resolvers import query, mutation, repo

type_defs = load_schema_from_path("src/graphql")


# Create executable GraphQL schema
# repo_schema = make_executable_schema(type_defs, query, repo)
repo_schema = make_executable_schema(type_defs, [query, mutation], repo)
