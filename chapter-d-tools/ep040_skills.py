"""EP040 · Skills. Only name and description are preloaded; the body loads on a match."""
SKILLS = {
    "pdf-report": {"description": "build a pdf report from data", "body": "Step 1: ... (long instructions)"},
    "git-helper": {"description": "write git commit messages", "body": "Step 1: ... (long instructions)"},
}


def index():
    return {n: s["description"] for n, s in SKILLS.items()}


def load_for(task):
    for name, s in SKILLS.items():
        if any(w in task.split() for w in s["description"].split() if len(w) > 3):
            return name, s["body"]
    return None, ""


if __name__ == "__main__":
    print("preloaded:", index())
    print("loaded   :", load_for("please write a commit message")[0])
