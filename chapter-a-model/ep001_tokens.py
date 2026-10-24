"""EP001 · Tokens. Split text into tokens and count them.
Uses tiktoken if installed (pip install tiktoken); otherwise falls back to a naive splitter.
Exact splits differ by model: every tokenizer has its own vocabulary."""
import re
import sys


def tokenize(text: str):
    try:
        import tiktoken

        enc = tiktoken.get_encoding("cl100k_base")
        ids = enc.encode(text)
        return [enc.decode([i]) for i in ids], ids
    except ImportError:
        pieces = re.findall(r"\s?\w{1,4}|\s?[^\w\s]", text)
        return pieces, list(range(len(pieces)))


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or "Agents are unbelievable"
    pieces, ids = tokenize(text)
    print("text  :", text)
    print("tokens:", pieces)
    print("ids   :", ids)
    print(f"{len(text)} chars -> {len(pieces)} tokens (~{len(text) / max(len(pieces), 1):.1f} chars/token)")
