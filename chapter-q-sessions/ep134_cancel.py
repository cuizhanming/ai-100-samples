"""EP134 · Cancellation: a flag checked between steps stops the loop and keeps history."""
import threading

cancel = threading.Event()
history = []


def loop(steps):
    for s in steps:
        if cancel.is_set():
            history.append("cancelled")
            return
        history.append(s)
        if s == "step2":
            cancel.set()  # simulated Esc press


loop(["step1", "step2", "step3"])
assert history == ["step1", "step2", "cancelled"]
print("history kept:", history)
print("cancel ok")
