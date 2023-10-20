from ariadne import make_executable_schema
from src.graphql_app.define_types import type_defs
from src.graphql_app.resolvers import full_event
from ariadne.asgi import GraphQL

schema = make_executable_schema(type_defs, full_event)

app = GraphQL(schema, debug=True)
