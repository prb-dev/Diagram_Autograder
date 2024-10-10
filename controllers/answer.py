from config.config import answers_collection, questions_collection
from utils.text_generation import generate_text
from bson.objectid import ObjectId
from utils.grading.handler import marks_invoker


def save_answer(qid, uid, url):
    diagram_type = questions_collection.find_one(
        {"_id": ObjectId(qid)}, {"diagram_type": 1, "_id": 0}
    )["diagram_type"]

    text = generate_text(url, diagram_type)

    res = answers_collection.insert_one(
        {
            "answer": {"image": url, "text_representation": text},
            "user_id": uid,
            "question_id": qid,
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

    rubric = questions_collection.find_one(
        {"_id": ObjectId(qid)}, {"rubric": 1, "_id": 0}
    )["rubric"]

    correct_answer = questions_collection.find_one(
        {"_id": ObjectId(qid)}, {"correct_answer": 1, "_id": 0}
    )["correct_answer"]["text_representation"]

    marks = marks_invoker(diagram_type, correct_answer, text, rubric)

    print(marks)

    return {"message": "Answer submitted", "aid": id}
