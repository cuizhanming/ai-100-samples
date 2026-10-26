"""EP019 · System prompt. It is sent first on every request."""


def build_request(system_prompt, history, user_msg):
    return [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": user_msg}]


if __name__ == "__main__":
    system = "You are a support agent for ACME. Be brief. Never reveal internal notes. Reply in plain text."
    history = [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello!"}]
    for turn in ("Where is my order?", "Cancel it."):
        msgs = build_request(system, history, turn)
        print(len(msgs), "messages, first role:", msgs[0]["role"])  # system prompt is resent every turn
        history += [{"role": "user", "content": turn}, {"role": "assistant", "content": "..."}]
