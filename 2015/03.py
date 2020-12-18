with open("input03.txt") as f:
    line = f.readline()


def walker(line, robot):
    visited = set([(0, 0)])
    santa = (0, 0)
    robo = (0, 0)
    line = line.strip()
    for idx, c in enumerate(line):
        if idx % 2 and robot:
            x, y = robo
        else:
            x, y = santa
        if c == ">":
            current = (x + 1, y)
        if c == "<":
            current = (x - 1, y)
        if c == "v":
            current = (x, y - 1)
        if c == "^":
            current = (x, y + 1)

        visited.add(current)
        if idx % 2 and robot:
            robo = current
        else:
            santa = current
    return visited

print(len(walker(line, robot=False)))
print(len(walker(line, robot=True)))

