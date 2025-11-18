import numpy as np
from openai import OpenAI

client = OpenAI(api_key="pk_a1999_b15_c06")

def get_embedding(text: str, model: str = "text-embedding-3-small"):
    if not text or text.strip() == "":
        return [0.0] * 1536

    res = client.embeddings.create(
        model=model,
        input=text
    )
    return res.data[0].embedding


def cosine(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10))