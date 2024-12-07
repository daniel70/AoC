from collections import defaultdict
from itertools import cycle

maze = defaultdict(str) | {(x, y): s for y, line in enumerate(open("input06.txt").readlines())
                                     for x, s in enumerate(line.strip())}

pos = [k for k, v in maze.items() if v == '^']
x, y = pos[0]
maze[(x, y)] = '.'
char = '.'
direction = 'N'
seen = set()
seenl = []
seend = defaultdict(list)
obstructions = set()

def get_next_pos(direction, position) -> tuple:
    x, y = position
    if direction == 'N':
        return x, y - 1
    elif direction == 'E':
        return x + 1, y
    elif direction == 'S':
        return x, y + 1
    elif direction == 'W':
        return x - 1, y

def turn(direction):
    return 'NESW'[('NESW'.index(direction) + 1) % 4]

def is_loop(direction, position) -> bool:
    seen_this_loop = defaultdict(list)
    # first turn 90 degrees then start walking
    direction = turn(direction)
    x, y = position
    char = maze[(x, y)]
    while True:
        next_pos = get_next_pos(direction, (x, y))
        next_char = maze[next_pos]

        if next_char == '':
            return False

        if next_char == '#':
            direction = turn(direction)
            continue

        x, y = next_pos

        if direction in seend[(x, y)]:
            return True

        if direction in seen_this_loop[(x, y)]:
            print("loop closed")
            return True

        seen_this_loop[(x, y)].append(direction)


while True:
    next_pos = get_next_pos(direction, (x, y))
    next_char = maze[next_pos]

    if next_char == '':
        seen.add((x, y))
        break

    if next_char == '#':
        direction = turn(direction)
        continue

    if is_loop(direction, (x, y)):
        obstructions.add(next_pos)

    seen.add((x, y))
    seenl.append((x, y))
    seend[(x, y)].append(direction)
    x, y = next_pos


print(len(seen))
print(len(obstructions))

# 1678 is too low
# 1818 is too high



