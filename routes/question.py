from fastapi import APIRouter, Body, Request
from utils.jwt.verify_token import verify_token
from utils.jwt.verify_permission import verify_permission
from controllers.question import (
    create_question,
    get_questions,
    save_question_to_db,
    save_image_url,
    get_question_by_id,
    get_question_ids,
    delete_question_by_id,
)
from models.question import Question

questions_router = APIRouter()


@questions_router.get("/")
def health():
    return {"message": "OK"}


@questions_router.post("/questions/create")
def add_question(request: Request, question: str = Body(...)):
    payload = verify_token(request)
    verify_permission(payload)
    res = create_question(question)
    return {"diagram_type": res["diagram_type"], "rubric": res["rubric"]}


@questions_router.post("/questions/save")
def save_question(request: Request, question: Question):
    payload = verify_token(request)
    verify_permission(payload)
    res = save_question_to_db(question)
    return {"qid": res["qid"]}


@questions_router.post("/questions/{qid}/add/image")
def save_image(
    request: Request, qid: str, url: str = Body(...), diagram_type: str = Body(...)
):
    payload = verify_token(request)
    verify_permission(payload)
    res = save_image_url(qid, url, diagram_type)
    return {"message": res["message"]}


@questions_router.get("/questions")
def retreive_questions(request: Request):
    verify_token(request)
    res = get_questions()
    return {"questions": res["questions"]}


@questions_router.get("/questions/ids")
def retreive_question_ids(request: Request):
    payload = verify_token(request)
    verify_permission(payload)
    res = get_question_ids()
    return {"qids": res["qids"]}


@questions_router.get("/questions/{qid}")
def retreive_question_by_id(request: Request, qid: str):
    verify_token(request)
    res = get_question_by_id(qid)
    return {"question": res["question"]}


@questions_router.delete("/questions/{qid}")
def delete_question(request: Request, qid: str):
    payload = verify_token(request)
    verify_permission(payload)
    res = delete_question_by_id(qid)
    return {"message": res["message"]}
