"""EP077 · Gateway and daemon: one long-running loop owns events, sessions and replies."""
import queue


def gateway(events, handle):
    sessions = {}
    while True:
        try:
            ev = events.get_nowait()
        except queue.Empty:
            break  # a real daemon would block here and keep waiting
        history = sessions.setdefault(ev["chat"], [])
        history.append(ev["text"])
        print(f"[{ev['chat']}] {handle(history)}")
    return sessions


if __name__ == "__main__":
    q = queue.Queue()
    for chat, text in [("a", "hi"), ("b", "status?"), ("a", "thanks")]:
        q.put({"chat": chat, "text": text})
    s = gateway(q, lambda h: f"reply #{len(h)} to {h[-1]!r}")
    print({k: len(v) for k, v in s.items()})
