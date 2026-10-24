"""EP002 · Context window. A window is a token budget; old content is trimmed when it is full.
Token counts here are a rough estimate (~4 characters per token)."""


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def fit_to_window(messages, budget: int, reserve_for_reply: int = 200):
    """Keep the system message plus the newest messages that fit in the budget."""
    system, rest = messages[0], messages[1:]
    remaining = budget - reserve_for_reply - estimate_tokens(system["content"])
    kept = []
    for m in reversed(rest):
        cost = estimate_tokens(m["content"])
        if cost > remaining:
            break
        kept.append(m)
        remaining -= cost
    return [system] + list(reversed(kept))


if __name__ == "__main__":
    history = [{"role": "system", "content": "You are a helpful agent."}]
    for i in range(1, 41):
        history.append({"role": "user" if i % 2 else "assistant", "content": f"turn {i}: " + "word " * 40})
    kept = fit_to_window(history, budget=800)
    print(f"{len(history)} messages -> {len(kept)} kept")
    print("oldest kept:", kept[1]["content"][:12], "| newest kept:", kept[-1]["content"][:12])
