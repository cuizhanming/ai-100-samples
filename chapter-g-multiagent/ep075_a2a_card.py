"""EP075 · A2A: discover a remote agent by its card, then send it a task (simulated, no network)."""
import json

AGENT_CARD = {
    "name": "Translator",
    "url": "http://localhost:9999/a2a",
    "skills": [{"id": "translate", "description": "Translate text"}],
}


def remote_handle(task):
    return {"status": "completed", "artifact": task["text"].upper()}


if __name__ == "__main__":
    print(json.dumps(AGENT_CARD))
    skill = AGENT_CARD["skills"][0]["id"]
    print(remote_handle({"skill": skill, "text": "hello"}))
