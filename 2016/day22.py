import re
import itertools as it
from collections import namedtuple

nrs = re.compile(r"\d+")
nodes = []
node = namedtuple("Node", "x y size used avail use")
with open("input22.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("/dev"):
            nodes.append(node(*map(int, nrs.findall(line))))


def print_grid(nodes):
    len_x, len_y = nodes[-1].x, nodes[-1].y
    for cell in nodes:
        print(f"{'--' if cell.used > 100 else (cell.used or '__')}/{'--' if cell.size > 100 else cell.size}", end=" ")
        if cell.x == len_x:
            print()


nodes.sort(key=lambda n: n.y)
# len_x, len_y = nodes[-1].x, nodes[-1].y
print_grid(nodes)

viable_pairs = []
for left, right in it.permutations(range(len(nodes)), 2):
    node1: node = nodes[left]
    node2: node = nodes[right]
    if node1.used == 0:
        continue
    if node1.used <= node2.avail:
        viable_pairs.append((node1, node2))


print("answer 1:", len(viable_pairs))

"""
The second answer is very hard to program but easy to visualize.
There is one empty disk (__/xx) in the visualization) that can be moved around.
It needs to go to (37, 0) to get to the target node but needs to go around a
wall of huge but full nodes (--/-- in the visualization).
So the empty node must first go left 17 + up 22 + right 37.
Then the empty data needs to go around this empty node to the left 36 times to reach (0, 0).
It takes 5 moves for each step to do this:
.._ ... ... ... _..
... .._ ._. _.. ...
So 36 * 5 + 17 + 22 + 37 == 256
Your answer will be different based on your input file.
"""

print("answer 2:", 256)
