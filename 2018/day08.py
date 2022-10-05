from dataclasses import dataclass, field

nodes = []
with open("input08.txt") as f:
    line = [int(c) for c in f.readline().split()]


@dataclass
class Node:
    header1: int
    header2: int
    children: list = field(default_factory=list)
    metadata: list[int] = field(default_factory=list)
    sum_metadata: int = 0
    value: int = 0


def create_node():
    node = Node(0, 0, [], [])
    node.header1 = line.pop(0)
    node.header2 = line.pop(0)
    for child in range(node.header1):
        node.children.append(create_node())
    for meta in range(node.header2):
        node.metadata.append(line.pop(0))
    node.sum_metadata += sum(node.metadata)
    for c in node.children:
        node.sum_metadata += c.sum_metadata
    # part two
    if node.children:
        for m in node.metadata:
            node.value += node.children[m-1].value if 0 < m <= len(node.children) else 0
    else:
        node.value = sum(node.metadata)

    return node


root = create_node()
print("answer 1:", root.sum_metadata)
print("answer 2:", root.value)
