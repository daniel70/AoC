lines = [line.strip() for line in open("input15.txt").readlines()]
units = {}
map_ = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in "EG":
            units[(x, y)] = (char, 300)
            line = line[:x] + "." + line[x+1:]
    map_.append(line)


def enemy_is_adjacent(pos, units: dict):
    gender, hp = units[pos]
    x, y = pos
    for other_pos, other_props in units.items():
        if pos == other_pos:
            continue  # myself
        other_gender, _ = other_props
        if gender == other_gender:
            continue  # friend
        other_x, other_y = other_pos
        if abs(x - other_x) == 1 and abs(y - other_y) == 1:  # a nearby enemy
            return True
    return False


for round in range(1, 2):
    # order the units
    sorted_units = sorted(units)
    sorted_units.sort(key=lambda pos: pos[1])
    for pos in sorted_units:
        unit = units[pos]
        if not enemy_is_adjacent(pos, units):
            pass  # make_a_move(pos, units, map_)
        if enemy_is_adjacent(pos, units):
            pass  # attack


