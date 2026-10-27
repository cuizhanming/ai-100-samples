"""EP039 · MCP vs plain tools. Both end up as the same tool definition for the model."""


def plain_tool(x):
    return x * 2


class RemoteTool:
    """Stand-in for a tool served by an MCP server in another process."""

    def __call__(self, x):
        return x * 2


def definition(name, fn):
    return {"name": name, "description": f"{name} tool", "callable": callable(fn)}


if __name__ == "__main__":
    print(definition("double_local", plain_tool))
    print(definition("double_remote", RemoteTool()))
