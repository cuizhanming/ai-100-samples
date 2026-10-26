"""EP023 · Chain-of-thought. Ask for steps first, answer last. Always verify the answer."""


def cot_prompt(question):
    return f"{question}\nThink step by step, then give the final answer on a line starting with 'Answer:'."


def extract_answer(reply):
    for line in reversed(reply.splitlines()):
        if line.startswith("Answer:"):
            return line[len("Answer:"):].strip()
    return None


if __name__ == "__main__":
    fake_reply = "12 apples, give away 5 -> 7.\n7 + 3 bought -> 10.\nAnswer: 10"  # scripted stand-in for a model
    print(cot_prompt("I have 12 apples, give away 5, buy 3. How many?"))
    ans = extract_answer(fake_reply)
    print("answer:", ans, "| verified:", ans == str(12 - 5 + 3))
