from fastapi import APIRouter, UploadFile, File, Form
from controllers.question import create_question, submit_rubric, get_questions
from models.rubric import Rubric

questions_router = APIRouter()

@questions_router.post("/questions/create")
def add_question(question: str = Form(...), image: UploadFile = File(...)):
    res = create_question(question, image)
    return {
        "qid": res["qid"],
        "diagram_type": res["diagram_type"],
        "rubric": res["rubric"]
    }
    
@questions_router.post("/questions/rubrics/{qid}")
def add_rubric(qid: str, rubric: Rubric):
    res = submit_rubric(qid, rubric.model_dump())
    return {"message": res["message"]}

@questions_router.get("/questions")
def retreive_questions():
    res = get_questions()
    return{
        "questions": res["questions"]
    }