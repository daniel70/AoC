import re, math

instructions = list(open("2023/input08.txt").readlines())
LR = instructions[0]
maps: dict[str, dict[str, str]] = {}
for line in instructions[2:]:
    node, left, right = re.findall("\w+", line)
    maps[node] = {
        "L": left,
        "R": right,
    }

all_steps = []
current: list[str] = [key for key in maps if key.endswith("A")]
# current = ["AAA",]
for this in current:
    steps = 0
    while not this.endswith("Z"):
        for direction in LR.strip():
            steps += 1
            this = maps[this][direction]
            if this.endswith("Z"):
                all_steps.append(steps)
                break

gcd = math.gcd(*all_steps)
reduced_steps = [i // gcd for i in all_steps]
print(all_steps)
print(gcd)
print(reduced_steps)
print(math.prod(reduced_steps))
