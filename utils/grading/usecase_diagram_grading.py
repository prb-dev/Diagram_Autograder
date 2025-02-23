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

    percentage = (valid_usecase_count / total_usecases) * 100
    mark = calculate_marks(rubric["criterias"][1], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_actor_relationships(correct, student, rubric):
    valid_count = 0
    total_relationships = len(correct["actor_relationships"])

    for c_rel in correct["actor_relationships"]:
        for s_rel in student["actor_relationships"]:
            if (
                c_rel["type"] == s_rel["type"]
                and compare_classnames(c_rel["start"], s_rel["start"])
                and compare_classnames(c_rel["end"], s_rel["end"])
            ):
                valid_count += 1

    percentage = (valid_count / total_relationships) * 100
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
