"""EP116 · Skills: progressive disclosure (metadata first, body on demand)."""
SKILLS = {
    "pdf": ("Fill and merge PDF forms", "STEP 1 ... STEP 2 ... " * 40),
    "sql": ("Write safe SQL queries", "RULES ... EXAMPLES ... " * 60),
}
index = [f"{name}: {desc}" for name, (desc, _) in SKILLS.items()]
print("always in context:", index)
loaded = SKILLS["sql"][1]
print(f"metadata chars: {sum(len(i) for i in index)} | one body on demand: {len(loaded)} chars")
assert sum(len(i) for i in index) < len(loaded)
