"""EP073 · Shared state vs messages: two coordination styles."""


def shared_state():
    state = {"draft": "", "review": ""}
    state["draft"] = "writer: v1"
    state["review"] = f"reviewer read '{state['draft']}'"
    return state


def messages():
    inbox = []
    inbox.append({"from": "writer", "to": "reviewer", "body": "draft v1"})
    msg = inbox.pop(0)
    return f"reviewer got '{msg['body']}' from {msg['from']}"


if __name__ == "__main__":
    print(shared_state())
    print(messages())
