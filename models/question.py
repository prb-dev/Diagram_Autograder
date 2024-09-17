from pydantic import BaseModel
from models.rubric import Rubric


class Question(BaseModel):
    question: str
    diagram_type: str
    deadline: str
    rubric: Rubric
