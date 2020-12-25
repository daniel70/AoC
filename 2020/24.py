black_tiles = set()
moves = {
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
    "ne": (1, 1),
}

lines = []
with open("input24.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

directions = moves.keys()
for line in lines:
    pos = (0, 0)
    while line:
        for direction in directions:
            if line.startswith(direction):
                line = line[len(direction):]
                x, y = pos
                dx, dy = moves[direction]
                pos = (x+dx, y+dy)

    if pos in black_tiles:
        black_tiles.remove(pos)
    else:
        black_tiles.add(pos)

print(len(black_tiles))

for day in range(1, 101):
    black_flips = set()
    white_flips = set()

    for bt in black_tiles:
        x, y = bt
        neighbours = [(x+2,y), (x+1, y-1), (x-1, y-1), (x-2, y), (x-1, y+1), (x+1, y+1)]
        # black rule
        black_rule_count = 0
        for neighbour in neighbours:
            if neighbour in black_tiles:
                black_rule_count += 1
        if black_rule_count == 0 or black_rule_count > 2:
            black_flips.add(bt)

        # white rule
        for neighbour in neighbours:
            if neighbour not in black_tiles:
                white_rule_count = 0
                x, y = neighbour
                neighneighbours = [(x + 2, y), (x + 1, y - 1), (x - 1, y - 1), (x - 2, y), (x - 1, y + 1), (x + 1, y + 1)]
                for neighneighbour in neighneighbours:
                    if neighneighbour in black_tiles:
                        white_rule_count += 1
                if white_rule_count == 2:
                    white_flips.add(neighbour)

    black_tiles = black_tiles.difference(black_flips)
    black_tiles = black_tiles.union(white_flips)

print(len(black_tiles))
