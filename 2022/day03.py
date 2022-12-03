from string import ascii_letters

total = 0
instructions = []
with open('input03.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append(line)


for items in instructions:
    left, right = items[:len(items) // 2], items[len(items) // 2:]
    letter = set(left).intersection(set(right)).pop()
    total += ascii_letters.index(letter) + 1

print("answer 1:", total)

total = 0
for a, b, c in list(zip(*[iter(instructions)]*3)):
    letter = set(a).intersection(set(b)).intersection(set(c)).pop()
    total += ascii_letters.index(letter) + 1

print("answer 2:", total)
