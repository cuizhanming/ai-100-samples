"""EP080 · Heartbeats: a timer wakes the agent; it acts only when something needs attention."""
CHECKLIST = {"inbox": 0, "calendar": 1, "alerts": 0}  # illustrative state


def heartbeat(state):
    todo = [k for k, v in state.items() if v]
    return "HEARTBEAT_OK" if not todo else "needs attention: " + ", ".join(todo)


if __name__ == "__main__":
    for tick in range(3):
        if tick == 2:
            CHECKLIST["calendar"] = 0
        print(f"tick {tick}:", heartbeat(CHECKLIST))
