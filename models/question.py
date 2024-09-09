from pydantic import BaseModel
from typing import Any

class Question(BaseModel):
    question: str
    diagram_type: str
    correct_answer: dict[str, Any]
    student_answers: list
    
    class Config:
        arbitrary_types_allowed = True