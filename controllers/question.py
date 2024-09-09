from utils.diagram_classification import classify_diagram
from config.config import questions_collection
from utils.save_image import save_image
from bson.objectid import ObjectId
from utils.marking_rubrics import get_marking_rubric

def create_question(question, image):
    res = questions_collection.insert_one({"question" : question})
    id = str(res.inserted_id)
    
    file_location = save_image(id, image)
    type = classify_diagram(file_location)
    
    questions_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set":{
        "diagram_type":type
    }})
    
    rubric = get_marking_rubric(type)()
    
    return {
        "qid": id ,
        "rubric" : rubric}

def submit_rubric(qid, rubric):
    questions_collection.find_one_and_update({"_id": ObjectId(qid)}, {"$set":{
        "rubric": rubric
    }})
    
    return {
        "nice"
    }