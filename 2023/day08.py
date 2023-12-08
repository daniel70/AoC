import re
instructions = list(open("2023/input08.txt").readlines())
LR = instructions[0]
maps: dict[str, dict[str, str]] = {}
for line in instructions[2:]:
    node, left, right = re.findall("\w+", line)
    maps[node] = {
        "L": left,
        "R": right,
    }
print(maps)

steps = 0
current = "AAA"
while current != "ZZZ":
    for direction in LR.strip():
        steps += 1
        current = maps[current][direction]
        if current == "ZZZ":
            break
        
print(steps)