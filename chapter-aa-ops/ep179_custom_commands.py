"""EP179 · Custom commands: a saved prompt template with arguments."""
commands = {"review": "Review {file} for bugs and list the top {n}."}

def run(line):
    name, *args = line.lstrip("/").split()
    file, n = args
    return commands[name].format(file=file, n=n)

assert run("/review app.py 3") == "Review app.py for bugs and list the top 3."
print("custom commands ok")
