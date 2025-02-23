prompts = {
    "class": (
        "Please generate a JSON object for the following class diagram. The JSON object should include:\n\n"
        "- `classnames`: A list of all class names in the diagram.\n"
        "- `attributes`: A list of attributes for each class, where each attribute has:\n"
        "  - `class`: The name of the class the attribute belongs to.\n"
        "  - `name`: The name of the attribute.\n"
        "  - `accessmodifier`: The access modifier of the attribute (e.g., public, private, protected).\n"
        "- `methods`: A list of methods for each class, where each method has:\n"
        "  - `class`: The name of the class the method belongs to.\n"
        "  - `name`: The name of the method.\n"
        "  - `accessmodifier`: The access modifier of the method (e.g., public, private, protected).\n"
        "- `relationships`: A list of relationships between classes, where each relationship includes:\n"
        "  - `type`: The type of relationship (e.g., inheritance, association, aggregation).\n"
        "  - `start`: The name of the starting class.\n"
        "  - `end`: The name of the ending class."
    ),
    "usecase": (
        "Please generate a JSON object as the response for the following use case diagram. The JSON object should include:\n\n"
        "- `actors`: A list of all actors in the diagram.\n"
        '  Example: `actors`: ["a", "b"]\n'
        "- `usecases`: A list of all use cases in the diagram.\n"
        '  Example: `usecases`: ["c", "d", "e", "f", "g", "h"]\n'
        "- `actor_relationships`: A list of relationships between actors, where each relationship specifies:\n"
        "  - `generalization`: Represents an inheritance relationship between actors, with:\n"
        "    - `start`: The name of the parent actor.\n"
        "    - `end`: The name of the child actor.\n"
        '  Example: `actor_relationships`: {"generalization": [{"start": "a", "end": "b"}]}\n'
        "- `usecase_relationships`: A list of relationships between use cases, categorized by type, where each type includes:\n"
        "  - `generalization`: Represents an inheritance relationship between use cases, with:\n"
        "    - `start`: The name of the parent use case.\n"
        "    - `end`: The name of the child use case.\n"
        '  - `includes`: Represents an "include" relationship, with:\n'
        "    - `start`: The name of the use case that includes another.\n"
        "    - `end`: The name of the included use case.\n"
        '  - `excludes`: Represents an "exclude" relationship, with:\n'
        "    - `start`: The name of the use case that excludes another.\n"
        "    - `end`: The name of the excluded use case.\n"
        "  Example: `usecase_relationships`: {\n"
        '    "generalization": [{"start": "c", "end": "d"}],\n'
        '    "includes": [{"start": "e", "end": "f"}],\n'
        '    "excludes": [{"start": "g", "end": "h"}]\n'
        "  }"
    ),
    "er": (
        "Please generate a JSON object as the response for the following ER diagram using the specified format. The JSON object should include:\n\n"
        "- `entities`: A list of all entities in the diagram, where each entity has:\n"
        "  - `name`: The name of the entity (e.g., Student, Course).\n"
        "  - `primary_key`: The primary key that uniquely identifies the entity (e.g., Student_ID).\n"
        "  - `attributes`: A list of attributes for the entity (e.g., Name, Age).\n"
        "- `relationships`: A list of relationships between entities, where each relationship has:\n"
        "  - `start`: The name of the starting entity (e.g., Student).\n"
        "  - `end`: The name of the ending entity (e.g., Course).\n"
        "  - `name`: The name of the relationship (e.g., Enrolls In).\n"
        "  - `cardinality`: The cardinality of the relationship (e.g., one-to-many, many-to-many)."
    ),
    "sequence": (
        "Please generate a JSON object as the response for the following sequence diagram using the specified format. The JSON object should include:\n\n"
        "- `actors`: A list of all actors involved in the sequence diagram.\n"
        '  Example: actors: ["Actor1", "Actor2"]\n'
        "- `objects`: A list of all objects or components involved in the sequence diagram.\n"
        '  Example: objects: ["Object1", "Object2", "Object3"]\n'
        "- `messages`: A list of messages exchanged between actors and objects. Each message should contain:\n"
        "  - `from`: The entity sending the message (actor or object).\n"
        "  - `to`: The entity receiving the message (actor or object).\n"
        '  - `message`: A short description of the message being passed (e.g., "Request Data").\n'
        "  - `type`: The type of message (synchronous or asynchronous).\n"
        "  - `time`: The timestamp when the message is exchanged.\n"
        "  Example:\n"
        '  {"from": "Actor1", "to": "Object1", "message": "Request Data", "type": "synchronous", "time": "t1"}\n'
        "- `lifelines`: A list of lifelines, each representing an entity's participation in the sequence. Each lifeline should include:\n"
        "  - `entity`: The name of the entity (actor or object).\n"
        "  - `start_time`: The time when the entity starts participating in the sequence.\n"
        "  - `end_time`: The time when the entity stops participating in the sequence.\n"
        "  Example:\n"
        '  {"entity": "Actor1", "start_time": "t0", "end_time": "t2"}'
    ),
}


def get_prompts(diagram_type):
    return prompts.get(diagram_type)
