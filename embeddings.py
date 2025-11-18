import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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