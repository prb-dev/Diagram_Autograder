from gradio_client import Client, handle_file
from utils.prompts import get_prompts
from utils.convert_to_json import get_json


def generate_text(image_url, diagram_type):
    prompt = get_prompts(diagram_type)

    client = Client("prithivMLmods/Qwen2.5-VL-7B-Instruct")
    result = client.predict(
        message={
            "text": prompt,
            "files": [handle_file(image_url)],
        },
        api_name="/chat",
    )

    result = get_json(result)

    return result
