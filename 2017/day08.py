from collections import defaultdict

reg = defaultdict(int)
highest = 0


def process(line: str) -> None:
    action, condition = line.split(" if ")
    tokens = condition.split()
    tokens[0] = f"reg['{tokens[0]}']"
    if eval(" ".join(tokens)):
        tokens = action.split()
        if tokens[1] == "inc":
            reg[tokens[0]] += int(tokens[2])
        else:
            reg[tokens[0]] -= int(tokens[2])


with open("input08.txt") as f:
    for line in f:
        line = line.strip()
        process(line)
        highest = max([highest, *reg.values()])

print("answer 1:", max(reg.values()))
print("answer 2:", highest)
