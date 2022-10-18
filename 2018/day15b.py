from itertools import count
from copy import deepcopy

lines = [line.strip() for line in open("test15.txt").readlines()]
units = {}
lmap = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in "EG":
            units[(x, y)] = (char, 300)
    lmap.append(list(line))


def print_map(units, list_map):
    for k, v in units.items():
        x, y = k
        gender, hp = v
        list_map[x][y] = gender

    for line in list_map:
        print("".join([str(c) for c in line]))


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
    assert list_map[x][y] in "GE"

    target: tuple[int, int] | None = None
    gender, hp = units[pos]
    enemy = "G" if gender == "E" else "E"
    previous_points = [pos,]
    for distance in count(1):
        next_points = []
        for x, y in previous_points:
            up = list_map[y - 1][x]
            left = list_map[y][x - 1]
            right = list_map[y][x + 1]
            down = list_map[y + 1][x]
            adjacent_points = [up, left, right, down]

            if enemy in [up, left, right, down]:
                target = x, y
                break
            if up == ".":
                list_map[y - 1][x] = distance
                next_points.append((x, y-1))
            if left == ".":
                list_map[y][x-1] = distance
                next_points.append((x-1, y))
            if right == ".":
                list_map[y][x+1] = distance
                next_points.append((x+1, y))
            if down == ".":
                list_map[y+1][x] = distance
                next_points.append((x, y+1))

        if not next_points or target is not None:
            break
        previous_points = next_points

    # now we need to find our way back in reading order
    if target is None:
        return None
    for distance in range(distance, 0, -1):
        x, y = target
        if list_map[y-1][x] == distance:
            target = (x, y-1)
        elif list_map[y][x-1] == distance:
            target = (x-1, y)
        elif list_map[y][x+1] == distance:
            target = (x+1, y)
        elif list_map[y+1][x] == distance:
            target = (x, y+1)

    return target

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
            new_pos = make_a_move(pos, units, deepcopy(lmap))
            if new_pos is not None:
                new_x, new_y = new_pos
                lmap[y][x] = "."
                lmap[new_y][new_x] = gender
                del units[pos]
                units[new_pos] = gender, hp

        enemy = find_adjacent_enemy(pos, enemies)
        if find_adjacent_enemy(pos, enemies):
            print(f"{pos} has an enemy adjacent at {enemy}")
            pass  # attack

print_map(units, lmap)