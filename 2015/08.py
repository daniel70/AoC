import re

re_matchsticks = re.compile(r'\\(\\|\"|x[0-9a-f]{2})')
lines = []
total = 0
with open("input08.txt") as f:
    for line in f:
        line = line.strip()
        line = line[1:-1]
        total += len(line)
        lines.append(line)

answer1 = 0
answer2 = 0
for line in lines:
    answer1 += 2
    answer2 += 4
    m = re_matchsticks.findall(line)
    for i in m:
        answer1 += len(i)
        answer2 += 2 if len(i) == 1 else 1

print(answer1)
print(answer2)