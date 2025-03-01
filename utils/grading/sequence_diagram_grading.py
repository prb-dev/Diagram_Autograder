import spacy

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")


def compare_actors(c_aname, s_aname):
    similarity = nlp(c_aname).similarity(nlp(s_aname))
    return similarity >= 0.9


def compare_objects(c_oname, s_oname):
    similarity = nlp(c_oname).similarity(nlp(s_oname))
    return similarity >= 0.9


def compare_messages(c_message, s_message):
    similarity = nlp(c_message).similarity(nlp(s_message))
    return similarity >= 0.9


def compare_items(c_item, s_item):
    similarity = nlp(c_item).similarity(nlp(s_item))
    return similarity >= 0.9


def grade_actors(correct, student, rubric):
    valid_actor_count = 0
    total_actors = len(correct.get("actors", []))

    for c_actor in correct["actors"]:
        for s_actor in student["actors"]:
            if compare_actors(c_actor, s_actor):
                valid_actor_count += 1
                break

    if total_actors > 0:
        percentage = (valid_actor_count / total_actors) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][0], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_objects(correct, student, rubric):
    valid_object_count = 0
    total_objects = len(correct.get("objects", []))

    for c_object in correct["objects"]:
        for s_object in student["objects"]:
            if compare_objects(c_object, s_object):
                valid_object_count += 1
                break

    if total_objects > 0:
        percentage = (valid_object_count / total_objects) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][1], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_messages(correct, student, rubric):
    valid_message_count = 0
    total_messages = len(correct.get("messages", []))

    matched_indices = set()

    for c_message in correct["messages"]:
        for i, s_message in enumerate(student["messages"]):
            if i in matched_indices:
                continue

            if (
                compare_messages(c_message["message"], s_message["message"])
                and compare_items(c_message["from"], s_message["from"])
                and compare_items(c_message["to"], s_message["to"])
                and c_message["time"] == s_message["time"]
                and c_message["type"] == s_message["type"]
            ):
                valid_message_count += 1
                matched_indices.add(i)
                break

    if total_messages > 0:
        percentage = (valid_message_count / total_messages) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][2], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_lifelines(correct, student, rubric):
    valid_lifeline_count = 0
    total_lifelines = len(correct.get("lifelines", []))

    matched_indices = set()

    for c_lifeline in correct["lifelines"]:
        for i, s_lifeline in enumerate(student["lifelines"]):
            if i in matched_indices:
                continue

            if (
                compare_items(c_lifeline["entity"], s_lifeline["entity"])
                and c_lifeline["start_time"] == s_lifeline["start_time"]
                and c_lifeline["end_time"] == s_lifeline["end_time"]
            ):
                valid_lifeline_count += 1
                matched_indices.add(i)
                break

    if total_lifelines > 0:
        percentage = (valid_lifeline_count / total_lifelines) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][3], percentage)

    return {"correctness": percentage, "mark": mark}


def calculate_marks(rubric_criteria, percentage):
    for range_item in rubric_criteria["marks_ranges"]:
        if range_item["range"][0] <= percentage <= range_item["range"][1]:
            return range_item["marks"]
    return 0


def calculate_total(marks):
    total = sum(criteria["mark"] for criteria in marks.values())
    return total


def get_sequence_marks(correct, student, rubric):
    marks = {}

    # Grading process and populating the marks dictionary
    marks["actors"] = grade_actors(correct, student, rubric)
    marks["objects"] = grade_objects(correct, student, rubric)
    marks["messages"] = grade_messages(correct, student, rubric)
    marks["lifelines"] = grade_lifelines(correct, student, rubric)

    marks["total"] = calculate_total(marks)

    return marks
