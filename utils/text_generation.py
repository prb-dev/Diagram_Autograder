from gradio_client import Client, handle_file
from utils.prompts import get_prompts
from utils.convert_to_json import get_json


def generate_text(image_url, diagram_type):
    prompt = get_prompts(diagram_type)

    client = Client("GanymedeNil/Qwen2-VL-7B")
    result = client.predict(
        image=handle_file(image_url),
        text_input=prompt,
        model_id="Qwen/Qwen2-VL-7B-Instruct",
        api_name="/run_example",
    )

    result = get_json(result)

    return result
