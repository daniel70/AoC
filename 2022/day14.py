from itertools import pairwise
down, left, right = 0+1j, -1+1j, +1+1j


def make_blocked(lines):
    blocked = set()
    for line in lines:
        for start, end in pairwise(line.strip().split("->")):
            start = complex(*[int(p) for p in start.strip().split(",")])
            end = complex(*[int(p) for p in end.strip().split(",")])
            if start.imag == end.imag:
                for p in range(min(int(start.real), int(end.real)), max(int(start.real), int(end.real)) + 1):
                    blocked.add(complex(p, start.imag))
            elif start.real == end.real:
                for p in range(min(int(start.imag), int(end.imag)), max(int(start.imag), int(end.imag)) + 1):
                    blocked.add(complex(start.real, p))

    return blocked


def is_blocked(blocked: dict[complex, str], pos: complex, floor: bool = False) -> bool:
    global low
    if floor and pos.imag >= low + 2:
        return True
    return pos in blocked


def count_sand(blocked: dict[complex, str], floor: bool = False) -> int:
    global low
    grain = 500 + 0j
    steps = 0
    while True:
        if not floor and grain.imag > low:
            return steps

        if is_blocked(blocked, grain + down, floor):
            if is_blocked(blocked, grain + left, floor):
                if is_blocked(blocked, grain + right, floor):
                    steps += 1
                    if grain == 500+0j:
                        return steps

                    blocked[grain] = "o"
                    grain = 500+0j

                else:
                    grain = grain + right
            else:
                grain = grain + left
        else:
            grain = grain + down


blocked = make_blocked(open("input14.txt").readlines())
blocked = {p: "#" for p in blocked}
low = max(p.imag for p in blocked)

print("answer 1:", count_sand(blocked, floor=False))
blocked = {k: v for k, v in blocked.items() if v == "#"}
print("answer 2:", count_sand(blocked, floor=True))
