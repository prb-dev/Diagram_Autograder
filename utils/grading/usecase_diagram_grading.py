import spacy

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")


def compare_actors(c_aname, s_aname):
    similarity = nlp(c_aname).similarity(nlp(s_aname))
    return similarity >= 0.9


def compare_usecases(c_uname, s_uname):
    similarity = nlp(c_uname).similarity(nlp(s_uname))
    return similarity >= 0.9


def grade_actors(correct, student, rubric):
    valid_actor_count = 0
    total_actors = len(correct["actors"])

    for c_aname in correct["actors"]:
        for s_aname in student["actors"]:
            if compare_actors(c_aname, s_aname):
                valid_actor_count += 1
                break

    percentage = (valid_actor_count / total_actors) * 100
    mark = calculate_marks(rubric["criterias"][0], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_usecases(correct, student, rubric):
    valid_usecase_count = 0
    total_usecases = len(correct["usecases"])

    for c_uname in correct["usecases"]:
        for s_uname in student["usecases"]:
            if compare_usecases(c_uname, s_uname):
                valid_usecase_count += 1
                break

    percentage = (valid_usecase_count / total_usecases) * 100
    mark = calculate_marks(rubric["criterias"][1], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_actor_relationships(correct, student, rubric):
    valid_relationship_count = 0
    total_relationships = len(correct["actor_relationships"].get("generalization", []))

    for c_rel in correct["actor_relationships"]:
        for s_rel in student["actor_relationships"]:
            if compare_actors(c_rel["start"], s_rel["start"]) and compare_actors(
                c_rel["end"], s_rel["end"]
            ):
                valid_relationship_count += 1

    if total_relationships > 0:
        percentage = (valid_relationship_count / total_relationships) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][2], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_usecase_relationships(correct, student, rubric):
    valid_relationship_count = 0
    total_relationships = (
        len(correct["usecase_relationships"].get("generalization", []))
        + len(correct["usecase_relationships"].get("includes", []))
        + len(correct["usecase_relationships"].get("excludes", []))
    )

    for key in correct["usecase_relationships"]:
        for c_rel in correct["usecase_relationships"][key]:
            for s_rel in student["usecase_relationships"][key]:
                if compare_usecases(
                    c_rel["start"], s_rel["start"]
                ) and compare_usecases(c_rel["end"], s_rel["end"]):
                    valid_relationship_count += 1

    if total_relationships > 0:
        percentage = (valid_relationship_count / total_relationships) * 100
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


def get_usecase_marks(correct, student, rubric):
    marks = {}

    # Grading process and populating the marks dictionary
    marks["actors"] = grade_actors(correct, student, rubric)
    marks["usecases"] = grade_usecases(correct, student, rubric)
    marks["actor_relationships"] = grade_actor_relationships(correct, student, rubric)
    marks["usecase_relationships"] = grade_usecase_relationships(
        correct, student, rubric
    )

    marks["total"] = calculate_total(marks)

    return marks
