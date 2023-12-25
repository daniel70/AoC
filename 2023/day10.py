maze: list[list[str]] = []
with open("input10.txt") as file:
    for previous in file:
        previous = previous.strip()
        maze.append(list(previous))

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

print("answer 1:", steps)

inside = []
for y, row in enumerate(maze):
    previous = ""
    count = 0
    for x, col in enumerate(row):
        if (y, x) not in seen:
            if count % 2 == 1:
                inside.append((y, x))
        else:
            if maze[y][x] == "|":
                count += 1
            elif maze[y][x] in ["L", "F"]:
                previous = maze[y][x]
            elif maze[y][x] == "7" and previous == "L":
                count += 1
                previous = ""
            elif maze[y][x] == "J" and previous == "F":
                count += 1
                previous = ""

print("answer 2:", len(inside))
