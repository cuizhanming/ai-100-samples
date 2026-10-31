"""EP074 · Specialist roles: each agent has one job and only its own tools."""
ROLES = {
    "researcher": {"tools": ["search"], "prompt": "Find sources."},
    "writer": {"tools": [], "prompt": "Write from the notes."},
    "checker": {"tools": ["search", "calc"], "prompt": "Verify claims."},
}


def can_use(role, tool):
    return tool in ROLES[role]["tools"]


if __name__ == "__main__":
    for r in ROLES:
        print(r, ROLES[r]["tools"], "calc allowed:", can_use(r, "calc"))
