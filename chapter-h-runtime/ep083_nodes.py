"""EP083 · Nodes and devices: a paired device exposes only the capabilities it advertises."""


class Node:
    def __init__(self, name, caps, approved):
        self.name, self.caps, self.approved = name, caps, approved

    def invoke(self, cap, **kw):
        if not self.approved:
            return "denied: not paired"
        if cap not in self.caps:
            return f"denied: {cap} not advertised"
        return f"{self.name}.{cap}({kw}) ok"


if __name__ == "__main__":
    phone = Node("phone", {"camera_snap", "location"}, approved=True)
    print(phone.invoke("camera_snap", facing="back"))
    print(phone.invoke("shell", cmd="ls"))
    print(Node("stranger", {"shell"}, approved=False).invoke("shell"))
