from collections import Counter
import re, math

node_map = {}
node_steps = {}

instructions = list(open("2023/input08.txt").readlines())
LR = instructions[0]
maps: dict[str, dict[str, str]] = {}
for line in instructions[2:]:
    node, left, right = re.findall("\w+", line)
    maps[node] = {
        "L": left,
        "R": right,
    }


# current: list[str] = [key for key in maps if key.endswith("A")]
# current = ["AAA",]

for current in maps.keys():
    start = current
    steps = 0
    while not current.endswith("Z"):
        for direction in LR.strip():
            steps += 1
            current = maps[current][direction]
            if current.endswith("Z"):
                node_map[start] = maps[current][direction]
                node_steps[start] = steps
                break


# every starting node can keep adding numbers to a counter until there are x equal numers
nodes = [k for k in maps.keys() if k.endswith("A")]
node_counter = Counter()
counter = Counter("0")
while max(counter.values()) < len(nodes):
    for nr, node in enumerate(nodes):
        nodes[nr] = node_map[node] # put the next starting node in de map
        node_counter[nr] += node_steps[node] # adjust the counter for this node
        counter[node_counter[nr]] += 1

# create n generators that yield and can be asked for their next value
# then make them run in turns until they all end up on the same number

print(counter)