"""EP007 · Chat template and roles. A chat is rendered into one token stream with marker tokens.
The marker format below is made up; every model family has its own."""


def render_chat(messages, add_generation_prompt=True):
    parts = [f"<|{m['role']}|>\n{m['content']}\n<|end|>" for m in messages]
    if add_generation_prompt:
        parts.append("<|assistant|>\n")
    return "\n".join(parts)


if __name__ == "__main__":
    chat = [
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "What is 2 + 2?"},
        {"role": "assistant", "content": "4"},
        {"role": "tool", "content": "calculator: 2 + 2 = 4"},
        {"role": "user", "content": "Thanks! And 3 + 3?"},
    ]
    print(render_chat(chat))
    # Roles are labels inside one sequence: a user message can contain "<|system|>" text,
    # which is why roles are guidance, not a security boundary.
