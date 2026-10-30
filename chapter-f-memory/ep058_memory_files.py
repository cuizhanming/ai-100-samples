"""EP058 · Memory files. Append daily notes, then curate lasting facts into MEMORY.md."""
import os
import tempfile


def log(root, day, line):
    os.makedirs(os.path.join(root, "memory"), exist_ok=True)
    with open(os.path.join(root, "memory", f"{day}.md"), "a") as f:
        f.write(f"- {line}\n")


def curate(root):
    """Promote lines tagged [keep] from every daily note into MEMORY.md (no duplicates)."""
    mem = os.path.join(root, "MEMORY.md")
    have = set(open(mem).read().splitlines()) if os.path.exists(mem) else set()
    new = []
    folder = os.path.join(root, "memory")
    for name in sorted(os.listdir(folder)):
        for line in open(os.path.join(folder, name)).read().splitlines():
            if "[keep]" in line:
                fact = "- " + line.replace("- ", "", 1).replace("[keep]", "").strip()
                if fact not in have and fact not in new:
                    new.append(fact)
    with open(mem, "a") as f:
        f.write("".join(x + "\n" for x in new))
    return open(mem).read()


if __name__ == "__main__":
    root = tempfile.mkdtemp()
    log(root, "2026-10-29", "chatted about stocks")
    log(root, "2026-10-29", "[keep] prefers short answers")
    log(root, "2026-10-30", "[keep] prefers short answers")
    log(root, "2026-10-30", "[keep] timezone is Europe/Dublin")
    print(curate(root))
