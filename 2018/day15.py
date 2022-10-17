lines = [line.strip() for line in open("input15.txt").readlines()]
units = {}
map_ = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in "EG":
            units[(x, y)] = (char, 300)
            line = line[:x] + "." + line[x+1:]
    map_.append(line)


def find_adjacent_enemy(pos, enemies: list[tuple[int, int]]) -> tuple[int, int] | bool:
    x, y = pos
    for other_x, other_y in enemies:
        if abs(x - other_x) == 1 and y == other_y:  # a nearby enemy on the same line
            return other_x, other_y
        if x == other_x and abs(y - other_y) == 1:  # a nearby enemy above or below
            return other_x, other_y
    else:
        return False


def make_a_move(pos: tuple[int, int], units: dict, map_: list) -> tuple[int, int] | None:
    pass


for round in range(1, 2):
    # order the units
    sorted_units = sorted(units)
    sorted_units.sort(key=lambda pos: pos[1])
    for pos in sorted_units:
        x, y = pos
        gender, hp = units[pos]

        enemies: list[tuple[int, int]] = sorted([k for k, v in units.items() if v[0] != gender and k != pos])
        enemies.sort(key=lambda pos: pos[1])
        enemy = find_adjacent_enemy(pos, enemies)
        if not enemy:
            print(f"{pos} has no enemy adjacent")
            pass  # make_a_move(pos, units, map_)

        enemy = find_adjacent_enemy(pos, enemies)
        if find_adjacent_enemy(pos, enemies):
            print(f"{pos} has an enemy adjacent at {enemy}")
            pass  # attack


