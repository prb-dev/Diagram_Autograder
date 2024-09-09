from pydantic import BaseModel
from typing import List

class MarkRange(BaseModel):
    range: List[int]
    marks: int

class Criteria(BaseModel):
    name: str
    marks_ranges: List[MarkRange]

class Rubric(BaseModel):
    criterias: List[Criteria]
