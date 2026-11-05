"""EP106 · Anatomy: three harness configs share one skeleton (loop, tools, rules file); only the skin differs."""

SKELETON = ["loop", "tools", "permissions", "rules_file"]

HARNESSES = {  # illustrative summary, not an exact feature matrix
    "claude-code": {"rules_file": "CLAUDE.md", "sandbox": "permission prompts + optional sandbox", "providers": "Claude"},
    "codex-cli": {"rules_file": "AGENTS.md", "sandbox": "sandboxed commands", "providers": "OpenAI (configurable)"},
    "opencode": {"rules_file": "AGENTS.md", "sandbox": "permission rules", "providers": "many"},
}

for name, skin in HARNESSES.items():
    print(f"{name}: skeleton={SKELETON} rules={skin['rules_file']} sandbox={skin['sandbox']} providers={skin['providers']}")
