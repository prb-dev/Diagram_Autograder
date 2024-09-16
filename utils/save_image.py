import shutil
import os

def save_image(image):
    # Save the file to a desired location
    directory = "images"
    _, file_extension = os.path.splitext(image.filename)
    file_location = os.path.join(directory, f"image{file_extension}")
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        
    return file_location