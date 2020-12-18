with open("input01.txt") as f:
    line = f.readline().strip()

print(line.count('(') - line.count(')'))
floor = 0
for idx, c in enumerate(line):
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1

    if floor == -1:
        break

print(idx+1)