def class_template():
    return {
        "criterias": [
            "classnames", "attributes", "methods", "relationships", "access modifiers" 
        ],
        "ranges": [[0, 20],    
        [21, 40],  
        [41, 60],  
        [61, 80],  
        [81, 100]]
    }
    
def use_case_template():
    return {
        "criterias": [
            "classnames", "attributes", "methods", "relationships", "access modifiers" 
        ],
        "ranges": [[0, 20],    
        [21, 40],  
        [41, 60],  
        [61, 80],  
        [81, 100]]
    }
    
functions = {
    "class" : class_template,
    "usecase": use_case_template
}

def get_marking_rubric(diagram_type):
    return functions.get(diagram_type)