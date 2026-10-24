"""EP004 · Embeddings. Text becomes a vector; close vectors mean similar meaning.
This toy hashes words into a small vector so it runs offline. A real embedding model captures
meaning (synonyms land close together); this toy only captures shared words."""
import hashlib
import math
import re

DIM = 64


def embed(text: str):
    vec = [0.0] * DIM
    for word in re.findall(r"[a-z']+", text.lower()):
        h = int(hashlib.md5(word.encode()).hexdigest(), 16)
        vec[h % DIM] += 1.0 if (h >> 8) % 2 else -1.0
    norm = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [x / norm for x in vec]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


if __name__ == "__main__":
    docs = ["how do I reset my password", "reset password steps", "best pizza recipe"]
    query = embed("reset my password")
    for d in sorted(docs, key=lambda d: -cosine(query, embed(d))):
        print(f"{cosine(query, embed(d)):.2f}  {d}")
