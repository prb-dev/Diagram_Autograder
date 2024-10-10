from fastapi import APIRouter, UploadFile, File, Body
from controllers.answer import save_answer

answer_router = APIRouter()

@answer_router.post("/answers/submit/{qid}/{uid}")
def submit_answer(qid: str, uid: str, url: str = Body(...)):
    res = save_answer(qid, uid, url)
    
    return {
        "message": res["message"],
        "aid": res["aid"]
    }