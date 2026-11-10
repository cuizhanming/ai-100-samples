"""EP127 · Worktrees and merge conflicts: isolated edits, conflict at merge time."""
import os
import subprocess
import tempfile

G = ["git", "-c", "user.name=demo", "-c", "user.email=demo@example.com"]


def git(cwd, *args, check=True):
    return subprocess.run(G + list(args), cwd=cwd, capture_output=True, text=True, check=check)


root = tempfile.mkdtemp()
repo = os.path.join(root, "repo")
os.makedirs(repo)
git(repo, "init", "-q")
git(repo, "checkout", "-q", "-b", "main")
open(os.path.join(repo, "app.txt"), "w").write("timeout=30\n")
git(repo, "add", ".")
git(repo, "commit", "-q", "-m", "init")

for name, value in (("agent-a", 60), ("agent-b", 90)):
    wt = os.path.join(root, name)
    git(repo, "worktree", "add", "-q", "-b", name, wt)
    open(os.path.join(wt, "app.txt"), "w").write(f"timeout={value}\n")
    git(wt, "commit", "-q", "-am", name)

assert open(os.path.join(repo, "app.txt")).read() == "timeout=30\n"  # main untouched
assert git(repo, "merge", "agent-a").returncode == 0
r = git(repo, "merge", "agent-b", check=False)
assert r.returncode != 0 and "CONFLICT" in r.stdout
print("worktrees ok: conflict surfaced at merge")
