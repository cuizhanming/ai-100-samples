"""EP180 · Worktrees: two isolated checkouts of one repo."""
import os, subprocess, tempfile

def git(cwd, *a):
    subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True)

with tempfile.TemporaryDirectory() as d:
    repo = os.path.join(d, "repo")
    os.mkdir(repo)
    git(repo, "init", "-q")
    git(repo, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "init")
    wt = os.path.join(d, "wt-a")
    git(repo, "worktree", "add", "-q", "-b", "agent-a", wt)
    open(os.path.join(wt, "a.txt"), "w").write("x")
    assert not os.path.exists(os.path.join(repo, "a.txt"))
    git(repo, "worktree", "remove", "--force", wt)
print("worktrees ok")
