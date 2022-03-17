import re
re_first = re.compile(r"^(\w+)")

roots = set()
leaves = set()
instructions = []
with open("input07.txt") as f:
    for line in f:
        line = line.strip()
        instructions = line.split(" -> ")
        if len(instructions) == 2:
            roots.add(re_first.findall(instructions[0])[0])
            for leave in instructions[1].split(","):
                leaves.add(leave.strip())

print("answer 1:", (roots - leaves).pop())
