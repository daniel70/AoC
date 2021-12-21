import re
import math
from itertools import product

last_nr = re.compile(r"(\d+)\D*$")
first_nr = re.compile(r"(\d+)")
split_nr = re.compile(r"(\d{2,})")

lines = []
with open("input18.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)


def add(l: str, r: str):
    return f"[{l},{r}]"


def split(s: str):
    m = split_nr.search(s)
    if m:
        d = int(m[1])
        ss = "[" + str(d // 2) + "," + str(math.ceil(d / 2)) + "]"
        s = s[:m.start(1)] + ss + s[m.end(1):]

    return s


def explode(s: str):
    # find the 5th [ in the string
    brackets = 0
    for idx, c in enumerate(s):
        if c == "[":
            brackets += 1
        elif c == "]":
            brackets -= 1

        if brackets == 5:
            break
    if idx + 1 == len(s):
        return s

    pair = s[idx+1:s.index("]", idx)]
    l, r = pair.split(",")
    # replace right to left last digit, pair, first digit
    # first find the closing brackets index
    close_bracket = s.index("]", idx)

    m = first_nr.search(s, pos=close_bracket+1)
    if m:
        d = int(m[1]) + int(r)
        s = s[:m.start(1)] + str(d) + s[m.end(1):]

    s = s[:idx] + "0" + s[close_bracket+1:]

    # replace previous character
    m = last_nr.search(s, endpos=idx)
    if m:
        d = int(m[1]) + int(l)
        s = s[:m.start(1)] + str(d) + s[m.end(1):]

    return s


def ssum(lines: list):
    if not lines:
        return None
    total = lines[0]
    for line in lines[1:]:
        total = add(total, line)

        changed = True
        while changed:
            orig = total
            changed = False
            total = explode(total)
            if orig != total:
                changed = True
                continue
            total = split(total)
            if orig != total:
                changed = True

    return total


def magnitude(obj, total=0, level=1):
    mul = 4
    for item in obj:
        mul -= 1
        if isinstance(item, list):
            if len(item) == 2 and all([isinstance(i, int) for i in item]):
                val = (3 * item[0] * level * mul) + (2 * level * mul * item[1])
                total += val
            else:
                total = magnitude(item, total, level*mul)
        elif isinstance(item, int):
            val = level * item * mul
            total += val

    return total


print("answer 1:", magnitude(eval(ssum(lines))))

max_magnitude = 0
for line1, line2 in product(lines, repeat=2):
    m = magnitude(eval(ssum([line1, line2])))
    max_magnitude = max(max_magnitude, m)
print("answer 2:", max_magnitude)
