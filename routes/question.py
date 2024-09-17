from fastapi import APIRouter, UploadFile, File, Form, Body
from controllers.question import (
    create_question,
    get_questions,
    save_question_to_db,
    save_image_url,
    get_question_by_id,
)
from models.question import Question

questions_router = APIRouter()


@questions_router.post("/questions/create")
def add_question(image: UploadFile = File(...)):
    res = create_question(image)
    return {"diagram_type": res["diagram_type"], "rubric": res["rubric"]}


@questions_router.post("/questions/save")
def save_question(question: Question):
    res = save_question_to_db(question)
    return {"qid": res["qid"]}


@questions_router.post("/questions/{qid}/add/image")
def save_image(qid: str, url: str = Body(...), diagram_type: str = Body(...)):
    res = save_image_url(qid, url, diagram_type)
    return {"message": res["message"]}


@questions_router.get("/questions")
def retreive_questions():
    res = get_questions()
    return {"questions": res["questions"]}


@questions_router.get("/questions/{qid}")
def retreive_question_by_id(qid: str):
    res = get_question_by_id(qid)
    return {"question": res["question"]}
