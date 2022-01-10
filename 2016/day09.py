import re

marker = re.compile(r"\((\d+)x(\d+)\)")


def decompress(line: str, multiplier=1, once=True) -> int:
    total = 0
    m = marker.search(line)
    if not m:
        return len(line) * multiplier
    else:
        total += m.start() * multiplier
        line = line[m.end():]
        if once:
            total += int(m[1]) * int(m[2])
        else:
            total += decompress(line[:int(m[1])], multiplier * int(m[2]), once)
        total += decompress(line[int(m[1]):], multiplier, once)

    return total


line = open("input09.txt").read().strip()
print("answer 1:", decompress(line, once=True))
print("answer 1:", decompress(line, once=False))
