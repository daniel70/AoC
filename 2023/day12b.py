import re
from datetime import datetime as dt


total = 0
def matcher(s: str, groups: tuple, solution: str = ""):
    global total
    if not groups and not "#" in s:
        # print(solution + "." * len(s))
        total += 1
        return
    if not groups:
        return
    if groups and not s:
        return
    if sum(groups) + len(groups) - 1 > len(s):
        return
    
    match = re.match(f"^([\?#]{{{groups[0]}}})([^#]|$)", s)
    if match:
        matcher(s[match.end():], groups[1:], solution + "#" * (match.end() - match.start() - 1) + ".")

    if not s.startswith("#"):
        matcher(s[1:], groups, solution + ".")

    return total


instructions: list[str, tuple[int, ...]] = []
with open("input12.txt") as file:
    for line in file:
        line = line.strip()
        left, right = line.split()
        instructions.append([left, tuple([int(i) for i in right.split(",")])])


for line, groups in instructions:
    start = dt.now()
    begin = total
    print(f"{line}, {groups}", end="")
    matcher("?".join([line] * 5), groups * 5)
    print(f": {total - begin} ({(dt.now() - start).seconds})")


print(total)