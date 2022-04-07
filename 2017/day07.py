import re
from collections import defaultdict, Counter

re_first = re.compile(r"^(\w+) \((\d+)\)")
answer2 = None
roots = defaultdict(list)
leaves = set()
programs = {}
instructions = []
with open("input07.txt") as f:
    for line in f:
        line = line.strip()
        instructions = line.split(" -> ")
        program, weight = re_first.findall(instructions[0])[0]
        programs[program] = int(weight)
        if len(instructions) == 2:
            for leave in instructions[1].split(","):
                leaves.add(leave.strip())
                roots[program].append(leave.strip())

root = (set(roots.keys()) - leaves).pop()
print("answer 1:", root)


def check_weights(program):
    global answer2
    weight = programs[program]
    if program not in roots:
        return weight  # I am a simple leave
    else:
        weights = []
        for sub in roots[program]:
            weights.append(check_weights(sub))

        if len(set(weights)) != 1:
            if answer2 is None:
                counter = Counter(weights).most_common()
                diff = counter[1][0] - counter[0][0]
                faulty_program = roots[program][weights.index(counter[1][0])]
                answer2 = programs[faulty_program] - diff
        return sum(weights) + weight


check_weights(root)
print("answer 2:", answer2)
