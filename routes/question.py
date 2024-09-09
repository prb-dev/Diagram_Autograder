from fastapi import APIRouter, UploadFile, File, Form
from controllers.question import create_question
from models.rubric import Rubric

questions_router = APIRouter()

@questions_router.post("/questions")
def add_question(question: str = Form(...), image: UploadFile = File(...)):
    res = create_question(question, image)
    return {
        "qid": res["qid"],
        "rubric": res["rubric"]
    }
    
@questions_router.post("/questions/rubrics/{qid}")
def add_rubric(qid: str, rubric: Rubric):
    return {qid}