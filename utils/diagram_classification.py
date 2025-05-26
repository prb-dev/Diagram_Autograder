# from gradio_client import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("HF_TOKEN")
INFER_URL = os.getenv("DEBERTA_INFER_URL")


def classify_diagram(question):
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # for _ in range(3):
    #     response = requests.post(
    #         INFER_URL,
    #         headers=headers,
    #         json={
    #             "inputs": question,
    #             "parameters": {
    #                 "candidate_labels": ["class", "usecase", "er", "sequence"]
    #             },
    #         },
    #         timeout=10,
    #     )

    #     if response.status_code == 200:
    #         return response.json()["labels"][0]

    # raise Exception("Failed to classify diagram")
    response = requests.post(
        INFER_URL,
        headers=headers,
        json={
            "inputs": question,
            "parameters": {"candidate_labels": ["class", "usecase", "er", "sequence"]},
        },
    )

    if response.status_code == 200:
        print(response.json())
        return response.json()["labels"][0]
    else:
        print(f"Error {response.status_code}: {response.text}")
        raise Exception("Failed to classify diagram")


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
