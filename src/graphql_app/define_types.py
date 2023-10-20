from ariadne import gql



type_defs = gql("""

    scalar ResponseEvent

    type Query {
        get_full_event(id: Int): ResponseEvent
    }
#
#     type Event {
#         id: Int,
#         title: String,
#         content: String,
#         dresscode: String,
#         event_type: EventType!
#     }
# 
#     type EventType {
#         id: Int,
#         name: String
#     }
""")
