def captcha(nrs: str) -> int:
    total = 0
    previous_character = None
    for c in nrs:
        if c == previous_character:
            total += int(c)
        previous_character = c

    if nrs[0] == nrs[-1]:
        total += int(nrs[0])

    return total


def captcha2(nrs: str) -> int:
    total = 0
    for l, r in zip(nrs[:len(nrs)//2], nrs[len(nrs)//2:]):
        if l == r:
            total += int(l) * 2

    return total


instruction = open("input01.txt").readline().strip()
print("answer 1:", captcha(instruction))
print("answer 2:", captcha2(instruction))
