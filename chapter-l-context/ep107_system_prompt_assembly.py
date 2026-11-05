"""EP107 · System prompt assembly: base + project + session layers, rebuilt each session."""
import datetime


def assemble(base, project_files, env):
    parts = [base]
    parts += project_files  # your instruction files come after the built-in text
    parts.append("Date: %s | Cwd: %s | Mode: %s" % (env["date"], env["cwd"], env["mode"]))
    return "\n\n".join(parts)


prompt = assemble(
    "You are a coding agent. Use tools to read and edit files.",
    ["# AGENTS.md\nRun tests with `pytest -q`."],
    {"date": datetime.date.today().isoformat(), "cwd": "/repo", "mode": "ask-before-edit"},
)
print(prompt)
print("approx tokens (illustrative, 4 chars/token):", len(prompt) // 4)
