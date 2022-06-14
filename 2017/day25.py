import re
from collections import defaultdict

parser = re.compile(pattern=r"([A-Z]):.*?([0-9])\..*?(left|right).*?([A-Z])\..*?([0-9])\..*?(left|right).*?([A-Z])\.",
                    flags=re.MULTILINE | re.DOTALL)

states = {}
with open("input25.txt") as f:
    line1 = f.readline()
    start_state = line1[-3]
    line2 = f.readline()
    steps = int(re.search(r'\d+', line2).group())
    empty = f.readline()

    instructions = f.read()
    for match in parser.findall(instructions):
        states[match[0]] = [[int(match[1]), int(match[4])], [match[2], match[5]], [match[3], match[6]]]

tape = defaultdict(int)
cursor = 0


def runner(opts: list) -> str:
    global tape, cursor
    write, move, ret = opts
    current = tape[cursor]
    tape[cursor] = write[current]
    if move[current] == 'left':
        cursor -= 1
    elif move[current] == 'right':
        cursor += 1

    return ret[current]


state = states[start_state]
for _ in range(steps):
    state = states[runner(state)]

print("answer 1:", sum(tape.values()))
print("answer 2: The last star was gained by pressing a button.")
