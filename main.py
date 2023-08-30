from ariadne.asgi import GraphQL
from fastapi import FastAPI

from src.repo import repo_schema

app = FastAPI()

app.mount("/graphql/", GraphQL(repo_schema, debug=True))
