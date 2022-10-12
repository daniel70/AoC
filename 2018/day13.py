# 72,22 is not correct
from itertools import cycle, count

track = []
with open("input13.txt") as f:
    for line in f:
        line = line.rstrip()
        track.append(line)

carts = {}


def get_carts():
    global track
    new_track = []
    cart_chars = {
        "<": ("-", "L"),
        ">": ("-", "R"),
        "^": ("|", "U"),
        "v": ("|", "D"),
    }
    for y, line in enumerate(track):
        for x, char in enumerate(line):
            if char in cart_chars:
                repl_char, direction = cart_chars[char]
                carts[(x,  y)] = (direction, cycle("LSR"))
                line = line[:x] + repl_char + line[x+1:]

        new_track.append(line)
    track = new_track


get_carts()

for tick in count(1):
    print(f"{tick=}")
    print("=" * 20)
    crashed = False
    sorted_carts = sorted(carts)
    for pos in sorted_carts:
        turn = ''
        new_direction = ''

        direction, next_turn = carts[pos]
        x, y = pos
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        elif direction == "U":
            y -= 1
        elif direction == "D":
            y += 1
        else:
            print("wrong direction")
            break

        # crash detection
        if (x, y) in carts:
            print(f"crash detected {x=}, {y=}, {tick=}")
            crashed = True
            break

        # determine next direction
        track_char = track[y][x]
        if direction == "R":
            if track_char == r"/":
                new_direction = "U"
            elif track_char == "\\":
                new_direction = "D"
            elif track_char == "+":
                turn = next(next_turn)
                print(f"{pos} going {turn}")
                if turn == "L":
                    new_direction = "U"
                elif turn == "S":
                    new_direction = "R"
                elif turn == "R":
                    new_direction = "D"
            else:
                new_direction = direction

        elif direction == "L":
            if track_char == "/":
                new_direction = "D"
            elif track_char == "\\":
                new_direction = "U"
            elif track_char == "+":
                turn = next(next_turn)
                print(f"{pos} going {turn}")
                if turn == "L":
                    new_direction = "D"
                elif turn == "S":
                    new_direction = "L"
                elif turn == "R":
                    new_direction = "U"
            else:
                new_direction = direction

        elif direction == "U":
            if track_char == "/":
                new_direction = "R"
            elif track_char == "\\":
                new_direction = "L"
            elif track_char == "+":
                turn = next(next_turn)
                print(f"{pos} going {turn}")
                if turn == "L":
                    new_direction = "L"
                elif turn == "S":
                    new_direction = "U"
                elif turn == "R":
                    new_direction = "R"
            else:
                new_direction = direction

        elif direction == "D":
            if track_char == "/":
                new_direction = "L"
            elif track_char == "\\":
                new_direction = "R"
            elif track_char == "+":
                turn = next(next_turn)
                print(f"{pos} going {turn}")
                if turn == "L":
                    new_direction = "R"
                elif turn == "S":
                    new_direction = "D"
                elif turn == "R":
                    new_direction = "L"
            else:
                new_direction = direction

        # save the new cart
        carts[(x, y)] = (new_direction, next_turn)
        del carts[pos]
        print(f"{pos=},{direction=},{track_char=},{turn=},{new_direction=}")

    if crashed:
        break

    if tick > 10_000:
        print("exhausted")
        break
