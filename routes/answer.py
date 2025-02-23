from fastapi import APIRouter, UploadFile, File, Body
from controllers.answer import save_answer, get_answers, get_answer

answer_router = APIRouter()


@answer_router.post("/answers/submit/{qid}/{uid}")
def submit_answer(qid: str, uid: str, url: str = Body(...)):
    res = save_answer(qid, uid, url)

    return {"message": res["message"], "aid": res["aid"]}


@answer_router.get("/answers/{qid}")
def retrieve_answers(qid: str):
    res = get_answers(qid)
    return {"answers": res["answers"]}


@answer_router.get("/answers/{qid}/{aid}")
def retrieve_answer(qid: str, aid: str):
    res = get_answer(qid, aid)
    return {"answer": res["answer"]}
