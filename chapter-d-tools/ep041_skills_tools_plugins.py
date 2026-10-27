"""EP041 · Skills vs tools vs plugins. A plugin bundles skills and tools."""
tool = {"kind": "tool", "name": "read_file", "does": "action"}
skill = {"kind": "skill", "name": "code-review", "does": "instructions"}
plugin = {"kind": "plugin", "name": "dev-kit", "bundles": [tool, skill]}

if __name__ == "__main__":
    for part in plugin["bundles"]:
        print(f"{part['kind']:6} {part['name']:12} -> {part['does']}")
    print("plugin:", plugin["name"], "ships", len(plugin["bundles"]), "parts")
