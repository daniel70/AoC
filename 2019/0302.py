import collections as cl

lines = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    "U62,R66,U55,R34,D71,R55,D58,R83",  # steps 610
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",  # steps 410
    "R8,U5,L5,D3",
    "U7,R6,D4,L4",  # steps 30
]

lines = []
with open("input03.txt") as f:
    for line in f:
        lines.append(line)


def plot_path(plane, path, wire):
    x = 0
    y = 0
    step_count = 0
    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        if direction == "U":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x, y + i)]
                coord[wire] = True
                if f"steps{wire}" not in coord.keys():
                    coord[f"steps{wire}"] = step_count
            y = y + steps
        if direction == "D":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x, y - i)]
                coord[wire] = True
                if f"steps{wire}" not in coord.keys():
                    coord[f"steps{wire}"] = step_count
            y = y - steps
        if direction == "R":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x + i, y)]
                coord[wire] = True
                if f"steps{wire}" not in coord.keys():
                    coord[f"steps{wire}"] = step_count
            x = x + steps
        if direction == "L":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x - i, y)]
                coord[wire] = True
                if f"steps{wire}" not in coord.keys():
                    coord[f"steps{wire}"] = step_count
            x = x - steps

    return plane


paths = [line.split(",") for line in lines]
path_iterator = iter(paths)
for path in path_iterator:
    plane = cl.defaultdict(dict)
    plane = plot_path(plane, path, 0)
    path = next(path_iterator)
    plane = plot_path(plane, path, 1)

    print(
        min(
            [
                val["steps0"] + val["steps1"]
                for val in plane.values()
                if all(wire in val for wire in (0, 1))
            ]
        )
    )
