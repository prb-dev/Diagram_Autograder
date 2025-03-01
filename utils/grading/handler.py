from utils.grading.class_diagram_grading import get_class_marks
from utils.grading.usecase_diagram_grading import get_usecase_marks
from utils.grading.er_diagram_grading import get_er_marks
from utils.grading.sequence_diagram_grading import get_sequence_marks

functions = {
    "class": get_class_marks,
    "usecase": get_usecase_marks,
    "er": get_er_marks,
    "sequence": get_sequence_marks,
}


def marks_invoker(type, correct, student, rubric):
    marks = functions.get(type)(correct, student, rubric)
    return marks
