import itertools as it
from copy import deepcopy
from collections import defaultdict
from hashlib import md5


def adjacent_rooms(from_room):
    """
    Return adjacent rooms in the up, down, left, right order or None if there is no such room.
    """
    rooms = []
    if from_room <= 3:
        rooms.append(None)
    else:
        rooms.append(from_room - 4)

    if from_room >= 12:
        rooms.append(None)
    else:
        rooms.append(from_room + 4)

    if from_room % 4 == 0:
        rooms.append(None)
    else:
        rooms.append(from_room - 1)

    if from_room % 4 == 3:
        rooms.append(None)
    else:
        rooms.append(from_room + 1)

    return rooms


code = "ioramepc"
dirs = "UDLR"
access = "bcdef"
moves = defaultdict(list)
moves[0].append("")
first = ""
longest = 0


for count in it.count(1):
    if 15 in moves:
        if not first:
            first = moves[15][0]
        for move in moves[15]:
            longest = max(len(move), longest)
        moves[15].clear()  # the line ends here

    if all([len(path) == 0 for path in moves.values()]):
        break

    deep_moves = deepcopy(moves)
    moves = defaultdict(list)

    for room, paths in deep_moves.items():
        if not paths:
            continue
        for path in paths:
            hash_code = md5((code + path).encode("utf-8")).hexdigest()[:4]
            adjacent = adjacent_rooms(room)
            for i in range(4):
                if hash_code[i] in access and adjacent[i] is not None:
                    moves[adjacent[i]].append(path + dirs[i])


print("answer 1:", first)
print("answer 2:", longest)
