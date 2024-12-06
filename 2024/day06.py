from collections import defaultdict
from itertools import cycle

maze = defaultdict(str) | {(x, y): s for y, line in enumerate(open("input06.txt").readlines())
                                     for x, s in enumerate(line.strip())}
pos = [k for k, v in maze.items() if v == '^']
directions = cycle(['N', 'E', 'S', 'W'])
x, y = pos[0]
maze[(x, y)] = '.'
char = '.'
direction = next(directions)
seen = {(x, y)}
seenl = [(x, y)]

while True:
    match direction:
        case 'N':
            next_pos = (x, y - 1)
        case 'E':
            next_pos = (x + 1, y)
        case 'S':
            next_pos = (x, y + 1)
        case 'W':
            next_pos = (x - 1, y)
    next_char = maze[next_pos]

    if next_char == '':
        seen.add((x, y))
        break

    if next_char == '#':
        direction = next(directions)
        continue

    seen.add((x, y))
    seenl.append((x, y))
    x, y = next_pos


print(len(seen))







