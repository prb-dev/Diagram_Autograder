from utils.grading.class_diagram_grading import get_class_marks

functions = {"class": get_class_marks}


def marks_invoker(type, correct, student, rubric):
    marks = functions.get(type)(correct, student, rubric)
    return marks
