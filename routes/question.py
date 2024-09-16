from fastapi import APIRouter, UploadFile, File, Form
from controllers.question import create_question, get_questions, save_question_to_db
from models.question import Question

questions_router = APIRouter()

@questions_router.post("/questions/create")
def add_question(image: UploadFile = File(...)):
    res = create_question(image)
    return {
        "diagram_type": res["diagram_type"],
        "rubric": res["rubric"]
    }
    
@questions_router.post("/questions/save")
def save_question(question: Question):
    res = save_question_to_db(question)
    return {"message": res["message"]}

@questions_router.get("/questions")
def retreive_questions():
    res = get_questions()
    return{
        "questions": res["questions"]
    }