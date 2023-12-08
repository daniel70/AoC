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

steps = 0
is_found = False
current: list[str] = [key for key in maps if key.endswith("A")]
# current: ["AAA",]
while not is_found:
    for direction in LR.strip():
        if steps % 1_000_000 == 0:
            print(steps // 1_000_000, end=", ", flush=True)
        steps += 1
        for idx, this in enumerate(current):
            current[idx] = maps[this][direction]

        if all([key.endswith("Z") for key in current]):
            is_found = True
            break

print(current)
print(steps)