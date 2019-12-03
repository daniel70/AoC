import collections as cl

lines = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    "U62,R66,U55,R34,D71,R55,D58,R83",  # distance 159
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",  # distance 135
    "R8,U5,L5,D3",
    "U7,R6,D4,L4",  # distance 6
]

lines = []
with open("input03.txt") as f:
    for line in f:
        lines.append(line)


def plot_path(plane, path, wire):
    x = 0
    y = 0

    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        if direction == "U":
            for i in range(1, steps + 1):
                plane[(x, y + i)].add(wire)
            y = y + steps
        if direction == "D":
            for i in range(1, steps + 1):
                plane[(x, y - i)].add(wire)
            y = y - steps
        if direction == "R":
            for i in range(1, steps + 1):
                plane[(x + i, y)].add(wire)
            x = x + steps
        if direction == "L":
            for i in range(1, steps + 1):
                plane[(x - i, y)].add(wire)
            x = x - steps

    return plane


paths = [line.split(",") for line in lines]
path_iterator = iter(paths)
for path in path_iterator:
    plane = cl.defaultdict(set)
    plane = plot_path(plane, path, 0)
    path = next(path_iterator)
    plane = plot_path(plane, path, 1)

    print(min([abs(c[0]) + abs(c[1]) for c, w in plane.items() if len(w) > 1]))
