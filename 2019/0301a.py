"""
Advent of Code 2019, day 3, puzzle 1
this time with a list of tuples
"""
import collections as cl

# lines = ["R8,U5,L5,D3", "U7,R6,D4,L4"]  # distance 6
# lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]  # distance 159
# lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]  # distance 135

lines = []
with open("input03.txt") as f:
    for line in f:
        lines.append(line)


def plot_path(path):
    coords = []
    x, y = 0, 0
    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        if direction == "U":
            for i in range(1, steps + 1):
                coords.append((x, y + i))
            y = y + steps
        if direction == "D":
            for i in range(1, steps + 1):
                coords.append((x, y - i))
            y = y - steps
        if direction == "R":
            for i in range(1, steps + 1):
                coords.append((x + i, y))
            x = x + steps
        if direction == "L":
            for i in range(1, steps + 1):
                coords.append((x - i, y))
            x = x - steps
    return coords


paths = [line.split(",") for line in lines]
wires = []
for nr, path in enumerate(paths):
    wires.append(plot_path(path))

print(min([abs(x) + abs(y) for x, y in set(wires[0]) & set(wires[1])]))
