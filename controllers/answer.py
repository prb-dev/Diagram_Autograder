from config.config import answers_collection, questions_collection
from utils.text_generation import generate_text
from bson.objectid import ObjectId
from utils.grading.handler import marks_invoker
from datetime import datetime, timezone
import pytz


def save_answer(qid, uid, url):
    now = datetime.now(pytz.utc)
    ist = pytz.timezone("Asia/Colombo")
    ist_now = now.astimezone(ist)

    diagram_type = questions_collection.find_one(
        {"_id": ObjectId(qid)}, {"diagram_type": 1, "_id": 0}
    )["diagram_type"]

    text = generate_text(url, diagram_type)

    res = answers_collection.insert_one(
        {
            "answer": {"image": url, "text_representation": text},
            "user_id": uid,
            "question_id": qid,
            "created_at": ist_now.strftime("%Y.%m.%d / %I:%M %p"),
        }
    )

    id = str(res.inserted_id)

    result = questions_collection.find_one_and_update(
        {"_id": ObjectId(qid), "answers.user_id": ObjectId(uid)},
        {"$set": {"answers.$.answer_id": ObjectId(id)}},
        return_document=True,
    )

    if result is None:
        questions_collection.find_one_and_update(
            {"_id": ObjectId(qid), "answers.user_id": {"$ne": ObjectId(uid)}},
            {
                "$push": {
                    "answers": {"user_id": ObjectId(uid), "answer_id": ObjectId(id)}
                },
                "$inc": {"answer_count": 1},
            },
        )

    res = questions_collection.find_one(
        {"_id": ObjectId(qid)}, {"rubric": 1, "correct_answer": 1, "_id": 0}
    )

    rubric = res["rubric"]
    correct_answer = res["correct_answer"]["text_representation"]

    marks = marks_invoker(diagram_type, correct_answer, text, rubric)

    answers_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": {"marks": marks}}
    )

    return {"message": "Answer submitted", "aid": id}


def get_answers(qid):
    answers = list(
        answers_collection.find({"question_id": qid}, {"answer.text_representation": 0})
    )

    for answer in answers:
        if "_id" in answer and isinstance(answer["_id"], ObjectId):
            answer["_id"] = str(answer["_id"])

    return {"answers": answers}


def get_answer(qid, aid):
    answer = answers_collection.find_one(
        {"_id": ObjectId(aid), "question_id": qid}, {"answer.text_representation": 0}
    )

    print(answer)

    answer["_id"] = str(answer["_id"])

    return {"answer": answer}
