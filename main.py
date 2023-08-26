# from fastapi import FastAPI
# import strawberry
# from strawberry.fastapi import GraphQLRouter
#
# # import schemas here
#
# graphql_app = GraphQLRouter()
# app = FastAPI()
#
# app.include_router(graphql_app, prefix="/graphql")
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from src.repo import repo_schema

# Mount Ariadne GraphQL as sub-application for FastAPI
app = FastAPI()

app.mount("/graphql/", GraphQL(repo_schema, debug=True))
