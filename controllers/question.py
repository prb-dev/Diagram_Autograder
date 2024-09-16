from utils.diagram_classification import classify_diagram
from config.config import questions_collection
from utils.save_image import save_image
from bson.objectid import ObjectId
from utils.marking_rubrics import get_marking_rubric
from datetime import datetime, timezone

def create_question(image):
    # res = questions_collection.insert_one({"question" : question, "deadline": deadline, "answers": [], "answer_count": 0, "created_at": now.strftime("%Y.%m.%d / %I:%M %p")})
    # id = str(res.inserted_id)
    
    file_location = save_image(image)
    type = classify_diagram(file_location)
    
    # questions_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set":{
    #     "diagram_type":type
    # }})
    
    rubric = get_marking_rubric(type)()
    
    return {
        "diagram_type": type,
        "rubric" : rubric}
    
def save_question_to_db(question):
    now = datetime.fromisoformat(str(datetime.now(timezone.utc)))
    
    res = questions_collection.insert_one({"question" : question.question, "deadline": question.deadline, "answers": [], "answer_count": 0, "created_at": now.strftime("%Y.%m.%d / %I:%M %p"), "diagram_type":question.diagram_type, "rubric": question.rubric.model_dump() })
    
    return{
        "message": "Question added."
    }
    
def get_questions():
    questions = list(questions_collection.find())
    
    for question in questions:
        if "_id" in question:
            question["_id"] = str(question["_id"])
    
    return{
        "questions": questions
    }