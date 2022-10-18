lines = [line.strip() for line in open("test15.txt").readlines()]
units = {}
string_map = []
list_map = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in "EG":
            units[(x, y)] = (char, 300)
            line = line[:x] + "." + line[x+1:]
            char = "." # reset char ot make a clean dict_map
    string_map.append(line)
    list_map.append(list(line))


def print_map(units, list_map):
    for k, v in units.items():
        x, y = k
        gender, hp = v
        list_map[x][y] = gender

    for line in list_map:
        print("".join(line))


def find_adjacent_enemy(pos, enemies: list[tuple[int, int]]) -> tuple[int, int] | bool:
    x, y = pos
    for other_x, other_y in enemies:
        if abs(x - other_x) == 1 and y == other_y:  # a nearby enemy on the same line
            return other_x, other_y
        if x == other_x and abs(y - other_y) == 1:  # a nearby enemy above or below
            return other_x, other_y
    else:
        return False


def make_a_move(pos: tuple[int, int], units: dict, list_map: list) -> tuple[int, int] | None:
    x, y = pos
    for distance in count(1):
        pass


combat_end = False
for round in range(1, 2):
    if combat_end:
        print("The war is over")
        break
    # order the units
    sorted_units = sorted(units)
    sorted_units.sort(key=lambda pos: pos[1])
    for pos in sorted_units:
        x, y = pos
        gender, hp = units[pos]

        enemies: list[tuple[int, int]] = sorted([k for k, v in units.items() if v[0] != gender and k != pos])
        if not enemies:
            combat_end = True
        enemies.sort(key=lambda pos: pos[1])
        enemy = find_adjacent_enemy(pos, enemies)

        if not enemy:
            print(f"{pos} has no enemy adjacent")
            pass  # make_a_move(pos, units, map_)

        enemy = find_adjacent_enemy(pos, enemies)
        if find_adjacent_enemy(pos, enemies):
            print(f"{pos} has an enemy adjacent at {enemy}")
            pass  # attack
