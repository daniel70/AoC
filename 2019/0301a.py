"""
Advent of Code 2019, day 3, puzzle 1
this time with a list of tuples
"""
lines = []
with open("input03.txt") as f:
    lines = f.readlines()


def plot_path(path):
    coords = []
    x, y = 0, 0
    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        for i in range(1, steps + 1):
            if direction == "U":
                y += 1
            if direction == "D":
                y -= 1
            if direction == "R":
                x += 1
            if direction == "L":
                x -= 1

            coords.append((x, y))
    return coords


paths = [line.split(",") for line in lines]
wires = []
for nr, path in enumerate(paths):
    wires.append(plot_path(path))

print('answer puzzle 1:', min([abs(x) + abs(y) for x, y in set(wires[0]) & set(wires[1])]))
print('answer puzzle 2:', min([wires[0].index(s) + wires[1].index(s) for s in set(wires[0]) & set(wires[1])]))