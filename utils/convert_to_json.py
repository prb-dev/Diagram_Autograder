import json

def get_json(text:str):
    text = text.strip().replace("json", "").replace("`", "").strip()
    
    try:
        json_obj = json.loads(text)
        return json_obj
    except json.JSONDecodeError as e:
        print('error: ', e)