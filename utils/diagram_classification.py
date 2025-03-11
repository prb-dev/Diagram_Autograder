# from gradio_client import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("HF_TOKEN")
API_URL = os.getenv("API_URL")


def classify_diagram(question):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": question,
            "parameters": {"candidate_labels": ["class", "usecase", "er", "sequence"]},
        },
    )

    return response.json()["labels"][0]


# def classify_diagram(question):
#     client = Client("hrmndev/MoritzLaurer-deberta-v3-large-zeroshot-v2.0")
#     result = client.predict(
#         param_0=question,
#         param_1="class,usecase,er,sequence",
#         param_2=False,
#         api_name="/predict",
#     )
#     predicted_classname = result["label"]
#     return predicted_classname
