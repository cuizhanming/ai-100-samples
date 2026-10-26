"""EP021 · Few-shot. Examples placed before the real input teach the format."""

EXAMPLES = [("great battery life", "positive"), ("screen cracked in a week", "negative")]


def few_shot_prompt(examples, text):
    shots = "\n".join(f"Review: {a}\nLabel: {b}" for a, b in examples)
    return f"Label each review as positive or negative.\n\n{shots}\n\nReview: {text}\nLabel:"


if __name__ == "__main__":
    print(few_shot_prompt(EXAMPLES, "fast shipping, works fine"))
