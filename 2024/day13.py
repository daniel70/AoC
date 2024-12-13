import itertools
import re
nrs = re.compile(r'\d+')
ax=94
ay=34
bx=22
by=67
x=X=8400
y=Y=5400

ax=26
ay=66
bx=67
by=21
x=X=12748
y=Y=12176

ax=17
ay=86
bx=84
by=37
x=X=7870
y=Y=6450

ax=69
ay=23
bx=27
by=71
x=X=18641
y=Y=10279



input = [nrs.findall(line) for line in open('test13.txt').read().split('\n\n')]

def wins(ax, ay, bx, by, x, y) -> list[tuple[int, int]]:
    ret = []
    round = 0
    while x >= 0 and y >= 0:
        if x % bx == 0 and y % by == 0 and x // bx == y // by:
            ret.append((round, x // bx))

        round += 1
        x -= ax
        y -= ay
    return ret

def big_wins(ax, ay, bx, by, x, y) -> list[tuple[int, int]]:
    x += 10_000_000_000_000
    y += 10_000_000_000_000
    ret = []
    round = 0
    while x >= 0 and y >= 0:
        if x % bx == 0 and y % by == 0 and x // bx == y // by:
            ret.append((round, x // bx))

        round += 1
        x -= ax
        y -= ay
    return ret

answer1 = 0
for machine in input:
    win = wins(*[int(i) for i in machine])
    big_win = big_wins(*[int(i) for i in machine])
    print(win)
    print(big_win)
    if win:
        a, b = win[0]
        answer1 += a * 3 + b
print(answer1)