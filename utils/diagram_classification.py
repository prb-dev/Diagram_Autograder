from ultralytics import YOLO
import numpy as np


def classify_diagram(image_path):
    model = YOLO("./ai_models/last.pt")  # load a custom model

    # Predict with the model
    results = model(image_path)

    class_names = results[0].names
    probs = results[0].probs.tolist()
    predicted_classname = class_names[np.argmax(probs)]

    return predicted_classname
