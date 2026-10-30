"""EP065 · Vector search with a toy bag-of-words embedding and cosine similarity."""
import math

VOCAB = ["refund", "money", "back", "ship", "delivery", "days", "password", "reset", "login"]
SYN = {"reimbursement": "refund", "parcel": "ship", "shipping": "ship"}  # tiny stand-in for learned meaning


def embed(text):
    words = [SYN.get(w, w) for w in text.lower().split()]
    return [float(sum(w.startswith(v) for w in words)) for v in VOCAB]


def cosine(a, b):
    na, nb = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(x * x for x in b))
    return sum(x * y for x, y in zip(a, b)) / (na * nb) if na and nb else 0.0


DOCS = ["refund money back in 30 days", "shipping delivery takes 5 days", "reset password at login"]
INDEX = [(d, embed(d)) for d in DOCS]

if __name__ == "__main__":
    q = embed("reimbursement")
    for d, v in sorted(INDEX, key=lambda x: -cosine(q, x[1])):
        print(round(cosine(q, v), 2), d)
