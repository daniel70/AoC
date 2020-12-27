import re
lines: list = []

with open("input05.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)


def part1(lines):
    re_twice = re.compile(r"([a-z])\1")
    nice: int = 0
    for line in lines:
        # rule 3
        nope = False
        for forbidden in ["ab", "cd", "pq", "xy"]:
            if forbidden in line:
                nope = True
        if nope:
            continue

        # rule 1
        vowels = 0
        for c in line:
            if c in "aeiou":
                vowels += 1

        if vowels < 3:
            continue

        # rule 2
        if re_twice.search(line):
            nice += 1

    return nice


def part2(lines):
    re_rule1 = re.compile(r"(\w)(\w).*\1\2")
    re_rule2 = re.compile(r"(\w)\w\1")
    nice = 0
    for line in lines:
        if re_rule1.search(line) is not None and re_rule2.search(line) is not None:
           nice += 1

    return nice

print(part1(lines))
print(part2(lines))
