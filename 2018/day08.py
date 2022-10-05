from collections import deque
from dataclasses import dataclass
# 7807295 is too high

nodes = []
sum_metadata = 0

with open("input08.txt") as f:
    line = [int(c) for c in f.readline().split()]


@dataclass
class Node:
    header1: int
    header2: int
    children: list[int]
    metadata: list[int]
    value: int = 0


def create_node():
    global sum_metadata
    node = Node(0, 0, [], [])
    node.header1 = line.pop(0)
    node.header2 = line.pop(0)
    for child in range(node.header1):
        node.children.append(create_node())
    for meta in range(node.header2):
        node.metadata.append(line.pop(0))
    sum_metadata += sum(node.metadata)

    if node.children:
        for m in node.metadata:
            node.value += node.children[m-1].value if 0 < m <= len(node.children) else 0
    else:
        node.value = sum(node.metadata)
    return node


while line:
    nodes.append(create_node())

print("answer 1:", sum_metadata)
print("answer 2:", nodes[0].value)