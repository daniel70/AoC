import re, math

instructions = list(open("input08.txt").readlines())
LR = instructions[0].strip()
maps: dict[str, dict[str, str]] = {}
for line in instructions[2:]:
    node, left, right = re.findall("\w+", line)
    maps[node] = {"L": left, "R": right,}


def find_path(find: list[str]):
    steps = []
    for node in find:
        count = 0
        while not node.endswith("Z"):
            for direction in LR:
                count += 1
                node = maps[node][direction]
                if node.endswith("Z"):
                    steps.append(count)
                    break
    return math.lcm(*steps)


print("answer 1:", find_path(find=["AAA", ]), )
print("answer 2:", find_path(find=[key for key in maps if key.endswith("A")]))
