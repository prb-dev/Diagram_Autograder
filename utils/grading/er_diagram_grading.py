import spacy

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")


def compare_entities(c_ename, s_ename):
    similarity = nlp(c_ename).similarity(nlp(s_ename))
    return similarity >= 0.9


def compare_attributes(c_aname, s_aname):
    similarity = nlp(c_aname).similarity(nlp(s_aname))
    return similarity >= 0.9


def compare_relationships(c_rname, s_rname):
    similarity = nlp(c_rname).similarity(nlp(s_rname))
    return similarity >= 0.9


def grade_entities(correct, student, rubric):
    valid_entity_count = 0
    total_entities = len(correct.get("entities", []))

    for c_entity in correct["entities"]:
        for s_entity in student["entities"]:
            if compare_entities(c_entity["name"], s_entity["name"]):
                valid_entity_count += 1
                break

    if total_entities > 0:
        percentage = (valid_entity_count / total_entities) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][0], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_attributes(correct, student, rubric):
    valid_attribute_count = 0
    total_attributes = sum(
        len(c_entity.get("attributes", [])) for c_entity in correct["entities"]
    )

    for c_entity in correct["entities"]:
        for s_entity in student["entities"]:
            if compare_entities(c_entity["name"], s_entity["name"]):
                for c_aname in c_entity.get("attributes", []):
                    for s_aname in s_entity.get("attributes", []):
                        if compare_attributes(c_aname, s_aname):
                            valid_attribute_count += 1
                            break

    if total_attributes > 0:
        percentage = (valid_attribute_count / total_attributes) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][1], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_relationships(correct, student, rubric):
    valid_relationship_count = 0
    total_relationships = len(correct.get("relationships", []))

    for c_rel in correct["relationships"]:
        for s_rel in student["relationships"]:
            if (
                compare_relationships(c_rel["name"], s_rel["name"])
                and c_rel["cardinality"] == s_rel["cardinality"]
            ):

                entity_match_count = 0

                for c_ename in c_rel["entities"]:
                    for s_ename in s_rel["entities"]:
                        if compare_entities(c_ename, s_ename):
                            entity_match_count += 1

                if entity_match_count == len(c_rel["entities"]):
                    valid_relationship_count += 1

    if total_relationships > 0:
        percentage = (valid_relationship_count / total_relationships) * 100
    else:
        percentage = 100
    mark = calculate_marks(rubric["criterias"][2], percentage)

    return {"correctness": percentage, "mark": mark}


def calculate_marks(rubric_criteria, percentage):
    for range_item in rubric_criteria["marks_ranges"]:
        if range_item["range"][0] <= percentage <= range_item["range"][1]:
            return range_item["marks"]
    return 0


def calculate_total(marks):
    total = sum(criteria["mark"] for criteria in marks.values())
    return total


def get_er_marks(correct, student, rubric):
    marks = {}

    # Grading process and populating the marks dictionary
    marks["entities"] = grade_entities(correct, student, rubric)
    marks["attributes"] = grade_attributes(correct, student, rubric)
    marks["relationships"] = grade_relationships(correct, student, rubric)

    marks["total"] = calculate_total(marks)

    return marks
