"""
Advent of Code 2019, day 4, puzzle 2
"""


def is_password(pw):
    prev = pw[0]
    double = False
    for this in pw[1:]:
        if int(this) < int(prev):
            return False
        if this == prev and not this * 3 in pw:
            double = True
        prev = this
    return double


cnt = 0
for nr in range(231832, 767346):
    if is_password(str(nr)):
        cnt += 1

print(cnt)
