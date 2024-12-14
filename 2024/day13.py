import re

nrs = re.compile(r'\d+')
input = [nrs.findall(line) for line in open('input13.txt').read().split('\n\n')]
answer1 = answer2 = 0

def wins(ax, ay, bx, by, x, y, part=1) -> tuple[int, int] | None:
    if part == 2:
        x += 10_000_000_000_000
        y += 10_000_000_000_000
    b = (x * ay - y * ax) / (bx * ay - by * ax)
    if b % 1 != 0:
        return
    a = (x - bx * b) / ax
    return int(a), int(b)

for part in [1, 2]:
    for machine in input:
        win = wins(*[int(i) for i in machine], part=part)
        if win:
            a, b = win
            answer1 += a * 3 + b if part == 1 else 0
            answer2 += a * 3 + b if part == 2 else 0

print("answer 1:", answer1)
print("answer 2:", answer2)
