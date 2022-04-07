with open("input01.txt") as f:
    instructions = f.readline().strip()

print("answer 1:", instructions.count('(') - instructions.count(')'))

floor = 0
for idx, c in enumerate(instructions):
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1

    if floor == -1:
        break

print("answer 2:", idx+1)
