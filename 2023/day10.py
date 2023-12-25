maze: list[list[str]] = []
with open("input10.txt") as file:
    for line in file:
        line = line.strip()
        maze.append(list(line))

directions = {
    "|": {"N", "S"},
    "-": {"E", "W"},
    "L": {"N", "E"},
    "J": {"N", "W"},
    "7": {"S", "W"},
    "F": {"S", "E"},
    ".": set(),
    # "S": "NESW",
}

# build a wall around the maze
for row in maze:
    row.insert(0, ".")
    row.append(".")

maze.insert(0, ["."] * len(maze[0]))
maze.append(["."] * len(maze[0]))

# find start
for nr, row in enumerate(maze):
    if "S" in row:
        S = (nr, row.index("S"))

seen = {
    S,
}
steps = 1
y, x = S

# fix Start
s_neighbours = set()
if maze[y - 1][x] in ["F", "|", "7"]:
    s_neighbours.add("N")
if maze[y + 1][x] in ["J", "|", "L"]:
    s_neighbours.add("S")
if maze[y][x + 1] in ["J", "-", "7"]:
    s_neighbours.add("E")
if maze[y][x - 1] in ["F", "-", "L"]:
    s_neighbours.add("W")

for k, v in directions.items():
    if v == s_neighbours:
        print("S is", k)
        maze[y][x] = k

positions = []
if "S" in directions[maze[y - 1][x]]:
    positions.append((y - 1, x, "S"))
    seen.add((y - 1, x))
if "W" in directions[maze[y][x + 1]]:
    positions.append((y, x + 1, "W"))
    seen.add((y, x + 1))
if "N" in directions[maze[y + 1][x]]:
    positions.append((y + 1, x, "N"))
    seen.add((y + 1, x))
if "E" in directions[maze[y][x - 1]]:
    positions.append((y, x - 1, "E"))
    seen.add((y, x - 1))

is_seen = False
while not is_seen:
    steps += 1
    new_positions = []
    for position in positions:
        y, x, _from = position
        direction_set = directions[maze[y][x]] - set(_from)
        if len(direction_set) == 0:
            continue
        direction = direction_set.pop()
        if direction == "N":
            y -= 1
            _from = "S"
        if direction == "E":
            x += 1
            _from = "W"
        if direction == "S":
            y += 1
            _from = "N"
        if direction == "W":
            x -= 1
            _from = "E"

        if (y, x) in seen:
            is_seen = True
            break

        seen.add((y, x))
        new_positions.append((y, x, _from))

    positions = new_positions

print(S)
print(steps)


# S and N = F|L and 7|J
# E and W = F-7 and L-J
# find all the outsiders, count what's left


def is_inside(point: tuple[int, int], seen, maze) -> bool:
    if point in seen:
        # print("seen")
        return False

    px, py = point
    pipes = {maze[x][y] for x, y in seen if x < px and y == py}  # north
    if not pipes - {"F", "|", "L"} or not pipes - {"7", "|", "J"}:
        # print("north")
        return False
    pipes = {maze[x][y] for x, y in seen if x > px and y == py}  # south
    if not pipes - {"F", "|", "L"} or not pipes - {"7", "|", "J"}:
        # print("south")
        return False
    pipes = {maze[x][y] for x, y in seen if x == px and y > py}  # east
    if not pipes - {"F", "-", "7"} or not pipes - {"L", "-", "J"}:
        # print("east")
        return False
    pipes = {maze[x][y] for x, y in seen if x == px and y < py}  # west
    if not pipes - {"F", "-", "7"} or not pipes - {"L", "-", "J"}:
        # print("west")
        return False

    return True


def has_outside_neighbour(point, seen, maze, outsides):
    if point in seen:
        return False
    if point in outsides:
        return False

    x, y = point
    if (
        (x + 1, y) in outsides
        or (x - 1, y) in outsides
        or (x, y + 1) in outsides
        or (x, y - 1) in outsides

        # or (x + 1, y + 1) in outsides
        # or (x + 1, y - 1) in outsides
        # or (x - 1, y + 1) in outsides
        # or (x - 1, y - 1) in outsides

    ):
        return True

    return False

def has_outside_in_line(point: tuple[int, int], seen, outsides, maze) -> bool:
    if point in seen:
        return False
    if point in outsides:
        return False

    px, py = point
    pipes = set()
    for x in range(px - 1, 0, -1):
        if (x, py) in seen:
            pipes.add(maze[x][py])
            if pipes - {"F", "|", "L"} and pipes - {"7", "|", "J"}:
                break
        if (x, py) in outsides:
            return True

    pipes = set()
    for x in range(px + 1, len(maze), 1):
        if (x, py) in seen:
            pipes.add(maze[x][py])
            if pipes - {"F", "|", "L"} and pipes - {"7", "|", "J"}:
                break
        if (x, py) in outsides:
            return True

    pipes = set()
    for y in range(py + 1, len(maze[0]), 1):
        if (px, y) in seen:
            pipes.add(maze[px][y])
            if pipes - {"F", "-", "7"} and pipes - {"L", "-", "J"}:
                break
        if (px, y) in outsides:
            return True

    pipes = set()
    for y in range(py - 1, 0, -1):
        if (px, y) in seen:
            pipes.add(maze[px][y])
            if pipes - {"F", "-", "7"} and pipes - {"L", "-", "J"}:
                break
        if (px, y) in outsides:
            return True

    return False


outsides = []
insides = []
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if (x, y) not in seen and is_inside((x, y), seen, maze) == False:
            outsides.append((x, y))


found = True
while found:
    found = False
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if has_outside_neighbour((x, y), seen, maze, outsides):
                outsides.append((x, y))
                found = True

# find outsides in straight lines
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if has_outside_in_line((x, y), seen, outsides, maze):
            print("found one")
            outsides.append((x, y))


found = True
while found:
    found = False
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if has_outside_neighbour((x, y), seen, maze, outsides):
                outsides.append((x, y))
                found = True



# find outsides in straight lines
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if has_outside_in_line((x, y), seen, outsides, maze):
            print("found one")
            outsides.append((x, y))


found = True
while found:
    found = False
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if has_outside_neighbour((x, y), seen, maze, outsides):
                outsides.append((x, y))
                found = True

# find outsides in straight lines
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if has_outside_in_line((x, y), seen, outsides, maze):
            print("found one")
            outsides.append((x, y))


found = True
while found:
    found = False
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if has_outside_neighbour((x, y), seen, maze, outsides):
                outsides.append((x, y))
                found = True

insides = []
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if (x, y) not in seen and (x, y) not in outsides:
            insides.append((x, y))

print(len(insides))

for x in range(len(maze)):
    for y in range(len(maze[0])):
        if (x, y) in outsides:
            print("O", end="")
        elif (x, y) in insides:
            print("I", end="")
        elif (x, y) in seen:
            print(maze[x][y], end="")
        else:
            print("?", end="")
    print("")

# 819 too high, 815 is incorrect, 811

