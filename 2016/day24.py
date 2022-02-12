# the maze is 185x41 and has 8 points
import itertools
import math
from collections import defaultdict, namedtuple
from pprint import pprint

point = namedtuple("Point", "x y")

maze = []
mazed = {}
pois = {}
with open("input24.txt") as f:
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
                # pois[c] = point(char_nr, line_nr)

        maze.append(maze_line)


def print_maze(maze, points):
    print(f"{step=}")
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


distances = defaultdict(dict)

steps = set()
for poi, nr in pois.items():
    step = 0
    points = [poi]
    seen = set(points)
    while True:
        step += 1
        new_points = []
        for p in points:
            neighbours = get_neighbours(p)
            for neighbour in neighbours:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if neighbour in pois:
                        distances[nr][pois[neighbour]] = step
                    new_points.append(neighbour)
        points = new_points
        # print_maze(maze, points)

        if len(distances[nr]) == len(pois) - 1:
            break

pprint(distances)

routes = list(distances.keys())
routes.remove('0')
shortest = math.inf
for route in itertools.permutations(routes, len(routes)):
    start_from = '0'
    trip_total = 0
    for location in route:
        trip_total += distances[start_from][location]
        start_from = location
    shortest = min(shortest, trip_total)

print(shortest)
