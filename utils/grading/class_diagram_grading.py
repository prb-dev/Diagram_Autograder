import spacy

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")


def compare_classnames(c_cname, s_cname):
    similarity = nlp(c_cname).similarity(nlp(s_cname))
    return similarity >= 0.9


def grade_classnames(correct, student, rubric):
    valid_class_count = 0
    total_classes = len(correct["classnames"])

    for c_cname in correct["classnames"]:
        for s_cname in student["classnames"]:
            if compare_classnames(c_cname, s_cname):
                valid_class_count += 1

    if total_classes > 0:
        percentage = (valid_class_count / total_classes) * 100
    else:
        percentage = 100

    mark = calculate_marks(rubric["criterias"][0], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_attributes_methods(correct, student, category, rubric):
    valid_count = 0
    total_count = len(correct[category])

    for correct_item in correct[category]:
        for student_item in student[category]:
            if compare_classnames(correct_item["class"], student_item["class"]):
                name_similarity = nlp(correct_item["name"]).similarity(
                    nlp(student_item["name"])
                )
                if (
                    name_similarity >= 0.9
                    and correct_item["accessmodifier"] == student_item["accessmodifier"]
                ):
                    valid_count += 1

    if total_count > 0:
        percentage = (valid_count / total_count) * 100
    else:
        percentage = 100

    mark = calculate_marks(rubric, percentage)

    return {"correctness": percentage, "mark": mark}


def grade_relationships(correct, student, rubric):
    valid_count = 0
    total_relationships = len(correct["relationships"])

    for c_rel in correct["relationships"]:
        for s_rel in student["relationships"]:
            if (
                c_rel["type"] == s_rel["type"]
                and compare_classnames(c_rel["start"], s_rel["start"])
                and compare_classnames(c_rel["end"], s_rel["end"])
            ):
                valid_count += 1

    if total_relationships > 0:
        percentage = (valid_count / total_relationships) * 100
    else:
        percentage = 100

    mark = calculate_marks(rubric["criterias"][3], percentage)

    return {"correctness": percentage, "mark": mark}


def grade_access_modifiers(correct, student, rubric):
    valid_count = 0
    total_count = len(correct["attributes"]) + len(correct["methods"])

    # Compare attributes
    for correct_item, student_item in zip(correct["attributes"], student["attributes"]):
        if (
            compare_classnames(correct_item["class"], student_item["class"])
            and correct_item["accessmodifier"] == student_item["accessmodifier"]
        ):
            valid_count += 1

    # Compare methods
    for correct_item, student_item in zip(correct["methods"], student["methods"]):
        if (
            compare_classnames(correct_item["class"], student_item["class"])
            and correct_item["accessmodifier"] == student_item["accessmodifier"]
        ):
            valid_count += 1

    if total_count > 0:
        percentage = (valid_count / total_count) * 100
    else:
        percentage = 100

    mark = calculate_marks(rubric["criterias"][4], percentage)

    return {"correctness": percentage, "mark": mark}


def calculate_marks(rubric_criteria, percentage):
    for range_item in rubric_criteria["marks_ranges"]:
        if range_item["range"][0] <= percentage <= range_item["range"][1]:
            return range_item["marks"]
    return 0


def calculate_total(marks):
    total = sum(criteria["mark"] for criteria in marks.values())
    return total


def get_class_marks(correct, student, rubric):
    marks = {}

    # Grading process and populating the marks dictionary
    marks["classnames"] = grade_classnames(correct, student, rubric)
    marks["attributes"] = grade_attributes_methods(
        correct, student, "attributes", rubric["criterias"][1]
    )
    marks["methods"] = grade_attributes_methods(
        correct, student, "methods", rubric["criterias"][2]
    )
    marks["relationships"] = grade_relationships(correct, student, rubric)
    marks["access_modifiers"] = grade_access_modifiers(correct, student, rubric)

    # Add total to marks
    marks["total"] = calculate_total(marks)

    return marks
