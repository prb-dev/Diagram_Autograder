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
    "er": "Generate json object for this er diagram.",
    "sequence": "Generate json object for this sequence diagram.",
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
}


def get_prompts(diagram_type):
    return prompts.get(diagram_type)
