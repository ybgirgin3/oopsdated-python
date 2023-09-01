from ariadne.asgi import GraphQL
from fastapi import FastAPI

from src.repo import repo_schema
from src.commons import _create_table

try:
    _create_table()
except Exception as e:
    pass

app = FastAPI()

app.mount("/graphql/", GraphQL(repo_schema, debug=True))
