instructions = []
with open('input04.txt') as f:
    for line in f:
        line = line.strip()
        left, right = line.split(',')
        a, b = left.split('-')
        c, d = right.split('-')
        instructions.append((int(a), int(b), int(c), int(d)))

answer1 = answer2 = 0
for a, b, c, d in instructions:
    if (a <= c and b >= d) or (c <= a and d >= b):
        answer1 += 1

    if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
        answer2 += 1

print("answer 1:", answer1)
print("answer 2:", answer2)
