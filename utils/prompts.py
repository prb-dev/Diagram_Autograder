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
    "usecase": "Generate json object for this er diagram.",
}


def get_prompts(diagram_type):
    return prompts.get(diagram_type)
