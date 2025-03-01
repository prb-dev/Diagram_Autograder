from gradio_client import Client


def classify_diagram(question):
    client = Client("hrmndev/MoritzLaurer-deberta-v3-large-zeroshot-v2.0")
    result = client.predict(
        param_0=question,
        param_1="class,usecase,er,sequence",
        param_2=False,
        api_name="/predict",
    )
    predicted_classname = result["label"]
    return predicted_classname
