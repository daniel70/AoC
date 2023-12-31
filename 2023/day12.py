import re
from collections import Counter

instructions: list[str, tuple[int, ...]] = []
qs = []
with open("input12.txt", "r") as file:
    for line in file:
        line = line.strip()
        left, right = line.split()
        left, right = left, right
        instructions.append([left, tuple([int(i) for i in right.split(",")])])


def arrangements(line: str):
    # count the number of question marks
    # loop 2 ** ?s times
    # replace 1 with # and 0 with . at the right place in the string
    # yield
    line: list = list(line)
    pos = [i for i, c in enumerate(line) if c == "?"]
    count = len(pos)
    for val in range(2**count):
        b_str = format(val, f"0{count}b")
        for idx, ipos in enumerate(pos):
            line[ipos] = "." if b_str[idx] == "0" else "#"
        yield "".join(line)


# 1, 1, 3
r"\.*#{1}\.+#{1}\.+#{3}\.*"
r = "\.+".join([rf"#{{{i}}}" for i in (1, 1, 3)])
r = "\.*" + r + "\.*"

count = 0
f = open("method1.txt", "w")
for line, groups in instructions:
    line = line
    groups = groups
    r = "\.+".join([rf"#{{{i}}}" for i in groups])
    r = "^\.*" + r + "\.*$"
    for arrangement in arrangements(line):
        if re.match(r, arrangement):
            count += 1
    f.write(f"{line}, {count}\n")
f.close()
print(count)



# 51356 is too high