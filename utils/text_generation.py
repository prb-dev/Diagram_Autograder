from gradio_client import Client, handle_file
from utils.prompts import get_prompts
from utils.convert_to_json import get_json
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv("HF_TOKEN")

# client = InferenceClient(
#     provider="nebius",
#     api_key=TOKEN,
# )


# def generate_text(image_url, diagram_type):
#     prompt = get_prompts(diagram_type)

#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": prompt,
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": image_url,
#                     },
#                 },
#             ],
#         }
#     ]

#     completion = client.chat.completions.create(
#         model="Qwen/Qwen2-VL-7B-Instruct",
#         messages=messages,
#         max_tokens=500,
#     )

#     result = get_json(completion.choices[0].message["content"])

#     return result


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
