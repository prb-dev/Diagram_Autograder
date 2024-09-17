from utils.diagram_classification import classify_diagram
from config.config import questions_collection
from utils.save_image import save_image
from bson.objectid import ObjectId
from utils.marking_rubrics import get_marking_rubric
from datetime import datetime, timezone
from utils.text_generation import generate_text


def create_question(image):
    file_location = save_image(image)
    type = classify_diagram(file_location)

    rubric = get_marking_rubric(type)()

    return {"diagram_type": type, "rubric": rubric}


def save_question_to_db(question):
    now = datetime.fromisoformat(str(datetime.now(timezone.utc)))
    deadline = datetime.strptime(
        question.deadline[:24], "%a %b %d %Y %H:%M:%S"
    ).strftime("%m/%d/%Y %H:%M:%S")

    res = questions_collection.insert_one(
        {
            "question": question.question,
            "deadline": str(deadline),
            "answers": [],
            "answer_count": 0,
            "created_at": now.strftime("%Y.%m.%d / %I:%M %p"),
            "diagram_type": question.diagram_type,
            "rubric": question.rubric.model_dump(),
        }
    )
    id = str(res.inserted_id)

    return {"qid": id}


def save_image_url(qid, url, diagram_type):
    text = generate_text(url, diagram_type)
    questions_collection.find_one_and_update(
        {"_id": ObjectId(qid)},
        {
            "$set": {
                "correct_answer.image": url,
                "correct_answer.text_representation": text,
            }
        },
    )

    return {"message": "Question published."}


def get_questions():
    questions = list(questions_collection.find())

    for question in questions:
        if "_id" in question:
            question["_id"] = str(question["_id"])

    return {"questions": questions}


def get_question_by_id(id):
    res = questions_collection.find_one(
        {"_id": ObjectId(id)}, {"question": 1, "deadline": 1}
    )
    res["_id"] = str(res["_id"])
    return {"question": res}
