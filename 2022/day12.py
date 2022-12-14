from string import ascii_lowercase as az
import sys

sys.setrecursionlimit(1500)
instructions: list[list[str]] = []
with open("input12.txt") as f:
    for row, line in enumerate(f):
        line = line.strip()
        if "S" in line:
            start = (line.index("S"), row)
            line = line.replace("S", "a")
        if "E" in line:
            goal = (line.index("E"), row)
            line = line.replace("E", "z")

        instructions.append([char for char in line])

width, height = len(line), len(instructions)
seen = {}
shortest = 999_999_999


def explore(start, steps):
    global seen
    global shortest
    if steps >= shortest:
        return

    if start == goal:
        shortest = min(shortest, steps)

    seen[start] = steps

    x, y = start
    char = instructions[y][x]
    # up
    if y > 0 and az.index(instructions[y-1][x]) <= az.index(char) + 1 \
            and ((x, y-1) not in seen or seen[(x, y-1)] > steps + 1):
        explore((x, y-1), steps + 1)

    # right
    if x < width - 1 and az.index(instructions[y][x+1]) <= az.index(char) + 1 \
            and ((x+1, y) not in seen or seen[(x+1, y)] > steps + 1):
        explore((x+1, y), steps + 1)

    # down
    if y < height - 1 and az.index(instructions[y+1][x]) <= az.index(char) + 1 \
            and ((x, y+1) not in seen or seen[(x, y+1)] > steps + 1):
        explore((x, y+1), steps + 1)

    # left
    if x > 0 and az.index(instructions[y][x-1]) <= az.index(char) + 1 \
            and ((x-1, y) not in seen or seen[(x-1, y)] > steps + 1):
        explore((x-1, y), steps + 1)


explore(start, 0)
print("answer 1:", shortest)
for a in [(x, y) for y, row in enumerate(instructions) for x, c in enumerate(row) if c == "a"]:
    explore(a, 0)
print("answer 2:", shortest)
