from ariadne import gql



type_defs = gql("""

    scalar ResponseEvent
    scalar ResponseEventType

    type Query {
        get_full_event(id: Int): ResponseEvent
        get_event_type(id: Int): EventType
        get_event(id: Int): Event
    }

    type Event {
        title(id: Int): String,
        content(id: Int): String,
        dresscode(id: Int): String,
        event_type(id: Int): EventType!
    }
    
    type EventType {
        event_type: ResponseEventType
    }
""")
