from ariadne import make_executable_schema
from src.graphql_app.define_types import type_defs
from src.graphql_app.resolvers.resolvers_query import query
from src.graphql_app.resolvers.resolvers_event import event
from src.graphql_app.resolvers.resolvers_event_type import eventtype
from ariadne.asgi import GraphQL

schema = make_executable_schema(type_defs, query, event, eventtype)


app = GraphQL(schema, debug=True)
