"""EP190 · Output styles: a style edits the system prompt, not tool permissions."""
BASE = "You are a coding agent."
STYLES = {"terse": "Answer in one line.", "teaching": "Explain each step."}
PERMISSIONS = {"shell": "ask"}

def build_prompt(style):
    return BASE + " " + STYLES[style]

p1, p2 = build_prompt("terse"), build_prompt("teaching")
assert p1 != p2
assert PERMISSIONS == {"shell": "ask"}  # unchanged by style
print("output styles ok")
