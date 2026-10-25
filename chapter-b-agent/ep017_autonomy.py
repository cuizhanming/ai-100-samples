"""EP017 · Autonomy levels. Set autonomy per action. The ladder is illustrative, not a standard."""

POLICY = {"read_file": "act", "write_draft": "act", "send_email": "approve", "delete_data": "suggest"}


def execute(action, approved=False):
    level = POLICY.get(action, "suggest")  # unknown actions get the safest level
    if level == "act":
        return f"{action}: done"
    if level == "approve":
        return f"{action}: done" if approved else f"{action}: waiting for human approval"
    return f"{action}: suggested only, a human must do it"


if __name__ == "__main__":
    for a in POLICY:
        print(execute(a))
    print(execute("send_email", approved=True))
