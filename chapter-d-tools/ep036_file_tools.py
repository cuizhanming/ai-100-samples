"""EP036 · File tools. Read a slice, not the whole file."""
import tempfile
from pathlib import Path


def read_range(path, start, end):
    lines = Path(path).read_text().splitlines()
    return "\n".join(f"{i}: {l}" for i, l in enumerate(lines[start - 1:end], start))


def grep(path, needle):
    return [i for i, l in enumerate(Path(path).read_text().splitlines(), 1) if needle in l]


if __name__ == "__main__":
    f = Path(tempfile.mkdtemp()) / "log.txt"
    f.write_text("\n".join(f"line {i}" + (" ERROR" if i == 42 else "") for i in range(1, 101)))
    hit = grep(f, "ERROR")
    print("hits:", hit)
    print(read_range(f, hit[0] - 1, hit[0] + 1))
