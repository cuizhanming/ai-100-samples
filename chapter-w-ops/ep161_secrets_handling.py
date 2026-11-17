"""EP161 · Secrets handling: pass secrets through the environment, never into the prompt."""
import os, re

def build_prompt(task):
    return f"Task: {task}. Use the DEPLOY_TOKEN environment variable."

def scrub_env(env, allow=("PATH", "HOME")):
    return {k: v for k, v in env.items() if k in allow}

os.environ["DEPLOY_TOKEN"] = "s3cr3t-value"
prompt = build_prompt("deploy the app")
assert "s3cr3t-value" not in prompt
child_env = scrub_env(os.environ)
assert "DEPLOY_TOKEN" not in child_env
assert not re.search(r"s3cr3t", prompt)
print("secrets handling ok")
