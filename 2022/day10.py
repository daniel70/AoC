X = [1]
current = 1

with open("input10.txt") as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            X.append(current)
            continue
        op, val = line.split()
        if op == "addx":
            X.append(current)
            current += int(val)
            X.append(current)

total = 0
for x in [20, 60, 100, 140, 180, 220]:
    total += X[x-1] * x
print("answer 1:", total)

for cycle, pos in enumerate(X[:-1]):
    if pos - 1 <= cycle % 40 <= pos + 1:
        print("#", end="")
    else:
        print(" ", end="")
    if cycle % 40 == 39 and cycle:
        print("")