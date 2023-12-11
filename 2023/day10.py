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
# print(seen)

# even = outside, odd = inside
