from itertools import cycle


def get_track_and_carts():
    carts = {}
    track = []
    replaced_track = []

    with open("input13.txt") as f:
        for line in f:
            line = line.rstrip()
            track.append(line)

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

        replaced_track.append(line)
    return replaced_track, carts


track, carts = get_track_and_carts()
first_crash = False
while len(carts) > 1:
    sorted_carts = sorted(carts)  # sort on y axis
    sorted_carts = sorted(sorted_carts, key=lambda p: p[1])  # sort on x axis
    for pos in sorted_carts:
        if pos not in carts:
            continue  # it was deleted due to a crash

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

        # crash detection
        if (x, y) in carts:
            if not first_crash:
                print(f"answer 1: {x},{y}")
                first_crash = True
            del carts[pos]     # remove me
            del carts[(x, y)]  # remove other

        else:
            # determine next direction based on the tracks char
            track_char = track[y][x]

            if direction == "R":
                if track_char == "/":
                    new_direction = "U"
                elif track_char == "\\":
                    new_direction = "D"
                elif track_char == "+":
                    turn = next(next_turn)
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
                    if turn == "L":
                        new_direction = "R"
                    elif turn == "S":
                        new_direction = "D"
                    elif turn == "R":
                        new_direction = "L"
                else:
                    new_direction = direction

            del carts[pos]  # remove the old cart
            carts[(x, y)] = (new_direction, next_turn)  # save the new cart

k, *ks = carts.keys()
print(f"answer 2: {k[0]},{k[1]}")
