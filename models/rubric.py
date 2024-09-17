from pydantic import BaseModel
from typing import List


class MarkRange(BaseModel):
    range: List[int]
    marks: int


class Criteria(BaseModel):
    name: str
    marks_ranges: List[MarkRange]
    sub_total: int


class Rubric(BaseModel):
    criterias: List[Criteria]
    total: int
