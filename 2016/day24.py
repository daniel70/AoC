# the maze is 185x41 and has 8 points
from collections import defaultdict, namedtuple

point = namedtuple("Point", "x y")

maze = []
mazed = {}
pois = {}
with open("test24.txt") as f:
    for line_nr, line in enumerate(f):
        line = line.strip()
        maze_line = []
        for char_nr, c in enumerate(line):
            if c == "#":
                maze_line.append(True)
                mazed[point(char_nr, line_nr)] = True
            else:
                maze_line.append(False)
                mazed[point(char_nr, line_nr)] = False
            if c.isdigit():
                pois[point(char_nr, line_nr)] = c

        maze.append(maze_line)


def print_maze(maze, points):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if point(x, y) in points:
                print("x", end="")
            elif point(x, y) in pois:
                print(pois[point(x, y)], end="")
            elif char:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def get_neighbours(neighbour: point) -> list:
    return [neighbour for neighbour in [
        point(p.x, p.y - 1),  # U
        point(p.x + 1, p.y),  # R
        point(p.x, p.y + 1),  # D
        point(p.x - 1, p.y),  # L
    ] if not mazed[neighbour]]


distances = defaultdict(list)
points = [point(1, 1)]
found = False
step = 0
steps = set()
seen = set(points[0])
while not found:
    step += 1
    new_points = []
    for p in points:
        neighbours = get_neighbours(p)
        for neighbour in neighbours:
            if neighbour not in seen:
                seen.add(neighbour)
                if neighbour in pois:
                    # found = True
                    distances[(1, 1)].append((pois[neighbour], step))
                new_points.append(neighbour)
    points = new_points

    print_maze(maze, points)
    print()
    if step == 8:
        break
