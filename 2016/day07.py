import re

lines = open("input07.txt").read().splitlines()
abba = re.compile(r"([a-z])(?!\1)([a-z])\2\1")
aba = re.compile(r"(?=(([a-z])(?!\2)[a-z]\2))")
outside = re.compile(r"(?:^|])(.+?)(?:\[|$)")
inside = re.compile(r"\[(.+?)]")


def is_tls(v7: str) -> bool:
    inners = inside.findall(v7)
    if any([bool(abba.search(s)) for s in inners]):
        return False
    outers = outside.findall(v7)
    if any([bool(abba.search(s)) for s in outers]):
        return True
    return False


def is_ssl(v7: str) -> bool:
    inners = inside.findall(v7)
    outers = outside.findall(v7)
    for outer in outers:
        abas = aba.findall(outer)
        for m in abas:
            # m holds a list of tuples with aba (match, first char)
            bab = m[0][1] + m[1] + m[0][1]
            if any([bab in inner for inner in inners]):
                return True
    return False


total1 = sum([is_tls(line) for line in lines])
total2 = sum([is_ssl(line) for line in lines])

print("answer 1:", total1)
print("answer 2:", total2)
