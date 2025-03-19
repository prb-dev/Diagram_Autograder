from fastapi import APIRouter, Body, Request
from controllers.answer import (
    save_answer,
    get_answers,
    get_answer,
    get_answer_by_student_id,
)
from utils.jwt.verify_token import verify_token
from utils.jwt.verify_permission import verify_permission

answer_router = APIRouter()


@answer_router.post("/answers/submit/{qid}/{uid}")
def submit_answer(request: Request, qid: str, uid: str, url: str = Body(...)):
    # verify_token(request)
    res = save_answer(qid, uid, url)

    return {"message": res["message"], "aid": res["aid"]}


@answer_router.get("/answers/{qid}")
def retrieve_answers(request: Request, qid: str):
    # verify_token(request)
    res = get_answers(qid)
    return {"answers": res["answers"]}


@answer_router.get("/answers/{qid}/{aid}")
def retrieve_answer(request: Request, qid: str, aid: str):
    # payload = verify_token(request)
    # verify_permission(payload)
    res = get_answer(qid, aid)
    return {"answer": res["answer"]}


@answer_router.get("/{sid}/answers")
def retrieve_answers_by_student_id(request: Request, sid: str):
    # verify_token(request)
    res = get_answer_by_student_id(sid)
    return {"answers": res["answers"]}
