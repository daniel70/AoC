from collections import namedtuple

instructions = []
with open("input09.txt") as f:
    for line in f:
        line = line.strip()
        direction, steps = line.split()
        instructions.append((direction, int(steps)))

print(instructions)
pos = namedtuple("Pos", "x y")
H = pos(x=0, y=0)
T = pos(x=0, y=0)
seen = {pos(x=0, y=0)}
for direction, steps in instructions:
    for i in range(steps):
        print(f"{direction=}, {i=}")
        if direction == "U":
            H = pos(x=H.x, y=H.y + 1)
        elif direction == "R":
            H = pos(x=H.x + 1, y=H.y)
        elif direction == "D":
            H = pos(x=H.x, y=H.y - 1)
        elif direction == "L":
            H = pos(x=H.x - 1, y=H.y)
        else:
            raise NotImplementedError(f"unknown {direction}")

        # check if we need to move and where to
        if (abs(H.x - T.x) <= 1 and (H.y - T.y) == 0) or (abs(H.y - T.y) <= 1 and (H.x - T.x) == 0):
            continue
        if H.x == T.x:
            T = pos(x=H.x, y=((H.y + T.y) // 2))
        elif H.y == T.y:
            T = pos(x=((H.x + T.x) // 2), y=H.y)
        else:
            # if H is above then get under
            if H.y - T.y > 1:
                T = pos(H.x, H.y - 1)
            # if H is below then get above
            if H.y - T.y < -1:
                T = pos(H.x, H.y + 1)
            # if H is right
            if H.x - T.x > 1:
                T = pos(H.x - 1, H.y)
            # if H is left
            if H.x - T.x < -1:
                T = pos(H.x + 1, H.y)
        seen.add(T)

print(len(seen))